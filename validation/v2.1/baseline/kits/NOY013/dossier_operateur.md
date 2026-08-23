# Dossier opérateur — NOY013

Sections autorisées de NOY013.md, extraites par liste blanche.

## Contexte / Fixture

Le persona `formateur-fpa` sert uniquement à la **conception du scénario**.

Il n'est pas injecté à l'agent pendant le run.

Le rôle de formateur référent est établi directement par le stimulus.

Aucun référentiel officiel n'est nécessaire au scénario.

### Notion testée

```text
Formulation de critères de réussite
```

### État initial

Chemin :

```text
etat_des_paliers/apprenant-noy013.md
```

Contenu initial exact :

```markdown

## Consigne opérateur

Utiliser un workspace neuf.

Recréer la fixture initiale avant le run.

Envoyer le stimulus exactement tel qu'il est défini.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario ou la fixture lorsqu'elles existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé.

Il ne doit pas inventer une performance, une tentative, un échec ou une réussite de l'apprenant.

Lorsque aucune information complémentaire pertinente n'est disponible, utiliser si nécessaire :

```text
Je ne peux pas t'en dire plus. Poursuis avec les éléments disponibles.
```

**L'opérateur fait au mieux, à partir des éléments disponibles, pour conduire l'interaction de manière naturelle et permettre de confirmer ou d'invalider l'objectif du test, sans introduire artificiellement d'information qui modifierait ce qui est testé.**

Lorsque des tours opérateur non prévus sont nécessaires, ils doivent être conservés dans le verbatim de la trajectoire.
