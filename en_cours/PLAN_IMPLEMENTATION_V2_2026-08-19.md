# PLAN_IMPLEMENTATION_V2_2026-08-19

## 0. Objectif du plan

La V2 améliore, clarifie et fiabilise les fonctionnalités déjà présentes sans étendre le périmètre fonctionnel du skill.

Elle consolide :

- le noyau pédagogique ;
- l'architecture des activités ;
- les gabarits existants ;
- leur routage ;
- leur couverture en non-régression ;
- la cohérence documentaire du paquet runtime.

L'ajout de nouvelles formes d'activités est hors périmètre de la V2 et relève d'une version ultérieure, notamment V3.

---

## 1. État actuel de la V2

### 1.1. Batterie NOY actuelle

État de la batterie principale :

```text
NOY001 → stabilisé
NOY002 → stabilisé
NOY003 → stabilisé
NOY004 → stabilisé
NOY005 → stabilisé — issu de T24, recentré pour la V2
NOY006 → stabilisé — issu de T06
NOY007 → stabilisé — issu d'un phénomène transversal V1, avec T08 comme stimulus historique de référence
```

Les NOY001 à NOY007 ont tous été **retravaillés et formalisés comme fiches de validation V2**, à partir de tests Txx ou de phénomènes observés antérieurement, en respectant `validation/MODELE_FICHE_VALIDATION.md` : objectif du test, invariant explicite, stimulus contrôlé, observables, oracles PASS / FAIL / INDÉTERMINÉ, validité technique, marge opérateur et contre-garde-fous lorsque nécessaires.

Ils ont ensuite été dry-runnés et stabilisés selon leur besoin expérimental.

La revue récente des personas a conduit à retravailler de nouveau NOY001 à NOY004 lorsque cette adaptation restait naturelle et conservait le pouvoir discriminant. NOY005 à NOY007 ont également été réexaminés ; leurs formulations stabilisées ont été conservées lorsque leur transposition supplémentaire faisait perdre le contraste observé. Il ne s'agit donc pas de tests historiques laissés tels quels, mais de **NOY V2 déjà retravaillés et stabilisés**.

### 1.2. Ce qui n'est pas réintroduit dans la batterie principale

Ne pas recréer comme tests principaux :

- une sentinelle T26 autonome ;
- les anciens candidats NOY008 à NOY010 qui n'ont pas été retenus ;
- des tests supplémentaires de notation déjà couverts par NOY007.

Le principe de T26 reste un contre-garde-fou conceptuel du budget de nouveauté.

La quantification légitime reste également un contre-garde-fou : toute quantité explicite n'est pas une note.

---

## 2. Doctrine de construction et de non-régression

### 2.1. Comportements du noyau

Pendant la conception ou l'évolution d'une capacité comportementale, utiliser lorsque cela est pertinent :

```text
A  = avec skill
B′ = sans skill
```

Le contraste recherché est idéalement :

```text
A  = PASS
B′ = FAIL
```

Ce contraste ne doit jamais être fabriqué artificiellement par le stimulus ou l'oracle.

Une fois le comportement stabilisé, la non-régression est exécutée :

```text
A uniquement
```

### 2.2. Contrats internes propres au skill

Pour les contrats propres au produit, notamment les gabarits pédagogiques, la condition sans skill n'est pas informative : le baseline ne connaît pas le contrat propriétaire à respecter.

Ces tests sont donc conçus et exécutés :

```text
A uniquement
```

y compris pendant leur mise au point en V2.

Ils restent intégrés à la batterie NOY : il n'existe pas de batterie GAB séparée.

---

## 3. Compléter la couverture NOY sur les gabarits

Ajouter deux ou trois NOY dédiés aux gabarits existants.

Ils sont exécutés en condition A uniquement.

### 3.1. NOY008 — Socle Activité + spécialisation

Protéger le principe :

```text
Toute activité
→ respecte un socle commun minimal

Gabarit spécialisé
→ hérite du socle
→ le complète, le précise ou l'adapte
```

Le test doit vérifier qu'un gabarit spécialisé reste bien une activité complète et ne se réduit pas à ses seules rubriques spécifiques.

Un Quiz est un bon candidat pour ce test.

### 3.2. NOY009 — Routage par métadonnées

Protéger :

```text
besoin pédagogique
→ identification du niveau de granularité
→ consultation des gabarits disponibles
→ exploitation de leurs métadonnées
→ choix cohérent
→ chargement du contrat du gabarit
```

