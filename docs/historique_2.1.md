# Historique — candidat V2.1

Journal court des étapes réalisées sur le candidat V2.1. Mis à jour avant chaque commit touchant à ce candidat. Ordre chronologique inverse (le plus récent en premier).

---

## 2026-09-01 — Chantier §9 : instrumentation NOY014 — mécanisme partiellement démontré, un FAIL réel identifié

Exécution du chantier §9 de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` (instrument seul, **aucun fichier de `en_cours/` modifié**). Plan préalable : `docs/v2.1/PLAN_CHANTIER_NOY014_V2.1_2026-09-01.md`.

- Fixtures `mock_sans_derogation.md`/`mock_avec_derogation.md` réinstrumentées sur le mécanisme front matter (`perimetre:`/`deroge_a:`), corps de texte rendus strictement identiques. 3 nouvelles fixtures ajoutées (déclarations invalides ×2, périmètre neutre). Nouveau `CONTROLES_COMPLEMENTAIRES_NOY014.md`.
- Nouveau wrapper technique `tmp/run_check_noy014.sh` (non versionné) : injecte `references/mock.md` dans le skill isolé et recalcule le manifeste SHA-256, sans modifier `run_isole.sh` (recette figée).
- **6 runs joués : 5 PASS/conforme, 1 FAIL.** PASS : NOY014_1 (sans dérogation → noyau, après relance), NOY014_2 (dérogation valide → règle spécialisée appliquée), C0-bis (périmètre neutre → comportement inchangé), les deux déclarations invalides (aucune dérogation, noyau tient). Anti-gate (relecture NOY009) conforme.
- **FAIL sur le contrôle de non-extension hors périmètre (D3)** : une dérogation valide de `mock.md` s'est appliquée à une tâche ne mentionnant pas son périmètre déclaré. Le mécanisme de préséance posé au Lot B fonctionne sur les branches déjà couvertes mais **ne borne pas encore effectivement une dérogation à son périmètre**. Aucune correction tentée dans ce chantier (instrument seul ; une correction toucherait `SKILL.md`, donc hors périmètre, et poserait une question de conception — éviter de réintroduire un verbe de gate proscrit par R5).
- Conséquence : le point 5 des critères de sortie §11 du plan AMENDE_V2 (mécanisme de préséance intégralement démontré) **n'est pas atteint**. `NOY014_1`/`NOY014_2` restent suspendus du décompte officiel. Le Lot D et la V3 tutorat restent conditionnés à la résolution de ce FAIL.
- Ajout de `docs/v2.1/RAPPORT_CHANTIER_NOY014_V2.1_2026-09-01.md`.

## 2026-09-01 — Lot C : relocalisation des règles mal placées (étapes C.1-C.4)

Exécution du LOT C de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`. Deux relocalisations, aucune doctrine modifiée.

- Nouveau `en_cours/references/production_documentaire.md` : conventions de rédaction d'une fiche (périmètre, niveau de détail, séparation apprenant/formateur, callouts, réflexe andragogique), extraites de `decoupage_pedagogique.md` §4 (P11). `decoupage_pedagogique.md` §4 devient un renvoi ; `SKILL.md` référence la nouvelle source. Dispersion de I21 sur `activite.md`/`quiz.md` volontairement non nettoyée (hors périmètre du lot).
- `taxonomie.md` (A2) et `etat_des_paliers.md` : dé-duplication du seuil de la clause A3, qui n'était pas défini par `etat_des_paliers.md` mais s'y trouvait re-narré (P10). `etat_des_paliers.md` renvoie désormais explicitement à `taxonomie.md` §2 pour ce seuil.
- Contrôle statique (C.3) : CS6 = 0, CS9 = OK. Contrôle grep spécifique du plan (`"l'activité est refusée"` limité à `taxonomie.md`) non satisfaisable tel quel — cette formulation littérale n'a jamais existé dans `taxonomie.md`, seulement dans `etat_des_paliers.md` avant dé-duplication ; documenté sans correction, hors décision d'implémenteur (même famille que les écarts CS1/CS2/A.3 du lot A).
- **Non-régression comportementale (C.3) : 3/3 PASS (NOY003, NOY007, NOY010) et C0 conforme**, aucun incident technique. Runs joués et scorés par un sous-agent Sonnet dédié. Un rerun isolé de NOY010 après C.1 seule (consigne du plan sur le risque I21) déjà conforme avant même C.2.
- Écart d'instrumentation signalé sans correction : `validation/v2.1/baseline/kits/C0/dossier_operateur.md`, cité par le plan comme source de l'attendu C0, est absent du dépôt ; l'attendu a été pris à la source réellement autoritative référencée par le kit (`CONTROLE_STABILISATION_NOY014.md` §2).
- Ajout de `docs/v2.1/RAPPORT_IMPLEMENTATION_LOT_C_V2.1_2026-09-01.md`.

