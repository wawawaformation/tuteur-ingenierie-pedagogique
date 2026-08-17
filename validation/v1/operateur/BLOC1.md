# BLOC 1 — préparation et lancement d'un run V1

## Racine de campagne

```text
/projets/skill/tests/validation_v1_2026-08-17
```

Les artefacts historiques présents ailleurs sous `/projets/skill/tests/` ne doivent
pas être utilisés ni écrasés.

## Principe

Un seul run est préparé et lancé à la fois.

Le run est choisi dans le plan gelé :

```text
validation/v1/plan/RUNS.csv
```

Aucun scoring comportemental n'est effectué pendant l'exécution.

## Paramètres communs

```text
Claude Code      : 2.1.232
binaire          : /home/david/.local/share/claude/versions/2.1.232
modèle           : claude-sonnet-5
effort           : medium
permission mode  : default
auto-update      : désactivé
auto-memory      : désactivée
persona          : aucune
skill            : tuteur-ingenierie-pedagogique
```

## Valeurs du run

Depuis `RUNS.csv`, relever :

- `run_id`
- `test_id`
- `condition`
- `repetition`
- `status`

Correspondance de condition :

```text
avec skill  -> collector: skill    -> skill_expected: yes
sans skill  -> collector: no-skill -> skill_expected: n/a
```

Le `test_id` est transmis au collector comme `scenario-id`.

## Chemins

```bash
REPO="/projets/skill/tuteur-ingenierie-pedagogique"
CAMPAIGN="/projets/skill/tests/validation_v1_2026-08-17"
COLLECTOR="$REPO/validation/collector-kit/collect_run.py"
CLAUDE_BIN="/home/david/.local/share/claude/versions/2.1.232"
```

Le prompt matérialisé est :

```text
/projets/skill/tests/validation_v1_2026-08-17/prompts/RUN-ID.txt
```

Avec skill :

```text
/projets/skill/tests/validation_v1_2026-08-17/tests_avec_skill_A/RUN-ID/
```

Sans skill :

```text
/projets/skill/tests/validation_v1_2026-08-17/tests_sans_skill_B/RUN-ID/
```

## Extraction du prompt exact

Après avoir renseigné `RUN_ID` et `SCENARIO_ID` :

```bash
REPO="/projets/skill/tuteur-ingenierie-pedagogique"
CAMPAIGN="/projets/skill/tests/validation_v1_2026-08-17"

TEST_FILE="$REPO/validation/v1/tests/$SCENARIO_ID.md"
PROMPT_FILE="$CAMPAIGN/prompts/$RUN_ID.txt"

mkdir -p "$CAMPAIGN/prompts"

python3 -c 'from pathlib import Path; import re,sys; s=Path(sys.argv[1]).read_text(encoding="utf-8"); m=re.search(r"(?ms)^#{2,4}[ \t]+Prompt exact[ \t]*\n+```(?:text)?[ \t]*\n(.*?)\n```",s); m or (_ for _ in ()).throw(SystemExit("ERREUR: section Prompt exact introuvable")); Path(sys.argv[2]).write_text(m.group(1).rstrip("\n")+"\n",encoding="utf-8")' "$TEST_FILE" "$PROMPT_FILE"

cat "$PROMPT_FILE"
```

Le contenu affiché doit correspondre exactement au `Prompt exact` de la fiche T.

## A — avec skill

