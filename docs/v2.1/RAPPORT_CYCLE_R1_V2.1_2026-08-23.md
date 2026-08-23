# Rapport — cycle correctif R1 (NOY014_1)

**Projet :** `tuteur-ingenierie-pedagogique`
**Version :** candidat V2.1
**Date :** 2026-08-23
**Plan de référence :** `docs/v2.1/PLAN_CORRECTION_R1_V2.1_2026-08-23.md`
**Statut :** **correctif appliqué, INVALIDÉ par le rerun, puis reverté sur décision de l'utilisateur.** NOY014_1 reste en FAIL. `en_cours/SKILL.md` est revenu à son état du commit `01e9ca1`. Le cycle correctif dédié est clos sans modification du noyau ; la préséance est renvoyée à la refactorisation générale.

---

# 1. Verdict sur la validité du scénario NOY014

Verdict initial (avant runs) : **A — scénario sain**. Verdict révisé après collecte de preuves : **mixte, dominé par un défaut d'instrument**.

| Élément | Verdict | Constat |
|---|---|---|
| Oracle NOY014_1 | **Sain** | Conforme à G02 (`promesse.md` l. 148-171). Les conditions de FAIL (§8 étape 2) correspondent exactement à la doctrine décidée. Aucune règle implicite plus stricte que la doctrine. |
| Stimulus | **Sain, mais non discriminant** | Strictement identique entre `_1` et `_2` (confirmé par lecture). Une constante partagée ne peut pas expliquer un résultat différentiel. Il instancie verbatim l'antécédent de la règle du mock (« plusieurs étapes successives »), mais c'est la prémisse nécessaire du test : sans applicabilité, pas de conflit à résoudre. |
| Overlay / chargement | **Sain** | SHA-256 des fixtures vérifiés, pas d'inversion d'overlay (`sans` = 0 marqueur, `avec` = 1), noyaux des copies identiques à `en_cours/` hors `mock.md`. |
| `mock_avec_derogation.md` | **Sain** | Marqueur explicite et discriminant présent. |
| Attendu `Activité → étapes` | **Sain** | La règle générale existe réellement : `references/decoupage_pedagogique.md` l. 69 et `references/activite.md` l. 7. `Micro-activité` n'apparaît nulle part dans le runtime. |
| **`mock_sans_derogation.md`** | **DÉFECTUEUX comme cas négatif** | Voir §3. C'est un **quasi-positif** : il réunit toutes les composantes sémantiques d'une dérogation, sauf le mot. |
| **C0** | **Jamais exécuté avant ce cycle** | Prérequis de validité de l'instrument (`CONTROLE_STABILISATION_NOY014.md` §2) resté non exécuté et non consigné. Exécuté ici pour la première fois (§2). |

Conséquence méthodologique : le FAIL de NOY014_1 est **surdéterminé**. Il a deux causes indépendantes, dont une seule relève du noyau.

---

# 2. C0 — exécuté et consigné pour la première fois

C0 n'avait jamais été joué (vérifié : aucune trace dans le dépôt). Sans lui, on ne pouvait pas exclure que le candidat produise spontanément `Micro-activité`, ce qui aurait vidé NOY014_1 de tout sens.

| Run | Condition | Sortie | Lecture |
|---|---|---|---|
| C0 avant correctif | A, sans `mock.md` | `Activité (Brique)` → `Étape 1`, `Étape 2` | Aucun `Micro-activité`. **Contraste établi.** |
| C0 après correctif | A, sans `mock.md` | `Activité (Brique)` → `Consigne`/`Étape 1`, `Production`/`Étape 2` | Aucun `Micro-activité`. **Pas de régression.** |

L'instrument est donc valide sur ce point : le comportement de référence tient sans fixture.

---

# 3. Cause racine retenue

## 3.1 Ce qui a été écarté

- « L'agent n'a pas lu le mock » → écarté : `mock.md` lu dans tous les runs.
- « L'agent n'a pas mobilisé la règle générale » → **écarté formellement** : `decoupage_pedagogique.md` (porteur de la règle générale) a été lu dans **tous** les runs avec mock. Le conflit était réellement mobilisé, donc la condition d'entrée de la règle de préséance était remplie.
- « Inversion d'overlay » → écarté par SHA-256.
- « Le candidat invente spontanément `Micro-activité` » → écarté par C0.

## 3.2 Cause 1 — sous-spécification du runtime (R1, confirmé mais insuffisant)

`SKILL.md` l. 120 exigeait une préséance entre « référence spécialisée » et « **règle générale du skill** ». Ce second terme est **non résolvable à l'exécution** :

- le mot « noyau » est absent de `SKILL.md` et de `references/` (présent seulement dans `promesse.md`, `base_de_travail.md`, `README.md`, non chargés au runtime) ;
- la règle générale en jeu vit elle-même dans `references/` — indiscernable structurellement de `mock.md`, dans le même dossier.

Le conflit est donc perçu comme **référence contre référence**, et la décision retombait sur la seule maxime de priorité offerte par `SKILL.md` : l. 99, « la référence normative spécialisée **fait foi** » — un *lex specialis*.

