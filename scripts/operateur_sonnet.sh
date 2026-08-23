#!/usr/bin/env bash
# scripts/operateur_sonnet.sh — couche opérateur aveugle du harnais expérimental.
#
# Rend le jugement d'opérateur que les fiches NOY subordonnent à une appréciation
# ("si l'agent demande une précision..."), là où un runner ne peut trancher.
#
# Il ne score pas. Il ne connaît ni oracle, ni invariant, ni PASS/FAIL, ni
# historique, ni résultat antérieur. Il fait partie du harnais : mêmes modèle,
# effort et prompt avant et après refactorisation.
#
# Usage : operateur_sonnet.sh <racine_run> <kit>
# Sortie : DECISION / MOTIF / REPONSE sur stdout, verbatim conservé dans le run.
set -u

RUN_ROOT="${1:?racine du run manquante}"
KIT="${2:?répertoire du kit manquant}"

REPO="$(cd "$(dirname "$0")/.." && pwd)"
PROMPT="$REPO/validation/v2.1/baseline/prompt_operateur.md"

# --- Paramètre de l'opérateur, figé et distinct de celui du candidat ---------
# Le candidat tourne en effort `medium` (paramètre autoritatif V1/V2). L'opérateur
# tourne en `high` : son jugement borné est plus exigeant que la production testée.
# Ne pas aligner l'un sur l'autre.
OP_MODEL=claude-sonnet-5
OP_EFFORT=high
CLAUDE_BIN=/home/david/.local/share/claude/versions/2.1.241
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

OP="$RUN_ROOT/operateur"
TOURS=$(sed -n 's/^tours=//p' "$KIT/meta.env")
DERNIERE="$RUN_ROOT/verbatim/tour${TOURS}_reponse.txt"

mkdir -p "$OP/config" "$OP/cwd"
chmod 700 "$OP/config"
cp /home/david/.claude/.credentials.json "$OP/config/"
chmod 600 "$OP/config/.credentials.json"

# Le contexte de l'opérateur est assemblé ici, en entier. Son cwd est un
# répertoire vide et tous les outils lui sont interdits : il ne peut donc pas
# atteindre les fiches, les oracles ni le candidat par le système de fichiers.
{
  cat "$PROMPT"
  echo
  echo "# Dossier du scénario"
  echo
  cat "$KIT/dossier_operateur.md"
  echo
  if [ -f "$RUN_ROOT/workspace/persona.md" ]; then
    echo "# Persona en vigueur"; echo; cat "$RUN_ROOT/workspace/persona.md"; echo
  fi
  FIXTURE=$(sed -n 's/^fixture=//p' "$KIT/meta.env")
  if [ -n "$FIXTURE" ] && [ -f "$KIT/fixtures/$FIXTURE" ]; then
    echo "# Fixture initiale — $FIXTURE"; echo '```'
    cat "$KIT/fixtures/$FIXTURE"; echo '```'; echo
  fi
  echo "# Messages déjà envoyés à l'assistant"
  echo
  for n in $(seq 1 "$TOURS"); do
    echo "## Message $n"; echo; cat "$KIT/t$n.txt"; echo
  done
  echo "# Dernière réponse de l'assistant"
  echo
  cat "$DERNIERE"
} > "$OP/contexte.txt"

cd "$OP/cwd" || exit 1
CLAUDE_CONFIG_DIR="$OP/config" "$CLAUDE_BIN" -p \
  --model "$OP_MODEL" --effort "$OP_EFFORT" \
  --disallowed-tools Read Write Edit Bash Glob Grep WebFetch WebSearch Task Skill \
  < "$OP/contexte.txt" > "$OP/verdict_brut.txt" 2> "$OP/stderr.txt"
RC=$?

sed -n 's/^DECISION: *//p' "$OP/verdict_brut.txt" | head -1 > "$OP/decision.txt"
sed -n 's/^MOTIF: *//p'    "$OP/verdict_brut.txt" | head -1 > "$OP/motif.txt"
sed -n '/^REPONSE:/,$p'    "$OP/verdict_brut.txt" | tail -n +2 \
  | sed '/^```$/d' | sed '/./,$!d' > "$OP/reponse.txt"

cat "$OP/verdict_brut.txt"
exit $RC
