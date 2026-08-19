# Tuteur & ingénierie pédagogique

> **La version publique recommandée se trouve dans [`dist/stable/`](dist/stable/).**
>
> Elle correspond toujours à la dernière version ayant terminé son cycle de validation.

`tuteur-ingenierie-pedagogique` est un skill destiné à accompagner deux types d’utilisateurs autour d’une situation de formation :

* **le formateur**, qui conçoit et ajuste des activités de formation ;
* **l’apprenant**, qui découvre, pratique, consolide et progresse.

L’objectif est d’aider Claude à mieux tenir compte de **ce qui est réellement attesté chez l’apprenant** avant de décider de ce qu’il peut lui demander ensuite.

Claude est déjà capable, tel quel, d’apporter beaucoup dans le domaine de la formation : expliquer, proposer des exercices, structurer une séance ou accompagner ponctuellement un apprenant.

Mais son comportement peut être amélioré lorsqu’on attend de lui un **accompagnement pédagogique cohérent dans la durée**, notamment lorsqu’il faut distinguer ce qui a simplement été vu de ce qui a réellement été démontré.

`tuteur-ingenierie-pedagogique` ajoute principalement des **garde-fous sur la progression, les prérequis, les preuves de maîtrise et la conception des activités**.

---

## Versions et organisation du dépôt

Le projet distingue volontairement la **version publique validée** de la **version en cours de développement**.

```text
dist/stable/
→ dernière version publique stable et validée

stable/
→ source de la dernière version validée

en_cours/
→ candidat en développement

validation/
→ tests, procédures et éléments de validation
```

### Version publique

[`dist/stable/`](dist/stable/) est le point d'entrée recommandé pour une utilisation publique.

Son contenu doit toujours provenir d'une version ayant terminé son cycle de validation.

La version actuellement distribuée correspond à la **V1 validée**.

### Version en cours

[`en_cours/`](en_cours/) contient la version actuellement travaillée.

Elle est identifiée comme **V2** et peut évoluer au fil des tests, dry-runs et corrections du noyau pédagogique.

Elle ne doit pas être considérée comme la version publique recommandée tant que son cycle de validation n'est pas terminé.

### Principe de promotion

Le flux attendu est :

```text
en_cours/
→ validation
→ stable/
→ dist/stable/
```

`dist/stable/` ne doit donc jamais être construit directement depuis une version expérimentale non validée.

---

## Côté formateur

Le skill aide le formateur à concevoir des activités compatibles avec l’état d’apprentissage connu de l’apprenant.

Il peut notamment l’aider à :

* identifier les notions mobilisées par une activité ;
* distinguer les notions déjà attestées de celles qui ne le sont pas encore ;
* raisonner sur le niveau atteint **notion par notion**, plutôt qu’attribuer un niveau global à l’apprenant ;
* éviter de cumuler plusieurs nouveautés dans une même activité évaluée ;
* identifier les prérequis nécessaires ;
* formuler des objectifs pédagogiques observables ;
* aligner objectif, activité et preuve attendue ;
* définir des conditions et des critères permettant d’observer la réussite ;
* distinguer une preuve de maîtrise d’une simple impression ou déclaration ;
* construire des syllabus, séquences, séances, ateliers, activités ou quiz à partir de formats structurés ;
* adapter la suite d’une progression aux résultats réellement observés.

Le skill n’a pas vocation à remplacer le jugement ou l’expérience du formateur.

Il sert plutôt de **garde-fou et d’appui à la décision pédagogique**.

---

## Côté apprenant

Le skill peut également accompagner directement un apprenant adulte.

Dans ce contexte, il cherche à éviter qu’une notion soit considérée comme acquise simplement parce qu’elle a déjà été expliquée, montrée ou utilisée une fois.

Il peut notamment :

* partir du problème rencontré par l’apprenant ;
* chercher ce qu’il sait déjà réellement faire ;
* décomposer une tâche en notions mobilisées ;
* proposer une activité compatible avec l’état connu de ces notions ;
* expliquer ou illustrer une notion ;
* proposer un exercice ;
* utiliser une production de l’apprenant comme élément d’observation ;
* identifier plus précisément ce qui bloque ;
* proposer une remédiation ciblée ;
* adapter la suite du travail aux résultats obtenus.