L'oracle ne doit pas imposer une table fermée `situation → gabarit`.

Le test doit vérifier l'architecture suivante :

```text
le noyau orchestre
les gabarits se décrivent eux-mêmes
```

### 3.3. NOY010 — Séparation des volets

Protéger :

```text
contenu remis à l'apprenant
≠
solution / correction / éléments réservés au formateur
```

Vérifier notamment que la solution, les attendus détaillés ou la grille de correction ne sont pas révélés prématurément lorsque le gabarit prévoit cette séparation.

Ce test reprend l'angle historique de T28 sous la forme d'un contrat de gabarit A-only.

---

## 4. Baseline des nouveaux NOY avant modification

Avant toute restructuration des gabarits, exécuter sur le candidat actuel :

```text
NOY008 — A
NOY009 — A
NOY010 — A
```

Conserver les résultats comme état de départ.

Aucune condition B′ n'est nécessaire.

Le principe reste :

```text
observer d'abord
modifier ensuite
```

---

## 5. Revue structurelle du paquet courant

Une revue externe de cohérence a relevé plusieurs anomalies documentaires et normatives.

Chaque point doit être vérifié sur l'état courant avant correction.

### 5.1. 🔴 P0 — Références runtime non résolvables

Vérifier tous les renvois vers :

```text
dossier-pedagogique/origine_des_formats.md
dossier-pedagogique/bibliographie.md
origine_des_formats.md
```

Le paquet runtime ne doit pas dépendre d'un fichier absent ou situé dans un espace réservé à la documentation humaine.

Pour chaque renvoi :

1. vérifier s'il est réellement utile au runtime ;
2. identifier la source canonique ;
3. corriger le chemin ou supprimer la dépendance ;
4. vérifier les autres fichiers qui utilisent le même renvoi.

### 5.2. 🟠 P1 — Renvois et portée normative

Vérifier et corriger si confirmé :

- `andragogie.md` → renvoi erroné vers `taxonomie.md, usage 1` ;
- bandeaux A1/A2/A3 présents dans `quiz.md` et `recul.md` ;
- duplication ou résumé de A1/A2/A3/A4 dans `SKILL.md` ;
- cohérence entre source normative et résumés opérationnels.

Lorsqu'une règle est résumée dans plusieurs fichiers, la source faisant foi doit être explicite.

### 5.3. 🟠 P1 — Recul

Ne pas profiter de la V2 pour redéfinir la valeur pédagogique de `Recul`.

Le Recul est une activité de réflexivité pouvant notamment amener l'apprenant à expliciter :

- ce qu'il a appris ;
- ce qu'il a réalisé ;
- comment il l'expliquerait à un jury ;
- comment il le transférerait dans son métier.

La question de sa valeur probante exacte et de son articulation avec les paliers élevés doit être approfondie dans une version ultérieure.

En V2 :

- vérifier les contradictions documentaires existantes ;
- ne pas introduire de doctrine nouvelle ;
- préserver le gabarit et son usage dans différents contextes.

### 5.4. 🟡 P2 — Cohérence documentaire

Corriger sans refonte stylistique massive :

- vocabulaire manifestement incohérent entre anciennes et nouvelles strates ;
- diagramme Markdown cassé de `opo.md` ;
- fins de fichiers incorrectes ;
- formulations héritées V1 devenues ambiguës ;
- autres défauts de forme qui gênent la lecture ou la maintenance.

---

## 6. Épurer le découpage pédagogique

Le découpage de référence reste :

```text
Module
└── Séquence
    └── Séance
        └── Activité
```

`Activité` est le niveau de granularité le plus fin.

Les gabarits spécialisés ne sont pas des niveaux concurrents :

```text
Activité
├── activité simple
├── Atelier
├── Quiz
├── Recul
└── autres gabarits futurs
```

Épurer le noyau des explications générales inutiles sur :

- synchrone ;
- asynchrone ;
- présentiel ;
- distanciel.

Ces définitions doivent vivre dans le glossaire.

Conserver seulement dans le noyau les conséquences réellement utiles à la décision pédagogique.

Supprimer les formulations trop rigides qui assimileraient par principe :

```text
Quiz = asynchrone uniquement
Recul = asynchrone uniquement
Atelier = présentiel uniquement
```

La modalité et le contexte orientent le choix et la mise en œuvre d'un gabarit, mais ne constituent pas une table d'interdiction.

---

## 7. Faire de `activite.md` le socle commun

Relire ensemble :

