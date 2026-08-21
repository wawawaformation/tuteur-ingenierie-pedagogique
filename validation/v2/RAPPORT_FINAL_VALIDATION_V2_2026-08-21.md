# Rapport final — validation expérimentale V2

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-08-21  
**Candidat :** V2  
**Snapshot candidat exécuté :** provenance déclarée `97ee00a0623cdbff0ec774a96d3fbd8a45ed6653`  
**Runtime :** Claude Code 2.1.232 — `claude-sonnet-5` — effort `medium`

---

## Résumé exécutif

La campagne V2 fournit un résultat nettement favorable au candidat, tout en faisant apparaître un coût en tokens réel et une zone de vigilance résiduelle sur l'élicitation du point de départ.

La batterie confirmatoire comprend **40 runs de base** :

- `NOY001` à `NOY008` : comparaison **avec skill / sans skill**, deux répétitions par condition, soit 32 runs ;
- `NOY009` à `NOY012` : **avec skill uniquement**, deux répétitions, soit 8 runs.

Après double scoring aveugle, adjudication des trois désaccords inter-scoreurs, gel puis désaveuglement, les 40 runs de base donnent :

| Condition | PASS | FAIL | INDÉTERMINÉ | Total |
|---|---:|---:|---:|---:|
| **Avec skill** | **23** | **1** | **0** | **24** |
| **Sans skill** | **2** | **13** | **1** | **16** |

À titre descriptif :

- avec skill : **23/24 = 95,8 % de PASS** ;
- sans skill : **2/16 = 12,5 % de PASS**.

Ces taux ne constituent pas à eux seuls la conclusion de la campagne : le plan impose une lecture scénario par scénario.

Le contraste comportemental est particulièrement net sur `NOY004` à `NOY008` :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

`NOY003` montre également une meilleure stabilité avec skill :

```text
avec skill : PASS / PASS
sans skill : PASS / FAIL / PASS(R3)
```

`NOY001` reste la seule cellule avec skill ayant produit un FAIL :

```text
avec skill : FAIL / PASS / PASS(R3)
sans skill : FAIL / FAIL
```

Le troisième résultat important est `NOY002` : le comportement recherché est également observable sans skill lorsque la trajectoire est complète. La V2 ne doit donc pas prétendre à un gain artificiel sur ce scénario.

Les quatre contrats propres à la V2 (`NOY009` à `NOY012`) sont **stables en PASS : 8/8**.

Trois répétitions comportementales R3 avaient été pré-autorisées par la règle gelée, après constat d'une divergence R1/R2 dans trois cellules. Les trois ont été exécutées et scorées officiellement par l'opérateur humain :

```text
R3-NOY001-A   PASS
R3-NOY002-BP  PASS
R3-NOY003-BP  PASS
```

Ces R3 ne remplacent pas les résultats de base et ne sont pas intégrés dans un taux artificiel sur 43 runs. Ils servent à caractériser la stabilité des trois cellules discordantes.

La mesure secondaire d'efficience est complète : **40/40 runs disposent de métriques de tokens observables**.

Sur les **16 paires A/B′ directement comparables** :

- avec skill : **4 174 595 tokens** ;
- sans skill : **1 674 701 tokens** ;
- différence : **+2 499 894 tokens** ;
- ratio : **2,49×** ;
- surcoût relatif agrégé : **+149,3 %** ;
- le run avec skill consomme davantage dans **16/16 paires**.

Le surcoût est principalement un surcoût d'entrée et de lecture de contexte/cache, et non simplement une conséquence de réponses finales plus longues.

Ce coût relatif élevé doit cependant être distingué de la faisabilité pratique. À titre d'observation opérateur non instrumentée, les **20 derniers runs ont représenté environ 11 points du quota d'utilisation affiché par Claude**. Cet indicateur n'est pas une mesure de tokens ni de prix, mais il montre que la campagne n'a pas rencontré de contrainte pratique forte de quota.

### Conclusion

La lecture des résultats par rapport à la **promesse fonctionnelle V2** est globalement favorable, mais elle n'est pas uniforme :

- **P01 — établir le point de départ utile** : supportée, avec un contraste favorable au skill, mais **stabilité imparfaite** (`FAIL / PASS / PASS(R3)` avec skill) ;
- **P02 — raisonner par notion, palier et preuve** : **fortement supportée** par plusieurs scénarios convergents ; selon le sous-comportement, le skill apporte soit un différentiel net, soit une stabilisation d'une capacité déjà accessible au modèle nu ;
- **P03 — préserver la valeur diagnostique** : **fortement supportée**, avec un contraste reproductible ;
- **P04 — maintenir l'alignement objectif / tâche / production / critères / preuve / conclusion** : **fortement supportée**, avec un contraste reproductible ;
- **G05 — ne pas inventer de notation arbitraire** : contraste différentiel net et confirmatoire ;
- **G06 et les contrats d'architecture effectivement testés** : conformité observée avec skill ;
- **G01 à G04** : non revalidées spécifiquement par cette batterie et donc non revendiquées comme démontrées par la V2.

Cette lecture correspond à la promesse elle-même : le skill ne prétend pas améliorer globalement toute production pédagogique ; il cherche à rendre plus fiables certaines décisions lorsqu'une information pédagogique pertinente devrait modifier l'apprentissage ou l'évaluation.

Au regard des critères pré-définis dans le plan expérimental, la V2 satisfait les conditions d'un **candidat stabilisable** :

- `NOY009` à `NOY012` sont stables en PASS ;
- aucun défaut bloquant reproductible n'est établi sur `NOY001` à `NOY008` ;
- les instabilités sont limitées à trois cellules, identifiées et interprétables ;
- les trois R3 sont favorables ;
- l'intégrité du candidat, du protocole et des données de base est préservée.

La V2 peut donc être considérée comme **validée expérimentalement pour le périmètre testé et candidate à la promotion**.

La promotion effective vers `stable/` et `dist/stable/` reste une décision explicite distincte du présent rapport.

---

# 1. Objet de la validation

La V2 ne cherche pas à montrer que le skill rend systématiquement toute réponse pédagogique meilleure.

Le plan expérimental pose quatre questions :

1. le candidat respecte-t-il les comportements protégés par `NOY001` à `NOY008` ?
2. pour ces comportements, la disponibilité du skill modifie-t-elle effectivement certaines décisions par rapport au même modèle sans skill ?
3. le candidat respecte-t-il les contrats propres au produit protégés par `NOY009` à `NOY012` ?
4. quel surcoût de consommation de tokens accompagne l'utilisation du skill à stimulus comparable ?

Cette conception reprend une leçon importante de la V1 : l'utilité du skill doit être recherchée dans les **décisions et garde-fous qu'il rend plus fiables**, et non dans une impression générale de « meilleure pédagogie ».

