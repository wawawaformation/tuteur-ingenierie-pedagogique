# Plan de refactorisation du noyau V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Version concernée :** candidat V2.1 (`en_cours/`)
**Date :** 2026-08-23
**Nature :** plan d'implémentation, directement exécutable par un agent de développement
**Statut :** aucune modification fonctionnelle appliquée lors de la rédaction de ce plan

> **Pour l'agent qui exécutera ce plan.** Les « tests » de ce projet ne sont pas du code : ce sont des scénarios NOY joués dans des **contextes neufs et aveugles** (l'exécutant ne doit pas connaître l'oracle) et des **contrôles statiques** (`grep`). Chaque lot se termine par un contrôle explicite. N'enchaîne pas deux lots sans avoir passé le contrôle du premier. Ne modifie jamais un oracle, un scénario ou une fixture dans le même lot qu'une modification du runtime.

---

# 1. État de départ

## 1.1 Point de départ Git

Le refactoring part de l'état du commit `01e9ca1` pour `en_cours/`.

Le cycle correctif R1 a été **exécuté puis reverté** : `en_cours/SKILL.md` est revenu à son état de `01e9ca1`. Les modifications de ce cycle **ne constituent pas une doctrine** et ne doivent pas être reprises telles quelles. Voir `RAPPORT_CYCLE_R1_V2.1_2026-08-23.md`.

Vérification à faire avant de commencer :

```bash
cd /projets/skill/tuteur-ingenierie-pedagogique-v2
git diff --name-only -- en_cours/    # doit être vide
grep -c "fait foi" en_cours/SKILL.md # doit valoir 1 (l. 99 non corrigée)
```

Si `en_cours/` n'est pas propre, s'arrêter et demander.

## 1.2 Comportement observé au départ

Photographie du dry-run pré-refactorisation (`RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md`) : **15 PASS / 16**, seul `NOY014_1` en FAIL.

Cette photographie reste une **trace historique utile**, pas une validation officielle ni l'étalon de non-régression du refactoring. L'étalon de comparaison sera la baseline comportementale complète établie au lot 0.

## 1.3 Acquis du cycle R1 à conserver comme éléments d'architecture

| # | Constat | Conséquence pour ce plan |
|---|---|---|
| R1-a | C0 établit que sans fixture contradictoire, l'agent produit `Étape`, jamais `Micro-activité`. | Le contraste de granularité est réel. C0 doit être rejoué après tout changement touchant la granularité. |
| R1-b | `mock_sans_derogation.md` est un **quasi-positif** : il réunit règle contredisante + connaissance de la règle contredite + limitation de portée. Seul le mot « déroge » sépare les deux fixtures. | `NOY014` ne peut pas servir de contrôle discriminant en l'état. Chantier d'instrumentation séparé (§9). |
| R1-c | « Dérogation explicitement signalée » n'est pas opérationnalisé dans le runtime. | À traiter par une architecture, pas par une reformulation en prose (§6.3). |
| R1-d | Le « marqueur uniforme » de `base_de_travail.md` §18 n'est pas défini. | Le plan doit le définir — ou le remplacer par un mécanisme équivalent. |
| R1-e | `NOY014_2` passe avec **ou sans** marqueur : sur 5 runs avec fixture, la sortie fut `Micro-activité` dans 100 % des cas. Le PASS est **vacuous**. | Ne pas compter `NOY014_2` comme preuve que le discriminateur fonctionne. |
| R1-f | Une simulation « sur table » d'une règle en prose n'est pas une preuve comportementale (cf. CS-P4 du cycle précédent, validé à tort). | Tout contrôle de comportement doit passer par un run réel en contexte aveugle. |

---

# 2. Objectifs et non-objectifs

## 2.1 Objectifs

1. Réduire la **charge simultanée** imposée à l'agent et l'**ambiguïté** des règles, à doctrine constante.
2. Supprimer les duplications qui créent plusieurs sources pour une même règle.
3. Remettre au bon niveau architectural les règles mal placées.
4. Rendre la préséance général / spécialisé **opérationnelle** sans gate ni cérémonie.
5. Préparer l'insertion propre d'une future référence `tutorat.md`.

Critère de réussite global : **moins de charge et d'ambiguïté, même comportement doctrinal.**

Le nombre de lignes n'est pas un objectif. Une réduction qui ferait perdre un invariant est un échec.

## 2.2 Non-objectifs — explicitement hors périmètre

