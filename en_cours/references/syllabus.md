---
objectif: "Structurer le cadrage d'un Module sous forme de Syllabus Augmenté."
---

# Le syllabus augmenté

Ce document définit la structure du livrable le plus haut de l'ingénierie de formation (Niveau Module). Il compile toutes les données contractuelles, pédagogiques et logistiques nécessaires à la viabilité d'un parcours.

Le "Syllabus Augmenté" **est** le livrable du niveau Module défini dans `decoupage_pedagogique.md` (public cible, prérequis, grand découpage des séquences) — ce document en donne la structure détaillée, ce n'est pas un document distinct.

### 1. Structure Standard du Syllabus Augmenté

Lorsqu'un utilisateur demande à l'agent IA de concevoir un "Syllabus Augmenté", ce dernier doit impérativement générer les sections suivantes : 

### A. Bloc Identification & Logistique

* **Nom du module** : Titre clair et orienté compétences.
* **Public cible & Prérequis** : Profil type des apprenants et compétences minimales exigées pour suivre (ex: "Savoir utiliser un terminal").
* **Volume horaire & Modalités** : Durée totale (heures/jours) et format (100% distanciel, hybride, asynchrone).

### B. Bloc Pédagogique (Alignement strict)

* **Compétence macro visée** : La promesse de sortie de la formation.
* **Objectifs Pédagogiques Opérationnels (OPO)** : Rédigés selon la **règle des 3C** (Comportement, Conditions, Critères).
* **Matrice d'Évaluation** : Description explicite des modalités de contrôle (QCM, projet de fin d'études, soutenance orale) prouvant l'atteinte des OPO.

### C. Bloc "Augmenté" (La plus-value du document)

* **Le "Why" Global (Ancrage andragogique)** : Pourquoi ce module est indispensable sur le marché du travail ou en production réelle.
* **Ressources & Environnement technique** : Les outils requis (ex: VS Code, Docker, Node v20) et liens vers les documentations officielles.
* **Scénario de Progression (Le chemin de fer)** : Table des matières chronologique listant brièvement chaque Séquence amont et son enchaînement.

### 2. Directives Système pour la Génération

* **Portée de A1 à A4** : le syllabus n'est pas lui-même une activité évaluée. En revanche, dès qu'il décrit une évaluation, une progression ou des prérequis, ceux-ci doivent être compatibles avec l'état des paliers et les clauses A1 à A4 de `taxonomie.md`. Le détail des contrôles s'applique ensuite au niveau des activités évaluées.
* **Modalités et découpage** : expliciter les modalités utiles au cadrage, puis appliquer `decoupage_pedagogique.md` §2-3. Les modalités influencent la conception mais ne permettent pas de déduire automatiquement si le Module comporte des Séances ou des Activités directement rattachées à une Séquence, ni quel gabarit d'Activité utiliser.
* **Différence Clé avec la Fiche de Séance** : Le syllabus augmenté ne contient **pas de texte de cours**, pas de scripts de code détaillés, et pas de minutage au quart d'heure. Il trace le *cadre*, pas le détail des séances.
* **Interdiction d'inventer des éléments** : Si l'utilisateur demande un syllabus augmenté sur un thème générique sans donner ses contraintes, l'IA ne doit pas halluciner ces valeurs (public, durée...) — ce n'est pas une règle andragogique (l'andragogie porte sur les futurs apprenants du cours, pas sur la personne qui demande le syllabus), juste la confirmation d'hypothèse déjà attendue de tout agent. Elle propose une version standard puis demande à l'utilisateur de valider le public et la durée.
* **Exemple de transition vers le Micro** : Une fois le Syllabus Augmenté généré et validé par l'utilisateur, l'agent doit proposer la suite : *"Votre module est désormais cadré. Souhaitez-vous que nous rédigions la fiche de la première Séquence ou le déroulé de la première Séance ?"*