Ce diagnostic est réel, et c'est celui que le correctif a traité. **Il ne suffit pas.**

## 3.3 Cause 2 — l'instrument ne discrimine pas (cause dominante)

`mock_sans_derogation.md` contient :

| Ligne | Contenu | Fonction |
|---|---|---|
| 7 | « Dans ce périmètre, une `Activité` peut contenir des `Micro-activités`. » | règle locale contredisante |
| 11 | « La règle générale **du noyau** prévoit par ailleurs qu'`Activité` est la granularité la plus fine. » | **nomme la règle contredite, et connaît le conflit** |
| 13 | « Cette règle concerne uniquement le périmètre `MOCK-GRANULARITE`. » | **limitation de portée** |

Or une dérogation locale *est*, sémantiquement : une règle contredisante + la connaissance de la règle contredite + une limitation de portée. Les trois sont présentes. Le seul écart entre les deux fixtures est le **mot** « déroge ».

Preuve directe dans le verbatim du rerun A :

> « …dérogation explicitement bornée à ce périmètre par rapport à la **règle générale du noyau** selon laquelle l'`Activité` est la granularité la plus fine. »

L'agent emploie « noyau », terme **absent du runtime** : il le tient du mock. Il ne contourne donc pas la règle de préséance — il la **satisfait**, sur une lecture sémantique défendable d'une fixture qui signale bien une dérogation en substance.

## 3.4 Le marqueur exigé par la doctrine n'a jamais été implémenté

`base_de_travail.md` §18 : « Une dérogation au noyau doit être explicitement autorisée par le noyau, **signalée avec un marqueur uniforme** dans la référence spécialisée, et rester limitée à son périmètre. »

Vérifié : **aucun marqueur n'est défini dans le runtime** (`grep "marqueur"` sur `SKILL.md` et `references/` → vide). Le skill demande donc de détecter un « signalement explicite de dérogation » sans jamais dire ce qui en constitue un — face à une fixture construite exactement sur cette frontière.

**Cause racine consolidée :** la discrimination voulue repose sur un marqueur conventionnel que la doctrine exige, que le runtime ne définit pas, et que la fixture négative satisfait en substance sans le porter littéralement. Aucune reformulation en prose de la règle de préséance ne peut lever cela.

---

# 4. Modification appliquée (invalidée)

`en_cours/SKILL.md` uniquement, 2 lignes. **Non committée.**

| Ligne | Avant | Après |
|---|---|---|
| 99 | « …la référence normative spécialisée **fait foi**. » | « …c'est la référence normative spécialisée **qui porte cette règle, pas le glossaire**. » |
| 120 | préséance ancrée sur « une règle générale du skill » | préséance ancrée sur « règle bornée à un périmètre » vs « règle énoncée sans restriction de périmètre » ; ajout explicite que la spécialisation ne confère par elle-même aucune priorité |

**Écart par rapport au plan :** le plan `PLAN_CORRECTION_R1_V2.1_2026-08-23.md` §2 prévoyait de ne toucher **que** la l. 99 et de laisser la l. 120 intacte. J'ai également modifié la l. 120, sur la base de l'analyse statique du §3.2 (terme non résolvable) — écart assumé et signalé, décidé avant les reruns.

Justification doctrinale : G02 est préservée à l'identique. Le changement porte sur l'*opérationnalisation* (remplacer un pôle non résolvable par une propriété textuellement observable), pas sur la doctrine. La clause de signalement est conservée mot pour mot. L'amorce conditionnelle est conservée : aucun gate ajouté.

---

# 5. Contrôles statiques

| # | Contrôle | Résultat |
|---|---|---|
| CS-R1-1 | Portée du diff | ✅ `en_cours/SKILL.md` seul, 2 insertions / 2 suppressions |
| CS-R1-2 | « fait foi » éliminé de `SKILL.md` | ✅ 0 occurrence |
| CS-R1-3 | Terme non résolvable « règle générale du skill » éliminé | ✅ 0 occurrence |
| CS-R1-4 | Clause « ne pas arbitrer silencieusement ; la signaler » préservée | ✅ présente à l'identique |
| CS-R1-5 | Absence de gate | ✅ amorce conditionnelle conservée ; aucun verbe de recherche systématique |
| CS-R1-6 | Références porteuses du contraste intactes | ✅ aucun fichier de `references/` modifié |
| CS-R1-7 | Aucun NOY / oracle / fixture modifié | ✅ `validation/` intact |
| CS-R1-8 | Surface de déclenchement de la nouvelle règle | ✅ aucune référence du runtime ne déclare de restriction de périmètre → pas de sur-déclenchement sur les gabarits (qui *précisent* le socle sans le contredire) |

---

# 6. Résultat des runs

