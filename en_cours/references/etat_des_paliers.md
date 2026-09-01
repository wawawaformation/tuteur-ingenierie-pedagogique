---
objectif: "Donner le format de la trace qui rend vérifiables les clauses A2 et A3."
---

# GABARIT : État des paliers

La clause A2 (`activite_evaluee.md`) impose de tenir une trace de ce qui est attesté, sinon « formellement validé » redevient une impression. Ce fichier en donne le format. Ce n'est pas un document pédagogique remis à qui que ce soit : c'est l'artefact de suivi qui rend les clauses A2 et A3 calculables.

## Format

| Notion | Palier attesté | Fondement | Quand |
|---|---|---|---|
| *nom de la notion, pas du chapitre* | 0 à 6 | l'activité + le critère rempli, ou l'attestation explicite du formateur | séance, atelier ou date |

Exemple :

| Notion | Palier attesté | Fondement | Quand |
|---|---|---|---|
| Formule conditionnelle | 3. Appliquer | Activité 2.1 — les 4 cas de test passent | Séance 3 |
| Référence absolue | 2. Comprendre | Quiz 2, feedback relu | Avant séquence 2 |
| Boucle for | 2. Comprendre | a donné l'exemple d'un parcours de panier e-commerce, correctement transposé | Séance 1, à l'oral |
| Tableau croisé | 0 | notion identifiée dans les prérequis, rien d'attesté | — |
| Injection de dépendances par constructeur | 3. Appliquer | Attestation explicite du formateur référent (rôle déclaré dans le contexte) | Séance 4 |

**Compatibilité avec les fichiers existants.** Un état des paliers déjà créé dont la colonne s'appelle `Preuve` reste valide : ne pas réécrire son en-tête au seul motif de conformité au format. La colonne porte le fondement de la notion quel que soit son libellé.

## Règles de tenue

