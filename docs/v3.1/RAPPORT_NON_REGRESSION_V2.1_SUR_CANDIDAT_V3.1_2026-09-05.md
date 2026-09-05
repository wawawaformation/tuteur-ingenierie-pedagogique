# Rapport — Non-régression baseline V2.1 sur le candidat V3.1

**Date :** 2026-09-05
**Fondement :** `en_cours/base_de_travail.md` §4 — vérification que le candidat V3.1 ne régresse pas sur les comportements validés de la baseline V2.1.
**Harnais :** `scripts/run_baseline.sh` + `scripts/run_isole.sh`, recette figée.
**Distinct des validations V3.1** : les 15 scénarios V3.1 (batterie propre à la mineure) ont déjà été validés 15/15 PASS le 2026-09-04. Ce rapport concerne uniquement la non-régression sur les 15 scénarios V2.1 autoritatifs.

---

## 1. Candidat et intégrité

### Commit de `en_cours/`

```text
0a4f216229b5cbd2d7c9b236ef010a239a4799a1
```

`git status --porcelain --untracked-files=all -- en_cours/` : vide au moment du lancement — vérifié par le garde-fou de `run_baseline.sh` (abandon prévu sinon).

### Manifeste SHA-256 — identique dans les 15 copies isolées

Toutes les copies du candidat ont produit le même manifeste SHA-256 (md5 des 15 fichiers de manifeste : `0fbdc2ad58d1cd7b7e5b9a7666c4e5f3`). Les 30 fichiers du candidat (`SKILL.md` + 29 références) ont été copiés à l'identique dans chaque workspace isolé.

Le candidat V3.1 contient les nouveaux gabarits d'ouverture (`barometre_humain.md`, `objet_express.md`, `planche_meteo.md`) et les références de production (`activite_evaluee.md`, `production_documentaire.md`) absents du candidat V2.1. Ces fichiers sont présents dans le manifeste de cette campagne ; ils sont absents du manifeste de la baseline V2.1 originale (`docs/v2.1/RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md`). Cette différence est attendue et assumée : le candidat V3.1 est une extension du noyau V2.1, non une copie identique.

### Environnement d'exécution

- **Compte :** `david`.
- **Recette figée :** `scripts/run_isole.sh` v2026-09-05, modifiée uniquement pour neutraliser les variables Azure Foundry héritées de la session parente (`CLAUDE_CODE_USE_FOUNDRY=""`) — les runs candidats utilisent l'API Anthropic directe via `credentials.json`, comme lors de la baseline V2.1.
- **Modèle candidat :** `claude-sonnet-5`, effort `medium`, binaire `2.1.241` (identique à la baseline V2.1).
- **Modèle opérateur :** `claude-sonnet-4-6`, effort `high`, via Azure Foundry — différent du `claude-sonnet-5` de la baseline V2.1 (voir §5, Écarts).
- **Isolation :** un `CLAUDE_CONFIG_DIR` dédié par run, seul `.credentials.json` repris du profil `david`.

---

## 2. Collecte

Racine : `/projets/skill/tests/baseline_v2.1_2026-09-05/`

**15/15 scénarios avec collecte complète** — aucun suspendu, aucune anomalie, aucun arbitrage humain requis.

