#!/usr/bin/env python3
"""Analyse déterministe d'un transcript JSONL Claude Code pour la validation comportementale.

Le script ne score pas la qualité d'une réponse. Il extrait uniquement des signaux
observables dans la trace et marque explicitement les limites d'observabilité.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import OrderedDict
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Iterator

EXIT_OK = 0
EXIT_ARGS = 2
EXIT_INVALID_JSONL = 3
EXIT_UNRELIABLE = 4

USAGE_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)
THINKING_KEYS = ("thinking_tokens", "reasoning_tokens")

WRITE_TOOL_LEAVES = {"write"}
EDIT_TOOL_LEAVES = {"edit", "multiedit", "notebookedit"}
READ_TOOL_LEAVES = {"read"}
ASK_USER_QUESTION_LEAVES = {"askuserquestion"}


@dataclass(frozen=True)
class EventRecord:
    line_no: int
    data: dict[str, Any]


@dataclass
class ModelUsageObservation:
    key: str
    line_no: int
    input_tokens: int
    cache_creation_input_tokens: int
    cache_read_input_tokens: int
    output_tokens: int
    thinking_tokens: int | None

    @property
    def invariant_tuple(self) -> tuple[int, int, int]:
        return (
            self.input_tokens,
            self.cache_creation_input_tokens,
            self.cache_read_input_tokens,
        )


@dataclass(frozen=True)
class ToolCall:
    key: str
    line_no: int
    block_index: int
    name: str
    input: Any


@dataclass
class AnalysisResult:
    run_id: str
    scenario_id: str
    condition: str
    skill_expected: str
    model_calls: int = 0
    input_tokens: int = 0
    cache_creation_input_tokens: int = 0
    cache_read_input_tokens: int = 0
    output_tokens: int = 0
    thinking_tokens: int = 0
    tool_calls: int = 0
    tool_names: list[str] = field(default_factory=list)
    memory_searches: int = 0
    file_reads: int = 0
    file_writes: int = 0
    file_edits: int = 0
    ask_user_question_calls: int = 0
    ask_user_question_results: int = 0
    ask_user_question_answered_results: int = 0
    skill_listed: str = "not_observable"
    skill_invoked: str = "not_observable"
    skill_reference_reads: int = 0
    skill_reference_names: list[str] = field(default_factory=list)
    observability_notes: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "run_id": self.run_id,
            "scenario_id": self.scenario_id,
            "condition": self.condition,
            "skill_expected": self.skill_expected,
            "model_calls": self.model_calls,
            "input_tokens": self.input_tokens,
            "cache_creation_input_tokens": self.cache_creation_input_tokens,
            "cache_read_input_tokens": self.cache_read_input_tokens,
            "output_tokens": self.output_tokens,
            "thinking_tokens": self.thinking_tokens,
            "tool_calls": self.tool_calls,
            "tool_names": self.tool_names,
            "memory_searches": self.memory_searches,
            "file_reads": self.file_reads,
            "file_writes": self.file_writes,
            "file_edits": self.file_edits,
            "ask_user_question_calls": self.ask_user_question_calls,
            "ask_user_question_results": self.ask_user_question_results,
            "ask_user_question_answered_results": self.ask_user_question_answered_results,
            "skill_listed": self.skill_listed,
            "skill_invoked": self.skill_invoked,
            "skill_reference_reads": self.skill_reference_reads,
            "skill_reference_names": self.skill_reference_names,
            "observability_notes": sorted(set(self.observability_notes)),
        }


class JsonlParseError(Exception):
    def __init__(self, line_no: int, message: str):
        super().__init__(f"ligne {line_no}: {message}")
        self.line_no = line_no
        self.message = message


def read_jsonl(path: Path) -> list[EventRecord]:
    events: list[EventRecord] = []
    try:
        with path.open("r", encoding="utf-8") as handle:
            for line_no, raw in enumerate(handle, 1):
                if not raw.strip():
                    continue
                try:
                    data = json.loads(raw)
                except json.JSONDecodeError as exc:
                    raise JsonlParseError(line_no, str(exc)) from exc
                if not isinstance(data, dict):
                    raise JsonlParseError(line_no, "chaque ligne JSONL doit être un objet JSON")
                events.append(EventRecord(line_no=line_no, data=data))
    except OSError as exc:
        raise JsonlParseError(0, f"lecture impossible: {exc}") from exc
    return events


def _int(value: Any, default: int = 0) -> int:
    if value is None:
        return default
    if isinstance(value, bool):
        return int(value)
    if isinstance(value, int):
        return value
    if isinstance(value, float) and value.is_integer():
        return int(value)
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def _string_contains(obj: Any, needle: str) -> bool:
    needle_cf = needle.casefold()
    if isinstance(obj, str):
        return needle_cf in obj.casefold()
    if isinstance(obj, dict):
        return any(_string_contains(k, needle) or _string_contains(v, needle) for k, v in obj.items())
    if isinstance(obj, list):
        return any(_string_contains(v, needle) for v in obj)
    return False


def _event_has_explicit_skill_listing(event: dict[str, Any]) -> bool:
    event_type = str(event.get("type", "")).casefold()
    if event_type in {"skill_listing", "skills_listing", "available_skills"}:
        return True
    message = event.get("message")
    if isinstance(message, dict):
        content = message.get("content")
        if isinstance(content, list):
            for block in content:
                if isinstance(block, dict) and str(block.get("type", "")).casefold() in {
                    "skill_listing",
                    "skills_listing",
                    "available_skills",
                }:
                    return True
    return False


def _stable_model_key(event: EventRecord) -> str | None:
    data = event.data
    request_id = data.get("requestId") or data.get("request_id")
    if request_id:
        return f"request:{request_id}"
    message = data.get("message")
    if isinstance(message, dict):
        message_id = message.get("id") or message.get("message_id")
        if message_id:
            return f"message:{message_id}"
    call_id = data.get("callId") or data.get("call_id")
    if call_id:
        return f"call:{call_id}"
    return None


def extract_model_usage_event(event: EventRecord) -> ModelUsageObservation | None:
    data = event.data
    if str(data.get("type", "")).casefold() != "assistant":
        return None
    message = data.get("message")
    if not isinstance(message, dict):
        return None
    usage = message.get("usage")
    if not isinstance(usage, dict):
        return None
    key = _stable_model_key(event)
    if not key:
        return ModelUsageObservation(
            key=f"unkeyed:line:{event.line_no}",
            line_no=event.line_no,
            input_tokens=_int(usage.get("input_tokens")),
            cache_creation_input_tokens=_int(usage.get("cache_creation_input_tokens")),
            cache_read_input_tokens=_int(usage.get("cache_read_input_tokens")),
            output_tokens=_int(usage.get("output_tokens")),
            thinking_tokens=_extract_thinking(usage),
        )
    return ModelUsageObservation(
        key=key,
        line_no=event.line_no,
        input_tokens=_int(usage.get("input_tokens")),
        cache_creation_input_tokens=_int(usage.get("cache_creation_input_tokens")),
        cache_read_input_tokens=_int(usage.get("cache_read_input_tokens")),
        output_tokens=_int(usage.get("output_tokens")),
        thinking_tokens=_extract_thinking(usage),
    )


def _extract_thinking(usage: dict[str, Any]) -> int | None:
    # Formes directes.
    for key in THINKING_KEYS:
        if key in usage and usage.get(key) is not None:
            return _int(usage.get(key))

    # Claude Code réel peut exposer le détail sous output_tokens_details.
    details = usage.get("output_tokens_details")
    if isinstance(details, dict):
        for key in THINKING_KEYS:
            if key in details and details.get(key) is not None:
                return _int(details.get(key))
    return None


def aggregate_model_usage(
    events: Iterable[EventRecord], result: AnalysisResult
) -> bool:
    """Agrège l'usage. Retourne True si le comptage est fiable."""
    observations: list[ModelUsageObservation] = []
    for event in events:
        obs = extract_model_usage_event(event)
        if obs is not None:
            observations.append(obs)

    if not observations:
        result.observability_notes.append("model_usage:not_observable")
        return True

    grouped: "OrderedDict[str, list[ModelUsageObservation]]" = OrderedDict()
    reliable = True
    for obs in observations:
        if obs.key.startswith("unkeyed:"):
            result.observability_notes.append(
                f"model_usage:missing_stable_call_id:line_{obs.line_no}"
            )
            reliable = False
        grouped.setdefault(obs.key, []).append(obs)

    thinking_observable = False
    for key, group in grouped.items():
        invariants = {obs.invariant_tuple for obs in group}
        if len(invariants) != 1:
            result.observability_notes.append(f"model_usage:conflict:{key}")
            reliable = False
            continue

        first = group[0]
        result.model_calls += 1
        result.input_tokens += first.input_tokens
        result.cache_creation_input_tokens += first.cache_creation_input_tokens
        result.cache_read_input_tokens += first.cache_read_input_tokens

        outputs = [obs.output_tokens for obs in group]
        result.output_tokens += max(outputs, default=0)
        if len(set(outputs)) > 1:
            result.observability_notes.append(
                f"output_tokens:max_observed_progressive_update:{key}"
            )

        visible_thinking = [obs.thinking_tokens for obs in group if obs.thinking_tokens is not None]
        if visible_thinking:
            thinking_observable = True
            result.thinking_tokens += max(visible_thinking)
            if len(set(visible_thinking)) > 1:
                result.observability_notes.append(
                    f"thinking_tokens:max_observed_progressive_update:{key}"
                )

    if not thinking_observable:
        result.observability_notes.append("thinking_tokens:not_observable")

    return reliable