La V2 resserre donc la campagne autour de douze scénarios explicitement reliés à des invariants.

---

# 2. Batterie expérimentale

## 2.1 Scénarios A/B′ — NOY001 à NOY008

| Scénario | Comportement protégé |
|---|---|
| **NOY001** | Éliciter un point de départ utile avant une exposition substantielle dépendante de prérequis non établis |
| **NOY002** | Ne pas confondre exposition ou auto-déclaration avec preuve, puis réviser le diagnostic lorsqu'une preuve autonome devient disponible |
| **NOY003** | Ne pas attester un palier d'application à partir d'une preuve qui n'atteste que connaissance/compréhension |
| **NOY004** | Préserver la valeur diagnostique d'une activité évaluée en maîtrisant le nombre de notions nouvelles simultanées |
| **NOY005** | Maintenir l'alignement objectif → tâche → preuve → critère |
| **NOY006** | Raisonner notion par notion sur la portée d'une réussite intégrée |
| **NOY007** | Ne pas transformer une auto-déclaration en attestation d'un palier |
| **NOY008** | Évaluer sans inventer spontanément une notation ou un barème arbitraire |

Pour chacun :

```text
avec skill × R1/R2
sans skill × R1/R2
```

Soit **32 runs**.

## 2.2 Contrats propres au produit — NOY009 à NOY012

| Scénario | Contrat testé |
|---|---|
| **NOY009** | Un gabarit Quiz reste une Activité complète et hérite de son socle commun |
| **NOY010** | Le routage d'un gabarit ne doit pas être enfermé dans une modalité rigide présentiel/distanciel ou synchrone/asynchrone |
| **NOY011** | Dans une activité évaluée, préserver la valeur de preuve en séparant critères accessibles et solution/correction décisive |
| **NOY012** | Représenter correctement le catalogue de gabarits, leur architecture et leurs contextes d'usage |

Ces contrats n'ont de sens qu'avec le skill :

```text
avec skill × R1/R2
```

Soit **8 runs**.

## 2.3 Total

```text
32 runs A/B′
+ 8 runs A uniquement
= 40 runs de base
```

Les R3 sont conditionnels et ne font pas partie de ces 40 runs.

---

# 3. Gel, exécution et intégrité

Le paquet opérateur a été gelé avant l'exécution officielle.

Le gel portait notamment sur :

- le candidat ;
- les douze scénarios ;
- les prompts exacts ;
- les personas et fixtures ;
- les oracles ;
- `RUNS.csv` et la randomisation ;
- les règles de répétition ;
- le collector ;
- les métriques de tokens ;
- les paramètres Claude Code.

Le préflight avait notamment confirmé :

```text
candidat SHA-256          PASS
40 runs                   PASS
32 A/B′ + 8 A-only        PASS
12 scénarios NOY          PASS
20 cellules R3 prévues    PASS
collector                 51/51 tests PASS
Claude Code               2.1.232
usage tokens réel         PASS
```

Le mode opérateur à deux blocs a été introduit avant le premier run officiel. Cet ajustement concernait la couche d'exploitation et non le candidat, les scénarios, les oracles, l'ordre expérimental ou la logique de scoring.

La campagne de base a ensuite été exécutée dans l'ordre randomisé gelé.

---

# 4. Scoring aveugle et adjudication

Deux scoreurs indépendants ont évalué le même paquet de **40 trajectoires anonymisées**.

Ils ne disposaient pas :

- de la condition expérimentale ;
- de la répétition ;
- du `run_id` source ;
- des résultats historiques ;
- du verdict de l'autre scoreur.

Verdicts autorisés :

```text
PASS
FAIL
INDÉTERMINÉ
```

## 4.1 Accord inter-scoreurs

Résultat :

```text
N = 40
accords = 37
désaccords = 3
accord brut = 92,5 %
κ de Cohen = 0,8435
```

Le niveau d'accord est nettement supérieur à celui observé pendant la V1.

Les trois désaccords portent sur :

| Trajectoire | Scénario |
|---|---|
| `TRAJ-0024` | NOY005 |
| `TRAJ-0035` | NOY011 |
| `TRAJ-0038` | NOY001 |

## 4.2 Adjudication

Les trois désaccords ont été transmis à une adjudication distincte.

Verdicts finaux :

| Trajectoire | Scénario | Verdict |
|---|---|---|
| `TRAJ-0024` | NOY005 | **FAIL** |
| `TRAJ-0035` | NOY011 | **PASS** |
| `TRAJ-0038` | NOY001 | **FAIL** |

Après cette adjudication, les **40 verdicts comportementaux de base ont été gelés avant désaveuglement**.

Les trois trajectoires adjudicées ne sont pas celles qui ont ensuite déclenché les R3. Les deux mécanismes sont donc indépendants :

```text
désaccord de scoreurs
≠
discordance comportementale R1/R2
```

---

# 5. Résultats des 40 runs de base

## 5.1 Résultat global descriptif

### Avec skill

24 runs :

- PASS : **23**
- FAIL : **1**
- INDÉTERMINÉ : **0**

Soit :

> **23/24 = 95,8 % de PASS**

### Sans skill

16 runs :

- PASS : **2**
- FAIL : **13**
- INDÉTERMINÉ : **1**

Soit :

> **2/16 = 12,5 % de PASS**

Ces taux décrivent les trajectoires de base. Ils ne remplacent pas l'analyse par scénario.

## 5.2 Tableau complet après désaveuglement

| Scénario | Avec skill R1 | Avec skill R2 | Sans skill R1 | Sans skill R2 |
|---|---|---|---|---|
| **NOY001** | FAIL | PASS | FAIL | FAIL |
| **NOY002** | PASS | PASS | PASS | INDÉTERMINÉ |
| **NOY003** | PASS | PASS | PASS | FAIL |
| **NOY004** | PASS | PASS | FAIL | FAIL |
| **NOY005** | PASS | PASS | FAIL | FAIL |
| **NOY006** | PASS | PASS | FAIL | FAIL |
| **NOY007** | PASS | PASS | FAIL | FAIL |
| **NOY008** | PASS | PASS | FAIL | FAIL |
| **NOY009** | PASS | PASS | — | — |
| **NOY010** | PASS | PASS | — | — |
| **NOY011** | PASS | PASS | — | — |
| **NOY012** | PASS | PASS | — | — |

---

# 6. Répétitions comportementales R3

## 6.1 Règle pré-définie

Le plan prévoyait deux répétitions indépendantes par cellule.

Un R3 ne pouvait être déclenché qu'en présence d'une **discordance comportementale entre R1 et R2**.

Le plan précise explicitement :

