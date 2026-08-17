from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import unittest
import uuid
from pathlib import Path
from types import SimpleNamespace

HERE = Path(__file__).resolve().parent
COLLECTOR_PATH = HERE.parent / "collect_run.py"
PARSER_PATH = HERE.parent / "analyse_jsonl.py"
FIXTURES = HERE / "fixtures"


def load(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


collector = load("collector_interactions", COLLECTOR_PATH)
parser = load("parser_interactions", PARSER_PATH)


def user(prompt: str, session: str, cwd: str, *, origin=True, prompt_id="p1"):
    e = {
        "type": "user",
        "promptId": prompt_id,
        "message": {"role": "user", "content": [{"type": "text", "text": prompt}]},
        "cwd": cwd,
        "sessionId": session,
        "timestamp": "2026-08-13T18:00:00.000Z",
    }
    if origin:
        e["origin"] = {"kind": "human"}
    return e


def assistant_text(text: str, session: str, cwd: str, request="r1", msg="m1"):
    return {
        "type": "assistant",
        "requestId": request,
        "message": {
            "role": "assistant",
            "id": msg,
            "content": [{"type": "text", "text": text}],
            "usage": {
                "input_tokens": 1,
                "cache_creation_input_tokens": 2,
                "cache_read_input_tokens": 3,
                "output_tokens": 4,
                "output_tokens_details": {"thinking_tokens": 1},
            },
        },
        "cwd": cwd,
        "sessionId": session,
        "timestamp": "2026-08-13T18:00:01.000Z",
    }


def assistant_tool(name: str, tool_id: str, tool_input, session: str, cwd: str, request="rt"):
    return {
        "type": "assistant",
        "requestId": request,
        "message": {
            "role": "assistant",
            "id": request,
            "content": [{"type": "tool_use", "id": tool_id, "name": name, "input": tool_input}],
            "usage": {
                "input_tokens": 1,
                "cache_creation_input_tokens": 2,
                "cache_read_input_tokens": 3,
                "output_tokens": 4,
            },
        },
        "cwd": cwd,
        "sessionId": session,
        "timestamp": "2026-08-13T18:00:02.000Z",
    }


def ask_result(tool_id: str, answers, questions, session: str, cwd: str):
    return {
        "type": "user",
        "promptId": "p1",
        "message": {
            "role": "user",
            "content": [{
                "type": "tool_result",
                "tool_use_id": tool_id,
                "content": "User has answered your questions.",
            }],
        },
        "toolUseResult": {"questions": questions, "answers": answers},
        "sourceToolAssistantUUID": "assistant-tool",
        "cwd": cwd,
        "sessionId": session,
        "timestamp": "2026-08-13T18:00:03.000Z",
    }


def write_events(path: Path, events):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in events) + "\n", encoding="utf-8")


class TestParserInteractions(unittest.TestCase):
    def analyze(self, events):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.jsonl"
            write_events(p, events)
            records = parser.read_jsonl(p)
            return parser.analyze(
                records,
                run_id="I",
                scenario_id="I",
                condition="skill",
                skill_expected="yes",
                skill_name="example-skill",
            )

    def test_i01_file_reads_is_explicit(self):
        s = str(uuid.uuid4())
        events = [assistant_tool("Read", "tool-read", {"file_path": "/tmp/a.md"}, s, "/tmp")]
        result, code = self.analyze(events)
        self.assertEqual(code, 0)
        self.assertEqual(result.file_reads, 1)

    def test_i02_ask_user_question_call_and_answered_result(self):
        s = str(uuid.uuid4())
        q = [{"question": "6 ou 8 ?", "header": "Effectif", "options": [{"label": "6"}, {"label": "8"}]}]
        events = [
            assistant_tool("AskUserQuestion", "tool-ask", {"questions": q}, s, "/tmp"),
            ask_result("tool-ask", {"6 ou 8 ?": "8"}, q, s, "/tmp"),
        ]
        result, code = self.analyze(events)
        self.assertEqual(code, 0)
        self.assertEqual(result.ask_user_question_calls, 1)
        self.assertEqual(result.ask_user_question_results, 1)
        self.assertEqual(result.ask_user_question_answered_results, 1)

    def test_i03_ask_user_question_empty_answers_is_not_answered(self):
        s = str(uuid.uuid4())
        q = [{"question": "Choix ?", "options": []}]
        events = [
            assistant_tool("AskUserQuestion", "tool-ask", {"questions": q}, s, "/tmp"),
            ask_result("tool-ask", {}, q, s, "/tmp"),
        ]
        result, _ = self.analyze(events)
        self.assertEqual(result.ask_user_question_results, 1)
        self.assertEqual(result.ask_user_question_answered_results, 0)

    def test_i04_generic_tool_result_is_not_ask_result(self):
        s = str(uuid.uuid4())
        e = ask_result("tool-read", {"x": "y"}, [], s, "/tmp")
        events = [assistant_tool("Read", "tool-read", {"file_path": "/tmp/a"}, s, "/tmp"), e]
        result, _ = self.analyze(events)
        self.assertEqual(result.ask_user_question_calls, 0)
        self.assertEqual(result.ask_user_question_results, 0)

    def test_i04b_multiple_unlinked_ask_results_are_not_attributed(self):
        s = str(uuid.uuid4())
        q = [{"question": "Choix ?", "options": []}]
        e = ask_result("unknown", {"Choix ?": "A"}, q, s, "/tmp")
        # Retirer l'identifiant exploitable pour forcer le repli ambigu.
        e["message"]["content"][0]["tool_use_id"] = "unknown"
        events = [
            assistant_tool("AskUserQuestion", "ask1", {"questions": q}, s, "/tmp", "r1"),
            assistant_tool("AskUserQuestion", "ask2", {"questions": q}, s, "/tmp", "r2"),
            e,
        ]
        result, _ = self.analyze(events)
        self.assertEqual(result.ask_user_question_calls, 2)
        self.assertEqual(result.ask_user_question_results, 0)
        self.assertTrue(any("ambiguous_unlinked_result" in n for n in result.observability_notes))

    def test_i04c_realshape_fixture_answered(self):
        records = parser.read_jsonl(FIXTURES / "ask_user_question_answered.jsonl")
        result, code = parser.analyze(
            records, run_id="F1", scenario_id="F1", condition="skill",
            skill_expected="yes", skill_name="example-skill",
        )
        self.assertEqual(code, 0)
        self.assertEqual((result.ask_user_question_calls, result.ask_user_question_results, result.ask_user_question_answered_results), (1, 1, 1))

    def test_i04d_realshape_fixture_empty(self):
        records = parser.read_jsonl(FIXTURES / "ask_user_question_empty.jsonl")
        result, code = parser.analyze(
            records, run_id="F2", scenario_id="F2", condition="skill",
            skill_expected="yes", skill_name="example-skill",
        )
        self.assertEqual(code, 0)
        self.assertEqual((result.ask_user_question_calls, result.ask_user_question_results, result.ask_user_question_answered_results), (1, 1, 0))


