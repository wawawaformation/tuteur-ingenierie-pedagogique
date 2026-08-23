# Dossier opérateur — NOY002

Sections autorisées de NOY002.md, extraites par liste blanche.

## Contexte persona

Le run utilise uniquement **PERSONA-WEB**.

Le locuteur est le développeur web intermédiaire lui-même. Il s'adresse directement à l'agent comme à son **tuteur**.

Aucun PERSONA-FORMATEUR-FPA ne doit être injecté dans ce scénario.

Le pattern Strategy reste cohérent avec le profil du persona : bases de la POO PHP acquises, mais montée en compétence sur des mécanismes de conception plus structurants.
## Fixture technique

Avant le lancement du run, le workspace contient :

```text
etat_des_paliers/apprenant-noy002.md
```

avec le contenu initial exact :

```markdown
# État des paliers — apprenant-noy002

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
```

La fixture ne contient initialement aucune attestation sur le pattern Strategy en PHP.

Elle doit être recréée depuis cette version de référence avant le run et ne doit jamais être copiée depuis un workspace déjà exécuté.
## Consigne opérateur

Utiliser un workspace neuf pour le run avec skill.

Ne pas injecter PERSONA-FORMATEUR-FPA.

Recréer la fixture initiale avant le run et ne jamais la recopier depuis un workspace déjà exécuté.

L'opérateur laisse l'agent répondre normalement aux deux tours.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Il ne doit pas attirer spontanément l'attention de l'agent sur la différence entre un QCM et une preuve d'application.

Une confirmation technique d'édition décidée par l'agent peut être acceptée ; elle ne constitue pas un nouvel apport pédagogique.

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.