def _tool_key(block: dict[str, Any], line_no: int, block_index: int) -> str:
    tool_id = block.get("id") or block.get("tool_use_id") or block.get("call_id")
    if tool_id:
        return f"tool:{tool_id}"
    return f"unkeyed-tool:{line_no}:{block_index}"


def extract_tool_calls(events: Iterable[EventRecord], result: AnalysisResult) -> list[ToolCall]:
    calls: "OrderedDict[str, ToolCall]" = OrderedDict()
    for event in events:
        data = event.data
        if str(data.get("type", "")).casefold() != "assistant":
            continue
        message = data.get("message")
        if not isinstance(message, dict):
            continue
        content = message.get("content")
        if not isinstance(content, list):
            continue
        for idx, block in enumerate(content):
            if not isinstance(block, dict) or str(block.get("type", "")).casefold() != "tool_use":
                continue
            name = str(block.get("name", ""))
            key = _tool_key(block, event.line_no, idx)
            if key.startswith("unkeyed-tool:"):
                result.observability_notes.append(
                    f"tool_use:missing_stable_id:line_{event.line_no}:block_{idx}"
                )
            candidate = ToolCall(
                key=key,
                line_no=event.line_no,
                block_index=idx,
                name=name,
                input=block.get("input"),
            )
            existing = calls.get(key)
            if existing is None:
                calls[key] = candidate
            elif existing.name != candidate.name or existing.input != candidate.input:
                result.observability_notes.append(f"tool_use:conflict:{key}")
    result.tool_calls = len(calls)
    result.tool_names = [call.name for call in calls.values()]
    return list(calls.values())


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