class TestTrajectory(unittest.TestCase):
    def setUp(self):
        self.s = str(uuid.uuid4())
        self.cwd = "/tmp/work"
        self.prompt = "Conçois quelque chose."
        self.q = [{"question": "6 ou 8 ?", "header": "Effectif", "options": [{"label": "6"}, {"label": "8"}]}]

    def build(self, events):
        idx = collector.find_initial_prompt_index(events, self.prompt)
        return collector.build_trajectory(events, idx)

    def test_i05_multiturn_trajectory_keeps_all_visible_turns(self):
        events = [
            user(self.prompt, self.s, self.cwd),
            assistant_text("Je peux déjà avancer.", self.s, self.cwd, "r1", "m1"),
            user("Prends 8.", self.s, self.cwd, prompt_id="p2"),
            assistant_text("D'accord, voici la suite.", self.s, self.cwd, "r2", "m2"),
        ]
        md = collector.render_trajectory_markdown(self.build(events))
        self.assertIn("## USER\n\nConçois quelque chose.", md)
        self.assertIn("## ASSISTANT\n\nJe peux déjà avancer.", md)
        self.assertIn("## USER\n\nPrends 8.", md)
        self.assertIn("D'accord, voici la suite.", md)

    def test_i06_ask_user_question_keeps_before_answer_after(self):
        events = [
            user(self.prompt, self.s, self.cwd),
            assistant_text("Avant la question.", self.s, self.cwd, "r1", "m1"),
            assistant_tool("AskUserQuestion", "ask1", {"questions": self.q}, self.s, self.cwd, "r2"),
            ask_result("ask1", {"6 ou 8 ?": "8"}, self.q, self.s, self.cwd),
            assistant_text("Après la réponse.", self.s, self.cwd, "r3", "m3"),
        ]
        items = self.build(events)
        md = collector.render_trajectory_markdown(items)
        response = collector.render_response_raw(items)
        self.assertIn("Avant la question.", md)
        self.assertIn("## TOOL AskUserQuestion", md)
        self.assertIn("6 ou 8 ?", md)
        self.assertIn("## USER VIA AskUserQuestion", md)
        self.assertIn("6 ou 8 ?: 8", md)
        self.assertIn("Après la réponse.", md)
        self.assertEqual(response, "Avant la question.\n\nAprès la réponse.")

    def test_i07_read_projects_path_but_not_tool_result_content(self):
        read = assistant_tool("Read", "read1", {"file_path": "/tmp/secret.md"}, self.s, self.cwd, "r2")
        tool_result = {
            "type": "user",
            "message": {"role": "user", "content": [{"type": "tool_result", "tool_use_id": "read1", "content": "CONTENU TRES LONG SECRET"}]},
            "toolUseResult": {"content": "CONTENU TRES LONG SECRET"},
            "sourceToolAssistantUUID": "x",
            "sessionId": self.s,
            "cwd": self.cwd,
        }
        events = [user(self.prompt, self.s, self.cwd), read, tool_result, assistant_text("OK", self.s, self.cwd, "r3", "m3")]
        md = collector.render_trajectory_markdown(self.build(events))
        self.assertIn("## TOOL Read", md)
        self.assertIn("/tmp/secret.md", md)
        self.assertNotIn("CONTENU TRES LONG SECRET", md)

    def test_i08_meta_injection_is_excluded(self):
        meta = {
            "type": "user",
            "isMeta": True,
            "message": {"role": "user", "content": [{"type": "text", "text": "INJECTION SKILL"}]},
            "sessionId": self.s,
            "cwd": self.cwd,
        }
        events = [user(self.prompt, self.s, self.cwd), meta, assistant_text("Visible", self.s, self.cwd)]
        md = collector.render_trajectory_markdown(self.build(events))
        self.assertNotIn("INJECTION SKILL", md)


    def test_i08b_tool_result_is_not_human_even_if_origin_says_human(self):
        event = {
            "type": "user",
            "origin": {"kind": "human"},
            "promptId": "p1",
            "toolUseResult": {"answers": {"Q": "A"}},
            "message": {"role": "user", "content": [{"type": "text", "text": "TECH"}]},
        }
        self.assertFalse(collector.is_human_user_event(event))

    def test_i09_progressive_assistant_text_is_not_duplicated(self):
        a = assistant_text("Bon", self.s, self.cwd, "same", "same-msg")
        b = assistant_text("Bonjour", self.s, self.cwd, "same", "same-msg")
        events = [user(self.prompt, self.s, self.cwd), a, b]
        md = collector.render_trajectory_markdown(self.build(events))
        self.assertIn("Bonjour", md)
        self.assertNotIn("\n\nBon\n", md)
        self.assertEqual(md.count("## ASSISTANT"), 1)


