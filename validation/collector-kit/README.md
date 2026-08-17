# Collector Kit

`collector-kit` est un outil de **collecte, structuration et archivage de runs de test comportemental** exécutés avec Claude Code.

Il est conçu pour être réutilisable avec **n’importe quel skill**. Il ne dépend ni du domaine fonctionnel testé, ni d’une version particulière du skill.

Son rôle est volontairement limité : conserver une trace exploitable de ce qui s’est réellement passé pendant un run afin de pouvoir ensuite :

- vérifier sa validité technique ;
- examiner la trajectoire produite ;
- comparer plusieurs conditions expérimentales ;
- appliquer ultérieurement un oracle ;
- transmettre le run à un scoreur ;
- archiver une campagne.

> **Le collector collecte. Il ne score pas.**

---

## Conditions expérimentales

La convention utilisée dans les campagnes comparatives est :

- **A — avec skill**
- **B′ — sans skill**

Les deux environnements de travail sont actuellement :

```text
/projets/skill/tests/tests_avec_skill_A
/projets/skill/tests/tests_sans_skill_B
```

> Le suffixe `_B` du répertoire `tests_sans_skill_B` est uniquement une convention de nommage des fichiers et répertoires.
> Dans le protocole expérimental, la condition reste notée **B′**.

Dans l’interface en ligne de commande du collector, ces deux conditions sont représentées techniquement par :

```text
A  → --condition skill
B′ → --condition no-skill
```

Cette différence entre **notation expérimentale** et **valeur CLI** est volontaire.

---

## Organisation de l’espace de test

Les données expérimentales ne sont pas stockées dans `collector-kit`.

L’espace de travail actif est organisé sous :

```text
/projets/skill/tests/
├── tests_avec_skill_A/
├── tests_sans_skill_B/
├── prompts/
├── runs/
└── archives/
```

- `tests_avec_skill_A/` : environnement de la condition A ;
- `tests_sans_skill_B/` : environnement physique de la condition B′ ;
- `prompts/` : prompts de la campagne en cours ;
- `runs/` : runs collectés de la campagne en cours ;
- `archives/` : campagnes terminées et figées.

L’organisation et l’archivage des campagnes sont documentés dans :

```text
/projets/skill/tests/README.md
```

Le collector reste un **outil d’instrumentation**, séparé des données qu’il produit.

---

## Structure du kit

```text
validation/
└── collector-kit/
    ├── README.md
    ├── collect_run.py
    ├── analyse_jsonl.py
    ├── commands/
    │   ├── bloc1.md
    │   └── bloc2.md
    └── tests/
        ├── README.md
        ├── test_analyse_jsonl.py
        ├── test_collect_run.py
        ├── test_interactions.py
        └── fixtures/
```

---

## Un run en deux blocs

L’exécution opérateur d’un run est volontairement réduite à **deux blocs de commandes**.

### Bloc 1 — préparation et lancement

Le premier bloc :

1. désactive la mémoire automatique ;
2. crée le fichier contenant le prompt exact ;
3. place l’opérateur dans l’environnement A ou B′ ;
4. initialise la collecte ;
5. lance l’agent testé via Claude Code.

Voir :

[`commands/bloc1.md`](commands/bloc1.md)

### Bloc 2 — collecte et archivage du run

Le second bloc est exécuté **après avoir quitté Claude Code avec `exit`**.

Il :

1. finalise la collecte ;
2. produit les artefacts du run ;
3. crée une archive ZIP du run.

Voir :

[`commands/bloc2.md`](commands/bloc2.md)

---

## Identifiants

Chaque exécution reçoit un `RUN-ID` unique :

```text
RUN-001
RUN-002
RUN-003
```

Chaque run est également associé à un `SCENARIO-ID` :

```text
SRC-1
CTX-2
NR-01
```

Le collector ne définit pas la nomenclature des scénarios. Celle-ci appartient au protocole de la campagne.

Il faut distinguer :

```text
SCENARIO-ID → scénario fonctionnel stable
RUN-ID      → exécution particulière de ce scénario
```

Par exemple :

```text
RUN-001 → SRC-1 → A
RUN-002 → SRC-1 → B′
```

---

## Nom du skill

Le collector est générique : le nom du skill testé n’est pas codé en dur.

Il doit être fourni explicitement avec :

```text
--skill-name NOM-DU-SKILL
```

Cela permet notamment de vérifier l’observabilité de l’invocation du skill attendu dans les traces.

---

## Prompts gelés

