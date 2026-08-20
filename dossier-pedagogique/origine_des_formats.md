---
objectif: "Distinguer ce qui, dans le skill, relève de cadres établis, d'observations ou de choix de conception."
---

# Origine des choix pédagogiques et des formats

Ce document explique d'où viennent les principaux choix du skill.

Il distingue trois statuts :

- **établi** — appuyé sur un cadre, une pratique ou une terminologie documentée ;
- **observé** — constaté dans un dispositif de formation ou pendant la validation du skill ;
- **choisi** — décision de conception propre au produit.

Cette distinction est importante : une observation n'est pas une règle universelle, et un cadre théorique ne prescrit pas nécessairement la manière exacte dont le skill l'implémente.

Les sources externes vérifiables sont regroupées dans `bibliographie.md`.

Ce dossier est une documentation humaine de justification et de provenance. Il n'est pas une source normative du runtime : les règles opérationnelles restent dans `en_cours/`.

## 1. Cadres et notions établis

### Taxonomie cognitive

L'échelle utilisée dans `en_cours/references/taxonomie.md` s'appuie sur la taxonomie de Bloom révisée par Anderson & Krathwohl.

Le skill utilise cette taxonomie comme vocabulaire pour décrire une performance cognitive et aider à l'alignement.

Il n'en déduit pas qu'un apprentissage doive obligatoirement parcourir tous les niveaux dans un ordre rigide.

### Andragogie

La posture définie dans `en_cours/references/andragogie.md` s'appuie notamment sur les travaux de Knowles : expérience de l'adulte, autonomie, utilité perçue et implication dans l'apprentissage.

Le détail des formulations du skill reste une adaptation au contexte d'un tuteur ou assistant d'ingénierie pédagogique piloté par LLM.

### Point de départ et élicitation

L'intérêt de partir de ce que l'apprenant sait déjà est cohérent avec les travaux d'Ausubel sur l'ancrage des nouveaux apprentissages et avec la zone proximale de développement de Vygotsky.

Le skill en tire un comportement pratique en tutorat individuel : lorsqu'une information manque et qu'elle change la décision pédagogique, privilégier le dialogue et l'élicitation plutôt que l'invention de prérequis.

### Objectif pédagogique opérationnel

Les trois dimensions utilisées dans `en_cours/references/opo.md` s'appuient sur Mager :

- performance / comportement ;
- conditions ;
- critère(s).

Le skill les utilise pour rendre la performance attendue observable et évaluable.

### Alignement pédagogique

La cohérence :

```text
objectif
→ activité / tâche
→ évaluation
```

s'appuie sur l'alignement constructif de John Biggs.

Le skill l'étend opérationnellement jusqu'à :

```text
objectif
→ tâche
→ production / performance
→ critères
→ preuve
→ conclusion
```

Cette chaîne est un outil de contrôle du produit, pas une citation littérale de Biggs.

### Charge cognitive

La nécessité d'éviter une accumulation excessive de nouveautés simultanées est cohérente avec la théorie de la charge cognitive.

En revanche, la valeur précise :

```text
budget de nouveauté = 1
```

est un choix de conception du skill, pas un seuil fourni par la théorie.

### Réflexivité

La mise à distance de son action, son explicitation, son analyse et la projection vers une situation future sont des pratiques établies en formation professionnelle et en apprentissage expérientiel.

Le gabarit `Recul` constitue l'implémentation particulière retenue par le skill pour soutenir cette réflexivité.

### Fonctions de l'évaluation

La distinction entre évaluations :

- diagnostique ;
- formative ;
- sommative ;

relève du vocabulaire courant de l'évaluation en formation.

Une évaluation sommative peut être certificative lorsqu'elle participe à une validation institutionnelle.

Le skill conserve surtout une distinction fonctionnelle : le type d'évaluation dépend de ce que l'on cherche à faire de l'information recueillie, pas uniquement de son emplacement dans le parcours.

## 2. Ce qui vient de l'observation

### Formats pédagogiques historiques

Les premières versions des gabarits Atelier, Quiz et Recul ont été inspirées par des formats réellement utilisés dans un parcours de formation professionnelle au développement web.

Cette observation a fourni des exemples concrets de structures utilisables, mais elle ne constitue pas une norme générale de formation.

### Atelier

L'observation a notamment montré l'intérêt d'une structure stable pour des travaux longs réalisés avec une forte autonomie.

Le contrat actuel de l'Atelier conserve cette stabilité et une démarche en plusieurs étapes.

Le nombre et l'ordre de ses sections constituent toutefois un **contrat du skill**, pas une règle issue de la littérature pédagogique.

### Quiz

Le dispositif observé utilisait le Quiz comme auto-positionnement sans notation scolaire, avec une formulation explicitant qu'il était normal de ne pas tout réussir.

Le skill a conservé cette fonction diagnostique.

Le QCM à choix unique, la correction après chaque réponse et l'explication de la solution sont aujourd'hui des comportements par défaut du gabarit lorsque ce format est pertinent ; ce ne sont pas des propriétés universelles de tout quiz pédagogique.

### Recul

Le dispositif observé comportait des temps de reformulation et de prise de distance.

Les travaux réalisés depuis ont conduit à recentrer clairement ce gabarit sur la **réflexivité** plutôt que sur sa position dans le parcours.

Il n'est donc plus défini comme obligatoirement situé après un Atelier ni comme nécessitant une validation par un tiers.

### Durées

Certaines fourchettes de durée présentes historiquement dans les gabarits viennent de pratiques observées.

Elles restent des repères pratiques.

La durée ne définit ni une granularité ni un gabarit.

### Un enseignement important de cette observation

