# Tests du Collector Kit

Ce dossier contient les **tests automatisés de l’instrumentation** `collector-kit`.

Ils vérifient le comportement de :

- `collect_run.py` ;
- `analyse_jsonl.py` ;
- la détection de signaux observables dans les traces ;
- les interactions particulières comme `AskUserQuestion` ;
- les cas limites couverts par les fixtures JSONL.

Ces tests ne scorent **aucun comportement fonctionnel d’un skill**.

Ils servent uniquement à vérifier que l’outil de collecte et d’analyse fonctionne comme attendu.

---

## Structure

```text
tests/
├── README.md
├── test_analyse_jsonl.py
├── test_collect_run.py
├── test_interactions.py
└── fixtures/
    ├── ask_user_question_answered.jsonl
    ├── ask_user_question_empty.jsonl
    ├── fichiers.jsonl
    ├── malformed.jsonl
    ├── outils_skill.jsonl
    ├── sans_observabilite_skill.jsonl
    ├── usage_conflit.jsonl
    ├── usage_duplique.jsonl
    └── usage_progressif.jsonl
```

---

## Lancer la suite complète

Depuis `validation/collector-kit/` :

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

La suite actuellement généralisée contient :

```text
51 tests
```

Tous doivent passer avant de considérer une modification du collector comme prête à être utilisée dans une campagne.

---

## Répartition des tests

### `test_analyse_jsonl.py`

Vérifie notamment l’analyse déterministe des traces JSONL :

- détection des outils ;
- observabilité de l’invocation d’un skill ;
- fichiers lus ;
- cas de traces malformées ;
- signaux d’usage du skill.

### `test_collect_run.py`

Vérifie notamment :

- l’initialisation d’un run ;
- les métadonnées ;
- les paramètres CLI ;
- le `skill-name` fourni explicitement ;
- la collecte et les artefacts attendus ;
- la cohérence avec `analyse_jsonl.py`.

### `test_interactions.py`

Vérifie les interactions qui peuvent modifier la lecture d’une trajectoire, notamment :

- `AskUserQuestion` sans réponse ;
- `AskUserQuestion` avec réponse ;
- les limites d’observabilité associées.

---

## Fixtures

Les fichiers de `fixtures/` sont des traces JSONL contrôlées utilisées uniquement pour tester l’instrumentation.

Le skill fictif utilisé dans les tests est nommé :

```text
example-skill
```

Ce nom est volontairement neutre afin que la suite de tests ne dépende d’aucun skill réel.

Les fixtures ne doivent pas être interprétées comme des runs de campagne.

---

## A/B′ et tests unitaires

La notation expérimentale :

- **A — avec skill**
- **B′ — sans skill**

appartient aux campagnes comportementales.

Les tests unitaires du collector ne cherchent pas à établir qu’un skill est meilleur dans une condition ou dans l’autre.

Ils vérifient seulement que l’instrumentation sait correctement enregistrer et analyser les informations nécessaires à ce type de protocole.

---

## Après une modification du collector

Après toute modification de :

- `collect_run.py` ;
- `analyse_jsonl.py` ;
- la logique d’observabilité ;
- la structure des métadonnées ;

relancer la suite complète :

```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
```

Une modification qui casse un test existant doit être expliquée et traitée avant utilisation du collector dans une nouvelle campagne.

---

## Ce dossier n’est pas l’archive des campagnes

Les runs réels, prompts de campagne et archives expérimentales ne doivent pas être stockés ici.

Ils appartiennent à l’espace de travail :

```text
/projets/skill/tests/
```

et sont documentés dans :

```text
/projets/skill/tests/README.md
```

Cette séparation évite de mélanger :

- **tests du collector** ;
- **tests comportementaux d’un skill** ;
- **résultats expérimentaux**.

---

## Principe directeur

> **Tester l’instrument de mesure séparément de ce que l’on cherche à mesurer.**