Pour un test comparatif A/B′, le **même prompt exact** doit être utilisé dans les deux conditions.

Les prompts actifs sont conservés sous :

```text
/projets/skill/tests/prompts/
```

Par exemple :

```text
/projets/skill/tests/prompts/RUN-001.txt
```

La conservation du prompt réellement exécuté permet de vérifier ultérieurement que le stimulus correspond bien au scénario prévu.

---

## Mémoire automatique

Les runs sont lancés avec :

```bash
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

Cette règle vise à réduire les contaminations entre exécutions et à éviter qu’un résultat dépende d’une mémoire automatique issue d’un run précédent.

---

## `AskUserQuestion`

Lorsqu’un scénario ne fournit pas l’information demandée par `AskUserQuestion`, l’opérateur ne doit pas inventer de réponse.

La règle opératoire est :

> **faire `Esc` sans injecter d’information supplémentaire.**

Le comportement observé ensuite — y compris l’arrêt éventuel de la trajectoire — appartient au résultat expérimental.

L’opérateur ne doit pas corriger manuellement le comportement de l’agent pendant le run.

---

## Ce que collecte le kit

Selon la trace disponible, un dossier de run peut notamment contenir :

- `metadata.json` ;
- `trajectory.md` ;
- la trace de session ;
- les outils invoqués ;
- les références consultées ;
- les informations nécessaires à la validation technique ;
- les empreintes SHA-256 des artefacts.

Les résultats actifs sont stockés sous :

```text
/projets/skill/tests/runs/RUN-ID/
```

et peuvent être archivés individuellement sous :

```text
/projets/skill/tests/runs/RUN-ID.zip
```

---

## Collecte ≠ scoring

Une campagne distingue au minimum trois étapes.

### 1. Exécution

L’agent reçoit le stimulus prévu par le scénario.

### 2. Collecte

Le collector conserve ce qui s’est réellement passé.

### 3. Scoring

Un scoreur confronte ensuite la trajectoire à l’oracle gelé du scénario.

> **La collecte doit préserver le résultat brut sans essayer de le corriger ni de décider de sa valeur fonctionnelle.**

---

## Validation technique d’un run

Avant le scoring fonctionnel, on peut notamment vérifier :

- le bon `RUN-ID` ;
- le bon `SCENARIO-ID` ;
- la condition correcte : A ou B′ ;
- le bon environnement d’exécution ;
- la désactivation de la mémoire automatique ;
- le prompt exact ;
- le nom du skill attendu ;
- l’éventuelle invocation du skill ;
- les outils et références observés ;
- les éventuels `AskUserQuestion` ;
- le bon fonctionnement de la collecte ;
- l’intégrité des artefacts.

Un **run techniquement invalide** ne doit pas être confondu avec un **FAIL fonctionnel**.

---

## Tests A/B′

Dans un test comparatif :

```text
RUN-001 → scénario X → A — avec skill
RUN-002 → scénario X → B′ — sans skill
```

le prompt et l’oracle sont identiques.

La question n’est pas seulement :

> « La réponse avec skill est-elle correcte ? »

mais :

> **« Le skill modifie-t-il réellement le comportement ciblé, et dans quel sens ? »**

Le collector ne définit pas cette stratégie : il fournit seulement les artefacts permettant de l’appliquer.

---

## Tests de non-régression

Le même outil peut servir à rejouer des scénarios protégeant des comportements déjà établis.

Le principe reste :

```text
scénario gelé
+
prompt gelé
+
oracle gelé
+
nouvelle exécution
```

Le collector conserve la nouvelle trajectoire ; le protocole décide ensuite comment la comparer à l’invariant attendu.

---

## Ce que le collector ne fait pas

`collector-kit` ne définit pas :

- l’objectif fonctionnel ;
- le scénario ;
- le prompt ;
- l’oracle ;
- les alternatives acceptables ;
- le verdict ;
- la stratégie A/B′ ;
- les règles de non-régression ;
- la décision de conserver ou non une modification du skill.

Ces éléments appartiennent au **protocole expérimental**.

---

## Tests du collector

Les tests automatisés du kit se trouvent dans :

```text
validation/collector-kit/tests/
```

Ils valident le fonctionnement de l’instrumentation elle-même, pas les comportements pédagogiques ou fonctionnels d’un skill.

Voir :

[`tests/README.md`](tests/README.md)

---

## Principe directeur

> **Capturer proprement ce qui s’est passé pendant un run, sans décider à la place du protocole expérimental de ce que le résultat signifie.**
