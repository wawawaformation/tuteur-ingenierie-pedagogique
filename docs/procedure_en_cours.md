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

## 6. Gel actuel

Deux zones sont gelées avant préparation des runs :

```text
en_cours/
validation/v1/tests/
```

Manifestes :

```text
validation/v1/manifest/EN_COURS.sha256
validation/v1/manifest/TESTS.sha256
```

Le gel est matérialisé dans Git par le commit et le tag créés au moment du gel.

Avant toute exécution, vérifier :

```bash
sha256sum -c validation/v1/manifest/EN_COURS.sha256
sha256sum -c validation/v1/manifest/TESTS.sha256
```

Les deux contrôles doivent être entièrement `OK`.

---

## 7. Règle de modification après gel

À partir du gel :

- ne pas modifier `en_cours/` pendant les runs ;
- ne pas modifier les fiches de `validation/v1/tests/` pendant les runs ;
- ne pas adapter un test parce qu'un résultat avec skill est défavorable ;
- ne pas adapter un test parce que la condition sans skill réussit ;
- conserver les trajectoires observées telles quelles.

Si une modification du candidat ou d'un test devient nécessaire :

1. arrêter la série concernée ;
2. documenter la raison ;
3. effectuer la modification ;
4. recréer les manifestes ;
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

On évite donc, au départ :

- les nouveaux oracles plus stricts ;
- les familles de scénarios dérivées ;
- les métamorphismes complexes ;
- les conclusions statistiques prématurées.

---

## 9. Statut du projet avant planification

À ce stade :

- ancien projet : **archivé** ;
- nouveau projet : **créé et poussé sur GitHub** ;
- candidat `en_cours/` : **gelé** ;
- tests `validation/v1/tests/` : **gelés** ;
- manifestes SHA-256 : **créés** ;
- jeu historique T01–T30 : **conservé comme référence** ;
- runs de cette nouvelle reprise : **non lancés**.

---

## 10. Plan d'exécution

Le plan d'exécution est préparé hors des zones gelées.

Il fixe notamment :

- l'identifiant du run ;
- le test concerné ;
- la condition avec skill / sans skill ;
- la répétition ;
- l'ordre d'exécution ;
- le statut initial du run.

Aucun run ne doit être lancé avant vérification et gel du plan.

---

## 11. Plan de répétitions

La campagne V1 utilise les 30 tests historiques `T01` à `T30`.

Chaque test est exécuté dans deux conditions :

- avec skill ;
- sans skill.

Pour chaque couple `test × condition`, deux répétitions indépendantes sont
exécutées initialement.

Volume initial :

```text
30 tests
× 2 conditions
× 2 répétitions
= 120 runs
```

### Troisième répétition conditionnelle

Si les verdicts des répétitions 1 et 2 d'un même couple `test × condition`
diffèrent, une troisième répétition est obligatoire.

Les troisièmes répétitions sont pré-déclarées dans :

```text
validation/v1/plan/RUNS_CONDITIONNELS.csv
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

## 12. Fichiers du plan

Le plan d'exécution courant est défini par :

```text
validation/v1/plan/RUNS.csv
validation/v1/plan/RUNS_CONDITIONNELS.csv
validation/v1/plan/REGLE_REPETITIONS.md
validation/v1/plan/RANDOMISATION.txt
```

`RUNS.csv` contient les 120 runs initiaux.

`RUNS_CONDITIONNELS.csv` contient les 60 troisièmes répétitions potentielles.

Aucun run de cette campagne ne doit être créé librement en dehors de ces règles.

---

## 13. Statut actuel

À ce stade :

- `en_cours/` : **GELÉ** ;
- `validation/v1/tests/` : **GELÉ** ;
- plan des runs : **PRÊT** ;
- runs lancés : **0**.

La prochaine étape est le gel du plan puis la préparation du protocole
opérateur.