> R3 sert à caractériser la stabilité du comportement, pas à effacer un résultat défavorable.

Après gel des 40 verdicts et désaveuglement, trois cellules répondaient à cette condition :

| Scénario | Condition | R1 | R2 |
|---|---|---|---|
| **NOY001** | avec skill | FAIL | PASS |
| **NOY002** | sans skill | PASS | INDÉTERMINÉ |
| **NOY003** | sans skill | PASS | FAIL |

La décision de lancer ces R3 a été gelée avant connaissance de leur résultat.

## 6.2 Scoring humain officiel

Pendant l'examen du premier R3, `R3-NOY001-A`, un risque méthodologique a été identifié : un agent scoreur a initialement durci l'oracle en interprétant « avant exposition substantielle » comme une quasi-interdiction de tout contenu avant la réponse diagnostique.

Or l'oracle précise qu'une courte phrase de cadrage ou une accroche reste compatible avec le comportement attendu.

Afin d'éviter qu'une règle implicite ajoutée par un scoreur IA ne décide du sort des trois derniers cas, une décision spécifique a été gelée :

```text
SCORING_R3 = HUMAIN_UNIQUE
R3 concernés = 3/3
délégation IA du verdict = interdite
réversibilité dans cette campagne = non
```

Les agents IA ont pu fournir une aide d'exécution et des avis consultatifs, mais **le verdict officiel des R3 appartient uniquement à l'opérateur humain**.

Cette décision est documentée dans :

`DECISION_SCORING_HUMAIN_R3_V2_2026-08-21.md`

## 6.3 Résultats

| R3 | Condition | Verdict humain officiel |
|---|---|---|
| `R3-NOY001-A` | avec skill | **PASS** |
| `R3-NOY002-BP` | sans skill | **PASS** |
| `R3-NOY003-BP` | sans skill | **PASS** |

## 6.4 Lecture correcte des R3

Après R3 :

| Scénario | Condition | Séquence observée |
|---|---|---|
| NOY001 | avec skill | **FAIL / PASS / PASS** |
| NOY002 | sans skill | **PASS / INDÉTERMINÉ / PASS** |
| NOY003 | sans skill | **PASS / FAIL / PASS** |

Les R3 montrent donc une troisième observation favorable dans chacune des trois cellules instables.

Ils **n'annulent pas** :

- le FAIL initial de NOY001 avec skill ;
- l'INDÉTERMINÉ initial de NOY002 sans skill ;
- le FAIL initial de NOY003 sans skill.

Il serait méthodologiquement incorrect de les ajouter aux 40 runs pour calculer un nouveau « taux de PASS sur 43 ».

---

# 7. Comparaison directe de l'apport du skill

La V2 permet une lecture plus précise qu'un taux global.

## 7.1 Contraste net et reproductible — NOY004 à NOY008

Sur cinq scénarios consécutifs :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

### NOY004 — budget de nouveauté

Le skill protège la valeur diagnostique d'une activité évaluée lorsqu'elle mobilise plusieurs notions nouvelles non attestées.

Le modèle sans skill échoue dans les deux répétitions.

### NOY005 — alignement objectif / tâche / preuve / critère

Le skill distingue la simple complétude d'un livrable de la preuve réelle de son alignement pédagogique.

Le modèle sans skill échoue dans les deux répétitions.

### NOY006 — portée d'une réussite intégrée

Le skill raisonne notion par notion et ne transforme pas la réussite globale d'une activité en attestation automatique de tout ce qu'elle mobilise.

Le modèle sans skill échoue dans les deux répétitions.

### NOY007 — auto-déclaration et palier

Le skill empêche une déclaration de compréhension de devenir une preuve d'application.

Le modèle sans skill échoue dans les deux répétitions.

### NOY008 — évaluation sans notation arbitraire

Le skill évite de transformer spontanément une activité évaluée en barème ou système de points lorsque rien ne l'impose.

Le modèle sans skill échoue dans les deux répétitions.

Ce dernier résultat est particulièrement important dans la continuité de la V1 : la tendance du modèle sans skill à inventer des barèmes avait été observée **post hoc** pendant la V1. En V2, cette observation devient une hypothèse explicitement testée avant exécution et reçoit un résultat confirmatoire propre :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

---

## 7.2 NOY001 — gain favorable mais stabilité imparfaite

Résultat :

```text
avec skill : FAIL / PASS / PASS(R3)
sans skill : FAIL / FAIL
```

Le contraste est favorable au skill : la condition sans skill échoue deux fois, tandis que la condition avec skill produit deux comportements conformes sur trois observations.

Cependant, le FAIL initial avec skill reste un résultat valide.

NOY001 ne doit donc pas être présenté comme parfaitement stabilisé.

Le R3 apporte également une leçon de scoring : l'oracle protège l'élicitation **avant exposition substantielle**, pas une règle de « silence pédagogique absolu avant toute réponse ». Un cadrage bref, l'annonce d'un plan ou une amorce ne constituent pas automatiquement un FAIL.

Ce point doit rester explicitement documenté pour les futures campagnes.

---

## 7.3 NOY003 — le skill stabilise un comportement que le modèle de base sait parfois produire

Résultat :

```text
avec skill : PASS / PASS
sans skill : PASS / FAIL / PASS(R3)
```

Le modèle sans skill est capable de distinguer un QCM de compréhension d'une preuve d'application.

Mais il ne le fait pas de manière stable : une répétition a attesté `Application` sur la seule base du QCM 10/10.

La valeur observée du skill est donc ici moins l'apparition d'une capacité inexistante que sa **stabilisation**.

---

## 7.4 NOY002 — gain différentiel non démontré

Résultat :

```text
avec skill : PASS / PASS
sans skill : PASS / INDÉTERMINÉ / PASS(R3)
```

Lorsque la décision est observable, le modèle sans skill sait lui aussi :

1. refuser `Appliquer` sur la seule auto-déclaration « je pense avoir compris » ;
2. accepter ensuite une performance autonome suffisamment précise accompagnée de tests passants.

Le résultat `INDÉTERMINÉ` de R2 sans skill provient de l'absence de la réponse décisive dans la trajectoire et ne constitue pas un FAIL comportemental.

La conclusion correcte est donc :

> **NOY002 est stable avec skill, mais cette campagne ne démontre pas que le skill est nécessaire pour obtenir ce comportement.**

C'est un résultat nul informatif, explicitement accepté par le plan expérimental.

---

# 8. Contrats propres à la V2

Les quatre scénarios exécutés uniquement avec skill donnent :

| Scénario | R1 | R2 |
|---|---|---|
| **NOY009** | PASS | PASS |
| **NOY010** | PASS | PASS |
| **NOY011** | PASS | PASS |
| **NOY012** | PASS | PASS |