```bash
REPO="/projets/skill/tuteur-ingenierie-pedagogique"
CAMPAIGN="/projets/skill/tests/validation_v1_2026-08-17"
COLLECTOR="$REPO/validation/collector-kit/collect_run.py"
CLAUDE_BIN="/home/david/.local/share/claude/versions/2.1.232"

MODEL_ID="claude-sonnet-5"
EFFORT="medium"
PERMISSION_MODE="default"
SKILL_NAME="tuteur-ingenierie-pedagogique"

PROMPT_FILE="$CAMPAIGN/prompts/$RUN_ID.txt"
RUN_DIR="$CAMPAIGN/tests_avec_skill_A/$RUN_ID"
RUNS_ROOT="$CAMPAIGN/runs"

[ ! -e "$RUN_DIR" ] || { echo "STOP — workspace déjà présent: $RUN_DIR"; exit 1; }
[ ! -e "$RUNS_ROOT/$RUN_ID" ] || { echo "STOP — collecte déjà présente: $RUNS_ROOT/$RUN_ID"; exit 1; }
[ ! -e "$RUNS_ROOT/$RUN_ID.zip" ] || { echo "STOP — archive déjà présente: $RUNS_ROOT/$RUN_ID.zip"; exit 1; }

mkdir -p "$RUN_DIR/.claude/skills"
mkdir -p "$RUNS_ROOT"

cp -a "$REPO/en_cours" "$RUN_DIR/.claude/skills/$SKILL_NAME"

diff -qr "$REPO/en_cours" "$RUN_DIR/.claude/skills/$SKILL_NAME"

export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

cd "$RUN_DIR"

python3 "$COLLECTOR" start \
  --run-id "$RUN_ID" \
  --scenario-id "$SCENARIO_ID" \
  --condition skill \
  --skill-expected yes \
  --skill-name "$SKILL_NAME" \
  --prompt-file "$PROMPT_FILE" \
  --output-root "$RUNS_ROOT"

"$CLAUDE_BIN" \
  --model "$MODEL_ID" \
  --effort "$EFFORT" \
  --permission-mode "$PERMISSION_MODE" \
  "$(cat "$PROMPT_FILE")"
```

## B' — sans skill

```bash
REPO="/projets/skill/tuteur-ingenierie-pedagogique"
CAMPAIGN="/projets/skill/tests/validation_v1_2026-08-17"
COLLECTOR="$REPO/validation/collector-kit/collect_run.py"
CLAUDE_BIN="/home/david/.local/share/claude/versions/2.1.232"

MODEL_ID="claude-sonnet-5"
EFFORT="medium"
PERMISSION_MODE="default"
SKILL_NAME="tuteur-ingenierie-pedagogique"

PROMPT_FILE="$CAMPAIGN/prompts/$RUN_ID.txt"
RUN_DIR="$CAMPAIGN/tests_sans_skill_B/$RUN_ID"
RUNS_ROOT="$CAMPAIGN/runs"

[ ! -e "$RUN_DIR" ] || { echo "STOP — workspace déjà présent: $RUN_DIR"; exit 1; }
[ ! -e "$RUNS_ROOT/$RUN_ID" ] || { echo "STOP — collecte déjà présente: $RUNS_ROOT/$RUN_ID"; exit 1; }
[ ! -e "$RUNS_ROOT/$RUN_ID.zip" ] || { echo "STOP — archive déjà présente: $RUNS_ROOT/$RUN_ID.zip"; exit 1; }

mkdir -p "$RUN_DIR"
mkdir -p "$RUNS_ROOT"

[ ! -e "$RUN_DIR/.claude/skills/$SKILL_NAME" ] || {
  echo "STOP — skill présent dans le workspace sans skill"
  exit 1
}

export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

cd "$RUN_DIR"

python3 "$COLLECTOR" start \
  --run-id "$RUN_ID" \
  --scenario-id "$SCENARIO_ID" \
  --condition no-skill \
  --skill-expected n/a \
  --skill-name "$SKILL_NAME" \
  --prompt-file "$PROMPT_FILE" \
  --output-root "$RUNS_ROOT"

"$CLAUDE_BIN" \
  --model "$MODEL_ID" \
  --effort "$EFFORT" \
  --permission-mode "$PERMISSION_MODE" \
  "$(cat "$PROMPT_FILE")"
```

## Pendant le run

Suivre :

```text
validation/v1/operateur/INTERACTIONS.md
```

Si Claude demande une information pédagogique absente du scénario et non prévue
par la fiche gelée, répondre exactement :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

Ne pas répondre automatiquement à toute question : l'opérateur interprète la
nature de l'interaction.

À la fin :

```text
exit
```

Puis BLOC 2.