L’objectif est notamment d’éviter de placer l’apprenant en autonomie sur une activité dont plusieurs prérequis sont encore inconnus ou non attestés.

---

## L’élément déclencheur

Le projet est né d’une situation très concrète pendant mon propre apprentissage en développement IA agentique.

Nous venions de découvrir les **middlewares dans LangChain**.

Le principe avait été abordé rapidement, puis nous avions utilisé un middleware très simple, `PIIMiddleware`, afin de comprendre à quoi ce mécanisme pouvait servir.

À ce stade, j’avais essentiellement :

* découvert le concept ;
* vu son fonctionnement général ;
* utilisé rapidement un middleware simple.

Juste après, Claude me propose un **travail autonome** autour des middlewares.

Le problème n’était pas le travail autonome en lui-même.

Le problème était ce que cette activité supposait déjà de savoir faire.

Pour la réaliser, je devais simultanément manipuler plusieurs éléments nouveaux ou insuffisamment travaillés :

* **l’héritage** ;
* **un décorateur spécifique** ;
* **une clé de redirection de graphe**.

Claude avait bien respecté, en apparence, la logique :

> théorie → pratique

Mais quelque chose manquait entre les deux.

Avoir **vu** un middleware et avoir utilisé un exemple simple ne démontrait pas que toutes les notions nécessaires à la réalisation suivante étaient maîtrisées.

Une notion peut avoir été :

* simplement présentée ;
* manipulée avec aide ;
* utilisée dans un exemple ;
* réussie une première fois ;
* réussie plusieurs fois en autonomie.

Ces situations ne constituent pas les mêmes preuves.

Et lorsque plusieurs notions non attestées sont introduites simultanément dans une activité, un autre problème apparaît : si l’apprenant échoue, il devient difficile de savoir **ce qui a réellement bloqué**.

C’est ce décalage qui a déclenché le projet.

L’idée initiale peut se résumer ainsi :

> **éviter qu’un tuteur IA confonde exposition à une notion et maîtrise réelle, puis construise la suite de l’apprentissage sur cette confusion.**

---

## Les principaux garde-fous

Le skill s’appuie actuellement sur quelques principes centraux.

### Un état par notion

Il n’attribue pas un niveau global du type :

> « l’apprenant est niveau 3 »

Le niveau ou palier est attaché à une **notion précise**.

Un apprenant peut par exemple être autonome sur les classes PHP tout en ayant encore besoin d’aide sur l’héritage.

---

### Une preuve plutôt qu'une impression

Une affirmation comme :

> « Je suis très à l’aise avec les interfaces PHP »

est une information utile, mais ne constitue pas à elle seule une preuve de maîtrise.

Le skill cherche à distinguer :

* ce qui est déclaré ;
* ce qui a été observé ;
* les conditions dans lesquelles la réalisation a eu lieu ;
* ce que cette observation permet réellement d’attester.

---

### Exposition ≠ maîtrise

Voir une notion, lire une explication ou suivre un exemple ne suffit pas à conclure que l’apprenant sait la mobiliser seul.

Le skill conserve cette distinction lorsqu’il prépare la suite de l’apprentissage.

---

### Budget de nouveauté

Pour une **activité évaluée**, le skill cherche à ne mobiliser qu’une seule notion non encore attestée.

L’objectif n’est pas de simplifier artificiellement toutes les activités.

Il s’agit surtout de conserver leur **valeur diagnostique**.

Si une activité évaluée dépend simultanément de trois notions inconnues et que l’apprenant échoue, il devient difficile de déterminer laquelle nécessite réellement une remédiation.

---

### Alignement entre objectif, activité et preuve

Le skill cherche à maintenir une cohérence entre :

```text
objectif
   ↓
activité demandée
   ↓
production ou comportement observable
   ↓
preuve
   ↓
critères de réussite
```

Si l’objectif consiste par exemple à savoir **produire** quelque chose, une simple question de restitution ne constitue pas nécessairement une preuve suffisante de cette capacité.

