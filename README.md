# Tuteur & ingénierie pédagogique

<img src="docs/assets/koabana-logo.svg" alt="Koabana" width="64" />

*Koabana — les acquis en action, les preuves à l'appui.*

> **La version publique recommandée se trouve dans [`dist/stable/`](dist/stable/).**
>
> Elle correspond toujours à la dernière version ayant terminé son cycle de validation.

`tuteur-ingenierie-pedagogique` est un skill destiné à deux usages complémentaires :

- **tutorat direct d’un apprenant adulte** ;
- **assistance à l’ingénierie pédagogique pour un formateur ou concepteur**.

Il ne cherche pas à remplacer le jugement du formateur ni à imposer une méthode pédagogique universelle. Il apporte surtout des **garde-fous explicites** pour rendre la progression plus traçable, les activités évaluées plus interprétables et la conception pédagogique plus cohérente.

---

## Les trois fonctions principales

### 1. Suivre une progression par notion, palier et preuve

Le skill évite d’attribuer un niveau global à l’apprenant.

Il raisonne plutôt ainsi :

```text
notion
→ palier visé ou attesté
→ preuve disponible
→ décision pédagogique
```

Une notion peut avoir été expliquée, reconnue, appliquée avec aide ou mobilisée de manière autonome : ces situations ne constituent pas les mêmes preuves.

Le skill cherche donc à distinguer :

- ce qui a simplement été exposé ;
- ce qui est déclaré ;
- ce qui a réellement été observé ;
- ce que cette observation permet d’attester.

---

### 2. Concevoir des activités évaluées interprétables

Une activité évaluée doit permettre de comprendre ce que signifie sa réussite ou son échec.

Le skill contrôle notamment la chaîne :

```text
objectif
→ tâche
→ production ou performance observable
→ critères
→ preuve
→ conclusion
```

Il protège également la valeur diagnostique de l’activité : plusieurs notions non attestées ne doivent pas être introduites silencieusement dans une même activité évaluée.

L’objectif n’est pas de rendre les activités faciles, mais de faire en sorte qu’un résultat puisse être interprété.

---

### 3. Structurer la conception avec une bibliothèque de gabarits pédagogiques

Le skill s’appuie sur un socle commun `Activité` et sur une bibliothèque de gabarits spécialisés :

```text
Activité
├── Brique
├── Atelier
├── Quiz
└── Recul
```

Chaque gabarit précise sa finalité et des usages typiques. Ces indications orientent le choix sans enfermer le format dans une modalité unique.

L’architecture est pensée de manière agentique : les gabarits jouent un rôle proche de **tools mis à disposition de l’agent**.

```text
description / métadonnées
→ aide au choix

contenu du gabarit
→ contrat d’utilisation

SKILL.md
→ orchestration
```

Il s’agit d’une **analogie d’architecture** : les gabarits ne sont pas techniquement des tool calls.

---

## Deux modes d’utilisation

### Tutorat direct

Le skill peut accompagner un apprenant dans la conversation.

Il aide notamment à :

- partir d’un problème ou d’un objectif réel ;
- identifier ce qui est déjà attesté ;
- distinguer les notions mobilisées ;
- proposer une progression compatible avec l’état connu ;
- expliquer, guider et faire pratiquer ;
- utiliser les productions comme éléments d’observation ;
- ajuster la suite à partir des résultats obtenus.

### Ingénierie pédagogique

Le skill peut assister un formateur ou concepteur pour :

- formuler des objectifs pédagogiques observables ;
- identifier prérequis, notions et compétences mobilisées ;
- construire des Modules, Séquences, Séances et Activités ;
- choisir un gabarit d’Activité pertinent ;
- expliciter brief, production attendue et critères ;
- préserver la séparation entre ce qui est donné à l’apprenant et ce qui relève de la correction ;
- maintenir l’alignement entre objectif, tâche, preuve et conclusion.

---

## Architecture pédagogique

