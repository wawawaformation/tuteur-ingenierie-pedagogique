#!/usr/bin/env python3
"""
Contrôle en lecture seule de la présence et de l'exploitabilité des compteurs
de tokens dans les traces JSONL de Claude Code.

Usage:
    python3 controle_usage_tokens_claude_jsonl.py <fichier-ou-dossier>
    python3 controle_usage_tokens_claude_jsonl.py <fichier-ou-dossier> --show-records

Le script :
- ne modifie aucun fichier source ;
- cherche les objets `usage` associés aux messages assistant ;
- déduplique les enregistrements répétés d'un même message API ;
- conserve séparément input/cache_creation/cache_read/output ;
- calcule total_input_tokens et total_tokens ;
- signale explicitement les champs absents.

Codes de sortie :
    0 = compteurs présents et complets
    2 = aucun compteur d'usage trouvé
    3 = erreur de lecture / JSONL invalide
    4 = compteurs trouvés mais incomplets
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable

CORE_FIELDS = (
    "input_tokens",
    "cache_creation_input_tokens",
    "cache_read_input_tokens",
    "output_tokens",
)


@dataclass(frozen=True)
class UsageRecord:
    source: str
    line: int
    message_id: str
    input_tokens: int | None
    cache_creation_input_tokens: int | None
    cache_read_input_tokens: int | None
    output_tokens: int | None

    @property
    def complete(self) -> bool:
        return all(getattr(self, field) is not None for field in CORE_FIELDS)

    @property
    def total_input_tokens(self) -> int | None:
        vals = (
            self.input_tokens,
            self.cache_creation_input_tokens,
            self.cache_read_input_tokens,
        )
        if any(v is None for v in vals):
            return None
        return sum(vals)  # type: ignore[arg-type]

    @property
    def total_tokens(self) -> int | None:
        ti = self.total_input_tokens
        if ti is None or self.output_tokens is None:
            return None
        return ti + self.output_tokens


def iter_jsonl_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    if path.is_dir():
        return sorted(p for p in path.rglob("*.jsonl") if p.is_file())
    raise FileNotFoundError(path)


def as_non_negative_int(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and value >= 0:
        return value
    return None


def find_assistant_usage(obj: Any) -> tuple[str | None, dict[str, Any] | None]:
    """
    Schéma Claude Code attendu :
      {
        "type": "assistant",
        "message": {
          "id": "msg_...",
          "role": "assistant",
          "usage": {...}
        }
      }

    Une petite tolérance est gardée pour les traces où `usage` serait placé
    directement sur l'objet assistant.
    """
    if not isinstance(obj, dict):
        return None, None

    msg = obj.get("message")
    if isinstance(msg, dict):
        role = msg.get("role")
        usage = msg.get("usage")
        if role == "assistant" and isinstance(usage, dict):
            mid = msg.get("id")
            return (str(mid) if mid is not None else None), usage

    if obj.get("type") == "assistant" and isinstance(obj.get("usage"), dict):
        mid = obj.get("message_id") or obj.get("id")
        return (str(mid) if mid is not None else None), obj["usage"]

    return None, None


def load_records(files: Iterable[Path]) -> tuple[list[UsageRecord], list[str]]:
    records: list[UsageRecord] = []
    errors: list[str] = []

    for file in files:
        try:
            fh = file.open("r", encoding="utf-8")
        except OSError as exc:
            errors.append(f"{file}: ouverture impossible: {exc}")
            continue

        with fh:
            for lineno, raw in enumerate(fh, start=1):
                if not raw.strip():
                    continue
                try:
                    obj = json.loads(raw)
                except json.JSONDecodeError as exc:
                    errors.append(
                        f"{file}:{lineno}: JSON invalide "
                        f"(colonne {exc.colno}: {exc.msg})"
                    )
                    continue

                message_id, usage = find_assistant_usage(obj)
                if usage is None:
                    continue

                if not message_id:
                    # Identifiant déterministe local si le message API n'en expose pas.
                    message_id = f"{file}:{lineno}"

                records.append(
                    UsageRecord(
                        source=str(file),
                        line=lineno,
                        message_id=message_id,
                        input_tokens=as_non_negative_int(usage.get("input_tokens")),
                        cache_creation_input_tokens=as_non_negative_int(
                            usage.get("cache_creation_input_tokens")
                        ),
                        cache_read_input_tokens=as_non_negative_int(
                            usage.get("cache_read_input_tokens")
                        ),
                        output_tokens=as_non_negative_int(usage.get("output_tokens")),
                    )
                )

    return records, errors


def deduplicate(records: list[UsageRecord]) -> tuple[list[UsageRecord], list[str]]:
    """
    Claude Code peut matérialiser plusieurs lignes pour un même message API.
    On ne compte qu'une fois un même message_id lorsque les compteurs sont
    identiques.

    Si un même message_id apparaît avec des compteurs différents, on NE tranche
    PAS silencieusement : toutes les variantes sont conservées et une alerte
    est produite.
    """
    by_id: dict[str, list[UsageRecord]] = {}
    for record in records:
        by_id.setdefault(record.message_id, []).append(record)

    unique: list[UsageRecord] = []
    warnings: list[str] = []

    for message_id, group in by_id.items():
        signatures: dict[tuple[Any, ...], UsageRecord] = {}
        for r in group:
            sig = tuple(getattr(r, f) for f in CORE_FIELDS)
            signatures.setdefault(sig, r)

        if len(signatures) == 1:
            unique.append(next(iter(signatures.values())))
        else:
            warnings.append(
                f"message_id={message_id}: {len(signatures)} jeux de compteurs "
                "différents ; aucune déduplication arbitraire appliquée."
            )
            unique.extend(signatures.values())

    return unique, warnings


def fmt(value: int | None) -> str:
    return "INDISPONIBLE" if value is None else str(value)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Vérifie les compteurs de tokens dans des traces JSONL Claude Code."
    )
    parser.add_argument("path", type=Path, help="Fichier JSONL ou dossier à inspecter")
    parser.add_argument(
        "--show-records",
        action="store_true",
        help="Affiche chaque enregistrement d'usage dédupliqué",
    )
    args = parser.parse_args()

    try:
        files = iter_jsonl_files(args.path)
    except FileNotFoundError:
        print(f"ERREUR: chemin introuvable: {args.path}", file=sys.stderr)
        return 3

    if not files:
        print(f"ERREUR: aucun fichier .jsonl trouvé sous {args.path}", file=sys.stderr)
        return 3

    records, errors = load_records(files)
    unique, warnings = deduplicate(records)

    print("=== CONTROLE USAGE TOKENS CLAUDE JSONL ===")
    print(f"chemin={args.path}")
    print(f"jsonl_files={len(files)}")
    print(f"usage_records_raw={len(records)}")
    print(f"usage_records_unique={len(unique)}")

    for warning in warnings:
        print(f"ALERTE: {warning}")

    if errors:
        for error in errors:
            print(f"ERREUR_JSONL: {error}", file=sys.stderr)
        print("TOKEN_CHECK=ERROR")
        return 3

    if not unique:
        print("TOKEN_CHECK=NO_USAGE_FOUND")
        return 2

    incomplete = [r for r in unique if not r.complete]

    sums: dict[str, int] = {field: 0 for field in CORE_FIELDS}
    for r in unique:
        for field in CORE_FIELDS:
            value = getattr(r, field)
            if value is not None:
                sums[field] += value

    total_input = (
        sums["input_tokens"]
        + sums["cache_creation_input_tokens"]
        + sums["cache_read_input_tokens"]
    )
    total = total_input + sums["output_tokens"]

    print(f"input_tokens={sums['input_tokens']}")
    print(f"cache_creation_input_tokens={sums['cache_creation_input_tokens']}")
    print(f"cache_read_input_tokens={sums['cache_read_input_tokens']}")
    print(f"output_tokens={sums['output_tokens']}")
    print(f"total_input_tokens={total_input}")
    print(f"total_tokens={total}")

    if args.show_records:
        print()
        print("=== ENREGISTREMENTS DEDUPLIQUES ===")
        for r in unique:
            print(
                f"{r.message_id} "
                f"source={r.source}:{r.line} "
                f"input={fmt(r.input_tokens)} "
                f"cache_create={fmt(r.cache_creation_input_tokens)} "
                f"cache_read={fmt(r.cache_read_input_tokens)} "
                f"output={fmt(r.output_tokens)} "
                f"total={fmt(r.total_tokens)}"
            )

    if incomplete:
        print()
        print(f"usage_records_incomplete={len(incomplete)}")
        for r in incomplete:
            missing = [f for f in CORE_FIELDS if getattr(r, f) is None]
            print(
                f"INCOMPLET: message_id={r.message_id} "
                f"champs_absents={','.join(missing)}"
            )
        print("TOKEN_CHECK=PARTIAL")
        return 4

    print("TOKEN_CHECK=PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