---

## Deux usages principaux

### Tutorat en direct

Claude accompagne directement un apprenant dans la conversation.

Il utilise alors l’état connu des notions et les productions observées pour adapter progressivement son aide.

### Ingénierie pédagogique

Claude peut aussi aider à produire des objets pédagogiques structurés, notamment :

* syllabus ;
* séquences ;
* séances ;
* ateliers ;
* activités ;
* quiz ;
* objectifs pédagogiques opérationnels ;
* activités de recul métacognitif.

Les formats et règles associés sont définis dans les fichiers de référence du skill.

---

## Périmètre

`tuteur-ingenierie-pedagogique` se concentre principalement sur :

* la progression individuelle d’un apprenant ;
* les notions et prérequis mobilisés ;
* les preuves disponibles ;
* le choix du niveau de difficulté ;
* les objectifs pédagogiques ;
* la conception d’activités ;
* l’évaluation de productions ou comportements observables ;
* la remédiation ;
* la structuration de livrables d’ingénierie pédagogique.

Il intervient donc surtout autour de questions comme :

> **Que sait déjà réellement faire l’apprenant ?**
> **Quelles notions cette activité mobilise-t-elle ?**
> **Que peut-on raisonnablement lui demander maintenant ?**
> **Quelle production permettra d’observer sa progression ?**

---

## Hors périmètre

Le skill ne cherche pas à couvrir l’ensemble du métier de formateur ni toutes les dimensions de l’accompagnement humain.

Sont notamment hors de son périmètre :

* la **gestion et la dynamique de groupe** ;
* l’animation des relations entre apprenants ;
* la gestion des conflits ;
* les problèmes de comportement ou de discipline ;
* la posture relationnelle du formateur face à un apprenant ;
* la qualité de la relation **apprenant–formateur** ;
* l’accompagnement psychosocial ou personnel ;
* les problématiques psychologiques ;
* la gestion de situations individuelles sensibles ;
* les problématiques RH ;
* la gestion administrative d’un organisme de formation.

`tuteur-ingenierie-pedagogique` n’a donc pas vocation à devenir un **assistant généraliste du métier de formateur**.

Son objectif reste volontairement plus étroit : améliorer certains comportements de l’agent liés à **la conception pédagogique et à la progression individuelle**.

---

## Attention — RGPD et données personnelles

Le skill **ne gère pas lui-même les problématiques de conformité RGPD**.

Son utilisation peut conduire à manipuler des informations concernant un apprenant :

* niveau ;
* difficultés ;
* progression ;
* productions ;
* observations ;
* éléments de suivi.

Ces informations peuvent constituer des données personnelles.

Il appartient donc à l’utilisateur de veiller notamment à :

* ne transmettre que les informations nécessaires ;
* éviter les données nominatives lorsqu’elles ne sont pas utiles ;
* anonymiser ou pseudonymiser autant que possible ;
* éviter de transmettre des données sensibles ;
* respecter les procédures de protection des données de son organisation ;
* vérifier les conditions de traitement des données par les outils utilisés.

> **Le skill ne doit pas être considéré comme un système de gestion de dossiers d’apprenants ni comme une solution assurant, à lui seul, la conformité RGPD.**

---

## Attention — les fichiers du skill ne sont pas des supports de formation

Les fichiers présents dans `tuteur-ingenierie-pedagogique` sont principalement conçus pour **guider le comportement d’un agent IA**.

Ils contiennent notamment :

* des règles ;
* des garde-fous ;
* des distinctions conceptuelles ;
* des structures de décision ;
* des critères d’observation ;
* des formats de sortie.

Ils ne sont donc **pas conçus comme des supports destinés à former directement des formateurs**.

Pris tels quels, certains documents peuvent être trop denses ou trop structurés pour un usage pédagogique humain.

> **Le skill est un outil pour agents, pas un manuel de formation pour formateurs.**

Les contenus peuvent naturellement servir de matière à un support de formation, mais ils nécessiteraient alors un travail de sélection, de simplification et d’adaptation.
