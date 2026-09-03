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

### Facettes (candidat V3.1.0)

Observé de façon répétée, comme formateur et comme apprenant, plutôt qu'issu d'un protocole académique appliqué tel quel : ce format sert surtout à **introduire** un sujet ou un thème, dans une logique où l'apprenant va chercher le savoir lui-même plutôt que de le recevoir — posture active déjà rattachée à Knowles dans ce document (§1, `andragogie.md`), pas une référence supplémentaire à ajouter ici.

Filiation établie et citable, sans en être une implémentation :

- **interdépendance positive** (Deutsch, 1949 ; Johnson & Johnson, 1989) — chaque sous-groupe détient une pièce indispensable à la vision d'ensemble ;
- **Group Investigation** (Sharan & Sharan — germe dans *Small-Group Teaching*, 1976 ; forme mature : *Group Investigation Expands Cooperative Learning*, 1990, et *Expanding Cooperative Learning through Group Investigation*, 1992) — parenté forte sur la structure (sous-thèmes → groupes parallèles → restitution → vision globale), mais sans l'autonomie de choix des apprenants sur les sous-thèmes ni la durée (investigation de plusieurs semaines dans la GI canonique, contre quelques dizaines de minutes ici) ;
- **Co-op Co-op** (Kagan, 1985, *Co-op Co-op: A Flexible Cooperative Learning Technique*) — parenté sur la logique équipe → présentation collective, mais sans la sous-spécialisation individuelle à l'intérieur de chaque sous-groupe que Co-op Co-op prévoit ;
- explicitement **pas un Jigsaw** (Aronson, 1978) : aucune phase de groupes d'experts recomposés entre sous-groupes.

Aucune source établie ne nomme cette variante allégée et pré-structurée par le formateur, ni son usage typique en introduction/classe inversée — vérifié par recoupement de deux sources indépendantes avant de conclure. Facettes est donc **observé + choisi** : la filiation théorique est établie, l'implémentation précise ne l'est pas.

### Devine-carte (candidat V3.1.0)

Adaptation pédagogique directe d'un jeu de société connu, de la famille **Time's Up!** (aussi désigné Celebrity ou Fishbowl selon les traditions) : mêmes cartes réutilisées sur trois manches progressivement contraintes (explication libre, un seul mot, mime). **Établi** comme mécanique de jeu, **choisi** comme adaptation pédagogique — les cartes portent des notions de formation déjà rencontrées plutôt que des noms ou expressions à deviner pour le jeu.

Observé par le formateur comme particulièrement adapté à un groupe qui a besoin de se détendre (fatigue, tension), tout en restant utile pédagogiquement : les trois manches ne testent pas la même chose. L'explication libre mobilise la compréhension ; la manche « un seul mot » force une identification précise du terme ; le mime, sans recours au verbal, vérifie un niveau d'appropriation plus exigeant que les deux précédentes.

Double fonction assumée, pas accessoire : détente du groupe **et** réactivation de savoirs théoriques déjà rencontrés — jamais introduction d'une notion nouvelle (cohérent avec les `typical_uses` déclarés du gabarit).

### Étude de cas (candidat V3.1.0)

**Établi.** La méthode des cas est l'une des techniques pédagogiques les plus anciennement documentées et les plus largement adoptées, notamment popularisée par la Harvard Business School (à partir d'une méthode d'abord développée en droit, à la Harvard Law School, sous Langdell, avant son adaptation à l'enseignement du management au début du XXe siècle). Présente nommément dans la quasi-totalité des LMS et référentiels de formation professionnelle et supérieure.

Distinction utile avec les gabarits précédents de cette liste : `étude de cas` mobilise typiquement `appliquer`, `analyser`, `évaluer` (et `créer` en option) — un tout autre niveau d'exigence cognitive que Facettes (`comprendre`/`appliquer`) ou Devine-carte (`savoir`/`comprendre`). Ce n'est pas un gabarit de premier contact ou de réactivation légère : il suppose un raisonnement complexe sur une situation contextualisée déjà en partie maîtrisée, pas une découverte ou une révision.

### Simulation / mise en situation (candidat V3.1.0)

**Établi.** Apprentissage par la mise en situation / jeu de rôle : techniques anciennement documentées et largement adoptées en formation professionnelle (santé, relation client, management), reliées à l'apprentissage expérientiel (Kolb) — l'expérience concrète comme déclencheur, suivie d'une réflexion et d'une conceptualisation, ce que le débrief de ce gabarit opérationnalise directement.

