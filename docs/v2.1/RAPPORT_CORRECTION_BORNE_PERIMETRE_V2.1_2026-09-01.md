# Rapport — Correction de la borne de périmètre (I30 / décision D3)

**Date :** 2026-09-01
**Plan appliqué :** `PLAN_CORRECTION_BORNE_PERIMETRE_V2.1_2026-09-01.md`
**Origine :** FAIL du contrôle « non-extension hors périmètre » (`RAPPORT_CHANTIER_NOY014_V2.1_2026-09-01.md` §3)
**Rôle :** implémenteur strict. Doctrine G02 inchangée — la correction implémente la promesse existante, elle ne la modifie pas.

---

## 1. Modification

Une seule édition, `en_cours/SKILL.md`, section « Périmètre et préséance ». Deux phrases ajoutées après « ne s'étend à aucun autre périmètre » :

> Le périmètre est une condition d'application, pas une étiquette : il est établi par le contexte de travail, jamais par la seule présence de la référence dans le skill. Lorsque le contexte de travail ne relève pas du périmètre déclaré, ou qu'il ne l'établit pas, la règle générale tient.

Rien retiré, rien d'autre modifié. La clause de signalement reste mot pour mot ; l'index des règles dérogeables est inchangé ; aucune référence de `references/` ni `promesse.md` touchée.

---

## 2. Contrôles statiques

- Clause de signalement (« ne pas arbitrer silencieusement ; la signaler ») : 1 occurrence, inchangée.
- CS6 (aucun « fait foi » sur l'axe de préséance) : 0.
- CS9 (aucun gate de dérogation) : OK.

---

## 3. Contrôles ciblés (avant la batterie complète)

| Contrôle | Avant correction | Après correction | Fondement |
|---|---|---|---|
| **NON_EXTENSION** (D3) | FAIL | **PASS** | l'agent cite explicitement la phrase ajoutée : « le fait que la référence soit présente dans le skill ou mentionnée par vous n'établit pas ce périmètre » ; aucune `Micro-activité` introduite |
| **NOY014_2** (branche positive — risque de sur-correction) | PASS | **PASS** | `Micro-activité` toujours appliqué dans le périmètre déclaré — aucune sur-correction |
| NOY014_1 | PASS | PASS | pas de `Micro-activité`, R-GRAN tient |
| Déclaration invalide — sans `perimetre:` | PASS | PASS | aucune dérogation, noyau tient |
| C0-bis | conforme | conforme | comportement inchangé, aucun surcoût de raisonnement |

Aucun incident technique, aucune relance nécessaire au-delà du protocole prévu.

**Complément après commit** : la déclaration invalide « ID absent de l'index » (`mock_derogation_id_invalide.md`) n'avait pas été incluse dans les contrôles ciblés initiaux — oubli signalé et corrigé séparément. Rejouée seule : **PASS**, tranché dès le tour 1 (contre 2 tours lors du chantier §9, avant la correction). L'ID `Z99` étant absent de l'index indépendamment de toute question de périmètre, ce verdict ne dépendait pas de la clause modifiée — confirmé.

**Lecture qualitative du run NON_EXTENSION.** La réponse distingue explicitement « on m'a signalé cette référence » de « la tâche relève de son périmètre » — exactement la confusion qui produisait le FAIL initial. Elle traite au passage la tâche comme un gabarit Brique standard (Consigne → Production), sans y voir matière à créer un niveau structurel supplémentaire.

---

## 4. Batterie complète (contrôle de régression transverse)

15 runs (C0 + NOY001-011, NOY012_1, NOY012_2, NOY013) rejoués en contextes neufs et aveugles.

**Résultat : 14/14 PASS + C0 conforme. Aucun écart par rapport à la baseline officielle** (`RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md`).

**Point de vigilance spécifique à ce cycle** : recherche systématique (`grep -i "dérog\|deroge\|périmètre\|perimetre"`) sur l'ensemble des 15 verbatims. Aucune trace de raisonnement sur une dérogation ou son périmètre — la seule occurrence lexicale (NOY011, « périmètre restreint » dans la description générique du gabarit Brique) est sans rapport avec le mécanisme de préséance. **Aucun surcoût de gate introduit par la correction.**

Aucun incident technique, tous les runs à `rc=0` au premier passage.

---

## 5. Critère de sortie de la correction — satisfait

Les deux conditions posées par le plan sont réunies conjointement :

- `NON_EXTENSION` PASS **et** `NOY014_2` PASS.
- `NOY014_1`, la déclaration invalide et C0-bis restent PASS/conformes.
- 14/14 PASS sur la batterie officielle, C0 conforme, CS9 « OK ».

---

## 6. Conséquence sur les critères de sortie du refactoring (§11 du plan AMENDE_V2)

**Le point 5 des critères de sortie est désormais atteint** : les deux branches de NOY014 sont PASS avec des corps de fixture identiques (seule variable : `deroge_a:`), le contrôle de non-extension (D3) est PASS, les déclarations invalides sont PASS, l'anti-gate est conforme sur l'ensemble de la batterie.

Cela débloque deux décisions, toutes deux à reconsidérer explicitement (aucune n'est prise par ce rapport) :

- **Décision D2 (Lot D)** : le split de `taxonomie.md` peut maintenant être reconsidéré — sa condition de report est levée.
- **V3 tutorat** : le mécanisme dont `tutorat.md` dépendra (§11, dernière ligne du plan AMENDE_V2) est maintenant démontré sur les huit branches testées (sans dérogation, avec dérogation valide, deux déclarations invalides, non-extension, neutre, anti-gate, régression transverse).

`NOY014_1` et `NOY014_2` restent formellement **suspendus** du décompte automatisé de la batterie officielle (le harnais `run_baseline.sh` ne les inclut pas) ; leur statut de non-régression est désormais démontré par ce rapport et celui du chantier §9, pas encore par une exécution automatisée intégrée.
