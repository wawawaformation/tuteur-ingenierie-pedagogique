# État post-gel — validation V1

Dernière mise à jour : 2026-08-18

Ce document complète l’état de préparation de la campagne V1 après le gel local
du runtime et de l’outillage opérateur.

Il ne remplace pas les documents gelés et ne doit pas être inclus rétroactivement
dans le manifeste déjà figé.

---

## 1. Frontière expérimentale atteinte

La préparation de la campagne est terminée localement.

État vérifié :

```text
candidat gelé                    : OK
tests historiques T01–T30        : OK
plan expérimental                : OK
collector                        : 51/51 tests unitaires OK
runtime/opérateur                : gelé
premier run comportemental       : non lancé
```

Aucun run comportemental n’a été exécuté avant le gel du runtime.

---

## 2. Référence Git du gel runtime/opérateur

Commit :

```text
a132ef59e6010d7d264545f70f50233be22ca159
```

Tag annoté :

```text
validation-v1-runtime-frozen
```

Le tag a été vérifié comme pointant vers exactement le même commit :

```text
HEAD :
a132ef59e6010d7d264545f70f50233be22ca159

validation-v1-runtime-frozen^{commit} :
a132ef59e6010d7d264545f70f50233be22ca159
```

Le `git status --short` était vide au moment de cette vérification.

Le push distant du commit et du tag doit être confirmé séparément après exécution
de la commande de push. Tant que cette confirmation n’a pas été observée, ce
document ne prétend pas que le gel est présent sur le dépôt distant.

---

## 3. Manifeste runtime/opérateur

Manifeste :

```text
validation/v1/manifest/RUNTIME_OPERATEUR.sha256
```

Il contient 28 entrées.

Les chemins ont été normalisés en chemins relatifs au dépôt.

Le manifeste couvre notamment :

- le collector restauré ;
- les tests et fixtures du collector ;
- les personas historiques restaurées ;
- les fichiers opérateur V1 ;
- le document d’état précédent du 17 août.

Le contrôle `sha256sum -c` a réussi pour l’ensemble des entrées avant le commit
et le tag.

---

## 4. Collector

Emplacement :

```text
validation/collector-kit/
```

Validation unitaire :

```text
Ran 51 tests

OK
```

Le collector a été conservé sans refonte.

Interface vérifiée :

### `start`

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

```text
--run-id
--output-root
--session-id
--parser
```

---

## 5. Conditions et convention `skill-expected`

La convention retenue reste alignée avec le bloc historique éprouvé :

```text
avec skill  -> condition=skill    -> skill-expected=yes
sans skill  -> condition=no-skill -> skill-expected=n/a
```

Le fichier opérateur correspondant est :

```text
validation/v1/operateur/BLOC1.md
```

---

## 6. Personas

Les ressources historiques sont présentes :

```text
validation/personas/apprenant.md
validation/personas/formateur.md
validation/personas/README.md
```

La recherche dans les fiches T01 à T30 a donné :

```text
AUCUNE_PERSONA_EXPLICITE
```

Décision :

```text
persona injectée = aucune
```

Les personas sont conservées comme artefacts historiques mais ne sont pas
injectées dans les runs de cette campagne.

---

## 7. Racine runtime isolée de la campagne

La campagne courante utilise exclusivement :

```text
/projets/skill/tests/validation_v1_2026-08-17/
```

Arborescence :

```text
/projets/skill/tests/validation_v1_2026-08-17/
├── prompts/
├── runs/
├── tests_avec_skill_A/
└── tests_sans_skill_B/
```

Cette isolation a été décidée après détection d’artefacts historiques utilisant
déjà les identifiants `RUN-001`, etc. sous les anciennes racines.

Les anciens artefacts ne sont ni supprimés ni écrasés.

Les identifiants gelés du plan restent inchangés.

---

## 8. Plan expérimental

Plan initial :

```text
validation/v1/plan/RUNS.csv
```

Colonnes vérifiées :

```text
run_id | test_id | condition | repetition | status
```

Volume initial :

```text
30 tests × 2 conditions × 2 répétitions = 120 runs
```

