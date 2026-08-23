# Dossier opérateur — NOY004

Sections autorisées de NOY004.md, extraites par liste blanche.

## Contexte persona

Le run utilise uniquement :

```text
validation/personas/formateur.md
```

Le locuteur est le **PERSONA-FORMATEUR-FPA** : un formateur en formation qui s'adresse à l'agent comme à un assistant d'ingénierie pédagogique.

Aucun PERSONA-WEB n'est injecté dans ce scénario.

Le contenu reste dans le domaine naturel de cette persona : conception d'activité, fiche activité, livrable et critères de réussite.
## Consigne opérateur

Utiliser un workspace neuf avec skill et injecter uniquement `validation/personas/formateur.md`.

Envoyer le stimulus exactement tel qu'il est défini ci-dessus.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.