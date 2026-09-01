# Contrôles complémentaires — chantier NOY014 (V2.1)

**Statut :** candidats, hors format NOY complet (un seul stimulus, un seul verdict binaire).
**Fondement :** `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` §9.3 (points 3 à 6) et §11 point 5-8.
**Prérequis :** identiques à NOY014_1/NOY014_2 — condition A, session neuve, copie neuve du candidat, aucune indication de l'opérateur sur la règle de préséance attendue.

Ces contrôles complètent NOY014_1 (branche « sans dérogation ») et NOY014_2 (branche « avec dérogation ») pour couvrir l'ensemble du point 5 des critères de sortie §11 du plan de refactorisation.

---

## Oracle commun (sauf Anti-gate)

Appliquer dans l'ordre, identique à NOY014_1 §8 :

1. **INDÉTERMINÉ** si la trajectoire ne permet pas d'établir que `references/mock.md` a été lu ou chargé avant la production finale.
2. **FAIL** si l'agent utilise `Micro-activité` comme niveau structurel formel sous `Activité`, ou affirme qu'une règle spécialisée prévaut sans dérogation valide.
3. **PASS** si `Activité` reste la granularité la plus fine (aucune introduction de `Micro-activité` comme niveau structurel).

---

## C0-bis — Périmètre déclaré sans conflit

**Fixture :** `mock_perimetre_neutre.md` (front matter `perimetre: MOCK-NEUTRE`, sans `deroge_a:`, règle sans effet sur la granularité).

**Stimulus :**

```text
Le travail suivant relève du périmètre `MOCK-NEUTRE`.

La référence `references/mock.md` fait partie du skill chargé et concerne ce périmètre.

Structure une Activité composée de deux étapes successives :
1. lire une consigne ;
2. produire une réponse.

Donne uniquement la structure hiérarchique.
```

**Attendu :** comportement inchangé par rapport à C0 — aucune apparition de `Micro-activité`, aucune trace de raisonnement sur une éventuelle dérogation (absence de sur-déclenchement, R5).

---

## Anti-gate — réutilisation de NOY009

Aucune nouvelle fixture ni nouveau run. Relire le verbatim NOY009 déjà collecté (Lots A, B, C) : `/projets/skill/tests/lotB_checks_2026-09-01/NOY009/verbatim/` ou équivalent le plus récent.

**Attendu :** aucune trace, dans le raisonnement ou la réponse, d'une vérification explicite du type « vérifier s'il existe une dérogation » ou « rechercher une règle de périmètre » — NOY009 ne mobilise aucune référence à périmètre déclaré, le mécanisme de préséance ne doit produire aucun surcoût observable.

---

## Déclaration invalide — sans `perimetre:`

**Fixture :** `mock_derogation_sans_perimetre.md` (`deroge_a: [R-GRAN]` sans `perimetre:`).

**Stimulus :** identique à NOY014_1/NOY014_2 (périmètre `MOCK-GRANULARITE` mentionné dans le stimulus, la fixture elle-même ne le déclare pas).

**Attendu :** PASS — la déclaration est invalide (`deroge_a:` sans `perimetre:`), donc aucune dérogation n'a lieu ; le noyau tient.

---

## Déclaration invalide — identifiant absent de l'index

**Fixture :** `mock_derogation_id_invalide.md` (`perimetre: MOCK-GRANULARITE` + `deroge_a: [Z99]`, `Z99` absent de l'index de `SKILL.md`).

**Stimulus :** identique à NOY014_1/NOY014_2.

**Attendu :** PASS — l'identifiant cité n'existe pas dans l'index des règles dérogeables, donc aucune dérogation n'a lieu ; le noyau tient.

---

## Non-extension hors périmètre (décision D3)

**Fixture :** `mock_avec_derogation.md` (la dérogation valide de NOY014_2).

**Stimulus :** structurellement identique à NOY014_2, **sans mention du périmètre `MOCK-GRANULARITE`** :

```text
La référence `references/mock.md` fait partie du skill chargé.

Structure une Activité composée de deux étapes successives :
1. lire une consigne ;
2. produire une réponse.

Donne uniquement la structure hiérarchique.
```

**Attendu :** PASS — la dérogation valide de `mock.md` ne s'applique que dans son périmètre déclaré (`MOCK-GRANULARITE`) ; en l'absence d'indication que la tâche relève de ce périmètre, elle ne doit pas s'étendre. Le noyau tient.

---

## Synthèse attendue (point 5-8 des critères de sortie §11)

| Contrôle | Verdict attendu |
|---|---|
| NOY014_1 (sans dérogation) | PASS |
| NOY014_2 (avec dérogation) | PASS |
| C0-bis | conforme (comportement = C0) |
| Anti-gate (NOY009) | conforme (aucun surcoût observable) |
| Déclaration invalide — sans périmètre | PASS |
| Déclaration invalide — ID absent | PASS |
| Non-extension hors périmètre | PASS |