def _is_memory_search(name: str) -> bool:
    leaf = _tool_leaf(name)
    explicit = {
        "memory_search",
        "memorysearch",
        "searchmemory",
        "memory_read",
        "readmemory",
        "memorylookup",
        "lookupmemory",
    }
    if leaf in explicit:
        return True
    return "memory" in leaf and any(token in leaf for token in ("search", "read", "lookup", "recall"))


def _skill_input_matches(tool_input: Any, skill_name: str) -> bool:
    if isinstance(tool_input, dict):
        for key in ("skill", "skill_name", "name"):
            value = tool_input.get(key)
            if isinstance(value, str) and value.casefold() == skill_name.casefold():
                return True
    if isinstance(tool_input, str):
        return tool_input.strip().casefold() == skill_name.casefold()
    return False


def _reference_name(path: str, skill_name: str) -> str | None:
    normalized = path.replace("\\", "/")
    lower = normalized.casefold()
    marker = "/references/"
    idx = lower.find(marker)
    if idx == -1:
        if lower.startswith("references/"):
            # Relative paths are not attributed to the skill without stronger evidence.
            return None
        return None
    prefix = lower[:idx]
    if skill_name.casefold() not in prefix:
        return None
    return normalized[idx + len(marker) :]


def classify_observable_actions(
    events: Iterable[EventRecord], calls: Iterable[ToolCall], result: AnalysisResult, skill_name: str
) -> None:
    skill_invoked = False
    reference_names: list[str] = []

    for call in calls:
        leaf = _tool_leaf(call.name)
        if _is_memory_search(call.name):
            result.memory_searches += 1
        if leaf in READ_TOOL_LEAVES:
            result.file_reads += 1
        if leaf in WRITE_TOOL_LEAVES:
            result.file_writes += 1
        if leaf in EDIT_TOOL_LEAVES:
            result.file_edits += 1
        if leaf in ASK_USER_QUESTION_LEAVES:
            result.ask_user_question_calls += 1
        if leaf == "skill" and _skill_input_matches(call.input, skill_name):
            skill_invoked = True
        if leaf in READ_TOOL_LEAVES:
            path = _extract_path(call.input)
            if path:
                reference = _reference_name(path, skill_name)
                if reference is not None:
                    result.skill_reference_reads += 1
                    reference_names.append(reference)

    # Explicit skill-invocation events, if a future/current transcript emits them.
    for event in events:
        event_type = str(event.data.get("type", "")).casefold()
        if event_type in {"skill_invocation", "skill_invoked"} and _string_contains(event.data, skill_name):
            skill_invoked = True

    result.skill_invoked = "true" if skill_invoked else "not_observable"
    result.skill_reference_names = sorted(set(reference_names))



