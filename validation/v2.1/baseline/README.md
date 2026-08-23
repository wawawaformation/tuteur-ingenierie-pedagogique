# Baseline comportementale V2.1 — instrumentation

Instrumentation d'exécution de la baseline du **lot 0** de la refactorisation du
noyau (`docs/v2.1/PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`,
étapes 0.4 à 0.9).

Ce dossier **collecte**. Il ne score pas et ne contient aucun oracle.

---

## Lancer la baseline

```bash
cd /projets/skill/tuteur-ingenierie-pedagogique-v2
./scripts/run_baseline.sh
```

Rejouer un sous-ensemble :

```bash
./scripts/run_baseline.sh NOY006 NOY013
```

Un scénario déjà présent dans la racine de collecte est ignoré : la commande est
donc relançable sans risque d'écraser une collecte.

## Ce que la commande produit

Racine par défaut, hors dépôt (`validation/CLAUDE.md`, « Données lourdes ») :

```text
/projets/skill/tests/baseline_v2.1_<AAAA-MM-JJ>/
```

Surchargeable par `BASELINE_ROOT`. Un répertoire par scénario :

```text
<SCENARIO>/
├── config/                     # CLAUDE_CONFIG_DIR isolé du run (trace jsonl incluse)
├── workspace/                  # cwd de l'exécutant
│   ├── .claude/skills/tuteur-ingenierie-pedagogique/   # candidat, en lecture seule
│   ├── etat_des_paliers/       # fixture, si la fiche en prévoit une
│   └── persona.md              # si la fiche en injecte un
├── verbatim/
│   ├── tourN_stimulus.txt      # ce qui a été envoyé
│   ├── tourN_reponse.txt       # réponse mot pour mot
│   ├── tourN_rc.txt            # code de retour
│   ├── relance_*.txt           # si la relance neutre a été déclenchée
│   └── fichiers_lus.txt        # skills invoqués et fichiers ouverts, lus dans la trace
├── fixtures_finales/           # état des paliers après le run
├── skill_manifeste.sha256      # empreinte du candidat au départ
├── session_id.txt
└── INVALIDE                    # présent seulement si le candidat a été modifié
```

## Couche opérateur aveugle

Les 14 fiches NOY subordonnent la relance à un jugement d'opérateur — « si
l'agent demande une précision… », « si l'agent demande quel palier… ». Ce
jugement est rendu par un opérateur Sonnet aveugle, membre du harnais
expérimental. C0 n'a aucune clause de relance.

**Paramètres figés, distincts de ceux du candidat :**

```text
modèle opérateur : claude-sonnet-5
effort opérateur : high            # le candidat reste en medium
prompt opérateur : validation/v2.1/baseline/prompt_operateur.md
binaire          : 2.1.241
```

Modèle, effort, prompt et recette doivent être **identiques avant et après
refactorisation**. Ne pas aligner l'effort de l'opérateur sur celui du candidat :
ce sont deux paramètres autoritatifs distincts.

**Quatre décisions, et rien d'autre :**

| Décision | Effet |
|---|---|
| `AUCUNE` | aucune précision demandée → rien n'est envoyé |
| `REPONDRE_AVEC_CONTEXTE` | l'opérateur rédige une réponse minimale, uniquement à partir d'informations explicitement présentes |
| `RELANCE_NEUTRE` | le harnais envoie le texte **exact** de la fiche, pas une reformulation |
| `AMBIGU_OPERATEUR` | le scénario est suspendu, un humain arbitre |

Une seule intervention d'opérateur par scénario, conformément au « une seule
fois, à l'identique » du plan §0.5.

**Ce que l'opérateur ne reçoit jamais** : oracle, invariant, observables,
périmètre de notation, validité technique, verdict, PASS/FAIL, dry-runs,
baselines antérieures, résultat d'un autre scénario. Son dossier
(`kits/<SCENARIO>/dossier_operateur.md`) est construit par **liste blanche** de
sections. Son cwd est un répertoire vide et tous les outils lui sont interdits
(`--disallowed-tools`) : il ne peut atteindre ni les fiches, ni le candidat, ni
le système de fichiers.

**L'opérateur ne score jamais.** Il ne juge pas la qualité de la réponse, ne la
corrige pas, ne la commente pas.

Verbatim conservé par run dans `<SCENARIO>/operateur/` : contexte exact soumis,
sortie brute, décision, motif, réponse éventuelle.

## Arbitrage humain (AMBIGU_OPERATEUR uniquement)