Runs conditionnels :

```text
validation/v1/plan/RUNS_CONDITIONNELS.csv
```

Une troisième répétition n’est exécutée que si les deux premières répétitions
d’un même couple `test × condition` produisent des verdicts différents.

Aucun quatrième run comportemental n’est prévu.

---

## 9. Premier run du plan

Le premier run randomisé vérifié est :

```text
run_id      = RUN-001
test_id     = T13
condition   = avec skill
repetition  = 1
status      = PLANNED
```

Le prompt exact extrait à blanc est :

```text
Crée une activité asynchrone dans laquelle l'apprenant :
1. analyse le problème ;
2. choisit une solution ;
3. implémente ;
4. teste ;
5. rédige un court bilan.

La production doit durer environ 2 heures.
```

Le contrôle à blanc a confirmé :

```text
condition plan      = avec skill
condition collector = skill
skill_expected      = yes
```

Aucun workspace, prompt runtime, dossier de collecte ou ZIP de cette nouvelle
campagne n’existait pour `RUN-001` au moment du préflight final.

---

## 10. Fichiers opérateur

Répertoire :

```text
validation/v1/operateur/
```

Fichiers :

```text
PARAMETRES_EXECUTION.md
BLOC1.md
BLOC2.md
INTERACTIONS.md
DECISION_ISOLATION_RUNTIME.md
```

Mécanique retenue :

```text
BLOC 1
→ interaction avec Claude
→ exit
→ BLOC 2
```

L’opérateur interprète les interactions au lieu d’appliquer une réponse
mécanique à toute question.

Pour une demande pédagogique non couverte par le scénario, la phrase neutre
exacte reste :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

Il n’y a pas de `Esc` systématique.

---

## 11. Paramètres Claude Code

Configuration commune aux deux conditions :

```text
Claude Code      : 2.1.232
binaire          : /home/david/.local/share/claude/versions/2.1.232
modèle           : claude-sonnet-5
effort           : medium
permission mode  : default
auto-update      : désactivé
auto-memory      : désactivée
persona          : aucune
```

Variables :

```bash
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

---

## 12. Documents gelés à ne pas modifier

Le document suivant appartient au gel protocolaire précédent :

```text
docs/protocole_operateur.md
```

Il ne doit pas être modifié pour refléter l’état courant.

Le document :

```text
docs/ETAT_VALIDATION_V1_2026-08-17.md
```

est lui-même inclus dans :

```text
validation/v1/manifest/RUNTIME_OPERATEUR.sha256
```

Il constitue donc désormais un instantané historique couvert par le gel runtime.

Il ne faut pas le modifier après le tag `validation-v1-runtime-frozen`, sinon le
manifeste serait invalidé.

Le présent document du 18 août sert précisément à consigner l’état post-gel sans
altérer cet instantané.

---

## 13. Règles opératoires de sécurité terminal

Les commandes destinées à être copiées directement dans un terminal interactif
doivent utiliser des chemins absolus.

Elles ne doivent pas inclure :

```text
set -e
set -euo pipefail
exit
exit 1
```

dans les blocs de préparation ou de contrôle, afin d’éviter de fermer
accidentellement le shell interactif.

Les contrôles doivent signaler les anomalies avec des messages `STOP` ou
`ERREUR` sans quitter le terminal.

---

## 14. Étape suivante

La phase de conception/préparation est considérée terminée.

Avant passage à l’agent opérateur :

1. pousser le commit `a132ef59e6010d7d264545f70f50233be22ca159` sur le dépôt distant ;
2. pousser le tag `validation-v1-runtime-frozen` ;
3. vérifier que le dépôt distant contient bien les deux ;
4. préparer la consigne de l’agent opérateur à partir des artefacts gelés.

L’agent opérateur prendra ensuite en charge l’exécution de la campagne.

Il ne devra pas modifier :

- le candidat ;
- les tests T01–T30 ;
- le plan ;
- le collector ;
- les fichiers opérateur ;
- les règles de répétition.

Le scoring comportemental restera séparé de l’exécution.
