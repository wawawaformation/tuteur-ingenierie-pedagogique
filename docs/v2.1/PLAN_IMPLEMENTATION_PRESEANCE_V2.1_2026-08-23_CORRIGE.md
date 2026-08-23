# Plan d'implémentation — préséance et dérogation locale V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** V2.1.0
**Date :** 2026-08-23
**Rôle de production :** architecte / reviewer — plan uniquement, aucune modification du runtime effectuée
**Cible :** satisfaire G02 de `en_cours/promesse.md` dans le runtime, et rendre exécutables `NOY014_1` / `NOY014_2`
**Statut :** prêt pour implémentation, sous réserve des deux points de décision signalés en fin de document

**Sources lues :** `en_cours/SKILL.md`, `en_cours/promesse.md`, `en_cours/base_de_travail.md`, `en_cours/references/*`, `docs/historique_2.1.md`, `validation/v2.1/non_regression/NOY014_1.md`, `NOY014_2.md`, `CONTROLE_STABILISATION_NOY014.md`, `mock_sans_derogation.md`, `mock_avec_derogation.md`.

---

# 0. Hypothèses de départ corrigées après lecture des fichiers réels

**H1 — « la règle de granularité pourrait ne pas exister » : FAUX, elle existe et à trois endroits.**

| Fichier | Ligne | Formulation |
|---|---|---|
| `en_cours/references/decoupage_pedagogique.md` | 69 | « L'Activité est la granularité la plus fine : la tâche effectivement proposée à l'apprenant. » |
| `en_cours/references/activite.md` | 7 | « Une Activité est la granularité la plus fine du découpage pédagogique […] » |
| `en_cours/references/glossaire.md` | 35 | « Granularité la plus fine : ce que l'apprenant doit effectivement faire. » |

La source **normative** est `decoupage_pedagogique.md` (fichier dont l'objectif déclaré est « Définir les échelles du découpage pédagogique »). `activite.md` la reprend comme socle, `glossaire.md` en descriptif. Le contraste de NOY014 est donc solidement établi : la vérification statique du §1 de `CONTROLE_STABILISATION_NOY014.md` passera, et le risque que C0 invalide l'instrument est faible.

**H2 — « le terme *noyau* est disponible pour rédiger la règle » : FAUX.**

`grep -rn "noyau" en_cours/SKILL.md en_cours/references/` renvoie **zéro résultat**. Le mot n'existe que dans `promesse.md`, `base_de_travail.md` (spec et feuille de route, hors runtime) et dans les fiches NOY014. Écrire « le noyau prévaut » dans `SKILL.md` introduirait un terme non défini pour l'agent au moment du run. Ce point conditionne la formulation retenue au §7.

Atténuation constatée : les deux mocks écrivent eux-mêmes « La règle générale du noyau prévoit par ailleurs qu'`Activité` est la granularité la plus fine. » — la fixture fournit donc le cadrage. La formulation runtime doit néanmoins être auto-suffisante.

---

# 1. État actuel observé

## Ce qui existe déjà dans le runtime

`en_cours/SKILL.md` porte **déjà trois règles d'arbitrage documentaire**, toutes dans ce seul fichier :

| Ligne | Section | Règle |
|---|---|---|
| 26 | Garde-fous prioritaires | « Ces lignes sont des repères de navigation : appliquer les conditions exactes de `references/taxonomie.md` §2 **sans les réinterpréter ici**. » |
| 99 | Sources de vérité | « Le glossaire est descriptif : lorsqu'une définition implique une règle comportementale, **la référence normative spécialisée fait foi**. » |
| 120 | Contrôles avant réponse ou livraison | « Pour toute contradiction pertinente entre deux références effectivement mobilisées : **ne pas arbitrer silencieusement ; la signaler**. » |

**Aucune référence de `references/` ne porte de règle d'arbitrage inter-documents.** Elles portent chacune une doctrine de domaine (paliers, preuve, granularité, alignement, posture, gabarits).

## Ce qui existe hors runtime

- `en_cours/promesse.md` **G02** contient le mécanisme complet, y compris la clause « Ce mécanisme est une règle de résolution de priorité ; il n'ajoute pas de gate ni de vérification systématique de dérogation. » (ajoutée lors de l'alignement de `promesse.md` du 2026-08-23).
- `en_cours/base_de_travail.md` §6.1 à §6.4 et §8.5 décrivent le mécanisme, son marqueur uniforme et la nécessité de le rendre visible et auditable.

