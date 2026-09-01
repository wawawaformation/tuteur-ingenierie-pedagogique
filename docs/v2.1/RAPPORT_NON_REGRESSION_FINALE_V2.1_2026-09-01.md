# Rapport — Non-régression finale du candidat V2.1 (gel, §9 de `base_de_travail.md`)

**Date :** 2026-09-01
**Fondement :** `en_cours/base_de_travail.md` §9 — « Quand V2.1 est prête, on gèle le candidat et on rejoue les tests de noyau. Condition A uniquement, une répétition par scénario, seulement les NOY qui protègent encore des règles du noyau V2.1. »
**Distinct des vérifications de lot** (Lots A-D, chantier §9-NOY014, correction de périmètre) : celles-ci validaient chaque changement individuellement, avec un run par scénario. Cette passe est la validation finale du candidat dans son ensemble, avec répétition systématique, sur un candidat strictement gelé.

---

## 1. Candidat gelé

`en_cours/` vérifié propre (`git status --short -- en_cours/` vide) avant le lancement de chacune des deux passes. HEAD constant : `7020ec3` (dernier commit du Lot D).

Un incident sans lien avec la campagne a interrompu la fenêtre entre les deux passes : des fichiers non suivis (`en_cours/v2.1.zip`, `en_cours/v2.1/`) sont apparus suite à une manipulation manuelle de l'utilisateur en dehors de cette session. Le lancement de la passe 2 a été bloqué par le garde-fou de propreté de `run_baseline.sh` — comportement attendu, aucun run n'a démarré sur un candidat non conforme. Confirmé et nettoyé par l'utilisateur ; `en_cours/` revenu strictement identique à `7020ec3` avant la passe 2.

---

## 2. Méthode

- Harnais officiel `scripts/run_baseline.sh` (recette figée `run_isole.sh`), pas l'outil `tmp/run_check.sh` utilisé pour les vérifications intra-lot.
- **Condition A uniquement**, 15 scénarios (C0 + NOY001-011, NOY012_1, NOY012_2, NOY013). NOY014_1/NOY014_2 hors périmètre (harnais séparé, déjà couverts par le chantier §9 et la correction de périmètre).
- **Deux passes complètes et indépendantes** : `BASELINE_ROOT=.../gel_v2.1_2026-09-01_run1` puis `.../gel_v2.1_2026-09-01_run2`, chacune une exécution neuve et aveugle des 15 scénarios.
- Scoring appliqué exactement contre les oracles de `validation/v2.1/non_regression/` pour chaque passe, indépendamment.
- Règle de reproductibilité : un FAIL sur au moins une des deux passes aurait déclenché deux reprises supplémentaires du scénario concerné (règle du §9 « Si un test A échoue »), sans moyenne ni vote — non déclenchée ici, aucun FAIL sur aucune passe.

---

## 3. Résultat

| Scénario | Passe 1 | Passe 2 | Reproductible |
|---|---|---|---|
| C0 | conforme | conforme | oui |
| NOY001 | PASS | PASS | oui |
| NOY002 | PASS | PASS | oui |
| NOY003 | PASS | PASS | oui |
| NOY004 | PASS | PASS | oui |
| NOY005 | PASS | PASS | oui |
| NOY006 | PASS | PASS | oui |
| NOY007 | PASS | PASS | oui |
| NOY008 | PASS | PASS | oui |
| NOY009 | PASS | PASS | oui |
| NOY010 | PASS | PASS | oui |
| NOY011 | PASS | PASS | oui |
| NOY012_1 | PASS | PASS | oui |
| NOY012_2 | PASS | PASS | oui |
| NOY013 | PASS | PASS | oui |

**14/14 scénarios reproductibles PASS/PASS, C0 conforme sur les deux passes, 0 discordance.** Aucun scénario n'a nécessité de reprise supplémentaire.

Conforme à `RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md` et à l'ensemble des rapports de lot (A, B, C, D, chantier NOY014, correction de périmètre) : aucune régression n'a été introduite par le refactoring, du début à la fin.

---

## 4. Incident NOY009 (passe 1)

Le candidat a posé 5 questions de précision avant toute production, faisant tomber le run sur `AMBIGU_OPERATEUR`. Résolu par `relance_operateur.sh` avec le texte neutre pré-rédigé du kit — identique à celui explicitement autorisé par l'oracle NOY009, aucune information nouvelle introduite. Le verdict PASS repose de toute façon sur l'affirmation explicite produite *avant* la demande de précision, conformément à la clause de notation de la fiche. En passe 2, la même situation s'est résolue automatiquement (relance neutre standard) sans arbitrage.

---

## 5. Conclusion

Le noyau V2.1 satisfait la passe de non-régression finale décrite par `base_de_travail.md` §9. Combiné aux critères de sortie du refactoring (§11 de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, tous satisfaits), la construction de V2.1 telle que décrite en §8 est complète :

- §8.1 Version V2.1.0 ✓
- §8.2 Repartir de V2, fichiers de référence récupérés ✓
- §8.3 P01 sorti du noyau ✓
- §8.4 Attestation explicite du formateur intégrée ✓
- §8.5 Noyau allégé, règle de préséance posée ✓
- §9 Non-régression finale à répétition, candidat gelé ✓

**Ce que ce rapport ne fait pas :** il ne constitue pas une décision de promotion vers `dist/stable/`. Cette promotion reste, par les règles du projet, une décision explicite séparée, avec son propre contrôle de copie et sa propre traçabilité.

Artefacts complets : `/projets/skill/tests/gel_v2.1_2026-09-01_run1/` et `/projets/skill/tests/gel_v2.1_2026-09-01_run2/`.
