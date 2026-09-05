---
objectif: "Définir les échelles du découpage pédagogique, indépendamment des modalités, et orienter vers les gabarits associés."
---

# Découpage pédagogique

Ce document définit l'architecture de travail utilisée par le skill pour organiser les contenus et choisir le bon niveau de détail.

Il distingue trois dimensions qui ne doivent pas être confondues :

- la **granularité pédagogique** : Module, Séquence, Séance, Activité ;
- les **modalités de mise en œuvre** : synchrone / asynchrone et présentiel / distanciel ;
- le **gabarit d'Activité** utilisé selon la finalité pédagogique.

## 0. Principe de découpage

La structure de travail est :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité
```

Une **Séance** est une unité d'organisation à l'intérieur d'une Séquence. Elle peut regrouper plusieurs activités lorsqu'un déroulé commun est utile.

Une **Activité** peut également être rattachée directement à une Séquence, par exemple pour un travail autonome, une intersession ou une activité qui n'a pas besoin d'être encapsulée dans une Séance.

La présence ou l'absence d'une Séance ne se déduit donc pas automatiquement de la modalité.

De même, la durée ne définit jamais à elle seule le niveau de découpage. Les durées éventuellement indiquées dans les gabarits sont des repères pratiques, pas des critères de classification.

## 1. Les échelles du découpage pédagogique

### Module

Le Module est l'enveloppe globale : un ensemble cohérent de compétences et de Séquences organisé autour d'une finalité de formation.

**Document produit s'il est demandé** : cadrage global, public cible, prérequis, compétences ou objectifs généraux et découpage en Séquences.

Gabarit associé : `syllabus.md`.

### Séquence

La Séquence organise un sous-ensemble cohérent d'apprentissages et articule plusieurs activités ou Séances vers une progression commune.

Elle donne le cap sans détailler chaque consigne d'activité.

**Document produit s'il est demandé** : une fiche de progression logique montrant les objectifs, prérequis, activités prévues, livrables et articulation d'ensemble.

Gabarit associé : `sequence.md`.

### Séance

La Séance est une unité de travail organisée et pilotable à l'intérieur d'une Séquence.

Elle peut regrouper des temps d'ancrage, d'apport, de démonstration, d'activité, de retour ou de transition. Son déroulé peut être minuté lorsque cela aide le formateur à piloter le temps, sans faire du minutage une définition de la Séance.

Une Séance n'est pas synonyme de présentiel ni de synchrone. Sa mise en œuvre dépend du contexte pédagogique choisi.

**Document produit s'il est demandé** : un déroulé utilisable par le formateur, avec l'intention, l'organisation des temps, les activités prévues et les transitions utiles.

Gabarit associé : `seance.md`.

### Activité

L'Activité est la granularité la plus fine : la tâche effectivement proposée à l'apprenant. *(règle `R-GRAN`)*

Elle peut être intégrée dans une Séance ou rattachée directement à une Séquence.

Toute Activité repose sur un contrat commun. Des gabarits spécialisés peuvent préciser ce contrat selon la finalité pédagogique.

Les formes actuellement prévues sont notamment :

- Brique ;
- Atelier ;
- Quiz ;
- Recul.

Le choix entre ces formes dépend de ce que l'on veut faire réaliser ou observer, pas de la seule modalité.

Le socle commun est défini dans `activite.md`. Les gabarits spécialisés se trouvent dans `activites_type/` : `brique.md`, `atelier.md`, `quiz.md` et `recul.md`.

## 2. Modalités de mise en œuvre

Deux axes indépendants peuvent qualifier une situation pédagogique :

```text
temps
→ synchrone / asynchrone

espace
→ présentiel / distanciel
```

**Synchrone** signifie que les participants interagissent au même moment.

**Asynchrone** signifie que les interactions ou productions peuvent être réalisées à des moments différents.

**Présentiel** signifie que les participants sont réunis dans un même lieu physique.

**Distanciel** signifie que les participants travaillent à distance.

Ces axes peuvent se combiner. Ils décrivent les conditions de mise en œuvre ; ils ne définissent ni la granularité pédagogique ni le gabarit d'Activité.

Ne jamais déduire automatiquement :

```text
présentiel ou synchrone
→ Séance obligatoire
→ Brique obligatoire

asynchrone ou distanciel
→ absence de Séance
→ Atelier / Quiz / Recul uniquement
```

Un Atelier, un Quiz ou un Recul peut être adapté à plusieurs modalités lorsque sa finalité pédagogique reste cohérente.

## 3. Choisir le niveau avant le gabarit

Lorsqu'une demande de conception est formulée :

1. identifier d'abord la granularité réellement demandée : Module, Séquence, Séance ou Activité ;
2. si la demande porte sur une Activité, identifier ensuite le gabarit le plus pertinent ;
3. prendre en compte les modalités pour adapter la mise en œuvre, sans les utiliser comme règle d'exclusion automatique.

La relation est donc :

```text
granularité
→ niveau du document à produire

finalité pédagogique
→ gabarit d'Activité pertinent

modalités
→ adaptation de la mise en œuvre
```

## 4. Production des fiches

Les conventions de production d'une fiche — périmètre, niveau de détail, séparation apprenant / formateur, callouts — sont définies dans `production_documentaire.md`.

Les règles relatives aux paliers, aux preuves, au budget de nouveauté et aux activités évaluées restent définies par `taxonomie.md` et `etat_des_paliers.md`.
