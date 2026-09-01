# Plan — Correction de la borne de périmètre (I30 / décision D3)

**Date :** 2026-09-01
**Rôle :** architecte/relecteur. Aucun fichier modifié pendant la rédaction de ce plan.
**Origine :** FAIL du contrôle « non-extension hors périmètre » consigné dans `RAPPORT_CHANTIER_NOY014_V2.1_2026-09-01.md` §3.
**Nature :** implémentation seule — la doctrine G02 n'est pas modifiée.

---

## 1. Diagnostic

Le comportement observé n'est pas une violation de la règle écrite : c'est la résolution, par l'agent, d'un **cas que la règle ne traite pas**.

La section « Périmètre et préséance » de `SKILL.md` couvre aujourd'hui deux cas sur trois :

| Cas | Traité par le texte actuel ? |
|---|---|
| 1. La tâche relève du périmètre déclaré | oui — la dérogation s'applique |
| 2. La tâche relève d'un **autre** périmètre | oui — « ne s'étend à aucun autre périmètre » |
| 3. **Le périmètre de la tâche n'est pas établi** | **non — silence** |

Le cas 3 est de loin le plus fréquent : une tâche ordinaire ne déclare aucun périmètre. Face à ce silence, l'agent a comblé avec l'indice disponible — la seule référence à périmètre présente dans le skill — et a appliqué sa dérogation. Il a même nommé `MOCK-GRANULARITE` dans sa justification alors que le stimulus ne le mentionnait pas.

Autrement dit : le champ `perimetre:` a été lu comme une **étiquette descriptive** de la référence, pas comme une **condition d'application** de sa dérogation.

---

## 2. Pourquoi la correction n'a pas besoin d'un gate

La tentation naturelle serait d'écrire « avant d'appliquer une dérogation, vérifier que la tâche relève du périmètre déclaré ». C'est exclu, et pas seulement par le garde-fou R5 du plan de refactorisation : la promesse elle-même l'interdit.

> G02, `en_cours/promesse.md` : « Ce mécanisme est une règle de résolution de priorité ; **il n'ajoute pas de gate ni de vérification systématique de dérogation**. »

Or le mécanisme comporte déjà une condition d'absence qui, elle, **fonctionne empiriquement** :

> « En l'absence de `deroge_a:`, aucune dérogation n'a lieu : la règle contredite tient. »

Cette formulation a été validée par trois runs du chantier §9 — `NOY014_1`, « déclaration invalide sans périmètre » et « déclaration invalide ID absent » sont tous PASS, et tous reposent exactement sur ce patron « en l'absence de X → la règle générale tient ». Aucun de ces trois runs n'a produit de comportement de gate.

La condition `perimetre:` n'a, elle, aucun défaut symétrique. **La correction consiste donc à donner à la seconde condition le même patron déclaratif que la première**, qui est déjà démontré comme efficace et non gatifiant. Ce n'est pas l'ajout d'une étape, c'est la fermeture d'un cas.

---

## 3. Modification proposée — une seule, dans `en_cours/SKILL.md`

Section « Périmètre et préséance ». Remplacer :

```
Une dérogation déclarée ne vaut que dans son périmètre. Elle ne modifie pas la règle à laquelle elle déroge et ne s'étend à aucun autre périmètre.
```

par :

```
Une dérogation déclarée ne vaut que dans son périmètre. Elle ne modifie pas la règle à laquelle elle déroge et ne s'étend à aucun autre périmètre. Le périmètre est une condition d'application, pas une étiquette : il est établi par le contexte de travail, jamais par la seule présence de la référence dans le skill. Lorsque le contexte de travail ne relève pas du périmètre déclaré, ou qu'il ne l'établit pas, la règle générale tient.
```

Deux phrases ajoutées, rien retiré.