## 2026-09-01 — Lot B : périmètre et préséance déclarés en front matter (étapes B.1-B.6)

Exécution du LOT B de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`. Change la **doctrine d'implémentation** de la préséance, pas la doctrine G02 elle-même. Aucun oracle, fixture ou kit modifié.

- `en_cours/SKILL.md` l. 99 : suppression de « fait foi » et « spécialisée », qui portaient une transposition implicite de *lex specialis* ; la phrase est bornée au seul axe glossaire/norme et renvoie à la section dédiée (P5).
- `en_cours/SKILL.md` : le bloc « Préséance entre règles » quitte les contrôles de livraison (P12) et devient une section `## Périmètre et préséance`. Une dérogation n'existe plus que si le fichier la **déclare** (`deroge_a:` + `perimetre:` en front matter, identifiant pris dans un index fermé) — plus rien à inférer à l'exécution (P6, P7). Clause de signalement conservée mot pour mot.
- `en_cours/references/decoupage_pedagogique.md` : suffixe `*(règle R-GRAN)*` ajouté, proposition de la règle inchangée. `en_cours/references/activite.md` : puce sur la dérogation déclarée ajoutée au rôle du front matter.
- Neutralité vérifiée : aucune référence du runtime ne porte `deroge_a:` après le lot ; le mécanisme est posé mais activé nulle part.
- Contrôles statiques : les 8 contrôles obligatoires de B.2/B.3/B.4 conformes ; CS6 à 0 occurrence et CS9 « OK » (B.5).
- **Non-régression comportementale (B.6) : 14/14 PASS et C0 conforme**, aucun incident technique, aucun rerun. Conforme à la baseline. Runs joués et scorés par un sous-agent Sonnet dédié, contre les oracles de `validation/v2.1/non_regression/`.
- `NOY014_1`/`NOY014_2` non joués (consigne explicite de B.6 : leurs fixtures signalent la dérogation en prose, plus en front matter — elles ne testent plus le mécanisme cible et devront être réinstrumentées dans un cycle séparé).
- Ajout de `docs/v2.1/RAPPORT_IMPLEMENTATION_LOT_B_V2.1_2026-09-01.md` : détail des étapes, contrôles, verdicts, un écart de procédure consigné (C0 joué après B.4 et non après B.3 seule) et la réserve de portée (aucun run n'exerce le chemin « dérogation déclarée valide »).

## 2026-09-01 — Matériau de fond « psychologie cognitive » et axes de travail V3

Sans effet sur le runtime ni sur la promesse V2.1 : documentation hors noyau, pour l'écriture ultérieure de la promesse minimale V3.

- Ajout de `dossier-pedagogique/psychologie_cognitive_formation_tutorat.md` : 18 principes cognitifs de l'apprentissage et 12 biais cognitifs/métacognitifs, avec conséquences opérationnelles pour la conception d'activités et le comportement du tuteur.
- `en_cours/base_de_travail.md` §12 : ajout d'un pointeur vers ce document, sans modification de la liste des propriétés candidates.
- `en_cours/base_de_travail.md` : nouvelle section « Axes de travail V3 » (entre §4 et §5) — volet tutorat, extensibilité des activités sans modification du noyau, psychologie cognitive/biais. Distincte de la liste de propriétés candidates du §12 ; non encore développée ni priorisée.

## 2026-09-01 — Lot A : dé-duplication du noyau à doctrine constante (étapes A.1-A.12)

Exécution du LOT A de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`. Aucune doctrine créée, modifiée ou supprimée : des paraphrases deviennent des pointeurs vers une source unique. Non commité (A.13 en attente).

- `en_cours/SKILL.md`, `taxonomie.md` : suppression de deux paraphrases de « preuve externe rapportée », pointeurs vers `etat_des_paliers.md` (P2).
- `en_cours/references/opo.md` : nouvelle chaîne d'alignement canonique (union des 4 variantes concurrentes de P1, y compris les maillons propres à `taxonomie.md` A4 et `SKILL.md`). `SKILL.md`, `taxonomie.md` A4 et `glossaire.md` transformés en pointeurs vers cette source unique.
- `en_cours/references/glossaire.md` : définitions de Module/Séquence/Séance/Activité/Granularité et règle d'indépendance des axes de modalité réduites à un renvoi vers `decoupage_pedagogique.md` (prérequis de I25 à une seule source).
- `en_cours/SKILL.md`, `glossaire.md`, `activite.md` : I26 (`typical_uses`) et I25 (« Activité = granularité la plus fine ») ramenés chacun à une seule source portante dans le runtime (`activite.md` et `decoupage_pedagogique.md` respectivement).
- **~14 vérifications comportementales** exécutées pendant le lot (A.2 : NOY001 ; A.7 : NOY004/NOY002/NOY007 ; A.10 : C0 immédiat, point le plus à risque du lot ; A.12 : 10 scénarios) : **toutes conformes, aucune régression**, y compris sur le risque R2 (perte de visibilité) explicitement signalé par le plan comme le point le plus exposé.
- Trois écarts entre les attendus numériques du plan (CS1, CS2, A.3) et la réalité mesurée, tous retracés à des erreurs de comptage de l'auteur du plan (pas des défauts d'exécution) et consignés en détail dans le rapport.
- Contrôles intra-lot exécutés via `scripts/run_isole.sh` directement (pas `run_baseline.sh`, dont le garde-fou de propreté git est incompatible avec un état intermédiaire non commité) — brique explicitement prévue pour cet usage. Script utilitaire non versionné `tmp/run_check.sh` (`tmp/` ajouté au `.gitignore`).
- Ajout de `docs/v2.1/RAPPORT_IMPLEMENTATION_LOT_A_V2.1_2026-09-01.md` : détail complet étape par étape, verdicts et clause d'oracle par run, écarts documentés, contrôle statique CS1-CS9.

## 2026-09-01 — Baseline comportementale V2.1 exécutée et scorée (lot 0, étapes 0.4-0.9)

`./scripts/run_baseline.sh` lancé sous `david` : 15 runs (C0 + 14 NOY, `NOY014_1`/`NOY014_2` hors baseline) joués dans des copies isolées avec relance opérateur Sonnet aveugle, tous `COLLECTE_COMPLETE`, aucune anomalie, aucun scénario suspendu. `en_cours/` vérifié strictement identique à HEAD (`01e9ca1`) avant et après.

Scoring effectué manuellement (étape 0.7) contre les oracles de `validation/v2.1/non_regression/` : **14/14 PASS + C0 conforme**, aucun rerun nécessaire (étape 0.8 sans objet). `NOY012_2` — le scénario que l'implémentation M1-M7 de l'attestation formateur visait spécifiquement à corriger — confirmé PASS, sans régression sur les scénarios voisins à risque (`NOY001`, `NOY006`, `NOY012_1`).

Ajout de `docs/v2.1/RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md` (étape 0.9) : commit et intégrité de `en_cours/`, SHA-256 des 15 copies isolées (identiques entre elles et à `en_cours/`), verbatim complet et clause d'oracle appliquée pour chacun des 15 runs, statut « run de référence » pour l'ensemble (environnement `david`/`CLAUDE_CONFIG_DIR` isolé, distinct de la session de développement), rappel du motif de suspension de `NOY014` (R1-b, R1-e), aucune dette d'instrumentation majeure constatée. Ce rapport remplace `RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md` comme référence de non-régression pour les lots suivants.

## 2026-08-31 — Environnement d'exécution `claude-test` (collector-kit) et correction du collector

Concerne uniquement les runs exécutés via `collector-kit` (utilisé pour les dry-runs NOY012/NOY013). **Sans effet sur le harnais de baseline** (`scripts/run_baseline.sh`), qui reste sous le compte `david` avec sa propre isolation par run — voir entrée « Lot 0 » ci-dessous. Aucun run lancé dans ce lot.

- `validation/collector-kit/commands/bloc1.md` et `bloc2.md` : correction de 3 chemins obsolètes vers `collect_run.py` (`/projets/skill/tuteur-ingenierie-pedagogique/` → `…-v2/`). Le chemin cité n'existait pas : l'opérateur aurait échoué dès la première commande du bloc 1.
- `validation/CLAUDE.md`, section « Données lourdes » : documentation du transfert des artefacts depuis `claude-test` pour les runs `collector-kit`, avec rappel explicite que le harnais de baseline n'est pas concerné. Les comptes `claude-test`/`david` sont cloisonnés (`/home/claude-test` en `drwxr-x---`, `/projets/skill/tests/` non inscriptible par `claude-test`), donc ni pull ni push direct n'est possible. Le transfert passe par un point de dépôt neutre `/projets/tests/inbox` (sticky) : `claude-test` dépose, `david` classe dans `archives/`. Décision explicite de ne pas fusionner les groupes, l'isolation faisant partie du dispositif.
- Précisé que `collect_run.py` doit tourner sous `claude-test` pour que `--claude-root` (défaut `~/.claude/projects`) pointe sur la bonne trace de session, et que `--output-root` / `--prompt-file` visent l'espace de `claude-test`.
- Rien ajouté au collector-kit lui-même : son `CLAUDE.md` interdit d'y introduire une règle propre à ce skill lorsqu'elle peut rester dans le protocole de campagne.

## 2026-08-23 — Lot 0 : durcissement du harnais de baseline (deux tours de revue)

Deux tours de revue du harnais de baseline (`scripts/run_baseline.sh`, `scripts/relance_operateur.sh`, `scripts/generer_kits_baseline.py`), avant tout lancement officiel. **Aucun run de baseline exécuté. `en_cours/` et les 16 fiches NOY strictement inchangés.**

- **Parseur des dossiers opérateur** : `section()`/`bloc_apres()` (`generer_kits_baseline.py`) ignoraient l'état des blocs ```` ``` ```` : un titre Markdown cité à l'intérieur d'une fixture (ex. `# État des paliers` dans `NOY001.md` l.63-68) était pris pour une borne de section, laissant 7 des 14 `dossier_operateur.md` avec des fences déséquilibrées. Corrigé par `etats_fence()` (suivi de parité par ligne) ; contrôle automatique de fences équilibrées ajouté en fin de script. Fidélité systématique des 15 kits revérifiée après coup (tous les extraits restent des sous-chaînes exactes de leur fiche source).
- **NOY005** : la consigne opérateur de la fiche contenait une clause dépendant de la connaissance de l'oracle (« si l'agent a déjà produit assez d'éléments pour appliquer l'oracle »), transmise littéralement à l'opérateur Sonnet aveugle — seule fiche concernée sur 14. Traitement en deux temps : d'abord retrait simple du paragraphe (tour 1), puis remplacement par une instruction opératoire neutralisée générique — « si la décision requiert un critère évaluatif volontairement masqué, rends AMBIGU_OPERATEUR plutôt que de supposer » (tour 2, sur demande explicite de préserver le signal sans révéler l'oracle). La fiche source n'a jamais été modifiée ; `regle_relance.txt` (destiné à l'humain arbitrant) conserve la clause intacte ; trace d'audit dans `redactions.txt`.
- **Propreté de `en_cours/`** : `git diff --quiet -- en_cours/` ne voyait ni une modification déjà stagée, ni un fichier non suivi. Remplacé par `git status --porcelain --untracked-files=all -- en_cours/` dans `run_baseline.sh`.
- **Codes retour** : seul RC=65 (intégrité du candidat) était traité ; tout autre code non nul (incident technique) était silencieusement traité comme un tour réussi. Pire, RC=65 lui-même laissait le script continuer vers la couche opérateur après le `break` (régression latente trouvée en corrigeant). Corrigé dans `run_baseline.sh` et `relance_operateur.sh` : RC≠0 (65 ou autre) suspend désormais le scénario avant tout traitement ultérieur (opérateur, décision, fichiers lus, fixtures finales).
- **Incident opérateur ≠ ambiguïté** : un échec technique de `operateur_sonnet.sh` (RC≠0) retombait dans la même branche que `AMBIGU_OPERATEUR`, confondant panne et jugement. Séparé : RC≠0 suspend immédiatement le scénario (stdout/stderr conservés) avant toute lecture de `decision.txt` ; le cas RC=0 avec sortie non parseable continue de router vers `AMBIGU_OPERATEUR` avec anomalie de format consignée (repli validé, pas une nouvelle catégorie).
- **Répertoire de run ≠ scénario terminé** : un simple `[ -d "$RUN" ]` valait « déjà joué ». Remplacé par un état explicite par marqueur : `COLLECTE_COMPLETE` (terminé, ignoré à la relance), `SCENARIO_SUSPENDU.md` (incident, jamais rejoué silencieusement), `DECISION_OPERATEUR_REQUISE.md` (arbitrage en attente), et répertoire sans aucun de ces marqueurs → `ANOMALIE_ETAT_INCONNU.md` (run interrompu anormalement). Le résumé final recalcule `COMPLETS/TOTAL` sur le système de fichiers et le script sort en erreur si la campagne n'est pas intégralement complète.
- **Incident de manipulation, clos** : un test du harnais a omis `BASELINE_ROOT`, écrivant des données factices (« réponse factice ») dans le chemin par défaut réel `/projets/skill/tests/baseline_v2.1_2026-08-23`. Repéré immédiatement, contenu vérifié comme purement factice, supprimé ; racine officielle confirmée propre. Conservé ici comme trace, sur demande explicite.
- Tous les smoke tests ont été joués dans des clones Git jetables avec `run_isole.sh`/`operateur_sonnet.sh` bouchonnés (aucun appel réseau, aucun scénario officiel). Kits régénérés et revérifiés après chaque tour : 14/14 fences équilibrées, déterminisme confirmé, `bash -n`/`py_compile` sans erreur.

## 2026-08-23 — Lot 0 : harnais d'exécution de la baseline comportementale

Préparation du lot 0 de la refactorisation, sur la base de `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` (versé au dépôt ici, il n'y figurait pas). **Aucun run de baseline n'a été exécuté** ; `en_cours/` et les 16 fiches NOY sont intacts.

- **Étapes 0.1 à 0.3 réalisées.** `scripts/controle_statique_refactoring.sh` (CS1–CS9) créé et joué. Écart constaté et consigné sans traitement : CS2 remonte 5 porteurs de la chaîne d'alignement au lieu des 3 annoncés par le plan — les deux supplémentaires sont `activites_type/atelier.md` l. 88 et `activites_type/brique.md` l. 126, à réexaminer sur P1/A.3–A.7 après la baseline.
- **Recette d'exécution isolée** (`scripts/run_isole.sh`), vérifiée par préflight technique non scoré : `CLAUDE_CONFIG_DIR` dédié par run, seules les credentials reprises du profil de développement, `/home/david/.claude` inchangé (empreinte avant/après identique), aucun `CLAUDE.md`, skill, plugin, hook, agent, commande ni mémoire hérité, multi-tours fonctionnel.
- **Trois défauts trouvés au préflight et corrigés :**
  1. `en_cours/CLAUDE.md`, présent dans le dossier du skill, est **injecté en contexte système** dès que le skill est utilisé (prouvé par canari sur copie jetable) et énumère les invariants testés par NOY001-004/006/007 — un aide-mémoire de l'oracle dans chaque run de condition A. Le paquet candidat est réduit au runtime (`SKILL.md` + `references/`). Le protocole V2 copiant `en_cours/` entier, la campagne V2 a vraisemblablement tourné avec cette contamination ; constat consigné, archive non réécrite.
  2. En mode `--print`, `permission mode: default` **refuse les écritures**, ce qui aurait vidé de leur observable les six scénarios exigeant une mise à jour de l'état des paliers. Bascule en `acceptEdits`, l'invariance du candidat étant garantie autrement (voir ci-dessous).
  3. Le binaire 2.1.232 du paramètre autoritatif V1/V2 n'est plus installé ; 2.1.241 épinglé.
- **Invariance du candidat** : sous-arbre du skill en lecture seule (`chmod a-w`) et manifeste SHA-256 vérifié avant et après chaque tour ; toute modification renvoie le code 65 et pose un marqueur `INVALIDE`. Garde-fou éprouvé en conditions réelles.
- **Kits d'exécution** (`validation/v2.1/baseline/kits/`, 15 scénarios) **générés par extraction** des blocs de code des fiches autoritatives (`scripts/generer_kits_baseline.py`), jamais recopiés à la main.
- **Runner automatisé** (`scripts/run_baseline.sh`) : une commande, 15 sessions fraîches et isolées, collecte des verbatims, des fixtures finales et des fichiers réellement ouverts (extraits de la trace, jamais demandés à l'agent). Il collecte et ne score pas. NOY014_1/NOY014_2 hors baseline (§9).
- **Couche opérateur Sonnet aveugle** (`scripts/operateur_sonnet.sh`, `validation/v2.1/baseline/prompt_operateur.md`) : rend le jugement d'opérateur que les fiches subordonnent à une appréciation, avec quatre décisions (`AUCUNE`, `REPONDRE_AVEC_CONTEXTE`, `RELANCE_NEUTRE`, `AMBIGU_OPERATEUR`) et une seule intervention par scénario. Aveuglement par construction : dossier bâti par liste blanche de sections, cwd vide, tous les outils interdits. Paramètres figés `claude-sonnet-5` / effort `high`, distincts du candidat (`medium`). L'opérateur ne score jamais. `AMBIGU_OPERATEUR` suspend le scénario pour arbitrage humain (`scripts/relance_operateur.sh`).
- **Deux corrections apportées à AMENDE_V2**, datées dans le document : la règle « aucun persona » du §8.2, erronée, contredisait huit fiches dont six où le persona est une clause de validité technique — le persona est désormais injecté exactement lorsque la fiche le prescrit ; et la prescription de réinitialiser physiquement `/home/david/.claude` est écartée au profit du `CLAUDE_CONFIG_DIR`, le plan ouvrant lui-même la voie à un « mécanisme équivalent ».
- **Dettes consignées, non traitées** : les chemins de fixtures portent l'identifiant du scénario (`apprenant-noy001.md`) alors que le §0.5 interdit de le transmettre à l'exécutant ; les consignes opérateur de NOY008, NOY009 et NOY010 nomment ce que le test observe, conservées parce qu'il s'agit d'interdictions protectrices ; `validation/CLAUDE.md` l. 57 cite encore la session `claude-test`, caduque.

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
- **Régularisation Git postérieure (2026-08-23)** : `RAPPORT_CYCLE_R1_V2.1_2026-08-23.md` et le bandeau « CADUC » de `PLAN_CORRECTION_R1_V2.1_2026-08-23.md` avaient été omis du commit `633173d`. Ils sont committés à part, sans modification de leur contenu, pour clore le cycle R1 avant l'ouverture du refactoring.

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
