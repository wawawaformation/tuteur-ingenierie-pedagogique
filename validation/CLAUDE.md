# CLAUDE.md — `validation/`

Ce dossier contient le **dispositif de validation** du skill : scénarios, personas, instrumentation, procédures et archives de campagnes.

## Exécution — toujours l'un des deux harnais, jamais une reconstitution

Toute campagne de validation ou de non-régression sur ce dépôt utilise l'un des deux harnais existants :

- **`scripts/run_baseline.sh` + `scripts/run_isole.sh`** (compte `david`) pour la batterie V2.1 (`validation/v2.1/baseline/kits/`) ;
- **`validation/collector-kit/`** (compte `claude-test`) pour les campagnes candidates d'une mineure V3.x.

**Ne jamais improviser un équivalent** — par exemple dispatcher des sous-agents génériques (outil `Agent`) avec le stimulus et l'oracle reconstitués à la main. Même en reprenant fidèlement le stimulus, la fixture et la convention opérateur, rien ne garantit que le modèle, l'effort de raisonnement ou le mode de permission utilisés correspondent aux paramètres épinglés par le harnais — et un verdict obtenu ainsi n'est pas comparable aux campagnes précédentes.

Incident survenu le 2026-09-04 : une campagne entière (8 scénarios V3.1 + 14 scénarios V2.1) a été jouée par sous-agents improvisés, produisant un `FAIL` sur `NOY004` qui s'est révélé faux dès rejeu avec le vrai harnais (`PASS` des deux côtés). Détail complet : `docs/v3.1/RAPPORT_INCIDENT_METHODOLOGIE_VALIDATION_2026-09-04.md`.

## Principe central

La validation doit protéger l'objectif du test, pas une chorégraphie mécanique.

L'opérateur joue les tours gelés et peut adapter les interactions intermédiaires uniquement à partir des informations déjà disponibles lorsque cela est nécessaire pour rendre l'objectif observable, sans :

- souffler l'oracle ;
- inventer une nouvelle information pédagogique ;
- introduire artificiellement un élément qui change ce que le scénario mesure.

Lorsqu'aucune information supplémentaire pertinente n'existe, une réponse neutre du type suivant est appropriée si la procédure l'autorise :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

## Séparer les couches

Toujours distinguer :

```text
conception du scénario
→ exécution / collecte
→ contrôle technique
→ anonymisation
→ scoring
→ adjudication éventuelle
→ désaveuglement
→ répétition conditionnelle éventuelle
→ synthèse
```

Ne pas utiliser un résultat d'une couche future pour modifier rétroactivement une couche déjà gelée.

## Scoring

- Appliquer l'oracle correspondant au `scenario_id`.
- Juger les observables réellement présents.
- Ne pas ajouter une règle implicite plus stricte que l'oracle.
- Ne pas transformer une préférence pédagogique en critère de FAIL.
- Conserver `PASS`, `FAIL`, `INDÉTERMINÉ` lorsque le protocole l'impose.

## Campagnes historiques

Les dossiers `v1/` et `v2/` sont des éléments de traçabilité.

Ne pas les modifier pour refléter le candidat courant. Une nouvelle version doit avoir sa propre campagne ou ses propres artefacts clairement séparés.

## Données lourdes

Les workspaces et traces d'exécution peuvent vivre hors du dépôt lorsque la procédure le prévoit. Le dépôt doit conserver les artefacts pérennes nécessaires à la compréhension, à l'audit et à la reproductibilité.

Les dry runs et runs de validation exécutés via `collector-kit` utilisent une session Linux dédiée (`claude-test`), systématiquement réinitialisée, pour garantir un workspace neuf et une fixture non contaminée.

Cette convention ne s'applique pas au harnais de baseline comportementale (`scripts/run_baseline.sh` et `scripts/run_isole.sh`, `validation/v2.1/baseline/`) : celui-ci s'exécute **sous le compte `david`**, avec sa propre isolation par run (`CLAUDE_CONFIG_DIR` dédié, candidat en lecture seule avec empreinte SHA-256), indépendante du compte système. Ne pas tenter de le faire tourner sous `claude-test` sans revoir ses dépendances (binaire figé et identifiants sous `/home/david/`).

### Transfert des artefacts depuis `claude-test` (runs via `collector-kit`)

`claude-test` et `david` ne partagent aucun accès direct : `/home/claude-test` est en `drwxr-x---` (david ne peut pas y lire) et `/projets/skill/tests/` appartient à david sans écriture pour les autres (claude-test ne peut pas y écrire).

Le transfert passe donc par un point de dépôt neutre :

```text
/projets/tests/inbox     (drwxrwxrwt, sticky)
```

- les runs et la collecte s'exécutent **entièrement sous `claude-test`** : `collect_run.py` doit être lancé par ce compte pour que `--claude-root` (`~/.claude/projects` par défaut) pointe sur la bonne trace de session ;
- `--output-root` et `--prompt-file` sont dirigés vers l'espace de `claude-test`, jamais vers `/projets/skill/tests/` ;
- `claude-test` **dépose** les archives de run dans `inbox/` ; david les classe ensuite dans `/projets/skill/tests/archives/`.

Ne pas résoudre ce cloisonnement en ajoutant david au groupe `claude-test` : l'isolation entre le compte de test et le compte de travail fait partie du dispositif.