```bash
./scripts/relance_operateur.sh <racine> <SCENARIO> --aucune "motif"
./scripts/relance_operateur.sh <racine> <SCENARIO> --envoyer
./scripts/relance_operateur.sh <racine> <SCENARIO> --repondre "texte"
```

La décision est consignée dans `DECISION_OPERATEUR.txt` et le fichier d'attente
devient `DECISION_OPERATEUR_TRANCHEE.md`. La baseline n'est pas close tant qu'un
scénario reste en attente.

`regle_relance.txt` et `DECISION_OPERATEUR_REQUISE.md` sont destinés à l'humain
et **ne sont jamais envoyés au candidat**.

Supprimer une racine de collecte demande `chmod -R u+w` au préalable : le
sous-arbre du candidat est volontairement non modifiable.

## Recette d'exécution figée

`scripts/run_isole.sh` porte la recette. **Les contrôles post-refactoring
doivent l'utiliser sans modification**, sinon les verdicts ne sont pas
comparables à la baseline.

```bash
DISABLE_AUTOUPDATER=1 CLAUDE_CODE_DISABLE_AUTO_MEMORY=1 \
CLAUDE_CONFIG_DIR="<run>/config" \
/home/david/.local/share/claude/versions/2.1.241 -p \
  --model claude-sonnet-5 --effort medium --permission-mode acceptEdits \
  [--session-id UUID | --resume UUID] \
  [--append-system-prompt-file <run>/workspace/persona.md] \
  < stimulus.txt
# cwd = <run>/workspace
```

Isolation garantie et vérifiée au préflight :

- `/home/david/.claude` de développement jamais lu en écriture ni modifié ;
- aucun `CLAUDE.md`, skill, plugin, hook, agent, commande ou mémoire hérité ;
- le candidat est le seul skill utilisateur visible ;
- seules les credentials sont reprises du profil de développement.

Limite irréductible : les skills intégrés au binaire (`code-review`, `run`,
`init`…) restent présents dans tout exécutant. Un `/home/david/.claude`
réinitialisé n'y changerait rien.

## Kits

`kits/<SCENARIO>/` est **généré**, jamais édité à la main :

```bash
python3 scripts/generer_kits_baseline.py
```

Les stimuli et fixtures sont extraits des blocs de code des fiches
autoritatives de `validation/v2.1/non_regression/`. Aucune recopie manuelle,
donc aucune divergence typographique possible entre la fiche et ce qui est
réellement envoyé.

## Écarts assumés, à connaître avant de scorer

1. **`--permission-mode acceptEdits`** au lieu du `default` de
   `validation/v2/operateur/PARAMETRES_EXECUTION.md`. La campagne V2 était
   interactive : un opérateur humain approuvait les écritures. En headless,
   `default` les refuse, ce qui viderait de leur observable les six scénarios
   exigeant une mise à jour de l'état des paliers. L'invariance du candidat est
   garantie autrement : `chmod a-w` plus manifeste SHA-256 avant et après chaque
   tour, code de retour 65 et marqueur `INVALIDE` en cas de modification.

2. **Binaire 2.1.241** au lieu du 2.1.232 de V1/V2, qui n'est plus installé sur
   la machine. La continuité binaire avec la campagne V2 est donc rompue ; seule
   compte la constance entre cette baseline et les contrôles post-refactoring.

3. **Paquet candidat réduit au runtime** (`SKILL.md` + `references/`).
   `en_cours/CLAUDE.md` est injecté en contexte système dès que le skill est
   utilisé et énumère les invariants testés : le livrer reviendrait à souffler
   l'oracle. `promesse.md` et `base_de_travail.md` sont écartés pour la même
   raison. Le protocole V2 copiait `en_cours/` entier.

4. **Relance conditionnelle : aucune heuristique.** Le jugement d'opérateur
   prescrit par les fiches est rendu par la couche opérateur Sonnet aveugle
   décrite plus haut, jamais par une règle mécanique de ponctuation.

5. **Réserve résiduelle sur le dossier opérateur.** La consigne opérateur de
   certaines fiches nomme elle-même ce que le test observe — NOY009 : « cette
   affirmation est précisément l'un des observables du test » ; NOY008 et NOY010
   énumèrent ce qu'il ne faut pas demander. Ces phrases sont des **interdictions
   protectrices** : les retirer rendrait l'opérateur plus susceptible de
   contaminer le run, pas moins. Elles sont donc conservées, comme pour un
   opérateur humain. La section « Contrôle des interventions opérateur » est en
   revanche exclue : elle cite des éléments de l'oracle en exemples sans rien
   ajouter d'opérationnel.