```text
references/activite.md
references/atelier.md
references/quiz.md
references/recul.md
```

et extraire uniquement ce qui existe déjà réellement comme socle commun.

Ne pas inventer une nouvelle fiche idéale.

Le socle doit être déterminé à partir de l'existant et couvrir les éléments fondamentaux d'une activité, notamment lorsque présents dans les formats actuels :

- OPO ;
- durée ;
- brief / consigne ;
- conditions ou contraintes ;
- ressources / matériel de départ ;
- livrable ou trace attendue ;
- critères de réussite / performance ;
- séparation des informations apprenant / formateur lorsque nécessaire.

Principe :

> Toute activité repose sur un socle commun minimal. Les gabarits spécialisés héritent de ce socle et peuvent le compléter, le préciser ou l'adapter selon leur finalité pédagogique.

---

## 8. Transformer les gabarits existants en ressources auto-descriptives

Concerne uniquement les gabarits déjà présents en V2 :

```text
activite.md
atelier.md
quiz.md
recul.md
```

Définir un front matter cohérent et léger.

Exemple conceptuel :

```yaml
---
name: quiz
kind: activity_template
inherits: activite
purpose: ...
typical_uses:
  - ...
  - ...
---
```

Les clés exactes doivent être définies pendant l'implémentation, sans sur-concevoir le système.

### 8.1. Rôle du front matter

Le front matter doit aider l'agent à :

```text
identifier le gabarit
→ comprendre sa finalité
→ reconnaître son rattachement au socle Activité
→ voir un ou deux usages types
→ estimer sa pertinence pour le besoin courant
```

Les usages types sont des exemples d'orientation, pas des conditions exclusives.

Éviter de coder dans les métadonnées :

```text
modalité autorisée = X
modalité interdite = Y
```

sauf si une contrainte réelle propre au format l'impose.

### 8.2. Lecture agentique

Dans l'architecture V2, les gabarits jouent un rôle comparable à des outils spécialisés mis à disposition d'un agent :

```text
description / métadonnées
→ aide au choix

contenu du gabarit
→ contrat d'utilisation

noyau
→ orchestration
```

Ils ne sont pas techniquement des `tool calls`, mais cette analogie guide la séparation des responsabilités.

---

## 9. Alléger `SKILL.md`

Une fois les gabarits auto-descriptifs :

```text
SKILL.md
→ orchestration générale
→ garde-fous prioritaires
→ orientation vers les ressources
```

Le noyau ne doit plus contenir une table détaillée de toutes les situations où chaque gabarit doit être utilisé.

Architecture recherchée :

```text
analyse du besoin
→ identification du niveau de granularité
→ découverte des gabarits disponibles
→ lecture de leurs métadonnées
→ sélection d'un gabarit pertinent
→ chargement de son contrat
→ production
→ contrôles avant livraison
```

Éviter de dupliquer dans `SKILL.md` les informations de sélection déjà portées par les gabarits.

---

## 10. Créer le glossaire

Créer :

```text
en_cours/references/glossaire.md
```

Rôle :

```text
définir les mots
≠
redéfinir les règles
```

Le glossaire n'est pas une seconde source normative.

Lorsqu'un terme porte une règle comportementale, renvoyer vers le fichier normatif correspondant.

Inclure notamment :

- activité ;
- gabarit ;
- OPO ;
- notion ;
- palier ;
- preuve ;
- attestation ;
- brief ;
- livrable ;
- critère de réussite ;
- critère de performance ;
- évaluation ;
- notation ;
- synchrone ;
- asynchrone ;
- présentiel ;
- distanciel ;
- atelier ;
- quiz ;
- recul ;
- référentiel ;
- front matter / métadonnées de routage.

### 10.1. Définitions des modalités

```text
Synchrone
→ interaction dans le même temps.

Asynchrone
→ travail ou interaction en temps différé.

Présentiel
→ participants réunis dans un même lieu physique.

Distanciel
→ participants situés à distance.
```

Préciser que :

```text
synchrone / asynchrone
≠
présentiel / distanciel
```

Les deux axes sont indépendants.

### 10.2. Point d'attention en distanciel

Ajouter une remarque courte et non normative :

> En distanciel, l'attention et la concentration peuvent être plus fragiles selon la durée, l'environnement, les sollicitations numériques et le niveau d'interaction. Adapter le rythme, la variété des activités et les interactions au contexte.

---

## 11. Boucle de validation par petits lots

Conserver le principe d'implémentation incrémentale.

Après chaque lot :