Soit :

> **8 PASS / 8 runs**

## NOY009 — héritage du socle Activité

Le gabarit Quiz est bien traité comme une Activité spécialisée et non comme un questionnaire isolé.

## NOY010 — routage sans enfermement par modalité

Le skill ne transforme pas les axes présentiel/distanciel et synchrone/asynchrone en table rigide d'autorisation des gabarits.

## NOY011 — maîtrise de l'exposition

Le skill maintient la distinction entre :

```text
critères accessibles à l'apprenant
et
solution / correction / indices décisifs réservés au moment approprié
```

Ce résultat apporte une réponse favorable à une faiblesse proche de celle observée en V1 autour de la séparation du contenu destiné à l'apprenant et des éléments réservés au formateur, sans prétendre que NOY011 reproduit exactement l'ancien test T28.

## NOY012 — catalogue et architecture

Le skill représente correctement :

```text
Module
└── Séquence
    └── Séance
        └── Activité
```

et traite les gabarits spécialisés comme des formes d'Activité, avec des contextes d'usage non exclusifs.

### Conclusion sur les contrats V2

Le premier critère explicite de stabilisabilité du plan est satisfait :

> **NOY009 à NOY012 sont stables en PASS.**

---

# 9. Consommation de tokens

## 9.1 Statut de la mesure

La consommation de tokens était **pré-spécifiée dans le plan expérimental** comme mesure secondaire d'efficience.

Elle ne participe jamais au verdict pédagogique.

Les compteurs proviennent des traces runtime et non d'une reconstruction approximative.

Disponibilité :

> **40/40 runs avec métriques observables**

Compteurs conservés :

```text
input_tokens
cache_creation_input_tokens
cache_read_input_tokens
output_tokens
total_input_tokens
total_tokens
```

## 9.2 Comparaison appariée A/B′

La comparaison valide porte sur `NOY001` à `NOY008`, appariés par scénario et répétition :

```text
16 runs avec skill
vs
16 runs sans skill
```

### Résultat agrégé

| Mesure | Avec skill | Sans skill | Différence |
|---|---:|---:|---:|
| `total_input_tokens` | **4 110 856** | **1 657 103** | **+2 453 753** |
| `output_tokens` | **63 739** | **17 598** | **+46 141** |
| `total_tokens` | **4 174 595** | **1 674 701** | **+2 499 894** |

Sur le total :

```text
ratio A / B′ = 2,49×
surcoût agrégé = +149,3 %
```

Le surcoût est positif dans :

> **16 paires sur 16**

### Distribution des deltas

| Indicateur | Delta A − B′ |
|---|---:|
| Moyenne | **+156 243 tokens** |
| Médiane | **+147 234 tokens** |
| Minimum | **+44 983 tokens** |
| Maximum | **+310 502 tokens** |

Le surcoût existe donc sur toute la batterie comparative, et n'est pas produit par un seul run aberrant.

## 9.3 Composition du surcoût

| Composante | Avec skill | Sans skill | Delta |
|---|---:|---:|---:|
| Input non caché | 168 | 80 | +88 |
| Création de cache | 335 719 | 145 021 | **+190 698** |
| Lecture de cache | 3 774 969 | 1 512 002 | **+2 262 967** |
| Sortie | 63 739 | 17 598 | **+46 141** |

En valeur absolue :

- environ **98,2 %** du delta total provient de l'entrée ;
- environ **90,5 %** du delta total provient à lui seul de la lecture de cache ;
- le surcoût de sortie représente environ **1,8 %** du delta total.

La lecture correcte est donc :

> **Le coût supplémentaire du skill vient principalement du contexte et des références qu'il mobilise, beaucoup plus que d'une simple augmentation de la longueur des réponses finales.**

Les sorties sont néanmoins elles-mêmes plus volumineuses en condition A : **63 739 contre 17 598 tokens**, soit environ **3,62×** sur cette campagne.

## 9.4 Détail par scénario

| Scénario | Tokens A | Tokens B′ | Delta | Surcoût agrégé du scénario |
|---|---:|---:|---:|---:|
| **NOY001** | 172 684 | 82 418 | +90 266 | **+109,5 %** |
| **NOY002** | 1 034 452 | 466 322 | +568 130 | **+121,8 %** |
| **NOY003** | 693 898 | 464 030 | +229 868 | **+49,5 %** |
| **NOY004** | 611 945 | 169 125 | +442 820 | **+261,8 %** |
| **NOY005** | 393 777 | 83 206 | +310 571 | **+373,3 %** |
| **NOY006** | 274 672 | 80 334 | +194 338 | **+241,9 %** |
| **NOY007** | 351 148 | 246 127 | +105 021 | **+42,7 %** |
| **NOY008** | 642 019 | 83 139 | +558 880 | **+672,2 %** |

Le coût n'est donc pas constant.

En relatif, `NOY008` est le scénario le plus coûteux par rapport à son témoin.

En valeur absolue, les plus gros contributeurs sont :

1. `NOY002` : **+568 130 tokens** ;
2. `NOY008` : **+558 880 tokens** ;
3. `NOY004` : **+442 820 tokens**.

Il serait incorrect de transformer le `+149,3 %` global en règle générale du type « le skill coûte toujours 149 % de plus ». Il s'agit d'un résultat propre à cette batterie, ce runtime, ce modèle et ces trajectoires.

## 9.5 NOY009 à NOY012

Ces scénarios n'ont pas de témoin B′ ; aucun « surcoût dû au skill » ne peut donc être calculé.

Consommation absolue :

| Scénario | 2 runs avec skill |
|---|---:|
| NOY009 | **173 681 tokens** |
| NOY010 | **579 727 tokens** |
| NOY011 | **550 698 tokens** |
| NOY012 | **363 506 tokens** |
| **Total** | **1 667 612 tokens** |

Sur les **24 runs avec skill** de la campagne de base :

> **5 842 207 tokens au total**

Ce total ne doit pas être comparé directement aux 16 runs sans skill, car les deux ensembles n'ont ni la même taille ni exactement le même périmètre.

## 9.6 Mise en perspective par le quota Claude

Une observation opérateur, extérieure aux compteurs expérimentaux, apporte un contexte pratique :

> les 20 derniers runs ont représenté environ **11 points du quota d'utilisation affiché par Claude**.

Cette donnée doit rester secondaire :

- l'interface ne garantit pas que le pourcentage de quota soit une simple fonction linéaire des tokens ;
- ce n'est pas une mesure de temps de calcul ;
- ce n'est pas un prix ;
- cette observation n'a pas été enregistrée comme métrique gelée run par run.

Elle permet toutefois une conclusion pratique raisonnable :

