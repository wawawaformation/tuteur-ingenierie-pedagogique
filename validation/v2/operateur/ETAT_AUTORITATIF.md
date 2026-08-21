# État autoritatif de la campagne V2 — gelé

## Candidat

Le candidat embarqué est le snapshot fourni dans :

```text
CANDIDATE/en_cours/
```

Il est copié du paquet opérateur V2 précédent, dont la provenance déclarée était le dépôt transmis le 20 août 2026 avec HEAD observé :

```text
97ee00a0623cdbff0ec774a96d3fbd8a45ed6653
```

Cette valeur documente la provenance du snapshot ; elle ne prétend pas être le HEAD actuel du dépôt vivant.

Pendant la campagne, le candidat exécuté est exclusivement le snapshot du paquet gelé.

## Paramètres Claude Code

```text
binaire : /home/david/.local/share/claude/versions/2.1.232
modèle  : claude-sonnet-5
effort  : medium
mode    : default
mémoire : désactivée
update  : désactivé
```

## Batterie

```text
NOY001 → NOY008 : A/B′, 2 répétitions par condition
NOY009 → NOY012 : A uniquement, 2 répétitions
TOTAL            : 40 runs de base
```

## Mesure secondaire

Les compteurs de tokens exposés dans la trace Claude Code sont agrégés par `COLLECTOR_KIT/analyse_jsonl.py` et conservés dans `metrics.json` : entrée, création de cache, lecture de cache, sortie et totaux dérivés.

## Règle de gel

Une fois le paquet explicitement gelé et le premier run lancé : ne modifier ni candidat, ni scénarios, ni oracles, ni personas, ni plan, ni `RUNS.csv`, ni ordre, ni outils de collecte. Un résultat défavorable n'autorise jamais une correction en cours de campagne.

## Mode opérateur autoritatif

Le mode autoritatif d'exécution est désormais le **mode deux blocs** décrit
dans `MODE_OPERATEUR_2_BLOCS.md`.

L'agent opérateur dirige l'opérateur humain ; il n'exécute pas lui-même la
campagne de manière autonome.
