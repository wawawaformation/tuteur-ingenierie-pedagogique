# Dossier opérateur — NOY009

Sections autorisées de NOY009.md, extraites par liste blanche.

## Contexte / Fixture

Aucune fixture technique ni état préalable n’est nécessaire.

Le run utilise uniquement :

```text
validation/personas/formateur.md
```

Le locuteur est un formateur qui demande si le gabarit Atelier est cohérent avec une activité collaborative en visioconférence, puis demande sa préparation.

### Si l’agent demande des informations supplémentaires

L’opérateur répond à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu’elles permettent de poursuivre sans modifier l’objet du test.

Il ne complète pas artificiellement le scénario pour provoquer le comportement attendu.

Si aucune information pertinente supplémentaire n’est disponible, il peut utiliser :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Puis laisser l’agent poursuivre sa réponse.

## Consigne opérateur

Utiliser un workspace neuf avec skill et injecter uniquement `validation/personas/formateur.md`.

Envoyer le stimulus exactement tel qu’il est défini ci-dessus.

Ne pas préciser spontanément si l’Atelier doit être synchrone, asynchrone, présentiel ou distanciel au-delà des informations déjà contenues dans le stimulus.

Ne pas corriger l’agent s’il affirme qu’un Atelier est réservé à une modalité : cette affirmation est précisément l’un des observables du test.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

L’opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d’invalider l’objectif du test sans introduire artificiellement de nouveaux éléments.