Point de vigilance observé, à conserver : l'apprentissage produit par une mise en situation est souvent **discret mais réel** — moins immédiatement visible qu'une production écrite (étude de cas, par exemple), parce qu'il touche à un comportement rejoué plutôt qu'à un raisonnement explicité. Ceci rejoint directement le principe déjà central au skill : la portée d'une preuve est limitée à ce qu'elle montre réellement (`activite_evaluee.md`). Un bon débrief ne prouve pas à lui seul un changement de comportement réel ; inversement, un apprentissage réel peut rester peu visible dans le débrief.

Précision tranchée avec l'utilisateur sur `properties.ludique: false` du front matter : confirmé correct, pas une erreur. Le jeu de rôle peut être ludique (registre théâtral, léger) ; la simulation/mise en situation au sens de ce gabarit vise la fidélité et l'entraînement comportemental proche du réel, sans obligation d'être ludique — c'est d'ailleurs ce qui a été observé dans `V31-ACT02-2` (entretien managérial sérieux). Le nom du gabarit accole les deux notions ; seule une variante jeu de rôle plus légère porterait la dimension ludique, non représentée ici.

### Tabou conceptuel — besoin identifié, véhicule non validé, **hors catalogue V3.1.0**

À la différence de Facettes et Devine-carte, ce candidat n'a **aucune validation** de l'utilisateur : ni observé, ni utilisé, ni enseigné avec, ni comme formateur ni comme apprenant. Il rompt donc le critère qui fonde le chantier 1 (`promesse.md`) — des formats éprouvés par un formateur expérimenté, pas des inventions à valider a posteriori.

Le **besoin** qu'il vise reste réel et identifié : vérifier qu'une notion est comprise en profondeur — au-delà d'une définition ou d'un vocabulaire mémorisé par cœur — en forçant sa reformulation sans les mots-clés les plus immédiats. Distinct de Devine-carte, qui teste la disponibilité en mémoire (largeur, répétition sur plusieurs notions) plutôt que la profondeur de compréhension d'une notion donnée.

Le **véhicule** envisagé — adaptation du jeu Tabou (Hasbro) — est une hypothèse de conception (**choisi**), non testée dans ce contexte pédagogique. Décision : ne pas l'intégrer au catalogue de la mineure V3.1.0 tant qu'il n'a pas été testé, par l'utilisateur ou par un run réel. Le besoin reste ouvert pour une mineure ultérieure ou un autre véhicule.

### Brainstorming (candidat V3.1.0)

**Établi.** Formalisé par Alex Osborn (*Applied Imagination*, 1953) : suspendre le jugement, viser la quantité, accueillir les idées inhabituelles, rebondir sur les idées des autres. L'une des techniques de facilitation les plus universellement documentées et diffusées.