---

# 2. Écart spec → runtime

Le runtime sait **signaler** une contradiction. Il ne sait pas **la résoudre** par un marqueur de dérogation.

Formellement, il manque les points 1 à 5 et 7 de la doctrine G02 :

```text
manquant : dérogation explicitement signalée + périmètre applicable
           → la règle spécialisée prévaut, localement

manquant : absence de dérogation explicite
           → la règle générale prévaut

présent  : contradiction non résolue → signaler
```

Conséquence directe : `NOY014_2` échouerait aujourd'hui (l'agent n'a aucune règle l'autorisant à faire prévaloir `mock.md`), et `NOY014_1` passerait pour une raison non garantie (absence de règle de préséance plutôt qu'application d'une préséance correcte) — un PASS structurellement fragile.

---

# 3. Architecture minimale proposée

**Source normative retenue : `en_cours/SKILL.md`.** Justification, par élimination :

- **Ce n'est pas une doctrine de domaine.** Contrairement à l'attestation (qui relevait de la preuve, donc de `etat_des_paliers.md`), la préséance est une règle d'**orchestration documentaire** : elle dit quel document gagne, pas ce qu'est un palier ou une preuve.
- **Aucune référence existante n'est compétente.** `decoupage_pedagogique.md` porte la granularité, pas l'arbitrage ; y loger la règle la rendrait invisible pour tout autre conflit (A3, alignement, tutorat V3 à venir) et créerait une dépendance absurde entre « préséance » et « découpage ».
- **`SKILL.md` est déjà le porteur de cette famille de règles** (l. 26, 99, 120). Ajouter la préséance à côté de la l. 120 place la règle dans son voisinage naturel, où elle est déjà cherchée.
- **Créer `references/preseance.md` serait disproportionné** : un fichier pour trois phrases, à charger en plus, alors que `SKILL.md` est toujours en contexte. Cela contredirait aussi « une seule source normative claire par règle » sans rien apporter.

**Rôle de `SKILL.md` : porteur de la règle elle-même**, pas simple routage. C'est la différence assumée avec M6 du cycle attestation (où `SKILL.md` ne recevait qu'un renvoi, parce que la doctrine détaillée vivait ailleurs). Ici, il n'y a pas d'ailleurs.

**Emplacement précis retenu : en place, à la l. 120**, en étendant la règle existante plutôt qu'en créant une section. Rationale : la clause de signalement doit devenir le *dernier recours* du même mécanisme ; les séparer dans deux zones du fichier recréerait exactement la contradiction que le §8 doit éviter.

*Alternative écartée :* déplacer la règle vers « Sources de vérité » (près de la l. 99, également consacrée à la préséance). Écartée car cela toucherait deux zones au lieu d'une, pour un gain de cohérence purement esthétique.

**Nouveau fichier fonctionnel : NON.**

---

# 4. Fichiers fonctionnels à modifier

| Fichier | Pourquoi |
|---|---|
| `en_cours/SKILL.md` | Seul porteur des règles d'arbitrage documentaire. La l. 120 doit passer de « signaler toute contradiction » à « résoudre par la règle de préséance, et signaler ce qui reste non résolu ». **Unique modification fonctionnelle du lot.** |

**Un seul fichier fonctionnel.** Plus `docs/historique_2.1.md` (documentation, cf. §6.2).

---

# 5. Fichiers explicitement à ne pas modifier

