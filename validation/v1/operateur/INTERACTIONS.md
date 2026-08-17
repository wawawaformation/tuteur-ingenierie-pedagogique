# INTERACTIONS — règle opérateur V1

Ce document définit comment l’opérateur intervient pendant une trajectoire Claude Code.

Il s’applique aux tests historiques T01 à T30 sans modifier leurs critères.

## Principe général

L’opérateur n’est pas un apprenant improvisant librement.

Il interprète chaque interaction et répond uniquement lorsque cela est nécessaire à la poursuite fidèle du scénario.

Il ne doit :

- ni enrichir le scénario ;
- ni aider Claude à réussir le test ;
- ni provoquer artificiellement un échec ;
- ni scorer le comportement pendant le run.

## 1. Interaction technique

Une interaction liée au fonctionnement de Claude Code n’est pas une réponse pédagogique.

Exemples :

- demande de confiance dans le dossier ;
- permission d’accès à un fichier ;
- permission liée au workspace ;
- confirmation technique de l’interface.

Une demande de confiance dans le workspace du run peut être traitée comme une interaction technique.

Une permission qui sortirait du périmètre prévu du workspace ou compromettrait l’isolation expérimentale ne doit pas être utilisée pour fournir indirectement des informations pédagogiques.

Toute interaction technique notable est conservée dans la trajectoire et pourra être prise en compte lors du contrôle technique.

## 2. Question pédagogique explicitement couverte par le test

Si la fiche historique gelée prévoit explicitement une information ou une réponse à fournir, l’opérateur fournit exactement cette information.

Il n’ajoute rien d’autre.

La fiche T concernée reste l’autorité.

## 3. Question demandant une information absente du scénario

Si Claude demande une information pédagogique qui :

- n’est pas fournie dans le prompt ;
- n’est pas prévue par la fiche T gelée ;
- et est nécessaire pour que Claude décide comment poursuivre,

l’opérateur répond exactement :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

Cette phrase ne constitue pas un nouvel élément pédagogique du scénario.

Elle signifie uniquement qu’aucune donnée supplémentaire ne sera fournie.

## 4. Proposition facultative après une réponse déjà complète

Si Claude a produit une réponse complète puis termine par une proposition du type :

- « Voulez-vous que je continue ? »
- « Souhaitez-vous un exemple ? »
- « Veux-tu que je prépare la suite ? »

et qu’aucune réponse supplémentaire n’est exigée par la fiche historique, l’opérateur ne joue pas un nouveau tour d’apprenant.

La trajectoire est terminée.

Quitter Claude Code avec :

```text
exit
```

## 5. Pas de `Esc` systématique

Une `AskUserQuestion` n’entraîne pas automatiquement `Esc`.

L’opérateur détermine d’abord si la demande est :

1. technique ;
2. explicitement couverte par le test ;
3. une demande d’information pédagogique absente ;
4. une simple proposition facultative après réponse complète.

La réponse dépend de cette catégorie.

## 6. Neutralité

Pendant le run, l’opérateur ne doit jamais choisir une intervention en fonction de l’impression que :

- le skill réussit ;
- le skill échoue ;
- la condition sans skill réussit ;
- la condition sans skill échoue.

Le verdict comportemental appartient à la phase de scoring ultérieure.

## 7. Fin de trajectoire

Lorsque la réponse attendue par le scénario est terminée et qu’aucune interaction nécessaire n’est en attente :

```text
exit
```

Puis exécuter le BLOC 2.

## Phrase neutre prête à copier-coller

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
