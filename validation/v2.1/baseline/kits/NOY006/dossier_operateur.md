# Dossier opérateur — NOY006

Sections autorisées de NOY006.md, extraites par liste blanche.

## Fixture

Le run fournit explicitement l'état des paliers sous forme de fixture.

Chemin dans le workspace :

```text
etat_des_paliers/apprenant-noy006.md
```

Contenu initial exact :

```markdown

## Consigne opérateur

Utiliser un workspace neuf pour chaque condition. Recréer la fixture initiale depuis la version de référence ci-dessus et utiliser exactement le même prompt avec et sans skill.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Une confirmation technique d'édition décidée par l'agent peut être acceptée ; elle ne constitue pas un apport pédagogique au scénario.

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.
