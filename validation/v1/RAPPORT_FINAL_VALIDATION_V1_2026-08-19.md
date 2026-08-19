# Rapport final — validation expérimentale V1

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-08-19  
**Candidat :** V1

---

## Résumé exécutif

La campagne V1 met en évidence une **utilité réelle mais ciblée** du skill.

Sur les **18 tests directement comparables en PASS/FAIL dans les deux conditions** :

- **9 tests** sont favorables au skill ;
- **8 tests** ne montrent pas de gain par rapport au modèle sans skill ;
- **1 test** est défavorable au skill.

Les **12 autres tests** restent hors de cette comparaison stricte parce qu'au moins une condition n'a pas pu recevoir un verdict PASS/FAIL définitif.

Au niveau des 60 couples `test × condition`, après scoring et répétitions conditionnelles :

- **48/60 couples** disposent d'un verdict final exploitable ;
- **12/60 couples** restent non tranchables ;
- avec skill : **24 PASS / 2 FAIL** sur 26 couples tranchés ;
- sans skill : **9 PASS / 12 FAIL / 1 INDÉTERMINÉ** sur 22 couples tranchés.

Le contraste principal est fonctionnel : le skill est surtout utile lorsqu'il agit comme **garde-fou d'ingénierie pédagogique**. Il apporte une discipline plus fiable sur les prérequis, les preuves, le budget de nouveauté, l'alignement pédagogique et le choix des formats.

Un second résultat ressort des trajectoires : **sans skill, le modèle tend spontanément à transformer une activité évaluée en système de notation chiffré ; avec skill, il raisonne davantage en critères, productions, preuves et attestation.**

---

# 1. Objet de la validation

La campagne vise à vérifier si le candidat V1 apporte une différence comportementale observable par rapport au même modèle utilisé sans skill.

Le corpus historique comprend **30 tests T01 à T30**.

La série initiale a été exécutée dans deux conditions :

- avec skill ;
- sans skill.

Chaque couple `test × condition` comporte deux répétitions initiales.

Le plan initial représente donc :

```text
30 tests
× 2 conditions
× 2 répétitions
= 120 trajectoires
```

Des troisièmes répétitions étaient pré-déclarées et ne pouvaient être déclenchées qu'en cas de désaccord entre les deux répétitions comportementales initiales d'un même couple.

---

# 2. Scoring et traitement des désaccords

Deux scoreurs indépendants ont évalué le même paquet aveugle :

- **S1 : ChatGPT — effort élevé** ;
- **S2 : Sonnet — effort élevé 3/6**.

Sur les 120 trajectoires initiales :

- **103 accords S1/S2** ;
- **17 désaccords S1/S2** ;
- accord brut : **85,8 %** ;
- κ de Cohen : **environ 0,708**.

Une règle conservatrice a ensuite été retenue :

> **Une trajectoire n'est considérée comme tranchée que lorsque S1 et S2 produisent le même verdict.**

Les 17 désaccords ne sont donc ni moyennés, ni arbitrés artificiellement, ni convertis en verdicts définitifs.

Au niveau des 60 couples `test × condition` :

- **45 couples** avaient deux répétitions initiales concordantes ;
- **12 couples** étaient non tranchables à cause d'au moins un désaccord inter-scoreurs ;
- **3 couples** avaient deux répétitions exploitables mais divergentes et ont déclenché une troisième répétition.

Les trois répétitions conditionnelles ont donné :

| Run | Test | Condition | Répétitions | Verdict final |
|---|---|---|---|---|
| `RUN-142` | T19 | sans skill | PASS / FAIL / FAIL | **FAIL (2/3)** |
| `RUN-156` | T07 | avec skill | FAIL / PASS / PASS | **PASS (2/3)** |
| `RUN-159` | T26 | avec skill | FAIL / PASS / FAIL | **FAIL (2/3)** |

Les deux scoreurs ont attribué les mêmes verdicts aux trois trajectoires complémentaires.

## 2.1 Enseignement méthodologique : préciser davantage les oracles

Les **17 désaccords inter-scoreurs** constituent aussi un résultat sur la qualité du dispositif de test.

Plusieurs désaccords ne sont pas isolés : ils se répètent sur les **deux répétitions d'un même couple `test × condition`**. C'est notamment le cas pour plusieurs tests où S1 et S2 appliquent de manière différente la même fiche historique.

Ce motif suggère que certains oracles historiques laissent encore trop de latitude d'interprétation au scoreur. Les principales zones d'ambiguïté concernent notamment :

