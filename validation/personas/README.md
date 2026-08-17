# Personas de validation

Ce dossier contient les **personas fixes utilisés comme fixtures de test** dans les campagnes de validation.

Les personas fournissent uniquement un **contexte stable**.
La situation particulière, les contraintes propres au test et les informations nécessaires à l'oracle appartiennent au **scénario**.

> **Le persona fournit le contexte stable ; le scénario fournit la situation particulière.**

## Fichiers

- [`apprenant.md`](apprenant.md) — anciennement `PERSONA-WEB`
- [`formateur.md`](formateur.md) — anciennement `PERSONA-FPA`

Les anciens identifiants sont conservés dans les fiches afin de pouvoir relire les protocoles et campagnes historiques.

## Règles d'utilisation

### 1. Ne pas mettre la réponse à l'oracle dans le persona

Un persona ne doit pas contenir artificiellement une information qui rendrait le comportement attendu évident.

Par exemple, le persona formateur peut indiquer qu'il prépare le titre professionnel FPA, mais il ne doit pas fournir automatiquement le référentiel officiel complet si le scénario cherche précisément à tester la détection ou la vérification d'un référentiel.

### 2. Séparer le stable du circonstanciel

Le persona décrit seulement les caractéristiques stables utiles à plusieurs scénarios.

Exemples :

- domaine ou rôle ;
- niveau général ;
- connaissances déjà établies nécessaires à la campagne ;
- contexte professionnel générique.

Les éléments propres à un run restent dans le prompt ou la fixture du scénario.

### 3. Ne pas enrichir implicitement un run

La présence d'une information dans une fiche persona ne signifie pas qu'elle est automatiquement connue du modèle.

Le protocole de campagne doit préciser comment le persona est effectivement injecté ou rendu disponible pendant l'exécution.

### 4. Geler les personas avec la campagne

Lorsqu'une campagne dépend d'une persona, sa version doit être figée avec :

- les objectifs ;
- les prompts ;
- les oracles ;
- les autres fixtures utiles.

Une persona ne doit pas être modifiée après observation des résultats pour faciliter le scoring.

## Portée

Ces personas sont des **fixtures de test contrôlées**.

Ils ont été définis dans le périmètre réellement maîtrisé et testé du projet. Ils ne constituent pas une preuve de généricité à d'autres métiers, publics ou contextes de formation.