Le dispositif d'origine était largement asynchrone et ne matérialisait pas toujours le niveau « Séance ».

Cette observation a d'abord été généralisée à tort en une règle :

```text
asynchrone
→ pas de Séance
```

Cette généralisation a été supprimée en V2.

L'enseignement conservé est différent :

> observer un dispositif réel peut nourrir un gabarit, mais les particularités de ce dispositif ne doivent pas devenir automatiquement des règles universelles.

## 3. Ce qui vient de l'observation du comportement des LLM

La validation du skill a également produit des observations qui ne viennent ni d'un référentiel pédagogique ni du dispositif de formation d'origine.

### Exposition et preuve

Les tests ont montré l'importance de distinguer :

```text
notion exposée
≠ notion déclarée acquise
≠ performance observée
```

Cette distinction a été transformée en règle du produit : une attestation doit reposer sur une preuve compatible avec la performance visée.

Une preuve rapportée par un formateur reste recevable lorsqu'elle décrit suffisamment précisément une performance réellement observée.

### Notation spontanée

La campagne de validation a mis en évidence l'ajout fréquent de notes, points, bonus ou seuils lorsqu'une activité était simplement qualifiée d'« évaluée », même sans demande de notation.

Le skill en a tiré une règle explicite :

> évaluer d'abord à partir d'une performance observable et de critères ; ne pas inventer spontanément un système de points ou une note.

Cela ne signifie pas interdire les mesures numériques lorsqu'elles appartiennent réellement au critère ou au dispositif.

## 4. Choix de conception propres au skill

### A1 à A4

Les clauses A1 à A4 sont des garde-fous conçus pour rendre le comportement du LLM plus contrôlable.

Elles s'appuient sur des concepts pédagogiques établis et sur les observations de validation, mais leur formulation exacte appartient au produit.

La source normative est `en_cours/references/taxonomie.md`.

### Suivi notion par notion

Le choix de rattacher :

```text
notion
→ palier
→ preuve
```

plutôt que d'attribuer un niveau global à l'apprenant est un contrat du skill.

Il permet notamment d'éviter qu'une réussite globale soit interprétée comme la preuve de toutes les notions mobilisées.

### Budget de nouveauté = 1

Le seuil d'une seule notion non attestée dans une activité évaluée est volontairement conservateur.

Il répond au problème observé d'activités qui cumulent plusieurs nouveautés et perdent alors leur valeur diagnostique.

Il doit être compris comme un garde-fou du produit, pas comme une loi pédagogique générale.

### Évaluation critériée sans notation spontanée

Le skill privilégie :

```text
objectif
→ performance observable
→ critères
→ preuve
→ conclusion
```

La note ou les points restent possibles lorsqu'un référentiel, un dispositif ou une demande réelle les justifie.

### Structure de travail

Le skill utilise comme structure interne :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité
```

Cette structure sert à stabiliser le raisonnement et la génération.

Elle n'est pas présentée comme une nomenclature universelle : les organismes et référentiels peuvent employer d'autres noms ou organiser différemment les mêmes niveaux.

### Granularité, modalité et gabarit

La V2 sépare explicitement :

```text
granularité
≠ modalité
≠ gabarit
≠ difficulté
```

Les axes :

```text
synchrone / asynchrone
présentiel / distanciel
```

décrivent des conditions de mise en œuvre.

Ils ne suffisent pas à imposer une Séance, une Brique, un Atelier, un Quiz ou un Recul.

Cette séparation corrige une généralisation excessive des observations historiques.

### Socle Activité et spécialisations

`en_cours/references/activite.md` constitue le socle commun du niveau Activité.

Les gabarits spécialisés vivent dans :

```text
en_cours/references/activites_type/
```

Ils héritent du socle et ajoutent uniquement les caractéristiques nécessaires à leur finalité.

L'architecture :

```text
Activité
├── Brique
├── Atelier
├── Quiz
└── Recul
```

est un choix de conception du produit.

### Brique

La Brique a été introduite en V2 pour nommer une forme **élémentaire** d'Activité sans utiliser les termes « activité simple », « devoir », « production » ou « réalisation ».

« Élémentaire » porte sur la structure pédagogique, pas sur la difficulté.

La Brique peut notamment servir de travail autonome ou préparatoire, y compris dans une logique de classe inversée, sans être définie par cet usage.

### Découvrabilité des gabarits

Les gabarits d'Activité possèdent un front matter léger :

```yaml
kind
inherits
purpose
typical_uses
```

Ce mécanisme est un choix d'architecture agentique.

Le noyau n'a pas vocation à connaître une table fermée :

```text
situation
→ gabarit imposé
```

Il doit pouvoir identifier les gabarits disponibles, lire leur finalité et charger le contrat pertinent.

Les `typical_uses` servent d'indices de sélection et non de conditions exclusives.

### Glossaire

Le glossaire commun a été introduit pour stabiliser les termes sans dupliquer les règles.

Il est volontairement descriptif et orientant.

Lorsqu'un terme implique une règle opérationnelle, le fichier spécialisé reste la source normative.

## 5. Ce qui reste ouvert

Certains choix sont volontairement révisables.

En particulier :

- la valeur probante exacte des différentes formes de réflexivité ;
- l'articulation fine entre Recul et paliers élevés ;
- l'enrichissement futur de la bibliothèque de gabarits ;
- la généricité du vocabulaire dans des métiers autres que ceux déjà travaillés.

Une évolution future doit donc distinguer :

```text
ce qui est documenté par des sources
ce qui a été observé
ce qui a été validé expérimentalement
ce qui reste un choix de conception
```

Le rôle de ce dossier est précisément de conserver cette distinction.