* **Une ligne par notion, jamais une ligne par apprenant.** « L'apprenant est au niveau 3 » n'a pas de sens (clause A2).
* **Palier 0 = notion identifiée, rien d'attesté.** C'est une information utile, pas une case vide : elle signale ce que la prochaine activité peut coûter.
* **La preuve est une référence, pas un adjectif.** « Il a bien compris » n'est pas une preuve ; « l'activité 2.1 passe les 4 cas de test » en est une (`opo.md`, Critères).
* **Une déclaration d'acquisition n'est pas une preuve.** « Il l'a déjà vu », « c'est acquis » ou « considère qu'il sait le faire » peuvent exprimer une hypothèse, mais ne suffisent pas à inscrire un palier comme attesté ni à utiliser la notion comme prérequis attesté d'une activité évaluée.
* **Le fondement doit nommer sa nature.** Lorsqu'un palier de maîtrise est attesté, la cellule `Fondement` indique s'il s'agit d'une preuve observée dans la session, d'une preuve externe rapportée ou d'une attestation explicite du formateur — voir « Fondements d'un palier attesté » ci-dessous. Une attestation ne doit jamais y être consignée comme si elle était une performance observée par l'agent lui-même.
* **Une preuve externe rapportée peut être recevable.** L'utilisateur ou le formateur peut rapporter une observation faite hors de la session. Elle est exploitable si elle décrit une performance observable et suffisamment précise pour juger le palier : par exemple « il a réalisé seul le refactoring demandé et les trois tests fournis passaient ». À l'inverse, « il a déjà fait plusieurs refactorings de ce type et ça marchait » reste trop vague : la tâche, les conditions et le résultat observé ne sont pas assez identifiables pour attester un palier. Si la précision manque, conserver l'information comme hypothèse et demander les éléments observables utiles. Ne pas exiger que Claude ait lui-même assisté à la production.
* **Une preuve peut être orale.** Le canal n'impose pas le palier : une performance observable peut être écrite, orale ou réalisée par une action. Ce qui compte est l'acte effectivement demandé et observé ; la trace de preuve doit nommer cet acte et son résultat observable, pas seulement qualifier l'aisance de l'apprenant.
* **Les actes diagnostiques faibles restent plafonnés.** Reconnaître, reformuler ou donner un exemple pertinent peut renseigner les paliers 1 et 2 ; cela ne prouve pas à lui seul une mise en pratique autonome. Un Quiz d'auto-positionnement reste plafonné au palier 2 (`activites_type/quiz.md`). En revanche, une activité orale qui demande réellement d'analyser, de justifier ou d'arbitrer à partir de critères explicites peut contribuer à attester un palier supérieur si la performance correspondante est observable.
* **Le palier peut redescendre.** Si une activité ultérieure montre qu'une notion supposée attestée ne l'est pas, corriger la ligne — sans en faire un échec (`andragogie.md` §2, droit à l'erreur). Cette révisabilité s'applique identiquement à un palier fondé sur une attestation explicite du formateur.
* **Réafficher le tableau à chaque changement de palier**, pas seulement en fin de parcours. C'est ce qui permet à l'apprenant adulte de voir où il en est sans avoir à le demander (Piliers 2 et 6).

## Fondements d'un palier attesté

Pour établir un **palier de maîtrise attesté (1 à 6)**, seuls deux types de fondement sont admissibles :

1. une **preuve compatible** avec le palier visé — performance observée dans la session, ou preuve externe rapportée selon la règle ci-dessus ;
2. une **attestation explicite** d'un formateur ou responsable pédagogique, valide au sens des quatre conditions ci-dessous.

Une déclaration, une appréciation, une impression, une exposition ou une simple instruction ne peuvent pas, à elles seules, fonder un palier de maîtrise attesté — quel que soit l'interlocuteur qui les exprime.

**Cas du palier 0.** Le palier 0 signifie « notion identifiée, rien d'attesté » ; il ne constitue pas un palier de maîtrise. La cellule `Fondement` peut alors consigner l'information ayant conduit à identifier la notion, ou la raison pour laquelle rien n'est encore attesté — cette trace contextuelle ne devient pas pour autant une preuve ou une attestation de maîtrise.

### Attestation explicite — quatre conditions cumulatives

Une attestation explicite d'un palier n'est constituée que si les quatre conditions suivantes sont réunies :

1. **Rôle** — l'interlocuteur est positionné dans le contexte comme formateur ou responsable pédagogique de l'apprenant ;
2. **Acte** — il engage explicitement sa propre décision pédagogique, et non une impression, une déclaration relayée ou une simple instruction ;
3. **Notion identifiable** ;
4. **Palier identifiable**.

Si une seule de ces conditions manque, il n'y a pas d'attestation : conserver l'information selon sa nature réelle (appréciation, déclaration, hypothèse).

Le rôle de formateur est **déclaré ou établi dans le contexte conversationnel** ; il n'est jamais authentifié techniquement — ne jamais écrire ni laisser entendre qu'une vérification d'identité a eu lieu. **L'apprenant ne peut pas s'auto-attester** par cette voie. Ne pas déduire le rôle de formateur du seul fait qu'une personne parle de l'apprenant à la troisième personne, gère son fichier de suivi, ou donne un ordre concernant son palier : en l'absence de positionnement explicite, la condition de rôle n'est pas remplie.

### Ce que l'interlocuteur invoque, pas le vocabulaire employé

La distinction ne repose pas sur la présence d'un mot comme « atteste ». Elle repose sur la nature de ce que l'interlocuteur invoque lui-même :

| Ce que l'interlocuteur invoque | Effet sur le palier |
|---|---|
| une déclaration de l'apprenant qu'il relaie | aucun — reste une déclaration |
| une impression ou une appréciation (« je pense », « il me semble », « mon appréciation ») | aucun — reste une appréciation |
| une performance qu'il a précisément observée | preuve externe rapportée, dans la limite de l'acte observé |
| sa propre décision pédagogique, engagée explicitement sur une notion et un palier identifiables | attestation explicite — fonde le palier nommé |

Une appréciation générale suivie d'une demande d'inscription d'un palier (« Je pense qu'il maîtrise bien X. Mets-le au palier 3. ») reste une appréciation : elle ne devient pas une attestation du seul fait qu'un palier est nommé.