> **le surcoût relatif en tokens est substantiel, mais il n'a pas rendu la campagne de cette taille opérationnellement difficile à exécuter.**

Autrement dit :

> **le skill échange davantage de contexte et de calcul contre une discipline comportementale plus forte ; dans cette campagne, ce coût reste pratiquement soutenable.**

---

# 10. Continuité entre V1 et V2

Les pourcentages V1 et V2 ne doivent pas être comparés directement : les batteries, les scénarios et les règles de scoring ne sont pas les mêmes.

La continuité est avant tout **fonctionnelle et méthodologique**.

## 10.1 Confirmation du rôle de garde-fou

La V1 concluait que la valeur du skill se trouvait surtout dans sa fonction de garde-fou :

- prérequis ;
- preuves ;
- paliers ;
- budget de nouveauté ;
- alignement ;
- structuration des activités.

La V2 retrouve précisément ce profil.

Le contraste le plus fort n'est pas « réponse jolie contre réponse mauvaise », mais :

```text
le modèle nu produit une réponse plausible
mais franchit une limite pédagogique
```

alors que le skill maintient plus souvent la contrainte.

`NOY004` à `NOY008` constituent l'expression la plus nette de ce phénomène.

## 10.2 De l'observation post hoc à la confirmation : la notation

En V1, l'usage spontané de notes et de barèmes dans la condition sans skill avait été découvert après la collecte.

La V2 transforme explicitement cette observation en `NOY008`.

Résultat :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Ce résultat est plus fort méthodologiquement que l'observation V1 : l'hypothèse a été définie avant l'exécution de la campagne V2.

## 10.3 Preuve et palier

Plusieurs tests historiques de V1 sont recentrés dans la V2 :

- QCM ≠ preuve d'application ;
- auto-déclaration ≠ preuve ;
- réussite intégrée ≠ attestation automatique de toutes les notions.

Les résultats `NOY003`, `NOY006` et `NOY007` montrent que ces garde-fous sont désormais obtenus de manière stable avec skill sur les répétitions de base.

## 10.4 Zone encore sensible : l'élicitation

La V1 avait déjà identifié le moment de l'élicitation comme une zone laissant de la latitude aux scoreurs.

`NOY001` resserre fortement l'oracle, notamment en précisant qu'une courte phrase de cadrage reste acceptable.

Malgré cela :

- une trajectoire avec skill échoue réellement ;
- un cas R3 a encore provoqué une première lecture trop stricte par un agent scoreur.

Le problème n'est donc pas entièrement disparu.

Il faut distinguer deux phénomènes :

1. **instabilité comportementale réelle** : le FAIL de base avec skill reste valide ;
2. **risque d'extension de l'oracle par le scoreur** : le R3 a montré qu'un scoreur pouvait ajouter une exigence de « zéro contenu » absente du texte.

NOY001 doit rester un test de non-régression particulièrement surveillé.

---

# 11. Confrontation des résultats à la promesse fonctionnelle V2

La campagne doit être jugée d'abord par rapport à ce que le candidat **promet réellement**, et non par rapport à une ambition plus large qui ne figure pas dans sa spécification.

La promesse V2 est volontairement limitée : le skill ne prétend pas améliorer globalement toute production pédagogique. Sa promesse centrale est d'amener l'agent à décider à partir du point de départ réellement établi, notion par notion et preuve par preuve, afin de préserver la valeur diagnostique des activités et l'alignement entre ce qui est visé, demandé, observé et conclu.

Le critère comportemental central peut être reformulé ainsi :

> **Une information pédagogique pertinente différente conduit-elle l'agent à prendre une décision différente lorsque cette information devrait effectivement modifier l'apprentissage ou l'évaluation ?**

Cette grille permet de distinguer quatre types de résultats :

1. un garde-fou apparaît nettement avec skill alors qu'il n'est pas maintenu sans skill ;
2. le skill stabilise un comportement que le modèle sans skill sait parfois produire ;
3. le comportement recherché existe déjà de manière satisfaisante sans skill ;
4. le comportement avec skill reste imparfaitement stable.

## 11.1 Tableau promesse → scénario → résultat

| Élément de la promesse | Scénarios principaux | Avec skill | Sans skill | Conclusion expérimentale |
|---|---|---|---|---|
| **P01 — Établir le point de départ utile** | NOY001 | FAIL / PASS / **PASS R3** | FAIL / FAIL | **Supportée, mais stabilité imparfaite** |
| **P02 — Raisonner par notion, palier et preuve** | NOY002, NOY003, NOY006, NOY007 | base stable en PASS sur tous ces scénarios | comportement variable, de PASS à FAIL | **Fortement supportée ; différentiel ou stabilisation selon le sous-comportement** |
| **P03 — Préserver la valeur diagnostique d'une activité évaluée** | NOY004, renforcé par NOY006 | PASS / PASS | FAIL / FAIL | **Très fortement supportée** |
| **P04 — Aligner objectif, tâche, production, critères, preuve et conclusion** | NOY005 | PASS / PASS | FAIL / FAIL | **Très fortement supportée** |
| **G05 — Ne pas inventer de notation arbitraire** | NOY008 | PASS / PASS | FAIL / FAIL | **Contraste différentiel net** |
| **G06 — Préserver la valeur de l'évaluation avant production** | NOY011 | PASS / PASS | non testé | **Conformité démontrée ; effet causal non mesuré** |
| **Architecture Activité / gabarits** | NOY009, NOY012 | PASS / PASS chacun | non testé | **Conformité démontrée** |
| **Modalités non rigides** | NOY010 | PASS / PASS | non testé | **Conformité démontrée** |
| **G01 à G04** | pas de scénario confirmatoire spécifique dans cette batterie | — | — | **Non revalidées par la campagne V2** |

Cette table constitue la lecture principale du résultat. Les taux globaux de PASS sont descriptifs ; ils ne remplacent pas cette correspondance entre promesse et observables.

---

## 11.2 P01 — Établir le point de départ utile

P01 demande de rechercher le point de départ utile lorsque son absence change réellement une décision pédagogique, sans transformer cette élicitation en questionnaire systématique.

Le principe n'est pas :

```text
toujours questionner avant de dire quoi que ce soit
```

mais :

```text
ne pas prendre une décision pédagogique importante
à partir d'acquis supposés ou inventés
```

Résultat :

```text
avec skill : FAIL / PASS / PASS(R3)
sans skill : FAIL / FAIL
```

Le contraste est favorable au skill : deux observations avec skill sont conformes, alors que les deux observations sans skill échouent.

Cependant, le FAIL initial avec skill reste un résultat valide.

La conclusion correcte est donc :

> **P01 est supportée expérimentalement et le contraste avec la condition sans skill est favorable, mais son exécution n'est pas encore parfaitement stable.**

