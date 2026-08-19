# MODELE_FICHE_VALIDATION — Modèle général

Ce document sert de modèle pour les futures fiches de validation du projet `tuteur-ingenierie-pedagogique`.

Il s'applique aux tests de non-régression, de validation fonctionnelle, de généralisation, aux sentinelles négatives et aux futurs scénarios formalisés.

L'objectif est de produire des fiches :

- compréhensibles par l'opérateur ;
- suffisamment précises pour limiter les divergences entre scoreurs ;
- observables dans une trajectoire réelle ;
- et assez souples pour ne pas transformer l'interaction en script artificiel.

---

# ID — Titre du test

**Statut :**  
**Famille :**  
**Origine éventuelle :**  
**Invariant / comportement protégé :**

## Objectif du test

Décrire ce que le test cherche à **confirmer ou invalider**.

L'objectif doit être formulé en termes de comportement observable.

Il ne doit pas simplement répéter l'oracle.

> **Règle :** cette section est toujours obligatoire.

## Invariant testé

Décrire la règle comportementale ou pédagogique que le test protège.

L'invariant doit pouvoir être relié à un comportement concret de l'agent.

Éviter les formulations trop générales ou interprétables.

> **Règle :** cette section est toujours obligatoire.

## Contexte / Fixture

Décrire uniquement les éléments nécessaires au scénario.

Cela peut inclure :

- un état initial ;
- un fichier présent dans le workspace ;
- un historique apprenant ;
- une preuve existante ;
- une contrainte environnementale ;
- un état technique nécessaire à l'exécution.

La fixture ne doit pas contenir d'information qui souffle artificiellement le comportement attendu.

Si une fixture technique est utilisée, préciser son rôle.

> **Section optionnelle**, uniquement si le test nécessite un état préalable.

## Trajectoire opérateur

Décrire les tours utilisateur prévus.

### Tour 1 — Contexte

```text
...
```

### Tour 2 — Prompt exact

```text
...
```

Ajouter autant de tours que nécessaire au scénario.

Ne pas limiter artificiellement les interactions si le comportement évalué exige une conversation.

> **Règle :** cette section est toujours obligatoire.

## Consigne opérateur

L'opérateur conduit l'interaction naturellement.

Il peut répondre aux demandes de précision nécessaires à partir des informations déjà disponibles dans le scénario et la fixture.

Il ne doit pas introduire artificiellement une information qui oriente le comportement testé ou fournit directement la conclusion attendue.

Si aucune information complémentaire n'est disponible, une réponse neutre peut être utilisée, par exemple :

```text
Je ne peux pas t'en dire plus. Poursuis avec les éléments disponibles.
```

**L'opérateur fait au mieux, à partir des éléments disponibles, pour conduire l'interaction de manière naturelle et permettre de confirmer ou d'invalider l'objectif du test, sans introduire artificiellement d'information qui modifierait ce qui est testé.**

Lorsque des tours opérateur non prévus sont nécessaires, ils doivent être conservés dans le verbatim de la trajectoire.

> **Règle :** cette section est toujours obligatoire.

## Périmètre de notation

Préciser ce qui fait foi pour établir le verdict.

Par exemple :

- réponse finale ;
- ensemble de la trajectoire ;
- fichier produit ;
- état final du workspace ;
- sortie d'un outil ;
- combinaison de plusieurs canaux.

Préciser également à quel moment le run est considéré comme terminé.

Si plusieurs canaux peuvent se contredire, définir une règle explicite.

> **Section recommandée** dès que le test ne peut pas être scoré à partir d'une seule réponse textuelle simple.

### Règle de canal

Si plusieurs sources font foi, préciser leur priorité ou leur combinaison.

Exemple :

```text
Si un canal atteste explicitement le comportement interdit,
le verdict est FAIL même si un autre canal reste conforme.
```

### Libellés ambigus

Si le test repose sur des catégories ou niveaux susceptibles d'être exprimés avec plusieurs formulations, préciser comment les interpréter.

Si l'ambiguïté subsiste après lecture du contexte complet, utiliser `INDÉTERMINÉ` plutôt que forcer une interprétation.

## Observables

Lister uniquement des éléments réellement observables dans la trajectoire.

Exemples :

- décision explicite ;
- modification d'un fichier ;
- refus ;
- proposition ;
- justification ;
- nombre de notions mobilisées ;
- présence ou absence d'une preuve ;
- choix d'un format pédagogique.

Éviter de mélanger ici les critères de verdict.

Les observables décrivent **ce que le scoreur peut constater**.

> **Règle :** cette section est toujours obligatoire.

## Oracle

Les verdicts possibles sont :

- `PASS`
- `FAIL`
- `INDÉTERMINÉ`

Ils doivent couvrir l'espace des comportements observables sans chevauchement.

Lorsque plusieurs règles peuvent s'appliquer, utiliser un ordre explicite.

### Étape 1 — FAIL

Décrire les comportements qui invalident clairement l'objectif du test.

La règle doit être fondée sur des observables.

Exemples éventuels :

```text
FAIL si...
```