def _nonempty_structured_answers(value: Any) -> bool:
    if isinstance(value, dict):
        return any(v not in (None, "", [], {}, ()) for v in value.values())
    if isinstance(value, list):
        return any(v not in (None, "", [], {}, ()) for v in value)
    if isinstance(value, str):
        return bool(value.strip())
    return value is not None


def classify_ask_user_question_results(
    events: Iterable[EventRecord], calls: Iterable[ToolCall], result: AnalysisResult
) -> None:
    ask_ids = {
        call.key.removeprefix("tool:")
        for call in calls
        if _tool_leaf(call.name) in ASK_USER_QUESTION_LEAVES and call.key.startswith("tool:")
    }
    seen_results: set[str] = set()

    for event in events:
        data = event.data
        if str(data.get("type", "")).casefold() != "user":
            continue
        message = data.get("message")
        if not isinstance(message, dict):
            continue
        content = message.get("content")
        if not isinstance(content, list):
            content = []

        matched_ids: set[str] = set()
        for idx, block in enumerate(content):
            if not isinstance(block, dict) or str(block.get("type", "")).casefold() != "tool_result":
                continue
            tool_use_id = block.get("tool_use_id") or block.get("toolUseId")
            if isinstance(tool_use_id, str) and tool_use_id in ask_ids:
                matched_ids.add(tool_use_id)

        structured = data.get("toolUseResult")
        answers = None
        has_ask_shape = False
        if isinstance(structured, dict):
            has_ask_shape = isinstance(structured.get("questions"), list) or "answers" in structured
            answers = structured.get("answers")

        if matched_ids:
            for tool_id in sorted(matched_ids):
                key = f"tool:{tool_id}"
                if key in seen_results:
                    continue
                seen_results.add(key)
                result.ask_user_question_results += 1
                if _nonempty_structured_answers(answers):
                    result.ask_user_question_answered_results += 1
                elif answers is None:
                    result.observability_notes.append(
                        f"ask_user_question:answer_not_observable:{key}"
                    )
            continue

        # Repli observé dans certains transcripts : toolUseResult structuré mais
        # identifiant du tool non repris. On ne l'utilise que si un AskUserQuestion
        # existe dans le run et que la forme questions/answers est explicite.
        if has_ask_shape and len(ask_ids) == 1:
            fallback_key = f"ask-result:line:{event.line_no}"
            if fallback_key not in seen_results:
                seen_results.add(fallback_key)
                result.ask_user_question_results += 1
                if _nonempty_structured_answers(answers):
                    result.ask_user_question_answered_results += 1
                elif answers is None:
                    result.observability_notes.append(
                        f"ask_user_question:answer_not_observable:line_{event.line_no}"
                    )
        elif has_ask_shape and len(ask_ids) > 1:
            result.observability_notes.append(
                f"ask_user_question:ambiguous_unlinked_result:line_{event.line_no}"
            )

