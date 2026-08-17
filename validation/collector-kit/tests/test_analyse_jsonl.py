from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
FIXTURES = HERE / "fixtures"
MODULE_PATH = HERE.parent / "analyse_jsonl.py"

spec = importlib.util.spec_from_file_location("analyse_jsonl", MODULE_PATH)
module = importlib.util.module_from_spec(spec)
assert spec.loader is not None
sys.modules[spec.name] = module
spec.loader.exec_module(module)


def analyze_fixture(name: str, **overrides):
    events = module.read_jsonl(FIXTURES / name)
    params = dict(
        run_id="T",
        scenario_id="T",
        condition="skill",
        skill_expected="yes",
        skill_name="example-skill",
    )
    params.update(overrides)
    return module.analyze(events, **params)


class TestAnalyseJsonl(unittest.TestCase):
    def test_t01_read_valid_jsonl_preserves_order(self):
        events = module.read_jsonl(FIXTURES / "usage_duplique.jsonl")
        self.assertEqual([e.line_no for e in events], [1, 2])
        self.assertEqual(events[0].data["requestId"], "req_1")

    def test_t02_invalid_json_reports_line_and_exit_3(self):
        proc = subprocess.run(
            [
                sys.executable,
                str(MODULE_PATH),
                str(FIXTURES / "malformed.jsonl"),
                "--run-id", "T02",
                "--scenario-id", "T02",
                "--condition", "skill",
                "--skill-expected", "yes",
                "--skill-name", "example-skill",
            ],
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(proc.returncode, module.EXIT_INVALID_JSONL)
        self.assertIn("ligne 2", proc.stderr)

    def test_t03_single_model_usage(self):
        result, code = analyze_fixture("sans_observabilite_skill.jsonl")
        self.assertEqual(code, 0)
        self.assertEqual(result.model_calls, 1)
        self.assertEqual(result.input_tokens, 2)
        self.assertEqual(result.output_tokens, 3)

    def test_t04_identical_usage_duplicate_is_counted_once(self):
        result, code = analyze_fixture("usage_duplique.jsonl")
        self.assertEqual(code, 0)
        self.assertEqual(result.model_calls, 1)
        self.assertEqual(result.input_tokens, 3)
        self.assertEqual(result.cache_creation_input_tokens, 10)
        self.assertEqual(result.cache_read_input_tokens, 20)
        self.assertEqual(result.output_tokens, 5)

    def test_t05_progressive_output_uses_max_observed(self):
        result, code = analyze_fixture("usage_progressif.jsonl")
        self.assertEqual(code, 0)
        self.assertEqual(result.model_calls, 1)
        self.assertEqual(result.output_tokens, 310)
        self.assertTrue(any("max_observed_progressive_update" in n for n in result.observability_notes))

    def test_t06_conflicting_invariants_exit_4(self):
        result, code = analyze_fixture("usage_conflit.jsonl")
        self.assertEqual(code, module.EXIT_UNRELIABLE)
        self.assertTrue(any(n.startswith("model_usage:conflict:") for n in result.observability_notes))

    def test_t07_multiple_model_calls_sum_by_request(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.jsonl"
            lines = [
                {"type":"assistant","requestId":"r1","message":{"usage":{"input_tokens":1,"cache_creation_input_tokens":2,"cache_read_input_tokens":3,"output_tokens":4}}},
                {"type":"assistant","requestId":"r2","message":{"usage":{"input_tokens":5,"cache_creation_input_tokens":6,"cache_read_input_tokens":7,"output_tokens":8}}},
            ]
            p.write_text("\n".join(json.dumps(x) for x in lines)+"\n", encoding="utf-8")
            events = module.read_jsonl(p)
            result, code = module.analyze(events, run_id="x", scenario_id="x", condition="skill", skill_expected="yes", skill_name="example-skill")
            self.assertEqual(code, 0)
            self.assertEqual(result.model_calls, 2)
            self.assertEqual((result.input_tokens, result.cache_creation_input_tokens, result.cache_read_input_tokens, result.output_tokens), (6,8,10,12))

    def test_t08_cache_categories_stay_separate(self):
        result, _ = analyze_fixture("usage_duplique.jsonl")
        self.assertEqual(result.input_tokens, 3)
        self.assertEqual(result.cache_creation_input_tokens, 10)
        self.assertEqual(result.cache_read_input_tokens, 20)

    def test_t09_thinking_absent_is_not_observable(self):
        result, _ = analyze_fixture("usage_duplique.jsonl")
        self.assertEqual(result.thinking_tokens, 0)
        self.assertIn("thinking_tokens:not_observable", result.observability_notes)

    def test_t10_tools_are_deduplicated_and_order_preserved(self):
        result, _ = analyze_fixture("outils_skill.jsonl")
        self.assertEqual(result.tool_calls, 3)
        self.assertEqual(result.tool_names, ["Skill", "Read", "Read"])

    def test_t11_read_write_edit_classification(self):
        result, _ = analyze_fixture("fichiers.jsonl")
        self.assertEqual(result.file_writes, 1)
        self.assertEqual(result.file_edits, 1)
        self.assertEqual(result.tool_calls, 4)

    def test_t12_skill_explicitly_listed_true(self):
        result, _ = analyze_fixture("outils_skill.jsonl")
        self.assertEqual(result.skill_listed, "true")

    def test_t13_complete_skill_listing_without_target_false(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.jsonl"
            p.write_text(json.dumps({"type":"skill_listing","skills":[{"name":"other"}]})+"\n", encoding="utf-8")
            events = module.read_jsonl(p)
            result, _ = module.analyze(events, run_id="x", scenario_id="x", condition="skill", skill_expected="yes", skill_name="example-skill")
            self.assertEqual(result.skill_listed, "false")

    def test_t14_skill_listing_not_observable(self):
        result, _ = analyze_fixture("sans_observabilite_skill.jsonl")
        self.assertEqual(result.skill_listed, "not_observable")

    def test_t15_skill_invocation_explicit_tool_use(self):
        result, _ = analyze_fixture("outils_skill.jsonl")
        self.assertEqual(result.skill_invoked, "true")

    def test_t16_skill_reference_read_is_explicit_and_relative(self):
        result, _ = analyze_fixture("outils_skill.jsonl")
        self.assertEqual(result.skill_reference_reads, 1)
        self.assertEqual(result.skill_reference_names, ["opo.md"])

    def test_t17_memory_search_is_only_explicit_tool(self):
        result, _ = analyze_fixture("fichiers.jsonl")
        self.assertEqual(result.memory_searches, 1)

    def test_t18_deterministic_compact_json(self):
        events = module.read_jsonl(FIXTURES / "outils_skill.jsonl")
        result1, _ = module.analyze(events, run_id="x", scenario_id="x", condition="skill", skill_expected="yes", skill_name="example-skill")
        result2, _ = module.analyze(events, run_id="x", scenario_id="x", condition="skill", skill_expected="yes", skill_name="example-skill")
        j1 = json.dumps(result1.to_dict(), ensure_ascii=False, separators=(",", ":"))
        j2 = json.dumps(result2.to_dict(), ensure_ascii=False, separators=(",", ":"))
        self.assertEqual(j1, j2)

    def test_cli_writes_output_file(self):
        with tempfile.TemporaryDirectory() as td:
            out = Path(td) / "metrics.json"
            proc = subprocess.run(
                [
                    sys.executable,
                    str(MODULE_PATH),
                    str(FIXTURES / "outils_skill.jsonl"),
                    "--run-id", "CLI",
                    "--scenario-id", "CLI",
                    "--condition", "skill",
                    "--skill-expected", "yes",
                    "--skill-name", "example-skill",
                    "--output", str(out),
                    "--pretty",
                ],
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            payload = json.loads(out.read_text(encoding="utf-8"))
            self.assertEqual(payload["run_id"], "CLI")
            self.assertEqual(payload["skill_invoked"], "true")

    def test_nested_output_tokens_details_thinking(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "nested.jsonl"
            p.write_text(
                json.dumps({
                    "type": "assistant",
                    "requestId": "nested-1",
                    "message": {
                        "role": "assistant",
                        "id": "msg-nested",
                        "content": [{"type": "text", "text": "ok"}],
                        "usage": {
                            "input_tokens": 1,
                            "cache_creation_input_tokens": 2,
                            "cache_read_input_tokens": 3,
                            "output_tokens": 4,
                            "output_tokens_details": {"thinking_tokens": 7}
                        }
                    }
                }) + "\n",
                encoding="utf-8",
            )
            events = module.read_jsonl(p)
            result, code = module.analyze(
                events,
                run_id="nested",
                scenario_id="nested",
                condition="skill",
                skill_expected="yes",
                skill_name="example-skill",
            )
            self.assertEqual(code, 0)
            self.assertEqual(result.thinking_tokens, 7)
            self.assertNotIn("thinking_tokens:not_observable", result.observability_notes)


if __name__ == "__main__":
    unittest.main()
