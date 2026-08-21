# CLAUDE.md — `validation/non_regression/`

Ce dossier contient les scénarios NOY autoritatifs actuellement utilisés comme batterie de non-régression.

## Ne pas modifier légèrement un oracle historique

Un scénario est un artefact expérimental. Modifier son prompt, son objectif, ses observables ou son oracle peut changer ce qu'il mesure.

Avant toute modification :

1. identifier les campagnes qui ont utilisé ce scénario ;
2. déterminer si la modification est une correction de forme ou un changement sémantique ;
3. ne jamais réinterpréter rétroactivement les verdicts d'une campagne terminée ;
4. si le comportement testé change, préférer une nouvelle version ou un nouveau scénario clairement traçable.

`validation/v2/tests/README.md` référence `NOY001` à `NOY012` ici pour éviter une seconde copie éditable.

## Structure attendue d'une fiche

Préserver autant que possible les éléments utiles à un test reproductible :

- statut ;
- fonction/famille ;
- persona ;
- invariant ou comportement protégé ;
- objectif ;
- stimulus exact ;
- consigne opérateur ;
- observables obligatoires ;
- oracle PASS / FAIL / INDÉTERMINÉ ;
- éventuelle provenance/dry-run clairement séparée du résultat officiel.

## Consigne opérateur

Pour les fiches qui comportent une section `Consigne opérateur`, laisser une marge de jugement permettant de confirmer ou d'invalider l'objectif du test à partir des informations disponibles, sans introduire artificiellement de nouveaux éléments.

## Cas limites

Un oracle doit décrire la frontière réellement recherchée.

Exemple important issu de NOY001 :

```text
« avant exposition substantielle »
≠
« aucune phrase pédagogique avant la réponse »
```

Ne pas durcir un oracle au-delà de son texte lors d'une révision.
