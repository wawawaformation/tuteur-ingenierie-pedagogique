---
objectif: "Définir la règle des 3C et l'alignement objectif / activité / évaluation."
---

# Objectifs pédagogiques opérationnels (3C)

Ce document définit la structure rigoureuse que l'agent IA doit utiliser pour formuler ses objectifs de cours et garantir la cohérence scientifique de ses évaluations. 

### 1. La Règle des 3C (Formulation d'un OPO)

Pour chaque session ou sous-chapitre, l'agent ne doit pas utiliser de verbes vagues (comme *"comprendre"* ou *"connaître"*). Il doit rédiger un **Objectif Pédagogique Opérationnel (OPO)** mesurable en cochant les 3 cases suivantes : 

* **C - Comportement** : L'action observable que l'apprenant doit réaliser. Ce comportement doit obligatoirement utiliser un verbe d'action issu de la grille taxonomique (ex: *Écrire*, *Isoler*, *Critiquer*).
* **C - Conditions** : Le contexte, les outils et les restrictions fournis à l'apprenant pour réaliser l'action (ex: *A partir d'une documentation API*, *Sans utiliser de bibliothèque tierce*, *Dans un terminal Git*).
* **C - Critères** : Le seuil de réussite minimal qui valide l'objectif (ex: *Le script s'exécute en moins de 2 secondes*, *Sans aucune erreur de syntaxe*, *En trouvant au moins 3 failles de sécurité*).

**Un critère mesurable n'est pas nécessairement une note.** Pour distinguer mesure de performance et notation arbitraire, appliquer `activite_evaluee.md`, clause A4.

### Exemple de mauvaise formulation (Interdit) :

*"L'apprenant va comprendre comment fonctionne une boucle for en Python."* (Non mesurable, pas de conditions ni de critères). 

### Exemple de bonne formulation (Exigé) :

*"À la fin de l'exercice, l'apprenant sera capable d'**écrire** une boucle for (Comportement), **à partir d'une liste de dictionnaires fournie** (Conditions), **de manière à ce que le script affiche chaque élément sans lever d'erreur** (Critères)."* 

### 2. Le Principe de l'Alignement Pédagogique

L'agent IA doit maintenir une symétrie parfaite entre trois piliers majeurs. Si l'un des trois piliers dévie, la session de formation est considérée comme défaillante. 

```text
       [ Objectif Pédagogique (OPO) ]
                  /        \
                 /          \
                /            \
[ Activité d'Apprentissage ] -- [ Méthode d'Évaluation ]
```

### La règle d'alignement pour l'IA :

1. **L'Objectif** définit le niveau visé (ex: Niveau 3 de Bloom - Appliquer).
2. **L'Activité** doit entraîner l'apprenant à ce niveau exact (ex: Codage guidé d'un script).
3. **L'Évaluation** doit tester ce niveau exact (ex: Vérifier que le code s'exécute).

*Exemple de désalignement (Interdit) :* Fixer un objectif de niveau 2 (Expliquer le fonctionnement d'une base de données), faire une activité de niveau 2 (Lire un schéma), mais évaluer au niveau 6 (Demander à l'utilisateur de coder le schéma SQL complet à partir d'une page blanche). 

### 3. Contrôles avant de proposer une activité évaluée

* **Avant de proposer une activité évaluée**, l'agent vérifie que l'OPO est formulable selon les 3C et que la tâche permet réellement d'en observer les critères.
* **Vérification d'alignement** : L'agent doit s'assurer que le niveau de complexité de l'exercice (Activité) correspond à 100% au niveau exigé par la validation (Évaluation).

### Chaîne d'alignement de référence

La chaîne complète, utilisée par tout le skill, est :

```text
objectif observable
→ tâche réellement demandée
→ production ou performance observable
→ critères de réussite
→ preuve
→ portée de la preuve
→ conclusion permise : attestation, feedback ou remédiation
```

Ne pas conclure à un niveau que la preuve ne permet pas d'établir. La portée de la preuve est traitée dans `etat_des_paliers.md` ; la quantification éventuelle relève de `activite_evaluee.md`, clause A4.

### Alignement entre performance visée et preuve

L’évaluation ne doit pas seulement produire un résultat observable :
la preuve recueillie doit permettre de conclure sur le comportement annoncé
dans l’objectif.

Un même résultat final peut parfois être obtenu sans que le processus visé
ait été démontré.

Par exemple :

- réparer un code ne prouve pas nécessairement que la cause a été diagnostiquée ;
- produire une solution ne prouve pas nécessairement qu’elle peut être justifiée ;
- réussir une mise en œuvre ne prouve pas nécessairement qu’elle peut être expliquée.

Lorsque la performance visée n’est pas directement observable dans le seul
résultat final, prévoir une trace suffisante de cette performance.

Cette trace n’impose aucun format particulier : elle peut être écrite, orale,
intégrée à l’action, annotée ou consignée autrement.
