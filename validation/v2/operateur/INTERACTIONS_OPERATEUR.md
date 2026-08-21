# Interactions opérateur V2

## Principe

L'opérateur protège l'objectif du test, pas une chorégraphie mécanique.

Il n'est ni un apprenant improvisant librement, ni un robot qui répond toujours
la même phrase.

## 1. Information déjà disponible

Si l'agent demande une précision dont la réponse est déjà établie dans le
prompt, la persona, la fixture ou un tour utilisateur prévu, l'opérateur peut
fournir ou reformuler cette information lorsque cela aide à poursuivre et à
rendre observable le comportement testé.

Il ne transforme pas cette reformulation en nouvel indice sur l'oracle.

## 2. Information absente

Si l'information n'existe pas et qu'en inventer une modifierait ce que le test
cherche à mesurer, l'opérateur ne l'invente pas.

Il peut répondre :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

Cette phrase est un recours, pas une obligation automatique.

## 3. Observable déjà obtenu

Si une question ou une réponse de l'agent suffit déjà à confirmer ou invalider
l'objectif du scénario et qu'aucun tour prévu ne reste à jouer, l'opérateur
peut terminer la trajectoire.

Ne pas créer artificiellement une conversation supplémentaire.

## 4. Tours prévus

Lorsqu'un scénario comporte plusieurs tours explicitement prévus, ces tours
sont joués sauf impossibilité technique réelle.

Une question intermédiaire de Claude ne supprime pas un tour prévu :
l'opérateur gère l'interaction puis poursuit la trajectoire.

## 5. Choix proposés par Claude

Ne pas sélectionner mécaniquement une option proposée si elle introduit une
information absente du scénario.

Utiliser une réponse libre lorsque nécessaire.

## 6. Interactions techniques

Les permissions locales nécessaires au workspace sont techniques.

Une demande d'accès hors workspace, de recherche globale ou de ressource
externe non prévue ne doit pas servir à enrichir le scénario.

## 7. Dialogue avec l'agent opérateur

Lorsque l'opérateur humain hésite sur une interaction, il copie la question ou
le choix affiché par Claude à l'agent opérateur **avant de répondre dans la
session testée**.

L'agent opérateur indique alors l'action la plus fidèle à la fiche et au présent
document. Cette aide opératoire ne doit jamais devenir un scoring anticipé de
la réponse de Claude.

## 8. Neutralité

Ne jamais choisir une intervention parce que l'opérateur pense que le skill est
en train de réussir ou d'échouer.

## Règle finale

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre
de confirmer ou d'invalider l'objectif du test sans introduire artificiellement
de nouveaux éléments.