| Fichier | Pourquoi aucune modification n'est nécessaire |
|---|---|
| `en_cours/promesse.md` | G02 contient déjà le mécanisme complet **et** la clause anti-gate. La spec est en avance sur le runtime, pas en écart avec lui. Aucun alignement requis. |
| `en_cours/references/decoupage_pedagogique.md` | Porte la règle de contraste (l. 69). **Doit rester strictement intacte** — la modifier invaliderait NOY014 et C0. |
| `en_cours/references/activite.md`, `glossaire.md` | Reprennent la granularité ; aucune n'a à connaître le mécanisme de préséance. |
| `en_cours/references/taxonomie.md`, `etat_des_paliers.md`, `opo.md`, `andragogie.md`, `sequence.md`, `seance.md`, `syllabus.md`, `activites_type/*` | Doctrines de domaine sans rapport. Y ajouter un marqueur de dérogation serait une duplication et créerait le risque « toute référence spécialisée est prioritaire ». |
| `en_cours/base_de_travail.md` | Feuille de route, pas runtime. |
| `validation/v2.1/non_regression/NOY014_1.md`, `NOY014_2.md`, `CONTROLE_STABILISATION_NOY014.md`, `mock_sans_derogation.md`, `mock_avec_derogation.md` | Instruments déjà audités et corrigés. Interdiction explicite. |
| Tous les autres NOY, oracles et fixtures | Règle projet : ne jamais modifier l'oracle et le runtime dans le même cycle (`base_de_travail.md` §11). |

---

# 6. Modifications prévues fichier par fichier

## 6.1 `en_cours/SKILL.md` — l. 120, section « Contrôles avant réponse ou livraison »

**Règle actuelle (texte exact) :**

> Pour toute contradiction pertinente entre deux références effectivement mobilisées : **ne pas arbitrer silencieusement ; la signaler**.

**Modification :** remplacer cette ligne unique par un bloc court de préséance qui (a) résout le conflit quand une dérogation explicite s'applique, (b) fait prévaloir la règle générale sinon, (c) **conserve la clause de signalement mot pour mot** comme cas résiduel.

**Contraintes de rédaction imposées à l'implémenteur :**

1. Conserver l'amorce conditionnelle et le qualificatif **« effectivement mobilisées »** — c'est ce membre de phrase qui borne le déclenchement et empêche le gate (cf. §10, R2).
2. Conserver le fragment **« ne pas arbitrer silencieusement ; la signaler »** à l'identique, en fin de bloc.
3. Ne pas introduire le terme « noyau » (cf. §0/H2) ; employer « règle générale du skill ».
4. Ne pas écrire de verbe d'obligation de recherche (« vérifier s'il existe », « rechercher une dérogation », « avant toute décision »).
5. Longueur cible : 4 phrases maximum, en un seul bloc, sans sous-titre ni liste à puces — la l. 120 est aujourd'hui une ligne unique, le bloc doit rester du même ordre de grandeur.
6. Ne toucher ni la l. 26 ni la l. 99.

## 6.2 `docs/historique_2.1.md` — à l'implémentation effective

Ajouter une entrée datée en tête (ordre chronologique inverse) consignant précisément :

- l'implémentation de la règle de préséance / dérogation locale dans `en_cours/SKILL.md`, comblant l'écart entre G02 et le runtime ;
- le fait que `SKILL.md` est retenu comme **source normative** de ce mécanisme (et non simple routage), parce qu'aucune référence de domaine n'est compétente pour l'arbitrage inter-documents ;
- la conservation de la clause de signalement des contradictions comme cas résiduel du même mécanisme ;
- le choix terminologique « règle générale du skill » plutôt que « noyau », le second étant absent du runtime ;
- qu'aucun NOY, oracle ou fixture n'a été modifié ;
- le statut : non testé, en attente de C0 → NOY014_1 → NOY014_2.

---

# 7. Formulation normative proposée

Texte recommandé pour remplacer la l. 120 :

> **Préséance entre règles.** Lorsque des règles effectivement mobilisées entrent en conflit, une référence spécialisée dont le périmètre s'applique et qui **signale explicitement déroger** à une règle générale du skill prévaut — pour ce seul périmètre. En l'absence d'une telle dérogation explicite, la règle générale prévaut. Une dérogation locale ne modifie pas la règle générale et ne s'étend à aucun autre périmètre. Si une contradiction pertinente reste non résolue par cette règle : **ne pas arbitrer silencieusement ; la signaler**.

**Vérification point par point contre G02 :**