Runs joués en contextes neufs, aveugles (aucune connaissance de l'oracle, de la doctrine de préséance ni de l'existence d'un conflit), copies isolées, `_1` et `_2` jamais dans la même conversation.

| Run | Fixture | Sortie | Verdict |
|---|---|---|---|
| NOY014_1 avant correctif | sans dérogation | `Activité → Micro-activité 1, Micro-activité 2` | **FAIL** (reproduit indépendamment du dry-run) |
| NOY014_2 avant correctif | avec dérogation | `Activité → Micro-activité 1, Micro-activité 2` | PASS |
| NOY014_1 après correctif — run A | sans dérogation | `Activité → Micro-activité 1, Micro-activité 2` | **FAIL** |
| NOY014_1 après correctif — run B | sans dérogation | `Activité → Micro-activité 1, Micro-activité 2` | **FAIL** |
| NOY014_2 après correctif | avec dérogation | `Activité → Micro-activité 1, Micro-activité 2` | PASS |

Attendu du plan : `_1` = PASS, `_2` = PASS. **Non atteint.** Conformément à la consigne, aucune modification en cascade n'a été tentée.

## 6.1 Constat le plus important

Sur les **5 runs comportant une fixture**, la sortie est `Micro-activité` — dans **100 % des cas**, avec ou sans marqueur de dérogation, avant comme après correctif. Les trajectoires de lecture sont elles aussi identiques (`SKILL.md` → `mock.md` → `decoupage_pedagogique.md`).

Le marqueur de dérogation a donc un **effet observé nul**.

Conséquence : le PASS de NOY014_2 **n'établit pas** que la branche positive fonctionne. Il est obtenu parce que la règle spécialisée est appliquée quoi qu'il arrive, et que cela coïncide avec l'attendu de `_2`. En l'état, NOY014_2 est un test qui **ne peut pas échouer pour la bonne raison**.

Cela corrige la conclusion du dry-run (`RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md` §5 : « Le mécanisme positif de dérogation locale fonctionne »). Le rapport de dry-run n'est pas réécrit — la divergence est consignée ici.

## 6.2 Leçon sur le contrôle statique CS-P4 du cycle précédent

`RAPPORT_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23.md` donnait CS-P4 en « ✅ PASS » par *simulation sur table* de NOY014_1. Cette simulation supposait une application lexicale du test de marqueur. Le comportement réel est sémantique. **Une simulation sur table d'une règle en prose n'est pas une preuve comportementale.**

---

# 7. Risques résiduels et état

- La modification de `SKILL.md` est **en place, non validée, non committée**. Elle corrige deux défauts réels (maxime *lex specialis* parasite, pôle non résolvable) sans produire le comportement visé, et n'introduit aucune régression observée (C0 et NOY014_2 inchangés).
- Tant que le marqueur n'est pas défini dans le runtime, `NOY014_1` restera vraisemblablement en FAIL et `NOY014_2` en PASS vacuous.
- La règle projet « on ne modifie pas l'oracle et le skill dans le même cycle » (`base_de_travail.md` §18) interdit de traiter simultanément la fixture et le runtime. La suite est donc un **point de décision**, pas une continuation mécanique.
- Les runs ont été joués via des contextes neufs de cette session, pas dans la session Linux dédiée `claude-test` prévue par `validation/CLAUDE.md`. Ils valent comme reproduction de diagnostic, **pas** comme runs officiels de campagne.

---

# 8. Décision prise et état final

Décision de l'utilisateur après lecture des résultats : **reverter et renvoyer la préséance à la refactorisation générale du noyau.**

- `en_cours/SKILL.md` a été reverté (`git checkout -- en_cours/SKILL.md`) : identique à son état du commit `01e9ca1`, l. 99 et l. 120 restaurées.
- Le cycle correctif dédié à R1 est **clos sans modification du noyau**. `PLAN_CORRECTION_R1_V2.1_2026-08-23.md` est de ce fait caduc comme plan d'exécution ; il reste pertinent comme trace du raisonnement écarté.
- Les acquis conservés de ce cycle sont **documentaires** : le résultat C0 (§2), la cause racine consolidée (§3), et le constat d'effet nul du marqueur (§6.1).

## Contraintes transmises à la refactorisation

1. La règle de préséance ne peut pas être rendue discriminante par une reformulation en prose : il faut **définir le marqueur de dérogation** dans le runtime, comme `base_de_travail.md` §18 l'exige déjà.
2. Le pôle « règle générale du skill » de la l. 120 est **non résolvable au runtime** — le runtime ignore la notion de « noyau », et les règles générales vivent dans `references/` au même titre qu'une référence spécialisée. Toute reformulation doit s'appuyer sur une propriété textuellement observable.
3. `SKILL.md` l. 99 (« la référence normative spécialisée fait foi ») reste une maxime *lex specialis* parasite sur l'axe de la préséance. Sa neutralisation est nécessaire mais non suffisante.
4. `NOY014_2` est actuellement un **PASS vacuous** : il ne peut pas échouer pour la bonne raison. Le rendre discriminant suppose de traiter la fixture négative — dans un cycle distinct de celui qui touche le noyau.
5. C0 doit être rejoué et consigné après toute modification touchant la granularité.

# 9. Ce que ce cycle n'a pas fait

- Aucun oracle modifié.
- Aucun NOY, aucune fixture modifiée.
- Aucun fichier du noyau modifié à l'état final (le correctif a été reverté).
- Aucun commit.
- Aucune refactorisation du noyau.
