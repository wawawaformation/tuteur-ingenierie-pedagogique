# Plan de correction — R1 (`SKILL.md` l. 99)

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** candidat V2.1
**Date :** 2026-08-23
**Déclencheur :** `RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md` — `NOY014_1` en FAIL reproductible 3/3.
**Cycle :** dédié, isolé de la refactorisation du noyau et de tout ajustement d'oracle, conformément à la recommandation de `PLAN_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23_CORRIGE.md` (§R1).

---

## 1. Rappel du diagnostic

`en_cours/SKILL.md` contient deux règles voisines mais sur des axes différents :

- **l. 99** (section « Sources de vérité ») : *« Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, la référence normative spécialisée fait foi. »* — axe **glossaire descriptif → référence normative**.
- **l. 120** (« Contrôles avant réponse ou livraison ») : bloc de préséance G02 — axe **règle générale du skill → référence spécialisée**, conditionné à une dérogation explicitement signalée.

Le dry-run confirme que Claude transpose la formulation de la l. 99 (« la référence normative spécialisée fait foi ») à l'axe de la l. 120, et traite une référence spécialisée applicable comme prioritaire même sans dérogation signalée — allant jusqu'à qualifier a posteriori le mock de « dérogation explicite » pour justifier ce choix.

## 2. Portée de la correction

Strictement `SKILL.md`, l. 99. Aucune autre ligne, aucun NOY, aucune fixture, aucun oracle.

Vérifié par grep : aucun scénario de non-régression existant (`validation/non_regression/`, `validation/v2.1/non_regression/`) ne teste explicitement l'axe glossaire/référence normative de la l. 99 — seul `NOY014` teste l'axe de la l. 120. La correction n'a donc pas de blast radius connu au-delà de `NOY014`.

## 3. Modification proposée

Retirer le tour « fait foi », qui sonne comme un verdict de préséance générale et se prête à la transposition vers l'axe l. 120. Reformuler pour exprimer que la règle comportementale est *portée par* la référence spécialisée plutôt que *tranchée en sa faveur*.

**Texte actuel (l. 99) :**

> Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, la référence normative spécialisée fait foi.

**Texte proposé :**

> Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, c'est la référence normative spécialisée qui porte cette règle, pas le glossaire.

Changement strictement local au lexique (« fait foi » → « porte cette règle »), sans ajout de renvoi croisé vers la l. 120 : un renvoi explicite risquerait d'alourdir la phrase et de recréer, en sens inverse, une lecture en gate (« avant de trancher, vérifier la règle de préséance ci-dessous »), ce que le CS-P2 du cycle précédent proscrit déjà.

## 4. Alternative écartée

Ajouter une clause explicite du type « ce point ne concerne que l'axe glossaire/référence normative, pas la préséance entre règle générale et référence spécialisée définie ci-dessous ». Écartée : plus lourde, introduit une référence croisée dans une section qui n'en avait pas besoin jusqu'ici, et le changement lexical seul (§3) suffit à retirer le mot qui portait l'ambiguïté (« fait foi »).

## 5. Contrôles statiques à effectuer après modification

| # | Contrôle | Méthode |
|---|---|---|
| CS-R1-1 | Portée du diff | `git diff --stat` limité à `en_cours/SKILL.md` (1 ligne) |
| CS-R1-2 | Non-régression lexicale | `grep -n "fait foi" en_cours/SKILL.md` ne doit plus rien renvoyer |
| CS-R1-3 | Simulation NOY014_1 sur table | Avec la nouvelle formulation, plus aucune phrase de `SKILL.md` n'énonce que « la référence spécialisée fait foi » sans condition ; seule l. 120 énonce une condition de préséance (dérogation explicite requise) |
| CS-R1-4 | l. 120 intacte | `git diff` ne touche pas le bloc de préséance G02 |

## 6. Vérification comportementale prévue

Ciblée, pas une non-régression complète (la refactorisation du noyau, cycle suivant, en sera l'occasion) :

1. `NOY014_1` — attendu : PASS (règle générale prévaut, pas de « Micro-activité »).
2. `NOY014_2` — attendu : PASS inchangé (dérogation explicite toujours respectée).

Si `NOY014_1` reste en FAIL avec un motif différent (pas la transposition l. 99 → l. 120), ne pas retoucher `SKILL.md` une seconde fois dans ce même cycle : documenter et redemander arbitrage.

## 7. Non traité par ce cycle

- La refactorisation/allègement du noyau (cycle suivant, cf. `RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md` §6).
- Tout ajustement d'oracle NOY014.
- La non-régression complète des 16 scénarios (prévue après la refactorisation, pas ici).
