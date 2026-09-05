# Tuteur & ingénierie pédagogique — V3.1.0

Ce dossier contient la version **V3.1.0**, validée, du skill `tuteur-ingenierie-pedagogique`.

Il est destiné au tutorat d’adultes et à l’assistance à l’ingénierie pédagogique. Son rôle n’est pas de remplacer le jugement du formateur, mais de fournir à l’agent des garde-fous et des ressources lui permettant de raisonner de façon plus cohérente sur la progression, l’évaluation et la conception des activités.

> **Version publique recommandée.**
>
> Cette V3.1.0 étend le socle V2.1 (chantier 1 de la V3 : catalogue d’activités) et remplace la V2.1 comme version publique recommandée. V1, V2 et V2.1 restent conservées pour historique dans `../`.

---

## Les trois fonctions principales

### 1. Progression par notions, paliers et preuves

Le skill suit l’état d’apprentissage **notion par notion**.

```text
notion
→ palier
→ preuve
→ décision
```

Il distingue notamment exposition, déclaration et preuve observable.

Une capacité n’est attestée qu’à hauteur de ce que la preuve permet réellement de conclure.

---

### 2. Activités évaluées interprétables

Lorsqu’une activité est évaluée, le skill cherche à préserver l’interprétabilité de son résultat.

```text
objectif
→ tâche
→ production / performance
→ critères
→ preuve
→ conclusion
```

Il protège notamment le budget de nouveauté : une activité évaluée ne doit pas introduire silencieusement plusieurs notions non attestées dont l’échec deviendrait impossible à diagnostiquer.

Les critères restent visibles pour l’apprenant, tandis que les éléments de correction ou une production de référence donnant la solution sont protégés jusqu’à sa propre production.

---

### 3. Bibliothèque de gabarits pédagogiques auto-descriptifs

Toute Activité repose sur un socle commun défini dans :

```text
references/activite.md
```

Les spécialisations disponibles sont :

```text
references/activites_type/
├── atelier.md
├── barometre_humain.md
├── brainstorming.md
├── brique.md
├── carte_conceptuelle.md
├── devine_carte.md
├── en_un_mot.md
├── etude_de_cas.md
├── evaluation_par_les_pairs.md
├── facettes.md
├── interview_croisee.md
├── objet_express.md
├── planche_meteo.md
├── quiz.md
├── recul.md
├── retrospective.md
└── simulation_mise_en_situation.md
```

Le catalogue du socle (`references/activite.md`) aide l’agent à effectuer une première sélection. Les métadonnées de sélection disponibles dans le front matter de chaque gabarit peuvent départager plusieurs candidats plausibles avant de charger le contrat détaillé du gabarit retenu.

L’analogie agentique est la suivante :

```text
métadonnées
→ description d’un outil possible

contenu du gabarit
→ contrat d’utilisation

SKILL.md
→ orchestration
```

Les gabarits jouent donc un rôle proche de **tools disponibles pour l’agent**, mais ce ne sont pas techniquement des tool calls.

---

## Deux modes d’usage

### Tutorat direct

L’agent accompagne un apprenant :

- comprend la demande ou le blocage ;
- établit le point de départ lorsque cela change la décision ;
- raisonne sur les notions et preuves disponibles ;
- explique ou fait pratiquer ;
- propose une activité compatible avec l’état connu ;
- ajuste la suite à partir des résultats observés.

### Ingénierie pédagogique

L’agent assiste un formateur ou concepteur :

- identifie le bon niveau de granularité ;
- structure Module, Séquence, Séance et Activité ;
- formule les objectifs pédagogiques ;
- choisit un gabarit d’Activité lorsque pertinent ;
- produit brief, tâche, production attendue et critères ;
- vérifie l’alignement avant livraison.

---

## Granularité, modalité et gabarit sont indépendants

