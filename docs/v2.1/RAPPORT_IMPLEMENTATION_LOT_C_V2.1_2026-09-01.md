# Rapport d'implémentation — LOT C « Relocalisation des règles mal placées » (V2.1)

**Date :** 2026-09-01
**Plan appliqué :** `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, §LOT C (étapes C.1 à C.4)
**Rôle :** implémenteur strict. Aucune doctrine créée ni arbitrée ; aucun oracle, fixture ou kit modifié.
**Référence de non-régression :** `RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md` (14/14 PASS + C0 conforme).

---

## 1. Nature du changement

Deux relocalisations, doctrine inchangée :

1. **Production documentaire (P11).** Les conventions de rédaction d'une fiche (périmètre demandé, niveau de détail par granularité, séparation apprenant/formateur, callouts, réflexe andragogique) vivaient dans `decoupage_pedagogique.md` §4, un fichier dont l'objet est la structure pédagogique (Module/Séquence/Séance/Activité), pas la production documentaire. Elles sont extraites vers un fichier dédié, `production_documentaire.md`.
2. **Dé-duplication A2 ↔ `etat_des_paliers.md` (P10).** `etat_des_paliers.md` re-narrait le seuil de la clause A3 (« s'il y en a plus d'une, l'activité est refusée »), alors qu'il n'en est pas la source. Le seuil est retiré de `etat_des_paliers.md` au profit d'un renvoi vers `taxonomie.md` §2.

---

## 2. Étapes exécutées

| Étape | Fichier | Changement |
|---|---|---|
| C.1 | nouveau `en_cours/references/production_documentaire.md` | Créé avec le contenu prescrit par le plan (périmètre/granularité, niveau de détail, séparation apprenant/formateur, callouts, réflexe andragogique). |
| C.1 | `en_cours/references/decoupage_pedagogique.md` §4 | Remplacé par un renvoi vers `production_documentaire.md`, avec rappel que paliers/preuves/budget de nouveauté restent définis par `taxonomie.md`/`etat_des_paliers.md`. |
| C.1 | `en_cours/SKILL.md` (« Sources de vérité ») | Ligne ajoutée pour `references/production_documentaire.md`. |
| C.2 | `en_cours/references/taxonomie.md` (A2, « Deux conséquences opératoires ») | La conséquence 2 ne redécrit plus le format du tableau ; elle renvoie à `etat_des_paliers.md` pour le format, les règles de tenue et le protocole de persistance. |
| C.2 | `en_cours/references/etat_des_paliers.md` (« Ce que ce tableau sert à calculer ») | Le seuil (« s'il y en a plus d'une, l'activité est refusée ») est retiré ; renvoi explicite : « Le seuil applicable est celui de la clause A3 (`taxonomie.md` §2). » |

**Neutralité sur l'existant (I21) :** conformément à la consigne du plan, la dispersion de l'invariant I21 sur `activite.md` et `quiz.md` n'a **pas** été nettoyée dans ce lot — seule la troisième source (`decoupage_pedagogique.md`) a été déplacée, pas retirée du contenu normatif.

---

## 3. Contrôles statiques

**Contrôle global** (`./scripts/controle_statique_refactoring.sh`) : CS6 = 0 occurrence, CS9 = OK. CS7/CS8 inchangés par rapport à la sortie du lot B, hormis `etat_des_paliers.md` qui passe de 2 à 3 ancrages `taxonomie.md §2` (le renvoi introduit en C.2, conforme à l'attendu).

**Contrôle spécifique du plan :**

```
grep -rn "l'activité est refusée" en_cours/references/
```

**Résultat : aucune occurrence, y compris dans `taxonomie.md`.** L'attendu du plan (« ne doit n'apparaître que dans `taxonomie.md` ») présuppose que la clause A3 y porte cette formulation littérale. Vérification faite : ce n'est pas le cas — A3 est formulée « Une activité évaluée ne mobilise qu'une seule notion non attestée », sans jamais employer l'expression « l'activité est refusée ». Cette phrase n'existait, avant C.2, qu'à l'endroit qui vient d'être dé-dupliqué (`etat_des_paliers.md`) ; elle n'a donc pas de source restante après ce lot.

**Nature de l'écart :** même famille que les trois écarts documentés dans le rapport du Lot A (CS1, CS2, A.3) — une hypothèse du plan sur le texte réel d'un fichier source ne correspond pas au contenu effectif, sans lien avec l'exécution. Aucune décision doctrinale n'a été prise ici : le contenu de A3 n'a pas été modifié pour faire correspondre le grep, conformément à la règle de ne pas retoucher au-delà du périmètre déclaré de l'étape.

---

## 4. Non-régression comportementale (C.3)

4 runs joués en contextes neufs et aveugles (`tmp/run_check.sh`), séquentiellement, contre l'état WIP du candidat après C.1+C.2. Scoring appliqué contre les oracles de `validation/v2.1/non_regression/`.

**Résultat : 3/3 PASS (NOY003, NOY007, NOY010), 0 FAIL, 0 INDÉTERMINÉ, C0 conforme.**

| Scénario | Verdict | Fondement |
|---|---|---|
| C0 | conforme | aucune introduction spontanée de granularité `Micro-activité` sous `Activité` |
| NOY003 | PASS | refus du bloc à nouveautés simultanées, séquençage en activités courtes |
| NOY007 | PASS | aucun barème inventé ; critères, livrables et tests explicites |
| NOY010 | PASS | séparation apprenant/formateur maintenue, solution protégée jusqu'à production |

Aucun incident technique : tous les runs sortis avec `rc=0` au premier essai, aucun rerun nécessaire.

**Note méthodologique.** `validation/v2.1/baseline/kits/C0/dossier_operateur.md`, référencé par le plan comme source de l'attendu C0, n'existe pas dans le dépôt (seuls `meta.env` et `t1.txt` sont présents dans ce kit). L'attendu a été pris à la source réellement autoritative référencée par `meta.env` du kit C0 (`CONTROLE_STABILISATION_NOY014.md` §2). Écart d'instrumentation pré-existant, sans rapport avec ce lot, signalé ici sans correction (hors périmètre C.1-C.4).

Artefacts : `/projets/skill/tests/lotC_checks_2026-09-01/<SCENARIO>/verbatim/`.

Contrôle complémentaire : la règle `R-GRAN` reste présente et référencée de façon cohérente (`SKILL.md`, `promesse.md`, `decoupage_pedagogique.md`) — non affectée par le déplacement des règles de production documentaire.

---

## 5. Écarts et réserves

1. **Contrôle grep du plan non satisfaisable tel quel** (§3 ci-dessus) : la phrase « l'activité est refusée » n'a jamais existé dans `taxonomie.md`. Documenté, non corrigé — hors décision d'implémenteur.
2. **`dossier_operateur.md` du kit C0 absent du dépôt** (§4 ci-dessus) : contournement méthodologique documenté, sans modification du dépôt.

---

## 6. Contrôle de sortie du lot C

> « Aucun comportement conforme de NOY003, NOY007 ou NOY010 dans la baseline ne régresse. »

**Satisfait.** Les 3 comportements restent PASS, C0 reste conforme.
