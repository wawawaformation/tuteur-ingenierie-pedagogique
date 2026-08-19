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

## 6. Recours spontané à la notation chiffrée

Un second résultat apparaît dans les trajectoires portant sur la production d'activités évaluées : **la condition sans skill recourt spontanément et de manière répétée à des systèmes de notation chiffrés**.

Ce comportement prend notamment la forme de :

- barèmes sur 10, 20 ou 100 ;
- points attribués par critère ;
- bonus ;
- seuils numériques de réussite tels que `9/12`, `16/20` ou `60/100`.

Le phénomène est observé dans **12 trajectoires sans skill**, réparties sur **6 scénarios différents**. Il apparaît dans **les deux répétitions de chacun de ces six scénarios**, ce qui montre qu'il ne s'agit pas d'un cas isolé.

Les barèmes produits ne semblent pas correspondre à un référentiel numérique stable. Pour un même scénario, le modèle peut proposer un barème sur 20 dans une répétition et sur 100 dans l'autre ; les seuils et les pondérations peuvent également varier. Le motif observé est donc compatible avec une heuristique spontanée de type :

> `activité évaluée → note chiffrée`

Dans les trajectoires correspondantes avec skill, ce même recours systématique à la notation numérique n'a pas été observé. Les réponses sont davantage structurées autour :

- de critères observables ;
- des productions attendues de l'apprenant ;
- des preuves réellement recueillies ;
- de la portée de ce que ces preuves permettent d'attester.

Ce résultat complète le résultat principal de scoring : au-delà du taux de réussite aux oracles historiques, le skill semble également modifier **la manière dont le modèle opérationnalise l'évaluation**, en privilégiant la relation entre critères, preuves et attestation plutôt qu'une conversion spontanée de l'activité en score numérique.

## 7. Couples restant non tranchables

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

## 8. Conclusion

La campagne V1 met en évidence deux résultats convergents.

Premièrement, sur la partie du corpus où les deux scoreurs permettent une décision commune, le skill obtient un résultat descriptif nettement supérieur à la condition sans skill :

- avec skill : **24 PASS / 2 FAIL** sur 26 couples tranchés ;
- sans skill : **9 PASS / 12 FAIL / 1 INDÉTERMINÉ** sur 22 couples tranchés.

Sur les tests disposant d'un verdict PASS/FAIL dans les deux conditions, le contraste apparié est favorable au skill dans **9 cas**, favorable à la condition sans skill dans **1 cas**, avec **7 égalités PASS/PASS** et **1 égalité FAIL/FAIL**.

Deuxièmement, les trajectoires montrent un contraste récurrent dans la manière de concevoir l'évaluation : sans skill, un ensemble de six scénarios produit dans les deux répétitions des systèmes de notation chiffrés variables ; avec skill, les trajectoires correspondantes structurent davantage l'évaluation autour des critères observables, des productions et des preuves.

Ces deux résultats portent sur des dimensions différentes mais complémentaires :

- **réussite comportementale selon les oracles historiques** ;
- **forme spontanée prise par l'évaluation produite par le modèle**.

La principale limite du résultat de scoring reste l'existence de **12 couples sur 60 non tranchables** selon la règle conservatrice d'accord inter-scoreurs. Ces cas sont conservés dans le corpus d'audit et ne sont pas convertis artificiellement en PASS ou FAIL.

## 9. Note méthodologique sur le résultat relatif à la notation chiffrée

Le résultat concernant le recours spontané à la notation chiffrée repose sur **les mêmes trajectoires expérimentales gelées** que le reste de l'analyse et sur des comportements directement observables dans ces trajectoires.

Il n'avait toutefois **pas été défini à l'avance comme hypothèse, variable ou oracle de la campagne**. Le motif a été identifié lors de la relecture postérieure des données. Cette différence de pré-spécification doit être signalée, mais elle ne change pas la provenance empirique du résultat : il est issu du même corpus expérimental gelé.

En conséquence :

- ce résultat est présenté dans la synthèse générale de la campagne au même titre que les autres constats empiriques ;
- son identification post hoc est explicitement documentée ;
- il ne modifie rétroactivement aucun oracle T01 à T30 ;
- il n'est pas utilisé pour rescoring des trajectoires ni pour déclencher de nouvelles répétitions ;
- il peut devenir une hypothèse pré-spécifiée dans une campagne ultérieure.

## 10. Empreintes des artefacts complémentaires

- S1 complémentaire : `86434729d0cd480934c263819ced55b8b3cd2ce582e19d05a587ce7bd152eb5c`
- S2 complémentaire : `86434729d0cd480934c263819ced55b8b3cd2ce582e19d05a587ce7bd152eb5c`
- résultats finaux par couple : `2b29dbbb427f7f6f7dbe5a53074b0332a6b7219262fac40d929cd029cb0fffc7`