Le découpage interne de référence est :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité directement rattachée si pertinent
```

`Activité` constitue la granularité la plus fine.

Cette structure n’est pas présentée comme une taxonomie universelle : les appellations peuvent varier selon les organismes et référentiels.

Le skill distingue également deux axes de modalité indépendants :

```text
synchrone / asynchrone
≠
présentiel / distanciel
```

Une modalité influence la conception, mais ne détermine pas automatiquement la granularité ni le gabarit à utiliser.

---

## Principaux garde-fous

### Exposition ≠ preuve

Voir une notion, lire une explication ou suivre une démonstration ne suffit pas à conclure que l’apprenant sait la mobiliser.

### Le palier appartient à la notion

Le skill évite les formulations globales du type :

> « l’apprenant est niveau 3 »

Le palier est attaché à une notion précise et doit être relié à une preuve compatible avec ce qui est attesté.

### Budget de nouveauté

Pour une activité évaluée, le skill protège la valeur diagnostique en évitant de cumuler plusieurs notions non attestées.

### La portée d’une preuve est limitée à ce qui a réellement été observé

Par exemple :

```text
utiliser ≠ créer
exécuter ≠ écrire
lire ≠ produire
```

Une production complexe ne prouve pas automatiquement toutes les capacités qu’elle mobilise.

### Pas de notation arbitraire

Une évaluation n’implique pas nécessairement une note.

Le skill n’ajoute pas spontanément de points, de score ou de barème scolaire lorsqu’aucun système de notation réel n’est fourni ou demandé.

---

## L’élément déclencheur

Le projet est né d’une situation rencontrée pendant un apprentissage en développement IA agentique.

Après une première découverte des **middlewares dans LangChain** et l’utilisation d’un middleware simple, une activité autonome proposée ensuite exigeait simultanément plusieurs éléments encore nouveaux ou insuffisamment travaillés :

- l’héritage ;
- un décorateur spécifique ;
- une clé de redirection de graphe.

La progression paraissait respecter :

```text
théorie → pratique
```

mais elle confondait en réalité **exposition** et **maîtrise attestée**.

Si l’activité échouait, il devenait difficile de déterminer quelle notion était réellement en cause.

Le projet est parti de cette idée :

> **éviter qu’un tuteur IA construise la suite d’un apprentissage sur des acquis supposés plutôt que sur des preuves suffisamment précises.**

---

## Sources et origine

Le contenu du skill s'appuie sur deux types de sources :

- des **sources externes** — formation de Formateur Pour Adultes (FPA), ouvrages de référence en sciences de l'éducation et en ingénierie pédagogique ;
- l'**expérience propre de l'auteur** — formateur, accompagnement de stagiaires, conception pédagogique.

Le détail — ce qui relève d'un cadre établi, d'une observation ou d'un choix de conception propre au produit — est documenté dans [`dossier-pedagogique/`](dossier-pedagogique/), notamment [`origine_des_formats.md`](dossier-pedagogique/origine_des_formats.md) et [`bibliographie.md`](dossier-pedagogique/bibliographie.md).

---

## Versions et organisation du dépôt

Le dépôt sépare volontairement la version publique validée du candidat en cours de validation.

```text
dist/stable/
→ dernière version publique distribuée et validée

en_cours/
→ candidat V2.1

validation/
→ protocoles, scénarios, non-régression et artefacts de validation

docs/
→ documentation de conception et de validation
```

### Version publique

[`dist/stable/`](dist/stable/) reste le point d’entrée recommandé pour un usage public.

La version actuellement distribuée correspond à la **V2.1 validée**. V1 et V2 restent conservées pour historique.

### Candidat V2.1

[`en_cours/`](en_cours/) contient le candidat V2.1.

Son architecture runtime est stabilisée, mais il ne devient pas pour autant la version publique tant que son cycle de validation et sa promotion explicite ne sont pas terminés.

Le flux de publication reste :

```text
en_cours/
→ validation
→ dist/stable/
```

---

## Validation

Le projet conserve ses protocoles, scénarios, décisions et artefacts dans [`validation/`](validation/).

La validation distingue deux usages :

- lors de la conception d’un comportement, une comparaison **avec skill / sans skill** peut être utilisée lorsqu’elle est informative ;
- une fois le comportement stabilisé, la **non-régression du candidat** est exécutée avec skill.

Les contrats propres au produit — par exemple l’héritage du socle `Activité` ou la représentation du catalogue de gabarits — sont contrôlés directement sur le candidat, car un témoin sans skill ne connaît pas ces contrats.

La validation cherche à établir des comportements observables et reproductibles. Elle ne prétend pas démontrer qu’une théorie pédagogique est universellement vraie.

---

## Périmètre

Le skill se concentre principalement sur :

- la progression individuelle ;
- les notions, prérequis, paliers et preuves ;
- les objectifs pédagogiques ;
- la conception d’activités ;
- l’évaluation de productions ou comportements observables ;
- la remédiation ;
- la structuration de dispositifs et livrables pédagogiques ;
- l’exploitation de référentiels lorsque le contexte en fournit un.

Il n’a pas vocation à devenir un assistant généraliste couvrant l’ensemble du métier de formateur.

Restent notamment hors périmètre :

- gestion et dynamique de groupe ;
- conflits et discipline ;
- accompagnement psychosocial ou psychologique ;
- problématiques RH ;
- gestion administrative d’un organisme de formation.

---

## Attention — RGPD et données personnelles

Le skill ne gère pas lui-même la conformité RGPD.

Son usage peut conduire à manipuler des informations sur la progression, les difficultés, les productions ou les observations relatives à un apprenant.

Il appartient donc à l’utilisateur de limiter les données transmises, d’anonymiser ou pseudonymiser lorsque possible, d’éviter les données sensibles et de respecter les procédures de son organisation.

> **Le skill ne doit pas être considéré comme un système de gestion de dossiers d’apprenants ni comme une solution assurant, à lui seul, la conformité RGPD.**

---

## Les fichiers du skill ne sont pas des supports de formation

Les fichiers runtime servent avant tout à **guider le comportement d’un agent IA**.

Ils contiennent des règles, garde-fous, structures de décision, critères et contrats de production.

Ils peuvent servir de matière à un support destiné à des humains, mais nécessitent alors un travail de sélection et d’adaptation.

> **Le skill est un outil pour agents, pas un manuel de formation pour formateurs.**
