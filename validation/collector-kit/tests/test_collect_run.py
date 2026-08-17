from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import unittest
import uuid
from types import SimpleNamespace
from pathlib import Path

HERE = Path(__file__).resolve().parent
COLLECTOR_PATH = HERE.parent / "collect_run.py"
PARSER_PATH = HERE.parent / "analyse_jsonl.py"


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


collector = load_module("collect_run_testmod", COLLECTOR_PATH)
parsermod = load_module("analyse_jsonl_r2_testmod", PARSER_PATH)


def event_user(prompt: str, session: str, cwd: str, ts: str = "2026-08-13T10:00:00.000Z"):
    return {
        "type": "user",
        "promptId": str(uuid.uuid4()),
        "origin": {"kind": "human"},
        "message": {"role": "user", "content": [{"type": "text", "text": prompt}]},
        "cwd": cwd,
        "sessionId": session,
        "timestamp": ts,
    }


def event_assistant_text(
    text: str,
    session: str,
    cwd: str,
    request_id: str = "req1",
    ts: str = "2026-08-13T10:00:01.000Z",
    nested_thinking: int = 7,
):
    return {
        "type": "assistant",
        "requestId": request_id,
        "message": {
            "role": "assistant",
            "id": "msg1",
            "content": [{"type": "text", "text": text}],
            "usage": {
                "input_tokens": 2,
                "cache_creation_input_tokens": 3,
                "cache_read_input_tokens": 4,
                "output_tokens": 5,
                "output_tokens_details": {"thinking_tokens": nested_thinking},
            },
        },
        "cwd": cwd,
        "sessionId": session,
        "timestamp": ts,
    }