Observation pratique de l'utilisateur, à conserver — elle nuance la réputation de simplicité du format : le protocole ne s'anime pas tout seul, le formateur doit intervenir activement pour éviter les longs silences. Ce risque est lui-même documenté dans la littérature sur la créativité en groupe (perte de productivité en groupe de brainstorming, parfois désignée *production blocking* — Diehl & Stroebe, 1987) : l'idéal d'Osborn (flux continu d'idées) se heurte en pratique à l'attente de son tour et à l'appréhension du jugement, même quand celui-ci est officiellement suspendu.

Combinaison observée avec les **5 Pourquoi** (5 Whys — origine Toyota Production System, Sakichi Toyoda), technique distincte de résolution de problème par questionnement en profondeur, parfois mobilisée par l'utilisateur en appui du brainstorming plutôt qu'en s'en tenant au seul protocole Osborn.

### Planche météo (candidat V3.1.0)

**Établi comme genre**, pas comme forme unique : les techniques de check-in d'état (« météo », couleurs, émoticônes, échelle numérique…) sont très répandues en facilitation et en méthodes agiles (rétrospectives Scrum notamment). La métaphore météo précisément est un choix parmi d'autres formes équivalentes, pas la seule référence établie.

Précision d'usage donnée par l'utilisateur : à positionner comme un **rituel**, pour des formations d'une durée un peu longue — répété au fil de la formation plutôt qu'utilisé une seule fois.

**Incohérence de métadonnée relevée par cette précision, à corriger avant intégration.** Le front matter du brouillon déclare déjà `ritual.suitable: true`, mais aussi `typical_frequency: ponctuel` — qui indique au contraire un usage isolé. Un rituel répété sur plusieurs jours de formation est l'inverse de ponctuel. `typical_frequency` devrait plutôt porter une fréquence répétée (quotidienne ou par demi-journée, par exemple), au moins pour les formations longues.

### Carte conceptuelle (candidat V3.1.0)

**Établi.** Le *concept mapping* de Joseph Novak (Cornell, années 1970-80 ; référence classique : Novak & Gowin, *Learning How to Learn*, 1984) est l'une des techniques les plus documentées en recherche pédagogique pour représenter des concepts et leurs relations.

Novak s'appuie explicitement sur la théorie de l'apprentissage significatif d'Ausubel — déjà citée en §1 de ce document (« Point de départ et élicitation ») pour un usage différent (ancrage des nouveaux apprentissages en tutorat individuel). Même filiation théorique, deux opérationnalisations distinctes dans le skill.

### En un mot (candidat V3.1.0)

**Établi comme genre** : le « one word check-out », pratique courante de clôture en facilitation et en méthodes agiles — pendant symétrique du check-in (voir Planche météo). Pas de source académique unique à citer, au même titre que Planche météo.

Distinction précisée par l'utilisateur, à ne pas confondre avec Planche météo malgré la ressemblance de surface (les deux sont brefs et ludiques) :

```text
Planche météo
→ état du moment de l'apprenant
→ plutôt en ouverture ou en milieu de séance
→ regarde vers l'apprenant, vers l'avant

En un mot
→ feedback sur les pratiques du formateur
→ en clôture : fin de journée, de séquence, de séance
→ regarde vers le formateur, vers l'arrière
```

Objectif explicitement déclaré par le `purpose` du gabarit : éclairer les futures pratiques pédagogiques du formateur — pas seulement mesurer une satisfaction ou une humeur générale.

### Évaluation par les pairs (candidat V3.1.0)

**Établi**, sur deux plans distincts : recherche en pédagogie (Topping, *Peer Assessment Between Students in Colleges and Universities*, 1998, référence de synthèse la plus citée du domaine) et présence nommée dans un LMS courant — Moodle propose un module natif dédié, « Atelier » (*Workshop*), spécifiquement construit pour l'évaluation par les pairs.

Niveau de taxonomie confirmé haut (`appliquer`, `analyser`, `évaluer` selon le front matter), cohérent avec un point relevé par l'utilisateur, plus important ici que pour les autres gabarits de cette liste : **les critères doivent être précisément spécifiés**. Ce n'est pas une simple bonne pratique externe — c'est directement le principe déjà central au skill (`activite_evaluee.md`, `opo.md` : alignement objectif → tâche → production → critères → preuve → conclusion, refus de la notation arbitraire). Sans critères explicites, l'évaluation par les pairs devient précisément ce que le skill interdit ailleurs : un jugement non justifié. Le niveau `évaluer` visé rend l'exercice du jugement lui-même l'objet de l'activité — un critère faible n'affaiblit pas seulement le retour produit, il invalide l'exercice pédagogique.

### Rétrospective (candidat V3.1.0)

**Établi.** La rétrospective Agile/Scrum — l'une des cérémonies centrales du framework Scrum (Schwaber & Sutherland, *Scrum Guide*), popularisée dans sa forme facilitée (Start/Stop/Continue et variantes) par Derby & Larsen, *Agile Retrospectives: Making Good Teams Great*, 2006 — largement diffusée bien au-delà du développement logiciel.

Point distinctif relevé par l'utilisateur, qui sépare ce gabarit des deux autres formats de « régulation » déjà documentés dans cette liste : la **régulation collective horizontale**.

```text
Planche météo / En un mot
→ collecte individuelle
→ chacun exprime séparément son état ou son avis
→ circuit vertical : vers le formateur, qui synthétise ensuite

Rétrospective
→ processus collectif
→ le groupe identifie ET priorise ensemble
→ circuit horizontal : le groupe régule lui-même, pas seulement le formateur
```

Ce n'est donc pas une variante plus longue d'En un mot : c'est un format structurellement différent, où la négociation collective (que retenir, que prioriser) fait partie de l'activité elle-même, pas seulement sa collecte.

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
