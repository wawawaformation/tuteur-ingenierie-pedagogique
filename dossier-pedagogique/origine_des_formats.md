---
objectif: "Distinguer, pour chaque règle du skill, ce qui est établi, observé, ou choisi."
---

# Origine des formats

Ce fichier existe pour une raison précise : distinguer ce qui, dans ce skill, vient de cadres établis, ce qui vient de l'observation d'un dispositif réel, et ce qui reste un choix de conception. Un formateur qui reprend ce skill doit pouvoir savoir ce qu'il peut modifier sans dommage.

Les liens vérifiables pour chaque cadre nommé ci-dessous sont dans `bibliographie.md` — ce fichier dit *quel* cadre soutient *quelle* règle, `bibliographie.md` donne la source.

## Ce qui vient de cadres établis

* **L'échelle des six paliers** (`taxonomie.md` §1) : taxonomie de Bloom révisée par Anderson & Krathwohl.
* **Les six piliers de la posture** (`andragogie.md`) : andragogie de Knowles.
* **L'élicitation en tutorat individuel** (`andragogie.md` §3, `etat_des_paliers.md`) : un cadre distinct de Knowles, plus ancien et de nature cognitive plutôt qu'andragogique. Ausubel (apprentissage significatif, 1968) : une notion nouvelle ne s'apprend pas dans le vide, elle s'accroche à une structure cognitive existante — sans ce point d'ancrage, l'apprenant mémorise sans comprendre. Vygotsky (zone proximale de développement) : ce qu'un apprenant peut faire demain avec de l'aide dépend de ce qu'il sait faire aujourd'hui sans elle — viser cette zone suppose de savoir où elle se situe, ce que seule l'élicitation renseigne de façon fiable. C'est ce second cadre, pas seulement Knowles, qui fait de l'élicitation une condition de possibilité du reste plutôt qu'une bonne pratique parmi d'autres : le budget de nouveauté (clause A3) ne peut être respecté que si l'on sait, par le dialogue, ce qui est déjà là.
* **La règle des 3C** (`opo.md` §1) : Robert Mager, *Preparing Instructional Objectives* (1962) — Performance / Conditions / Criterion, traduit ici en Comportement / Conditions / Critères.
* **L'alignement objectif / activité / évaluation** (`opo.md` §2) : John Biggs, *constructive alignment* (1996) — un cadre distinct de celui de Mager, qui porte sur la cohérence entre les trois éléments plutôt que sur la rédaction de chacun.
* **Les échelles de découpage** (`decoupage_pedagogique.md`) : macro- et micro-ingénierie de formation.

## Ce qui vient de l'observation d'un dispositif réel

Les gabarits `atelier.md`, `quiz.md` et `recul.md` ne sont pas des inventions théoriques. Ils reprennent la structure de trois formats effectivement utilisés en production sur une plateforme de formation asynchrone au développement web (parcours complet, une quinzaine de séquences, préparation à un titre professionnel).

Trois constats issus de cette observation, qui ont directement façonné les gabarits :

1. **La stabilité de structure compte plus que la richesse du plan.** Les ateliers observés suivent toujours les mêmes 8 sections, dans le même ordre. C'est ce qui rend un parcours long lisible pour un apprenant seul.
2. **La posture peut se porter par le texte courant**, sans encart dédié. Le quiz observé ne contient aucun callout « droit à l'erreur » : il écrit simplement que le quiz n'est pas noté et que l'objectif n'est pas de tout réussir. L'effet est le même.
3. **Le niveau intermédiaire « Séance » était absent de ce dispositif.** C'est ce constat qui a conduit à conditionner ce rung à la modalité (`decoupage_pedagogique.md` §0) plutôt qu'à le supprimer ou à le rendre obligatoire.

Les durées indiquées dans les gabarits sont des durées **observées**, données à titre indicatif — **jamais le critère qui définit un niveau**. Ce qui distingue réellement un niveau d'un autre : ce qui est produit (rien / un livrable minuscule / un livrable via une méthode en plusieurs étapes), le palier visé, et si l'activité est évaluée ou non. Une production qui prend dix minutes un jour et quarante un autre reste au même niveau si ces trois critères ne changent pas.

## Ce qui reste un choix de conception assumé

* **Le budget de nouveauté = 1** (`taxonomie.md` §2, clause A3) : le mécanisme invoqué a un nom — Sweller, théorie de la charge cognitive (1988) — mais le seuil précis (« une seule notion ») est un choix de ce skill, pas une valeur que la théorie impose. Elle traite le problème par la charge cognitive plutôt que par l'ordre des paliers, parce que le défaut qui a motivé ce skill était un cumul d'inconnues simultanées, pas une inversion de niveaux.
* **L'axe « types de connaissances » d'Anderson & Krathwohl a été retiré** de `taxonomie.md`, faute d'usage concret identifié au moment de sa rédaction. Le gabarit `recul.md` en constitue depuis un contre-exemple : expliciter et justifier ses propres choix relève exactement de la connaissance métacognitive. Ce retrait mérite donc d'être révisé — il n'a pas été maintenu par conviction, mais faute de preuve contraire au moment du choix.
* **Le rattachement du Recul aux paliers 5 et 2** est un pis-aller conséquence directe du point précédent.
* **Le destinataire de la fiche de Séance** (`seance.md`) n'est pas précisé dans les fichiers d'ingénierie de formation d'origine — silence total sur ce point. Une première version affirmait, par analogie hâtive avec l'Atelier, qu'elle était réservée au formateur. Ce n'était pas une donnée du corpus mais une inférence non signalée comme telle. Correction retenue : la fiche reste un outil de pilotage, mais le choix de la rendre visible à l'apprenant appartient au formateur — la dissimuler par défaut contredirait le Pilier 2 de `andragogie.md` (autonomie).
