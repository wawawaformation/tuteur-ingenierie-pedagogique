# CLAUDE.md — `validation/v3.1/non_regression/`

Ce dossier contient la **batterie de non-régression candidate pour la mineure V3.1.0** (chantier 1 — catalogue d'activités), distincte des scénarios NOY autoritatifs de `validation/non_regression/` et des scénarios candidats V2.1 de `validation/v2.1/non_regression/`.

## Statut

Sept scénarios candidats créés. Cinq ont été joués une fois en aveugle, de façon exploratoire (voir `docs/historique_3.md`) ; `V31-ACT01-3` et `V31-ACT02-4` (ajouts les plus récents) ne l'ont pas encore été. Voir `README.md` pour la batterie, `en_cours/base_de_travail.md` (§9, §13) et `en_cours/promesse.md` (V3.1.0, propriétés ACT01–02).

Aucun run n'est possible en l'état : les gabarits visés sont encore des brouillons dans `plus_tard/`. Les trois prérequis bloquants (énumération du catalogue, noms de champs du front matter dans `SKILL.md`, homogénéité du schéma) sont documentés dans `README.md`, section « Prérequis d'exécution ».

## Numérotation

Numérotation propre à ce dossier, **distincte de la convention `NOY00x`** de `validation/non_regression/` et `validation/v2.1/non_regression/` : les identifiants sont de la forme `V31-<propriété>-<n>` (`V31-ACT01-1`, `V31-ACT02-3`…).

Motif de l'écart : `base_de_travail.md` §9 exige que chaque scénario soit « directement relié à une propriété de promesse ». L'identifiant porte donc ce lien, au lieu d'un numéro séquentiel opaque nécessitant une table de correspondance.

Conséquence si ces scénarios sont un jour promus vers `validation/non_regression/` : la conversion vers la numérotation `NOY` devra être explicite et documentée, comme l'est déjà le décalage de `validation/v2.1/non_regression/`.

## Non-régression cumulative

Le gel de V3.1.0 rejoue, en une seule passe (`base_de_travail.md` §13.1–§13.2) :

- les 15 scénarios de la baseline V2.1 (`validation/v2.1/non_regression/`) ;
- les scénarios propres à ce dossier, une fois créés.

Un FAIL déclenche des reprises ciblées sur le scénario concerné, pas un retour à deux passes complètes.

## Avant de geler

Les scénarios discriminants pour ACT01–02 sont créés mais **non stabilisés** : aucun n'a encore été joué sur le catalogue réel. La promesse V3.1.0 reste non gelée jusqu'à ce que les runs aient permis de confirmer, retirer ou ajuster les propriétés (`base_de_travail.md` §9 et §15).

Point de vigilance issu de la rédaction : `V31-ACT01-1` est le scénario le plus faible de la batterie (quasi tautologique une fois le catalogue en place). La charge de preuve repose sur `V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3`, `V31-ACT02-4` et la paire `V31-ACT02-1`/`V31-ACT02-2`.

**Exigence de répétition, distincte de la règle de passe unique ci-dessus.** `V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3` et `V31-ACT02-4` protègent une propriété de **fiabilité** (`promesse.md`, tête du Chantier 1), pas seulement de capacité : chacun doit être rejoué trois fois (même stimulus, workspace neuf, majorité stable) avant de conclure à leur validité — un `PASS` isolé ne suffit pas. Cette exigence porte sur l'établissement initial de la propriété, avant qu'elle rejoigne la batterie de gel ci-dessus, qui elle ne sera rejouée qu'une fois.

## Promotion

Ce dossier n'est pas une batterie autoritative. Une promotion vers `validation/non_regression/` reste une décision explicite séparée.
