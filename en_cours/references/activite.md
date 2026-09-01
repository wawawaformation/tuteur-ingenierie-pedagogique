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
- `recul.md` — **Recul** : mise à distance réflexive d'une expérience, d'une action, d'une production ou d'une démarche.

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

Pour toute notation ou quantification, appliquer `taxonomie.md` §2, clause A4.
