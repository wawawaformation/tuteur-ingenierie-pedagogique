# Historique — candidat V2.1

Journal court des étapes réalisées sur le candidat V2.1. Mis à jour avant chaque commit touchant à ce candidat. Ordre chronologique inverse (le plus récent en premier).

---

## 2026-08-23 — Plan de refactorisation du noyau V2.1 : révisé et prêt pour implémentation

- Ajout de `docs/v2.1/PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23.md` : plan détaillé de refactorisation du noyau, directement exécutable par un agent de développement. Comble les défauts révélés par le cycle R1 : défaut de classification, non-opérationnalisation de la préséance, perte de visibilité de règles.
- **Trois points clés révisés après validation utilisateur :**
  1. **Glossaire :** ne conserve plus la formulation « granularité la plus fine », réduisant I25 à un seul porteur (donc conforme à l'objectif de A.10 et à prérequis de A.8).
  2. **Canonisation P1 :** la chaîne d'alignement a quatre étapes formant un bloc indivisible (A.3–A.7), avec contrôles comportementaux immédiats (NOY004, NOY002, NOY007) et repli documenté (conservation d'une chaîne compressée sur une ligne dans `SKILL.md` si risque R2 observé).
  3. **Lot 0 baseline comportementale :** 10 étapes garantissant 15 copies isolées, 15 exécutants aveugles, collecte verbatim, et une baseline de référence (`RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_<date>.md`) remplaçant le dry-run pré-refactorisation comme étalon.
- Mécanisme de préséance : remplacement du marqueur en prose par **`deroge_a:` / `perimetre:` en front matter**, avec index minimal de deux IDs stables (`A3`, `R-GRAN`) et aucune reclassification implicite des références existantes. Décision D1-bis : index initial à `A3` et `R-GRAN` seulement.
- Chantier NOY014 différé (§9) : fixtures à redessiner sur le mécanisme de front matter après lot B, avec contrôles anti-gate, déclarations invalides et non-extension hors périmètre.
- Critères de sortie explicites (§11) : 14/14 NOY hors NOY014, C0 conforme, deux PASS distinctifs de NOY014_1 et NOY014_2 conjointement avec corps de fixture identiques, trois contrôles de mécanique invalide et un contrôle de non-extension.
- **Aucune modification du runtime** pendant la rédaction du plan. `en_cours/` intact, validation/ intact.

## 2026-08-23 — Cycle correctif R1 : revue du scénario, correctif invalidé, reverté

