# Procédure en cours — validation V1

## 1. Objet

Ce document décrit l'état courant du projet
`tuteur-ingenierie-pedagogique` et la procédure retenue pour reprendre la
validation sur une base simple et traçable.

Il sert de point de reprise pour les sessions ultérieures.

---

## 2. Reprise du projet

L'ancien projet complet a été conservé localement sous :

```text
/projets/skill/tuteur-ingenierie-pedagogique.back
```

Il contient l'historique des anciennes campagnes, protocoles, collectes,
analyses et expérimentations.

Le nouveau projet de travail est :

```text
/projets/skill/tuteur-ingenierie-pedagogique
```

La reprise a volontairement été faite sur une structure minimale afin de ne
pas réimporter immédiatement la complexité des anciens protocoles.

---

## 3. Candidat testé

Le candidat courant est contenu dans :

```text
en_cours/
```

Principe :

> `en_cours/` représente le candidat exact soumis aux tests.

Aucune modification du candidat ne doit avoir lieu pendant une série de runs
effectuée sous un même gel.

---

## 4. Source historique des tests V1

Le jeu historique complet V1 a été restauré directement depuis l'archive :

```text
validation/v1/jeu_de_tests_v1.md
```

Ce document contient les 30 tests historiques :

```text
T01 à T30
```

Il est conservé comme **source historique de référence**.

Il ne doit pas être réécrit pour durcir, assouplir ou moderniser
rétroactivement les anciens tests.

---

## 5. Tests retenus pour la reprise

Les fiches de travail sont contenues dans :

```text
validation/v1/tests/
```

Le corpus de reprise couvre les tests historiques :

```text
T01 à T30
```

### Principe de scoring

Pour cette reprise, les tests sont évalués à partir de leurs **attendus
historiques**.

On ne leur ajoute pas de nouvelles contraintes qui n'existaient pas dans la
fiche d'origine.

Exemple important : T18 demande de privilégier une question diagnostique avant
de déverser un cours complet. Il ne doit pas être transformé en un oracle plus
strict imposant qu'aucune phrase de cadrage ou hypothèse prudente ne puisse
précéder cette question.

Cette règle vise à éviter une dérive entre le test historique et une nouvelle
interprétation plus exigeante.

---

## 6. Gel runtime / opérateur

Le runtime et l'outillage opérateur utilisés pour la campagne sont gelés sur :

```text
commit : a132ef59e6010d7d264545f70f50233be22ca159
tag    : validation-v1-runtime-frozen
```

Les zones gelées ne doivent pas être modifiées pendant la campagne, notamment :

```text
en_cours/
validation/v1/tests/
validation/v1/plan/
validation/collector-kit/
validation/v1/operateur/
```

Les manifestes présents sous :

```text
validation/v1/manifest/
```

constituent les références d'intégrité associées au gel.

Le RETEX post-gel sur les interactions opérateur complète les consignes
d'exécution sans modifier rétroactivement les oracles historiques des tests.

---

## 7. Règle de modification après gel

À partir du gel :

- ne pas modifier `en_cours/` pendant les runs ;
- ne pas modifier les fiches de `validation/v1/tests/` pendant les runs ;
- ne pas modifier le plan, le collector ou les blocs opérateur gelés ;
- ne pas adapter un test parce qu'un résultat avec skill est défavorable ;
- ne pas adapter un test parce que la condition sans skill réussit ;
- conserver les trajectoires observées telles quelles.

Si une modification du candidat ou d'un test devient nécessaire pour une
future série :

1. arrêter la série concernée ;
2. documenter la raison ;
3. effectuer la modification ;
4. recréer les manifestes concernés ;
5. créer un nouveau commit de gel ;
6. identifier clairement la nouvelle série comme appartenant au nouveau gel.

---

## 8. Philosophie de la reprise

Cette reprise est volontairement plus simple que les campagnes précédentes.

Ordre retenu :

1. repartir des tests historiques déjà connus ;
2. conserver leurs formulations et attendus ;
3. exécuter les runs avec et sans skill ;
4. vérifier quels comportements historiques sont encore reproduits ;
5. analyser seulement ensuite les éventuels écarts ;
6. complexifier le protocole uniquement si cela devient nécessaire.

On évite donc :

- les nouveaux oracles plus stricts ;
- les familles de scénarios dérivées ;
- les métamorphismes complexes ;
- les conclusions statistiques prématurées.

---

## 9. Plan d'exécution

Le plan initial est défini par :

```text
validation/v1/plan/RUNS.csv
```

Il contient :

```text
30 tests
× 2 conditions
× 2 répétitions
= 120 runs initiaux
```

La série initiale correspond à :

```text
RUN-001 .. RUN-120
```

Elle est désormais **entièrement exécutée**.

Il n'existe donc plus de prochain run à lancer dans `RUNS.csv`.

---

## 10. Racine runtime de la campagne

La campagne V1 a été exécutée exclusivement dans :

```text
/projets/skill/tests/validation_v1_2026-08-17
```

avec :

```text
/projets/skill/tests/validation_v1_2026-08-17/prompts/
/projets/skill/tests/validation_v1_2026-08-17/runs/
/projets/skill/tests/validation_v1_2026-08-17/tests_avec_skill_A/
/projets/skill/tests/validation_v1_2026-08-17/tests_sans_skill_B/
```

Les anciens artefacts présents ailleurs sous `/projets/skill/tests/` ne sont
pas utilisés comme résultats de cette campagne.