P01 constitue le principal point de vigilance résiduel du candidat V2 et doit rester un test de non-régression prioritaire.

Le R3 a également clarifié une frontière importante pour le scoring : « avant exposition substantielle » ne signifie pas « absence absolue de tout cadrage, plan ou amorce pédagogique avant la réponse ». Ajouter cette exigence reviendrait à durcir l'oracle au-delà de la promesse.

---

## 11.3 P02 — Raisonner par notion, palier et preuve

P02 demande de distinguer notamment :

- exposition ;
- accompagnement ;
- déclaration ou impression de compréhension ;
- performance observable ;
- preuve compatible avec le palier visé.

Une notion ne doit être attestée à un palier que lorsqu'une preuve compatible avec ce palier est disponible.

Plusieurs scénarios convergent sur cette promesse.

### NOY002 — exposition, auto-déclaration puis nouvelle preuve

```text
avec skill : PASS / PASS
sans skill : PASS / INDÉTERMINÉ / PASS(R3)
```

Le comportement est stable avec skill.

Mais, lorsque la trajectoire est observable, le modèle sans skill sait lui aussi :

1. refuser `Appliquer` sur la seule déclaration « je pense avoir compris » ;
2. réviser ensuite son diagnostic après une réalisation autonome suffisamment précise accompagnée de tests passants.

La campagne ne démontre donc pas un gain différentiel sur ce sous-comportement.

Elle démontre en revanche que le candidat respecte bien P02.

### NOY003 — QCM et capacité d'application

```text
avec skill : PASS / PASS
sans skill : PASS / FAIL / PASS(R3)
```

Le modèle sans skill peut produire le bon raisonnement, mais ne le maintient pas de manière stable.

L'apport observé du skill est ici une **stabilisation** :

> un QCM de compréhension n'est pas transformé en preuve d'application.

### NOY006 — portée d'une réussite intégrée

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Le skill limite la portée de la preuve à ce qui a effectivement été observé, notion par notion.

Le contraste différentiel est net.

### NOY007 — auto-déclaration et attestation

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Le skill résiste à l'auto-attestation et maintient l'exigence d'une preuve compatible avec le palier.

Le contraste différentiel est également net.

### Conclusion sur P02

> **La logique notion → palier → preuve est fortement supportée par la campagne. Selon le sous-comportement, le skill apporte soit une capacité différentielle nette, soit une stabilisation d'un comportement déjà accessible au modèle sans skill.**

Ce résultat correspond précisément à la promesse : la valeur du skill n'est pas d'être l'unique source de toute bonne décision, mais d'accroître la fiabilité de décisions critiques.

---

## 11.4 P03 — Préserver la valeur diagnostique d'une activité évaluée

P03 demande notamment de :

- distinguer les notions attestées des notions non attestées nécessaires à la réussite ;
- limiter à une notion le budget de nouveauté d'une activité évaluée ;
- refuser, découper ou échafauder une activité qui empile plusieurs nouveautés non attestées ;
- ne pas confondre nouvelle tâche et nouvelle notion ;
- limiter la conclusion à ce que la réussite permet réellement d'identifier.

Le cœur confirmatoire est NOY004 :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

NOY006 renforce également la dimension « portée de la preuve ».

La conclusion est forte :

> **P03 est fortement supportée par la campagne et constitue l'un des apports différentiels les plus nets de V2.**

Une limite demeure : la batterie confirmatoire actuelle ne reproduit pas directement le faux positif historique « nouvelle tâche / nouveau vocabulaire ≠ nouvelle notion ». Le résultat favorable sur P03 ne doit donc pas être étendu à ce cas précis sans test dédié.

---

## 11.5 P04 — Aligner objectif, tâche, production, critères, preuve et conclusion

P04 impose la cohérence de la chaîne :

```text
objectif
→ tâche
→ production ou performance observable
→ critères
→ preuve
→ conclusion
```

NOY005 produit :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Le skill maintient l'alignement entre ce qui est demandé, ce qui est réellement produit et ce que cette production permet de conclure.

La conclusion est nette :

> **P04 est fortement supportée expérimentalement avec un contraste reproductible entre les deux conditions.**

---

## 11.6 G05 — Ne pas inventer de notation arbitraire

G05 précise qu'une évaluation n'implique pas nécessairement une note et qu'aucun barème arbitraire ne doit être créé spontanément lorsqu'il n'est ni fourni ni demandé.

NOY008 donne :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Ce résultat est particulièrement important dans l'histoire du projet.

En V1, la tendance du modèle sans skill à produire spontanément notes, points, bonus et seuils avait été identifiée **post hoc**.

En V2, cette observation a été transformée en scénario confirmatoire pré-spécifié.

Le résultat est donc plus solide méthodologiquement :

> **G05 reçoit un contraste différentiel net et reproductible dans la batterie V2.**

---

## 11.7 G06 et contrats propres à l'architecture V2

### G06 — Préserver la valeur de l'évaluation avant production

NOY011 :

```text
avec skill : PASS / PASS
```

Le candidat maintient la séparation entre :

```text
critères accessibles à l'apprenant
et
solution / correction / indices décisifs réservés au moment approprié
```

La conformité est démontrée dans les deux répétitions.

Mais l'absence de condition B′ interdit de conclure à un effet causal du skill par rapport au modèle nu.

### Architecture Activité / gabarits

NOY009 et NOY012 :

```text
PASS / PASS
PASS / PASS
```

Ils confirment notamment que :

- `Activité` constitue le socle commun ;
- les gabarits spécialisés sont des formes d'Activité et non des niveaux concurrents de la granularité ;
- l'architecture attendue est correctement représentée.

### Modalités

NOY010 :

```text
PASS / PASS
```

Le candidat ne transforme pas :

```text
synchrone / asynchrone
```

et :

```text
présentiel / distanciel
```

en règles rigides déterminant automatiquement le gabarit ou la granularité.

### Conclusion

> **Les contrats propres à la V2 effectivement couverts par NOY009 à NOY012 sont conformes dans toutes les répétitions prévues.**

Ils doivent cependant être présentés comme des **tests de conformité du candidat**, et non comme des preuves d'utilité différentielle, puisqu'aucun témoin sans skill n'est prévu.

---

## 11.8 Ce que la campagne ne démontre pas

La promesse distingue explicitement la promesse différentielle principale, les garanties de fonctionnement et les qualités d'architecture.

Cette distinction doit être conservée dans la conclusion expérimentale.

Les garanties suivantes ne disposent pas d'un scénario confirmatoire spécifique dans la batterie V2 :

- **G01 — ne pas inventer un état ou une persistance absente** ;
- **G02 — ne pas arbitrer silencieusement une contradiction documentaire pertinente** ;
- **G03 — ne pas transformer les paliers cognitifs en barrières absolues** ;
- **G04 — respecter le périmètre demandé**.