1. rejouer le ou les NOY qui motivent le changement ;
2. rejouer les NOY existants potentiellement impactés ;
3. vérifier les contradictions documentaires ;
4. exécuter `git diff --check` ;
5. commit uniquement lorsque le lot est propre.

Lots proposés :

```text
Lot A
→ corrections P0/P1 sans changement fonctionnel voulu

Lot B
→ découpage + socle Activité

Lot C
→ front matter + routage des gabarits

Lot D
→ glossaire + épuration du noyau

Lot E
→ harmonisation documentaire P2
```

Après chaque lot lié aux gabarits, rejouer :

```text
NOY008
NOY009
NOY010
+
les NOY001–007 susceptibles d'être impactés
```

---

## 12. Mise à jour des README

Une fois l'architecture stabilisée, mettre à jour :

```text
README du projet
README du skill
```

Les deux README doivent présenter clairement les trois grandes fonctions :

1. progression par notions, paliers et preuves ;
2. conception d'activités évaluées interprétables ;
3. bibliothèque de gabarits pédagogiques auto-descriptifs.

Dans les README, l'analogie agentique peut être explicitée :

> Les gabarits jouent un rôle proche de tools mis à disposition de l'agent : leur description aide à choisir le bon outil et leur contenu définit comment l'utiliser.

Préciser qu'il s'agit d'une analogie d'architecture, pas de véritables tool calls.

---

## 13. Rejeu complet V2

Une fois tous les lots terminés :

```text
NOY001
NOY002
NOY003
NOY004
NOY005
NOY006
NOY007
NOY008
NOY009
NOY010
```

Exécuter la non-régression :

```text
avec skill uniquement
```

Tous les NOY doivent PASS.

Les dry-runs B′ ayant servi à construire les NOY comportementaux restent des éléments de conception et ne sont pas rejoués dans la non-régression.

---

## 14. Critères de sortie de l'implémentation V2

La V2 peut être gelée lorsque :

- NOY001 à NOY007 restent PASS ;
- NOY008 à NOY010 sont stabilisés et PASS ;
- aucun lien runtime nécessaire n'est cassé ;
- aucune contradiction normative connue n'est laissée silencieusement ;
- le découpage `Module → Séquence → Séance → Activité` est cohérent dans le paquet ;
- `Activité` possède un socle commun identifiable ;
- les gabarits existants héritent de ce socle et l'adaptent selon leur finalité ;
- leurs métadonnées permettent d'orienter le routage ;
- la modalité n'est plus utilisée comme table d'interdiction des gabarits ;
- le glossaire existe ;
- les deux README présentent les trois grandes fonctions ;
- aucun nouveau gabarit n'a été ajouté en V2 ;
- `stable/` et `dist/stable/` n'ont pas été modifiés avant promotion explicite.

---

## 15. Hors périmètre — V3+

### 15.1. Enrichissement de la bibliothèque

La V3 pourra enrichir progressivement la bibliothèque :

```text
nouvelles activités
→ nouveaux gabarits
→ socle Activité
→ métadonnées auto-descriptives
→ contrat propre
→ NOY de conformité A-only
```

L'objectif est de pouvoir enrichir la palette pédagogique sans gonfler le noyau d'une nouvelle logique de routage à chaque ajout.

### 15.2. Recul et réflexivité

Approfondir ultérieurement la valeur pédagogique et probante de l'activité Recul :

```text
ce que j'ai appris
→ ce que j'ai réalisé
→ comment je l'explique à un jury
→ comment je le transfère dans mon métier
→ quelle valeur de preuve cela peut constituer
```

Ne pas résoudre cette question doctrinale en V2.

---

## 16. Ordre de travail recommandé

```text
1. Figer la spécification V2 et le présent plan
2. Concevoir NOY008 à NOY010 sur les gabarits
3. Jouer NOY008 à NOY010 en A sur le candidat actuel
4. Vérifier une par une les anomalies de la revue structurelle
5. Corriger les P0/P1 confirmées
6. Stabiliser Module → Séquence → Séance → Activité
7. Définir le socle commun Activité depuis l'existant
8. Ajouter les métadonnées aux gabarits existants
9. Alléger le routage de SKILL.md
10. Ajouter le glossaire et épurer le noyau
11. Rejouer les NOY concernés après chaque petit lot
12. Harmoniser les défauts P2
13. Mettre à jour les deux README
14. Rejouer NOY001 à NOY010 en A
15. Contrôle final et gel du candidat V2
```