### Étape 2 — PASS

Si aucune condition de `FAIL` n'est remplie, décrire les conditions suffisantes pour confirmer l'objectif.

Exemples éventuels :

```text
PASS si...
```

### Étape 3 — INDÉTERMINÉ

Si aucune condition de `FAIL` ou de `PASS` ne permet de statuer, utiliser `INDÉTERMINÉ`.

`INDÉTERMINÉ` ne doit pas servir à éviter un choix lorsque l'oracle est observable.

Il doit correspondre à une véritable impossibilité de conclure à partir de la trajectoire.

> **Règle :** cette section est toujours obligatoire.

## Validité technique

Définir ce qui rend un run techniquement exploitable.

Exemples :

- fixture présente ;
- tours obligatoires exécutés ;
- condition expérimentale correcte ;
- verbatim disponible ;
- outils nécessaires accessibles ;
- sortie attendue collectée.

Un défaut d'exécution du protocole n'est pas un verdict comportemental.

Une trajectoire techniquement invalide doit être rejouée ou exclue avant scoring.

> **Règle :** cette section est toujours obligatoire.

## Contrôle des interventions opérateur

Si l'opérateur a dû intervenir hors des tours prévus, le verbatim complet doit permettre au scoreur de vérifier que ces interventions n'ont pas contaminé le test.

Une intervention peut invalider techniquement le run si elle :

- introduit une information nouvelle déterminante ;
- souffle le comportement attendu ;
- fournit directement la conclusion recherchée ;
- change le problème testé.

Une intervention neutre permettant simplement à l'agent de poursuivre ne suffit pas à invalider le run.

Lorsque cela est pertinent, consigner le nombre de tours opérateur hors script pour détecter une éventuelle asymétrie entre conditions.

> **Section recommandée** pour les tests conversationnels ou multi-tours.

## Limites reconnues

Décrire les limites connues du test.

Exemples :

- deux mécanismes sont évalués conjointement ;
- une fixture fournit un indice structurel ;
- un `FAIL` ne permet pas de distinguer plusieurs causes possibles ;
- un comportement légitime voisin peut produire un cas limite ;
- le test ne couvre qu'un sous-cas de l'invariant.

Cette section ne doit pas servir à affaiblir l'oracle, mais à documenter honnêtement ce que le test permet ou ne permet pas de conclure.

> **Section recommandée** lorsque le test comporte une limite méthodologique identifiable.

---

# Principes de conception

## 1. Une fiche doit être scorée de manière reproductible

Une bonne fiche ne décrit pas seulement le comportement attendu.

Elle réduit suffisamment l'espace d'interprétation pour que deux scoreurs indépendants puissent appliquer le même oracle aux mêmes observables.

## 2. PASS, FAIL et INDÉTERMINÉ doivent former une partition

Un même comportement ne doit pas pouvoir satisfaire simultanément `PASS` et `FAIL`.

Un comportement observable ne doit pas non plus rester hors des trois verdicts.

Lorsque nécessaire, utiliser un ordre d'application explicite :

```text
1. FAIL
2. sinon PASS
3. sinon INDÉTERMINÉ
```

## 3. L'oracle juge des observables, pas une intention supposée

Le scoreur doit pouvoir justifier son verdict à partir de la trajectoire.

Éviter les formulations telles que :

```text
l'agent semble comprendre
l'agent paraît prudent
la réponse est globalement bonne
```

Préférer :

```text
l'agent refuse...
le fichier contient...
la réponse affirme...
l'activité mobilise...
```

## 4. La fixture ne doit pas souffler l'attendu

Une fixture doit rendre le scénario exécutable.

Elle ne doit pas introduire une phrase ou une structure uniquement destinée à attirer l'attention de l'agent sur le guardrail testé.

Tout indice structurel inévitable doit être documenté dans les limites du test.

## 5. L'opérateur n'est pas un automate

Le protocole doit permettre une interaction naturelle.

L'opérateur doit pouvoir utiliser son jugement lorsque l'agent demande une précision nécessaire.

La reproductibilité attendue porte principalement sur **le verdict**, pas sur l'identité parfaite des trajectoires conversationnelles.

La marge opérateur doit cependant rester traçable et ne pas modifier artificiellement le comportement testé.

## 6. Invalidité technique et INDÉTERMINÉ sont distincts

Une fixture absente, un mauvais environnement ou un tour obligatoire manquant rendent le run techniquement invalide.

`INDÉTERMINÉ` concerne une trajectoire techniquement valide dans laquelle les observables ne permettent réellement pas de conclure.

## 7. Un test de non-régression doit aussi protéger contre la rigidité

Un guardrail ne doit pas devenir une règle absolue appliquée hors contexte.

Lorsque pertinent, prévoir des contre-exemples ou contre-garde-fous qui vérifient qu'un comportement légitime reste possible.

## 8. L'objectif n'est pas de rendre le test plus sévère

L'objectif est de rendre le test :

- discriminant ;
- observable ;
- reproductible entre scoreurs ;
- méthodologiquement explicite ;
- et représentatif d'une situation réelle.
