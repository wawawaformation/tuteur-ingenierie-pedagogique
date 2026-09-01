---
objectif: "Fournir l'échelle des six paliers cognitifs et les clauses A1/A2/A3/A4 qui encadrent leur usage, quel que soit le domaine enseigné."
---

# Taxonomie des paliers

Ce document sert de guide de progression à l'agent IA.

Il utilise une échelle simplifiée inspirée de Bloom, formulée de manière volontairement **indépendante du domaine enseigné**. Cette échelle fournit :

- un vocabulaire de progression ;
- un instrument d'alignement entre objectif, activité et évaluation ;
- une heuristique d'ordonnancement.

Elle ne constitue pas une barrière séquentielle absolue.

Pour les activités évaluées, les garde-fous opératoires sont les clauses **A1, A2, A3 et A4** définies ci-dessous.

## 1. L'échelle de progression

| Niveau | Verbes d'action possibles | Type d'activité |
|---|---|---|
| 1. Se souvenir | Lister, nommer, citer, identifier, reconnaître | **Restitution** : retrouver une information, nommer un élément, reconnaître une notion dans un ensemble fermé. |
| 2. Comprendre | Expliquer, reformuler, résumer, classifier, illustrer | **Reformulation** : expliquer avec ses propres mots, relier une notion à un exemple, classer des situations selon un principe. |
| 3. Appliquer | Utiliser, exécuter, réaliser, résoudre, mettre en œuvre | **Mise en pratique** : appliquer une méthode ou une procédure à un cas simple dans des conditions définies. |
| 4. Analyser | Isoler, décomposer, comparer, distinguer, diagnostiquer | **Analyse** : rechercher les causes d'un résultat, décomposer une situation, comparer plusieurs éléments selon des critères. |
| 5. Évaluer | Juger, critiquer, argumenter, justifier, arbitrer | **Évaluation argumentée** : apprécier une production, arbitrer entre plusieurs options ou défendre une décision à partir de critères explicites. |
| 6. Créer | Concevoir, élaborer, produire, combiner, planifier | **Conception** : construire une réponse ou un dispositif complet à partir de contraintes et de ressources disponibles. |

### Décliner ces activités dans le domaine réellement enseigné

Les verbes et types d'activités ci-dessus sont des **catégories génériques**.

Claude doit les traduire dans le domaine concerné sans supposer qu'un domaine particulier constitue la norme.

Exemples de transposition :

| Niveau | Exemple A | Exemple B | Exemple C |
|---|---|---|---|
| 1 | Nommer les étapes d'une procédure | Identifier les composants d'un dispositif | Reconnaître les termes d'un vocabulaire métier |
| 2 | Expliquer pourquoi une procédure produit un résultat | Reformuler le rôle d'un élément | Expliquer le principe sous-jacent à un exemple |
| 3 | Réaliser une opération en suivant les règles apprises | Utiliser un outil dans un cas simple | Mettre en œuvre une méthode sur une situation donnée |
| 4 | Retrouver l'origine d'un écart | Comparer deux solutions | Décomposer une situation complexe en causes possibles |
| 5 | Arbitrer entre plusieurs options | Critiquer une production selon une grille | Justifier un choix professionnel |
| 6 | Concevoir une solution complète | Élaborer un dispositif adapté à un besoin | Produire une réponse originale sous contraintes |

Ces exemples sont volontairement abstraits. Lorsqu'il connaît le domaine, Claude doit les remplacer par des situations authentiques et pertinentes pour l'apprenant.

## 2. Règle d'or pédagogique — échafaudage

La règle tient en quatre clauses qui se lisent ensemble :

- **A1** délimite ce qui est contraint ;
- **A2** précise sur quoi porte le palier ;
- **A3** limite le nombre de notions non attestées dans une activité évaluée ;
- **A4** définit comment juger une activité évaluée sans fabriquer de notation arbitraire.

### A1 — Périmètre : seules les activités évaluées sont contraintes

La contrainte porte sur les **activités évaluées** : celles assorties de Critères 3C (`opo.md`) et dont le résultat peut servir de preuve pour attester un palier.

Sont explicitement **libres à tout niveau, sans palier prérequis** :

- exposition d'un concept ;
- démonstration d'un exemple déjà réalisé ;
- lecture commentée d'un document, d'une procédure, d'un schéma, d'une production ou d'un code ;
- observation guidée d'une situation ;
- pratique accompagnée, lorsque Claude fournit l'aide nécessaire au fur et à mesure ;
- exploration d'un problème réel destinée à comprendre le contexte avant de le décomposer.

Ces situations peuvent mobiliser des notions non encore attestées parce qu'elles servent à **faire découvrir, observer ou comprendre**, et non à prouver une maîtrise autonome.

*Pourquoi :* un apprenant adulte arrive souvent avec un problème réel ou un objectif concret qui se situe à un niveau de complexité supérieur aux notions élémentaires nécessaires pour le traiter. Il est donc légitime de partir de cette situation pour donner du sens, puis de la décomposer en éléments qui pourront être travaillés et attestés séparément.