- ce qui doit être compté comme une **notion nouvelle** ;
- le moment où une **question diagnostique** suffit à satisfaire l'oracle ;
- le poids d'une **erreur locale** dans le verdict global ;
- la distinction entre conformité de la **structure générale** et satisfaction de chaque contrainte précise ;
- le niveau d'observation nécessaire pour déclarer un comportement `PASS`, `FAIL` ou `INDÉTERMINÉ`.

Lorsque deux scoreurs indépendants produisent des lectures différentes de façon répétée sur le même test, le problème ne relève plus seulement du bruit de scoring : il peut révéler une **ambiguïté de spécification du test lui-même**.

La leçon pour les futures campagnes est donc :

> **Les tests doivent préciser davantage les observables obligatoires, les conditions exactes de PASS et de FAIL, la granularité du jugement et le traitement des cas limites.**

Cette conclusion ne conduit pas à réécrire rétroactivement T01 à T30 : leurs oracles restent l'autorité historique de la campagne V1.

En revanche, les désaccords observés doivent être utilisés comme matière de RETEX pour améliorer les futures fiches de test et réduire la part d'interprétation laissée aux scoreurs.

Autrement dit, la campagne V1 a évalué deux choses à la fois :

1. la contribution du skill ;
2. la capacité des tests eux-mêmes à produire des verdicts reproductibles.

---

# 3. Résultat global

Après application de la règle d'accord inter-scoreurs et des troisièmes répétitions :

## Avec skill

**26/30 couples tranchés**

- PASS : **24**
- FAIL : **2**
- INDÉTERMINÉ : **0**

Soit :

> **24/26 = 92,3 % de PASS parmi les couples tranchés**

## Sans skill

**22/30 couples tranchés**

- PASS : **9**
- FAIL : **12**
- INDÉTERMINÉ : **1**

Soit :

> **9/22 = 40,9 % de PASS parmi les couples tranchés**

Ces pourcentages décrivent uniquement les couples effectivement tranchés. Ils ne doivent pas être transformés en taux sur l'ensemble des 30 tests de chaque condition.

---

# 4. Comparaison directe de l'utilité du skill

Les deux conditions disposent d'un verdict final PASS/FAIL directement comparable sur **18 tests**.

Le bilan est :

```text
9  tests : le skill fait mieux
8  tests : le skill n'apporte pas plus
1  test  : le skill fait moins bien
```

---

## 4.1 Là où le skill fait la différence

Ces tests aboutissent à :

> **avec skill = PASS / sans skill = FAIL**

| Test | Apport observé du skill |
|---|---|
| **T04 — Une activité évaluée est soumise aux contraintes** | Empêche de traiter une activité évaluée comme si les prérequis étaient déjà acquis et pousse à adapter l'activité ou à prévoir une étape préalable. |
| **T07 — Un quiz ne peut pas attester le palier 3** | Évite de transformer un bon score de quiz en preuve d'application et exige une production compatible avec le palier visé. |
| **T09 — Trois notions nouvelles : activité interdite telle quelle** | Détecte un budget de nouveauté dépassé et impose de refuser ou découper l'activité. |
| **T12 — Critère désaligné avec le palier** | Détecte l'incohérence entre objectif, tâche et niveau de preuve attendu. |
| **T13 — Activité versus Atelier** | Reconnaît qu'une demande dépasse le format d'une petite activité et applique un format pédagogique plus adapté. |
| **T15 — Synchrone versus asynchrone** | Tient compte de la modalité pédagogique et choisit la structure correspondante. |
| **T24 — Reproduction du bug d'origine** | Évite de considérer que plusieurs notions déjà rencontrées peuvent automatiquement être mobilisées ensemble dans une activité finale. |
| **T27 — Demande d'exercice très difficile** | Résiste à une difficulté artificielle lorsqu'elle introduit trop de notions non attestées. |
| **T29 — Atelier avec les huit sections** | Maintient précisément l'architecture attendue du gabarit Atelier. |

### Lecture commune

Ces neuf tests ont un point commun : ils exigent de **préserver une contrainte pédagogique explicite face à une réponse qui pourrait sembler plausible sans l'être pédagogiquement**.

Le skill apporte principalement :

- le contrôle des prérequis ;
- le raisonnement par preuve ;
- la limitation des nouveautés simultanées ;
- l'alignement objectif / tâche / preuve / conclusion ;
- la résistance aux demandes pédagogiquement inadéquates ;
- le choix et le respect de formats pédagogiques structurés.