**Le fondement invoqué détermine la voie ; les voies ne se cumulent pas et ne se convertissent pas.** Lorsqu'un interlocuteur invoque une performance observée, la voie applicable est celle de la preuve, avec sa portée limitée à l'acte réellement observé (voir « Portée d'une preuve dans une activité intégrée » ci-dessous) — une instruction jointe ne convertit pas cette preuve en attestation et ne permet pas d'étendre sa portée.

La voie d'attestation permet d'établir **un palier** ; elle ne permet jamais d'établir une non-maîtrise, une incapacité ou un déficit. « Manque de preuve ≠ preuve de manque » reste pleinement applicable : une attestation ne peut jamais fonder une conclusion négative.

### Ce qui ne constitue pas une attestation

- une appréciation générale du formateur, même assortie d'un palier demandé ;
- une déclaration de l'apprenant relayée par un tiers, même par un formateur ;
- une auto-déclaration de l'apprenant sur lui-même ;
- une instruction d'inscrire un palier qui ne repose que sur l'une des situations ci-dessus.

## Portée d'une preuve dans une activité intégrée

La réussite globale d'une activité ne se propage pas automatiquement à toutes les notions qu'elle mobilise.

Pour chaque notion, vérifier ce que l'apprenant a effectivement produit ou réalisé lui-même et si cette observation correspond au comportement que l'on veut attester.

Pour chaque notion, comparer l'action exacte à attester avec l'action effectivement observée dans la preuve.

Ne pas transformer une action en une autre parce qu'elles portent sur le même objet :

* utiliser ≠ créer ;
* exécuter ≠ écrire ;
* lire ≠ produire ;
* modifier ≠ concevoir.

Lorsqu'une notion vise la création ou la production d'un artefact, son utilisation réussie — même autonome et même dans une activité globalement réussie — ne suffit pas à attester cette création ou cette production.

Exemples :

* utiliser une exception personnalisée déjà fournie ≠ avoir créé une exception personnalisée ;
* exécuter ou faire passer des tests fournis ≠ avoir écrit des tests ;
* utiliser un artefact fourni ≠ savoir le produire.

Une même activité intégrée peut néanmoins attester plusieurs notions si la performance propre à chacune est réellement observable dans la preuve.

La règle est donc :

```text
preuve de réussite globale
≠ attestation automatique de chaque notion

mais :

preuve explicite de plusieurs performances
→ plusieurs attestations possibles
```

### Portée d'une attestation explicite

Une attestation explicite `notion X + palier N` ne vaut que pour cette notion et ce palier. Elle n'atteste pas automatiquement :

- les notions voisines ou apparentées ;
- les autres prérequis d'une tâche ;
- les notions simplement mobilisées par la même activité ;
- un palier supérieur.

## Ce que ce tableau sert à calculer

Avant chaque activité évaluée : lister les notions mobilisées, lire leur palier ici, compter celles qui sont sous le palier requis. Le seuil applicable est celui de la clause A3 (`activite_evaluee.md`). Sans ce tableau, ce comptage est impossible.

## Persistance entre sessions

Le format ci-dessus vit dans la conversation. Sans protocole, il disparaît à la fin de la session — exactement le défaut que la clause A2 (`activite_evaluee.md`) interdit de tolérer. Le protocole suivant s'applique quand l'agent tourne dans un environnement avec accès fichiers (Claude Code, un projet local) ; en environnement purement conversationnel sans accès fichiers, ce protocole ne s'applique pas et la limite reste réelle (voir dernier point).

### Convention de fichier

Un fichier par apprenant, **hors du dossier du skill** — ce n'est pas une règle du skill, c'est une donnée de suivi qui appartient à l'apprenant et au formateur, et qui doit survivre à une mise à jour du skill :

```
etat_des_paliers/<nom-ou-identifiant-apprenant>.md
```

Contenu : exactement le tableau défini plus haut (Notion | Palier attesté | Fondement | Quand), rien d'autre.

### Protocole en trois temps

1. **Ouverture de session** : avant toute activité évaluée, chercher ce fichier. S'il existe, le charger comme état de départ — ne jamais repartir de zéro sans vérifier. S'il n'existe pas, le proposer à la création plutôt que de l'improviser en mémoire ; le silence de l'apprenant sur ce point n'est pas un refus, c'est une absence de décision à combler.
2. **Pendant la session** : écrire la mise à jour **au moment du changement de palier**, pas en fin de session. Une session peut s'interrompre sans préavis ; un état non écrit est un état perdu, et perdre l'état revient à annuler la clause A2 pour toute la session suivante.
3. **Reprise** : à la session suivante, le fichier fait foi — pas la mémoire de la conversation précédente, qui peut ne plus être disponible. C'est la seule source qui doit rester vraie d'une session à l'autre.

### Ce que ce protocole ne résout pas

En environnement purement conversationnel, sans accès fichiers ni mémoire persistante entre sessions gérée par ailleurs, aucun protocole ne peut créer de la persistance qui n'existe pas dans l'outil. Dans ce cas, le geste minimal est d'afficher l'état des paliers en fin de session et de demander explicitement à l'apprenant de le conserver pour le fournir à la session suivante — ce qui déplace la responsabilité de la persistance sur l'apprenant plutôt que de prétendre la résoudre.
