# Rapport d'implémentation — préséance et dérogation locale V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** V2.1.0
**Date :** 2026-08-23
**Plan exécuté :** `docs/v2.1/PLAN_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23_CORRIGE.md`
**Statut :** implémentation terminée, **non testée**. Aucun dry-run lancé, aucun commit effectué.

Ce rapport documente ce qui a été fait, pas ce qui reste à décider — les deux points de décision du plan (§15 : choix terminologique, traitement de R1) ont été tranchés dans le sens recommandé par le plan et n'ont pas été rouverts pendant l'implémentation.

---

# 1. Fichiers modifiés

`en_cours/SKILL.md`, `docs/historique_2.1.md`.

Aucun NOY, aucune fixture, aucun oracle, aucune autre référence du noyau n'a été touché — en particulier `en_cours/references/decoupage_pedagogique.md` (porteur du contraste de granularité) et `en_cours/promesse.md` (G02, déjà à jour) sont restés strictement intacts.

---

# 2. Détail par fichier

## `en_cours/SKILL.md` — modification unique

| Emplacement | Règle précédente | Modification effectuée | Raison |
|---|---|---|---|
| l. 120, section « Contrôles avant réponse ou livraison » | « Pour toute contradiction pertinente entre deux références effectivement mobilisées : **ne pas arbitrer silencieusement ; la signaler**. » | Remplacée par un bloc unique de préséance (voir texte ci-dessous), qui conserve le fragment de signalement à l'identique en dernière clause | Combler l'écart entre G02 (`promesse.md`) et le runtime : le skill ne savait que signaler une contradiction, pas la résoudre par un marqueur de dérogation explicite |

**Texte introduit (remplace intégralement la l. 120) :**

> **Préséance entre règles.** Lorsque des règles effectivement mobilisées entrent en conflit, une référence spécialisée dont le périmètre s'applique et qui **signale explicitement déroger** à une règle générale du skill prévaut — pour ce seul périmètre. En l'absence d'une telle dérogation explicite, la règle générale prévaut. Une dérogation locale ne modifie pas la règle générale et ne s'étend à aucun autre périmètre. Si une contradiction pertinente reste non résolue par cette règle : **ne pas arbitrer silencieusement ; la signaler**.

**Lignes explicitement non touchées** (conformément aux contraintes de rédaction du plan §6.1, points 6) :

- l. 26 — « appliquer les conditions exactes de `references/taxonomie.md` §2 sans les réinterpréter ici » ;
- l. 99 — « la référence normative spécialisée fait foi » (identifiée par le plan comme risque principal R1, volontairement non désambiguïsée par anticipation — voir §6).

**Choix terminologique appliqué :** « règle générale du skill », le mot « noyau » étant absent du runtime (vérifié par `grep`, présent seulement dans `promesse.md`, `base_de_travail.md` et les fiches NOY014).

## `docs/historique_2.1.md`

Entrée ajoutée en tête (ordre chronologique inverse), consignant l'implémentation, le choix de `SKILL.md` comme source normative, le choix terminologique, et le statut non testé — conformément au §6.2 du plan.

---

# 3. Contrôles statiques CS-P1 à CS-P8

| # | Contrôle | Résultat | Constat |
|---|---|---|---|
| **CS-P1** | Non-duplication | ✅ PASS | `grep -rn "déroge\|dérogation" en_cours/references/` ne renvoie rien. La règle n'existe que dans `SKILL.md`. |
| **CS-P2** | Absence de gate | ✅ PASS | Le bloc s'ouvre sur une condition (« Lorsque des règles effectivement mobilisées entrent en conflit »), pas sur une instruction. Aucune occurrence de « avant toute décision », « vérifier s'il existe », « rechercher ». |
| **CS-P3** | Clause de signalement préservée | ✅ PASS | Le fragment « ne pas arbitrer silencieusement ; la signaler » est présent à l'identique, en fin de bloc, subordonné à « reste non résolue ». |
| **CS-P4** | Simulation NOY014_1 sur table | ✅ PASS | `mock_sans_derogation.md` ne contient aucun marqueur de dérogation explicite → condition « qui signale explicitement déroger » non remplie → branche « en l'absence d'une telle dérogation explicite, la règle générale prévaut » → `Activité` reste la granularité la plus fine, pas de `Micro-activité` formelle. Condition manquante nommable : absence de signalement explicite. |
| **CS-P5** | Simulation NOY014_2 sur table | ✅ PASS | `mock_avec_derogation.md` contient « Dérogation explicite au noyau : la règle spécialisée ci-dessus déroge, pour ce seul périmètre, à cette règle générale du noyau. » ; le stimulus déclare le périmètre `MOCK-GRANULARITE` applicable → les deux conditions sont réunies → la règle spécialisée prévaut, dans son périmètre → `Micro-activité` appliqué. Le conflit étant résolu par la dérogation, rien ne doit être signalé comme non résolu (cohérent avec l'oracle FAIL de NOY014_2 sur ce point). |
| **CS-P6** | Références compatibles | ✅ PASS | Aucune référence de `activites_type/`, ni `sequence.md`/`seance.md`/`syllabus.md`, n'a été modifiée ou annotée. Ces références ne contredisant aucune règle générale, elles ne sont pas concernées par le mécanisme (condition d'entrée non remplie). |
| **CS-P7** | Contraste intact | ✅ PASS | Vérifié caractère pour caractère : `decoupage_pedagogique.md` l. 69, `activite.md` l. 7, `glossaire.md` l. 35 — identiques à l'état antérieur. |
| **CS-P8** | Portée du diff | ✅ PASS | `git diff --stat` : exactement `en_cours/SKILL.md` (2 lignes) et `docs/historique_2.1.md` (10 lignes). Aucun fichier de `validation/` ni de `references/` dans le diff. |