class TestCollectorInteractiveIntegration(unittest.TestCase):
    def test_i10_collect_writes_trajectory_metadata_and_hashes(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            claude = root / "claude"
            runs = root / "runs"
            work = root / "work"
            work.mkdir()
            prompt_text = "Conçois."
            prompt_file = root / "prompt.txt"
            prompt_file.write_text(prompt_text, encoding="utf-8")

            start_args = SimpleNamespace(
                run_id="IRUN", scenario_id="IRUN", condition="skill",
                skill_expected="yes", prompt_file=str(prompt_file),
                claude_root=str(claude), cwd=str(work), output_root=str(runs),
                skill_name="example-skill",
            )
            self.assertEqual(collector.cmd_start(start_args), 0)

            session = str(uuid.uuid4())
            q = [{"question": "Effectif ?", "options": [{"label": "8"}]}]
            events = [
                user(prompt_text, session, str(work)),
                assistant_text("Je commence.", session, str(work), "r1", "m1"),
                assistant_tool("Read", "read1", {"file_path": "/tmp/ref.md"}, session, str(work), "r2"),
                assistant_tool("AskUserQuestion", "ask1", {"questions": q}, session, str(work), "r3"),
                ask_result("ask1", {"Effectif ?": "8"}, q, session, str(work)),
                assistant_text("Je termine.", session, str(work), "r4", "m4"),
            ]
            source = claude / "project" / f"{session}.jsonl"
            write_events(source, events)

            collect_args = SimpleNamespace(
                run_id="IRUN", output_root=str(runs), session_id=None,
                parser=str(PARSER_PATH),
            )
            self.assertEqual(collector.cmd_collect(collect_args), 0)
            dest = runs / "IRUN"
            self.assertEqual(
                sorted(p.name for p in dest.iterdir()),
                ["metadata.json", "metrics.json", "prompt.txt", "response_raw.md", "sha256.txt", "trace.jsonl", "trajectory.md"],
            )
            md = (dest / "trajectory.md").read_text(encoding="utf-8")
            self.assertIn("Je commence.", md)
            self.assertIn("## TOOL Read", md)
            self.assertIn("## TOOL AskUserQuestion", md)
            self.assertIn("## USER VIA AskUserQuestion", md)
            self.assertIn("Je termine.", md)
            metrics = json.loads((dest / "metrics.json").read_text(encoding="utf-8"))
            self.assertEqual(metrics["file_reads"], 1)
            self.assertEqual(metrics["ask_user_question_calls"], 1)
            self.assertEqual(metrics["ask_user_question_results"], 1)
            self.assertEqual(metrics["ask_user_question_answered_results"], 1)
            meta = json.loads((dest / "metadata.json").read_text(encoding="utf-8"))
            self.assertEqual(meta["human_turns"], 1)
            self.assertEqual(meta["collector_version"], collector.COLLECTOR_VERSION)
            self.assertEqual(meta["trajectory_sha256"], collector.sha256_file(dest / "trajectory.md"))
            manifest = (dest / "sha256.txt").read_text(encoding="utf-8")
            self.assertIn("trajectory.md", manifest)


if __name__ == "__main__":
    unittest.main(verbosity=2)