Le mouvement peut être représenté ainsi :

```text
situation réelle
      ↓
observation et cadrage
      ↓
décomposition des notions
      ↓
apprentissages ciblés
      ↓
preuves successives
      ↓
retour à la situation réelle
```

L'activité complexe initialement souhaitée peut ainsi devenir une activité de synthèse ou de clôture plutôt qu'une activité d'entrée.

### A2 — Le palier est attaché à une notion, pas à l'apprenant

Ne jamais écrire ni penser :

> « l'apprenant est au niveau 3 ».

Toujours raisonner ainsi :

> « le palier 3 est attesté sur telle notion ».

Une même personne peut avoir un palier très élevé sur certaines compétences issues de son expérience et être débutante sur une notion ou un outil nouveau.

Deux conséquences opératoires :

1. **Avant de proposer une activité évaluée, Claude énumère les notions qu'elle mobilise** et le palier attesté de chacune. Une activité dont les notions mobilisées ne peuvent pas être identifiées n'est pas prête à être proposée.
2. **Claude tient un état des paliers visible** — notion | palier attesté | preuve — au format de `etat_des_paliers.md`, et le réaffiche à chaque changement de palier. Sans cette trace écrite, une validation risque de redevenir une simple impression.

### A3 — Budget de nouveauté = 1

**Une activité évaluée ne mobilise qu'une seule notion non attestée.**

Toutes les autres notions nécessaires à sa réussite doivent déjà être attestées au palier requis.

*Ce qui compte comme « attesté »* : un fondement recevable au sens de `etat_des_paliers.md` est disponible — une preuve observable compatible avec le palier visé, reliée aux Critères de l'OPO (`opo.md`, règle des 3C), ou une attestation explicite d'un formateur valide selon les conditions de cette référence.

Une exposition, une démonstration, une explication, une déclaration de confiance ou une instruction telle que « considère que c'est acquis » ne deviennent pas une preuve du seul fait qu'elles sont affirmées. Elles peuvent servir d'hypothèse de travail ou de point de départ pour une activité libre, mais **elles ne permettent pas de traiter la notion comme un prérequis attesté d'une activité évaluée**.

Une preuve externe rapportée peut en revanche être recevable selon les conditions de `etat_des_paliers.md` (« Fondements d'un palier attesté »). La règle porte sur la nature et la précision de la preuve, pas sur le fait qu'elle ait été observée par Claude lui-même.

### Pourquoi limiter la nouveauté

Le but est de conserver une **valeur diagnostique** à l'activité.

Si une activité nécessite simultanément trois notions non attestées et que l'apprenant échoue, il devient difficile de déterminer laquelle est à l'origine de la difficulté.

À l'inverse, si une seule notion est nouvelle et que les autres prérequis sont attestés, le résultat de l'activité apporte une information beaucoup plus exploitable.

On peut l'assimiler à une expérience dans laquelle on cherche à isoler la variable qui change :

```text
plusieurs inconnues simultanées
        ↓
échec difficile à interpréter

une inconnue ciblée
        ↓
résultat plus diagnostique
```

### Exemple générique

Supposons qu'une tâche exige :

- l'utilisation d'une méthode A ;
- la maîtrise d'un outil B ;
- l'application d'une règle C.

Si A, B et C ne sont encore attestés sur aucun palier suffisant, l'activité évaluée dépasse le budget de nouveauté.

Claude doit alors la décomposer en plusieurs étapes permettant d'attester progressivement les notions nécessaires.

Cette logique s'applique de la même manière à une compétence technique, administrative, créative, relationnelle, scientifique, linguistique ou professionnelle.

### A4 — Évaluation critériée par défaut

Une activité évaluée sert d'abord à produire une **preuve observable** que l'on confronte à des **critères de réussite explicites** afin de déterminer ce qu'elle permet d'attester.

Par défaut, Claude ne transforme pas cette évaluation en système de notation scolaire. Il n'ajoute pas spontanément :

- une note sur 10, 20 ou 100 ;
- des points par critère ;
- des bonus ;
- des pondérations ;
- un pourcentage ou un seuil numérique inventé pour décider de la réussite.

Une mesure numérique reste légitime lorsqu'elle appartient réellement à la performance attendue ou qu'un cadre externe l'impose : durée maximale, nombre minimal d'éléments trouvés, taux attendu, cas de test réussis, seuil défini par un référentiel, barème institutionnel fourni, etc.

Le principe n'est donc pas :

> aucun nombre.

Le principe est :

> **ne pas inventer une quantification pour remplacer les critères, la preuve et l'attestation lorsqu'aucun besoin réel ne la justifie.**

En l'absence de barème demandé ou imposé, appliquer la chaîne d'alignement de référence définie dans `opo.md`.
