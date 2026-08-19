---
objectif: "Donner le format de la trace qui rend vérifiables les clauses A2 et A3."
---

# GABARIT : État des paliers

La clause A2 (`taxonomie.md` §2) impose de tenir une trace de ce qui est attesté, sinon « formellement validé » redevient une impression. Ce fichier en donne le format. Ce n'est pas un document pédagogique remis à qui que ce soit : c'est l'artefact de suivi qui rend les clauses A2 et A3 calculables.

## Format

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| *nom de la notion, pas du chapitre* | 0 à 6 | l'activité + le critère rempli | séance, atelier ou date |

Exemple :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| Formule conditionnelle | 3. Appliquer | Activité 2.1 — les 4 cas de test passent | Séance 3 |
| Référence absolue | 2. Comprendre | Quiz 2, feedback relu | Avant séquence 2 |
| Boucle for | 2. Comprendre | a donné l'exemple d'un parcours de panier e-commerce, correctement transposé | Séance 1, à l'oral |
| Tableau croisé | 0 | notion identifiée dans les prérequis, rien d'attesté | — |

## Règles de tenue

* **Une ligne par notion, jamais une ligne par apprenant.** « L'apprenant est au niveau 3 » n'a pas de sens (clause A2).
* **Palier 0 = notion identifiée, rien d'attesté.** C'est une information utile, pas une case vide : elle signale ce que la prochaine activité peut coûter.
* **La preuve est une référence, pas un adjectif.** « Il a bien compris » n'est pas une preuve ; « l'activité 2.1 passe les 4 cas de test » en est une (`opo.md`, Critères).
* **Une déclaration d'acquisition n'est pas une preuve.** « Il l'a déjà vu », « c'est acquis » ou « considère qu'il sait le faire » peuvent exprimer une hypothèse ou une décision du formateur, mais ne suffisent pas à inscrire un palier comme attesté ni à utiliser la notion comme prérequis attesté d'une activité évaluée.
* **Une preuve externe rapportée peut être recevable.** L'utilisateur ou le formateur peut rapporter une observation faite hors de la session. Elle est exploitable si elle décrit une performance observable et suffisamment précise pour juger le palier : par exemple « il a réalisé seul le refactoring demandé et les trois tests fournis passaient ». Ne pas exiger que Claude ait lui-même assisté à la production.
* **Une preuve peut venir d'un dialogue, pas seulement d'un document écrit.** En tutorat individuel, une question ouverte suivie d'une bonne réponse, ou un exemple personnel correctement transposé, sont des preuves valables (`andragogie.md`, Pilier 3) — à condition de les référencer précisément (« a donné l'exemple de… », pas « semblait à l'aise »).
* **Un quiz ou un dialogue ne renseignent jamais au-delà du palier 2** (`quiz.md`) : cocher la bonne réponse, ou donner un exemple pertinent, n'est pas produire sous contrainte réelle.
* **Le palier peut redescendre.** Si une activité ultérieure montre qu'une notion supposée attestée ne l'est pas, corriger la ligne — sans en faire un échec (`andragogie.md` §2, droit à l'erreur).
* **Réafficher le tableau à chaque changement de palier**, pas seulement en fin de parcours. C'est ce qui permet à l'apprenant adulte de voir où il en est sans avoir à le demander (Piliers 2 et 6).

## Ce que ce tableau sert à calculer

Avant chaque activité évaluée : lister les notions qu'elle mobilise, lire leur palier dans ce tableau, compter celles qui sont sous le palier requis. **S'il y en a plus d'une, l'activité est refusée** (clause A3). Sans ce tableau, ce comptage est impossible et la clause A3 n'est qu'une déclaration.

## Persistance entre sessions

Le format ci-dessus vit dans la conversation. Sans protocole, il disparaît à la fin de la session — exactement le défaut que la clause A2 (`taxonomie.md` §2) interdit de tolérer. Le protocole suivant s'applique quand l'agent tourne dans un environnement avec accès fichiers (Claude Code, un projet local) ; en environnement purement conversationnel sans accès fichiers, ce protocole ne s'applique pas et la limite reste réelle (voir dernier point).

### Convention de fichier

Un fichier par apprenant, **hors du dossier du skill** — ce n'est pas une règle du skill, c'est une donnée de suivi qui appartient à l'apprenant et au formateur, et qui doit survivre à une mise à jour du skill :

```
etat_des_paliers/<nom-ou-identifiant-apprenant>.md
```

Contenu : exactement le tableau défini plus haut (Notion | Palier attesté | Preuve | Quand), rien d'autre.

### Protocole en trois temps

1. **Ouverture de session** : avant toute activité évaluée, chercher ce fichier. S'il existe, le charger comme état de départ — ne jamais repartir de zéro sans vérifier. S'il n'existe pas, le proposer à la création plutôt que de l'improviser en mémoire ; le silence de l'apprenant sur ce point n'est pas un refus, c'est une absence de décision à combler.
2. **Pendant la session** : écrire la mise à jour **au moment du changement de palier**, pas en fin de session. Une session peut s'interrompre sans préavis ; un état non écrit est un état perdu, et perdre l'état revient à annuler la clause A2 pour toute la session suivante.
3. **Reprise** : à la session suivante, le fichier fait foi — pas la mémoire de la conversation précédente, qui peut ne plus être disponible. C'est la seule source qui doit rester vraie d'une session à l'autre.

### Ce que ce protocole ne résout pas

En environnement purement conversationnel, sans accès fichiers ni mémoire persistante entre sessions gérée par ailleurs, aucun protocole ne peut créer de la persistance qui n'existe pas dans l'outil. Dans ce cas, le geste minimal est d'afficher l'état des paliers en fin de session et de demander explicitement à l'apprenant de le conserver pour le fournir à la session suivante — ce qui déplace la responsabilité de la persistance sur l'apprenant plutôt que de prétendre la résoudre.