Le découpage interne de référence est :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité directement rattachée si pertinent
```

`Activité` est le niveau de granularité le plus fin.

La modalité ne choisit pas automatiquement la structure ou le gabarit.

```text
synchrone / asynchrone
≠
présentiel / distanciel
```

De même :

```text
court ≠ automatiquement Brique
difficile ≠ automatiquement Atelier
asynchrone ≠ automatiquement Atelier
présentiel ≠ automatiquement Séance
```

La décision dépend du besoin pédagogique et du contexte.

---

## Gabarits disponibles

### Brique

Activité élémentaire au sens de la structure pédagogique : une tâche ciblée, suffisamment autonome pour être utilisée seule ou composée avec d’autres.

« Élémentaire » ne signifie pas « facile ».

### Atelier

Activité structurée autour d’une production évaluée nécessitant une démarche organisée en plusieurs étapes.

Sa caractéristique n’est ni sa durée ni sa modalité.

### Quiz

Activité principalement destinée au diagnostic ou à l’auto-positionnement.

Le format exact dépend du besoin ; ses règles détaillées sont définies dans son propre contrat.

### Recul

Activité de réflexivité permettant d’expliciter, analyser et mettre en perspective une expérience, une production, une démarche ou des choix.

Il n’a pas de palier propre : la valeur de preuve dépend de la performance réellement observable.

### Étude de cas

Analyser une situation contextualisée pour identifier les éléments pertinents, poser un diagnostic ou argumenter une décision.

### Simulation / mise en situation

Faire agir l’apprenant dans une situation proche d’un contexte de référence, pour observer la mobilisation de connaissances, procédures, stratégies ou comportements.

### Facettes

Répartir l’exploration d’un même thème entre sous-groupes complémentaires, avant restitution et reconstruction d’une vision d’ensemble.

### Devine-carte

Récupération et reconnaissance ludiques de notions déjà travaillées, par indices progressifs.

### Brainstorming

Produire un ensemble diversifié d’idées ou de pistes en suspendant temporairement leur évaluation, avant une phase distincte de structuration, de sélection ou de décision.

### Carte conceptuelle

Représenter des concepts et leurs relations pour expliciter une organisation mentale et favoriser une lecture systémique.

### Évaluation par les pairs

Faire examiner une production par d’autres apprenants à partir de critères explicites.

### Interview croisée

Créer rapidement du lien dans un groupe en faisant découvrir une personne par l’écoute, la reformulation et la présentation par un pair, en binôme.

### Rétrospective

Réguler collectivement les conditions de travail et d’apprentissage : réussites, freins, priorités.

### Objet express

Faciliter une première prise de parole à l’aide d’un objet choisi par l’apprenant comme médiateur.

### Planche météo

Faire exprimer l’état du moment (disponibilité, énergie, ressenti) susceptible d’influencer la situation d’apprentissage.

### Baromètre humain

Faire apparaître la diversité du groupe par un positionnement physique sur un continuum, avant de courtes prises de parole.

### En un mot

Recueillir un feedback apprenant très bref sur une journée, une séance, une activité ou une séquence, pour éclairer les pratiques du formateur.

Les gabarits ne bénéficient d’aucune priorité du seul fait de leur nouveauté : ils rejoignent la même boîte à outils que les activités historiques et se départagent sur la pertinence réelle, pas sur leur ancienneté.

---

## Garde-fous du noyau

Les conditions exactes sont définies dans `references/activite_evaluee.md`.

Le noyau utilise notamment quatre repères :

```text
A1 — Exposition libre
A2 — Palier attaché à une notion
A3 — Budget de nouveauté = 1
A4 — Pas de notation arbitraire
```

Ces intitulés sont des repères de navigation. La formulation normative complète reste celle de `references/activite_evaluee.md`.

Autres principes importants :

- une déclaration n’est pas une preuve attestée ;
- une preuve externe rapportée peut être recevable si la tâche, les conditions et le résultat observé sont suffisamment précis ;
- le canal oral n’impose pas un palier : c’est l’acte observable qui compte ;
- la portée d’une preuve est limitée à ce qui a réellement été produit ou démontré ;
- `utiliser ≠ créer`, `exécuter ≠ écrire`, `lire ≠ produire`.

---

## Références runtime

```text
SKILL.md
references/
├── activite.md
├── activite_evaluee.md
├── activites_type/
│   ├── atelier.md
│   ├── barometre_humain.md
│   ├── brainstorming.md
│   ├── brique.md
│   ├── carte_conceptuelle.md
│   ├── devine_carte.md
│   ├── en_un_mot.md
│   ├── etude_de_cas.md
│   ├── evaluation_par_les_pairs.md
│   ├── facettes.md
│   ├── interview_croisee.md
│   ├── objet_express.md
│   ├── planche_meteo.md
│   ├── quiz.md
│   ├── recul.md
│   ├── retrospective.md
│   └── simulation_mise_en_situation.md
├── andragogie.md
├── decoupage_pedagogique.md
├── etat_des_paliers.md
├── glossaire.md
├── opo.md
├── production_documentaire.md
├── seance.md
├── sequence.md
├── syllabus.md
└── taxonomie.md
```

Rôles principaux :

- `SKILL.md` : orchestration et garde-fous prioritaires ;
- `taxonomie.md` : échelle des paliers cognitifs ;
- `activite_evaluee.md` : règles normatives A1 à A4 ;
- `etat_des_paliers.md` : suivi notion / palier / preuve ;
- `opo.md` : objectifs pédagogiques opérationnels ;
- `decoupage_pedagogique.md` : granularité et articulation des niveaux ;
- `activite.md` : socle commun et catalogue des gabarits ;
- `activites_type/` : contrats spécialisés (17 gabarits) ;
- `production_documentaire.md` : contrat de production documentaire ;
- `glossaire.md` : clarification descriptive du vocabulaire.

Le glossaire n’est pas une seconde source normative.

---

## Statut de validation

Cette V3.1.0 est la première mineure de la V3 (chantier 1 : catalogue d’activités). Sa promesse (`promesse.md`) a été gelée le 2026-09-03.

Elle a été validée avant sa promotion par deux batteries indépendantes : la batterie propre à la mineure (15/15 PASS) et la non-régression cumulative de la baseline V2.1 (14/14 PASS, aucune régression des garde-fous hérités).

Les tests de non-régression du projet, ainsi que le runtime candidat qui a produit cette version, sont conservés dans le dépôt de développement, hors de cette distribution.