def write_transcript(path: Path, prompt: str, response: str, session: str, cwd: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    events = [
        event_user(prompt, session, cwd),
        {
            "type": "user",
            "isMeta": True,
            "sourceToolUseID": "tool1",
            "message": {
                "role": "user",
                "content": [{"type": "text", "text": "META SKILL INJECTION"}],
            },
            "cwd": cwd,
            "sessionId": session,
            "timestamp": "2026-08-13T10:00:00.500Z",
        },
        event_assistant_text(response, session, cwd),
    ]
    path.write_text("\n".join(json.dumps(e, ensure_ascii=False) for e in events) + "\n", encoding="utf-8")


def run_cli(args, env=None):
    return subprocess.run(
        [sys.executable, str(COLLECTOR_PATH), *args],
        text=True,
        capture_output=True,
        check=False,
        env=env,
    )


class TestParserThinkingRealShape(unittest.TestCase):
    def test_nested_output_tokens_details_thinking(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td) / "x.jsonl"
            session = str(uuid.uuid4())
            p.write_text(
                json.dumps(event_assistant_text("ok", session, td)) + "\n",
                encoding="utf-8",
            )
            events = parsermod.read_jsonl(p)
            result, code = parsermod.analyze(
                events,
                run_id="x",
                scenario_id="x",
                condition="skill",
                skill_expected="yes",
                skill_name="example-skill",
            )
            self.assertEqual(code, 0)
            self.assertEqual(result.thinking_tokens, 7)
            self.assertNotIn("thinking_tokens:not_observable", result.observability_notes)


class TestCollector(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.claude = self.root / "claude"
        self.runs = self.root / "runs"
        self.cwd = str((self.root / "work").resolve())
        Path(self.cwd).mkdir()
        self.prompt_text = "Prompt exact de test."
        self.prompt = self.root / "prompt.txt"
        self.prompt.write_text(self.prompt_text, encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def start(self, run_id="R1", env=None):
        args = SimpleNamespace(
            run_id=run_id, scenario_id="S1", condition="skill",
            skill_expected="yes", prompt_file=str(self.prompt),
            claude_root=str(self.claude), cwd=self.cwd,
            output_root=str(self.runs), skill_name="example-skill",
        )
        old = os.environ.get("CLAUDE_CODE_DISABLE_AUTO_MEMORY")
        try:
            if env is not None and "CLAUDE_CODE_DISABLE_AUTO_MEMORY" in env:
                os.environ["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"]
            return SimpleNamespace(returncode=collector.cmd_start(args), stderr="")
        except collector.CollectError as exc:
            return SimpleNamespace(returncode=exc.code, stderr=exc.message)
        finally:
            if old is None:
                os.environ.pop("CLAUDE_CODE_DISABLE_AUTO_MEMORY", None)
            else:
                os.environ["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = old

    def collect(self, run_id="R1", session_id=None):
        args = SimpleNamespace(
            run_id=run_id, output_root=str(self.runs), session_id=session_id,
            parser=str(PARSER_PATH),
        )
        try:
            return SimpleNamespace(returncode=collector.cmd_collect(args), stderr="")
        except collector.CollectError as exc:
            return SimpleNamespace(returncode=exc.code, stderr=exc.message)

    def add_transcript(self, prompt=None, response="Réponse utile.", session=None):
        session = session or str(uuid.uuid4())
        path = self.claude / "project" / f"{session}.jsonl"
        write_transcript(path, prompt or self.prompt_text, response, session, self.cwd)
        return path, session

    def test_c01_human_prompt_excludes_meta(self):
        path, _ = self.add_transcript()
        info = collector.inspect_transcript(path)
        self.assertEqual(info.human_prompts, [self.prompt_text])

    def test_c02_start_creates_pending_and_snapshot(self):
        old, _ = self.add_transcript(prompt="ancien")
        proc = self.start()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        pending = json.loads((self.runs / ".pending" / "R1.json").read_text())
        self.assertIn(str(old.resolve()), pending["jsonl_snapshot"])
        self.assertEqual(pending["prompt_text"], self.prompt_text)

    def test_c03_unique_candidate_collects_seven_files(self):
        self.assertEqual(self.start().returncode, 0)
        source, session = self.add_transcript()
        source_hash = collector.sha256_file(source)
        proc = self.collect()
        self.assertEqual(proc.returncode, 0, proc.stderr)
        dest = self.runs / "R1"
        self.assertTrue(dest.is_dir())
        self.assertEqual(
            sorted(p.name for p in dest.iterdir()),
            ["metadata.json", "metrics.json", "prompt.txt", "response_raw.md", "sha256.txt", "trace.jsonl", "trajectory.md"],
        )
        self.assertTrue(source.exists())
        self.assertEqual(collector.sha256_file(source), source_hash)
        meta = json.loads((dest / "metadata.json").read_text())
        self.assertEqual(meta["session_id"], session)
        self.assertEqual(meta["source_jsonl_sha256"], meta["archive_jsonl_sha256"])
        metrics = json.loads((dest / "metrics.json").read_text())
        self.assertEqual(metrics["thinking_tokens"], 7)

    def test_c04_no_candidate(self):
        self.assertEqual(self.start().returncode, 0)
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_NO_CANDIDATE)

    def test_c05_ambiguity_is_refused(self):
        self.assertEqual(self.start().returncode, 0)
        self.add_transcript()
        self.add_transcript()
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_AMBIGUOUS)
        self.assertIn("--session-id", proc.stderr)

    def test_c06_session_id_disambiguates(self):
        self.assertEqual(self.start().returncode, 0)
        _, s1 = self.add_transcript(response="A")
        self.add_transcript(response="B")
        proc = self.collect(session_id=s1)
        self.assertEqual(proc.returncode, 0, proc.stderr)
        meta = json.loads((self.runs / "R1" / "metadata.json").read_text())
        self.assertEqual(meta["session_id"], s1)

    def test_c07_wrong_cwd_is_not_candidate(self):
        self.assertEqual(self.start().returncode, 0)
        session = str(uuid.uuid4())
        path = self.claude / "project" / f"{session}.jsonl"
        write_transcript(path, self.prompt_text, "x", session, str(self.root / "other"))
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_NO_CANDIDATE)

    def test_c08_wrong_prompt_is_not_candidate(self):
        self.assertEqual(self.start().returncode, 0)
        self.add_transcript(prompt="autre prompt")
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_NO_CANDIDATE)

    def test_c09_uuid_filename_mismatch_rejected(self):
        self.assertEqual(self.start().returncode, 0)
        internal = str(uuid.uuid4())
        filename = str(uuid.uuid4())
        path = self.claude / "project" / f"{filename}.jsonl"
        write_transcript(path, self.prompt_text, "x", internal, self.cwd)
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_NO_CANDIDATE)

    def test_c10_response_extraction_ignores_meta(self):
        path, _ = self.add_transcript(response="VISIBLE")
        text = collector.extract_response_text(path)
        self.assertEqual(text, "VISIBLE")
        self.assertNotIn("META", text)

    def test_c11_existing_run_is_never_overwritten(self):
        self.assertEqual(self.start().returncode, 0)
        self.add_transcript()
        self.assertEqual(self.collect().returncode, 0)
        proc = self.start()
        self.assertEqual(proc.returncode, collector.EXIT_EXISTS)

    def test_c12_memory_env_is_captured(self):
        env = os.environ.copy()
        env["CLAUDE_CODE_DISABLE_AUTO_MEMORY"] = "1"
        proc = self.start(env=env)
        self.assertEqual(proc.returncode, 0)
        pending = json.loads((self.runs / ".pending" / "R1.json").read_text())
        self.assertEqual(pending["claude_code_disable_auto_memory"], "1")

    def test_c13_sha_manifest_matches_files(self):
        self.assertEqual(self.start().returncode, 0)
        self.add_transcript()
        self.assertEqual(self.collect().returncode, 0)
        dest = self.runs / "R1"
        entries = {}
        for line in (dest / "sha256.txt").read_text().splitlines():
            digest, name = line.split("  ", 1)
            entries[name] = digest
        for name in ["prompt.txt", "trace.jsonl", "trajectory.md", "response_raw.md", "metrics.json", "metadata.json"]:
            self.assertEqual(entries[name], collector.sha256_file(dest / name))

    def test_c14_pending_removed_only_after_success(self):
        self.assertEqual(self.start().returncode, 0)
        pending = self.runs / ".pending" / "R1.json"
        self.assertTrue(pending.exists())
        self.add_transcript()
        self.assertEqual(self.collect().returncode, 0)
        self.assertFalse(pending.exists())

    def test_c15_ambiguous_failure_preserves_pending_and_sources(self):
        self.assertEqual(self.start().returncode, 0)
        p1, _ = self.add_transcript()
        p2, _ = self.add_transcript()
        proc = self.collect()
        self.assertEqual(proc.returncode, collector.EXIT_AMBIGUOUS)
        self.assertTrue((self.runs / ".pending" / "R1.json").exists())
        self.assertTrue(p1.exists())
        self.assertTrue(p2.exists())

    def test_c16_cli_start_smoke(self):
        proc = run_cli([
            "start", "--run-id", "CLI", "--scenario-id", "S1",
            "--condition", "skill", "--skill-expected", "yes",
            "--prompt-file", str(self.prompt), "--claude-root", str(self.claude),
            "--cwd", self.cwd, "--output-root", str(self.runs),
            "--skill-name", "example-skill",
        ])
        self.assertEqual(proc.returncode, 0, proc.stderr)
        self.assertTrue((self.runs / ".pending" / "CLI.json").exists())


if __name__ == "__main__":
    unittest.main(verbosity=2)
