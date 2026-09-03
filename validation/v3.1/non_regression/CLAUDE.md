# CLAUDE.md — `validation/v3.1/non_regression/`

Ce dossier contient la **batterie de non-régression candidate pour la mineure V3.1.0** (chantier 1 — catalogue d'activités), distincte des scénarios NOY autoritatifs de `validation/non_regression/` et des scénarios candidats V2.1 de `validation/v2.1/non_regression/`.

## Statut

**Sept scénarios candidats, tous joués et validés — promesse gelée le 2026-09-03.** 15 exécutions au total (1 par scénario simple, 3 par scénario « charge de preuve »), **15/15 PASS**. Détail en `## Avant de geler` ci-dessous. Voir `README.md` pour la batterie, `en_cours/base_de_travail.md` (§9, §13) et `en_cours/promesse.md` (V3.1.0, propriétés ACT01–02, section « Statut de cette promesse »).

**Méthode des runs** : les gabarits candidats n'étant pas encore intégrés au candidat versionné, les runs ont été joués sur une **copie isolée** (`en_cours/` dupliqué dans un répertoire de test, gabarits candidats de `plus_tard/` ajoutés, `activite.md` et `SKILL.md` patchés localement pour le référencement) — voie (a) documentée dans `README.md`, candidat versionné non modifié. Exécutants : sous-agents vierges, sans accès à cette conversation ni aux oracles, restreints au seul répertoire de test.

Le candidat versionné (`en_cours/references/`, `en_cours/SKILL.md`) n'implémente toujours pas le catalogue enrichi : les prérequis bloquants (énumération du catalogue, noms de champs du front matter, homogénéité du schéma) documentés dans `README.md` restent à appliquer avant tout run sur le vrai candidat.

## Numérotation

Numérotation propre à ce dossier, **distincte de la convention `NOY00x`** de `validation/non_regression/` et `validation/v2.1/non_regression/` : les identifiants sont de la forme `V31-<propriété>-<n>` (`V31-ACT01-1`, `V31-ACT02-3`…).

Motif de l'écart : `base_de_travail.md` §9 exige que chaque scénario soit « directement relié à une propriété de promesse ». L'identifiant porte donc ce lien, au lieu d'un numéro séquentiel opaque nécessitant une table de correspondance.

Conséquence si ces scénarios sont un jour promus vers `validation/non_regression/` : la conversion vers la numérotation `NOY` devra être explicite et documentée, comme l'est déjà le décalage de `validation/v2.1/non_regression/`.

## Non-régression cumulative

Le gel de V3.1.0 rejoue, en une seule passe (`base_de_travail.md` §13.1–§13.2) :

- les 15 scénarios de la baseline V2.1 (`validation/v2.1/non_regression/`) ;
- les scénarios propres à ce dossier, une fois créés.

Un FAIL déclenche des reprises ciblées sur le scénario concerné, pas un retour à deux passes complètes.

## Avant de geler — fait, résultats

| Scénario | Runs | Verdict | Type retenu (constant) |
|---|---|---|---|
| `V31-ACT01-1` | 1/1 | PASS | Facettes |
| `V31-ACT01-2` | 3/3 | PASS | Quiz |
| `V31-ACT01-3` | 3/3 | PASS | Planche météo |
| `V31-ACT02-1` | 1/1 | PASS | Étude de cas |
| `V31-ACT02-2` | 1/1 | PASS | Simulation / mise en situation |
| `V31-ACT02-3` | 3/3 | PASS | Brique |
| `V31-ACT02-4` | 3/3 | PASS | Rétrospective |

**15/15 PASS.** Les quatre scénarios « charge de preuve » (`V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3`, `V31-ACT02-4`) sont unanimes sur leurs trois exécutions — la propriété de fiabilité qu'ils protègent est établie, pas seulement observée une fois. Aucune propriété n'a nécessité d'ajustement ou de retrait. Promesse gelée en conséquence (`promesse.md`, « Statut de cette promesse »).

Point qui reste vrai malgré ces résultats : `V31-ACT01-1` demeure le scénario le moins discriminant de la batterie (un seul run, propriété quasi tautologique une fois le catalogue en place) — son `PASS` confirme l'absence de régression, il ne porte pas la charge de preuve.

## Promotion

Ce dossier n'est pas une batterie autoritative. Une promotion vers `validation/non_regression/` reste une décision explicite séparée.