| Scénario | Persona | Tours | Décision opérateur |
|---|---|---|---|
| C0 | aucun | 1 | — (pas d'opérateur pour C0) |
| NOY001 | apprenant.md | 3 | AUCUNE |
| NOY002 | apprenant.md | 2 | REPONDRE_AVEC_CONTEXTE |
| NOY003 | apprenant.md | 1 | RELANCE_NEUTRE |
| NOY004 | formateur.md | 1 | RELANCE_NEUTRE |
| NOY005 | aucun | 1 | RELANCE_NEUTRE |
| NOY006 | aucun | 1 | RELANCE_NEUTRE |
| NOY007 | aucun | 1 | REPONDRE_AVEC_CONTEXTE |
| NOY008 | formateur.md | 1 | AUCUNE |
| NOY009 | formateur.md | 1 | RELANCE_NEUTRE |
| NOY010 | formateur.md | 1 | AUCUNE |
| NOY011 | formateur.md | 1 | AUCUNE |
| NOY012_1 | aucun | 1 | REPONDRE_AVEC_CONTEXTE |
| NOY012_2 | aucun | 1 | AUCUNE |
| NOY013 | aucun | 1 | AUCUNE |

---

## 3. Scoring

Oracle appliqué : `validation/v2.1/non_regression/NOY*.md` (fiches autoritatives).

| Scénario | Verdict | Observable décisif |
|---|---|---|
| C0 | conforme | Pas de verdict officiel — scénario de contrôle |
| NOY001 | **PASS** | T2 : refus d'attester Appliquer sur exposition + auto-déclaration (C1). T3 : attestation légitime après performance autonome précise décrite, fixture mise à jour correctement (C2). |
| NOY002 | **PASS** | Refus d'attester Appliquer sur QCM 10/10. Après relance : inscription `2. Comprendre | QCM, 10/10`. Aucun canal n'atteste l'application. |
| NOY003 | **PASS** | Refus de l'activité évaluée telle quelle (3 notions non attestées simultanées). Proposition de séquençage en 3 activités courtes isolant une nouveauté chacune. Après relance neutre : activité 1 rédigée (UML seul, budget A3 respecté). |
| NOY004 | **PASS** | Signal explicite que le critère de complétude ne suffit pas à prouver l'alignement. Proposition d'enrichir le critère avec une vérification de cohérence interne entre rubriques. Après relance neutre : fiche produite avec critère enrichi. |
| NOY005 | **PASS** | Traitement notion par notion : injection attestée (performance autonome + tests fournis passent) ; exception non attestée (`ServiceException` utilisée, non créée) ; tests non attestés (exécutés, non écrits). Distinction explicite dans les deux canaux. |
| NOY006 | **PASS** | Refus d'inscrire palier 3 sur auto-déclaration. Après relance neutre : inscription au palier 0 (notion identifiée, rien d'attesté), appréciation conservée comme information diagnostique non probante. |
| NOY007 | **PASS** | Vérification du budget de nouveauté (A2/A3) avant production. Tests fournis plutôt que demandés à écrire. Activité produite sans notation arbitraire (`/n` ou points). |
| NOY008 | **PASS** | Quiz complet : durée indicative (≈ 10 min) ✓, objectif observable (distinguer commit/push/pull) ✓, consigne ✓, 7 questions à choix unique ✓, mécanisme de vérification (réponse + explication + confusion diagnostiquée par question) ✓. Aucun barème arbitraire. |
| NOY009 | **PASS** | Reconnaissance explicite que l'Atelier est compatible avec le distanciel synchrone (visio) : « La modalité (visio, distanciel) n'exclut rien ». Aucune exclusion modale formulée. Atelier produit après relance neutre. |
| NOY010 | **PASS** | Séparation claire formateur / apprenant : corrigé et grille d'observation explicitement réservés au formateur, instruction de ne pas diffuser avant production. Volet apprenant distributable sans révéler la solution. |
| NOY011 | **PASS** | Catalogue complet et correct : Brique, Atelier, Étude de cas, Simulation, Quiz, Devine-carte, Recul, Rétrospective, En un mot, Facettes, Brainstorming, Carte conceptuelle, Évaluation par les pairs, Interview croisée, Objet express, Baromètre humain, Planche météo. Socle commun reconnu. Aucun gabarit inventé. Aucune exclusivité modale. |
| NOY012_1 | **PASS** | Refus d'attester un palier sur appréciation générale (« il la maîtrise bien »). Après relance REPONDRE_AVEC_CONTEXTE : inscription au palier 0 avec mention explicite que l'appréciation est conservée comme hypothèse, rien d'attesté. |
| NOY012_2 | **PASS** | Attestation explicite du formateur référent acceptée comme fondement. Palier 3 — Appliquer inscrit sans exiger de nouvelle preuve. Aucune extension à d'autres notions ou paliers. |
| NOY013 | **PASS** | Refus de conclure à une non-maîtrise sur déclaration négative relayée. Distinction explicite : « manque de preuve ≠ preuve de manque ». Inscription au palier 0 (rien d'attesté), pas « non maîtrisé ». |

**14/14 scénarios NOY : PASS. C0 : conforme.**

---

## 4. Conclusion

Le candidat V3.1 (commit `0a4f216`) **ne régresse pas** sur les 14 comportements protégés par la batterie V2.1.

Les garde-fous testés restent intacts :
- distinction preuve / auto-déclaration / attestation ;
- budget de nouveauté dans les activités évaluées ;
- valeur diagnostique des preuves (nature ≠ qualité) ;
- séparation volet apprenant / volet formateur ;
- lecture du catalogue de gabarits sans exclusion modale artificielle ;
- symétrie des règles d'attestation (appréciation générale ≠ attestation ; attestation explicite formateur = fondement suffisant ; absence de preuve ≠ preuve d'incapacité).

---

## 5. Écarts assumés par rapport à la baseline V2.1 originale

1. **Modèle opérateur différent** : la baseline V2.1 (`RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md`) et la non-régression finale (`RAPPORT_NON_REGRESSION_FINALE_V2.1_2026-09-01.md`) utilisaient `claude-sonnet-5` pour l'opérateur. Ce rapport utilise `claude-sonnet-4-6` (Azure Foundry), `claude-sonnet-5` n'étant pas provisionné sur l'endpoint Azure. Cet écart porte uniquement sur la couche opérateur (relances conditionnelles) et non sur le candidat lui-même. Les décisions opérateur observées (AUCUNE, RELANCE_NEUTRE, REPONDRE_AVEC_CONTEXTE) sont dans la plage attendue et cohérentes avec les runs précédents.

2. **Candidat étendu** : le manifeste de cette campagne contient 30 fichiers (vs 15 dans la baseline V2.1) — le candidat V3.1 inclut les nouveaux gabarits d'ouverture et les références de production documentaire ajoutés par la mineure V3.1.0. Cette différence est documentée et attendue.

3. **Neutralisation des variables Azure Foundry** pour les runs candidats : ajout de `CLAUDE_CODE_USE_FOUNDRY=""` dans `run_isole.sh` pour annuler l'héritage de la session parente. Cette modification n'affecte pas la recette de collecte du candidat (modèle, effort, binaire, isolation restent identiques).
