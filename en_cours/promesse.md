# Promesse du candidat

Ce document constitue la **spécification fonctionnelle** de la version candidate du skill.

La promesse est volontairement limitée aux comportements pour lesquels le skill cherche à modifier une décision pédagogique de l'agent par rapport à une génération plausible mais insuffisamment diagnostique.

Le skill ne promet pas d'améliorer globalement toute production pédagogique.

## Promesse centrale

> **Amener l'agent à prendre ses décisions d'apprentissage et d'évaluation à partir du point de départ réellement établi de l'apprenant, notion par notion, afin de préserver la valeur diagnostique des activités plutôt que de supposer les acquis ou d'empiler des difficultés.**

---

## P01 — Établir le point de départ utile avant de dérouler l'apprentissage

Lorsque les informations nécessaires à une décision pédagogique ne sont pas établies, l'agent doit chercher le point de départ utile avant de dérouler un contenu ou de construire une évaluation.

Il doit notamment :

- distinguer ce qui est explicitement connu de ce qui est seulement supposé ;
- demander les acquis pertinents lorsque leur absence change la décision pédagogique ;
- exploiter les réponses de l'apprenant pour adapter la suite ;
- ne pas transformer cette élicitation en questionnaire systématique lorsqu'elle n'est pas nécessaire.

L'objectif n'est pas de poser davantage de questions, mais de **ne pas prendre une décision importante à partir d'acquis inventés**.

**Test ancre historique :** T18.

---

## P02 — Raisonner par notion et par preuve

L'agent doit raisonner sur l'état des **notions effectivement mobilisées**, et non attribuer un niveau global à l'apprenant.

Il doit distinguer :

- exposition à une notion ;
- accompagnement dans sa mise en œuvre ;
- déclaration ou impression de compréhension ;
- preuve observable compatible avec le niveau que l'on souhaite attester.

Une notion n'est considérée comme maîtrisée au niveau demandé que lorsqu'une preuve compatible avec ce niveau est disponible.

Conséquences attendues :

- une démonstration ou un accompagnement guidé ne valent pas automatiquement preuve autonome ;
- un quiz de compréhension ne prouve pas à lui seul une capacité de production ;
- une activité évaluée doit être conçue à partir de ce qui est réellement attesté ;
- une nouvelle preuve peut conduire à réviser l'état précédemment retenu.

**Tests de référence :** T06, T07, T14, T24.

---

## P03 — Préserver la valeur diagnostique d'une activité évaluée

Avant de proposer une activité évaluée, l'agent doit identifier les notions nécessaires à sa réussite et distinguer celles qui sont attestées de celles qui sont nouvelles au niveau demandé.

Pour une activité évaluée visant à produire une preuve exploitable, le **budget de nouveauté est limité à une notion nouvelle**.

L'agent doit notamment :

- accepter une activité comportant une seule nouveauté lorsque les autres prérequis nécessaires sont attestés ;
- ne pas confondre nouvelle tâche et nouvelle notion ;
- refuser ou découper une activité qui empile plusieurs notions non attestées ;
- résister à une demande de difficulté artificielle si cette difficulté détruit la valeur diagnostique de l'activité ;
- fournir en échafaudage les éléments qui ne sont pas eux-mêmes l'objet de l'évaluation ;
- permettre une activité de synthèse intégrée lorsque les briques nécessaires ont préalablement été attestées.

Le principe n'est donc pas :

> une activité complexe est interdite.

Le principe est :

> **une activité ne doit pas être utilisée pour conclure sur une maîtrise si son échec ou sa réussite ne permet plus d'identifier ce qui est réellement démontré.**

**Tests ancres historiques :** T09, T24, T27.

---

## P04 — Aligner ce qui est visé, demandé et utilisé comme preuve

L'agent doit maintenir la cohérence entre :

1. ce que l'apprenant est censé apprendre ou démontrer ;
2. ce que l'activité lui demande effectivement de faire ;
3. ce que l'on utilisera pour conclure sur son niveau ou sa réussite.

Il doit notamment :

- ne pas utiliser une tâche de production autonome pour prétendre évaluer uniquement une compréhension ;
- ne pas utiliser une preuve de reconnaissance ou de restitution pour attester une capacité de production ;
- expliciter ou corriger un décalage entre objectif, tâche et critère ;
- choisir une forme d'évaluation compatible avec ce que l'on cherche réellement à établir.

**Tests de référence :** T12, T14.

---

# Garanties de fonctionnement

Ces garanties participent à la fiabilité du skill mais ne constituent pas, à elles seules, sa promesse différentielle principale.

## G01 — Ne pas inventer un état ou une persistance absente

L'agent ne doit pas prétendre disposer d'un état de progression qui n'est pas effectivement accessible.

## G02 — Ne pas arbitrer silencieusement une contradiction documentaire pertinente

Lorsque deux sources réellement mobilisées donnent des directives contradictoires, l'agent doit signaler la contradiction plutôt que choisir silencieusement une règle.

## G03 — Ne pas transformer les paliers cognitifs en barrières absolues

Les paliers servent à raisonner sur l'objectif et sur la preuve.

Ils ne doivent pas interdire l'utilisation d'une situation complexe, d'une analyse ou d'un problème réel comme point d'entrée pédagogique.

## G04 — Respecter le périmètre demandé

L'agent doit répondre au besoin demandé sans élargir inutilement la production.

---

# Principes de qualité hors promesse différentielle

Les éléments suivants restent souhaitables dans le skill, mais ne sont **pas revendiqués comme constituant à eux seuls sa valeur différentielle** :

- posture professionnelle et non infantilisante ;
- ancrage dans des situations concrètes ;
- choix pertinent entre Activité, Atelier, Quiz, Séance ou autre granularité ;
- adaptation à la modalité synchrone ou asynchrone ;
- stabilité des gabarits de production.

Ils peuvent faire l'objet de tests de non-régression ou de conformité, mais leur réussite ne suffit pas à démontrer l'apport propre du skill.

---

# Critère comportemental central

Le succès du skill ne se mesure pas à la longueur de la réponse ni au fait que l'agent cite ses règles.

La question centrale est :

> **Une information pédagogique pertinente différente conduit-elle l'agent à prendre une décision différente lorsque cette information devrait effectivement modifier l'apprentissage ou l'évaluation ?**

Le comportement recherché est :

Demande
   ↓
Point de départ utile
   ↓
Notions réellement mobilisées
   ↓
État attesté et preuves disponibles
   ↓
Nouveautés nécessaires
   ↓
Valeur diagnostique de l'activité
   ↓
Alignement objectif / tâche / preuve
   ↓
Décision pédagogique

et non :

Demande
   ↓
Génération immédiate d'une activité plausible
