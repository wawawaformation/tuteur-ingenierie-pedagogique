# CLAUDE.md — `validation/`

Ce dossier contient le **dispositif de validation** du skill : scénarios, personas, instrumentation, procédures et archives de campagnes.

## Principe central

La validation doit protéger l'objectif du test, pas une chorégraphie mécanique.

L'opérateur joue les tours gelés et peut adapter les interactions intermédiaires uniquement à partir des informations déjà disponibles lorsque cela est nécessaire pour rendre l'objectif observable, sans :

- souffler l'oracle ;
- inventer une nouvelle information pédagogique ;
- introduire artificiellement un élément qui change ce que le scénario mesure.

Lorsqu'aucune information supplémentaire pertinente n'existe, une réponse neutre du type suivant est appropriée si la procédure l'autorise :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

## Séparer les couches

Toujours distinguer :

```text
conception du scénario
→ exécution / collecte
→ contrôle technique
→ anonymisation
→ scoring
→ adjudication éventuelle
→ désaveuglement
→ répétition conditionnelle éventuelle
→ synthèse
```

Ne pas utiliser un résultat d'une couche future pour modifier rétroactivement une couche déjà gelée.

## Scoring

- Appliquer l'oracle correspondant au `scenario_id`.
- Juger les observables réellement présents.
- Ne pas ajouter une règle implicite plus stricte que l'oracle.
- Ne pas transformer une préférence pédagogique en critère de FAIL.
- Conserver `PASS`, `FAIL`, `INDÉTERMINÉ` lorsque le protocole l'impose.

## Campagnes historiques

Les dossiers `v1/` et `v2/` sont des éléments de traçabilité.

Ne pas les modifier pour refléter le candidat courant. Une nouvelle version doit avoir sa propre campagne ou ses propres artefacts clairement séparés.

## Données lourdes

Les workspaces et traces d'exécution peuvent vivre hors du dépôt lorsque la procédure le prévoit. Le dépôt doit conserver les artefacts pérennes nécessaires à la compréhension, à l'audit et à la reproductibilité.
