# État documenté — campagne de validation V1

Date : 2026-08-17

Ce document consigne l’état courant de la reprise de la campagne V1 du projet
`tuteur-ingenierie-pedagogique`, après restauration des briques opératoires
éprouvées et avant lancement du premier run comportemental.

---

## 1. Principe de la reprise

La reprise s’appuie sur les tests historiques V1 sans durcir leurs critères.

Règles retenues :

- ne pas réinterpréter les anciens oracles ;
- ne pas ajouter de critères plus stricts ;
- ne pas modifier le candidat pendant la campagne ;
- ne pas scorer au fil de l’eau ;
- conserver la mécanique opérateur qui avait déjà fonctionné ;
- isoler chaque run dans un workspace neuf ;
- conserver les artefacts techniques pour audit ultérieur.

---

## 2. Candidat gelé

Le candidat testé est :

```text
en_cours/
```

Son intégrité est contrôlée par :

```text
validation/v1/manifest/EN_COURS.sha256
```

Le contrôle d’intégrité réalisé après restauration de l’outillage est passé
sans erreur.

Le candidat ne doit pas être modifié pendant cette campagne.

---

## 3. Tests historiques gelés

Le corpus de référence comprend :

```text
T01 à T30
```

Les fiches sont situées dans :

```text
validation/v1/tests/
```

Leur intégrité est contrôlée par :

```text
validation/v1/manifest/TESTS.sha256
```

Le contrôle réalisé après restauration de l’outillage a confirmé que les
30 fiches sont intactes.

Ces fiches restent l’autorité pour :

- le `Prompt exact` ;
- les attendus ;
- les critères de FAIL ;
- les éventuelles interactions explicitement prévues par un test.

Aucun oracle plus strict ne doit être substitué à ceux des fiches historiques.

---

## 4. Plan expérimental

Le plan initial est déjà matérialisé dans :

```text
validation/v1/plan/RUNS.csv
```

Il contient les 120 runs initiaux.

Le plan couvre :

```text
30 tests × 2 conditions × 2 répétitions = 120 runs
```

Conditions :

- avec skill ;
- sans skill.

La troisième répétition n’est exécutée que si les deux premières répétitions
d’un même couple `test × condition` produisent des verdicts différents.

Les runs conditionnels sont pré-déclarés dans :

```text
validation/v1/plan/RUNS_CONDITIONNELS.csv
```

Il existe au maximum :

```text
30 tests × 2 conditions = 60 runs conditionnels
```

Le volume maximal de la campagne est donc :

```text
120 runs initiaux + 60 runs conditionnels = 180 runs comportementaux
```

La règle de répétition est documentée dans :

```text
validation/v1/plan/REGLE_REPETITIONS.md
```

La randomisation est documentée dans :

```text
validation/v1/plan/RANDOMISATION.txt
```

Aucun quatrième run comportemental n’est prévu.

Un éventuel rerun technique ne compte pas comme répétition comportementale et
doit être identifié séparément.

---

## 5. Collector restauré

Le collector éprouvé a été restauré depuis l’ancien dépôt archivé vers :

```text
validation/collector-kit/
```

Principaux fichiers :

```text
analyse_jsonl.py
collect_run.py
commands/bloc1.md
commands/bloc2.md
README.md
tests/
```

Les fixtures historiques ont également été restaurées.

Les caches Python `__pycache__` n’ont pas été recopiés.

### Validation unitaire

Commande exécutée :

```bash
python3 -m unittest discover   -s validation/collector-kit/tests   -p 'test_*.py'   -v
```

Résultat :

```text
Ran 51 tests in 0.795s

OK
```

Conclusion :

```text
51 tests exécutés
51 tests réussis
```

Le collector n’a donc pas besoin d’être modifié pour cette reprise.

---

## 6. Interface réelle du collector vérifiée

### `start`

Arguments disponibles :

```text
--run-id
--scenario-id
--condition
--skill-expected {yes,no,n/a}
--prompt-file
--claude-root
--cwd
--output-root
--skill-name
```

### `collect`

Arguments disponibles :

```text
--run-id
--output-root
--session-id
--parser
```

Les nouveaux blocs opérateur ont été écrits à partir de cette interface réelle,
sans supposer d’arguments non vérifiés.

---

## 7. Personas restaurées mais non injectées

Les ressources historiques suivantes ont été restaurées :

```text
validation/personas/apprenant.md
validation/personas/formateur.md
validation/personas/README.md
```

Une recherche explicite dans les fiches T01 à T30 a donné :

```text
AUCUNE_PERSONA_EXPLICITE
```

Décision pour cette campagne :

```text
persona injectée = aucune
```

Les personas sont conservées comme ressources historiques mais ne participent
pas aux runs T01–T30.

Le contexte pédagogique d’un run provient uniquement du `Prompt exact` de la
fiche historique concernée.

---

## 8. Paramètres techniques d’exécution

Ils sont documentés dans :

```text
validation/v1/operateur/PARAMETRES_EXECUTION.md
```

Configuration retenue :

```text
Claude Code      : 2.1.232
binaire          : /home/david/.local/share/claude/versions/2.1.232
modèle           : claude-sonnet-5
effort           : medium
permission mode  : default
auto-update      : désactivé
auto-memory      : désactivée
persona          : aucune
skill            : tuteur-ingenierie-pedagogique
```

Variables :

