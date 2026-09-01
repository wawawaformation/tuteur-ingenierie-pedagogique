# Rapport d'implémentation — LOT D « Split de `taxonomie.md` » (V2.1)

**Date :** 2026-09-01
**Plan appliqué :** `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, §LOT D (étapes D.1 à D.6), décision D2
**Rôle :** implémenteur strict. Aucune doctrine créée ni arbitrée ; aucun oracle, fixture ou kit modifié.
**Préalable :** décision D2 (« reporter jusqu'au point 5 des critères de sortie ») levée par `RAPPORT_CORRECTION_BORNE_PERIMETRE_V2.1_2026-09-01.md`.

---

## 1. Nature du changement

`taxonomie.md` portait deux responsabilités distinctes : une **échelle d'interprétation** (§1, six paliers, verbes, transposition par domaine) et des **invariants noyau** (§2, clauses A1-A4, garde-fous des activités évaluées). P3 demandait de les séparer : l'échelle reste une aide de lecture, les clauses A1-A4 deviennent la seule responsabilité d'un nouveau fichier `activite_evaluee.md`.

`taxonomie.md` ne garde que §1 et pointe vers `activite_evaluee.md` pour les garde-fous. Le contenu de §2 (A1 à A4, justifications, exemples) est déplacé **sans reformulation**.

---

## 2. Écart de périmètre par rapport au plan — signalé avant exécution

Le plan annonçait « 8 renvois répartis sur 7 fichiers ». Mesure réelle avant toute modification : **27 occurrences dans 12 fichiers** (`SKILL.md`, `activite.md`, `andragogie.md`, `etat_des_paliers.md`, `glossaire.md`, `opo.md`, `seance.md`, `sequence.md`, `activites_type/atelier.md`, `activites_type/brique.md`, `activites_type/quiz.md`, `activites_type/recul.md`). Signalé à l'utilisateur avant toute édition ; décision explicite de poursuivre à ce périmètre réel plutôt que de reporter à nouveau.

---

## 3. Étapes exécutées

| Étape | Action |
|---|---|
| D.1 | Création de `en_cours/references/activite_evaluee.md` : clauses A1-A4 avec justifications et exemples, copiées telles quelles depuis l'ancien §2 de `taxonomie.md`. |
| D.2 | `taxonomie.md` réduit au §1 (échelle, verbes, transposition). Pointeur ajouté en tête : « Les garde-fous des activités évaluées (A1 à A4) sont définis dans `activite_evaluee.md`. » Front matter et phrase d'introduction ajustés en conséquence. |
| D.3 | 27 renvois mis à jour dans les 12 fichiers listés en §2, remplaçant `taxonomie.md` §2[, clause Ax] par `activite_evaluee.md`[, clause Ax], sans autre reformulation. |
| D.4 | Contrôle de renvois orphelins (voir §4). |
| D.5 | Non-régression comportementale complète (voir §5). |

**Correction en cours d'exécution.** La première passe de D.2 a modifié l'introduction de `taxonomie.md` sans supprimer le corps du §2 : le contenu des clauses A1-A4 s'est retrouvé dupliqué (présent à la fois dans `taxonomie.md` et le nouveau `activite_evaluee.md`) pendant une partie de l'exécution. Détecté avant tout contrôle ou run via `grep -c "### A1\|### A2\|### A3\|### A4"` sur `taxonomie.md` (résultat 4 au lieu de 0 attendu) et par CS8 (« Budget de nouveauté » compté 7 fois au lieu de 6). Corrigé immédiatement (troncature de `taxonomie.md` à son §1) avant tout run comportemental — aucun contrôle n'a donc été exécuté sur l'état dupliqué.

**Hors périmètre strict de D.1-D.4, corrigé par cohérence directe :** le déplacement de contenu rendait obsolètes des mentions de `taxonomie.md` dans deux fichiers non listés par le plan et non chargés dans le runtime (`en_cours/CLAUDE.md`, `en_cours/README.md` — ni l'un ni l'autre copié par `run_isole.sh`) : l'arborescence documentée (absence de `activite_evaluee.md` et, déjà avant ce lot, de `production_documentaire.md` du Lot C) et la description du rôle de `taxonomie.md` (« règles normatives A1 à A4 », devenu faux). Mis à jour pour éviter qu'une documentation humaine contredise immédiatement le runtime qu'elle décrit.

---

## 4. Contrôle de renvois orphelins (D.4)

```bash
grep -rn "taxonomie.md\` §2" en_cours/        # 0 résultat
grep -rn "activite_evaluee.md" en_cours/ | wc -l   # 28 (27 renvois + 1 pointeur dans taxonomie.md)
```

**0 renvoi orphelin, 28 occurrences de la nouvelle référence, conforme à l'attendu (≥ 8).**

Contrôle statique global (`./scripts/controle_statique_refactoring.sh`) : CS8 (invariants gelés) revenu à l'état attendu après correction de la duplication (« Budget de nouveauté » : 6 occurrences, comme avant le lot). CS9 « OK ». **CS7 (« ancrages taxonomie.md §2 encore valides ») retourne désormais 0 résultat — attendu et non une régression** : ce contrôle datait d'avant l'existence du Lot D et vérifiait que les citations vers `taxonomie.md §2` restaient valides pendant les Lots A-C, qui ne déplaçaient jamais leur cible. Le Lot D déplace délibérément cette cible ; CS7 est de facto remplacé par le contrôle D.4 ci-dessus pour cet axe.

---

## 5. Non-régression comportementale (D.5)

15 runs (C0 + NOY001-011, NOY012_1, NOY012_2, NOY013) joués en contextes neufs et aveugles.

**Résultat : 14/14 PASS, C0 conforme. Aucun écart par rapport à la baseline officielle.**

Vigilance spécifique demandée sur les six scénarios mobilisant le plus directement A1-A4 (NOY001, NOY002, NOY003, NOY005, NOY006, NOY007) : tous confirmés s'appuyer correctement sur le contenu déplacé (budget de nouveauté explicitement nommé et appliqué sur NOY003, distinction déclaration/preuve intacte sur NOY001/NOY006, frontière palier 2/3 respectée sur NOY002, raisonnement notion par notion sur NOY005, absence de notation arbitraire sur NOY007) — aucun signe de perte ou d'affaiblissement du contenu relocalisé.

Une nuance sans effet sur le verdict a été notée sur NOY004 (mécanisme d'alignement porté par un repère formateur plutôt que par le seul jeu de critères apprenant) — consignée pour une revue future si le style de séparation apprenant/formateur évolue, sans lien avec ce lot.

Aucun incident technique, aucun rerun nécessaire.

Artefacts : `/projets/skill/tests/lotD_checks_2026-09-01/<SCENARIO>/verbatim/`.

---

## 6. Écarts et réserves

1. **Ampleur du lot 3,5× supérieure à l'annoncé** (§2) — signalée et actée avant exécution, pas après coup.
2. **Bug de duplication transitoire** (§3) — détecté et corrigé avant tout contrôle ou run ; aucun verdict n'a été rendu sur l'état incorrect.
3. **Deux fichiers hors périmètre déclaré du plan mis à jour par cohérence** (`en_cours/CLAUDE.md`, `en_cours/README.md`) — ni l'un ni l'autre chargés dans le runtime, corrigés uniquement pour éviter une documentation humaine immédiatement fausse.
4. **`en_cours/README.md` contient par ailleurs une mention obsolète non liée à ce lot** (« Le runtime V3 a été restructuré » — même nature que la correction déjà faite sur le `README.md` racine) : non corrigée ici, hors périmètre de ce rapport.

---

## 7. Contrôle de sortie du lot D

- 0 renvoi orphelin, 28 occurrences de la nouvelle référence.
- CS8 conforme à l'état pré-lot, CS9 « OK ».
- 14/14 PASS + C0 conforme sur la batterie officielle, aucune régression.

**Satisfait.**
