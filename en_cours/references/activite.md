---
objectif: "Définir le socle commun de toute Activité pédagogique et orienter vers ses gabarits spécialisés."
---

# ACTIVITÉ — Socle commun

Une Activité est ce que l'apprenant doit effectivement faire. Sa position dans le découpage est définie dans `decoupage_pedagogique.md` §1.

Elle peut être intégrée à une Séance ou rattachée directement à une Séquence. Sa durée, sa modalité ou sa forme ne définissent pas sa nature.

## Spécialisation

Ce fichier définit le socle commun à toute Activité.

Les gabarits spécialisés se trouvent dans :

`references/activites_type/`

La bibliothèque contient actuellement :

- `brique.md` — **Brique** : tâche ciblée sans nécessité d'organiser une démarche pédagogique en plusieurs étapes ;
- `atelier.md` — **Atelier** : production nécessitant une démarche pédagogique structurée en plusieurs étapes ;
- `quiz.md` — **Quiz** : diagnostic ou auto-positionnement sur des connaissances et compréhensions ;
- `recul.md` — **Recul** : mise à distance réflexive d'une expérience, d'une action, d'une production ou d'une démarche ;
- `facettes.md` — **Facettes** : répartir l'exploration d'un thème entre sous-groupes complémentaires, restituer, reconstruire une vision d'ensemble ;
- `devine_carte.md` — **Devine-carte** : récupération et reconnaissance ludiques de notions déjà travaillées, par indices progressifs ;
- `etude_de_cas.md` — **Étude de cas** : analyser une situation contextualisée, poser un diagnostic, argumenter une décision ;
- `simulation_mise_en_situation.md` — **Simulation / mise en situation** : agir dans une situation proche d'un contexte réel ;
- `brainstorming.md` — **Brainstorming** : produire des idées en suspendant temporairement leur évaluation ;
- `planche_meteo.md` — **Planche météo** : exprimer l'état du moment (disponibilité, énergie, ressenti) ;
- `carte_conceptuelle.md` — **Carte conceptuelle** : représenter des concepts et leurs relations ;
- `en_un_mot.md` — **En un mot** : feedback apprenant très bref pour éclairer les pratiques du formateur ;
- `evaluation_par_les_pairs.md` — **Évaluation par les pairs** : faire examiner une production par d'autres apprenants à partir de critères explicites ;
- `retrospective.md` — **Rétrospective** : réguler collectivement les conditions de travail et d'apprentissage ;
- `interview_croisee.md` — **Interview croisée** : créer du lien par l'écoute et la présentation d'un pair, en binôme ;
- `objet_express.md` — **Objet express** : faciliter une première prise de parole à l'aide d'un objet médiateur ;
- `barometre_humain.md` — **Baromètre humain** : faire apparaître la diversité du groupe par un positionnement physique sur un continuum.

Chaque gabarit hérite du socle défini ici, puis le précise ou le complète selon sa finalité pédagogique.

### Rôle du front matter

Le front matter de chaque gabarit fait partie de son contrat de découverte et de sélection.

Il permet à l'agent d'identifier rapidement :

- la nature du gabarit ;
- sa finalité principale ;
- son appartenance à la famille Activité ;
- les usages typiques pour lesquels il peut être pertinent ;
- une éventuelle dérogation déclarée et son périmètre.

Le catalogue ci-dessus fournit le premier niveau de sélection. Si plusieurs gabarits restent plausibles, l'agent peut lire leur front matter pour les départager, puis charger le contenu du gabarit retenu pour appliquer son contrat détaillé.

Les usages indiqués dans le front matter sont des **indices de sélection**, pas des conditions exclusives. Une modalité, une durée ou un contexte typique ne doit pas devenir automatiquement une règle interdisant l'usage du gabarit dans un autre contexte pertinent.

## Éléments communs

Tout gabarit d'Activité comporte les éléments suivants.

### Titre

Nommer clairement l'activité.

Le titre doit permettre de comprendre rapidement ce que l'apprenant va rencontrer ou réaliser.

### Chapeau

Immédiatement après le titre, introduire l'activité par une accroche courte, concrète et engageante.

Le chapeau donne envie d'entrer dans la tâche et en fait percevoir l'intérêt.

Il ne résume pas toute la fiche et ne répète pas simplement l'objectif.

### Intention / objectif

Indiquer clairement ce que l'activité cherche à faire travailler ou à faire produire à l'apprenant.

Lorsque l'activité vise un objectif pédagogique opérationnel, celui-ci reste aligné avec les principes définis dans `opo.md`.

### Durée estimée

Donner une estimation adaptée à l'activité.

Cette durée est un repère de préparation et de pilotage. Elle ne constitue ni une limite stricte ni un critère permettant de déterminer le type d'Activité.

### Consigne / tâche à réaliser

Formuler clairement ce que l'apprenant doit faire.

La consigne doit rendre l'action attendue compréhensible sans supprimer les choix, recherches ou ambiguïtés qui font partie de l'activité.

### Production, réponse ou action attendue

Indiquer ce que l'apprenant doit produire, répondre ou réaliser à l'issue de l'activité.

La forme dépend de l'activité : document, réponse, réalisation, démonstration, choix argumenté, action observable ou autre production pertinente.

### Critère(s) de réussite / performance

Lorsque l'activité est évaluée, expliciter en toutes lettres les critères permettant de juger la réussite ou la performance attendue.

Ces critères portent sur ce que l'activité cherche réellement à faire observer et restent alignés avec l'objectif et la tâche.

Lorsque l'activité est évaluée, les critères de réussite / performance restent explicites pour l'apprenant. En revanche, ne pas révéler avant sa production les attendus détaillés réservés à la correction, une production de référence qui donnerait la solution ni les éléments de correction.

Pour toute notation ou quantification, appliquer `activite_evaluee.md`, clause A4.