```bash
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

Les paramètres communs doivent rester identiques dans les deux conditions.

---

## 9. Workspaces isolés

Chaque run utilise un workspace neuf.

### Avec skill

```text
/projets/skill/tests/tests_avec_skill_A/RUN-ID/
```

Le candidat gelé est copié dans :

```text
RUN-ID/.claude/skills/tuteur-ingenierie-pedagogique/
```

La copie doit correspondre au contenu de :

```text
en_cours/
```

### Sans skill

```text
/projets/skill/tests/tests_sans_skill_B/RUN-ID/
```

Aucun skill ne doit être installé dans ce workspace.

Un workspace déjà existant ne doit pas être silencieusement réutilisé.

---

## 10. Prompt de chaque run

Les prompts matérialisés sont stockés dans :

```text
/projets/skill/tests/prompts/
```

Pour un run donné :

```text
/projets/skill/tests/prompts/RUN-ID.txt
```

Le prompt provient exclusivement de la section :

```text
Prompt exact
```

de la fiche T concernée.

Règles :

- aucune reformulation ;
- aucun enrichissement ;
- aucune persona ajoutée ;
- même prompt dans les deux conditions ;
- même prompt dans les répétitions du même test.

---

## 11. Mécanique opérateur

La campagne utilise deux blocs principaux par run.

Documents :

```text
validation/v1/operateur/BLOC1.md
validation/v1/operateur/BLOC2.md
validation/v1/operateur/INTERACTIONS.md
```

### BLOC 1

Le BLOC 1 couvre :

1. lecture des paramètres du run ;
2. matérialisation du prompt exact ;
3. création d’un workspace neuf ;
4. copie du skill uniquement en condition avec skill ;
5. contrôles préalables ;
6. `collector start` ;
7. lancement de Claude Code.

### Interaction avec Claude

L’opérateur interprète la nature de l’interaction.

Il ne répond pas mécaniquement de la même façon à toute question.

Catégories :

1. interaction technique ;
2. question pédagogique explicitement couverte par la fiche historique ;
3. demande d’information pédagogique absente du scénario ;
4. proposition facultative après une réponse déjà complète.

Pour une information pédagogique absente et non prévue par le scénario, la
réponse neutre exacte est :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

Une simple proposition de continuation après une réponse complète ne déclenche
pas un nouveau tour d’apprenant si la fiche historique ne l’exige pas.

Il n’y a pas de `Esc` systématique pour chaque `AskUserQuestion`.

Une interaction de confiance ou de permission liée à Claude Code est traitée
comme interaction technique, pas comme contenu pédagogique.

### Fin du run

Lorsque la trajectoire est terminée :

```text
exit
```

Puis exécution du BLOC 2.

---

## 12. BLOC 2

Le BLOC 2 est exécuté uniquement après `exit`.

Il couvre :

1. `collector collect` ;
2. utilisation explicite de `analyse_jsonl.py` comme parser ;
3. vérification minimale de présence de la collecte ;
4. création de l’archive ZIP ;
5. calcul du SHA-256 de l’archive.

Racine des artefacts :

```text
/projets/skill/tests/runs/
```

Pour un run :

```text
/projets/skill/tests/runs/RUN-ID/
/projets/skill/tests/runs/RUN-ID.zip
```

Une archive existante ne doit pas être silencieusement écrasée.

Le contrôle réalisé dans le BLOC 2 est technique uniquement.

Aucun verdict comportemental n’est produit à ce stade.

---

## 13. Scoring séparé

Pendant l’exécution de la campagne :

```text
aucun scoring au fil de l’eau
```

Les réponses sont collectées telles qu’observées.

Le scoring est réalisé ultérieurement à partir :

- des trajectoires collectées ;
- des fiches historiques gelées ;
- de leurs critères exacts.

Un résultat défavorable à une condition ne constitue jamais une raison de
relancer un run.

---

## 14. État des fichiers opérateur

Présents :

```text
validation/v1/operateur/PARAMETRES_EXECUTION.md
validation/v1/operateur/BLOC1.md
validation/v1/operateur/BLOC2.md
validation/v1/operateur/INTERACTIONS.md
```

Les fichiers historiques du collector restent également présents :

```text
validation/collector-kit/commands/bloc1.md
validation/collector-kit/commands/bloc2.md
```

Ils ne sont pas modifiés : ils restent une documentation historique du
collector.

Les fichiers `validation/v1/operateur/` représentent la procédure d’exécution
retenue pour cette campagne.

---

## 15. État Git / gels déjà établis

Le protocole et le plan avaient déjà été gelés avant la restauration de
l’outillage.

Référence Git connue :

```text
commit : 5777d0f93c1ba569f703778096aac80c6b79570c
tag    : validation-v1-protocol-frozen
```

Les zones déjà gelées ne doivent pas être modifiées sans décision explicite de
rupture de gel et nouveau point de référence.

La restauration du collector, des personas et la création des fichiers
`validation/v1/operateur/` sont postérieures à ce gel et doivent encore être
contrôlées puis gelées avant le lancement de la campagne.

---

## 16. Prochaine étape

Avant tout premier run comportemental :

1. vérifier à blanc la première ligne de `RUNS.csv` ;
2. vérifier que l’identifiant du run, le scénario et la condition sont lus
   correctement ;
3. vérifier l’extraction du `Prompt exact` ;
4. vérifier les chemins du workspace ;
5. ne pas lancer Claude pendant ce contrôle à blanc ;
6. après validation, créer le gel de l’outillage/runtime opérateur ;
7. seulement ensuite lancer le premier run de la campagne.

État actuel :

```text
candidat gelé                    : OK
tests T01–T30 gelés              : OK
plan RUNS.csv                    : présent
plan 2 + 1 répétition            : défini
collector restauré               : OK
tests unitaires collector        : 51/51 OK
personas restaurées              : OK
personas injectées               : aucune
paramètres d’exécution           : documentés
BLOC1/BLOC2/INTERACTIONS         : écrits
premier run comportemental       : non lancé
```
