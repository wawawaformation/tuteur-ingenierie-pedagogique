# Procédure scoreur aveugle V2

## Mission

Évaluer indépendamment chaque trajectoire uniquement à partir :

- de l'oracle correspondant dans `ORACLES_SCOREUR/` ;
- du transcript anonymisé ;
- des artefacts finaux annexés lorsqu'un scénario utilise un fichier d'état.

## Aveugle

Ne pas chercher à identifier :

- la condition avec/sans skill ;
- la répétition ;
- le run source ;
- le système ayant produit la trajectoire.

Ne pas comparer deux trajectoires pour décider du verdict d'une trajectoire donnée.

## Verdicts autorisés

Exclusivement :

- `PASS`
- `FAIL`
- `INDÉTERMINÉ`

Pas de `PARTIAL`, pas de note, pas de pondération.

## Règles

- Appliquer l'oracle, pas une conception personnelle de la pédagogie.
- Ne pas durcir une exigence absente de l'oracle.
- Une question de l'assistant peut elle-même satisfaire un observable lorsque l'oracle le permet.
- Pour les scénarios multi-tour, juger la trajectoire complète.
- Lorsque l'oracle prend en compte un fichier final, celui-ci est annexé à la trajectoire anonymisée.
- Les problèmes purement techniques ne sont pas transformés en `INDÉTERMINÉ` comportemental si le paquet les a déjà exclus.

## Sortie

Remplir le TSV fourni :

```text
trajectory_id	scenario_id	verdict	justification
```

La justification est courte et fondée sur l'observable décisif.

Après le TSV, produire une synthèse par scénario. Ne comparer aucune condition expérimentale avant désaveuglement.
