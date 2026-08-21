# CLAUDE.md — `validation/v2/`

Ce dossier est l'**archive pérenne de la campagne V2 terminée**.

Il ne décrit pas le candidat V3 courant.

## Statut

La campagne V2 est terminée et a conduit à la publication de V2 dans `dist/stable/`.

Les artefacts de ce dossier comprennent notamment :

- plan expérimental ;
- paramètres opérateur ;
- paquet aveugle ;
- scorings S1/S2 ;
- adjudication ;
- désaveuglement ;
- R3 ;
- métriques tokens ;
- rapport final ;
- fiche utilité/coût ;
- manifests et archives.

## Règle de conservation

Traiter ces artefacts comme historiques et auditables.

Ne pas :

- rescoring silencieusement les résultats ;
- remplacer un verdict gelé ;
- recalculer une campagne avec de nouvelles règles puis écraser l'ancienne sortie ;
- mettre à jour la promesse V2 pour la faire correspondre à V3 ;
- modifier une archive gelée sous le même nom.

Une correction documentaire nécessaire après coup doit être explicitement identifiable comme correction postérieure, sans réécriture des données historiques.

## R3 V2

Le scoring officiel des trois R3 V2 a été humain. Les avis IA étaient consultatifs.

Ne pas remplacer cette décision méthodologique par un nouveau scoring IA dans la campagne V2 historique.

## Tokens V2

Les métriques tokens sont une mesure secondaire d'efficience. Le ratio brut observé ne doit pas être présenté comme un ratio de prix sans pondération adaptée au cache et à la tarification réelle.