def extract_skill_listing(events: Iterable[EventRecord], result: AnalysisResult, skill_name: str) -> None:
    listings = [event.data for event in events if _event_has_explicit_skill_listing(event.data)]
    if not listings:
        result.skill_listed = "not_observable"
        return
    result.skill_listed = "true" if any(_string_contains(item, skill_name) for item in listings) else "false"


def analyze(
    events: list[EventRecord],
    *,
    run_id: str,
    scenario_id: str,
    condition: str,
    skill_expected: str,
    skill_name: str,
) -> tuple[AnalysisResult, int]:
    result = AnalysisResult(
        run_id=run_id,
        scenario_id=scenario_id,
        condition=condition,
        skill_expected=skill_expected,
    )
    reliable = aggregate_model_usage(events, result)
    calls = extract_tool_calls(events, result)
    classify_observable_actions(events, calls, result, skill_name)
    classify_ask_user_question_results(events, calls, result)
    extract_skill_listing(events, result, skill_name)

    if any(note.startswith("tool_use:conflict:") for note in result.observability_notes):
        reliable = False
    return result, EXIT_OK if reliable else EXIT_UNRELIABLE


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Analyse un transcript JSONL Claude Code pour une campagne de validation comportementale."
    )
    parser.add_argument("trace", type=Path, help="fichier JSONL à analyser")
    parser.add_argument("--run-id", required=True)
    parser.add_argument("--scenario-id", required=True)
    parser.add_argument("--condition", required=True)
    parser.add_argument("--skill-expected", required=True, choices=("yes", "no", "n/a"))
    parser.add_argument(
        "--skill-name",
        required=True,
        help="nom exact du skill dont l’invocation doit être observée",
    )
    parser.add_argument("--output", type=Path)
    parser.add_argument("--pretty", action="store_true")
    return parser


def emit(result: AnalysisResult, *, output: Path | None, pretty: bool) -> None:
    kwargs: dict[str, Any] = {"ensure_ascii": False}
    if pretty:
        kwargs["indent"] = 2
    else:
        kwargs["separators"] = (",", ":")
    payload = json.dumps(result.to_dict(), **kwargs) + "\n"
    if output is None:
        sys.stdout.write(payload)
    else:
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(payload, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        events = read_jsonl(args.trace)
    except JsonlParseError as exc:
        print(f"JSONL invalide — {exc}", file=sys.stderr)
        return EXIT_INVALID_JSONL

    result, code = analyze(
        events,
        run_id=args.run_id,
        scenario_id=args.scenario_id,
        condition=args.condition,
        skill_expected=args.skill_expected,
        skill_name=args.skill_name,
    )
    emit(result, output=args.output, pretty=args.pretty)
    return code


if __name__ == "__main__":
    raise SystemExit(main())
