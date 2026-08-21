# Validation V2 — dossier pérenne

Ce dossier rassemble les artefacts durables de la campagne de validation expérimentale V2 du skill `tuteur-ingenierie-pedagogique`.

Il ne remplace pas le dossier d'exécution/audit complet conservé sous `tests/validation_v2_40runs_2026-08-21/`.

## Organisation

- `RAPPORT_FINAL_VALIDATION_V2_2026-08-21.md` — rapport final de campagne.
- `FICHE_SYNTHESE_UTILITE_COUT_V2_2026-08-21.md` — lecture pratique utilité / limites / apport / coût.
- `plan/` — paramètres gelés utiles à la reproductibilité (le `PLAN_EXPERIMENTAL.md` déjà présent dans le dépôt est conservé séparément).
- `operateur/` — règles d'exécution du paquet opérateur final à deux blocs.
- `paquet-operateur/` — archive du paquet opérateur gelé final.
- `scoring/` — procédure, résultats des deux scoreurs, comparaison, adjudication, désaveuglement et R3.
- `mesures/` — métriques secondaires de tokens.
- `archives/collectes/` — archive gelée des 40 collectes de base.
- `specification/` — snapshot de la promesse fonctionnelle du candidat testé.
- `tests/` — pointeurs vers les scénarios NOY autoritatifs du dépôt ; les scénarios ne sont pas dupliqués ici.
- `manifest/` — empreintes du paquet de capitalisation.

## Source de vérité des scénarios

Les scénarios `NOY001` à `NOY012` restent dans `validation/non_regression/` afin d'éviter deux copies éditables concurrentes.

## R3

Les trois R3 officiels sont consignés dans `scoring/r3/`. Les traces d'exécution détaillées des R3 restent dans le dossier de campagne sous `tests/` et ne sont pas dupliquées ici.

## Principe de conservation

`validation/v2/` est le dossier de référence lisible et durable. Les traces lourdes et workspaces d'exécution restent dans le dossier `tests/` de la campagne.