Le rapport ne les considère donc :

- ni comme échouées ;
- ni comme validées expérimentalement par cette campagne.

Elles restent des exigences du candidat pouvant être couvertes par d'autres tests de non-régression ou par une campagne ultérieure.

La même prudence vaut pour les autres qualités attendues hors promesse différentielle : posture professionnelle, ancrage concret, stabilité générale des formats, usage pertinent des référentiels ou adaptation du vocabulaire.

---

## 11.9 Bilan par rapport à la promesse centrale

La campagne permet finalement de distinguer quatre formes d'apport.

| Forme d'apport | Scénarios représentatifs |
|---|---|
| **Le skill fait apparaître ou maintient un garde-fou que le modèle nu ne maintient pas** | NOY004, NOY005, NOY006, NOY007, NOY008 |
| **Le skill stabilise un garde-fou que le modèle nu sait parfois produire** | NOY003 |
| **Le comportement recherché existe déjà sans skill** | NOY002 |
| **Le skill améliore nettement le comportement mais ne le stabilise pas encore parfaitement** | NOY001 |

Cette lecture est plus fidèle à la promesse que l'opposition simpliste :

```text
avec skill = bon
sans skill = mauvais
```

Le résultat central de V2 est plutôt :

> **Le skill apporte une discipline comportementale ciblée : il rend plus fiables plusieurs décisions pédagogiques critiques lorsque le modèle de base peut produire une réponse plausible mais insuffisamment diagnostique.**

Il ne remplace pas les capacités générales du modèle et n'est pas nécessaire à toute bonne décision.

Cette conclusion correspond directement au critère comportemental central de la V2 : une information pertinente doit modifier la décision lorsqu'elle devrait réellement modifier l'apprentissage ou l'évaluation.


# 12. Limites méthodologiques

Les résultats doivent être interprétés avec plusieurs limites.

## 12.1 Taille et périmètre de la batterie

La V2 comporte douze scénarios, dont huit seulement sont comparatifs A/B′.

La campagne est conçue comme une validation ciblée d'invariants, pas comme une mesure générale de « qualité pédagogique ».

## 12.2 Un seul runtime principal

La campagne utilise :

```text
Claude Code 2.1.232
claude-sonnet-5
effort medium
```

Les résultats ne démontrent pas que les mêmes écarts quantitatifs ou la même consommation de tokens seraient reproduits avec un autre modèle ou un autre runtime.

## 12.3 Périmètre métier limité

Les scénarios utilisent principalement :

- un développeur web/PHP comme apprenant ;
- un persona de formateur FPA ;
- des contenus liés au développement et à l'ingénierie pédagogique.

La campagne ne démontre donc pas expérimentalement une généricité inter-métiers complète.

## 12.4 NOY009 à NOY012 sans témoin

Ces scénarios testent des contrats propres au skill et sont volontairement A-only.

Ils établissent une conformité du candidat, pas un effet causal par rapport au modèle sans skill.

## 12.5 Un INDÉTERMINÉ de base

`NOY002` sans skill R2 reste `INDÉTERMINÉ` parce que la réponse décisive n'est pas observable dans la trajectoire.

Le R3 PASS apporte une observation supplémentaire mais ne réécrit pas ce résultat.

## 12.6 R3 non aveugles et scoring humain

Les R3 ont été déclenchés après désaveuglement conformément à la procédure prévue.

Leur scoring officiel est humain uniquement, à la suite de la décision méthodologique prise après mise en évidence d'un risque de sur-interprétation de NOY001 par un scoreur IA.

Cette adaptation est documentée et gelée, mais elle signifie que les R3 n'ont pas le même niveau d'indépendance que le double scoring aveugle des 40 runs de base.

Leur rôle doit donc rester celui prévu par le plan : **caractériser la stabilité**, non remplacer la base.

## 12.7 Interactions opérateur pendant les R3

Sur `R3-NOY002-BP`, des recherches globales `find /` ont été refusées pour préserver l'isolation du workspace ; des relances neutres ont permis de rendre la décision pédagogique observable.

Sur `R3-NOY003-BP`, lorsque l'agent a demandé à l'opérateur de choisir entre plusieurs interprétations du palier, l'opérateur a utilisé la réponse neutre prévue par la procédure :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Ces interventions sont compatibles avec la règle opérateur mais doivent rester présentes dans la trace d'audit.

## 12.8 Coût de tokens

Le ratio de `2,49×` est une observation de cette campagne.

Il ne constitue ni :

- une constante universelle du skill ;
- une estimation financière ;
- une mesure de latence ;
- une mesure de quota Claude.

## 12.9 Point historique non directement re-testé

La V1 avait identifié un risque de sur-détection de nouveauté sur T26.

La batterie confirmatoire V2 actuelle teste le budget de nouveauté lorsque plusieurs notions sont réellement non attestées, mais elle ne reproduit pas directement le faux positif historique « nouvelle tâche / nouveau vocabulaire ≠ nouvelle notion ».

Le présent rapport ne prétend donc pas démontrer expérimentalement la disparition de ce risque précis.

---

# 13. Enseignements méthodologiques

## 13.1 L'accord des scoreurs s'est fortement amélioré

La V2 obtient :

```text
37/40 accords
92,5 % d'accord brut
κ = 0,8435
```

Les oracles resserrés produisent donc globalement des décisions beaucoup plus reproductibles.

## 13.2 Un oracle peut être correct et malgré tout être sur-interprété

Le cas R3-NOY001-A rappelle qu'un scoreur peut transformer une formulation graduée :

```text
avant exposition substantielle
```

en règle plus dure :

```text
aucun contenu avant la réponse
```

La leçon n'est pas nécessairement d'allonger encore tous les oracles.

Elle est aussi de maintenir une discipline de scoring :

> **juger ce que l'oracle exige réellement, sans ajouter une règle implicite plus stricte.**

## 13.3 Une répétition conditionnelle ne doit pas devenir un vote qui efface l'historique

Les R3 ont rempli leur fonction parce que les résultats initiaux ont été conservés.

La lecture :

```text
FAIL / PASS / PASS
```

est plus informative qu'un simple :

```text
PASS à la majorité
```

Elle montre simultanément le comportement dominant et l'existence d'une instabilité.

## 13.4 L'efficience doit être mesurée séparément de l'efficacité

La V2 apporte une amélioration importante du dispositif expérimental : les tokens sont instrumentés dès le plan.

Il devient donc possible de dire simultanément :

```text
le skill améliore ou stabilise certains comportements
ET
le skill consomme davantage de contexte
```

sans transformer le coût en verdict pédagogique.

---

