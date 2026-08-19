---
objectif: "Déterminer, selon la modalité, les échelles de découpage à générer et leurs gabarits associés."
---

# Découpage pédagogique

Ce document sert de moteur de structure temporelle et de catalogue de livrables pour l'agent IA. Il définit l'architecture des contenus et encadre la génération de fiches pédagogiques à la demande. 

## 0. Préalable : la modalité détermine le découpage

Avant tout découpage, l'agent lit la **modalité** déclarée dans le Syllabus Augmenté (`syllabus.md`, Bloc A — « Volume horaire & Modalités »). C'est elle qui décide du nombre d'échelles :

| Échelle | Synchrone / présentiel | Asynchrone / plateforme |
|---|---|---|
| 1 | Module | Parcours (même niveau, autre nom produit) |
| 2 | Séquence — articulation entre activités | Séquence — articulation entre activités |
| 3 | **Séance** — unité encadrée, un seul OPO | *absente* |
| 4 | Activité — un seul palier, pas de méthode en étapes | Atelier (méthode en étapes) / Quiz (diagnostic) / Recul (métacognitif) |

*Durées observées, à titre indicatif seulement — jamais le critère de niveau : Séquence 2-4h encadrées en présentiel ou 8-15h en asynchrone (production incluse) ; Séance 30-60min ; Activité 5-15min ; Atelier 1h30-3h ; Quiz 10-15min ; Recul 20-40min. Voir `origine_des_formats.md`.*

**Le rung « Séance » n'est pas facultatif au sens flou : il est conditionné par la modalité, pas par sa durée.** En présentiel, la Séance est l'unité de temps que le formateur doit tenir devant un groupe — le déroulé minuté est un livrable réel et attendu. En asynchrone, elle n'a pas d'objet : l'apprenant gère lui-même son temps, et on passe de la Séquence directement à l'Atelier / Quiz / Recul. C'est le découpage réellement observé en production (`origine_des_formats.md`).

**Les deux fourchettes de durée de la Séquence ne se contredisent pas** : elles ne mesurent pas la même chose, et aucune des deux n'est le critère qui définit le niveau Séquence — c'est l'articulation entre activités qui le définit (§1). En présentiel, les heures encadrées excluent la production du livrable, faite hors séance. En asynchrone, elles l'incluent. Ne pas corriger l'une par l'autre : choisir selon la modalité déclarée.

## 1. Les Échelles du Découpage Pédagogique

L'agent doit catégoriser son contenu selon l'échelle appropriée pour maintenir le cap sans noyer l'apprenant.

[ MODULE / PARCOURS ] ➔ Grand bloc de compétences (ex: 2 semaines / plusieurs chapitres)
   ↳ [ SÉQUENCE ] ➔ Thématique ou chapitre précis
        ↳ [ SÉANCE ] ➔ (synchrone uniquement) unité encadrée, un seul OPO
             ↳ [ ACTIVITÉ ] ➔ L'exercice de l'apprenant — en asynchrone : Atelier / Quiz / Recul

## Le Module (L'enveloppe globale)

* **Contenu** : Un grand ensemble de compétences visant un objectif métier global.
* **Livrable attendu s'il est demandé** : Un référentiel de compétences, les prérequis globaux, le public cible et le grand découpage des séquences (ex: *"Programme de formation complet : Développeur API Node.js"*).

## La Séquence (Le chapitre thématique)

* **Contenu** : Un sous-ensemble cohérent de savoirs conceptuels et procéduraux.
* **Livrable attendu s'il est demandé** : Une fiche de progression logique (gabarit : `sequence.md`), avec l'articulation des concepts clés (ex: *"Fiche de séquence : Maîtriser le modèle CRUD et les bases de données"*).

## La Séance (L'unité de travail / le cours) — modalité synchrone uniquement

