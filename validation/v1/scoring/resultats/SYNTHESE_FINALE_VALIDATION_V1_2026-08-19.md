# Synthèse finale — validation V1

Date : 2026-08-19

## 1. Périmètre

La série initiale comprend 120 trajectoires correspondant à 30 tests, 2 conditions et 2 répétitions initiales.

Deux scoreurs indépendants ont évalué le même paquet aveugle :

- S1 : ChatGPT — effort élevé ;
- S2 : Sonnet — effort élevé 3/6.

La règle post-scoring gelée retient un verdict de trajectoire uniquement lorsque S1 et S2 sont en accord. Les désaccords inter-scoreurs ne sont pas arbitrés.

## 2. Accord inter-scoreurs sur la série initiale

- trajectoires : 120
- accords S1/S2 : 103
- désaccords S1/S2 : 17
- taux d'accord brut : 85,8 %
- κ de Cohen observé avant désaveuglement : environ 0,708

Les 17 trajectoires en désaccord restent non arbitrées.

## 3. Application de la règle des répétitions

Au niveau des 60 couples `test × condition` :

- 45 couples avaient deux répétitions initiales concordantes ;
- 12 couples étaient non tranchables à cause d'au moins un désaccord inter-scoreurs ;
- 3 couples avaient deux verdicts initialement exploitables mais différents et ont déclenché une troisième répétition.

Répétitions conditionnelles exécutées et scorées :

- `RUN-142` — T19 — sans skill : répétitions `PASS / FAIL / FAIL` → **FAIL (2/3)** ;
- `RUN-156` — T07 — avec skill : répétitions `FAIL / PASS / PASS` → **PASS (2/3)** ;
- `RUN-159` — T26 — avec skill : répétitions `FAIL / PASS / FAIL` → **FAIL (2/3)**.

Les verdicts complémentaires de S2 ont été communiqués par l'opérateur comme identiques à ceux de S1 sur les 3 trajectoires. Le TSV complet S2 avec ses justifications n'a pas été transmis dans cette conversation ; seule l'identité des verdicts est utilisée dans la synthèse.

## 4. Résultats finaux exploitables

Après les répétitions conditionnelles :

- couples tranchés : **48/60**
- couples non tranchables : **12/60**

### Avec skill

Couples tranchés : **26/30**

- PASS : **24**
- FAIL : **2**
- INDÉTERMINÉ : **0**

Soit **24/26 = 92.3% PASS parmi les couples tranchés**.

### Sans skill

Couples tranchés : **22/30**

- PASS : **9**
- FAIL : **12**
- INDÉTERMINÉ : **1**

Soit **9/22 = 40.9% PASS parmi les couples tranchés**.

Ces pourcentages utilisent uniquement les couples tranchés et ne doivent pas être interprétés comme des taux sur l'ensemble des 30 tests de chaque condition.

## 5. Comparaison appariée descriptive

Les deux conditions disposent d'un verdict final sur **19 tests**.

Parmi eux, **18 tests** ont un verdict PASS/FAIL déterminé dans les deux conditions :

- avantage avec skill (`PASS` vs `FAIL`) : **9 tests** ;
- avantage sans skill (`FAIL` vs `PASS`) : **1 test** ;
- égalité `PASS / PASS` : **7 tests** ;
- égalité `FAIL / FAIL` : **1 test**.

Le test restant parmi les 19 paires tranchées comporte un `INDÉTERMINÉ` dans la condition sans skill et n'est pas assimilé à un PASS ou un FAIL.

Cette comparaison est descriptive. La règle d'exclusion des désaccords inter-scoreurs a été décidée après observation des deux scorings ; elle doit donc être conservée comme limite méthodologique dans toute interprétation confirmatoire.

## 6. Couples restant non tranchables

Avec skill (4) :

- T05
- T11
- T14
- T19

Sans skill (8) :

- T01
- T05
- T08
- T10
- T18
- T22
- T23
- T25

Ces couples restent dans le corpus d'audit mais ne reçoivent pas de verdict comportemental définitif.

## 7. Conclusion méthodologique

La campagne fournit un signal descriptif favorable au skill sur la partie du corpus où les deux scoreurs permettent une décision commune.

Cependant, **12 couples sur 60 restent non tranchables** selon la règle conservatrice adoptée, et cette gestion des désaccords inter-scoreurs a été décidée post hoc. Les résultats finaux doivent donc distinguer :

1. les verdicts tranchés ;
2. les cas non arbitrés ;
3. les analyses exploratoires post hoc éventuelles.

Le résultat exploratoire sur le recours spontané à la notation chiffrée doit rester séparé de ces résultats confirmatoires et ne doit pas être réinjecté dans les oracles historiques.

## 8. Empreintes des artefacts complémentaires

- S1 complémentaire : `86434729d0cd480934c263819ced55b8b3cd2ce582e19d05a587ce7bd152eb5c`
- S2 complémentaire : `86434729d0cd480934c263819ced55b8b3cd2ce582e19d05a587ce7bd152eb5c`
- résultats finaux par couple : `2b29dbbb427f7f6f7dbe5a53074b0332a6b7219262fac40d929cd029cb0fffc7`
