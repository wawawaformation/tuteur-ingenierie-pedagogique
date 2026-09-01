# CLAUDE.md — `validation/v2.1/non_regression/`

Ce dossier contient la **batterie de non-régression candidate pour V2.1**, distincte des scénarios NOY autoritatifs de `validation/non_regression/`.

## Statut

Candidat V2.1 — à stabiliser avant gel. Voir `en_cours/base_de_travail.md` (§9) et `en_cours/promesse.md`.

## Numérotation décalée par rapport à `validation/non_regression/`

Ce dossier repart de `NOY001`, alors que `validation/non_regression/` va de `NOY001` à `NOY012`. Le même identifiant ne désigne donc pas le même scénario d'un dossier à l'autre.

| Ici | `validation/non_regression/` | Statut |
|---|---|---|
| NOY001 | NOY002 | repris à l'identique |
| NOY002 | NOY003 | repris à l'identique |
| NOY003 | NOY004 | repris à l'identique |
| NOY004 | NOY005 | repris à l'identique |
| NOY005 | NOY006 | repris à l'identique |
| NOY006 | NOY007 | repris à l'identique |
| NOY007 | NOY008 | repris à l'identique |
| NOY008 | NOY009 | repris à l'identique |
| NOY009 | NOY010 | repris à l'identique |
| NOY010 | NOY011 | repris à l'identique |
| NOY011 | NOY012 | repris à l'identique |
| NOY012_1 | — | nouveau candidat V2.1 (appréciation générale du formateur ≠ attestation explicite d'un palier) |
| NOY012_2 | — | nouveau candidat V2.1 (attestation explicite du formateur = fondement suffisant d'un palier) |
| NOY013 | — | nouveau candidat V2.1 (manque de preuve ≠ preuve de manque) |
| — | NOY001 | volontairement exclu : P01 est sorti du noyau, ne protège plus V2.1 |

`NOY012_1` et `NOY012_2` remplacent un `NOY012` initial à deux tours, scindé après contre-revue : le Tour 2 (attestation explicite) restait exposé à une simple cohérence conversationnelle avec le Tour 1 (appréciation générale). Voir `observation_conclusion_recommandation_dry_run.md` §3.

## Citations et codes d'incident préservés sous l'ancienne numérotation

Certaines mentions internes pointent délibérément vers un artefact externe ou un incident déjà journalisé sous l'**ancien** numéro (celui de `validation/non_regression/`), et ne doivent pas être remappées lors d'une future modification :

- `NOY008.md` cite « plan d'implémentation V2, NOY009 » ;
- `NOY006.md` et `NOY007.md` conservent des codes d'incident `DRY-NOY007-*` / `DRY-NOY008-*`.

## Avant de geler

`NOY012_1`, `NOY012_2` et `NOY013` doivent être stabilisés (au moins un run et une méta-discussion) avant de considérer V2.1 prête pour la non-régression décrite dans `en_cours/base_de_travail.md` §9 (condition A uniquement, une répétition, tout FAIL rejoué ×2 avant diagnostic).

D'après les dry-runs déjà réalisés (`observation_conclusion_recommandation_dry_run.md`) : `NOY012_1` et `NOY013` sont stabilisés et déjà satisfaits par le candidat actuel (PASS). `NOY012_2` est stabilisé mais échoue encore sur le candidat actuel (FAIL) : c'est le comportement que le changement fonctionnel V2.1 (attestation explicite du formateur) doit corriger avant que ce scénario puisse passer.

## NOY014 — suspendu du décompte officiel

`NOY014_1` et `NOY014_2` (préséance entre règles) sont **suspendus** de la batterie de non-régression officielle depuis le Lot 0 (jamais comptés dans les 14/14 PASS des lots 0/A/B/C). Réinstrumentés le 2026-09-01 sur le mécanisme front matter (`perimetre:`/`deroge_a:`) posé au Lot B, avec 5 contrôles complémentaires dans `CONTROLES_COMPLEMENTAIRES_NOY014.md`. Voir `docs/v2.1/PLAN_CHANTIER_NOY014_V2.1_2026-09-01.md`. Réintégration au décompte officiel conditionnée aux points 5-8 des critères de sortie de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` §11.

## Promotion

Ce dossier n'est pas la batterie autoritative. Une promotion vers `validation/non_regression/` doit rester une décision explicite, pas une copie automatique — et devra alors résoudre le décalage de numérotation documenté ci-dessus.
