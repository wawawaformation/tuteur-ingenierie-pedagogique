# Statut du paquet — GELÉ

**Date de gel : 2026-08-21**

Le paquet opérateur de validation V2 est gelé après préflight complet.

## Périmètre gelé

Sont désormais figés :

- le candidat `CANDIDATE/en_cours/` ;
- les scénarios `NOY001` à `NOY012` ;
- les prompts exacts ;
- les personas et fixtures ;
- les oracles ;
- `RUNS.csv` et la randomisation ;
- le régime expérimental des 40 runs ;
- les règles de répétition et de rerun ;
- le collector et les outils opérateur ;
- la collecte des métriques de tokens ;
- les paramètres d'exécution Claude Code.

Toute modification de l'un de ces éléments constitue une rupture de gel à documenter explicitement.

## Campagne

```text
NOY001 à NOY008 : avec skill / sans skill × 2 répétitions = 32 runs
NOY009 à NOY012 : avec skill uniquement × 2 répétitions = 8 runs

TOTAL = 40 runs de base
```

Les éventuels R3 sont conditionnels et ne font pas partie des 40 runs de base.

## Préflight

Le préflight effectué avant gel a confirmé notamment :

```text
candidat SHA-256          PASS
40 runs                   PASS
32 A/B′ + 8 A-only        PASS
12 scénarios NOY          PASS
20 cellules R3 prévues    PASS
prompts/configuration     PASS
ancienne famille DIFF-P   absente
compilation Python        PASS
collector                 51/51 tests PASS
Claude Code               2.1.232
ancien chemin campagne    absent
collision campagne        absente
usage tokens réel         PASS
```

La trace Claude Code utilisée pour confirmer l'observabilité des tokens
exposait bien :

```text
input_tokens
cache_creation_input_tokens
cache_read_input_tokens
output_tokens
```

Cette vérification ne constitue pas un run de la campagne.

## Autorisation d'exécution

Le paquet est **gelé**, mais le gel et le lancement sont deux décisions
distinctes.

Aucun run officiel ne doit être exécuté avant autorisation explicite de
l'opérateur humain.

Une fois l'exécution autorisée, le paquet ne doit plus être modifié pendant
la campagne.

## Ajustement opérateur avant exécution — mode deux blocs

Avant tout run officiel, le mode de pilotage opérateur a été remplacé par un
mode conversationnel à deux blocs : l'agent opérateur fournit les commandes à
l'opérateur humain, qui garde la main sur le terminal.

Cet ajustement ne modifie pas :

- le candidat ;
- les douze scénarios ;
- les prompts expérimentaux ;
- les personas ou fixtures ;
- les oracles ;
- les 40 cellules de `RUNS.csv` ;
- la randomisation ;
- les règles de répétition ;
- la logique de scoring.

Il modifie uniquement la couche d'exploitation opérateur et ajoute l'option
`--launch` à `OUTILS/prepare_run.py` afin que le BLOC 1 réalise réellement la
préparation et le lancement dans un seul copier-coller.

Aucun run officiel n'avait été lancé avant cet ajustement.
