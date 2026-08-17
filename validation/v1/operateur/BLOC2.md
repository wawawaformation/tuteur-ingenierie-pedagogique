# BLOC 2 — collecte et archivage d'un run V1

Ce bloc s'exécute uniquement après la fin de la trajectoire et après :

```text
exit
```

Aucun scoring comportemental n'est réalisé ici.

## Racine de campagne

```text
/projets/skill/tests/validation_v1_2026-08-17
```

## Valeur à renseigner

```text
RUN_ID
```

Le `RUN_ID` doit être exactement celui utilisé au BLOC 1.

## Collecte

```bash
REPO="/projets/skill/tuteur-ingenierie-pedagogique"
CAMPAIGN="/projets/skill/tests/validation_v1_2026-08-17"

COLLECTOR="$REPO/validation/collector-kit/collect_run.py"
PARSER="$REPO/validation/collector-kit/analyse_jsonl.py"
RUNS_ROOT="$CAMPAIGN/runs"

python3 "$COLLECTOR" collect \
  --run-id "$RUN_ID" \
  --output-root "$RUNS_ROOT" \
  --parser "$PARSER"
```

## Contrôle minimal

```bash
[ -d "$RUNS_ROOT/$RUN_ID" ] || {
  echo "STOP — collecte absente: $RUNS_ROOT/$RUN_ID"
  exit 1
}

echo "COLLECTE PRESENTE: $RUNS_ROOT/$RUN_ID"
```

Ce contrôle est technique uniquement.

## Archivage

```bash
[ ! -e "$RUNS_ROOT/$RUN_ID.zip" ] || {
  echo "STOP — archive déjà présente: $RUNS_ROOT/$RUN_ID.zip"
  exit 1
}

cd "$RUNS_ROOT"

zip -qr "$RUN_ID.zip" "$RUN_ID"

sha256sum "$RUN_ID.zip"
```

## Résultat attendu

```text
/projets/skill/tests/validation_v1_2026-08-17/runs/RUN-ID/
/projets/skill/tests/validation_v1_2026-08-17/runs/RUN-ID.zip
```

## Règles

- aucun scoring au fil de l'eau ;
- aucun rerun parce qu'un résultat paraît défavorable ;
- rerun uniquement en cas d'invalidité technique réelle ;
- un rerun technique est identifié séparément ;
- un rerun technique ne compte pas comme répétition comportementale ;
- le nombre brut de tours humains ne suffit pas à invalider un run.