| Doctrine G02 | Couvert par |
|---|---|
| 1. dérogation possible pour son seul périmètre | « dont le périmètre s'applique […] pour ce seul périmètre » |
| 2. valide seulement si signalée explicitement | « qui signale explicitement déroger » |
| 3. sans dérogation → règle générale | phrase 2 |
| 4. avec dérogation → spécialisée, localement | phrase 1 |
| 5. ne modifie pas implicitement, ne généralise pas | phrase 3 |
| 6. résolution de priorité documentaire | forme conditionnelle, aucune procédure |
| 7. pas de gate | cf. §10, R2 — aucun impératif de recherche |
| 8. contradiction résiduelle signalée | phrase 4, texte existant conservé |

**Propriétés :** 4 phrases · aucun terme non défini au runtime · déclenchement conditionnel · aucune duplication (la règle n'existe nulle part ailleurs dans le runtime) · portée bornée explicitée.

---

# 8. Articulation avec le signalement des contradictions

Les deux mécanismes ne sont pas concurrents : ils sont **deux issues du même test**, dans cet ordre.

```text
règles effectivement mobilisées en conflit ?
├── non  → rien ne se déclenche (cas nominal)
└── oui
    ├── une référence spécialisée applicable signale explicitement une dérogation
    │       → la règle spécialisée s'applique, dans son seul périmètre
    │         (le conflit est RÉSOLU — il n'y a plus rien à signaler)
    └── sinon
            → la règle générale prévaut
              └── si une contradiction pertinente demeure malgré cela
                      → la signaler, ne pas l'arbitrer silencieusement
```

Le point clé de rédaction est le mot **« résolue »** dans la dernière phrase : il subordonne le signalement au fait que la préséance n'ait pas tranché. Sans ce mot, l'agent pourrait appliquer correctement la dérogation **puis** signaler quand même une contradiction — ce que l'oracle de `NOY014_2` classe explicitement en `FAIL` (« signale une contradiction comme non résolue alors que la référence contient une dérogation explicite et bornée »).

C'est pourquoi le §3 impose de traiter les deux clauses **dans un seul bloc contigu** : séparées, l'agent risque de les appliquer indépendamment.

---

# 9. Traitement des références spécialisées compatibles

Une référence spécialisée qui **ne contredit rien** n'est jamais concernée, et ce pour une raison structurelle : la règle est gouvernée par une condition d'entrée (« lorsque des règles effectivement mobilisées entrent en conflit »). Sans conflit, aucune branche ne s'ouvre.

Vérification sur le parc réel de références spécialisées du candidat :

| Référence | Contredit-elle une règle générale ? | Marqueur requis |
|---|---|---|
| `activites_type/quiz.md` (plafond palier 2) | Non — précise, ne contredit pas | Aucun |
| `activites_type/brique.md`, `atelier.md`, `recul.md` | Non — spécialisent le socle `activite.md` | Aucun |
| `sequence.md`, `seance.md`, `syllabus.md` | Non — contrats de niveaux structurels | Aucun |

Aucune de ces références n'aura à être modifiée ni annotée. C'est un point à contrôler statiquement (CS-P6, §11) : si l'implémentation conduisait à devoir ajouter « dérogation » quelque part dans `activites_type/`, la formulation serait mauvaise et devrait être corrigée avant tout run.

Ce point protège aussi la trajectoire V3 : `tutorat.md` pourra apporter des règles complémentaires sans marqueur, et n'en aura besoin que pour les rares points où il contredit réellement le noyau (`base_de_travail.md` §6.3 : les dérogations doivent rester peu nombreuses et auditables).

---

# 10. Risques de régression

## Risques réels

**R1 — `SKILL.md` l. 99 lue comme une préséance générale des références spécialisées.** *(risque principal)*

La l. 99 dit « la référence normative spécialisée fait foi ». Elle vise l'axe *glossaire descriptif → référence normative*, mais un agent peut la transposer à l'axe *règle générale → référence spécialisée* et conclure que `mock.md` gagne toujours. Effet : **`NOY014_1` en FAIL**, et lecture conjointe « spécialisée dans les deux cas » = préférence générale pour la référence locale (§9 de NOY014_2).

*Atténuation :* la nouvelle règle nomme explicitement la condition (« qui signale explicitement déroger ») et se trouve dans le même fichier ; le contraste `Activité = granularité la plus fine` est par ailleurs porté par `decoupage_pedagogique.md` (normative) et pas seulement par le glossaire, ce qui affaiblit la transposition. **À vérifier en priorité par CS-P4 puis par le run NOY014_1.** Si NOY014_1 échoue de façon reproductible avec ce motif dans le verbatim, la correction portera sur une désambiguïsation minimale de la l. 99 — **dans un cycle ultérieur**, jamais en même temps qu'un oracle.

**R2 — effet de gate.**

Formulation qui deviendrait « avant toute décision, vérifier s'il existe une dérogation ». Effet : ralentissement systématique, recherche de références non pertinentes, régression diffuse sur l'ensemble de la batterie (notamment NOY009/NOY010/NOY011 sur le routage des gabarits).

*Atténuation :* contrainte de rédaction n° 4 (§6.1) + condition d'entrée conservée + contrôle CS-P2. Risque jugé **maîtrisable** mais à vérifier explicitement dans le diff.

**R3 — `mock.md` absent de la liste « Sources de vérité » (l. 90-97).**

L'agent pourrait considérer la liste comme un inventaire fermé et ignorer `mock.md`. Effet : sur `NOY014_1`, l'oracle bascule en `INDÉTERMINÉ` (l'observable de lecture obligatoire du §6 est précisément là pour ça — bonne conception de l'instrument) ; sur `NOY014_2`, effet **FAIL**.

*Atténuation :* le stimulus des deux fiches déclare explicitement « La référence `references/mock.md` fait partie du skill chargé et concerne ce périmètre ». Risque **modéré**, mais c'est le second motif de FAIL le plus plausible sur NOY014_2. Aucune modification du runtime n'est recommandée pour le couvrir : élargir la liste des sources de vérité pour accommoder une fixture de test reviendrait à modifier le candidat pour faire passer un test.

## Hypothèses peu probables

**R4 — perturbation des doctrines V2.1 déjà implémentées** (preuve/attestation, état des paliers, A3, alignement). La modification est strictement circonscrite à une ligne d'orchestration ; aucune règle de domaine n'est touchée. Probabilité faible, mais couverte par la passe complète de non-régression.

**R5 — granularité normale hors dérogation.** C0 est précisément là pour établir que le comportement de référence tient sans mock. Risque faible étant donné que la règle est portée par trois fichiers.

**R6 — invalidation du contraste NOY014.** Écarté par la vérification §0/H1 : la règle existe, normative, à trois endroits.

---

# 11. Contrôles statiques prévus

À exécuter par relecture du diff, **avant tout test comportemental**.

| # | Contrôle | Critère de réussite |
|---|---|---|
| **CS-P1** | Non-duplication | La règle de préséance n'apparaît **qu'une fois** dans le runtime (`SKILL.md`). `grep -rn "déroge\|dérogation" en_cours/` ne doit rien renvoyer dans `references/`. |
| **CS-P2** | Absence de gate | Aucune formulation impérative de recherche préalable. Le bloc commence par une condition (« Lorsque… »), pas par une instruction. Aucune occurrence de « avant toute décision », « vérifier s'il existe », « rechercher ». |
| **CS-P3** | Clause de signalement préservée | Le fragment « ne pas arbitrer silencieusement ; la signaler » est présent **à l'identique**, subordonné à « reste non résolue ». |
| **CS-P4** | Simulation NOY014_1 sur table | Avec `mock_sans_derogation.md` : la référence borne bien son périmètre mais **ne signale aucune dérogation** → branche « sinon » → règle générale prévaut → pas de `Micro-activité` comme niveau structurel. On doit pouvoir **nommer la condition qui manque**. |
| **CS-P5** | Simulation NOY014_2 sur table | Avec `mock_avec_derogation.md` : périmètre applicable **et** « Dérogation explicite au noyau » signalée → branche « dérogation » → `Micro-activité` appliqué, et **aucune contradiction signalée** (sinon FAIL selon l'oracle). |
| **CS-P6** | Références compatibles | Aucune référence de `activites_type/` ni aucun contrat de niveau n'a eu besoin d'être annoté. Si l'implémentation en a annoté une, la formulation est mauvaise. |
| **CS-P7** | Contraste intact | `decoupage_pedagogique.md` l. 69 vérifiée **strictement inchangée**, ainsi que `activite.md` l. 7 et `glossaire.md` l. 35. |
| **CS-P8** | Portée du diff | `git diff --stat` ne montre que `en_cours/SKILL.md` + `docs/historique_2.1.md`. Aucun fichier de `validation/`. |

Un échec de CS-P4, CS-P5 ou CS-P6 impose de corriger la rédaction **avant** de lancer le moindre run.

---

# 12. Séquence de validation après implémentation

```text
1. revue statique du diff fonctionnel (CS-P1 → CS-P8)
2. vérification statique de la règle de granularité
   → CONTROLE_STABILISATION_NOY014.md §1
   → consigner fichier + passage exact (decoupage_pedagogique.md l. 69)
3. C0 — A sans mock, session neuve
   → attendu : pas de « Micro-activité » spontanée
   → si l'agent l'invente : NE PAS GELER NOY014, contraste invalide
   → consigner le résultat (C0 ne reçoit pas de verdict officiel)
4. NOY014_1 — A + mock_sans_derogation, session et copie neuves
   → attendu PASS ; lecture de mock.md observable, sinon INDÉTERMINÉ
5. NOY014_2 — A + mock_avec_derogation, session et copie neuves
   → attendu PASS ; ne pas réutiliser la session de NOY014_1
6. smoke tests attestation formateur (déjà prévus)
   → NOY012_2, NOY012_1, NOY006
7. non-régression complète du noyau V2.1 — condition A × 1
   → les 16 scénarios, sans réduction aux seuls NOY jugés à risque
```

Conditions : `claude-test`, workspace neuf, copie neuve du candidat, aucun persona, mémoire automatique désactivée. Condition **A uniquement** — il n'y a volontairement aucun B′ pour NOY014, qui teste une architecture propre au skill.

**Règle de répétition :**

```text
premier A FAIL
→ deux reruns
→ seulement ensuite diagnostic
```

Les reruns mesurent la reproductibilité ; ce n'est **pas** un vote majoritaire. **Ne jamais modifier simultanément l'oracle et le runtime** pour faire disparaître un FAIL — si l'oracle est en cause, le corriger explicitement puis redémarrer un cycle avec le nouvel oracle gelé.

---

# 13. Critères de fin d'implémentation

L'implémentation est terminée et prête pour les tests lorsque **toutes** ces conditions sont réunies :

1. `en_cours/SKILL.md` contient la règle de préséance dans un bloc unique et contigu, à l'emplacement de l'ancienne l. 120 ;
2. la clause de signalement est conservée à l'identique et subordonnée à « reste non résolue » ;
3. les six contraintes de rédaction du §6.1 sont respectées ;
4. CS-P1 à CS-P8 sont tous au vert ;
5. `docs/historique_2.1.md` porte l'entrée décrite au §6.2 ;
6. `git status` ne montre aucune modification dans `validation/`, ni dans `references/`, ni dans `promesse.md` ;
7. aucun test comportemental n'a été lancé.

L'implémentation **n'est pas** considérée comme validée à ce stade : la validation comportementale commence au §12 et reste subordonnée à une autorisation explicite de lancer des dry-runs.

---

# 14. Résumé

```text
Fichiers fonctionnels à modifier : 1 — en_cours/SKILL.md
                                   (+ docs/historique_2.1.md, documentation)
Source normative retenue : en_cours/SKILL.md (l. 120, en place)
Rôle de SKILL.md : porteur de la règle elle-même, pas simple routage
Nouveau fichier fonctionnel : NON
Principal risque de régression : SKILL.md l. 99 (« la référence normative
  spécialisée fait foi ») transposée en préséance générale des références
  spécialisées, ce qui ferait échouer NOY014_1.
Complexité estimée : FAIBLE
```

---

# 15. Points de décision restant ouverts

Deux points appellent une décision avant implémentation :

1. **Choix terminologique** — « règle générale du skill » au lieu de « noyau » (§0/H2). Recommandé : retenir « règle générale du skill », le terme « noyau » étant absent du runtime.
2. **Traitement de R1** — recommandé : laisser `SKILL.md` l. 99 intacte et ne la désambiguïser que si `NOY014_1` échoue effectivement avec ce motif, plutôt que de modifier deux zones à l'aveugle.

Aucun autre arbitrage doctrinal n'est laissé à l'agent implémenteur.
