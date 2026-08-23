# Dossier opérateur — NOY008

Sections autorisées de NOY008.md, extraites par liste blanche.

## Contexte / Fixture

Aucune fixture technique ou état préalable n'est nécessaire.

Le run utilise uniquement :

```text
validation/personas/formateur.md
```

Le locuteur est un formateur qui demande un objet pédagogique directement exploitable.
## Consigne opérateur

Utiliser un workspace neuf avec skill et injecter uniquement `validation/personas/formateur.md`.

Envoyer le stimulus exactement tel qu'il est défini ci-dessus.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Ne pas demander explicitement un OPO, une durée, une consigne, un livrable, des critères ou une correction : cela soufflerait le contrat que le test cherche à observer.

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.