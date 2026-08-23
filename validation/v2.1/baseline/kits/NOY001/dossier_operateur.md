# Dossier opérateur — NOY001

Sections autorisées de NOY001.md, extraites par liste blanche.

## Contexte persona

Le run utilise uniquement **PERSONA-WEB**.

Le persona représente le développeur web intermédiaire qui s'adresse directement à l'agent comme à un **tuteur** pour progresser.

Aucun persona FORMATEUR-FPA ne doit être injecté dans ce scénario.

Le locuteur des trois tours est le même développeur apprenant.

## Notion testée

```text
Injection de dépendances par constructeur en PHP
```

Cette notion reste cohérente avec le profil du persona : bases de la programmation orientée objet acquises, mais architecture logicielle non supposée maîtrisée.

## Fixture

Le run fournit un état des paliers propre à l'apprenant.

Chemin :

```text
etat_des_paliers/apprenant-noy001.md
```

Contenu initial :

```markdown

## Consigne opérateur

Utiliser un workspace neuf pour le run avec skill.

Ne pas injecter PERSONA-FORMATEUR-FPA.

Recréer la fixture initiale avant le run et ne jamais la recopier depuis un workspace déjà exécuté.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.
