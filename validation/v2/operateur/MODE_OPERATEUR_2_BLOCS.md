# Mode opérateur — deux blocs de commande

## Principe

L'agent opérateur **ne lance jamais lui-même les runs**.

Il agit comme directeur de campagne conversationnel : il donne à l'opérateur
humain les commandes exactes à copier-coller dans son terminal, puis interprète
les retours techniques et les éventuelles interactions de Claude Code.

Chaque run suit le cycle suivant :

```text
agent opérateur
    ↓
RUN-XXX - BLOC 1
    ↓
opérateur humain copie-colle
    ↓
Claude Code testé
    ↓
interaction éventuelle gérée avec l'agent opérateur
    ↓
exit
    ↓
RUN-XXX - BLOC 2
    ↓
opérateur humain copie-colle
    ↓
contrôle collecte / archive / tokens
    ↓
run suivant
```

## BLOC 1

Le BLOC 1 prépare le workspace neuf, initialise la collecte puis lance la
session Claude Code du run.

Il utilise :

```text
OUTILS/prepare_run.py RUN-ID --launch
```

Le script détermine lui-même depuis `RUNS.csv` :

- le scénario ;
- la condition avec skill / sans skill ;
- la répétition ;
- la persona ;
- le prompt exact ;
- les fixtures ;
- le workspace neuf.

## Pendant la session

L'opérateur humain garde la main sur le terminal.

Lorsqu'une question, un choix ou une permission apparaît, il peut copier le
retour à l'agent opérateur avant de répondre.

L'agent opérateur applique `INTERACTIONS_OPERATEUR.md` et la consigne propre au
scénario. Il n'utilise jamais une réponse mécanique par défaut si le jugement
opérateur permet de mieux préserver l'objectif du test.

Si l'observable est déjà obtenu et qu'aucun tour prévu ne reste à jouer,
l'agent opérateur peut indiquer de terminer la trajectoire puis de quitter
Claude Code avec `exit`.

## BLOC 2

Après `exit`, l'agent opérateur fournit le BLOC 2 :

```text
OUTILS/finalize_run.py RUN-ID
```

Le BLOC 2 collecte la trajectoire, copie les artefacts prévus, contrôle les
métriques de tokens et crée l'archive du run.

## Format de réponse de l'agent opérateur

Pour un bloc de commande, la réponse doit être minimale :

```text
RUN-XXX - BLOC 1

<un seul bloc shell>
```

ou :

```text
RUN-XXX - BLOC 2

<un seul bloc shell>
```

Après le retour du BLOC 2, l'agent opérateur contrôle le résultat puis fournit
le BLOC 1 du run suivant si aucun STOP n'est requis.

L'agent opérateur ne score jamais les réponses pendant l'exécution.
