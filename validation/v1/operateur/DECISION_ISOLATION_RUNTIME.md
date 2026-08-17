# Décision d'isolation runtime — validation V1

Date : 2026-08-17

## Constat

Le contrôle à blanc de `RUN-001` a détecté des collisions avec des artefacts
historiques déjà présents :

```text
/projets/skill/tests/prompts/RUN-001.txt
/projets/skill/tests/runs/RUN-001/
/projets/skill/tests/runs/RUN-001.zip
```

Les workspaces `RUN-001` des deux conditions étaient libres, mais les prompts,
collectes et archives historiques ne devaient ni être supprimés ni être écrasés.

## Décision

La nouvelle campagne V1 est isolée dans :

```text
/projets/skill/tests/validation_v1_2026-08-17
```

Arborescence :

```text
/projets/skill/tests/validation_v1_2026-08-17/
├── prompts/
├── runs/
├── tests_avec_skill_A/
└── tests_sans_skill_B/
```

## Conséquence

Les identifiants gelés de `RUNS.csv`, notamment `RUN-001`, sont conservés tels
quels.

Seuls les chemins runtime sont déplacés vers la racine isolée de campagne.

Aucun ancien artefact sous `/projets/skill/tests/prompts/` ou
`/projets/skill/tests/runs/` n'est modifié.

Le plan expérimental, les fiches T01–T30 et le candidat `en_cours/` restent
inchangés.