---

## 11. Plan de répétitions

Chaque test `T01` à `T30` est exécuté dans deux conditions :

- avec skill ;
- sans skill.

Pour chaque couple `test × condition`, deux répétitions indépendantes ont été
exécutées initialement.

### Troisième répétition conditionnelle

Si les verdicts des répétitions 1 et 2 d'un même couple `test × condition`
diffèrent, une troisième répétition est obligatoire.

Les troisièmes répétitions sont pré-déclarées dans :

```text
validation/v1/plan/RUNS_CONDITIONNELS.csv
```

Elles correspondent à :

```text
RUN-121 .. RUN-180
```

Elles ne sont déclenchées qu'en cas de désaccord des deux verdicts initiaux.

Il n'existe pas de quatrième répétition comportementale.

Volume conditionnel maximal :

```text
30 tests
× 2 conditions
× 1 répétition conditionnelle
= 60 runs
```

Volume maximal de la campagne :

```text
180 runs
```

### Synthèse d'un couple test × condition

- mêmes verdicts sur les deux premières répétitions : concordance `2/2` ;
- désaccord initial : troisième répétition ;
- majorité après trois runs : résultat `2/3`, avec instabilité explicitement
  conservée ;
- trois verdicts différents : résultat non conclusif.

Un rerun dû à une invalidité purement technique ne compte pas comme répétition
comportementale.

La troisième répétition ne doit jamais être déclenchée parce qu'un résultat
favorise ou défavorise le skill.

---

## 12. Reruns techniques de la série initiale

Quatre exécutions initiales ont été remplacées à la suite d'une invalidité
technique réelle :

```text
RUN-026 -> RUN-026-R1
RUN-053 -> RUN-053-R1
RUN-091 -> RUN-091-R1
RUN-102 -> RUN-102-R1
```

Les exécutions originales invalides sont conservées pour audit.

Les quatre reruns ci-dessus sont les remplacements officiels dans le corpus
comportemental.

Ils ne constituent pas des répétitions comportementales supplémentaires.

---

## 13. Collectes gelées

La série initiale terminée contient :

```text
120 runs initiaux
4 reruns techniques
124 collectes conservées
120 trajectoires dans le corpus officiel
```

Le contrôle final avant gel a conclu :

```text
RESULTAT=PASS
erreurs=0
pending=0
PRET_POUR_GEL=OUI
```

Les contrôles d'intégrité du paquet gelé ont confirmé :

```text
124/124 collectes : SHA internes valides
métadonnées        : cohérentes avec le plan
```

Ces contrôles portent uniquement sur la validité technique et l'intégrité des
collectes. Ils ne constituent pas un scoring comportemental.

---

## 14. Archive de preuve

L'archive gelée des collectes est conservée sous :

```text
validation/v1/archives/collectes/
```

Fichiers :

```text
VALIDATION_V1_COLLECTES_FROZEN_2026-08-18.zip
VALIDATION_V1_COLLECTES_FROZEN_2026-08-18.sha256
```

SHA-256 du ZIP :

```text
c5a78127e076e4a8fa62e0babc56ecae5bbfb9e7dd1ea5008b3d2dd47a2623ee
```

Le ZIP constitue l'archive de preuve des collectes techniquement validées et
gelées. Il ne doit pas être modifié après gel.

---

## 15. Séparation exécution / scoring

La série initiale est terminée.

La validité technique d'un run est distincte de son verdict comportemental.

Aucun run ne doit être relancé parce que son résultat est :

- mauvais ;
- surprenant ;
- défavorable au skill ;
- favorable au skill.

Le scoring comportemental doit être réalisé séparément à partir des
trajectoires officielles et des oracles historiques `T01` à `T30`.

Les runs conditionnels ne sont déclenchés qu'après comparaison des verdicts des
deux répétitions initiales de chaque couple `test × condition`.

---

## 16. Fichiers du plan

Le plan de campagne est défini par :

```text
validation/v1/plan/RUNS.csv
validation/v1/plan/RUNS_CONDITIONNELS.csv
validation/v1/plan/REGLE_REPETITIONS.md
validation/v1/plan/RANDOMISATION.txt
```

`RUNS.csv` contient les 120 runs initiaux désormais exécutés.

`RUNS_CONDITIONNELS.csv` contient les 60 troisièmes répétitions potentielles.

Aucun run de cette campagne ne doit être créé librement en dehors de ces
règles.

---

## 17. Statut actuel

À ce stade :

```text
candidat en_cours/                    : GELÉ
tests historiques T01-T30             : GELÉS
plan expérimental                     : GELÉ
runtime / opérateur                   : GELÉ
RUN-001 .. RUN-120                    : TERMINÉS
reruns techniques officiels           : 4
collectes conservées                  : 124
corpus comportemental officiel        : 120 trajectoires
contrôle technique final              : PASS
archive gelée des collectes           : PRÉSENTE
runs conditionnels RUN-121 .. RUN-180 : NON EXÉCUTÉS
```

La série initiale de la campagne V1 est donc :

```text
TERMINÉE — TECHNIQUEMENT VALIDÉE — GELÉE
```

### Prochaine étape

La prochaine étape est le **scoring comportemental séparé des deux répétitions
initiales** à partir des oracles historiques.

Ce scoring déterminera, conformément à `REGLE_REPETITIONS.md`, quels couples
`test × condition` nécessitent éventuellement leur troisième répétition
conditionnelle.
