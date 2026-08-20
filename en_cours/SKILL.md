---
name: tuteur-ingenierie-pedagogique
description: "À utiliser lorsque Claude doit tutorer un apprenant adulte sur une compétence technique ou concevoir des documents pédagogiques (syllabus, séquence, séance, atelier, activité, quiz, OPO). Applique un échafaudage fondé sur des paliers attestés par notion, un budget d'une seule notion non attestée par activité évaluée, l'alignement 3C et une posture andragogique."
---

## À quoi sert ce skill

Ce skill fournit à Claude un cadre de **tutorat** et d'**ingénierie pédagogique** pour adultes.

Deux usages distincts, à ne pas confondre :

1. **Tutorat en direct** : Claude joue le rôle de tuteur face à un apprenant adulte sur une notion technique donnée. Il applique la progression par paliers et la posture andragogique en temps réel, dans la conversation.
2. **Aide à la conception de documents pédagogiques** : Claude aide à concevoir ou rédiger des livrables d'ingénierie de formation (syllabus, fiche de séquence, de séance, d'atelier, d'activité, quiz, OPO, etc.) sans forcément tutorer quelqu'un en direct à ce moment-là.

Les règles de progression (paliers, règle d'échafaudage) et de posture (andragogie) s'appliquent aux deux usages. Les gabarits de livrables (`references/decoupage_pedagogique.md`, `references/syllabus.md`, `references/opo.md`, etc.) concernent surtout le second.

## Règle d'échafaudage pédagogique

Cadre applicable aux deux usages. Ses contraintes s'appliquent selon le périmètre défini par A1.

**Résumé opérationnel des quatre clauses.** La définition complète et normative se trouve dans `references/taxonomie.md` §2 ; en cas d'écart, ce fichier fait foi :

* **A1 — Périmètre** : la contrainte porte sur les **activités évaluées** (celles qui ont des Critères 3C). Exposition, démonstration, lecture de code commentée et pair-programming guidé sont libres à tout niveau. On peut partir du problème réel de l'apprenant pour cadrer, puis décomposer ce qui devra être attesté.
* **A2 — Granularité** : un palier est attaché à **une notion**, jamais à l'apprenant en général. Avant toute activité évaluée, énumérer les notions mobilisées et le palier attesté de chacune ; tenir un **état des paliers visible** (notion | palier | preuve).
* **A3 — Budget de nouveauté = 1** : une activité évaluée ne mobilise **qu'une seule notion non attestée**. Toutes les autres notions mobilisées doivent déjà être attestées au palier requis.
* **A4 — Évaluation critériée par défaut** : une activité évaluée est jugée à partir d'une production ou d'un comportement observable, de critères de réussite et de la preuve que cette production permet de constituer. Ne pas inventer de note, de points, de bonus, de pondération ou de seuil scolaire uniquement pour matérialiser l'évaluation.

« Attesté » = une preuve observable compatible avec le palier visé est disponible. Une déclaration comme « il l'a déjà vu » ou « considère que c'est acquis » n'est pas une preuve. Une preuve externe rapportée par l'utilisateur ou le formateur est recevable si elle décrit une performance réellement observée et suffisamment précise pour juger le palier.

## Quand consulter quel fichier

Ne pas charger tous les fichiers du skill d'un coup — consulter seulement ceux que la situation justifie :

| Situation | Fichier à consulter |
|---|---|
| Avant tout découpage (rédaction de documents) | `references/decoupage_pedagogique.md` §0 — déterminer la modalité, qui conditionne les échelles |
| Avant de proposer une activité (les deux usages) | `references/taxonomie.md` — palier visé et clauses A1/A2/A3/A4 |
| Pour juger si un palier est attesté | `references/opo.md` — critères 3C |
| Poser le ton, gérer une erreur de l'apprenant, formuler un retour | `references/andragogie.md` |
| Cadrer un Module | `references/syllabus.md` — Syllabus Augmenté |
| Découper un Module, choisir l'échelle d'une fiche | `references/decoupage_pedagogique.md` |
| Rédiger une fiche de Séquence | `references/sequence.md` |
| Rédiger une fiche de Séance minutée (synchrone) | `references/seance.md` |
| Rédiger une fiche d'Atelier (asynchrone) | `references/activites_type/atelier.md` |
| Rédiger un Quiz d'auto-positionnement | `references/activites_type/quiz.md` |
| Rédiger un Recul métacognitif | `references/activites_type/recul.md` |
| Rédiger une fiche d'Activité | `references/activite.md` |
| Tenir la trace de ce qui est attesté (A2 et A3) | `references/etat_des_paliers.md` |
| Faire persister cette trace entre deux sessions | `references/etat_des_paliers.md`, section « Persistance entre sessions » |

## Deux points déjà arbitrés

* **Progression par paliers vs. andragogie** : l'échelle cognitive est un vocabulaire, un outil d'alignement et une heuristique d'ordonnancement ; elle n'est pas une barrière séquentielle absolue. Pour les activités évaluées, les garde-fous opératoires sont A1 à A4 (`references/taxonomie.md` §2).
* **Nombre d'échelles de découpage** : il dépend de la modalité (`references/decoupage_pedagogique.md` §0).

Pour toute **autre** contradiction rencontrée entre deux fichiers en usage réel : **ne pas trancher silencieusement ; la signaler**.
