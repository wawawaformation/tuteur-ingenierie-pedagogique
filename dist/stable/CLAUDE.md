# CLAUDE.md — `dist/stable/`

Ce dossier est la **zone de distribution publique validée**.

Il contient actuellement :

- V1, conservée pour historique ;
- V2, version publique recommandée ;
- les archives ZIP correspondantes.

## Règle principale

> Ne pas développer directement dans `dist/stable/`.

Les changements fonctionnels doivent être réalisés dans le candidat approprié (`en_cours/`), validés, puis promus explicitement.

## Versions publiées

Une version déjà publiée et taguée doit être considérée comme un artefact historique.

Ne pas :

- modifier silencieusement son runtime ;
- remplacer son ZIP par un contenu différent sous le même nom ;
- supprimer une version antérieure conservée pour traçabilité ;
- réécrire un tag public pour faire correspondre une archive modifiée.

Une correction purement documentaire du dépôt peut être committée après la release si nécessaire, sans réécrire le tag historique.

## Promotion d'une nouvelle version

Lors d'une promotion explicite :

1. partir du candidat validé ;
2. créer un nouveau dossier versionné à côté des versions existantes ;
3. vérifier que la copie correspond à la source validée ;
4. créer l'archive ZIP ;
5. contrôler l'intégrité du ZIP ;
6. vérifier `git status` et le diff ;
7. committer la promotion ;
8. poser le tag de release seulement sur l'état réellement publié ;
9. vérifier le distant avant push.

Ne pas confondre le tag qui gèle une campagne de validation avec le tag de version publique.
