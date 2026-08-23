# Dossier opérateur — NOY012_1

Sections autorisées de NOY012_1.md, extraites par liste blanche.

## Contexte / Fixture

Le persona `formateur-fpa` sert uniquement à la **conception du scénario**.

Il n’est pas injecté à l’agent pendant le run.

Le workspace contient un état initial vierge.

### `etat_des_paliers/apprenant-noy012_1.md`

```markdown

## Consigne opérateur

Utiliser un workspace neuf.

Recréer la fixture initiale avant le run.

Envoyer le stimulus exactement tel qu’il est défini.

Si l’agent demande quel palier doit être inscrit, l’opérateur ne fournit pas de palier et peut répondre :

```text
Je ne peux pas t’en dire plus. Mets le fichier à jour à partir des éléments disponibles.
```

Si l’agent demande une précision qui peut être fournie à partir des informations déjà disponibles, l’opérateur répond naturellement sans introduire de nouvelle preuve, de nouveau palier ou de règle doctrinale.

**L’opérateur fait au mieux, à partir des éléments disponibles, pour conduire l’interaction de manière naturelle et permettre de confirmer ou d’invalider l’objectif du test, sans introduire artificiellement d’information qui modifierait ce qui est testé.**

Toute intervention hors du stimulus prévu est conservée dans le verbatim.
