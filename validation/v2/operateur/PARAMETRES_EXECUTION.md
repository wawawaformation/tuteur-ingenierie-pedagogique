# Paramètres d'exécution V2

## Racine de campagne recommandée

```text
/projets/skill/tests/validation_v2_40runs_2026-08-21/execution
```

La variable `V2_CAMPAIGN_ROOT` peut la remplacer.

## Claude Code

```text
CLAUDE_BIN=/home/david/.local/share/claude/versions/2.1.232
MODEL_ID=claude-sonnet-5
EFFORT=medium
PERMISSION_MODE=default
DISABLE_AUTOUPDATER=1
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

## Arborescence générée

```text
validation_v2_2026-08-21/
├── workspaces/
├── prompts/
├── runs/
├── scoring/
└── private/
```

## Conditions

Condition A : le snapshot `CANDIDATE/en_cours/` est copié dans `workspace/.claude/skills/tuteur-ingenierie-pedagogique/`.

Condition B′ : aucun skill `tuteur-ingenierie-pedagogique` n'est présent dans le workspace.

## Persona

Lorsqu'une persona est indiquée, elle est copiée dans `workspace/persona.md` et injectée via `--append-system-prompt-file`.

## Collecte et tokens

Le collector snapshot du paquet est utilisé. `metrics.json` conserve notamment :

```text
input_tokens
cache_creation_input_tokens
cache_read_input_tokens
output_tokens
total_input_tokens
total_tokens
thinking_tokens (si observable)
```

Les fixtures finales `etat_des_paliers/*.md` sont ajoutées aux artefacts du run lorsque le scénario les utilise.

Si Claude Code n'expose pas l'usage pour une trajectoire, `token_usage_observable=false` et les totaux dérivés sont `null` : aucun zéro artificiel n'est interprété comme une consommation réelle.