- Implémenter les spécificités du tutorat V3.
- Créer `references/tutorat.md` (au-delà de la convention d'insertion décrite au §6.4).
- Généraliser la future règle V3 « une nouveauté = une activité ».
- Réintroduire une règle générale « toujours diagnostiquer avant toute exposition » (ex-P01).
- Faire passer `NOY014_1` avec l'instrument actuel.
- Obtenir « 16/16 » avec l'instrument actuel.
- Promouvoir `en_cours/` vers `dist/stable/`.
- Modifier une archive de campagne (`validation/v1/`, `validation/v2/`).

---

# 3. Invariants gelés

Ces comportements doivent être identiques avant et après refactoring. Ils sont **gelés** : aucune étape ne peut les modifier.

## 3.1 Preuve, déclaration, attestation

| # | Invariant | Source normative actuelle | NOY |
|---|---|---|---|
| I01 | Exposition ou déclaration ≠ preuve attestée. | `taxonomie.md` A3 ; `etat_des_paliers.md` | NOY001 |
| I02 | Auto-déclaration de l'apprenant ≠ preuve. | `etat_des_paliers.md` | NOY001, NOY006 |
| I03 | Une preuve doit être compatible avec le palier attesté. | `etat_des_paliers.md` | NOY002 |
| I04 | Manque de preuve ≠ preuve de manque ; palier 0 = « notion identifiée, rien d'attesté ». | `etat_des_paliers.md` l. 49, l. 79 | NOY013 |
| I05 | Preuve externe rapportée recevable si la performance observée est précise. | `taxonomie.md` A3 ; `etat_des_paliers.md` | NOY001 |
| I06 | Appréciation générale du formateur ≠ attestation. | `etat_des_paliers.md` l. 75, l. 83-86 | NOY012_1 |
| I07 | Attestation explicite valide (4 conditions) = fondement suffisant d'un palier. | `etat_des_paliers.md` l. 51-62 | NOY012_2 |
| I08 | Non-cumul / non-conversion : une performance observée reste dans la voie preuve. | `etat_des_paliers.md` l. 77 | NOY005, NOY012_2 |
| I09 | Une attestation ne peut jamais fonder une conclusion négative. | `etat_des_paliers.md` l. 79 | NOY013 |
| I10 | Un palier peut redescendre ; révisabilité identique pour l'attestation. | `etat_des_paliers.md` l. 37 | — |

## 3.2 Granularité des paliers et portée

| # | Invariant | Source | NOY |
|---|---|---|---|
| I11 | Le palier est attaché à une notion, jamais à l'apprenant. | `taxonomie.md` A2 | NOY005 |
| I12 | Réussite globale d'une activité intégrée ≠ attestation de toutes ses notions. | `etat_des_paliers.md` l. 88-123 | NOY005 |
| I13 | `utiliser ≠ créer`, `exécuter ≠ écrire`, `lire ≠ produire`, `modifier ≠ concevoir`. | `etat_des_paliers.md` l. 98-101 | NOY005 |
| I14 | Portée d'une attestation limitée à la notion et au palier nommés. | `etat_des_paliers.md` l. 125-132 | NOY012_2 |
| I15 | Un Quiz n'atteste jamais au-delà du palier 2. | `activites_type/quiz.md` l. 18, l. 63 | NOY008 |

## 3.3 Activité évaluée et évaluation

| # | Invariant | Source | NOY |
|---|---|---|---|
| I16 | Budget de nouveauté = 1 pour une activité évaluée. | `taxonomie.md` A3 | NOY003 |
| I17 | A1 : seules les activités évaluées sont contraintes ; exposition, démonstration, lecture commentée, observation guidée, pratique accompagnée, exploration restent libres. | `taxonomie.md` A1 | NOY003 |
| I18 | Alignement objectif → tâche → production/performance → critères → preuve → conclusion. | 4 formulations concurrentes (voir P1) | NOY004 |
| I19 | Un critère de réussite doit vérifier la compétence visée ; la complétude d'un livrable ne suffit pas. | `opo.md` | NOY004 |
| I20 | Pas de notation scolaire spontanée (A4) ; une mesure réelle ou imposée reste légitime. | `taxonomie.md` A4 | NOY007 |
| I21 | Critères explicites pour l'apprenant, mais solution / correction / indices décisifs non révélés avant production. | `activite.md` l. 91 ; `decoupage_pedagogique.md` l. 155 ; `quiz.md` | NOY010 |

## 3.4 Architecture des gabarits

| # | Invariant | Source | NOY |
|---|---|---|---|
| I22 | Un gabarit spécialisé reste une Activité complète : il hérite du socle puis le précise. | `activite.md` ; front matter `inherits` | NOY008 |
| I23 | La modalité adapte la mise en œuvre, elle n'interdit pas un gabarit par principe. | `decoupage_pedagogique.md` §2 | NOY009 |
| I24 | Brique / Atelier / Quiz / Recul sont des formes d'Activité, pas des niveaux concurrents de Séance / Séquence. | `activite.md` ; `decoupage_pedagogique.md` | NOY011 |
| I25 | `Activité` est la granularité la plus fine. | `decoupage_pedagogique.md` l. 69 ; `activite.md` l. 7 | NOY014, C0 |
| I26 | `typical_uses` = indices de sélection, pas conditions exclusives. | 3 emplacements (voir P9) | NOY009, NOY011 |

## 3.5 Posture et périmètre

| # | Invariant | Source | NOY |
|---|---|---|---|
| I27 | Établir le point de départ utile **avant une décision pédagogique qui en dépend** — et non « toujours diagnostiquer d'abord ». | `SKILL.md` l. 42, l. 118 | — (ex-P01, volontairement hors NOY) |
| I28 | Respecter le périmètre demandé : ne pas élargir la production. | `decoupage_pedagogique.md` §4 | — |
| I29 | Ne pas prétendre disposer d'un état de progression inaccessible. | `etat_des_paliers.md` §Persistance | — |

## 3.6 Architecture documentaire

| # | Invariant | Source | NOY |
|---|---|---|---|
| I30 | Une dérogation locale ne modifie pas la règle générale et ne s'étend pas hors de son périmètre. | `SKILL.md` l. 120 | NOY014_2 |
| I31 | Une contradiction pertinente non résolue n'est pas arbitrée silencieusement : elle est signalée. | `SKILL.md` l. 120 | — |
| I32 | Une référence spécialisée ne prévaut **pas** du seul fait qu'elle est spécialisée. | `SKILL.md` l. 120 (non opérationnel — voir P6) | NOY014_1 |

---

# 4. Cartographie du runtime actuel

## 4.1 Inventaire

| Fichier | Lignes | Rôle réel | Catégorie |
|---|---|---|---|
| `SKILL.md` | 120 | Orchestration, garde-fous résumés, liste des sources, contrôles de sortie, préséance | invariant noyau + procédure générale |
| `references/taxonomie.md` | 187 | §1 échelle de progression + §2 clauses A1-A4 | **double responsabilité** : aide d'interprétation + invariant noyau |
| `references/etat_des_paliers.md` | 160 | Gabarit de trace, fondements d'un palier, portée, persistance | invariant noyau (source normative centrale) |
| `references/opo.md` | 71 | Règle des 3C, alignement, contrôles avant activité évaluée | invariant noyau |
| `references/decoupage_pedagogique.md` | 167 | §0-3 granularité et modalités + §4 directives de rédaction de fiches | invariant noyau + **procédure mal placée** |
| `references/activite.md` | 93 | Socle commun d'Activité, catalogue, rôle du front matter | invariant noyau |
| `references/andragogie.md` | 53 | Posture, ton, élicitation | procédure générale |
| `references/glossaire.md` | 402 | Vocabulaire — mais porte aussi une règle normative et redéfinit structure et modalités | aide d'interprétation + **fuite normative** |
| `references/syllabus.md` | 39 | Contrat du niveau Module | règle spécialisée |
| `references/sequence.md` | 44 | Contrat du niveau Séquence | règle spécialisée |
| `references/seance.md` | 38 | Contrat du niveau Séance | règle spécialisée |
| `references/activites_type/brique.md` | 132 | Gabarit | règle spécialisée |
| `references/activites_type/atelier.md` | 105 | Gabarit | règle spécialisée |
| `references/activites_type/quiz.md` | 131 | Gabarit (porte I15) | règle spécialisée |
| `references/activites_type/recul.md` | 157 | Gabarit | règle spécialisée |

Total runtime : 1899 lignes / ~15 200 mots.

## 4.2 Sources normatives centrales de fait

Mesuré par les renvois entrants :

- **`taxonomie.md` §2** — cible de 8 renvois « clause A4 » depuis 7 fichiers (`opo.md`, `activite.md`, `glossaire.md`, `quiz.md`, `brique.md`, `atelier.md`, `recul.md`). C'est le **hub normatif du runtime**, alors que le titre du fichier annonce une taxonomie.
- **`etat_des_paliers.md`** — source unique de l'attestation, des fondements et de la portée. Devenue la référence la plus dense en doctrine V2.1.
- **`decoupage_pedagogique.md`** — source de la granularité et des modalités, et porteuse du contraste I25.

## 4.3 Dépendances implicites

| Dépendance | Nature | Risque |
|---|---|---|
| Les 7 renvois « `taxonomie.md` §2, clause A4 » | ancrage sur un **numéro de section** | toute renumérotation de `taxonomie.md` casse 8 renvois silencieusement |
| `taxonomie.md` A2 → `etat_des_paliers.md` | A2 impose la trace, `etat_des_paliers.md` en donne le format | les deux fichiers re-narrent mutuellement leur raison d'être (P10) |
| `taxonomie.md` A3 → `etat_des_paliers.md` (« fondement recevable ») | A3 délègue la définition du fondement | la définition existe aux deux endroits (P2) |
| `activite.md` ← `inherits:` des 4 gabarits | héritage déclaré en front matter | mécanisme sain, à réutiliser (§6.3) |
| `quiz.md` l. 18/63 → plafond palier 2 | invariant I15 porté par un gabarit | un invariant de preuve vit dans une règle spécialisée |
| I21 (exposition maîtrisée) | porté par **3** fichiers | dispersion d'un invariant NOY010 |

---

# 5. Problèmes identifiés

Numérotés `P*` et repris tels quels dans le plan d'implémentation.

## P1 — Quatre formulations concurrentes de la chaîne d'alignement

| Emplacement | Formulation |
|---|---|
| `SKILL.md` l. 105-112 | objectif → tâche réellement demandée → production ou performance observable → critères → preuve disponible → conclusion permise |
| `taxonomie.md` l. 180-187 (A4) | objectif observable → production ou comportement → critères de réussite → preuve → portée de la preuve → attestation / feedback / remédiation |
| `glossaire.md` l. 236 | Objectif → tâche → production/performance → critères → preuve → conclusion |
| `opo.md` §2 | triangle OPO / Activité / Évaluation, puis « Alignement entre performance visée et preuve » |

Aucune n'est désignée comme canonique. `taxonomie.md` ajoute deux maillons (`portée`, `attestation`) que les autres n'ont pas. **Impact :** l'agent doit réconcilier quatre variantes pour appliquer I18.

## P2 — Triplication de la règle « preuve externe rapportée », avec trois libellés de l'exemple

| Emplacement | Exemple employé |
|---|---|
| `SKILL.md` l. 30 | « il l'a déjà fait et ça marchait » |
| `taxonomie.md` l. 120 | « il a déjà fait plusieurs refactorings de ce type et ça marchait » |
| `etat_des_paliers.md` l. 34 | « il a déjà fait plusieurs refactorings de ce type et ça marchait » |

`SKILL.md` l. 30 annonce un renvoi (« appliquer `references/taxonomie.md` §2 ») **puis reformule quand même la règle et l'exemple**. C'est exactement le motif que `SKILL.md` l. 26 interdit pour A1-A4 (« sans les réinterpréter ici »).

## P3 — `taxonomie.md` porte deux responsabilités

§1 est une **aide d'interprétation** (échelle, verbes, exemples de transposition, ~45 lignes). §2 porte les **clauses normatives** A1-A4 (~130 lignes), cible de 8 renvois externes. Un fichier nommé « Taxonomie des paliers » est donc le hub normatif des activités évaluées.

## P4 — `glossaire.md` fuit hors de son rôle déclaré

Il déclare l. 9 : « Les règles détaillées restent portées par les fichiers spécialisés ». Or :

- l. 236 il **porte** une règle normative (la chaîne d'alignement) ;
- l. 19-43 il **redéfinit** Module / Séquence / Séance / Activité / Granularité, déjà définis dans `decoupage_pedagogique.md` §1 ;
- l. 251-267 il **redéfinit** les 4 modalités, déjà définies dans `decoupage_pedagogique.md` §2 ;
- l. 388 il **re-énonce** I26.

Sur 402 lignes, une part importante est encyclopédique sans effet comportemental (`référentiel`, `bloc de compétences`, `compétence`, `savoir` / `savoir-faire` / `savoir-être`, `micro-learning`, `classe inversée`, `ingénierie de formation`, `SMART`…).

## P5 — `SKILL.md` l. 99 : maxime *lex specialis* parasite

« lorsqu'une définition implique une règle comportementale, la référence normative spécialisée **fait foi** ». Visait l'axe *glossaire → source normative*. Se transpose à l'axe *règle générale → référence spécialisée*, où elle contredit I32. Confirmé par le cycle R1.

## P6 — `SKILL.md` l. 120 : pôle non résolvable à l'exécution

La règle oppose « une référence spécialisée » à « **une règle générale du skill** ». Or :

- « noyau » n'apparaît **nulle part** dans `SKILL.md` ni `references/` ;
- la règle générale en jeu (I25) vit elle-même dans `references/` — indiscernable d'une référence spécialisée.

L'agent ne peut donc pas instancier le terme de gauche. La décision retombe sur *lex specialis* (P5). **C'est la cause racine du FAIL NOY014_1.**

## P7 — Le marqueur de dérogation n'est pas défini

`base_de_travail.md` §18 exige « un **marqueur uniforme** dans la référence spécialisée ». Aucun marqueur n'existe dans le runtime (`grep "marqueur"` → vide). Le skill demande de détecter un signalement explicite sans dire ce qui en constitue un.

## P8 — I25 dupliqué sur deux fichiers

`decoupage_pedagogique.md` l. 69 et `activite.md` l. 7, formulations différentes. C'est le porteur du contraste NOY014/C0 : deux sources à maintenir cohérentes.

## P9 — I26 triplé

`SKILL.md` l. 75, `activite.md` l. 41, `glossaire.md` l. 388.

## P10 — A2 et `etat_des_paliers.md` se re-narrent mutuellement

`taxonomie.md` l. 107-108 énonce deux « conséquences opératoires » qui décrivent la raison d'être de `etat_des_paliers.md`. Réciproquement, `etat_des_paliers.md` l. 136 (« Ce que ce tableau sert à calculer ») re-narre A3.

## P11 — `decoupage_pedagogique.md` §4 est au mauvais niveau

§4 « Directives pour la génération de fiches » contient des **conventions de production** (respect de la granularité demandée, niveau de détail, séparation apprenant/formateur, callouts, réflexe andragogique) dans un fichier dont l'objet déclaré est « Définir les échelles du découpage pédagogique ». L'invariant I21 y est enfoui, alors qu'il est aussi porté par `activite.md` l. 91 et `quiz.md`.

## P12 — `SKILL.md` « Contrôles avant réponse ou livraison » mélange quatre choses

Le bloc l. 101-120 réunit : la chaîne d'alignement, une règle sur la complexité vs nouveauté, une règle d'élicitation en tutorat, et **la règle de préséance documentaire**. La préséance est une règle d'**architecture**, pas un contrôle de livraison : son emplacement actuel la rend à la fois mal située et peu visible.

## P13 — Incohérence mineure de front matter

Les gabarits utilisent `purpose:`, les références `objectif:`. Signalé pour information ; **ne pas corriger** (churn sans bénéfice comportemental).

---

# 6. Architecture cible

## 6.1 Principe directeur

Trois règles de placement :

1. **`SKILL.md` oriente, ne redit pas.** Il contient : le rôle, le mouvement d'orchestration, la liste des sources, la règle de périmètre/préséance, et des pointeurs. Aucun exemple normatif, aucune reformulation d'une règle portée par une référence.
2. **Une règle = une source normative.** Tout autre emplacement est un pointeur, jamais une paraphrase.
3. **Le glossaire est strictement descriptif.** Il ne porte aucune règle comportementale et ne redéfinit pas ce qu'une source normative définit déjà.

## 6.2 Ce qui reste dans `SKILL.md`

| Section | Devenir |
|---|---|
| Rôle du skill | conservée telle quelle |
| Garde-fous prioritaires | conservée comme **repères de navigation seuls** ; suppression de la paraphrase et de l'exemple de P2 |
| Orchestration | conservée ; le mouvement général reste dans `SKILL.md` |
| Sources de vérité | conservée ; la maxime l. 99 est bornée à son axe réel (P5) |
| Contrôles avant réponse ou livraison | conservée, mais **la chaîne devient un pointeur vers la source canonique** et la préséance en sort (P12) |
| **Périmètre et préséance** (nouveau) | section propre, courte, à la place de l'actuelle l. 120 |

## 6.3 Préséance : remplacer le marqueur lexical par un périmètre déclaré

C'est le cœur architectural du plan. Il répond à P6, P7, R1-b et R1-c.

### Pourquoi le mécanisme actuel ne peut pas marcher

L'actuel demande à l'agent de juger, **en prose**, si un document « signale explicitement qu'il déroge ». Le cycle R1 a montré que cette frontière est indécidable : un document qui contredit une règle, nomme cette règle et borne sa portée *est* sémantiquement une dérogation, même sans le mot.

### Ce que le mécanisme ne doit surtout pas faire

Une première version de ce plan définissait « règle générale » par l'**absence** de champ `perimetre:`. C'était un défaut : le runtime contient déjà des références spécialisées sans ce champ — `syllabus.md`, `sequence.md`, `seance.md` et les quatre gabarits de `activites_type/` n'ont que `objectif:` ou `kind:`/`inherits:`/`purpose:`/`typical_uses:`. Cette convention les aurait **reclassifiées implicitement en règles générales**, en contradiction avec la cartographie du §4.1 qui les classe en règles spécialisées.

Principe corrigé : **aucun champ ne classifie une référence.** Le mécanisme ne produit aucune taxonomie générale/spécialisé et ne reclassifie rien.

### Mécanisme cible

Le discriminateur passe du **texte** au **front matter**, mécanisme déjà établi du projet — mais il porte uniquement sur l'acte de **déroger**, jamais sur le statut de la référence.

Deux champs, tous deux **facultatifs et opt-in** :

```yaml
deroge_a: [<ID de règle>, ...]   # dérogation déclarée à une ou plusieurs règles identifiées
perimetre: <identifiant>         # borne de portée ; obligatoire dès que deroge_a: est présent
```

Règles de lecture :

- **`deroge_a:` est le seul discriminateur.** Une règle ne prévaut sur une autre que si son fichier nomme cette autre règle dans `deroge_a:`.
- Une dérogation déclarée ne vaut que dans le `perimetre:` déclaré par le même fichier.
- `deroge_a:` sans `perimetre:` est une **déclaration invalide** : elle ne produit aucune dérogation, et la contradiction est signalée. Ce garde-fou rend la localité obligatoire par construction.
- **Une référence sans `deroge_a:` ne déroge à rien** — quel que soit son degré de spécialisation, qu'elle déclare ou non un `perimetre:`, et qu'elle contredise ou non une autre règle. La règle contredite tient.
- Une contradiction pertinente non résolue par ce mécanisme reste signalée, non arbitrée.

Conséquence directe sur l'existant : **aucune des références actuelles n'est affectée.** Aucune ne porte `deroge_a:`, donc aucune ne déroge à quoi que ce soit, et leur statut ne change pas. Le lot B est neutre sur le comportement de toutes les références en place.

### Pourquoi c'est supérieur à un marqueur en prose

| Critère | Marqueur en prose (actuel) | `deroge_a:` déclaré (cible) |
|---|---|---|
| Décidable | non — frontière sémantique floue (R1-b) | oui — un champ nomme un ID, ou il est absent |
| Pôle de gauche instanciable | non : « règle générale du skill » sans référent (P6) | oui : **la règle nommée dans `deroge_a:`**, désignée par son ID — aucune classification à inférer |
| Reclassifie l'existant | — | non : sans `deroge_a:`, rien ne change |
| Gate imposé | risque réel | non : le front matter arrive **avec** le fichier que l'agent charge de toute façon |
| Localité | déclarative, non vérifiable | `perimetre:` obligatoire dès qu'il y a dérogation |
| Réutilise l'existant | non | oui — `activite.md` l. 28-30 établit déjà que le front matter fait partie du contrat |

Point important sur l'absence de gate : l'agent ne « cherche » jamais une dérogation. Il lit le front matter au moment où il ouvre la référence — geste qu'il fait déjà pour départager des gabarits (`SKILL.md` l. 72). Aucun contrôle préalable n'est ajouté.

### Identifiants stables des règles dérogeables

`deroge_a:` ne doit pas accepter une valeur libre : `granularité la plus fine` serait une chaîne instable, sensible à toute reformulation, et non vérifiable.

Le projet possède déjà une convention d'identifiants stables : **A1, A2, A3, A4**, cités 8 fois depuis 7 fichiers sous la forme `taxonomie.md` §2, clause A4. Le mécanisme la prolonge au lieu d'en inventer une autre.

Trois règles de gouvernance, volontairement minimales :

1. **Seules les règles réellement candidates à une dérogation reçoivent un ID dérogeable.** On n'identifie pas tout le runtime : un ID est ajouté quand un besoin existe, pas par anticipation.
2. **L'index des IDs dérogeables vit dans `SKILL.md`**, dans la section « Périmètre et préséance ». C'est de l'information de routage (ID → source), et le routage est le rôle de `SKILL.md`. Il est ainsi visible et auditable d'un seul coup d'œil.
3. **La règle porte son ID à sa source**, pour être trouvable dans les deux sens.

Index initial — **deux entrées**, chacune justifiée par un besoin existant :

| ID | Règle | Source normative | Pourquoi dérogeable |
|---|---|---|---|
| `A3` | Budget de nouveauté = 1 pour une activité évaluée | `taxonomie.md` §2, clause A3 | cible de dérogation nommée pour V3 tutorat (`base_de_travail.md` §6.3) |
| `R-GRAN` | `Activité` est la granularité la plus fine | `decoupage_pedagogique.md` §1 | contraste de `NOY014` et de C0 |

`A1`, `A2` et `A4` conservent leurs identifiants de **citation** existants mais **ne figurent pas** dans l'index des dérogeables : rien ne justifie aujourd'hui d'autoriser une dérogation locale à ces clauses. Les y ajouter serait inviter la dérogation plutôt que la permettre. Ajouter une entrée à l'index est donc un acte délibéré, pas un effet de bord.

Un `deroge_a:` citant un ID absent de l'index est une **déclaration invalide** : aucune dérogation, contradiction signalée. Même traitement qu'un `deroge_a:` sans `perimetre:`.

Coût total de la convention : deux champs facultatifs, deux IDs, un tableau de deux lignes dans `SKILL.md`, et un identifiant inline dans deux fichiers. Aucun registre externe, aucun validateur, aucune procédure.

### Conséquence sur l'instrumentation

Ce mécanisme **invalide les fixtures actuelles de NOY014** : `mock_avec_derogation.md` signale sa dérogation en prose, pas en front matter. C'est attendu et assumé — voir §9. Ne pas modifier les fixtures dans le même lot que le runtime.

## 6.4 Insertion future de `tutorat.md`

Aucun fichier `tutorat.md` n'est créé par ce plan. La convention d'insertion est simplement :

```yaml
---
objectif: "..."
perimetre: tutorat
deroge_a: [A3]        # « une nouveauté = une activité » déroge localement au budget A3
---
```

`A3` figure déjà dans l'index des dérogeables, et `perimetre:` est présent : la déclaration est valide.

Le noyau n'a alors **rien** à modifier pour l'accueillir — sauf si `tutorat.md` doit déroger à une règle non encore identifiée, auquel cas la seule modification requise est l'ajout d'une ligne à l'index de `SKILL.md`. C'est le test de qualité de l'architecture cible.

## 6.5 Consolidations et suppressions

| Élément | Décision | Problème traité |
|---|---|---|
| Chaîne d'alignement | source canonique unique = `opo.md` ; `SKILL.md`, `taxonomie.md` A4 et `glossaire.md` pointent | P1 |
| Règle « preuve externe rapportée » | source canonique = `etat_des_paliers.md` ; `taxonomie.md` A3 et `SKILL.md` pointent, sans exemple | P2 |
| I26 (`typical_uses`) | source canonique = `activite.md` ; `SKILL.md` et `glossaire.md` pointent | P9 |
| I25 (granularité la plus fine) | source canonique = `decoupage_pedagogique.md` l. 69 ; `activite.md` pointe | P8 |
| Redéfinitions structure/modalités du glossaire | remplacées par des renvois vers `decoupage_pedagogique.md` | P4 |
| Chaîne normative du glossaire l. 236 | supprimée, remplacée par un renvoi | P4 |
| `decoupage_pedagogique.md` §4 | déplacé vers une référence de production dédiée | P11 |
| A2 conséquences opératoires / `etat_des_paliers.md` l. 136 | dé-dupliqué, un seul énoncé | P10 |
| Split de `taxonomie.md` | **décision humaine**, lot optionnel D | P3 |
| Front matter `purpose:`/`objectif:` | non traité | P13 |

---

# 7. Plan d'implémentation étape par étape

Cinq lots. **Chaque lot est committé séparément.** Aucun lot ne modifie à la fois le runtime et un oracle.

## Convention de contrôle statique réutilisable

À créer une fois, au lot 0, et à rejouer à chaque fin de lot :

```bash
#!/usr/bin/env bash
# scripts/controle_statique_refactoring.sh — à créer au lot 0
cd "$(git rev-parse --show-toplevel)" || exit 1
R=en_cours
echo "== CS1 : aucune source normative dupliquée pour la preuve externe rapportée"
grep -rc "refactorings de ce type" $R/SKILL.md $R/references/ | grep -v ":0" || echo "  (0 occurrence)"
echo "== CS2 : chaîne d'alignement — une seule source portante"
grep -rn "→ critères" $R/SKILL.md $R/references/
echo "== CS3 : I25 — une seule source portante"
grep -rn "granularité la plus fine" $R/SKILL.md $R/references/
echo "== CS4 : I26 — une seule source portante"
grep -rn "conditions exclusives" $R/SKILL.md $R/references/
echo "== CS5 : le glossaire ne porte aucune règle comportementale"
grep -rn "doit \|ne doit pas \|jamais \|toujours " $R/references/glossaire.md | head
echo "== CS6 : aucun 'fait foi' sur l'axe de préséance"
grep -rn "fait foi" $R/SKILL.md
echo "== CS7 : ancrages 'taxonomie.md §2' encore valides"
grep -rc "taxonomie.md\` §2" $R/SKILL.md $R/references/ | grep -v ":0"
echo "== CS8 : invariants gelés toujours présents textuellement"
for m in "utiliser ≠ créer" "Budget de nouveauté" "palier 0" "auto-attester" "palier 2"; do
  printf "  %-28s %s occurrence(s)\n" "$m" "$(grep -rl "$m" $R --include=*.md | wc -l)"
done
echo "== CS9 : aucun gate de dérogation"
grep -rn "avant toute décision\|vérifier s'il existe\|rechercher systématiquement" $R/SKILL.md $R/references/ || echo "  OK"
```

---

## LOT 0 — Préparation (aucune modification du runtime)

**Fichiers :** créer `scripts/controle_statique_refactoring.sh`. Aucun fichier de `en_cours/` touché.

- [ ] **Étape 0.1 — Vérifier l'état de départ**

```bash
git diff --name-only -- en_cours/   # doit être vide
git log --oneline -1 -- en_cours/   # doit afficher 01e9ca1 ou plus récent non modifiant
```

Attendu : `en_cours/` propre.

Vérifier aussi l'environnement d'exécution de référence avant toute baseline :

- utilisateur Linux : `david` ;
- répertoire Claude de test : `/home/david/.claude` fraîchement initialisé pour cette phase de référence ;
- aucun skill, mémoire, plugin, hook, agent, commande ou personnalisation étrangère au candidat ;
- ne pas lancer la baseline tant que cet état n'est pas établi et consigné.

Ne pas purger automatiquement un environnement existant depuis ce plan : si `/home/david/.claude` n'est pas dans l'état attendu, s'arrêter et préparer explicitement l'environnement vierge avant de continuer. Après la baseline, cet environnement de test peut être remplacé/restauré par l'environnement de développement nécessaire à Opus ; il devra être recréé dans le même état propre avant la phase de référence suivante.

- [ ] **Étape 0.2 — Créer le script de contrôle statique**

Contenu : le bloc ci-dessus. `chmod +x`.

- [ ] **Étape 0.3 — Enregistrer la baseline statique**

```bash
./scripts/controle_statique_refactoring.sh > /tmp/baseline_statique.txt
cat /tmp/baseline_statique.txt
```

Attendu : CS1 montre 2 occurrences, CS2 montre 3 emplacements, CS3 en montre 2, CS4 en montre 3, CS6 en montre 1. **C'est la photographie des duplications à résorber.**

### Baseline comportementale complète — étapes 0.4 à 0.9

C'est le **véritable point zéro** du refactoring. La photographie du dry-run pré-refactorisation ne suffit pas : elle n'a pas conservé de verbatims dans le dépôt, elle comptait `NOY014_2` comme un PASS informatif alors qu'il est vacuous (R1-e), et elle n'a jamais exécuté C0. Sans baseline propre, tout basculement ultérieur sera inattribuable.

**Aucune modification fonctionnelle n'est autorisée avant la fin de l'étape 0.9.**

- [ ] **Étape 0.4 — Préparer 15 copies isolées du candidat**

Une copie neuve par run, pour garantir qu'aucun run n'en contamine un autre :

```bash
SP="$(mktemp -d)/baseline"; mkdir -p "$SP"
for s in NOY001 NOY002 NOY003 NOY004 NOY005 NOY006 NOY007 NOY008 \
         NOY009 NOY010 NOY011 NOY012_1 NOY012_2 NOY013 C0; do
  cp -a en_cours "$SP/$s"
done
# C0 et les 14 NOY n'utilisent AUCUNE fixture mock : ne rien injecter.
find "$SP" -name mock.md   # doit être vide
echo "$SP"   # conserver ce chemin
```

Contrôle d'intégrité : chaque copie doit être identique à `en_cours/`.

```bash
for d in "$SP"/*; do diff -rq en_cours "$d" >/dev/null && echo "OK $(basename "$d")" || echo "DIVERGE $(basename "$d")"; done
```

- [ ] **Étape 0.5 — Orchestrer 15 exécutants aveugles**

**Contrainte méthodologique centrale.** L'agent qui pilote ce plan connaît les oracles. Il ne peut donc pas jouer les runs lui-même : ce serait souffler l'oracle. Il doit **orchestrer des contextes exécutants qui n'y ont pas accès**, puis scorer après collecte.

Séparation des couches à respecter (`validation/CLAUDE.md`) :

```text
conception (déjà faite : les scénarios existent)
→ exécution / collecte      ← contextes aveugles
→ contrôle technique
→ scoring                   ← l'orchestrateur, après collecte
→ répétition conditionnelle
→ synthèse
```

Pour chaque scénario, l'exécutant reçoit **uniquement** :

1. le chemin de sa copie isolée du skill, présenté comme ses instructions de travail ;
2. le **stimulus exact** du §« Stimulus exact » de la fiche du scénario ;
3. le cas échéant, la relance neutre autorisée par le §« Consigne opérateur » de la fiche — **une seule fois**, à l'identique ;
4. la consigne de rendre sa réponse mot pour mot, plus la liste des fichiers qu'il a ouverts.

L'exécutant ne reçoit **jamais** : l'identifiant du scénario, son titre, son objectif, son invariant protégé, son oracle, ses conditions de FAIL, ni le fait qu'il participe à un test.

Contrôles anti-fuite à vérifier avant de lancer chaque run :

- le prompt de l'exécutant ne contient aucun mot de l'oracle du scénario ;
- il ne contient ni « NOY », ni « invariant », ni « attendu », ni « verdict », ni « test » ;
- il ne nomme pas le comportement recherché.

Les scénarios multi-tours doivent être joués tour par tour, dans l'ordre de leur fiche, sans anticiper le tour suivant.

- [ ] **Étape 0.6 — Collecter les verbatims**

Conserver, pour chaque run : le stimulus envoyé, toute relance opérateur, la réponse complète mot pour mot, la liste des fichiers lus, et l'horodatage.

Pour les runs joués via Claude Code en session dédiée, utiliser le collector du dépôt, qui collecte sans scorer :

```bash
python3 validation/collector-kit/collect_run.py start ...
# jouer le run dans une session fraîche
python3 validation/collector-kit/collect_run.py collect --run-id RUN_ID
```

Pour des runs de diagnostic joués en sous-contextes, conserver les verbatims dans le rapport de baseline lui-même. Les étiqueter explicitement comme diagnostic et non comme campagne officielle (R10).

- [ ] **Étape 0.7 — Scorer après collecte**

Le scoring se fait **une fois toutes les collectes terminées**, par l'orchestrateur, en appliquant l'oracle de chaque fiche à la trajectoire collectée.

Règles de scoring (`validation/CLAUDE.md`) : juger les observables réellement présents, n'ajouter aucune règle implicite plus stricte que l'oracle, conserver `PASS` / `FAIL` / `INDÉTERMINÉ` lorsque la fiche l'impose.

Ne pas ajuster un oracle à cette étape, même s'il paraît imprécis. Un oracle jugé fragile est consigné comme dette d'instrumentation (R6), pas corrigé ici.

- [ ] **Étape 0.8 — Reproduire tout FAIL inattendu avant tout diagnostic**

La baseline attendue est **14/14 PASS** hors NOY014, puisque le dry-run les donnait tous PASS.

Un FAIL inattendu **n'est pas diagnostiqué immédiatement**. Appliquer la règle de répétition des fiches (§11 de chaque scénario) :

```text
premier FAIL
→ deux reruns, copies et contextes neufs
→ seulement ensuite diagnostic
```

Interprétation : 1/3 ou 2/3 → instabilité, à consigner comme telle ; 3/3 → FAIL reproductible, qui **modifie uniquement la photographie comportementale de départ** pour ce scénario au lieu d'être traité comme un défaut à corriger tout de suite.

Un FAIL reproductible découvert ici ne modifie **ni l'oracle ni l'invariant normatif correspondant**. Il ne bloque pas à lui seul le refactoring puisqu'il lui préexiste, mais il est consigné comme non-conformité initiale distincte. Ne pas modifier le runtime pour le faire disparaître pendant le lot 0.

Pour les comparaisons ultérieures :

- un comportement conforme dans la baseline ne doit pas régresser ;
- un comportement initialement non conforme peut rester non conforme ou s'améliorer ;
- son passage à `PASS` constitue une amélioration, pas une régression ;
- l'oracle n'est jamais modifié pour normaliser le comportement observé.

- [ ] **Étape 0.9 — Consigner la baseline dans un rapport dédié**

Créer `docs/v2.1/RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_<AAAA-MM-JJ>.md`, contenant :

1. le commit exact de `en_cours/` sur lequel la baseline est établie, `git diff --name-only -- en_cours/` vide, et l'environnement d'exécution de référence (`david`, `/home/david/.claude` fraîchement initialisé pour cette phase de test, distinct de la session de développement Opus/Superpowers) ;
2. le SHA-256 de chaque copie isolée, ou à défaut la preuve d'identité avec `en_cours/` ;
3. pour chacun des 15 runs : scénario, stimulus envoyé, relances, réponse verbatim, fichiers lus, verdict, et la clause d'oracle appliquée ;
4. les reruns éventuels et leur résultat ;
5. le tableau de synthèse des 14 verdicts + C0 ;
6. la mention explicite que **NOY014_1 et NOY014_2 sont suspendus hors baseline** jusqu'à leur redesign (§9), avec le motif : fixtures non discriminantes (R1-b, R1-e) ;
7. le statut de chaque exécution : **run de référence** lorsqu'elle est jouée dans l'environnement de test propre `david` / `/home/david/.claude` défini en §8.2, distinct de la session de développement Opus/Superpowers, ou **diagnostic** lorsqu'elle est jouée hors de cet environnement ;
8. la liste des dettes d'instrumentation constatées, s'il y en a.

Ce rapport est la référence de comparaison de **tous** les lots suivants. Aucune affirmation de non-régression ultérieure ne peut s'appuyer sur le dry-run pré-refactorisation.

- [ ] **Étape 0.10 — Commit**

```bash
git add scripts/controle_statique_refactoring.sh docs/v2.1/RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_*.md docs/historique_2.1.md
git commit -m "Add behavioral baseline and static control script before V2.1 core refactoring"
```

**Contrôle de sortie du lot 0 — quatre conditions cumulatives :**

1. baseline statique enregistrée ;
2. **les 14 scénarios joués, collectés et scorés**, verbatims conservés ;
3. **C0 conforme** — `Activité` → `Étape 1` / `Étape 2`, aucun `Micro-activité`. Si C0 produit `Micro-activité`, **arrêter** : le contraste I25 n'est plus établi, et les lots A.10 et B ainsi que tout le §9 sont à revoir ;
4. rapport de baseline committé.

Tant que ces quatre conditions ne sont pas réunies, **ne pas commencer le lot A**.

---

## LOT A — Dé-duplication à doctrine strictement constante

Le lot le plus sûr : aucune règle n'est créée, modifiée ou supprimée. Seules des **paraphrases** deviennent des **pointeurs**.

**Fichiers :** `en_cours/SKILL.md`, `en_cours/references/glossaire.md`, `en_cours/references/taxonomie.md`, `en_cours/references/activite.md`.

- [ ] **Étape A.1 — `SKILL.md` l. 30 : supprimer la paraphrase et l'exemple (P2)**

Remplacer :

```
Pour une preuve externe rapportée, appliquer `references/taxonomie.md` §2 : une observation précise peut être recevable ; une affirmation vague telle que « il l'a déjà fait et ça marchait » reste insuffisante pour attester un palier.
```

par :

```
Pour une preuve externe rapportée, appliquer `references/etat_des_paliers.md` sans en réinterpréter les conditions ici.
```

*Raison :* P2. `SKILL.md` l. 26 interdit déjà de réinterpréter les conditions localement ; la l. 30 le faisait. La source canonique devient `etat_des_paliers.md`, qui porte les fondements.

*Invariants protégés :* I01, I05. *Risque :* faible — l'agent perd un exemple mais garde le pointeur ; le renvoi devient plus précis (`etat_des_paliers.md` au lieu de `taxonomie.md` §2).

*Contrôle :* `grep -c "il l'a déjà fait" en_cours/SKILL.md` → 0.

- [ ] **Étape A.2 — `taxonomie.md` A3 l. 120 : pointer au lieu de dupliquer (P2)**

Remplacer le paragraphe « Une preuve externe rapportée par l'utilisateur ou le formateur peut en revanche être recevable… » (l. 120, jusqu'à « …observée par Claude lui-même. ») par :

```
Une preuve externe rapportée peut en revanche être recevable selon les conditions de `etat_des_paliers.md` (« Fondements d'un palier attesté »). La règle porte sur la nature et la précision de la preuve, pas sur le fait qu'elle ait été observée par Claude lui-même.
```

*Raison :* P2. Conserve la clause de non-exigence d'observation directe (utile ici, car A3 parle de prérequis) et délègue les conditions.

*Invariants :* I05. *Risque :* moyen — NOY001 teste cette zone. À rejouer.

### Canonisation de la chaîne d'alignement — étapes A.3 à A.7 (P1)

Les quatre étapes suivantes forment un bloc : **elles se font ensemble ou pas du tout.** Retirer une variante sans avoir établi la source canonique laisserait un trou doctrinal.

Ordre impératif : établir la source canonique (A.3) **avant** de transformer les trois autres en pointeurs (A.4, A.5, A.6), puis contrôler (A.7).

- [ ] **Étape A.3 — Établir la chaîne canonique complète dans `opo.md` (P1)**

`opo.md` est le porteur légitime : son objectif déclaré est « Définir la règle des 3C et l'alignement objectif / activité / évaluation ».

La chaîne canonique doit être l'**union** des quatre variantes, sans perte. Elle intègre notamment les deux maillons que seul `taxonomie.md` A4 portait — `portée de la preuve` et `attestation / feedback / remédiation` — et le maillon `tâche réellement demandée` que seul `SKILL.md` portait.

Dans `opo.md`, à la fin de la section « 3. Contrôles avant de proposer une activité évaluée », ajouter :

```markdown
### Chaîne d'alignement de référence

La chaîne complète, utilisée par tout le skill, est :

```text
objectif observable
→ tâche réellement demandée
→ production ou performance observable
→ critères de réussite
→ preuve
→ portée de la preuve
→ conclusion permise : attestation, feedback ou remédiation
```

Ne pas conclure à un niveau que la preuve ne permet pas d'établir. La portée de la preuve est traitée dans `etat_des_paliers.md` ; la quantification éventuelle relève de `taxonomie.md` §2, clause A4.
```

*Raison :* P1. Crée la source unique dont A.4, A.5 et A.6 ont besoin.

*Invariants :* I18, et préservation de I12/I14 (portée) et I07 (attestation) via les deux maillons repris de A4.

*Risque :* faible — ajout pur, aucune règle retirée à ce stade.

*Contrôle :* `grep -c "portée de la preuve" en_cours/references/opo.md` → 1.

- [ ] **Étape A.4 — `glossaire.md` l. 236 : retirer la règle normative (P1, P4)**

Remplacer :

```
Repère utilisé par le skill :

Objectif → tâche → production/performance → critères → preuve → conclusion.
```

par :

```
La chaîne d'alignement de référence et ses contrôles sont définis dans `opo.md`.
```

*Raison :* le glossaire déclare l. 9 ne pas porter les règles détaillées. Il en portait une.

*Invariants :* I18. *Risque :* faible.

- [ ] **Étape A.5 — `SKILL.md` l. 105-112 : transformer la chaîne en pointeur (P1)**

Remplacer le bloc :

```
Lorsque la tâche implique apprentissage ou évaluation, vérifier notamment :

```text
objectif
→ tâche réellement demandée
→ production ou performance observable
→ critères
→ preuve disponible
→ conclusion permise
```

Ne pas conclure à un niveau que la preuve ne permet pas d'établir.
```

par :

```
Lorsque la tâche implique apprentissage ou évaluation, vérifier l'alignement complet selon la chaîne de référence de `references/opo.md`, et ne pas conclure à un niveau que la preuve ne permet pas d'établir.
```

*Raison :* P1. La phrase « Ne pas conclure à un niveau que la preuve ne permet pas d'établir » est **conservée dans `SKILL.md`** : c'est une interdiction directe, pas un maillon de chaîne, et sa visibilité au niveau du noyau est utile.

*Invariants :* I18, I03.

**Risque élevé et spécifique — R2 (perte de visibilité).** C'est le cas le plus exposé du lot A : la chaîne était jusqu'ici lisible sans ouvrir aucune référence. Après cette étape, l'agent doit charger `opo.md` pour connaître les maillons. `opo.md` figure bien dans « Sources de vérité » (l. 92), mais rien ne garantit qu'il soit chargé sur une tâche qui ne semble pas porter sur la formulation d'objectifs.

*Repli documenté si NOY004 régresse en A.7 :* restaurer dans `SKILL.md` une forme **compressée sur une seule ligne** de la chaîne canonique — identique dans ses maillons à celle d'`opo.md`, donc non concurrente — et accepter cette duplication contrôlée. Consigner l'écart. Ne pas revenir à l'ancienne variante à six maillons divergents.

- [ ] **Étape A.6 — `taxonomie.md` A4 l. 178-187 : transformer la chaîne en pointeur (P1)**

Remplacer :

```
En l'absence de barème demandé ou imposé, la chaîne par défaut est :

```text
objectif observable
→ production ou comportement
→ critères de réussite
→ preuve
→ portée de la preuve
→ attestation / feedback / remédiation
```
```

par :

```
En l'absence de barème demandé ou imposé, appliquer la chaîne d'alignement de référence définie dans `opo.md`.
```

*Raison :* P1. Les deux maillons propres à cette variante (`portée de la preuve`, `attestation / feedback / remédiation`) ont été intégrés à la chaîne canonique en A.3 : le pointeur ne perd donc rien.

**Vérifier avant de supprimer** que A.3 est bien faite :

```bash
grep -c "portée de la preuve" en_cours/references/opo.md   # doit valoir 1 AVANT cette étape
```

Si ce contrôle renvoie 0, **ne pas exécuter A.6** : la suppression provoquerait une perte doctrinale sur I12/I14.

*Invariants :* I18, I20, et indirectement I12, I14, I07.

*Risque :* moyen. A4 reste par ailleurs intégralement en place — seule la chaîne terminale devient un pointeur.

- [ ] **Étape A.7 — Contrôle comportemental immédiat de la canonisation**

Rejouer, en contexte neuf et aveugle : **NOY004** (alignement objectif / tâche / preuve / critère), puis **NOY002** et **NOY007**.

Justification du triplet : NOY004 teste directement I18/I19 ; NOY002 teste la compatibilité preuve/palier, qui dépend du maillon `portée de la preuve` ; NOY007 teste A4, dont la chaîne terminale vient d'être remplacée.

Attendu : aucun comportement conforme de la baseline du lot 0 ne régresse. Si l'un de ces scénarios était initialement non conforme dans la baseline, son résultat est évalué contre l'oracle : un passage à `PASS` est une amélioration, pas une régression.

**Si NOY004 régresse :** appliquer le repli documenté en A.5 (chaîne compressée sur une ligne dans `SKILL.md`), puis rejouer NOY004. Ne pas empiler d'autres modifications avant de l'avoir rétabli. Si NOY002 ou NOY007 régresse sans que NOY004 régresse, suspecter A.6 plutôt que A.5 et reverter A.6 seule (l'étape `taxonomie.md`, pas celle de I25).

- [ ] **Étape A.8 — `glossaire.md` : remplacer les redéfinitions structurelles par des renvois (P4)**

Dans la section « Structure pédagogique » (l. 13-43), remplacer les définitions de `Module`, `Séquence`, `Séance`, `Activité`, `Granularité` par des entrées courtes se terminant par un renvoi unique.

**Le glossaire ne doit conserver aucune formulation de la règle `R-GRAN`.** Il décrit ce qu'est une Activité ; il ne reprend pas sa position dans le découpage. Formulation exacte à employer pour `Activité` :

```
### Activité

Ce que l'apprenant doit effectivement faire.

Sa position dans le découpage et son articulation avec les autres niveaux sont définies dans `decoupage_pedagogique.md` §1.
```

Retirer donc explicitement de `glossaire.md` l. 35 le segment « Granularité la plus fine : ». De même, l'entrée `Granularité` (l. 39-43) ne doit plus énoncer de règle : conserver la définition du terme et renvoyer, pour les règles de non-déduction (durée, difficulté, modalité), à `decoupage_pedagogique.md` §2.

Faire de même pour la section « Modalités et organisation » (l. 240-267) : conserver les entrées de vocabulaire, renvoyer à `decoupage_pedagogique.md` §2 pour les règles d'indépendance des axes.

*Raison :* P4, et **prérequis de A.10** : si le glossaire conservait « granularité la plus fine », I25 resterait porté par deux sources après A.10 et CS3 contredirait l'objectif du lot.

*Invariants :* I23, I24, I25. *Risque :* moyen — NOY009 et NOY011 lisent parfois le glossaire. À rejouer.

*Contrôle immédiat :* `grep -c "granularité la plus fine" en_cours/references/glossaire.md` → **0**.

- [ ] **Étape A.9 — I26 : une seule source (P9)**

`activite.md` l. 41 reste la source. Dans `SKILL.md` l. 75, remplacer :

```
Les `typical_uses` sont des indices de sélection, pas des conditions exclusives. Ne pas charger systématiquement tous les gabarits pour choisir.
```

par :

```
Ne pas charger systématiquement tous les gabarits pour choisir. Le statut des `typical_uses` est défini dans `references/activite.md`.
```

Dans `glossaire.md` l. 388, remplacer l'énoncé par un renvoi à `activite.md`.

*Raison :* P9. *Invariants :* I26. *Risque :* moyen — NOY009, NOY011.

- [ ] **Étape A.10 — I25 : une seule source (P8)**

`decoupage_pedagogique.md` l. 69 reste la source. Dans `activite.md` l. 7, remplacer :

```
Une Activité est la granularité la plus fine du découpage pédagogique : c'est ce que l'apprenant doit effectivement faire.
```

par :

```
Une Activité est ce que l'apprenant doit effectivement faire. Sa position dans le découpage est définie dans `decoupage_pedagogique.md` §1.
```

**Prérequis :** A.8 doit être faite avant A.10. Sinon `glossaire.md` conserverait la formulation et I25 resterait à deux porteurs.

*Raison :* P8. **Risque élevé et spécifique :** I25 est le contraste de C0 et NOY014. Cette étape fait passer le nombre de porteurs de trois (`decoupage_pedagogique.md`, `activite.md`, `glossaire.md`) à un seul — or C0 avant refactoring a lu `activite.md` **et pas** `decoupage_pedagogique.md`. Cette étape pourrait donc affaiblir le contraste pour les trajectoires qui n'ouvrent pas `decoupage_pedagogique.md`.

*Contrôle obligatoire immédiat :* rejouer C0 après cette seule étape. Attendu : `Étape`, pas de `Micro-activité`.

*Si C0 régresse :* ne pas reverter A.8 (le glossaire n'a pas à porter une règle normative). Reverter **A.10 seule** et conserver la formulation d'`activite.md` comme second porteur assumé de `R-GRAN` — une duplication bénigne vaut mieux qu'un invariant affaibli (décision D4). Dans ce cas, CS3 attendra **2** porteurs et non 1 : consigner l'écart et sa raison, sans le traiter comme un échec de lot.

*Contrôle :* après A.8 et A.10, `grep -rc "granularité la plus fine" en_cours/` doit ne montrer qu'un seul fichier : `references/decoupage_pedagogique.md`.

- [ ] **Étape A.11 — Contrôle statique du lot A**

```bash
./scripts/controle_statique_refactoring.sh > /tmp/apres_lot_A.txt
diff /tmp/baseline_statique.txt /tmp/apres_lot_A.txt
```

Attendu : CS1 à 0 occurrence, CS2 réduit à 1 seul porteur (`opo.md`), CS3 réduit à 1 (sauf si A.10 revertée, cf. D4), CS4 réduit à 1.

- [ ] **Étape A.12 — Non-régression comportementale du lot A**

Rejouer, en contextes neufs et aveugles, une copie neuve par scénario : **NOY001, NOY002, NOY004, NOY005, NOY007, NOY008, NOY009, NOY011, NOY013** et **C0**.

Justification du sous-ensemble : le lot A touche la preuve externe rapportée (NOY001), la compatibilité preuve/palier (NOY002), la chaîne d'alignement (NOY004), la portée (NOY005), la clause A4 (NOY007), l'héritage et le routage des gabarits (NOY008, NOY009, NOY011), le palier 0 (NOY013) et la granularité (C0).

NOY002, NOY004 et NOY007 ont déjà été joués en A.7 ; les rejouer ici vérifie qu'aucune étape ultérieure (A.8 à A.10) ne les a fait basculer.

Attendu : **aucun comportement conforme de la baseline du lot 0 ne doit régresser**. Pour tout scénario initialement non conforme, le résultat est évalué contre l'oracle : un passage à `PASS` est une amélioration et ne doit pas être rejeté au motif qu'il diffère de la baseline. La photographie du dry-run pré-refactorisation n'est pas l'étalon de comparaison.

- [ ] **Étape A.13 — Commit**

```bash
git add en_cours/ docs/historique_2.1.md
git commit -m "Refactor V2.1 core: deduplicate normative rules into single sources"
```

**Contrôle de sortie du lot A :** aucun scénario conforme dans la baseline ne doit basculer vers une non-conformité. Un tel basculement → reverter l'étape responsable, ne pas empiler. Un scénario initialement non conforme qui passe à `PASS` est une amélioration et ne constitue pas une régression.

> **Zone de danger.** Le lot A ne change aucune doctrine. Si un NOY bascule, la cause est un **déplacement de visibilité** (P-risque R2 au §10), pas un changement de règle. Diagnostiquer avant de reformuler.

---

## LOT B — Périmètre et préséance

Ce lot change **la doctrine d'implémentation** de la préséance (pas la doctrine G02 elle-même) et **ne touche aucun oracle ni fixture**.

**Fichiers :** `en_cours/SKILL.md`. Éventuellement `en_cours/references/activite.md` (§ rôle du front matter).

- [ ] **Étape B.1 — Borner la maxime de la l. 99 à son axe réel (P5)**

Remplacer :

```
Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, la référence normative spécialisée fait foi.
```

par :

```
Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, c'est la référence normative qui porte cette règle, pas le glossaire. Ceci ne règle pas les conflits entre règles — voir « Périmètre et préséance ».
```

*Raison :* P5. Supprime « fait foi » et le mot « spécialisée », qui portaient la transposition *lex specialis*, et renvoie explicitement l'axe des conflits à la section dédiée.

*Invariants :* I32. *Risque :* faible seul ; c'est B.2 qui porte l'effet.

- [ ] **Étape B.2 — Remplacer la l. 120 par une section « Périmètre et préséance » (P6, P7, P12)**

Retirer le bloc de la l. 120 de la section « Contrôles avant réponse ou livraison » et créer une section propre en fin de `SKILL.md` :

```markdown
## Périmètre et préséance

Une règle ne prévaut sur une autre règle du skill que si son fichier le **déclare** dans son front matter :

```yaml
deroge_a: [A3]        # la ou les règles auxquelles ce fichier déroge, par leur identifiant
perimetre: tutorat    # borne de portée ; requis dès que deroge_a est présent
```

En l'absence de `deroge_a:`, aucune dérogation n'a lieu : la règle contredite tient. Cela vaut quel que soit le degré de spécialisation du fichier, qu'il déclare ou non un périmètre, et qu'il mentionne ou non la règle qu'il contredit.

Une dérogation déclarée ne vaut que dans son périmètre. Elle ne modifie pas la règle à laquelle elle déroge et ne s'étend à aucun autre périmètre.

Un `deroge_a:` sans `perimetre:`, ou citant un identifiant absent de l'index ci-dessous, est une déclaration invalide : elle ne produit aucune dérogation.

Règles dérogeables identifiées :

| ID | Règle | Source |
|---|---|---|
| `A3` | Budget de nouveauté = 1 pour une activité évaluée | `references/taxonomie.md` §2 |
| `R-GRAN` | `Activité` est la granularité la plus fine | `references/decoupage_pedagogique.md` §1 |

Si une contradiction pertinente n'est pas résolue par ce mécanisme : **ne pas arbitrer silencieusement ; la signaler**.
```

*Raison :* P6 (le pôle de gauche devient instanciable — c'est la règle nommée par son ID, sans aucune classification à inférer), P7 (le marqueur est défini et vérifiable), P12 (la préséance quitte les contrôles de livraison).

*Invariants :* I30, I31, I32. La clause de signalement est conservée **mot pour mot**.

*Neutralité sur l'existant :* aucune référence actuelle ne porte `deroge_a:`. Cette étape ne modifie donc le comportement d'aucune référence en place et ne reclassifie rien.

*Risque élevé :* c'est le seul endroit où la doctrine d'implémentation change. Voir §10 R5.

*Contrôles statiques obligatoires :*

```bash
grep -c "ne pas arbitrer silencieusement ; la signaler" en_cours/SKILL.md   # doit valoir 1
grep -c "règle générale du skill" en_cours/SKILL.md                        # doit valoir 0
grep -n "avant toute décision\|vérifier s'il existe\|rechercher" en_cours/SKILL.md  # doit être vide
grep -c "deroge_a" en_cours/SKILL.md                                       # doit valoir >= 1
grep -rn "deroge_a" en_cours/references/                                   # doit être VIDE : aucune référence ne déroge encore
grep -c "R-GRAN" en_cours/SKILL.md                                         # doit valoir 1
```

- [ ] **Étape B.3 — Poser les deux identifiants à leur source (P7)**

Les IDs doivent être trouvables depuis la règle, pas seulement depuis l'index.

Dans `taxonomie.md`, le titre de la clause A3 porte déjà son identifiant (`### A3 — Budget de nouveauté = 1`) : **ne rien modifier**.

Dans `decoupage_pedagogique.md` §1, sous-section `Activité`, remplacer :

```
L'Activité est la granularité la plus fine : la tâche effectivement proposée à l'apprenant.
```

par :

```
L'Activité est la granularité la plus fine : la tâche effectivement proposée à l'apprenant. *(règle `R-GRAN`)*
```

*Raison :* rendre l'ID trouvable dans les deux sens sans créer de registre externe. Modification d'un seul segment de phrase ; la formulation de la règle est inchangée.

**Risque spécifique :** cette ligne est le porteur du contraste I25, lu par C0 et NOY014. L'ajout est purement suffixal et ne touche pas la proposition. Rejouer C0 immédiatement après cette étape seule.

*Contrôle :* `grep -c "granularité la plus fine" en_cours/references/decoupage_pedagogique.md` → inchangé.

- [ ] **Étape B.4 — Aligner `activite.md` sur la convention**

Dans `activite.md`, section « Rôle du front matter » (l. 28-41), ajouter une puce à la liste de ce que le front matter permet d'identifier :

```
- une éventuelle dérogation déclarée et son périmètre.
```

*Raison :* le mécanisme de B.2 s'appuie sur le front matter ; `activite.md` est le fichier qui en définit déjà le rôle. Mentionner l'existence du champ, **sans** redire la règle de préséance.

*Contrôle :* `grep -c "prévaut\|préséance" en_cours/references/activite.md` → 0. La règle de préséance ne doit exister qu'à un seul endroit.

- [ ] **Étape B.5 — Contrôle statique du lot B**

```bash
./scripts/controle_statique_refactoring.sh
```

Attendu : CS6 à 0 occurrence, CS9 « OK ».

- [ ] **Étape B.6 — Non-régression comportementale du lot B**

Rejouer, en contextes neufs et aveugles, **les 14 scénarios** : NOY001 à NOY011, NOY012_1, NOY012_2, NOY013 — plus **C0**.

Justification : B.2 modifie une règle transverse d'orchestration ; son effet de bord potentiel n'est pas circonscrit à une famille.

**Ne pas rejouer NOY014_1 / NOY014_2 comme critère de succès de ce lot** : leurs fixtures signalent la dérogation en prose et non en front matter, donc elles ne testent plus le mécanisme cible. Les jouer pour information est autorisé ; les compter comme verdict ne l'est pas.

Attendu : **aucune régression par rapport aux comportements conformes de la baseline**, C0 conforme. L'objectif de stabilisation finale reste 14/14 PASS (§11) ; si un scénario était initialement non conforme, son amélioration vers `PASS` est acceptée et recherchée sans modification de l'oracle.

- [ ] **Étape B.7 — Commit**

```bash
git add en_cours/ docs/historique_2.1.md
git commit -m "Refactor V2.1 core: declare scope in front matter for rule precedence"
```

**Contrôle de sortie du lot B :** aucun comportement conforme de NOY001-NOY013 dans la baseline ne régresse et C0 reste conforme. Un comportement initialement non conforme peut s'améliorer vers `PASS`. NOY014 est explicitement hors critère.

> **Zone de danger maximale.** Ne jamais exécuter le lot B et le chantier d'instrumentation NOY014 (§9) dans le même cycle. Le lot B change le runtime ; §9 change l'instrument. Les faire ensemble rendrait impossible d'attribuer un changement de verdict.

---

## LOT C — Relocalisation des règles mal placées

**Fichiers :** `en_cours/references/decoupage_pedagogique.md`, nouveau `en_cours/references/production_documentaire.md`, `en_cours/SKILL.md`, `en_cours/references/taxonomie.md`, `en_cours/references/etat_des_paliers.md`.

- [ ] **Étape C.1 — Extraire `decoupage_pedagogique.md` §4 (P11)**

Créer `en_cours/references/production_documentaire.md` :

```markdown
---
objectif: "Définir les conventions de production d'une fiche pédagogique : périmètre, niveau de détail et séparation apprenant / formateur."
---

# Production documentaire

## Respecter le périmètre et la granularité demandés

Une demande de fiche de Séance ne devient pas le programme du Module. Une fiche de Séquence ne contient pas les énoncés complets des activités.

## Adapter le niveau de détail

- fiche de Séquence : intentions, objectifs, articulations, activités prévues ;
- fiche de Séance : déroulé suffisamment précis pour être piloté ;
- fiche d'Activité : tâche, conditions, productions attendues et critères.

## Séparation apprenant / formateur

Lorsque l'activité est évaluée, les critères de réussite restent explicites pour l'apprenant. Une solution, une correction, une production de référence donnant la solution ou des attendus détaillés de correction ne sont pas révélés avant sa production.

## Conventions de rédaction

Callouts disponibles : **Bon à savoir** (contexte ou choix de conception), **Vigilance** (limite ou point d'attention), **Important** (objection prévisible). Un callout n'est jamais obligatoire.

## Réflexe andragogique

Le document rend perceptible la finalité de l'apprentissage et laisse une autonomie adaptée au contexte (`andragogie.md`).
```

Puis, dans `decoupage_pedagogique.md`, remplacer tout le §4 (l. 143-167) par :

```
## 4. Production des fiches

Les conventions de production d'une fiche — périmètre, niveau de détail, séparation apprenant / formateur, callouts — sont définies dans `production_documentaire.md`.

Les règles relatives aux paliers, aux preuves, au budget de nouveauté et aux activités évaluées restent définies par `taxonomie.md` et `etat_des_paliers.md`.
```

Enfin, ajouter la nouvelle référence à la liste « Sources de vérité » de `SKILL.md` :

```
- `references/production_documentaire.md` — périmètre, niveau de détail et séparation apprenant / formateur d'une fiche ;
```

*Raison :* P11. *Invariants :* I21, I28.

**Risque élevé et spécifique :** I21 est l'invariant de NOY010, et il est actuellement porté par trois fichiers (`decoupage_pedagogique.md` l. 155, `activite.md` l. 91, `quiz.md`). Cette étape le déplace mais **ne retire rien** de `activite.md` ni de `quiz.md` : la dispersion est conservée volontairement à ce stade. Ne pas « nettoyer » les deux autres emplacements dans ce lot.

*Contrôle obligatoire :* rejouer **NOY010** immédiatement après cette étape seule.

- [ ] **Étape C.2 — Dé-dupliquer A2 ↔ `etat_des_paliers.md` (P10)**

Dans `taxonomie.md`, remplacer les deux « conséquences opératoires » de A2 (l. 105-108) par :

```
Deux conséquences opératoires :

1. **Avant de proposer une activité évaluée, Claude énumère les notions qu'elle mobilise** et le palier attesté de chacune. Une activité dont les notions mobilisées ne peuvent pas être identifiées n'est pas prête à être proposée.
2. **Claude tient un état des paliers visible** — le format, les règles de tenue et le protocole de persistance sont définis dans `etat_des_paliers.md`.
```

Dans `etat_des_paliers.md`, remplacer la section « Ce que ce tableau sert à calculer » (l. 134-136) par :

```
## Ce que ce tableau sert à calculer

Avant chaque activité évaluée : lister les notions mobilisées, lire leur palier ici, compter celles qui sont sous le palier requis. Le seuil applicable est celui de la clause A3 (`taxonomie.md` §2). Sans ce tableau, ce comptage est impossible.
```

*Raison :* P10 — retire la re-narration du seuil A3 (« s'il y en a plus d'une, l'activité est refusée ») depuis `etat_des_paliers.md`, qui n'en est pas la source.

*Invariants :* I11, I16. *Risque :* moyen — NOY003 teste A3. À rejouer.

- [ ] **Étape C.3 — Contrôle statique et comportemental du lot C**

```bash
./scripts/controle_statique_refactoring.sh
grep -rn "l'activité est refusée" en_cours/references/   # doit n'apparaître que dans taxonomie.md
```

Rejouer, en contextes neufs et aveugles : **NOY003, NOY007, NOY010** et **C0**.

- [ ] **Étape C.4 — Commit**

```bash
git add en_cours/ docs/historique_2.1.md
git commit -m "Refactor V2.1 core: move document production rules to their own reference"
```

**Contrôle de sortie du lot C :** aucun comportement conforme de NOY003, NOY007 ou NOY010 dans la baseline ne régresse. Un comportement initialement non conforme peut s'améliorer vers `PASS`.

---

## LOT D — Split de `taxonomie.md` (OPTIONNEL — décision humaine requise)

**Ne pas exécuter sans accord explicite.** Voir §12, décision D2.

Ce lot sépare l'échelle (aide d'interprétation) des clauses A1-A4 (invariants noyau), traitant P3.

Coût : 8 renvois « `taxonomie.md` §2, clause A4 » répartis sur 7 fichiers doivent être mis à jour. Risque de renvoi cassé silencieusement.

- [ ] **Étape D.1 — Créer `en_cours/references/activite_evaluee.md`** contenant l'intégralité du §2 actuel de `taxonomie.md` (clauses A1, A2, A3, A4, avec leurs justifications et exemples), sans reformulation.

- [ ] **Étape D.2 — Réduire `taxonomie.md`** au §1 (échelle, verbes, transposition), et ajouter en tête : `Les garde-fous des activités évaluées (A1 à A4) sont définis dans `activite_evaluee.md`.`

- [ ] **Étape D.3 — Mettre à jour les 8 renvois.** Liste exhaustive à traiter :

```bash
grep -rn "taxonomie.md\` §2" en_cours/
```

Fichiers concernés : `opo.md`, `activite.md`, `glossaire.md`, `activites_type/quiz.md`, `activites_type/brique.md`, `activites_type/atelier.md`, `activites_type/recul.md`, plus `SKILL.md` (renvois généraux à `§2`), `sequence.md`, `seance.md`, `syllabus.md` à vérifier.

- [ ] **Étape D.4 — Contrôle de renvois orphelins**

```bash
grep -rn "taxonomie.md\` §2" en_cours/   # doit être vide
grep -rn "activite_evaluee.md" en_cours/ | wc -l  # doit valoir >= 8
```

- [ ] **Étape D.5 — Non-régression complète** : les 14 scénarios (NOY001 à NOY011, NOY012_1, NOY012_2, NOY013) + C0.

- [ ] **Étape D.6 — Commit.**

---

# 8. Stratégie de non-régression

## 8.1 Deux natures de contrôle

| Type | Outil | Ce qu'il prouve |
|---|---|---|
| Contrôle statique | `grep`, script du lot 0 | qu'une duplication a disparu, qu'un ancrage n'est pas cassé, qu'aucun gate n'est introduit |
| Run comportemental | scénario NOY en contexte neuf et aveugle | que l'invariant tient réellement |

**Un contrôle statique ne prouve jamais un comportement** (R1-f). Toute affirmation de non-régression doit s'appuyer sur un run.

**La référence de comparaison est la baseline du lot 0**, consignée dans `RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_<date>.md` — jamais la photographie du dry-run pré-refactorisation, qui n'a pas conservé de verbatims, n'a pas exécuté C0, et comptait `NOY014_2` comme un PASS informatif alors qu'il est vacuous.

## 8.2 Conditions de run

Chaque run exige : condition A, copie neuve du candidat, contexte neuf, exécutant ne connaissant pas l'oracle, stimulus exact, verbatim conservé. `NOY014_1` et `NOY014_2` jamais dans la même conversation.

**Persona (corrigé le 2026-08-23).** La rédaction initiale de ce paragraphe exigeait « aucun persona ». Cette exigence est erronée : elle contredit huit fiches autoritatives. NOY001 à NOY004 prescrivent `validation/personas/apprenant.md` ou `validation/personas/formateur.md`, et NOY008 à NOY011 prescrivent `validation/personas/formateur.md` ; pour NOY002, NOY004 et NOY008 à NOY011, la présence du persona est une clause de **« Validité technique »** — un run sans persona n'y est pas `FAIL`, il est techniquement invalide.

Règle retenue : **le persona est injecté exactement lorsque la fiche le prescrit, et jamais autrement.** Aucun persona implicite n'est ajouté aux autres scénarios. NOY005, NOY006, NOY007, NOY012_1, NOY012_2, NOY013 et C0 s'exécutent donc sans persona, plusieurs de ces fiches l'excluant explicitement. L'injection suit le mécanisme de la campagne V2 (`validation/v2/operateur/PARAMETRES_EXECUTION.md`) : copie dans `workspace/persona.md` et `--append-system-prompt-file`.

Deux environnements doivent rester strictement séparés :

1. **Environnement d'implémentation** : la session de développement d'Opus, avec les outils et skills nécessaires au travail de refactoring, notamment Superpowers. Cette session n'est jamais utilisée comme exécutant d'un run de référence.
2. **Environnement de test de référence** : sous l'utilisateur Linux **`david`**, avec un **`/home/david/.claude` fraîchement réinitialisé pour la phase de test** : aucun skill, mémoire, plugin, hook, agent, commande ou personnalisation étrangère au candidat ne doit y être présent.

Il ne s'agit donc pas de conserver le même `/home/david/.claude` en continu avant, pendant et après le refactoring. Le protocole est : **réinitialiser proprement l'environnement de test pour la baseline, restaurer/utiliser l'environnement de développement pour l'implémentation Opus, puis recréer le même état propre de test avant chaque phase de contrôle comportemental de référence**. La comparabilité porte sur la configuration reproduite, pas sur la persistance physique du même répertoire.

**Environnement de test (corrigé le 2026-08-23).** La réinitialisation physique de `/home/david/.claude` n'est pas retenue : elle détruirait puis restaurerait l'environnement de la session de développement à chaque phase de contrôle. Le « mécanisme équivalent » ouvert par la phrase ci-dessus est utilisé à la place — un `CLAUDE_CONFIG_DIR` dédié par run, ne reprenant du profil de développement que `.credentials.json`. Vérifié au préflight : aucun `CLAUDE.md`, skill, plugin, hook, agent, commande ni mémoire hérité, candidat seul skill utilisateur, `/home/david/.claude` inchangé (empreinte avant/après identique). Limite subsistante, commune aux deux recettes : les skills intégrés au binaire restent présents. Recette figée dans `scripts/run_isole.sh`, documentée dans `validation/v2.1/baseline/README.md`.

Des runs joués dans des sous-contextes de la session de développement valent comme **diagnostic**, pas comme runs de référence.

## 8.3 Quels NOY après quel lot

| Lot | NOY à rejouer | C0 | Justification |
|---|---|---|---|
| 0 | **les 14 (baseline complète, verbatims conservés)** | oui | établir le point zéro comportemental ; NOY014 suspendu hors baseline |
| A | NOY001, NOY002, NOY004, NOY005, NOY007, NOY008, NOY009, NOY011, NOY013 | oui | zones touchées : preuve rapportée, compatibilité preuve/palier, alignement, portée, A4, gabarits, palier 0, granularité |
| A.7 (canonisation chaîne) | **NOY004, NOY002, NOY007 immédiatement** | — | I18 quitte `SKILL.md` : R2 maximal |
| A.10 seule | — | **oui, immédiatement** | I25 passe de trois porteurs à un |
| B | **les 14 (NOY001-NOY011, NOY012_1, NOY012_2, NOY013)** | oui | règle transverse d'orchestration, effet de bord non circonscrit |
| B.3 seule | — | **oui, immédiatement** | l'ID `R-GRAN` est posé sur le porteur du contraste I25 |
| C.1 seule | **NOY010 immédiatement** | — | I21 est déplacé |
| C | NOY003, NOY007, NOY010 | oui | A3, notation, exposition |
| D (si retenu) | les 14 | oui | 8 renvois normatifs déplacés |

## 8.4 Règle d'or de séquencement

Ne jamais modifier dans le même cycle :

1. la **doctrine** (ce que le skill doit faire) ;
2. l'**implémentation** (comment le runtime l'exprime) ;
3. l'**oracle / l'instrument** (comment on le mesure).

Application concrète à ce plan :

- lots A et C : implémentation seule → doctrine et oracle intacts ;
- lot B : implémentation + doctrine d'implémentation → oracle strictement intact ;
- chantier §9 : instrument seul → runtime strictement intact.

## 8.5 Quand le noyau est-il assez stable pour commencer V3 tutorat

Voir §11.

---

# 9. Traitement du chantier NOY014 / R1

## 9.1 Constat

`NOY014` ne peut pas servir de contrôle discriminant :

- son cas négatif est un quasi-positif (R1-b) ;
- son cas positif passe avec ou sans marqueur (R1-e) ;
- après le lot B, ses deux fixtures signalent la dérogation en **prose**, mécanisme que le runtime cible ne reconnaît plus.

## 9.2 Décision proposée

Traiter NOY014 comme un **chantier d'instrumentation séparé**, exécuté **après** le lot B, dans son propre cycle, sans aucune modification du runtime.

## 9.3 Contenu du chantier

1. **Retirer NOY014_1 et NOY014_2 de la batterie de non-régression** tant qu'ils ne sont pas redessinés. Ne pas les supprimer : les marquer comme suspendus, en conservant l'historique de leurs runs.
2. **Redessiner les fixtures** sur le mécanisme de front matter :
   - `mock_sans_derogation.md` : front matter `perimetre: MOCK-GRANULARITE`, **sans** `deroge_a:`. Retirer du corps la mention de la règle contredite (l. 11 actuelle) et la répétition de la limitation de portée (l. 13 actuelle), qui en faisaient un quasi-positif (R1-b).
   - `mock_avec_derogation.md` : même front matter **plus** `deroge_a: [R-GRAN]`. Retirer du corps le bloc « Dérogation explicite au noyau » : le signalement n'est plus en prose.
   - Les deux corps de texte doivent alors être **strictement identiques** — vérifier par `diff` en ignorant le front matter. La seule variable est le champ `deroge_a:`. C'est ce qui rend le test discriminant.
   - Employer l'ID `R-GRAN` de l'index, jamais une valeur libre décrivant la règle.
3. **Ajouter un contrôle C0-bis** : une référence déclarant `perimetre:` mais **sans conflit** ne doit rien changer au comportement (absence de sur-déclenchement).
4. **Ajouter un contrôle anti-gate** : vérifier sur un scénario de routage ordinaire (NOY009) que l'agent n'exécute aucune vérification de dérogation quand aucune référence à périmètre n'est en jeu.
5. **Ajouter deux contrôles de déclaration invalide** : `deroge_a:` sans `perimetre:`, et `deroge_a:` citant un ID absent de l'index. Attendu dans les deux cas : aucune dérogation, règle contredite maintenue.
6. **Ajouter un contrôle de non-extension hors périmètre** (décision D3) : une dérogation valide ne doit pas s'appliquer à une demande située hors du périmètre déclaré.
7. **Ne pas geler** NOY014 avant que C0, C0-bis, le contrôle anti-gate et les contrôles de déclaration invalide soient consignés.

## 9.4 Ce que le chantier ne doit pas faire

- Ne pas ajuster l'oracle pour absorber un comportement observé.
- Ne pas modifier le runtime pour faire passer une fixture.
- Ne pas réintroduire NOY014 dans le décompte de non-régression avant sa stabilisation.

---

# 10. Risques et garde-fous

| # | Risque | Probabilité | Gravité | Garde-fou |
|---|---|---|---|---|
| **R1** | Perte d'un invariant lors de la dé-duplication : la source canonique retenue est moins complète que la paraphrase supprimée. | moyenne | élevée | Chaque étape du lot A nomme l'invariant protégé. CS8 vérifie la présence textuelle des marqueurs d'invariants. Runs ciblés à chaque étape. |
| **R2** | **Perte de visibilité** : une règle déplacée vers une référence n'est plus lue au bon moment, alors qu'elle est toujours écrite. C'est le risque le plus insidieux — les contrôles statiques passent et le comportement change. | **élevée** | élevée | Ne jamais retirer un invariant de plusieurs porteurs dans le même lot (A.5, A.10, C.1). Contrôle comportemental immédiat après chaque étape de déplacement, avant d'enchaîner. |
| **R3** | Contradiction entre références après déplacement (deux fichiers énoncent une variante différente). | moyenne | moyenne | CS2/CS3/CS4 comptent les porteurs. Un porteur > 1 sur une règle canonisée = échec de lot. |
| **R4** | Sur-spécialisation du noyau en vue du tutorat : introduire dès maintenant des concepts V3. | faible | élevée | §2.2 liste les non-objectifs. Le lot B n'ajoute que `perimetre:`/`deroge_a:`, deux champs neutres. Aucun `tutorat.md` créé. |
| **R5** | Mécanisme de dérogation trop procédural : le front matter devient un gate déguisé (« vérifier le périmètre avant chaque référence »). | moyenne | élevée | La formulation de B.2 est **descriptive** (« le front matter déclare »), sans verbe d'obligation de recherche. CS9 interdit les verbes de recherche. Contrôle anti-gate au §9.3.4. |
| **R6** | Tests trop couplés au wording actuel : un NOY basculerait à cause d'une reformulation sans effet doctrinal. | moyenne | moyenne | Ne pas reformuler un oracle pour l'adapter. Si un NOY bascule sur une pure reformulation, c'est le NOY qui est fragile : le consigner comme dette d'instrumentation, sans le corriger dans le même cycle. |
| **R7** | **Faux sentiment de non-régression** : compter `NOY014_2` comme PASS alors qu'il est vacuous (R1-e), ou valider une étape par simulation sur table (R1-f). | **élevée** | élevée | NOY014 explicitement hors critère (lot B, §8.3). Interdiction de valider un comportement autrement que par un run réel. |
| **R8** | Le split de `taxonomie.md` casse un renvoi silencieusement. | moyenne | moyenne | Lot D optionnel, contrôle D.4 de renvois orphelins, non-régression complète. |
| **R9** | Dérive de périmètre : le refactoring absorbe des « améliorations » non demandées. | moyenne | moyenne | Chaque étape doit être rattachable à un `P*` du §5. Une modification sans `P*` correspondant est hors périmètre. |
| **R10** | Les runs servant de référence sont joués dans la session de développement d'Opus, ou l'environnement de test `david` n'est pas recréé dans le même état propre entre les phases de référence. | moyenne | moyenne | §8.2. Séparer strictement environnement d'implémentation et environnement de test ; recréer le même état propre de `/home/david/.claude` pour chaque phase de référence et distinguer explicitement diagnostic / run de référence dans tout rapport. |

---

# 11. Critères de sortie du refactoring

Le noyau V2.1 refactoré est considéré comme stable — et donc l'implémentation V3 tutorat peut commencer — lorsque **tous** les points suivants sont vrais :

1. Lots 0, A, B et C exécutés et committés séparément.
2. **Batterie hors NOY014 : 14/14 PASS.** Les 14 scénarios sont NOY001 à NOY011 (11), NOY012_1, NOY012_2 et NOY013. Joués en condition A, contextes neufs, sous l'utilisateur `david` avec un `/home/david/.claude` **recréé dans le même état propre que pour la baseline**, sur le candidat refactoré. La session de développement Opus/Superpowers n'est jamais utilisée comme exécutant de ces runs.
3. **C0 conforme** : sans fixture, l'agent produit `Étape`, jamais `Micro-activité`.
4. Contrôles statiques CS1 à CS9 au vert : plus aucune règle canonisée avec plus d'un porteur, aucun ancrage cassé, aucun verbe de gate.
5. **Chantier §9 terminé et NOY014 discriminant.** Les deux branches doivent être **PASS**, avec des corps de texte de fixture identiques et le champ `deroge_a:` pour seule variable :
   - **`NOY014_1` = PASS** — front matter **sans** `deroge_a:` : aucune dérogation n'a lieu, la règle `R-GRAN` tient, la production ne comporte **pas** de niveau `Micro-activité` ;
   - **`NOY014_2` = PASS** — front matter avec `deroge_a: [R-GRAN]` **et** `perimetre:` : la dérogation est valide, la règle locale s'applique **dans son seul périmètre**, la production comporte les `Micro-activités`.

   Ces deux PASS ne valent que conjointement : un PASS sur `NOY014_2` seul ne démontre rien (R1-e), et un PASS sur les deux avec des corps de texte différents ne démontre pas que `deroge_a:` est le discriminateur.
6. Contrôle anti-gate passé : aucun surcoût de vérification observable sur NOY009.
7. Test de non-extension hors périmètre : une référence fictive déclarant `perimetre:` et `deroge_a:` valides est respectée **dans** son périmètre et **ignorée hors** de son périmètre (non couvert par un NOY actuel — voir décision D3).
8. Test de déclaration invalide : un `deroge_a:` sans `perimetre:`, ou citant un ID absent de l'index, ne produit **aucune** dérogation.
9. `docs/historique_2.1.md` à jour, et un rapport de refactoring consigné dans `docs/v2.1/`.

Tant que le point 5 n'est pas atteint dans ses deux branches, le mécanisme de préséance reste **non démontré** : V3 tutorat peut alors être préparée sur le papier, mais pas implémentée, puisque `tutorat.md` dépendra précisément de ce mécanisme.

---

# 12. Points soumis à décision humaine

| # | Décision | Recommandation | Enjeu |
|---|---|---|---|
| **D1** | Adopter le mécanisme `deroge_a:` / `perimetre:` en front matter comme remplacement du marqueur en prose ? | **Oui.** C'est la seule proposition du plan qui rende le discriminateur décidable, et elle réutilise un mécanisme déjà établi du projet. Dans sa version révisée, elle ne classifie aucune référence et ne modifie le comportement d'aucune référence existante. | Structurant : conditionne le lot B et tout le chantier §9. Un refus impose de trouver une autre opérationnalisation, car la prose seule a été réfutée par R1. |
| **D1-bis** | Périmètre initial de l'index des règles dérogeables : `A3` et `R-GRAN` seulement ? | **Oui.** N'identifier que ce qui a un besoin réel — `A3` pour la dérogation V3 tutorat, `R-GRAN` pour le contraste NOY014. Laisser `A1`, `A2` et `A4` hors index : les y inscrire inviterait la dérogation au lieu de la permettre. | Gouvernance des IDs. Un index trop large ouvre des dérogations non voulues ; trop étroit oblige à l'étendre à chaque besoin — ce qui est le comportement souhaité. |
| **D2** | Exécuter le lot D (split de `taxonomie.md`) ? | **Reporter.** Le bénéfice est réel (P3) mais le coût — 8 renvois sur 7 fichiers — est disproportionné tant que le comportement n'est pas stabilisé. À reconsidérer après le point 5 des critères de sortie. | Lisibilité à long terme vs risque de renvois cassés. |
| **D3** | Créer un scénario NOY pour la **non-extension hors périmètre** (I30) ? | **Oui, dans le chantier §9.** Aucun NOY actuel ne teste qu'une dérogation ne fuit pas hors de son périmètre — `NOY014_2` §10 le liste explicitement comme non testé. C'est un trou de couverture sur un invariant gelé. | Sans lui, I30 reste une affirmation non vérifiée. |
| **D4** | Étape A.10 : accepter de reverter et **conserver la duplication de I25** si C0 régresse ? | **Oui.** Une duplication bénigne est préférable à un invariant affaibli. | Applique « suffisant > exhaustif ». |
| **D5** | Que faire des trois porteurs de I21 (`decoupage_pedagogique.md`, `activite.md`, `quiz.md`) ? | **Conserver la dispersion pour l'instant.** C.1 déplace sans retirer. Une canonisation de I21 mériterait son propre cycle, avec NOY010 comme contrôle. | I21 est un invariant NOY010 ; le sur-optimiser est risqué (R2). |
| **D6** | Comment séparer l'environnement de développement Opus de l'environnement des runs de référence ? | **Décision : séparation stricte.** Opus implémente dans sa session de développement avec Superpowers. Pour la baseline puis pour chaque phase de contrôle comportemental de référence, `/home/david/.claude` est recréé dans le même état propre, sans skill, mémoire, plugin, hook, agent, commande ou personnalisation étrangère au candidat. Après la phase de test, l'environnement de développement peut être restauré. Les runs de diagnostic en sous-contexte restent possibles s'ils sont explicitement étiquetés comme tels. | Reproductibilité sans priver Opus de ses outils d'implémentation ; distinction stricte développement / test (R10). |

---

# 13. Ce que ce plan ne fait pas

- Aucun fichier fonctionnel n'a été modifié pendant sa rédaction.
- Aucun oracle, scénario ou fixture n'a été modifié.
- Aucun commit n'a été créé.
- `references/tutorat.md` n'est pas créé.
- La promesse V2.1 (`en_cours/promesse.md`) n'est pas modifiée : le plan applique G02 sans en changer la doctrine. Si le lot B est adopté, G02 devra ultérieurement être mise à jour pour mentionner le mécanisme de périmètre déclaré — **dans un cycle documentaire distinct**, après démonstration comportementale.
