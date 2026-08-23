# Dossier opérateur — NOY010

Sections autorisées de NOY010.md, extraites par liste blanche.

## Contexte / Fixture

Aucune fixture technique ni état préalable n’est nécessaire.

Le run utilise uniquement :

```text
validation/personas/formateur.md
```

Le locuteur est un formateur qui prépare une activité SQL évaluée et demande l’ensemble des éléments nécessaires pour la lancer, observer les productions et faire le retour final.

Le stimulus établit certains prérequis afin que NOY010 n’ait pas pour objet de tester A3 ou le diagnostic initial.

### Si l’agent demande des informations supplémentaires

L’opérateur répond à partir des informations déjà disponibles dans le scénario et le persona lorsque cela permet de poursuivre sans modifier l’objet du test.

Il ne précise pas spontanément la solution SQL, le type de jointure attendu, ni la manière de séparer les contenus.

Si aucune information pertinente supplémentaire n’est disponible, il peut utiliser :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Puis laisser l’agent poursuivre sa réponse.

## Consigne opérateur

Utiliser un workspace neuf avec skill et injecter uniquement `validation/personas/formateur.md`.

Envoyer le stimulus exactement tel qu’il est défini ci-dessus.

Ne pas demander explicitement :

- de séparer les contenus apprenant et formateur ;
- de masquer la solution ;
- d’ajouter une correction ;
- d’ajouter une grille formateur ;
- d’indiquer ce qui peut être distribué aux apprenants ;
- de protéger la valeur de preuve.

Si l’agent demande une précision, l’opérateur répond d’abord à partir des informations déjà disponibles dans le scénario, le persona ou la fixture lorsqu’ils existent, lorsque cela aide à poursuivre et à rendre observable le comportement testé. Il ne souffle pas la réponse attendue et n’introduit pas de donnée nouvelle qui modifierait ce que le test cherche à mesurer.

Lorsque aucune information pertinente supplémentaire n’est disponible, l’opérateur peut utiliser la réponse neutre suivante :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Toute intervention supplémentaire doit être conservée dans le verbatim.

L’opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d’invalider l’objectif du test sans introduire artificiellement de nouveaux éléments.
