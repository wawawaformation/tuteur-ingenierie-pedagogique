# Bloc 2 — collecte et archivage du run

Ce bloc s’exécute **après avoir quitté Claude Code avec `exit`**.

Il finalise la collecte du run puis crée une archive ZIP du dossier correspondant.

Les runs sont stockés dans :

```text
/projets/skill/tests/runs/
```

---

## Valeur à adapter

Remplacer :

- `RUN-ID` : identifiant du run à collecter.

Le nom du skill a déjà été enregistré lors du `start` du Bloc 1 ; il n’a pas à être fourni de nouveau pendant `collect`.

---

## Commandes

```bash
python3 /projets/skill/tuteur-ingenierie-pedagogique/validation/collector-kit/collect_run.py collect \
  --run-id RUN-ID \
  --output-root /projets/skill/tests/runs

cd /projets/skill/tests/runs

zip -r RUN-ID.zip RUN-ID
```

---

## Résultat attendu

Après exécution :

```text
/projets/skill/tests/runs/RUN-ID/
```

contient les artefacts du run.

Une archive est également créée :

```text
/projets/skill/tests/runs/RUN-ID.zip
```

Cette archive peut ensuite être :

- conservée comme artefact du run ;
- transmise à un scoreur ;
- intégrée à une archive de campagne ;
- utilisée pour la validation technique ou le scoring ultérieur.

---

## Important

Le Bloc 2 ne doit être exécuté **qu’après la fin du run**.

Il ne modifie pas la réponse produite : il collecte et archive les éléments observés pendant l’exécution.

Le scoring fonctionnel reste séparé de cette étape.
