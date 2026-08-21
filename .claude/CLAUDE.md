# CLAUDE.md — règles de travail du dépôt

## Projet

`tuteur-ingenierie-pedagogique` est un skill destiné au tutorat d'adultes et à l'assistance à l'ingénierie pédagogique.

Le projet cherche surtout à rendre plus fiables les décisions de l'agent autour :

- du point de départ réel de l'apprenant ;
- des notions, paliers et preuves ;
- de la valeur diagnostique des activités évaluées ;
- de l'alignement objectif → tâche → production → critères → preuve → conclusion ;
- des formats et gabarits pédagogiques.

Ne pas présenter le skill comme un remplacement du jugement du formateur ni comme une méthode pédagogique universelle.

## Langue et style du dépôt

- Les documents sont principalement en français : conserver le français sauf nécessité technique.
- Conserver le vocabulaire du projet et les accents.
- Préférer des formulations explicites, opérationnelles et vérifiables.
- Ne pas transformer une préférence pédagogique en règle normative sans source dans le projet.

## État des versions

Toujours lire les fichiers et l'état Git courant avant de supposer une version.

Dans l'état actuel du dépôt :

```text
dist/stable/
→ distributions publiques validées
→ V2 est la version publique recommandée
→ V1 est conservée pour historique

en_cours/
→ candidat V3
→ non public
→ promesse V3 encore à déterminer
```

`en_cours/VERSION` fait foi pour le numéro du candidat en développement.

`en_cours/promesse.md` fait foi pour la promesse du candidat courant. Tant qu'elle indique « À déterminer », ne pas extrapoler silencieusement la promesse V2 vers V3.

Le dépôt actuel ne contient pas de dossier racine `stable/`. Certains documents historiques peuvent décrire un flux incluant ce niveau : ne pas créer ni supposer ce dossier sans décision explicite.

## Carte du dépôt

```text
en_cours/
→ runtime candidat en développement

dist/stable/
→ distributions publiques validées
→ zone de publication, pas zone de développement

validation/
→ scénarios, personas, procédures, instrumentation et campagnes

validation/non_regression/
→ scénarios NOY autoritatifs actuellement présents

validation/collector-kit/
→ instrumentation générique de collecte
→ le collector collecte ; il ne score pas

validation/v2/
→ archive pérenne de la campagne V2 terminée

docs/
→ documentation de procédure et d'historique

dossier-pedagogique/
→ références de fond sur l'origine et la justification pédagogique
```

## Sources de vérité

Avant de modifier un comportement, identifier le document autoritatif correspondant.

- Runtime candidat : `en_cours/SKILL.md` et `en_cours/references/`.
- Version du candidat : `en_cours/VERSION`.
- Promesse du candidat : `en_cours/promesse.md`.
- Scénarios NOY : `validation/non_regression/`.
- Campagne V2 historique : `validation/v2/`.
- Distribution publique : `dist/stable/`.

Ne pas créer une deuxième copie éditable d'un document autoritatif si un pointeur suffit.

## Principe de travail

Avant une modification significative :

1. lire le fichier concerné et ses références directes ;
2. identifier si le changement touche le runtime, un test, une archive historique ou une distribution ;
3. vérifier les effets de bord sur la promesse et la non-régression ;
4. modifier le minimum nécessaire ;
5. exécuter les contrôles/tests pertinents ;
6. présenter clairement ce qui a changé et ce qui reste non démontré.

Ne pas modifier le candidat uniquement pour faire passer un test sans vérifier que la modification reste cohérente avec la promesse fonctionnelle.

## Validation expérimentale

Une faiblesse pédagogique n'est pas automatiquement une invalidité technique.

Pour les campagnes comparatives :

- A = avec skill ;
- B′ = sans skill ;
- le stimulus doit rester identique entre conditions lorsque le protocole le prévoit ;
- ne pas inventer d'information pendant un run ;
- ne pas souffler l'oracle à l'agent testé ;
- respecter les verdicts autorisés par le protocole ;
- distinguer collecte, scoring, adjudication, désaveuglement et répétitions conditionnelles.

Les résultats historiques ne doivent pas être réécrits rétroactivement pour rendre une campagne plus propre.

## Git, gels et publication

- Ne pas réécrire un tag public existant sans demande explicite.
- Ne pas modifier l'historique Git publié par défaut.
- Ne pas promouvoir `en_cours/` vers `dist/stable/` sans décision explicite de validation/promotion.
- Ne pas modifier une distribution stable comme moyen de développement ; corriger d'abord la source appropriée.
- Avant commit : vérifier `git status`, le diff et les fichiers non suivis.
- Avant push : vérifier que la branche distante n'a pas divergé.
- Un tag de validation et un tag de release peuvent viser des commits différents : conserver cette distinction.

## Archives et traçabilité

Les campagnes terminées servent d'éléments d'audit.

- Préserver les SHA-256, manifests, paquets aveugles, verdicts et décisions gelées.
- Ne pas régénérer silencieusement une archive historique sous le même nom avec un contenu différent.
- Toute correction documentaire postérieure à un gel doit être identifiable comme telle.

## Sécurité des opérations de fichiers

Pour une copie ou promotion importante :

- comparer la source et la destination ;
- éviter les écrasements ambigus ;
- contrôler l'intégrité des ZIP ;
- vérifier les différences après copie ;
- conserver les versions publiques antérieures lorsqu'elles font partie de la traçabilité.