Les six contraintes de rédaction du plan §6.1 sont respectées : amorce conditionnelle et « effectivement mobilisées » conservées ; fragment de signalement intact ; terme « noyau » absent ; aucun verbe d'obligation de recherche ; bloc unique de 4 phrases sans sous-titre ni liste ; l. 26 et l. 99 non touchées.

---

# 4. Écarts par rapport au plan

Aucun. La modification appliquée correspond exactement à la formulation normative proposée au §7 du plan, sans reformulation ni ajustement.

---

# 5. Ambiguïté rencontrée

Aucune. Le plan livrait un texte normatif prêt à l'emploi (§7) et deux points de décision déjà tranchés avec une recommandation explicite (§15), qui n'ont pas eu besoin d'être réexaminés.

---

# 6. Risques de régression à surveiller au run

- **R1 (principal, non traité préventivement, par décision explicite du plan)** — `SKILL.md` l. 99 (« la référence normative spécialisée fait foi ») pourrait être lue par le modèle comme une préséance générale de toute référence spécialisée, indépendamment d'un marqueur de dérogation. Effet possible : `NOY014_1` en FAIL, avec une lecture conjointe « spécialisée dans les deux cas » suggérant une préférence générale plutôt qu'une préséance conditionnelle. **À vérifier en priorité par le run NOY014_1.** Si le FAIL est reproductible avec ce motif dans le verbatim, la correction (désambiguïsation minimale de la l. 99) devra faire l'objet d'un **cycle séparé**, jamais simultané à un ajustement d'oracle.
- **R2 (effet de gate)** — mitigé par construction (bloc conditionnel, aucun verbe de recherche) ; à confirmer par l'absence de ralentissement ou de sur-vérification sur les scénarios de routage (NOY009, NOY010, NOY011) lors de la non-régression complète.
- **R3 (`mock.md` hors de la liste « Sources de vérité »)** — risque modéré signalé par le plan comme non traité par choix (élargir la liste pour une fixture de test reviendrait à modifier le candidat pour faire passer un test). Observable via le critère de lecture obligatoire déjà intégré à l'oracle de NOY014_1 (bascule en INDÉTERMINÉ si `mock.md` n'est pas lu).
- **R4/R5/R6** — jugés peu probables par le plan ; couverts par la passe de non-régression complète et par CS-P7 (déjà vérifié).

---

# 7. État Git au moment du rapport

```
 M docs/historique_2.1.md
 M en_cours/SKILL.md
?? docs/v2.1/PLAN_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23_CORRIGE.md
?? validation/v2.1/non_regression/CONTROLE_STABILISATION_NOY014.md
?? validation/v2.1/non_regression/NOY014_1.md
?? validation/v2.1/non_regression/NOY014_2.md
?? validation/v2.1/non_regression/mock_avec_derogation.md
?? validation/v2.1/non_regression/mock_sans_derogation.md
```

```
 docs/historique_2.1.md | 10 ++++++++++
 en_cours/SKILL.md      |  2 +-
 2 files changed, 11 insertions(+), 1 deletion(-)
```

Les cinq fichiers non trackés dans `validation/v2.1/non_regression/` ont été copiés lors d'une étape antérieure (non liée à cette implémentation) et restent inchangés.

Aucun commit n'a été créé. Suite prévue par le plan (§12) : revue statique du diff (faite ci-dessus), vérification statique de la règle de granularité, C0, NOY014_1, NOY014_2, smoke tests attestation formateur, puis non-régression complète sur les 16 scénarios — en attente d'autorisation explicite de lancer des dry-runs.