* **Contenu** : Une unité continue centrée sur un objectif spécifique unique (durée indicative : 30 à 60 min).
* **Livrable attendu s'il est demandé** : Un déroulé pédagogique minute par minute contenant : le "Why" (ancrage), l'apport théorique (concept), le fil conducteur et la transition vers la séance suivante (ex: *"Fiche de séance : Sécuriser une route POST avec du hachage"*).
* **Ordre des activités** : les activités évaluées d'une même Séance suivent l'ordre croissant des niveaux Bloom et respectent le **budget de nouveauté** (`taxonomie.md` §2, clause A3 : une seule notion non attestée par activité évaluée). Les temps d'exposition, de démonstration ou de pair-programming guidé ne sont pas contraints par cet ordre (clause A1) et peuvent donc ouvrir la séance sur le problème réel, à n'importe quel niveau.

## L'Activité (Le micro-exercice)

* **Contenu** : La tâche précise, immédiate et évaluable confiée à l'apprenant.
* **Noms en modalité asynchrone** : ce niveau se décline en **Atelier** (production évaluée en plusieurs étapes), **Quiz** d'auto-positionnement (diagnostic non noté) et **Recul** métacognitif (aucun livrable technique) — gabarits dédiés : `atelier.md`, `quiz.md`, `recul.md`.
* **Livrable attendu s'il est demandé**, en deux volets distincts (ne jamais les fusionner en un seul document remis tel quel à l'apprenant) :

  * **Destiné à l'apprenant** : l'énoncé de l'exercice (un **OPO rédigé selon les 3C**) ciblant une case précise de **Bloom**, et le code de départ fourni.
  * **Interne au formateur, non transmis avec l'énoncé** : la solution attendue et ses critères de validation — sert à vérifier le travail de l'apprenant une fois produit, jamais à le lui fournir à l'avance (ex: *"Fiche d'activité : Écrire la fonction de hashage dans le contrôleur"*).

## Directives pour la Génération de Fiches à la Demande

Lorsque l'utilisateur demande explicitement la rédaction d'une fiche (Séquence, Séance, etc.), l'agent doit respecter les règles de granularité suivantes : 

* **Respecter le périmètre strict** : Si l'utilisateur demande une *fiche de séance*, l'IA ne doit pas rédiger le programme de tout le module. Elle doit se focaliser sur l'unité de temps demandée en mentionnant simplement succinctement où elle s'insère (Séquence amont/aval).
* **Adapter le niveau de détail** : 

  * Une fiche de *Séquence* liste des **intentions et des articulations de cours**.
  * Une fiche de *Séance* liste du **contenu textuel de cours, du timing et des transitions**.
  * Une fiche d'*Activité* fournit des **énoncés précis, des contraintes techniques (3C) et du code**.
* **Conventions de rédaction (callouts)** : trois encarts, et pas davantage, pour rester lisible d'une fiche à l'autre.
  * **Bon à savoir** — un argument de contexte ou un choix de conception délibéré (pourquoi un brief est volontairement incomplet, pourquoi cette étape existe).
  * **Vigilance** — une limite de l'exercice (ce qu'on ne cherche pas encore à faire).
  * **Important** — une objection prévisible de l'apprenant, traitée avant qu'il ne la formule.
  * Un callout n'est pas obligatoire : la posture andragogique peut parfaitement se porter par le texte courant.
* **Gabarits détaillés par format** : `syllabus.md` (Module), `sequence.md`, `seance.md` et `activite.md` (synchrone), `atelier.md`, `quiz.md`, `recul.md` (asynchrone). Trace de suivi : `etat_des_paliers.md`.
* **Garder le réflexe andragogique** : Même dans une fiche purement textuelle rédigée pour l'utilisateur, l'IA doit inclure une section "Ancrage / Pourquoi apprendre cela" (Pilier 1 de l'andragogie) dédiée aux futurs apprenants de ce cours. Au niveau Séquence en particulier, ce réflexe inclut aussi le Pilier 2 (autonomie) : proposer au moins deux cas pratiques ou fils conducteurs possibles pour la séquence, plutôt qu'un seul chemin imposé.