> **Le gain principal du skill est une discipline d'ingénierie pédagogique que le modèle sans skill n'applique pas de manière suffisamment fiable.**

---

## 4.2 Là où le skill n'apporte pas plus

### PASS dans les deux conditions

| Test | Lecture |
|---|---|
| **T02 — Une démonstration peut introduire une notion nouvelle** | Le modèle sans skill sait déjà éviter une lecture excessivement rigide interdisant toute nouveauté dans une démonstration. |
| **T03 — Pair-programming guidé libre** | Les deux conditions savent accompagner une construction guidée sans la transformer automatiquement en preuve autonome d'application. |
| **T16 — Gestion professionnelle de l'erreur** | Le comportement diagnostique et professionnel face à une erreur est déjà bien géré sans skill. |
| **T17 — Ancrage concret** | Le modèle sait déjà introduire une notion par un cas concret. |
| **T20 — Redescente d'un palier** | Les deux conditions acceptent de réviser une attestation à la baisse. |
| **T21 — Ne pas inventer une persistance** | Le modèle sait déjà signaler l'absence d'un état persistant plutôt que l'inventer. |
| **T30 — Respect du périmètre demandé** | Le modèle sait déjà rester globalement dans le périmètre de production demandé. |

Sur ces dimensions, le skill ne dégrade pas le comportement, mais **aucun gain n'est démontré par rapport au modèle de base**.

### FAIL dans les deux conditions

**T28 — Demande de solution avant production**

Résultat :

> **avec skill = FAIL / sans skill = FAIL**

Le skill n'apporte pas ici la séparation attendue entre :

- le contenu réellement remis à l'apprenant ;
- le volet formateur ou interne contenant la solution et les critères.

T28 constitue donc un **point faible du candidat V1** plutôt qu'un avantage.

---

## 4.3 Là où le skill apporte moins

Un seul test directement comparable est défavorable au skill.

### T26 — Même compétence, vocabulaire différent

Résultat :

> **avec skill = FAIL / sans skill = PASS**

L'attendu était de distinguer une **nouvelle tâche** d'une **nouvelle notion**.

Avec le skill, le modèle a tendance à qualifier de nouveauté pédagogique une variation de tâche autour d'une compétence déjà attestée.

Ce résultat met en évidence un risque de :

> **sur-détection de nouveauté**

La règle destinée à limiter la surcharge peut donc devenir trop sensible et rigidifier inutilement la progression.

T26 est le principal cas où la V1 produit un comportement moins bon que le modèle sans skill.

---

# 5. Tests qui ne permettent pas de conclure sur l'apport du skill

Ces tests ne sont pas forcés dans les catégories « mieux / pareil / moins bien ».

## Verdict non arbitré dans au moins une condition

- **T01 — Déclenchement sur demande pédagogique**
- **T05 — Pas de niveau global de l'apprenant**
- **T08 — Une seule notion nouvelle est acceptable**
- **T10 — Une nouveauté + prérequis attestés**
- **T11 — Faux positif : une notion n'est pas nouvelle parce qu'elle porte un nouveau nom**
- **T14 — Quiz d'auto-positionnement**
- **T18 — Élicitation avant exposition**
- **T19 — Mise à jour après preuve**
- **T22 — Contradiction entre deux fichiers**
- **T23 — Bloom n'est pas une barrière absolue**
- **T25 — Reformulation sans mots-clés**

## T06 — Une impression n'est pas une preuve

Résultat :

> **avec skill = PASS / sans skill = INDÉTERMINÉ**

Le comportement avec skill est satisfaisant, mais le résultat sans skill ne permet pas une comparaison PASS/FAIL suffisamment nette.

Au total, **12 tests** restent donc hors de la comparaison stricte `mieux / pareil / moins bien`.

---

# 6. Refus de la notation chiffrée par défaut

La campagne montre également que le skill modifie la manière dont le modèle conçoit spontanément l'évaluation : **sans skill, il tend à produire des barèmes chiffrés ; avec skill, il privilégie critères, preuves et attestation.**

Le contraste porte donc moins sur la forme de la réponse que sur **le cadre de raisonnement utilisé pour évaluer**.

## Observation ad hoc

Ce résultat est apparu après le gel de la collecte, lors de la relecture des trajectoires.

