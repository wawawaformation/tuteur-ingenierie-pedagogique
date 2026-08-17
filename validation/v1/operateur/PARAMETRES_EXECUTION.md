# Paramètres d'exécution — validation V1

## Racine de campagne

La campagne courante est isolée dans :

```text
/projets/skill/tests/validation_v1_2026-08-17
```

Cette racine a été créée afin d'éviter toute collision avec les artefacts historiques
déjà présents sous `/projets/skill/tests/`.

Les anciens prompts, collectes et ZIP ne sont ni supprimés ni écrasés.

## Corpus

Tests historiques gelés :

```text
T01 à T30
```

## Conditions

Deux conditions :

- avec skill ;
- sans skill.

## Personas

Aucune fiche T01–T30 ne référence explicitement de persona.

Décision :

```text
persona injectée = aucune
```

Les fichiers présents dans `validation/personas/` sont conservés comme ressources
historiques mais ne sont pas injectés dans les runs de cette campagne.

Le contexte pédagogique d'un run provient uniquement du prompt exact du test
historique concerné.

## Paramètres Claude Code

Configuration commune aux deux conditions :

```text
Claude Code      : 2.1.232
binaire          : /home/david/.local/share/claude/versions/2.1.232
modèle           : claude-sonnet-5
effort           : medium
permission mode  : default
auto-update      : désactivé
auto-memory      : désactivée
```

Variables :

```bash
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

## Workspaces

Chaque run utilise un workspace neuf.

Avec skill :

```text
/projets/skill/tests/validation_v1_2026-08-17/tests_avec_skill_A/RUN-ID/
```

Le candidat gelé `en_cours/` est copié dans :

```text
.claude/skills/tuteur-ingenierie-pedagogique/
```

Sans skill :

```text
/projets/skill/tests/validation_v1_2026-08-17/tests_sans_skill_B/RUN-ID/
```

Aucun skill n'est installé dans ce workspace.

## Prompts

Les prompts matérialisés sont stockés dans :

```text
/projets/skill/tests/validation_v1_2026-08-17/prompts/
```

Pour un run :

```text
/projets/skill/tests/validation_v1_2026-08-17/prompts/RUN-ID.txt
```

Le prompt envoyé à Claude est extrait de la section `Prompt exact` de la fiche
Txx gelée.

Le même prompt est utilisé dans les deux conditions et dans les répétitions du
même test.

Aucune persona ni instruction pédagogique supplémentaire n'est ajoutée.

## Collecte

Les artefacts de campagne sont stockés dans :

```text
/projets/skill/tests/validation_v1_2026-08-17/runs/
```

Pour un run :

```text
/projets/skill/tests/validation_v1_2026-08-17/runs/RUN-ID/
/projets/skill/tests/validation_v1_2026-08-17/runs/RUN-ID.zip
```

## Collector

Collector utilisé :

```text
validation/collector-kit/collect_run.py
validation/collector-kit/analyse_jsonl.py
```

État de référence :

```text
51 tests unitaires exécutés
51 tests réussis
```

## Exécution

Chaque run suit la mécanique opérateur :

```text
BLOC 1
→ interaction avec Claude
→ exit
→ BLOC 2
```

Aucun scoring comportemental n'est réalisé pendant l'exécution.