- La première requalifie `perimetre:` : condition, pas étiquette — et nie explicitement l'inférence exacte qui a produit le FAIL (« la référence est chargée, donc elle s'applique »).
- La seconde ferme les cas 2 et 3 avec le même défaut, calqué syntaxiquement sur la règle d'absence de `deroge_a:` qui fonctionne déjà.

Aucun verbe de recherche ou de vérification. Registre strictement descriptif, identique au reste de la section.

**Ce qui n'est pas touché :** la clause de signalement (« ne pas arbitrer silencieusement ; la signaler ») reste mot pour mot ; l'index des règles dérogeables est inchangé ; aucune référence de `references/` n'est modifiée ; `promesse.md` n'est pas modifiée (G02 exige déjà « uniquement dans son périmètre » — la correction implémente la promesse, elle ne la change pas).

---

## 4. Risques

| # | Risque | Gravité | Contrôle |
|---|---|---|---|
| **RA** | **Sur-correction.** L'agent devient réticent à appliquer une dérogation même lorsque le contexte établit bien le périmètre → `NOY014_2` bascule en FAIL. C'est le risque principal : la branche positive est la raison d'être du mécanisme pour V3. | élevée | rerun `NOY014_2`, qui doit rester PASS. Critère d'acceptation dans l'autre sens. |
| **RB** | **Dérive vers le gate.** L'agent se met à narrer un raisonnement de périmètre sur des scénarios ordinaires, ou à chercher des dérogations sans motif. | moyenne | CS9 doit rester « OK » ; C0 et C0-bis conformes ; relecture anti-gate sur `NOY009`. |
| **RC** | **Régression transverse.** `SKILL.md` est chargé à chaque run ; toute modification y est potentiellement transverse. | moyenne | batterie complète des 14 + C0, comme pour le lot B. |

---

## 5. Séquencement

1. Appliquer la modification du §3 (unique édition).
2. Contrôle statique : `./scripts/controle_statique_refactoring.sh` — CS9 « OK », CS6 à 0. Plus `grep -c "ne pas arbitrer silencieusement ; la signaler" en_cours/SKILL.md` → 1.
3. **Contrôles ciblés d'abord**, dans cet ordre, avant toute batterie complète :
   - `NON_EXTENSION` → doit basculer de FAIL à **PASS** (objectif de la correction) ;
   - `NOY014_2` → doit rester **PASS** (risque RA) ;
   - `NOY014_1`, les deux déclarations invalides → doivent rester **PASS** ;
   - `C0-bis` → doit rester conforme (risque RB).

   Si `NON_EXTENSION` ne bascule pas, **ne pas enchaîner** sur la batterie complète : la formulation est à revoir, et une seconde tentative doit être un cycle distinct, pas un ajustement en cours de route.
4. Si les contrôles ciblés sont au vert : batterie complète des 14 + C0 (risque RC).
5. Rapport dans `docs/v2.1/`, mise à jour de `docs/historique_2.1.md`, commit séparé.

---

## 6. Critère de sortie

- `NON_EXTENSION` PASS **et** `NOY014_2` PASS — les deux conjointement, faute de quoi la correction déplace le problème au lieu de le résoudre.
- `NOY014_1` et les deux déclarations invalides restent PASS.
- C0, C0-bis conformes ; CS9 « OK ».
- 14/14 PASS sur la batterie officielle.

Si ces conditions sont réunies, le point 5 des critères de sortie §11 du plan AMENDE_V2 est atteint et `NOY014_1`/`NOY014_2` peuvent être proposés au gel — ce qui débloque à la fois la reconsidération du Lot D (décision D2) et l'implémentation de V3 tutorat.

---

## 7. Ce que ce plan ne fait pas

- Ne modifie pas `promesse.md` (G02 inchangée).
- Ne modifie aucun oracle, fixture ou kit — ceux du chantier §9 viennent d'être gelés et servent ici de mesure.
- Ne touche à aucune référence de `references/`.
- Ne traite pas le Lot D, qui reste une décision séparée.