Dans la condition **sans skill**, le modèle introduit spontanément des systèmes de notation chiffrés lorsqu'il doit produire une activité évaluée. On retrouve notamment :

- des barèmes sur 10, 20 ou 100 ;
- des points attribués par critère ;
- des bonus ;
- des seuils de réussite tels que `9/12`, `16/20` ou `60/100`.

Le phénomène apparaît dans **12 trajectoires sans skill**, réparties sur **6 scénarios différents**. Il est présent dans **les deux répétitions de chacun de ces six scénarios**.

Les systèmes de notation produits ne semblent pas correspondre à un référentiel stable. Pour un même scénario, le modèle peut utiliser un barème sur 20 dans une répétition puis sur 100 dans l'autre. Les seuils et les pondérations changent également.

Le comportement observé ressemble donc davantage à une heuristique spontanée :

> **activité évaluée → note chiffrée**

Dans les trajectoires correspondantes **avec skill**, ce recours systématique à la notation numérique n'est pas observé. Le raisonnement est davantage structuré autour :

- des critères de réussite ;
- de la production de l'apprenant ;
- des éléments effectivement observables ;
- des preuves recueillies ;
- de ce que ces preuves autorisent à conclure.

Le contraste ne porte donc pas uniquement sur la présence d'une note. Il concerne plus largement **la représentation de ce qu'est une évaluation**.

## Hypothèse explicative

L'inspection du candidat `en_cours/` permet de proposer une explication à ce contraste.

Le skill ne repose pas principalement sur une interdiction générale de la notation chiffrée. Il fournit surtout au modèle **un système alternatif complet pour construire et interpréter une évaluation**.

Plusieurs mécanismes convergent.

Dans `SKILL.md`, une activité évaluée est explicitement reliée à des **Critères 3C**, et le skill demande de maintenir un état visible :

```text
notion | palier | preuve
```

Dans `references/opo.md`, l'évaluation repose sur :

- un comportement observable ;
- des conditions ;
- un critère de réussite.

Dans `references/etat_des_paliers.md`, la règle est explicite :

> **La preuve est une référence, pas un adjectif.**

L'attestation doit donc être reliée à un élément observable, par exemple une activité ou des tests réussis, plutôt qu'à une appréciation générale.

Dans `references/taxonomie.md`, une activité évaluée produit précisément une preuve susceptible d'attester un palier.

D'autres références renforcent ce cadre :

- `references/quiz.md` définit le quiz d'auto-positionnement comme **non noté** et précise que son résultat ne doit pas être interprété comme un score isolé ;
- `references/recul.md` indique qu'un exercice réflexif noté perd sa fonction ;
- `references/andragogie.md` demande de relier l'effort à un bénéfice concret pour l'apprenant plutôt qu'à une notation.

Le modèle dispose donc déjà d'une réponse structurée à la question :

> « Comment savoir si cette activité est réussie ? »

Il n'a plus besoin de fabriquer un mécanisme intermédiaire de points, de total et de seuil.

On peut représenter les deux cadres observés ainsi :

```text
Sans skill

activité évaluée
→ barème
→ points
→ total
→ seuil
→ réussite / échec
```

```text
Avec skill

objectif
→ production observable
→ critères
→ preuve
→ portée de la preuve
→ attestation
```

Cela ne signifie pas que le skill refuse toute mesure numérique.

Un nombre reste parfaitement pertinent lorsqu'il appartient réellement au critère : durée maximale, nombre minimal d'éléments à trouver, résultat attendu d'un test, seuil imposé par un référentiel, etc.

La différence semble plutôt être :

> **une mesure objectivement liée à la performance reste légitime ; un barème numérique inventé pour matérialiser l'évaluation ne constitue plus le mécanisme par défaut.**

L'hypothèse explicative est donc que **le skill réduit spontanément la notation chiffrée parce qu'il remplace la logique de quantification par une logique de preuve et d'attestation suffisamment structurée pour guider le modèle**.

Autrement dit :

> **évaluer n'est plus d'abord attribuer une valeur numérique ; évaluer consiste d'abord à observer une performance, appliquer des critères et déterminer ce qu'elle permet d'attester.**

La campagne met en évidence un **contraste comportemental reproductible dans les trajectoires observées**. Elle n'isole toutefois pas expérimentalement quelle règle interne particulière du skill produit cet effet.

---

# 7. Ce que la V1 permet de dire sur l'utilité du skill

## Le skill est utile comme garde-fou

