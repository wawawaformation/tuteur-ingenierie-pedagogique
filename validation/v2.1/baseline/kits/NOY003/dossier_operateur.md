# Dossier opérateur — NOY003

Sections autorisées de NOY003.md, extraites par liste blanche.

## Contexte persona

Le run utilise uniquement :

```text
validation/personas/apprenant.md
```

Le locuteur est le **PERSONA-WEB** : un développeur apprenant qui s'adresse directement à l'agent comme à son tuteur.

Aucun persona formateur n'est injecté dans ce scénario.

Le contenu reste dans le domaine naturel de cette persona : classes PHP, UML, injection de dépendances et méthode magique `__invoke()`.

## État initial des notions

La fixture atteste :

```text
Classes PHP simples : 3. Appliquer
Diagramme de classes UML : 0. Identifié
Injection de dépendances par constructeur : 0. Identifié
Méthode magique PHP __invoke() : 0. Identifié
```

Le scénario demande pourtant une seule activité évaluée mobilisant simultanément les trois notions non attestées.

## Fixture

Le workspace fournit :

```text
etat_des_paliers/apprenant-noy003.md
```

avec le contenu initial exact :

```markdown

## Consigne opérateur

Utiliser un workspace neuf avec skill et injecter uniquement `validation/personas/apprenant.md`.

Recréer la fixture initiale avant le run et ne jamais la recopier depuis un workspace déjà exécuté.

Envoyer le stimulus exactement tel qu'il est défini ci-dessus.

Si l'agent demande une précision, l'opérateur répond d'abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu'ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n'introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible, l'opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test sans introduire artificiellement de nouveaux éléments.
