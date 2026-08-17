#!/usr/bin/env python3
"""Collecte et archive de manière sûre un run Claude Code pour les campagnes.

Version 1.2.0 : collector générique pour les campagnes de validation de skills ; accepte aussi les trajectoires observables sans texte assistant (ex. AskUserQuestion annulé).

Workflow:
  collect_run.py start   ...
  # exécuter Claude Code dans une session fraîche, interactions comprises
  collect_run.py collect --run-id RUN_ID

Aucune suppression du store Claude Code n'est effectuée.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

COLLECTOR_VERSION = "1.2.0"

EXIT_OK = 0
EXIT_ARGS = 2
EXIT_NO_CANDIDATE = 3
EXIT_AMBIGUOUS = 4
EXIT_INVALID_TRANSCRIPT = 5
EXIT_EXISTS = 6
EXIT_INTEGRITY = 7
EXIT_PARSER = 8
EXIT_IO = 9

UUID_RE = re.compile(
    r"^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-"
    r"[89abAB][0-9a-fA-F]{3}-[0-9a-fA-F]{12}$"
)


class CollectError(Exception):
    def __init__(self, code: int, message: str):
        super().__init__(message)
        self.code = code
        self.message = message


@dataclass
class TranscriptInfo:
    path: str
    session_id: str | None
    session_ids: list[str]
    cwds: list[str]
    human_prompts: list[str]
    first_timestamp: str | None
    last_timestamp: str | None
    mtime_ns: int
    size: int
    filename_matches_session: bool | None

    @property
    def first_human_prompt(self) -> str | None:
        return self.human_prompts[0] if self.human_prompts else None

    @property
    def last_human_prompt(self) -> str | None:
        return self.human_prompts[-1] if self.human_prompts else None


@dataclass
class TrajectoryItem:
    kind: str
    text: str = ""
    tool_name: str | None = None
    details: str = ""
    key: str | None = None


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def normalize_prompt(text: str) -> str:
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text.rstrip()


def normalize_path_text(path_text: str) -> str:
    return str(Path(path_text).expanduser().resolve(strict=False))


def extract_text_blocks(message: dict[str, Any]) -> list[str]:
    content = message.get("content")
    if isinstance(content, str):
        return [content]
    texts: list[str] = []
    if isinstance(content, list):
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text")
                if isinstance(text, str):
                    texts.append(text)
    return texts


def is_human_user_event(event: dict[str, Any]) -> bool:
    if event.get("type") != "user":
        return False
    message = event.get("message")
    if not isinstance(message, dict) or message.get("role") != "user":
        return False

    # Les marqueurs techniques priment même si un futur schéma expose un origin.
    if event.get("isMeta"):
        return False
    if event.get("toolUseResult") is not None:
        return False
    if event.get("sourceToolUseID") is not None:
        return False
    if event.get("sourceToolAssistantUUID") is not None:
        return False

    origin = event.get("origin")
    if isinstance(origin, dict) and origin.get("kind") == "human":
        return True

    if event.get("promptId") and extract_text_blocks(message):
        return True
    return False


def read_events(path: Path) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    try:
        with path.open("r", encoding="utf-8") as fh:
            for line_no, raw in enumerate(fh, 1):
                if not raw.strip():
                    continue
                try:
                    value = json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise CollectError(
                        EXIT_INVALID_TRANSCRIPT,
                        f"{path}: JSON invalide ligne {line_no}: {exc}",
                    ) from exc
                if not isinstance(value, dict):
                    raise CollectError(
                        EXIT_INVALID_TRANSCRIPT,
                        f"{path}: ligne {line_no} n'est pas un objet JSON",
                    )
                events.append(value)
    except OSError as exc:
        raise CollectError(EXIT_IO, f"lecture impossible {path}: {exc}") from exc
    return events


def inspect_transcript(path: Path) -> TranscriptInfo:
    events = read_events(path)
    session_ids = sorted({str(e["sessionId"]) for e in events if e.get("sessionId")})
    session_id = session_ids[0] if len(session_ids) == 1 else None
    cwds = sorted({normalize_path_text(str(e["cwd"])) for e in events if e.get("cwd")})

    human_prompts: list[str] = []
    timestamps: list[str] = []
    for event in events:
        ts = event.get("timestamp")
        if isinstance(ts, str) and ts:
            timestamps.append(ts)
        if is_human_user_event(event):
            message = event.get("message")
            assert isinstance(message, dict)
            texts = extract_text_blocks(message)
            if texts:
                human_prompts.append("\n".join(texts))

    stat = path.stat()
    filename_matches: bool | None = None
    if session_id and UUID_RE.match(path.stem):
        filename_matches = path.stem == session_id

    return TranscriptInfo(
        path=str(path),
        session_id=session_id,
        session_ids=session_ids,
        cwds=cwds,
        human_prompts=human_prompts,
        first_timestamp=min(timestamps) if timestamps else None,
        last_timestamp=max(timestamps) if timestamps else None,
        mtime_ns=stat.st_mtime_ns,
        size=stat.st_size,
        filename_matches_session=filename_matches,
    )


def snapshot_jsonl(root: Path) -> dict[str, dict[str, int]]:
    snapshot: dict[str, dict[str, int]] = {}
    if not root.exists():
        return snapshot
    try:
        paths = sorted(root.rglob("*.jsonl"))
    except OSError as exc:
        raise CollectError(EXIT_IO, f"scan impossible de {root}: {exc}") from exc
    for path in paths:
        try:
            st = path.stat()
        except OSError:
            continue
        snapshot[str(path.resolve(strict=False))] = {
            "mtime_ns": st.st_mtime_ns,
            "size": st.st_size,
        }
    return snapshot


def changed_jsonl(root: Path, before: dict[str, dict[str, int]]) -> list[Path]:
    candidates: list[Path] = []
    if not root.exists():
        return candidates
    for path in sorted(root.rglob("*.jsonl")):
        try:
            st = path.stat()
        except OSError:
            continue
        key = str(path.resolve(strict=False))
        previous = before.get(key)
        if (
            previous is None
            or previous.get("mtime_ns") != st.st_mtime_ns
            or previous.get("size") != st.st_size
        ):
            candidates.append(path)
    return candidates


def transcript_matches(
    info: TranscriptInfo,
    *,
    cwd_expected: str,
    prompt_expected: str,
    session_id: str | None,
) -> bool:
    if len(info.session_ids) != 1 or not info.session_id:
        return False
    if info.filename_matches_session is False:
        return False
    if session_id and info.session_id != session_id:
        return False
    if normalize_path_text(cwd_expected) not in info.cwds:
        return False
    expected = normalize_prompt(prompt_expected)
    if expected not in {normalize_prompt(x) for x in info.human_prompts}:
        return False
    return True


def find_initial_prompt_index(events: list[dict[str, Any]], prompt_expected: str) -> int:
    expected = normalize_prompt(prompt_expected)
    for idx, event in enumerate(events):
        if not is_human_user_event(event):
            continue
        message = event.get("message")
        if not isinstance(message, dict):
            continue
        text = "\n".join(extract_text_blocks(message))
        if normalize_prompt(text) == expected:
            return idx
    raise CollectError(EXIT_INVALID_TRANSCRIPT, "prompt initial exact introuvable dans le transcript")


def _tool_leaf(name: str) -> str:
    leaf = name.strip()
    for sep in ("__", ".", "/", ":"):
        if sep in leaf:
            leaf = leaf.split(sep)[-1]
    return leaf.casefold()


def _extract_path(tool_input: Any) -> str | None:
    if isinstance(tool_input, str):
        return tool_input
    if not isinstance(tool_input, dict):
        return None
    for key in ("file_path", "path", "filepath", "filename", "uri"):
        value = tool_input.get(key)
        if isinstance(value, str) and value:
            return value
    return None


def _assistant_call_key(event: dict[str, Any], event_index: int) -> str:
    request_id = event.get("requestId") or event.get("request_id")
    if request_id:
        return f"request:{request_id}"
    message = event.get("message")
    if isinstance(message, dict):
        message_id = message.get("id") or message.get("message_id")
        if message_id:
            return f"message:{message_id}"
    event_uuid = event.get("uuid")
    if event_uuid:
        return f"uuid:{event_uuid}"
    return f"event:{event_index}"


def _tool_id(block: dict[str, Any], event_index: int, block_index: int) -> str:
    value = block.get("id") or block.get("tool_use_id") or block.get("call_id")
    if value:
        return str(value)
    return f"unkeyed:{event_index}:{block_index}"


def _format_ask_questions(tool_input: Any) -> str:
    if not isinstance(tool_input, dict):
        return ""
    questions = tool_input.get("questions")
    if not isinstance(questions, list):
        question = tool_input.get("question")
        return str(question).strip() if isinstance(question, str) else ""
    lines: list[str] = []
    for q in questions:
        if not isinstance(q, dict):
            continue
        header = q.get("header")
        question = q.get("question")
        label = f"[{header}] " if isinstance(header, str) and header.strip() else ""
        if isinstance(question, str) and question.strip():
            lines.append(f"{label}{question.strip()}")
        options = q.get("options")
        if isinstance(options, list):
            rendered: list[str] = []
            for option in options:
                if isinstance(option, dict):
                    value = option.get("label") or option.get("value") or option.get("description")
                    if isinstance(value, str) and value.strip():
                        rendered.append(value.strip())
                elif isinstance(option, str) and option.strip():
                    rendered.append(option.strip())
            if rendered:
                lines.append("Options: " + " | ".join(rendered))
    return "\n".join(lines)


def _format_tool_details(name: str, tool_input: Any) -> str:
    leaf = _tool_leaf(name)
    if leaf in {"read", "write", "edit", "multiedit", "notebookedit"}:
        path = _extract_path(tool_input)
        return path or ""
    if leaf == "skill":
        if isinstance(tool_input, dict):
            for key in ("skill", "skill_name", "name"):
                value = tool_input.get(key)
                if isinstance(value, str) and value:
                    return value
        if isinstance(tool_input, str):
            return tool_input
        return ""
    if leaf == "askuserquestion":
        return _format_ask_questions(tool_input)
    return ""


def _nonempty_answers(value: Any) -> bool:
    if isinstance(value, dict):
        return any(v not in (None, "", [], {}, ()) for v in value.values())
    if isinstance(value, list):
        return any(v not in (None, "", [], {}, ()) for v in value)
    if isinstance(value, str):
        return bool(value.strip())
    return value is not None


def _format_answers(value: Any) -> str:
    if isinstance(value, dict):
        lines: list[str] = []
        for key, answer in value.items():
            if answer in (None, "", [], {}, ()):
                continue
            if isinstance(answer, (dict, list)):
                rendered = json.dumps(answer, ensure_ascii=False, sort_keys=True)
            else:
                rendered = str(answer)
            lines.append(f"{key}: {rendered}")
        return "\n".join(lines)
    if isinstance(value, list):
        return "\n".join(str(v) for v in value if v not in (None, "", [], {}, ()))
    if isinstance(value, str):
        return value.strip()
    return "" if value is None else str(value)


def build_trajectory(events: list[dict[str, Any]], anchor_index: int) -> list[TrajectoryItem]:
    items: list[TrajectoryItem] = []
    # (appel assistant, index de bloc texte) -> index dans items
    text_slots: dict[tuple[str, int], int] = {}
    seen_tool_ids: set[str] = set()
    ask_tool_ids: set[str] = set()
    seen_ask_results: set[str] = set()

    for event_index in range(anchor_index, len(events)):
        event = events[event_index]
        event_type = str(event.get("type", "")).casefold()

        if is_human_user_event(event):
            message = event.get("message")
            assert isinstance(message, dict)
            text = "\n".join(extract_text_blocks(message)).strip()
            if text:
                items.append(TrajectoryItem(kind="user", text=text))
            continue

        if event_type == "assistant":
            message = event.get("message")
            if not isinstance(message, dict) or message.get("role") != "assistant":
                continue
            content = message.get("content")
            if not isinstance(content, list):
                continue
            call_key = _assistant_call_key(event, event_index)
            for block_index, block in enumerate(content):
                if not isinstance(block, dict):
                    continue
                block_type = str(block.get("type", "")).casefold()
                if block_type == "text":
                    text = block.get("text")
                    if not isinstance(text, str) or not text.strip():
                        continue
                    slot_key = (call_key, block_index)
                    existing_index = text_slots.get(slot_key)
                    if existing_index is None:
                        text_slots[slot_key] = len(items)
                        items.append(
                            TrajectoryItem(
                                kind="assistant",
                                text=text.strip(),
                                key=f"{call_key}:text:{block_index}",
                            )
                        )
                    else:
                        previous = items[existing_index].text
                        candidate = text.strip()
                        if candidate == previous:
                            continue
                        if candidate.startswith(previous):
                            items[existing_index].text = candidate
                        elif previous.startswith(candidate):
                            continue
                        else:
                            # Bloc distinct malgré le même index : conserver, ne pas écraser.
                            text_slots[(f"{call_key}:variant:{event_index}", block_index)] = len(items)
                            items.append(
                                TrajectoryItem(
                                    kind="assistant",
                                    text=candidate,
                                    key=f"{call_key}:variant:{event_index}:text:{block_index}",
                                )
                            )
                elif block_type == "tool_use":
                    tool_id = _tool_id(block, event_index, block_index)
                    if tool_id in seen_tool_ids:
                        continue
                    seen_tool_ids.add(tool_id)
                    name = str(block.get("name", ""))
                    details = _format_tool_details(name, block.get("input"))
                    items.append(
                        TrajectoryItem(
                            kind="tool",
                            tool_name=name,
                            details=details,
                            key=f"tool:{tool_id}",
                        )
                    )
                    if _tool_leaf(name) == "askuserquestion":
                        ask_tool_ids.add(tool_id)
            continue

        if event_type == "user" and not is_human_user_event(event):
            message = event.get("message")
            content = message.get("content") if isinstance(message, dict) else None
            matched_ask_id: str | None = None
            if isinstance(content, list):
                for block in content:
                    if not isinstance(block, dict) or str(block.get("type", "")).casefold() != "tool_result":
                        continue
                    tool_use_id = block.get("tool_use_id") or block.get("toolUseId")
                    if isinstance(tool_use_id, str) and tool_use_id in ask_tool_ids:
                        matched_ask_id = tool_use_id
                        break

            structured = event.get("toolUseResult")
            answers = structured.get("answers") if isinstance(structured, dict) else None
            has_ask_shape = isinstance(structured, dict) and (
                isinstance(structured.get("questions"), list) or "answers" in structured
            )

            result_key: str | None = None
            if matched_ask_id:
                result_key = f"tool:{matched_ask_id}"
            elif has_ask_shape and len(ask_tool_ids) == 1:
                result_key = f"ask-result:event:{event_index}"

            if result_key and result_key not in seen_ask_results:
                seen_ask_results.add(result_key)
                if _nonempty_answers(answers):
                    items.append(
                        TrajectoryItem(
                            kind="ask_user_answer",
                            text=_format_answers(answers),
                            tool_name="AskUserQuestion",
                            key=result_key,
                        )
                    )
            continue

    return items


def render_trajectory_markdown(items: list[TrajectoryItem]) -> str:
    parts: list[str] = []
    for item in items:
        if item.kind == "user":
            parts.append("## USER\n\n" + item.text)
        elif item.kind == "assistant":
            parts.append("## ASSISTANT\n\n" + item.text)
        elif item.kind == "tool":
            header = f"## TOOL {item.tool_name or ''}".rstrip()
            parts.append(header + ("\n\n" + item.details if item.details else ""))
        elif item.kind == "ask_user_answer":
            parts.append("## USER VIA AskUserQuestion\n\n" + item.text)
    return "\n\n".join(parts).strip()


def render_response_raw(items: list[TrajectoryItem]) -> str:
    return "\n\n".join(item.text for item in items if item.kind == "assistant" and item.text).strip()


def extract_response_text(path: Path) -> str:
    """Compatibilité 1.0 : vue assistant-only depuis le premier vrai prompt humain."""
    events = read_events(path)
    for idx, event in enumerate(events):
        if is_human_user_event(event):
            return render_response_raw(build_trajectory(events, idx))
    return ""


def count_human_turns(items: list[TrajectoryItem]) -> int:
    return sum(1 for item in items if item.kind == "user")


def atomic_json(path: Path, payload: dict[str, Any], *, pretty: bool = True) -> None:
    if pretty:
        data = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    else:
        data = json.dumps(payload, ensure_ascii=False, sort_keys=True) + "\n"
    path.write_text(data, encoding="utf-8")


def pending_path(output_root: Path, run_id: str) -> Path:
    return output_root / ".pending" / f"{run_id}.json"


def canonical_path(output_root: Path, run_id: str) -> Path:
    return output_root / run_id


def cmd_start(args: argparse.Namespace) -> int:
    output_root = Path(args.output_root).expanduser().resolve(strict=False)
    claude_root = Path(args.claude_root).expanduser().resolve(strict=False)
    cwd_expected = normalize_path_text(args.cwd)
    prompt_path = Path(args.prompt_file).expanduser().resolve(strict=False)

    if canonical_path(output_root, args.run_id).exists():
        raise CollectError(EXIT_EXISTS, f"run déjà archivé: {args.run_id}")
    ppath = pending_path(output_root, args.run_id)
    if ppath.exists():
        raise CollectError(EXIT_EXISTS, f"pending déjà existant: {args.run_id}")
    if not prompt_path.is_file():
        raise CollectError(EXIT_ARGS, f"prompt-file introuvable: {prompt_path}")

    prompt_bytes = prompt_path.read_bytes()
    try:
        prompt_text = prompt_bytes.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise CollectError(EXIT_ARGS, "prompt-file doit être UTF-8") from exc

    output_root.mkdir(parents=True, exist_ok=True)
    ppath.parent.mkdir(parents=True, exist_ok=True)

    payload = {
        "collector_version": COLLECTOR_VERSION,
        "run_id": args.run_id,
        "scenario_id": args.scenario_id,
        "condition": args.condition,
        "skill_expected": args.skill_expected,
        "skill_name": args.skill_name,
        "prompt_file_source": str(prompt_path),
        "prompt_text": prompt_text,
        "prompt_sha256": sha256_bytes(prompt_bytes),
        "claude_root": str(claude_root),
        "cwd_expected": cwd_expected,
        "claude_code_disable_auto_memory": os.environ.get(
            "CLAUDE_CODE_DISABLE_AUTO_MEMORY", ""
        ),
        "started_at": utc_now(),
        "jsonl_snapshot": snapshot_jsonl(claude_root),
    }
    atomic_json(ppath, payload)
    print(f"READY {args.run_id}")
    print(f"pending={ppath}")
    print(f"cwd={cwd_expected}")
    print(f"prompt_sha256={payload['prompt_sha256']}")
    return EXIT_OK


def run_parser(
    parser_path: Path,
    trace_path: Path,
    metrics_path: Path,
    pending: dict[str, Any],
) -> subprocess.CompletedProcess[str]:
    cmd = [
        sys.executable,
        str(parser_path),
        str(trace_path),
        "--run-id",
        str(pending["run_id"]),
        "--scenario-id",
        str(pending["scenario_id"]),
        "--condition",
        str(pending["condition"]),
        "--skill-expected",
        str(pending["skill_expected"]),
        "--output",
        str(metrics_path),
        "--pretty",
        "--skill-name",
        str(pending["skill_name"]),
    ]
    return subprocess.run(cmd, text=True, capture_output=True, check=False)


def write_sha_manifest(directory: Path, names: Iterable[str]) -> None:
    lines = []
    for name in names:
        path = directory / name
        lines.append(f"{sha256_file(path)}  {name}")
    (directory / "sha256.txt").write_text("\n".join(lines) + "\n", encoding="utf-8")


def cmd_collect(args: argparse.Namespace) -> int:
    output_root = Path(args.output_root).expanduser().resolve(strict=False)
    ppath = pending_path(output_root, args.run_id)
    if not ppath.is_file():
        raise CollectError(EXIT_ARGS, f"pending introuvable: {ppath}")
    if canonical_path(output_root, args.run_id).exists():
        raise CollectError(EXIT_EXISTS, f"run déjà archivé: {args.run_id}")

    try:
        pending = json.loads(ppath.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CollectError(EXIT_IO, f"pending illisible: {exc}") from exc

    claude_root = Path(pending["claude_root"]).expanduser().resolve(strict=False)
    before = pending.get("jsonl_snapshot")
    if not isinstance(before, dict):
        raise CollectError(EXIT_ARGS, "snapshot absent du pending")

    changed = changed_jsonl(claude_root, before)
    infos: list[TranscriptInfo] = []
    rejected: list[str] = []
    for path in changed:
        try:
            info = inspect_transcript(path)
        except CollectError as exc:
            rejected.append(f"{path}: {exc.message}")
            continue
        if transcript_matches(
            info,
            cwd_expected=str(pending["cwd_expected"]),
            prompt_expected=str(pending["prompt_text"]),
            session_id=args.session_id,
        ):
            infos.append(info)

    if not infos:
        details = "\n".join(f"- {x}" for x in rejected[:5])
        msg = (
            f"aucun transcript candidat pour {args.run_id}; "
            f"{len(changed)} JSONL nouveaux/modifiés inspectés"
        )
        if details:
            msg += f"\n{details}"
        raise CollectError(EXIT_NO_CANDIDATE, msg)
    if len(infos) > 1:
        lines = [
            f"- session={i.session_id} path={i.path} last={i.last_timestamp}"
            for i in infos[:10]
        ]
        raise CollectError(
            EXIT_AMBIGUOUS,
            "plusieurs transcripts correspondent au run; utiliser --session-id:\n"
            + "\n".join(lines),
        )

    info = infos[0]
    if len(info.session_ids) != 1 or not info.session_id:
        raise CollectError(EXIT_INVALID_TRANSCRIPT, "sessionId non unique")
    if info.filename_matches_session is False:
        raise CollectError(
            EXIT_INVALID_TRANSCRIPT,
            "nom de JSONL UUID différent du sessionId interne",
        )

    source = Path(info.path)
    parser_path = (
        Path(args.parser).expanduser().resolve(strict=False)
        if args.parser
        else Path(__file__).resolve().with_name("analyse_jsonl.py")
    )
    if not parser_path.is_file():
        raise CollectError(EXIT_ARGS, f"parseur introuvable: {parser_path}")

    staging_root = output_root / ".staging"
    failed_root = output_root / "_failed"
    staging_root.mkdir(parents=True, exist_ok=True)
    stage = staging_root / f"{args.run_id}-{uuid.uuid4()}"
    stage.mkdir()

    try:
        prompt_target = stage / "prompt.txt"
        trace_target = stage / "trace.jsonl"
        trajectory_target = stage / "trajectory.md"
        response_target = stage / "response_raw.md"
        metrics_target = stage / "metrics.json"
        metadata_target = stage / "metadata.json"

        prompt_target.write_text(str(pending["prompt_text"]), encoding="utf-8")

        source_hash = sha256_file(source)
        shutil.copyfile(source, trace_target)
        archive_hash = sha256_file(trace_target)
        if source_hash != archive_hash:
            raise CollectError(EXIT_INTEGRITY, "hash source/copie différent")

        events = read_events(trace_target)
        anchor_index = find_initial_prompt_index(events, str(pending["prompt_text"]))
        trajectory = build_trajectory(events, anchor_index)
        trajectory_md = render_trajectory_markdown(trajectory)
        response = render_response_raw(trajectory)
        # Une trajectoire peut être expérimentalement valide sans texte assistant :
        # par exemple Claude appelle AskUserQuestion puis l'opérateur fait Esc,
        # conformément au protocole, afin de ne pas injecter d'information absente.
        # Dans ce cas le TOOL est précisément le comportement à observer.
        has_observable_after_prompt = any(
            item.kind in {"assistant", "tool", "ask_user_answer"}
            for item in trajectory
        )
        if not has_observable_after_prompt:
            raise CollectError(
                EXIT_INVALID_TRANSCRIPT,
                "aucune activité assistant/outils observable depuis le prompt initial",
            )
        trajectory_target.write_text(trajectory_md + "\n", encoding="utf-8")
        response_target.write_text((response + "\n") if response else "", encoding="utf-8")

        proc = run_parser(parser_path, trace_target, metrics_target, pending)

        metadata = {
            "run_id": pending["run_id"],
            "scenario_id": pending["scenario_id"],
            "condition": pending["condition"],
            "skill_expected": pending["skill_expected"],
            "session_id": info.session_id,
            "source_jsonl": str(source.resolve(strict=False)),
            "source_jsonl_sha256": source_hash,
            "archive_jsonl_sha256": archive_hash,
            "cwd_expected": pending["cwd_expected"],
            "cwd_observed": info.cwds,
            "prompt_sha256": pending["prompt_sha256"],
            "initial_prompt": str(pending["prompt_text"]).rstrip("\r\n"),
            "first_human_prompt": info.first_human_prompt,
            "last_human_prompt": info.last_human_prompt,
            "human_turns": count_human_turns(trajectory),
            "trajectory_sha256": sha256_file(trajectory_target),
            "response_raw_sha256": sha256_file(response_target),
            "claude_code_disable_auto_memory": pending.get(
                "claude_code_disable_auto_memory", ""
            ),
            "collector_version": COLLECTOR_VERSION,
            "parser_sha256": sha256_file(parser_path),
            "analysis_exit_code": proc.returncode,
            "analysis_stderr": proc.stderr.strip(),
            "started_at": pending["started_at"],
            "collected_at": utc_now(),
            "source_filename_matches_session": info.filename_matches_session,
        }
        atomic_json(metadata_target, metadata)

        content_names = [
            "prompt.txt",
            "trace.jsonl",
            "trajectory.md",
            "response_raw.md",
            "metadata.json",
        ] + (["metrics.json"] if metrics_target.exists() else [])

        if proc.returncode != 0:
            failed_root.mkdir(parents=True, exist_ok=True)
            failed = failed_root / (
                f"{args.run_id}-"
                f"{dt.datetime.now().strftime('%Y%m%dT%H%M%S')}-"
                f"{uuid.uuid4().hex[:8]}"
            )
            write_sha_manifest(stage, content_names)
            stage.rename(failed)
            raise CollectError(
                EXIT_PARSER,
                f"parseur en échec code={proc.returncode}; diagnostic={failed}",
            )

        write_sha_manifest(
            stage,
            [
                "prompt.txt",
                "trace.jsonl",
                "trajectory.md",
                "response_raw.md",
                "metrics.json",
                "metadata.json",
            ],
        )

        destination = canonical_path(output_root, args.run_id)
        if destination.exists():
            raise CollectError(EXIT_EXISTS, f"destination existe: {destination}")
        stage.rename(destination)
        ppath.unlink()

        print(f"COLLECTED {args.run_id}")
        print(f"session_id={info.session_id}")
        print(f"human_turns={metadata['human_turns']}")
        print(f"archive={destination}")
        print(f"trace_sha256={archive_hash}")
        return EXIT_OK

    except CollectError:
        raise
    except OSError as exc:
        raise CollectError(EXIT_IO, f"erreur I/O: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Collecte sûre des runs Claude Code pour les campagnes de validation comportementale."
    )
    sub = parser.add_subparsers(dest="command", required=True)

    pstart = sub.add_parser("start", help="photographier le store avant un run")
    pstart.add_argument("--run-id", required=True)
    pstart.add_argument("--scenario-id", required=True)
    pstart.add_argument("--condition", required=True)
    pstart.add_argument("--skill-expected", required=True, choices=["yes", "no", "n/a"])
    pstart.add_argument("--prompt-file", required=True)
    pstart.add_argument("--claude-root", default="~/.claude/projects")
    pstart.add_argument("--cwd", default=os.getcwd())
    pstart.add_argument("--output-root", default="./runs")
    pstart.add_argument(
        "--skill-name",
        required=True,
        help="nom exact du skill dont l’invocation doit être observée",
    )

    pcollect = sub.add_parser("collect", help="collecter le run depuis le snapshot")
    pcollect.add_argument("--run-id", required=True)
    pcollect.add_argument("--output-root", default="./runs")
    pcollect.add_argument("--session-id")
    pcollect.add_argument("--parser", help="chemin du moteur analyse_jsonl.py")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.command == "start":
            return cmd_start(args)
        if args.command == "collect":
            return cmd_collect(args)
        raise CollectError(EXIT_ARGS, "commande inconnue")
    except CollectError as exc:
        print(f"ERROR[{exc.code}] {exc.message}", file=sys.stderr)
        return exc.code
    except KeyboardInterrupt:
        print("interrompu", file=sys.stderr)
        return 130


if __name__ == "__main__":
    raise SystemExit(main())