Les résultats montrent que sa principale valeur n'est pas de rendre le modèle généralement « meilleur pédagogue » sur toutes les dimensions.

Sa valeur apparaît surtout lorsqu'une décision exige de maintenir une discipline explicite :

1. **ne pas attester au-delà de la preuve disponible** ;
2. **contrôler les prérequis avant une activité évaluée** ;
3. **limiter la surcharge en nouveautés** ;
4. **aligner objectif, tâche, critère et preuve** ;
5. **résister à une demande utilisateur pédagogiquement inadéquate** ;
6. **choisir et respecter un format pédagogique adapté**.

## Le modèle de base sait déjà faire une partie du travail

Plusieurs comportements généraux ne nécessitent pas le skill pour être obtenus de manière fiable dans cette campagne :

- accompagnement guidé ;
- ancrage concret ;
- gestion professionnelle de l'erreur ;
- reconnaissance de l'absence de persistance ;
- respect général du périmètre.

Le skill ne doit donc pas être évalué uniquement sur sa capacité à produire de « bonnes réponses pédagogiques » génériques.

Sa valeur se situe davantage dans **les contraintes qu'il impose lorsque le comportement intuitif du modèle devient pédagogiquement fragile**.

## Deux points à corriger ou surveiller

### T26 — Sur-détection de nouveauté

Le skill peut transformer une règle de prudence en règle trop rigide et considérer une nouvelle tâche comme une nouvelle notion.

### T28 — Séparation apprenant / formateur

La V1 ne garantit pas encore correctement que la solution ou les éléments internes restent séparés du contenu remis à l'apprenant.

---

# 8. Conclusion générale

La campagne V1 ne montre pas un avantage uniforme du skill sur tous les comportements.

Elle montre quelque chose de plus précis :

> **le skill est utile lorsqu'il agit comme garde-fou d'ingénierie pédagogique.**

Sur les tests directement comparables :

- il fait mieux dans **9 cas** ;
- il n'apporte pas plus dans **8 cas** ;
- il fait moins bien dans **1 cas**.

Les gains se concentrent sur les dimensions qui constituent le cœur de sa promesse : prérequis, preuves, paliers, budget de nouveauté, alignement et structuration des activités.

Le résultat sur la notation chiffrée va dans le même sens. Le skill ne semble pas seulement ajouter des règles de forme : il modifie le **cadre de raisonnement** utilisé par le modèle pour décider ce qu'est une évaluation valide.

La V1 peut donc être décrite comme un candidat qui apporte une **discipline pédagogique explicite et observable**, avec deux réserves principales :

- éviter que cette discipline devienne une rigidité excessive ;
- renforcer la séparation entre contenu apprenant et contenu formateur.

---

# 9. Limites méthodologiques

Les résultats doivent être interprétés avec les limites suivantes :

- **17/120 trajectoires** ont produit un désaccord entre les deux scoreurs et restent non arbitrées ;
- **12/60 couples `test × condition`** restent non tranchables ;
- la règle conservatrice d'exclusion des désaccords inter-scoreurs a été décidée après observation des deux scorings puis gelée avant les répétitions conditionnelles ;
- pour le lot complémentaire de trois trajectoires, l'identité des verdicts S2 avec S1 a été consignée par l'opérateur ; le TSV complet S2 avec ses justifications n'est pas disponible dans les artefacts utilisés pour ce rapport ;
- le résultat relatif à la notation chiffrée a été identifié **post hoc**, après le gel de la collecte.

Cette dernière observation repose toutefois sur les **mêmes trajectoires expérimentales gelées** que le reste de la campagne. Son caractère post hoc concerne la pré-spécification de l'hypothèse, pas la provenance des données.

Elle n'a pas été utilisée pour modifier rétroactivement les oracles T01 à T30, rescoring les trajectoires ou déclencher de nouvelles répétitions.

---

# 10. Traçabilité des gels

Principaux jalons Git de la campagne :

- `validation-v1-runtime-frozen`
- `validation-v1-initial-series-frozen`
- `validation-v1-blind-scoring-frozen`
- `validation-v1-inter-scorer-decision-frozen`
- `validation-v1-conditional-repetitions-frozen`
- `validation-v1-conditional-blind-scoring-frozen`
- `validation-v1-final-scoring-frozen`

Le tag `validation-v1-final-scoring-frozen` correspond au gel des résultats de scoring avant intégration éditoriale ultérieure du résultat relatif à la notation chiffrée.