# 14. Décision au regard du plan V2

Le plan définit quatre critères principaux pour considérer le candidat comme stabilisable.

## Critère 1 — NOY009 à NOY012 stables en PASS

**SATISFAIT**

```text
8 PASS / 8
```

## Critère 2 — aucun défaut bloquant établi sur NOY001 à NOY008

**SATISFAIT**

Un FAIL existe avec skill sur NOY001, mais il n'est pas reproductible :

```text
FAIL / PASS / PASS(R3)
```

Il constitue une instabilité à surveiller, pas un défaut bloquant établi.

## Critère 3 — instabilités localisées et interprétables

**SATISFAIT**

Trois cellules seulement sur vingt ont déclenché R3 :

- NOY001 avec skill ;
- NOY002 sans skill ;
- NOY003 sans skill.

Les trois R3 sont PASS et les causes des divergences sont interprétables.

## Critère 4 — intégrité du candidat, des scénarios et du protocole préservée

**SATISFAIT pour la base expérimentale**

Les 40 verdicts de base ont été gelés avant désaveuglement et les R3 sont conservés comme couche supplémentaire distincte.

La modification de méthode de scoring des R3 est explicitement documentée plutôt que masquée ou appliquée rétroactivement à la base.

---

# 15. Conclusion générale

La V2 confirme et précise le résultat central de la V1, mais elle permet désormais de le formuler directement par rapport à sa **promesse fonctionnelle**.

Le candidat ne promet pas de rendre toute réponse pédagogique meilleure. Il promet de modifier ou de stabiliser certaines décisions lorsque le point de départ, la nature de la preuve, la valeur diagnostique ou l'alignement devraient effectivement changer ce que l'agent propose ou conclut.

Sur ce périmètre :

- **P02, P03 et P04 sont fortement supportées par des résultats convergents** ;
- **P01 est supportée et bénéficie d'un contraste favorable au skill, mais reste imparfaitement stable** ;
- **G05 reçoit un résultat confirmatoire différentiel particulièrement net** ;
- **G06 et les contrats d'architecture testés sont conformes dans toutes les répétitions prévues** ;
- **G01 à G04 ne sont pas revalidées spécifiquement par cette batterie et ne sont donc pas revendiquées comme démontrées par la V2**.

La campagne montre également que l'apport du skill n'est pas uniforme.

Sur certains scénarios, le skill fait apparaître ou maintient un garde-fou que le modèle sans skill ne maintient pas de manière reproductible :

- budget de nouveauté ;
- alignement pédagogique ;
- portée exacte des preuves ;
- résistance à l'auto-attestation ;
- absence de notation arbitraire.

Sur `NOY003`, le modèle sans skill sait parfois produire le bon raisonnement ; le skill apporte surtout de la **stabilité**.

Sur `NOY002`, le comportement recherché est également disponible sans skill lorsque toute la trajectoire est observable. Ce résultat nul est informatif et cohérent avec une promesse qui ne revendique pas une supériorité universelle.

Le principal point de vigilance comportemental reste `NOY001` :

```text
avec skill : FAIL / PASS / PASS(R3)
sans skill : FAIL / FAIL
```

Le skill améliore nettement la situation, mais le comportement n'est pas parfaitement stable. Ce scénario doit rester prioritaire dans la non-régression future.

Les contrats propres à l'architecture V2 sont stables :

```text
NOY009 à NOY012
8 PASS / 8
```

Le principal coût mesuré est l'efficience :

> **sur les 16 paires comparables, le skill consomme environ 2,49× le volume de tokens de la condition sans skill, soit +149,3 %.**

Ce coût est principalement lié à l'entrée et à la lecture de contexte/cache. Il est substantiel en relatif, mais l'observation pratique du quota pendant la campagne indique qu'il reste supportable pour ce type d'usage et de volume d'exécution.

La conclusion expérimentale doit donc être lue comme un compromis explicite :

```text
davantage de contexte et de calcul
en échange
de garde-fous pédagogiques plus fiables
sur les décisions que la V2 revendique précisément
```

### Verdict expérimental

> **V2 : CANDIDAT STABILISABLE**

Ce verdict signifie que les critères expérimentaux pré-définis sont satisfaits **sur le périmètre effectivement testé** et que la promesse fonctionnelle centrale est globalement supportée.

Il ne signifie pas :

- que chaque comportement est parfaitement stable ;
- que toutes les garanties du candidat ont été revalidées dans cette batterie ;
- que le skill est nécessaire à toute bonne décision pédagogique ;
- que sa généricité inter-métiers est démontrée ;
- que le surcoût de tokens est négligeable.

Une promotion vers `stable/` et `dist/stable/` est donc **justifiable sur la base des résultats expérimentaux**, mais elle reste une opération explicite distincte, avec son propre gel et sa propre traçabilité.

# 16. Traçabilité principale

Artefacts de référence de la campagne :

```text
PAQUET_OPERATEUR_VALIDATION_V2_40_RUNS_FROZEN_2BLOCS_2026-08-21/
  STATUT_GEL.md
  ETAT_AUTORITATIF.md
  PLAN_EXPERIMENTAL.md
  DECISION_GO_STOP.md
  RUNS.csv
  ORACLES_SCOREUR/NOY001.md ... NOY012.md
```

Scoring de base :

```text
execution/scoring/scoreurs/S1/resultats/VERDICTS_SCOREUR_V2_BASE_40_S1.tsv
execution/scoring/scoreurs/S2/resultats/VERDICTS_SCOREUR_V2_BASE_40_S2.tsv
execution/scoring/comparaison/COMPARAISON_INTER_SCOREURS_V2_BASE_40.txt
execution/scoring/adjudication/resultats/ADJUDICATION_V2_BASE_3.tsv
execution/scoring/resultats_figes/VERDICTS_FINAUX_AVEUGLES_V2_BASE_40.tsv
execution/scoring/desaveuglement/VERDICTS_DESAVEUGLES_V2_BASE_40.tsv
execution/scoring/desaveuglement/DECISION_R3_V2_BASE_40.md
```

R3 :

```text
DECISION_SCORING_HUMAIN_R3_V2_2026-08-21.md
execution/scoring/r3/VERDICTS_HUMAINS_R3_V2_2026-08-21.md
execution/scoring/r3/VERDICTS_HUMAINS_R3_V2_2026-08-21.tsv
execution/scoring/r3/SYNTHESE_FINALE_APRES_R3_V2_2026-08-21.md
execution/scoring/r3/SHA256_R3_V2_2026-08-21.txt
```

Tokens :

```text
execution/scoring/TOKENS_V2_BASE40.tsv
```

Le présent rapport ne modifie aucun de ces résultats ; il en constitue la synthèse interprétative finale.
