# Rapport d'implémentation — lot A (dé-duplication à doctrine constante)

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** V2.1.0
**Date :** 2026-09-01
**Plan exécuté :** `docs/v2.1/PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, LOT A (étapes A.1 à A.12)
**Statut :** implémentation terminée, **contrôlée comportementalement — non commitée**. Étape A.13 (commit) en attente d'accord.

Ce rapport documente ce qui a été fait. Aucune doctrine n'a été créée, modifiée ou supprimée : seules des paraphrases deviennent des pointeurs vers une source unique, conformément au principe du lot A.

---

# 1. Fichiers modifiés

`en_cours/SKILL.md`, `en_cours/references/opo.md`, `en_cours/references/taxonomie.md`, `en_cours/references/glossaire.md`, `en_cours/references/activite.md`.

`opo.md` s'ajoute aux quatre fichiers listés par le plan (§7, en-tête du lot A) : il est la destination de la canonisation décidée en A.3, implicite dans la liste des étapes mais absent de l'en-tête « Fichiers ».

Aucun NOY, aucune fixture, aucun oracle, aucun autre fichier du runtime touché — vérifié par `git status en_cours/` en fin de lot (exactement ces 5 fichiers) et par l'absence de tout marqueur `INVALIDE` sur les ~14 runs de contrôle exécutés pendant le lot.

---

# 2. Modifications, étape par étape

| Étape | Fichier | Modification | Contrôle | Résultat |
|---|---|---|---|---|
| A.1 | `SKILL.md` l. 30 | Paraphrase + exemple retirés, pointeur vers `etat_des_paliers.md` (P2) | `grep -c "il l'a déjà fait" SKILL.md` → 0 | ✅ |
| A.2 | `taxonomie.md` A3 l. 120 | Paragraphe remplacé par un pointeur vers `etat_des_paliers.md` (« Fondements d'un palier attesté ») (P2) | rerun NOY001 | ✅ PASS |
| A.3 | `opo.md` | Ajout de la chaîne d'alignement canonique (union des 4 variantes, y compris les maillons `portée de la preuve` et `attestation/feedback/remédiation` propres à `taxonomie.md` A4, et `tâche réellement demandée` propre à `SKILL.md`) | `grep -c "portée de la preuve" opo.md` | 2 (voir §4) |
| A.4 | `glossaire.md` l. 236 | Règle normative retirée, pointeur vers `opo.md` (P1, P4) | — | ✅ |
| A.5 | `SKILL.md` l. 105-112 | Chaîne transformée en pointeur vers `opo.md` ; clause « ne pas conclure à un niveau que la preuve ne permet pas d'établir » conservée telle quelle dans `SKILL.md` (P1) | rerun NOY004 (via A.7) | ✅ PASS — risque R2 ne s'est pas matérialisé |
| A.6 | `taxonomie.md` A4 l. 178-187 | Vérifié `opo.md` non vide avant exécution ; chaîne transformée en pointeur (P1) | pré-check ≥ 1 avant exécution | ✅ |
| A.7 | — | Rerun du triplet NOY004 + NOY002 + NOY007 | oracle | ✅ PASS × 3 |
| A.8 | `glossaire.md` l. 13-43 et 236-267 | Définitions de Module/Séquence/Séance/Activité/Granularité réduites à une phrase + un renvoi unique vers `decoupage_pedagogique.md` §1 ou §2 ; entrée « Modalité » de même pour la règle d'indépendance des axes (P4, prérequis de A.10) | `grep -c "granularité la plus fine" glossaire.md` → 0 | ✅ |
| A.9 | `SKILL.md` l. 75, `glossaire.md` l. 388 | I26 (`typical_uses`) ramené à une seule source portante : `activite.md` (P9) | — | ✅ |
| A.10 | `activite.md` l. 7 | I25 ramené à une seule source portante dans le runtime : `decoupage_pedagogique.md` §1 (P8) | rerun **C0** immédiat | ✅ conforme |
| A.11 | — | Contrôle statique complet, diff avec la baseline du lot 0 | `controle_statique_refactoring.sh` | voir §4 |
| A.12 | — | Non-régression complète : NOY001, NOY002, NOY004, NOY005, NOY007, NOY008, NOY009, NOY011, NOY013, C0 | oracle | ✅ 10/10 conformes |

---

# 3. Détail des contrôles comportementaux

Tous les runs ont été exécutés via `scripts/run_isole.sh`, réutilisé directement (pas `run_baseline.sh`, dont le garde-fou de propreté git est incompatible avec la vérification d'un état intermédiaire non commité — voir §6 pour la justification complète). Racine des runs de contrôle : `/projets/skill/tests/lotA_checks_2026-09-01/`.

## A.2 — NOY001 (après A.1, A.2 seules)

3 tours. C1 (Tour 2 : refuse le palier 3 sur exposition + auto-déclaration, cite explicitement le pointeur vers `etat_des_paliers.md`) et C2 (Tour 3 : reconnaît la réalisation autonome comme preuve compatible, met à jour l'état) tous deux satisfaits. Décision opérateur : `AUCUNE`. **PASS**, identique à la baseline du lot 0.

## A.7 — Triplet post-canonisation (après A.3 à A.6)

- **NOY004** — distingue explicitement présence et cohérence des rubriques, ajoute des critères et une grille d'alignement dédiée. **PASS.**
- **NOY002** — aucune capacité d'application attestée, palier 2 avec QCM comme fondement, refuse explicitement la demande d'auto-attestation. **PASS.**
- **NOY007** — aucune notation arbitraire, critères et quantifications restent liés à la tâche. **PASS.**

Aucun des trois n'a régressé : le risque **R2** (perte de visibilité de la chaîne, signalé par le plan comme le point le plus exposé du lot A) ne s'est pas matérialisé sur NOY004, qui teste directement cette zone.

## A.10 — C0 (après A.8, A.9, A.10)

`Activité (Brique)` avec `Étape 1` / `Étape 2` — aucune `Micro-activité` inventée. Contraste I25 préservé après consolidation à une seule source portante dans le runtime. Pas de repli nécessaire.

## A.12 — Non-régression complète (état final du lot)

| Scénario | Tours | Relance | Verdict |
|---|---|---|---|
| C0 | — | — | conforme (réutilisé de A.10, état inchangé depuis) |
| NOY001 | 3 | aucune | **PASS** |
| NOY002 | 2 | aucune | **PASS** |
| NOY004 | 1 | aucune | **PASS** |
| NOY005 | 1 | RELANCE_NEUTRE | **PASS** |
| NOY007 | 1 | RELANCE_NEUTRE | **PASS** |
| NOY008 | 1 | aucune | **PASS** |
| NOY009 | 1 | RELANCE_NEUTRE | **PASS** |
| NOY011 | 1 | aucune | **PASS** |
| NOY013 | 1 | aucune | **PASS** |

**10/10 conformes.** Aucun comportement conforme de la baseline du lot 0 n'a régressé — conformément au critère de sortie du lot A.

Incident technique sans conséquence doctrinale : le rerun de NOY007 a expiré une première fois (timeout de 2 minutes de l'outil d'exécution, pas du candidat) pendant la relance ; repris avec `--resume` sur la même session et un délai plus long, sans perte de trajectoire ni marqueur `INVALIDE`.

---

# 4. Écarts entre les attendus numériques du plan et la réalité mesurée

Trois écarts constatés, tous de même nature : une erreur de comptage de l'auteur du plan au moment de la rédaction, jamais un défaut d'exécution. Chacun a été retracé jusqu'à sa cause avant d'être accepté.

## CS2 — attendu 1, mesuré 3

```text
en_cours/references/opo.md:60
en_cours/references/activites_type/atelier.md:88
en_cours/references/activites_type/brique.md:126
```

Les deux occurrences dans `atelier.md` et `brique.md` ne font pas partie de l'inventaire P1 (qui liste exactement 4 variantes : `SKILL.md`, `taxonomie.md`, `glossaire.md`, `opo.md`) ni de la liste « Fichiers » du lot A. Ce sont des mentions déjà correctement pointées vers `opo.md`, dans le libellé de l'item « Alignement » de chaque gabarit. **Décision actée avec l'utilisateur avant l'implémentation** : rester strictement dans le périmètre déclaré du lot A plutôt que d'étendre le lot à ces deux fichiers hors scope. CS2 termine donc à 3 = 1 porteur canonique + 2 mentions hors périmètre jamais visées, pas à 1.

## CS1 — attendu 0, mesuré 1

```text
en_cours/references/etat_des_paliers.md:1
```

Le grep de CS1 (`refactorings de ce type`) ne cible pas les mêmes 3 emplacements que P2 dans son ensemble : `SKILL.md` l. 30 utilisait un libellé différent (« il l'a déjà fait et ça marchait », sans « refactorings de ce type ») et n'a donc jamais compté dans CS1. Seuls `taxonomie.md` et `etat_des_paliers.md` partageaient le libellé exact. Or `etat_des_paliers.md` est la **source canonique** de destination choisie en A.1/A.2 — elle n'a jamais été candidate à la suppression. Le grep, non discriminant entre canonique et duplicata, comptera donc toujours au moins 1 tant que la doctrine existe quelque part. L'attendu « 0 » du plan ne correspond à aucune étape réellement prescrite pour l'atteindre.

## A.3 — attendu 1, mesuré 2 (signalé en cours d'exécution, non un écart de sortie de lot)

Les deux occurrences de « portée de la preuve » sont toutes deux dans le seul bloc ajouté par A.3 (une fois dans la chaîne, une fois dans la phrase d'explication qui suit) — texte copié tel quel depuis le plan lui-même. Sans conséquence sur A.6 (dont le seul critère réel est « non nul avant exécution »).

**Aucun de ces trois écarts n'affecte le contrôle de sortie du lot A** (§8.3 du plan : « aucun comportement conforme de la baseline ne doit basculer vers une non-conformité »), qui porte sur le comportement observé, pas sur ces comptages statiques.

---

# 5. Contrôle statique complet (A.11)

```text
CS1 : 1 occurrence  (etat_des_paliers.md — canonique, cf. §4)
CS2 : 3 occurrences (opo.md canonique + 2 hors périmètre, cf. §4)
CS3 : 1 occurrence  (decoupage_pedagogique.md — conforme à l'attendu)
CS4 : 1 occurrence  (activite.md — conforme à l'attendu)
CS5 : inchangé (5 lignes, définitions purement descriptives)
CS6 : inchangé (1 occurrence, l. 99 — hors périmètre du lot A, matière du lot B)
CS7 : ancrages taxonomie.md §2 toujours valides (redistribution SKILL.md 3→2, opo.md 1→2 après A.3)
CS8 : invariants gelés — identiques à la baseline (utiliser≠créer:4, Budget de nouveauté:6, palier 0:4, auto-attester:1, palier 2:3)
CS9 : aucun gate de dérogation — OK
```

Note additionnelle, hors du périmètre officiel de CS3 (qui ne scanne que `SKILL.md` et `references/`, pas `en_cours/` en entier) : `en_cours/promesse.md` contient également « granularité la plus fine ». Ce fichier n'est pas chargé par le runtime (`run_isole.sh` ne copie que `SKILL.md` + `references/`) et n'est pas dans le périmètre de fichiers du lot A — non modifié, même traitement que CS2.

---

# 6. Note méthodologique — exécution des contrôles intra-lot

`run_baseline.sh` (orchestrateur du lot 0) refuse de s'exécuter si `en_cours/` diverge de HEAD — garde-fou approprié pour la baseline officielle, mais structurellement incompatible avec les contrôles **intra-lot** prescrits par le plan lui-même (A.2, A.7, A.10), qui portent nécessairement sur un état non commité.

`run_isole.sh`, la brique sous-jacente, ne porte pas ce garde-fou et est explicitement documentée comme réutilisable pour « TOUS les contrôles post-refactoring » (en-tête du script). Les contrôles de ce lot l'ont donc invoquée directement, en répliquant fidèlement la boucle de `run_baseline.sh` (préparation, fixtures, persona, tours, couche opérateur aveugle en cas de `relance.txt`) via un script utilitaire `tmp/run_check.sh` (non versionné, `tmp/` ajouté au `.gitignore`).

Aucune modification de `run_baseline.sh`, `run_isole.sh` ni `operateur_sonnet.sh` n'a été nécessaire.

---

# 7. Dette d'instrumentation

Aucune nouvelle dette constatée. Le comportement du candidat est resté stable et cohérent avec la baseline sur les 14 vérifications comportementales de ce lot, y compris sur le point à risque le plus élevé (A.5/R2, A.10/I25).

---

# 8. Prochaine étape

Étape A.13 du plan — commit :

```bash
git add en_cours/ docs/historique_2.1.md
git commit -m "Refactor V2.1 core: deduplicate normative rules into single sources"
```

En attente d'accord explicite avant exécution.
