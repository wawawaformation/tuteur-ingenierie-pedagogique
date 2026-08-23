# Historique — candidat V2.1

Journal court des étapes réalisées sur le candidat V2.1. Mis à jour avant chaque commit touchant à ce candidat. Ordre chronologique inverse (le plus récent en premier).

---

## 2026-08-23 — Plan d'implémentation du noyau V2.1

- Ajout de `docs/v2.1/PLAN_IMPLEMENTATION_V2.1_2026-08-23_REVISE_3.md` : analyse du noyau actuel au regard de NOY012_1, NOY012_2, NOY013 et de la synthèse des dry-runs. Localise les trois règles bloquantes (`etat_des_paliers.md` l. 29, `taxonomie.md` l. 116, `glossaire.md` « Attestation »), pose un discriminateur sémantique (fondement invoqué par le formateur, pas le mot « atteste »), et détaille les modifications M1–M7 fichier par fichier.
- Révision 2 après arbitrages tranchés par l'utilisateur : A1 (ordre fondé sur une appréciation ≠ attestation, sans chorégraphie conversationnelle imposée), A2 (l'attestation produit un palier réel, utilisable dans le budget A3), A3 (renommage `Preuve` → `Fondement` retenu, justifié par la relecture des fichiers réels et assorti d'une règle de compatibilité pour les fichiers existants). Ajoute une règle de non-cumul/non-conversion (protège NOY005, reclassé risque élevé) et une borne de polarité (protège NOY013).
- Révision 3 : verrouille trois ambiguïtés de rédaction restantes — définition non circulaire de l'« Attestation » dans le glossaire, distinction explicite entre la liste fermée des fondements (palier de maîtrise 1-6) et le cas du palier 0 (« rien d'attesté », pas une maîtrise), et confirmation que `taxonomie.md` l. 118 reste strictement inchangée. Plan jugé prêt pour implémentation par un autre agent, sans arbitrage restant.
- Aucun fichier du noyau touché à ce stade ; document de planification uniquement.

## 2026-08-23 — Dry-runs NOY012/NOY013 et split de NOY012

- Ajout de `validation/v2.1/non_regression/observation_conclusion_recommandation_dry_run.md` : synthèse des dry-runs (session `claude-test`, A avec candidat / B′ via `--safe-mode`) sur l'attestation formateur et « manque de preuve ≠ preuve de manque ». Résultats : NOY012_1 déjà protégé par le candidat actuel (PASS) ; NOY012_2 révèle le manque fonctionnel que V2.1 doit corriger (FAIL sur le candidat actuel, PASS attendu après implémentation) ; NOY013 non discriminant mais gardé comme garde-fou. Recommandations doctrinales R1–R7 et contre-tests futurs C1–C5.
- `NOY012.md` scindé en `NOY012_1.md` (appréciation générale ≠ attestation) et `NOY012_2.md` (attestation explicite = fondement suffisant), pour éliminer la dépendance conversationnelle entre les deux tours d'origine.
- `NOY013.md` révisé : persona non injecté pendant le run, stimulus reformulé pour ne plus tester l'obéissance à un ordre, oracle assoupli sur le libellé du palier 0.
- Corrections de cohérence : renvoi de `NOY013.md` vers `NOY012_2` (au lieu de l'ancien `NOY012`), mise à jour de la table de correspondance et de la section « avant de geler » de `validation/v2.1/non_regression/CLAUDE.md`.

## 2026-08-23 — Session de dry run dédiée

- `validation/CLAUDE.md` (section « Données lourdes ») : ajout d'une mention de la session Linux dédiée `claude-test`, systématiquement réinitialisée, utilisée pour les dry runs et runs de validation afin de garantir un workspace neuf.

## 2026-08-23 — Journal d'historique V2.1

- Création de `docs/historique_2.1.md` (ce fichier), rempli rétroactivement avec les deux commits précédents.
- Commit `6fb44d1`.

## 2026-08-23 — Documentation de `validation/v2.1/` et mise à jour de la carte du dépôt

- Création de `validation/v2.1/non_regression/CLAUDE.md` : statut candidat, table de correspondance de numérotation avec `validation/non_regression/`, citations/codes d'incident à ne pas remapper, condition avant gel, règle de promotion.
- Mise à jour de `.claude/CLAUDE.md` : `en_cours/` décrit comme candidat V2.1 (et non plus V3), ajout de `en_cours/base_de_travail.md` et de `validation/v2.1/non_regression/` dans la carte du dépôt et les sources de vérité.
- Commit `fa64873`.

## 2026-08-23 — Démarrage du candidat V2.1

- `en_cours/VERSION` : `V3` → `V2.1`.
- `en_cours/promesse.md` : rédaction de la promesse fonctionnelle V2.1.0 — promesse centrale, P02 (raisonner par notion/palier/preuve/attestation, hiérarchie des sources), P03 (budget de nouveauté d'une activité évaluée), P04 (alignement objectif → tâche → production → critères → preuve → conclusion), garanties G01–G06. P01 explicitement exclu du noyau, renvoyé à la future promesse tutorat V3.
- Création de `en_cours/base_de_travail.md` : feuille de route V2 → V2.1 → V3, tri de ce qui est repris ou écarté de la V3 expérimentale, mécanisme de dérogations locales au noyau.
- Mise à jour de `en_cours/CLAUDE.md` pour refléter cet état (VERSION, contenu de `promesse.md`, référence à `base_de_travail.md`).
- `validation/v2.1/non_regression/` : reprise à l'identique de NOY002–012 (renumérotés NOY001–011), deux nouveaux scénarios candidats NOY012 (appréciation générale du formateur ≠ attestation explicite d'un palier) et NOY013 (manque de preuve ≠ preuve de manque). NOY001 volontairement exclu (P01 sorti du noyau, ne protège plus V2.1).
- Commit `b062b7c`.

---

## Comment utiliser ce fichier

Avant chaque commit touchant au candidat V2.1, ajouter une entrée courte : date, ce qui a changé, hash du commit une fois créé. Pas de détail d'implémentation ici — il vit dans les fichiers sources (`promesse.md`, `base_de_travail.md`, les fiches NOY, les `CLAUDE.md` de chaque dossier).