- Ajout de `docs/v2.1/RAPPORT_CYCLE_R1_V2.1_2026-08-23.md`. Revue indépendante de NOY014 avant toute correction : oracle, stimulus, overlay et contraste jugés sains ; `mock_sans_derogation.md` jugé **défectueux comme cas négatif** (quasi-positif : ses l. 7/11/13 réunissent règle contredisante + connaissance de la règle contredite + limitation de portée — seul le mot « déroge » sépare les deux fixtures).
- **C0 exécuté et consigné pour la première fois** (il n'avait jamais été joué, alors qu'il conditionne la validité de l'instrument) : le candidat produit `Étape 1`/`Étape 2` et jamais `Micro-activité`. Contraste établi, avant comme après correctif.
- Cause racine consolidée : le pôle « règle générale du skill » de `SKILL.md` l. 120 est non résolvable au runtime (« noyau » absent de `SKILL.md` et `references/` ; la règle générale vit elle-même dans `references/`), et surtout le « marqueur uniforme » exigé par `base_de_travail.md` §18 n'a jamais été défini dans le runtime.
- Correctif appliqué sur `SKILL.md` l. 99 et l. 120, 8 contrôles statiques passés, puis **invalidé par le rerun** : NOY014_1 reste FAIL (2 runs), NOY014_2 PASS, C0 sans régression. Sur les 5 runs avec fixture, la sortie est `Micro-activité` dans 100 % des cas, avec ou sans marqueur : **l'effet du marqueur est nul**, donc le PASS de NOY014_2 est vacuous. Cela corrige la conclusion du dry-run sans réécrire son rapport.
- Décision : **revert** de `SKILL.md` (retour à l'état de `01e9ca1`) et renvoi de la préséance à la refactorisation générale du noyau. `PLAN_CORRECTION_R1_V2.1_2026-08-23.md` marqué caduc. Aucun oracle, NOY ou fixture modifié ; aucun fichier du noyau modifié à l'état final.

## 2026-08-23 — Dry-run pré-refactorisation : R1 confirmé, cycle correctif décidé

- Ajout de `docs/v2.1/RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md` : dry-run des 16 scénarios NOY sur le candidat V2.1 post-G02. 15/16 PASS ; `NOY014_1` en FAIL reproductible 3/3 — Claude applique la règle spécialisée sans dérogation explicitement signalée, correspondant exactement au risque R1 déjà identifié dans `RAPPORT_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23.md`. `NOY014_2` (dérogation explicite) reste PASS. Décision (§8, ajoutée après coup) : traiter R1 dans un cycle correctif séparé, strictement ciblé, avant d'engager la refactorisation du noyau.
- Ajout de `docs/v2.1/PLAN_CORRECTION_R1_V2.1_2026-08-23.md` : plan de correction limité à `en_cours/SKILL.md` l. 99 (« la référence normative spécialisée fait foi » → « c'est la référence normative spécialisée qui porte cette règle, pas le glossaire »), sans toucher l. 120 (bloc de préséance G02), ni les oracles/fixtures NOY014. Vérification prévue ciblée sur `NOY014_1`/`NOY014_2` uniquement, non-régression complète différée à après la refactorisation.
- Aucun fichier du noyau modifié à ce stade ; le plan est en attente d'exécution.

## 2026-08-23 — Implémentation de la règle de préséance / dérogation locale (G02)

Exécution stricte de `docs/v2.1/PLAN_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23_CORRIGE.md`. Comble l'écart entre G02 (`en_cours/promesse.md`) et le runtime, en s'appuyant sur les scénarios `NOY014_1`/`NOY014_2` déjà copiés dans `validation/v2.1/non_regression/`. Aucun NOY, oracle ou fixture modifié.

- `en_cours/SKILL.md`, l. 120 (section « Contrôles avant réponse ou livraison ») : la ligne « ne pas arbitrer silencieusement ; la signaler » est remplacée par un bloc unique de préséance — une référence spécialisée dont le périmètre s'applique et qui signale explicitement déroger à une règle générale du skill prévaut, pour ce seul périmètre ; sans dérogation explicite, la règle générale prévaut ; une dérogation locale ne s'étend jamais implicitement. La clause de signalement des contradictions est conservée à l'identique, comme cas résiduel subordonné à « reste non résolue ».
- `SKILL.md` est retenu comme **source normative** de ce mécanisme (pas un simple routage) : c'est une règle d'orchestration documentaire, et aucune référence de domaine (`decoupage_pedagogique.md`, `etat_des_paliers.md`, etc.) n'est compétente pour l'arbitrage inter-documents.
- Choix terminologique : « règle générale du skill », le mot « noyau » étant absent du runtime (présent seulement dans `promesse.md`, `base_de_travail.md` et les fiches NOY014).
- Contrôles statiques CS-P1 à CS-P8 passés par relecture (voir le rapport d'implémentation pour le détail). Risque principal identifié et non traité préventivement : `SKILL.md` l. 99 (« la référence normative spécialisée fait foi ») pourrait être lue comme une préséance générale des spécialisées, ce qui ferait échouer NOY014_1 — à vérifier par le run avant toute correction.
- Statut : non testé. Séquence prévue : contrôle statique de `Activité = granularité la plus fine`, C0, NOY014_1, NOY014_2, smoke tests attestation, non-régression complète (16 scénarios).

## 2026-08-23 — Rapport d'implémentation et alignement de `promesse.md`

- Ajout de `docs/v2.1/RAPPORT_IMPLEMENTATION_V2.1_2026-08-23.md` : compte rendu structuré de l'implémentation M1-M7 (fichiers modifiés, règle précédente/modification/raison par fichier, résultats CS1-CS6, écarts par rapport au plan, ambiguïté sur NOY006, risques de régression à surveiller).
- `en_cours/promesse.md` aligné sur la doctrine effectivement implémentée dans le noyau : rôle de formateur/responsable pédagogique déclaré ou établi dans le contexte (pas authentifié) ; une demande d'inscription fondée sur une appréciation, une impression ou une déclaration relayée ne devient pas une attestation ; règle de non-cumul explicitée pour P02 (une performance observée relève de la voie preuve, une instruction jointe ne la convertit pas en attestation) ; révisabilité étendue à tout fondement ; P03 précise qu'un palier attesté par voie d'attestation explicite est utilisable normalement comme prérequis, y compris pour le budget de nouveauté (arbitrage A2) ; G02 précise que la règle de dérogation locale ne crée pas de nouveau gate.

## 2026-08-23 — Implémentation du noyau V2.1 (M1-M7, non testée)

Exécution stricte de `docs/v2.1/PLAN_IMPLEMENTATION_V2.1_2026-08-23_REVISE_3.md`. Aucun oracle NOY ni aucune fixture modifiés ; aucun dry-run lancé.

- `en_cours/references/etat_des_paliers.md` : ajout de la section « Fondements d'un palier attesté » (deux fondements admissibles pour un palier de maîtrise 1-6 — preuve compatible ou attestation explicite valide à quatre conditions cumulatives ; cas du palier 0 distingué ; discriminateur sémantique par ce que l'interlocuteur invoque ; règle de non-cumul/non-conversion ; borne de polarité ; contre-exemples explicites). Retrait de l'incise « ou une décision du formateur » de la règle sur la déclaration d'acquisition. Extension de la portée limitée et de la révisabilité à l'attestation. Renommage de la colonne `Preuve` en `Fondement` (en-têtes et exemple), avec règle explicite de compatibilité pour les fichiers existants nommés `Preuve`.
- `en_cours/references/taxonomie.md` : la définition de « attesté » (clause A3) reconnaît les deux fondements en pointant vers `etat_des_paliers.md`, sans dupliquer les conditions. Les règles existantes (exposition/déclaration ≠ preuve, preuve externe rapportée) restent strictement inchangées.
- `en_cours/references/glossaire.md` : définition non circulaire de « Attestation » ; nouvelle entrée « Fondement » ; précision dans « Déclaration » la distinguant de l'attestation explicite.
- `en_cours/SKILL.md` : une ligne de renvoi vers `etat_des_paliers.md` pour l'attestation explicite, sans dupliquer les conditions.

Validation comportementale (smoke tests NOY012_2/NOY012_1/NOY006, contre-tests C1-C5, non-régression complète) volontairement non réalisée à ce stade — prévue après revue du diff par l'utilisateur.

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
