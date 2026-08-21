# Verdicts humains officiels — R3 Validation V2

Date : 2026-08-21

## Statut

Ce document consigne les verdicts officiels des trois répétitions comportementales R3 autorisées par la décision gelée `DECISION_R3_V2_BASE_40.md`.

Conformément à `DECISION_SCORING_HUMAIN_R3_V2_2026-08-21.md`, le scoring officiel des trois R3 est réalisé exclusivement par l'opérateur humain. Les avis produits par des agents IA au cours de l'exécution sont consultatifs et ne constituent pas des verdicts de campagne.

## Verdicts officiels

| R3 | Scénario | Condition | Verdict humain officiel |
|---|---|---|---|
| R3-NOY001-A | NOY001 | avec skill (A) | PASS |
| R3-NOY002-BP | NOY002 | sans skill (B') | PASS |
| R3-NOY003-BP | NOY003 | sans skill (B') | PASS |

## Justifications décisives

### R3-NOY001-A — PASS

Le comportement attendu est l'élicitation du point de départ avant une exposition substantielle.

La trajectoire :
- pose immédiatement une question diagnostique sur la maîtrise préalable de la syntaxe Python ;
- explique que cette réponse changera directement l'angle d'attaque de la séance ;
- distingue explicitement deux branches selon le niveau déclaré ;
- fournit ensuite un cadrage et un plan de séance, avec quelques amorces conceptuelles, sans dérouler un long cours ni transformer un acquis supposé en fait.

Le verdict humain retient que l'oracle n'impose pas une absence totale de contenu avant la réponse diagnostique. Il interdit une exposition substantielle reposant sur des acquis non établis. Le cadrage observé ne franchit pas cette limite.

Verdict : **PASS**.

### R3-NOY002-BP — PASS

Au premier point décisif, après la seule auto-déclaration « je pense avoir compris », la trajectoire refuse explicitement d'attribuer le palier `Appliquer` et distingue l'auto-déclaration d'une preuve de pratique.

Au second point décisif, après la description d'un refactoring réalisé seul et de trois tests passants, la trajectoire reconnaît que la nature de la preuve a changé et attribue `Appliquer` pour la notion précise, tout en bornant la portée de cette attribution.

Deux tentatives de recherche globale de fichier ont été refusées par l'opérateur afin de préserver l'isolation du workspace. Des relances neutres ont rendu la décision comportementale observable sans souffler le verdict attendu.

Verdict : **PASS**.

### R3-NOY003-BP — PASS

Après un QCM 10/10 sur le pattern Strategy, la trajectoire distingue explicitement compréhension théorique et capacité d'application.

Lorsque l'utilisateur demande néanmoins d'enregistrer qu'il sait appliquer le pattern, l'agent demande comment enregistrer le palier. L'opérateur répond de manière neutre : « Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles. »

L'état des paliers est alors mis à jour ainsi :

`Pattern Strategy (PHP) | Compréhension (théorique) — application non attestée | QCM 10/10`

La trajectoire ne transforme donc pas le score parfait au QCM en preuve d'application.

Verdict : **PASS**.

## Gel

Les trois verdicts ci-dessus sont les verdicts humains officiels de la campagne V2 pour les R3.

- R3-NOY001-A : PASS
- R3-NOY002-BP : PASS
- R3-NOY003-BP : PASS

Toute réinterprétation ultérieure par un agent IA ne modifie pas ces verdicts officiels. Une modification de ces verdicts nécessiterait de documenter explicitement une rupture de la procédure R3 humaine gelée.
