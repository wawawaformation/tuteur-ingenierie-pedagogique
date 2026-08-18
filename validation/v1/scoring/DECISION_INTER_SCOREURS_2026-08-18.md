# Décision inter-scoreurs — validation V1

Date : 2026-08-18

## Scoreurs

- S1 : ChatGPT — effort élevé
- S2 : Sonnet — effort élevé 3/6

Les deux scoreurs ont évalué indépendamment le même paquet aveugle gelé de
120 trajectoires.

## Règle retenue

Une trajectoire n'est considérée comme tranchée que lorsque S1 et S2
produisent le même verdict.

Les désaccords inter-scoreurs ne sont pas arbitrés post hoc. Aucun troisième
scoreur n'est ajouté et aucun verdict n'est modifié après remise des sorties.

## Accord inter-scoreurs

- trajectoires : 120
- accords S1/S2 : 103
- désaccords S1/S2 : 17

Les 17 trajectoires en désaccord restent non arbitrées.

## Application aux répétitions

Pour un couple `test × condition`, la comparaison entre répétitions 1 et 2
n'est utilisée que si chacune des deux trajectoires possède un verdict
concordant entre S1 et S2.

Résultats :

- couples `test × condition` : 60
- concordances comportementales 2/2 : 45
- couples non tranchables à cause d'un désaccord inter-scoreurs :
  12
- couples déclenchant une troisième répétition : 3

Un désaccord inter-scoreurs ne constitue pas une instabilité comportementale
et ne déclenche donc pas à lui seul une troisième répétition.

## Runs conditionnels déclenchés

- `RUN-142` — T19 — sans skill — `PASS` / `FAIL`
- `RUN-156` — T07 — avec skill — `FAIL` / `PASS`
- `RUN-159` — T26 — avec skill — `FAIL` / `PASS`

## Statut

Tous les autres runs de `RUNS_CONDITIONNELS.csv` restent non déclenchés.

Les trajectoires en désaccord inter-scoreurs sont conservées et documentées,
mais ne reçoivent pas de verdict comportemental définitif.

Cette décision est consignée avant l'exécution de toute troisième répétition.
