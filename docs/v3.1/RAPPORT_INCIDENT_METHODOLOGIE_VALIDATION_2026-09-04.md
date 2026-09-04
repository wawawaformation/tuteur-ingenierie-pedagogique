# Rapport d'incident — Campagnes de validation jouées hors des harnais du dépôt (2026-09-04)

**Statut :** incident méthodologique confirmé, corrigé pour la suite de la session — les campagnes concernées restent à rejouer avec le bon outillage avant de leur faire à nouveau confiance.
**Portée :** ce rapport documente une erreur de méthode commise par l'agent (Claude), pas un défaut du skill.

---

## 1. Ce qui s'est passé

Au cours de cette session, deux campagnes de validation ont été jouées **sans utiliser aucun des harnais du dépôt** :

- la batterie candidate V3.1.0 (`validation/v3.1/non_regression/`, 8 scénarios, jusqu'à 3 exécutions chacun) ;
- la batterie de non-régression V2.1 (`validation/v2.1/non_regression/`, 14 scénarios NOY001-013, passe unique).

Dans les deux cas, la méthode utilisée a été : dispatcher des sous-agents via l'outil `Agent`, avec un prompt du type « tu incarnes un tuteur qui applique le skill installé dans le répertoire X », en reconstruisant à la main fixtures et personas dans des répertoires de travail ad hoc sous `/tmp`.

**Cette méthode n'est ni `scripts/run_baseline.sh` / `scripts/run_isole.sh`, ni `validation/collector-kit/`.** Elle n'apparaît dans aucune documentation du dépôt : c'est une improvisation, pas une réutilisation d'un outillage existant — alors que les deux harnais officiels sont documentés, référencés depuis plusieurs endroits du dépôt (`validation/CLAUDE.md`, `en_cours/base_de_travail.md`, les rapports `docs/v2.1/RAPPORT_*`) et avaient déjà été lus par l'agent avant de choisir cette méthode.

## 2. Comment ça a été découvert

`NOY004` a échoué 4 fois sur 4 avec la méthode par sous-agents (candidat V3.1.0 : 3 exécutions ; V2.1 publiée : 1 exécution). L'utilisateur a demandé de rejouer ce scénario précis « sur claude-test », ce qui a forcé à relire attentivement `validation/CLAUDE.md` — et à y trouver ce qui y était déjà écrit :

> « Cette convention [`claude-test`] ne s'applique pas au harnais de baseline comportementale (`scripts/run_baseline.sh` et `scripts/run_isole.sh`) : celui-ci s'exécute **sous le compte `david`** [...]. Ne pas tenter de le faire tourner sous `claude-test` sans revoir ses dépendances. »

En rejouant `NOY004` avec le vrai harnais (`run_isole.sh`, non modifié pour V3.1.0 ; copie de travail avec `CANDIDAT` repointé pour V2.1, seule ligne différente) — modèle et effort épinglés (`claude-sonnet-5`, effort `medium`), binaire figé, isolation `CLAUDE_CONFIG_DIR` dédiée, candidat verrouillé en lecture avec empreinte SHA-256 — le résultat a été **PASS sur les deux candidats**, cohérent avec le `PASS/PASS` déjà consigné dans `docs/v2.1/RAPPORT_NON_REGRESSION_FINALE_V2.1_2026-09-01.md`.

**Le FAIL 4/4 n'était donc pas réel.** C'était un artefact de la méthode par sous-agents (prompt de cadrage différent, paramètres de modèle/effort non garantis identiques au harnais), pas un défaut du skill.

## 3. Cause racine

L'agent n'a jamais cherché, avant de lancer ces deux campagnes, si un harnais dédié existait déjà pour ce type d'exécution — alors que :

- `scripts/run_baseline.sh` et `scripts/run_isole.sh` existent, sont documentés comme la « recette figée » pour la baseline comportementale, et étaient visibles dans `scripts/` depuis le début de la session ;
- `validation/collector-kit/` existe, documenté comme l'outillage pour les campagnes candidates (le type même de ce qui a été fait pour V3.1.0) ;
- `validation/CLAUDE.md`, lu plusieurs fois au cours de la session, décrit explicitement les deux harnais, leurs comptes système respectifs (`david` pour la baseline, `claude-test` pour `collector-kit`), et le point de dépôt neutre entre les deux (`/projets/tests/inbox`, sticky bit).

Improviser une méthode équivalente en apparence (sous-agents, fixtures reconstruites à la main) a semblé suffisant sans vérifier qu'elle produisait des résultats comparables aux harnais calibrés — alors que ces harnais épinglent précisément des paramètres (modèle, effort, mode de permission, binaire) dont rien ne garantissait l'équivalence avec des sous-agents dispatchés via l'outil `Agent` de la session courante.

## 4. Ce que ça invalide

**Toutes les campagnes jouées par sous-agents dans cette session sont de fiabilité incertaine**, `NOY004` ayant démontré une divergence réelle entre méthode improvisée et harnais officiel :

- la batterie V3.1.0 à 8 scénarios (incluant les diagnostics et corrections faits sur `V31-ACT02-3` et `V31-ACT02-5` plus tôt dans la session) ;
- la batterie V2.1 à 14 scénarios (13 PASS + 1 FAIL initialement rapportés).

Aucune de ces campagnes n'a été rejouée avec le bon outillage à ce stade — ce rapport ne les invalide pas définitivement, il retire seulement la confiance qu'on pouvait leur accorder telles quelles.

## 5. Les deux harnais du dépôt — pour ne plus se tromper

| Harnais | Sert à | Compte système | Isolation |
|---|---|---|---|
| `scripts/run_baseline.sh` + `scripts/run_isole.sh` (`validation/v2.1/baseline/kits/`) | Batterie de non-régression V2.1 (C0 + NOY001-013) | **`david`** | `CLAUDE_CONFIG_DIR` dédié par run, candidat verrouillé en lecture (`chmod -w` + empreinte SHA-256), modèle/effort/binaire épinglés dans `run_isole.sh` |
| `validation/collector-kit/` (`collect_run.py`) | Campagnes candidates (scénarios NOY d'une mineure V3.x, dry-runs) | **`claude-test`**, session dédiée systématiquement réinitialisée | Compte système séparé ; transfert des artefacts via `/projets/tests/inbox` (sticky bit, dépôt neutre entre `david` et `claude-test`, qui ne partagent aucun accès direct) |

Aucun des deux n'est « l'outil `Agent` de la session Claude Code en cours ». Avant de lancer une campagne de validation ou de non-régression sur ce dépôt, vérifier lequel des deux s'applique et l'utiliser tel quel — ne jamais improviser un équivalent, même en reprenant fidèlement stimulus, oracle et convention opérateur.

## 6. À faire avant de considérer une campagne fiable

1. Identifier le harnais correspondant (tableau ci-dessus).
2. L'exécuter sous le compte système documenté, avec ses paramètres figés.
3. Ne considérer un verdict comme fiable que s'il vient de cette exécution — pas d'une reconstitution par sous-agent, même soigneuse.
