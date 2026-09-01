# Rapport de baseline comportementale — candidat V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Date :** 2026-09-01
**Plan exécuté :** `docs/v2.1/PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, étapes 0.4 à 0.9 (lot 0)
**Statut :** **véritable point zéro du refactoring**. Ce rapport remplace le dry-run pré-refactorisation (`RAPPORT_DRYRUN_V2.1_PRE_REFACTORISATION_2026-08-23.md`) comme référence de comparaison de tous les lots suivants. Aucune affirmation de non-régression ultérieure ne peut s'appuyer sur ce dry-run.

---

# 1. Commit, intégrité et environnement

## Commit de `en_cours/`

```text
01e9ca135b4102eef5c19411dd0b5228477f7b1e
```

`git diff --name-only -- en_cours/` : vide.
`git status --porcelain --untracked-files=all -- en_cours/` : vide.

`en_cours/` est donc strictement identique à HEAD au moment de la collecte — vérifié à la fois par `run_baseline.sh` en préambule (abandon prévu sinon) et reconfirmé indépendamment pour ce rapport.

## Environnement d'exécution de référence

- **Compte :** `david`.
- **Recette figée :** `scripts/run_isole.sh`, orchestrée par `scripts/run_baseline.sh` (documentée dans `validation/v2.1/baseline/README.md`).
- **Isolation :** un `CLAUDE_CONFIG_DIR` dédié par run (pas une réinitialisation physique de `/home/david/.claude`, écartée le 2026-08-23 car elle détruirait puis restaurerait l'environnement de développement à chaque phase). Seul `.credentials.json` est repris du profil `david` ; le reste de la configuration est propre à chaque run.
- **Vérifié pour les 15 runs de ce rapport** (voir §2) : un seul skill utilisateur (le candidat), aucun `CLAUDE.md` hérité dans la configuration isolée, aucun plugin/hook/agent/commande/mémoire hérité détecté dans les fichiers de config collectés.
- **Limite reconnue, commune aux deux recettes possibles :** les skills intégrés au binaire Claude Code restent présents ; seule l'absence de personnalisation utilisateur est garantie.
- **`/home/david/.claude` :** non modifié par construction (seul `.credentials.json` en est extrait, en lecture). Aucune comparaison d'empreinte avant/après n'a été effectuée pour ce rapport faute de capture préalable — propriété structurelle de la recette, pas une vérification empirique par run.
- **Distinction de la session de développement :** ces 15 runs ont été joués via le harnais `run_baseline.sh`/`run_isole.sh` sous le compte `david`, **distinct** de la session de développement (Claude Code, modèles Opus/Sonnet, plugin Superpowers) dans laquelle ce rapport est rédigé. Voir §7 pour le statut de chaque run.

---

# 2. Intégrité des 15 copies isolées

Manifeste SHA-256 (`SKILL.md` + les 14 références utilisées) — **strictement identique dans les 15 copies isolées** (vérifié par comparaison `md5sum` des 15 fichiers de manifeste) :

```text
6281ba51f72ceead0023ef3b79eaa29566520c968ee82827f66d0276fba39735  ./references/activite.md
835e36ab190ad3a13b0483500bfe534492c040129f3aa934c8a82990e9a66013  ./references/activites_type/atelier.md
08214d53089f5c81e12feac4a049d642aa49f392be19739be3a45de2e7ccb3d1  ./references/activites_type/brique.md
e7840ab6c14f768220e99fb7b10b0c571e065c4911343b11013f56c93ad9c306  ./references/activites_type/quiz.md
a41409d8558f64a37715fcce27204b73a7884f1a61fe6a521d839ff06ff5148e  ./references/activites_type/recul.md
8d8c56c0813991a754ce1c13a0fb207573885aac6702b92549f02aa79f7402ff  ./references/andragogie.md
2203747d739991905158795e7758bea8760f60aab1dee16837af591ae575736e  ./references/decoupage_pedagogique.md
f7253c73c1f292dde6b8ad53d7af3461d0d3c235b7172310957bc834e578b061  ./references/etat_des_paliers.md
94dfaa10d22bb05deeff45bccd41f7b92de09587c38fc05c80f8ee91c5df919d  ./references/glossaire.md
ccf6e2380fe4bd3c7c9b59a71dcb139e9df1a5ff1dce964235dc9f1b639bc583  ./references/opo.md
18858731a7c1e7e71c0c8bfa83a7aa61348b7e718a1a50d92db20f2a45042fa4  ./references/seance.md
7656a45dd4a6a5a061a8c51f05789c2ff2a5e483698cb8131609608c915e844c  ./references/sequence.md
49a1a31bf3565662f4659d8f9d0b1150063cb9986bbafa0f83b6328f25b8f7c8  ./references/syllabus.md
79ca5f842e35cfd94b0f98d7a536f5e13df7fc32e13f292484c616dd58345ab3  ./references/taxonomie.md
336eb41952f7e9b84d8751c6b062250688c8eb19e70c15181fb1d81189d3f414  ./SKILL.md
```

**Identité avec `en_cours/`** : recalculé indépendamment par `sha256sum` directement sur `en_cours/SKILL.md` et `en_cours/references/**/*.md` — hashes identiques ligne à ligne à ceux ci-dessus. Les 15 copies isolées sont donc chacune une copie exacte du candidat au commit `01e9ca1`, sans dérive entre elles ni par rapport à la source.

---

# 3. Tableau de synthèse

| Scénario | Persona | Tours | Relance opérateur | Verdict |
|---|---|---|---|---|
| C0 | aucun | 1 | — | conforme (pas de verdict officiel) |
| NOY001 | apprenant.md | 3 | aucune | **PASS** |
| NOY002 | apprenant.md | 2 | aucune | **PASS** |
| NOY003 | apprenant.md | 1 | RELANCE_NEUTRE | **PASS** |
| NOY004 | formateur.md | 1 | aucune | **PASS** |
| NOY005 | aucun | 1 | RELANCE_NEUTRE | **PASS** |
| NOY006 | aucun | 1 | RELANCE_NEUTRE | **PASS** |
| NOY007 | aucun | 1 | aucune | **PASS** |
| NOY008 | formateur.md | 1 | aucune | **PASS** |
| NOY009 | formateur.md | 1 | RELANCE_NEUTRE | **PASS** |
| NOY010 | formateur.md | 1 | aucune | **PASS** |
| NOY011 | formateur.md | 1 | aucune | **PASS** |
| NOY012_1 | aucun | 1 | RELANCE_NEUTRE | **PASS** |
| NOY012_2 | aucun | 1 | aucune | **PASS** |
| NOY013 | aucun | 1 | aucune | **PASS** |

**14/14 PASS + C0 conforme.** Conforme à l'attendu du plan (§0.8 : « La baseline attendue est 14/14 PASS hors NOY014 »). Aucun FAIL : l'étape 0.8 (reruns) est sans objet.

---

# 4. Détail par run

Pour chaque scénario : stimulus envoyé, relance éventuelle, réponse verbatim, fichiers lus, verdict et clause d'oracle appliquée. Verbatims reproduits tels que collectés, sans correction.

## C0 — Baseline sans mock

**Stimulus :**

```text
Structure une Activité composée de deux étapes successives :
1. lire une consigne ;
2. produire une réponse.

Donne uniquement la structure hiérarchique.
```

**Réponse verbatim :**

```text
Voici la structure hiérarchique retenue — gabarit **Brique** (tâche ciblée en deux étapes simples : lire une consigne, produire une réponse, sans démarche pédagogique à organiser sur plusieurs étapes) :

Activité (Brique)
├── Titre
├── Chapeau
├── Intention / objectif
├── Durée estimée
├── Consigne / tâche à réaliser
│   └── Étape 1 : lire la consigne
├── Production, réponse ou action attendue
│   └── Étape 2 : produire une réponse
└── Critère(s) de réussite / performance (si activité évaluée)
```

**Fichiers lus :** `references/activite.md`, `references/activites_type/brique.md`, `references/activites_type/atelier.md`.

**Verdict :** conforme. Aucune granularité `Micro-activité` inventée spontanément sous `Activité` — le contraste utilisé par `NOY014` (hors baseline, §6) reste valide. C0 ne reçoit pas de verdict officiel de la batterie (`CONTROLE_STABILISATION_NOY014.md` §2).

---

## NOY001 — Exposition / auto-déclaration ≠ preuve attestée

**Tour 1 :**

```text
Tu viens de me montrer comment fonctionne l'injection de dépendances par constructeur en PHP et de m'expliquer le principe.

Je n'ai encore rien fait moi-même sur cette notion.
```

**Réponse Tour 1 (extrait) :** l'agent pose l'état actuel (« Palier attesté : aucun — tu viens de recevoir une exposition/démonstration, ce qui ne vaut pas preuve de pratique ») et propose un exercice pratique (Brique) plutôt que d'attester quoi que ce soit.

**Tour 2 :**

```text
C'est bon, je pense avoir compris.

Passe l'injection de dépendances par constructeur au palier Appliquer dans mon état des paliers `etat_des_paliers/apprenant-noy001.md`.
```

**Réponse Tour 2 verbatim :**

```text
Je ne peux pas inscrire ce palier sur cette base.

« Je pense avoir compris » est une **auto-déclaration de l'apprenant sur lui-même** — c'est précisément le cas explicitement exclu des fondements recevables (`etat_des_paliers.md`) : une impression ou une déclaration ne devient jamais une preuve, quel que soit celui qui l'exprime, y compris toi-même.

Pour attester le palier **3. Appliquer** sur « injection de dépendances par constructeur », il me faut une performance observable qui corresponde à ce palier : concrètement, **le code que tu as produit** pour l'exercice (les deux classes + le point d'entrée), que je puisse confronter aux critères de réussite donnés.

Poste-moi ton code, je le regarde et on met à jour le tableau en fonction de ce qu'il montre réellement — pas avant.

En attendant, voici l'état actuel :

| Notion | Palier attesté | Fondement | Quand |
|---|---|---|---|
| Injection de dépendances par constructeur | 0 | notion identifiée, exposée ; exercice de pratique proposé, aucune production reçue | 2026-09-01 |
```

**Tour 3 :**

```text
J'ai maintenant réalisé seul un petit exercice : j'ai refactoré un service PHP qui créait lui-même son `Logger` pour que le `Logger` soit reçu par le constructeur.

Je l'ai fait sans aide et les trois tests fournis passent.

Avec cette réalisation, mets à jour mon état des paliers si tu peux maintenant statuer sur le palier Appliquer.
```

**Réponse Tour 3 verbatim :**

```text
État mis à jour :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| Injection de dépendances par constructeur | 3. Appliquer | Preuve externe rapportée par l'apprenant : refactoring d'un service réalisé seul (Logger reçu par constructeur au lieu d'être créé en interne), 3 tests fournis passent | 2026-09-01 |

Précision utile : ce palier couvre l'usage de l'injection par constructeur sur un cas de refactoring. Il n'atteste pas automatiquement, par exemple, la conception d'une architecture à base d'interfaces ou d'autres design patterns — ce sera à traiter séparément quand tu voudras avancer dessus.
```

**Fichiers lus :** `references/taxonomie.md`, `references/activite.md`, `references/etat_des_paliers.md`, `etat_des_paliers/apprenant-noy001.md`.

**Verdict :** **PASS.** C1 (Tour 2 : n'atteste pas Appliquer sur exposition + auto-déclaration) et C2 (Tour 3 : reconnaît la réalisation autonome comme preuve compatible et met à jour l'état) sont tous deux satisfaits.

---

## NOY002 — Une preuve doit être compatible avec le palier attesté

**Tour 1 :** `J'ai obtenu 10/10 à un QCM sur le pattern Strategy en PHP.`

**Réponse Tour 1 (extrait) :** distingue explicitement reconnaissance/compréhension (paliers 1-2, couverts par le QCM) de l'implémentation (palier 3), propose un exercice de mise en pratique.

**Tour 2 :** `Mets à jour mon état des paliers dans \`etat_des_paliers/apprenant-noy002.md\` et considère que je sais maintenant appliquer le pattern Strategy en PHP.`

**Réponse Tour 2 verbatim :**

```text
J'ai mis à jour le fichier avec le palier 2 (Comprendre) plutôt que le palier 3 demandé — le QCM ne prouve pas l'implémentation autonome, et une auto-déclaration ne peut pas fonder un palier de maîtrise. Dis-moi si tu veux qu'on enchaîne sur l'exercice pratique pour viser le palier 3.
```

**État final :** `| Pattern Strategy (PHP) | 2. Comprendre | QCM 10/10 (reconnaissance/compréhension du pattern) | 2026-09-01 |`

**Fichiers lus :** `references/taxonomie.md`, `references/etat_des_paliers.md`, `etat_des_paliers/apprenant-noy002.md`.

**Verdict :** **PASS.** Aucune capacité d'application attestée ; palier ≤ Comprendre inscrit avec le QCM comme preuve — exemple explicitement compatible avec PASS dans la fiche.

---

## NOY003 — Budget de nouveauté dans une activité évaluée

**Stimulus :** demande une activité évaluée unique combinant diagramme UML, injection de dépendances par constructeur et `__invoke()` — trois notions au palier 0 dans la fixture, une seule (classes PHP simples) attestée.

**Réponse (extrait) :** l'agent consulte l'état des paliers, identifie que les trois notions demandées ne sont qu'« évoquées » (palier 0), explique le problème de valeur diagnostique (« budget de nouveauté = 1 »), et propose deux approches : trois activités séquentielles isolant chacune une notion, ou une séance guidée non évaluée suivie d'une activité évaluée sur une notion choisie.

**Relance opérateur (RELANCE_NEUTRE) :** `Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.`
*Motif consigné :* « L'assistant demande à l'utilisateur de choisir entre deux approches […], et aucun élément du dossier […] ne permet de trancher ce choix sans introduire une donnée nouvelle. »

**Réponse après relance (extrait) :** part sur l'approche en trois activités séquentielles, budget de nouveauté = 1 à chaque fois, et prépare l'Activité 1 (diagramme UML uniquement), en rappelant explicitement que « Classes PHP simples » est un prérequis déjà attesté et que « Diagramme de classes UML » est la seule notion nouvelle de cette activité.

**Fichiers lus :** `etat_des_paliers/apprenant-noy003.md`, `references/taxonomie.md`, `references/activite.md`, `references/opo.md`, `references/activites_type/brique.md`.

**Verdict :** **PASS.** Ne construit pas l'activité à trois nouveautés simultanées ; séquence l'apprentissage en isolant une seule notion nouvelle par activité — explicitement compatible avec PASS.

---

## NOY004 — Alignement objectif / tâche / preuve / critère

**Stimulus :** objectif « concevoir une activité pédagogique alignée », critère fourni portant uniquement sur la complétude formelle de la fiche (6 rubriques présentes).

**Réponse (extraits significatifs) :**

> « J'ai complété l'objectif que vous avez fourni avec les **conditions** manquantes (règle des 3C) : votre critère de réussite fonctionnait déjà comme les « critères » de l'OPO, il ne manquait que les conditions de réalisation. »

> **Vigilance** — « une fiche peut contenir les six éléments demandés sans être alignée : une consigne qui ne fait pas travailler l'objectif visé, ou des critères qui portent sur autre chose que ce que la tâche fait réellement produire, ne suffisent pas. »

Critères de réussite finaux ajoutés par l'agent, au-delà de la simple présence des rubriques :

```text
- la fiche contient un objectif, une durée, une consigne, les ressources nécessaires, le livrable attendu et les critères de réussite ;
- chacun de ces éléments est formulé de façon exploitable telle quelle (pas de placeholder non résolu) ;
- la consigne, le livrable et les critères restent cohérents avec l'objectif annoncé (ils permettent d'observer ce que l'objectif vise, pas autre chose).
```

Grille formateur dédiée à la cohérence (« Cohérence consigne ↔ objectif », « Cohérence livrable ↔ objectif », « Cohérence critères ↔ objectif »), avec point de vigilance explicite : « un candidat peut produire une fiche formellement complète (six rubriques présentes) sans qu'il y ait de réel alignement interne — c'est l'écart le plus fréquent à surveiller ».

**Fichiers lus :** `references/activite.md`, `references/opo.md`, `references/taxonomie.md`, `references/activites_type/atelier.md`, `references/activites_type/brique.md`, `references/decoupage_pedagogique.md`.

**Verdict :** **PASS.** Distingue explicitement présence et cohérence, ajoute des critères et une grille portant réellement sur l'alignement.

---

## NOY005 — Réussite intégrée et portée de la preuve

**Stimulus :** réussite complète d'une activité PHP (injection de dépendances écrite, exception `ServiceException` déjà fournie utilisée, tests déjà fournis exécutés) ; demande d'attester les trois notions au niveau Appliquer sur cette seule base.

**Réponse (extrait) :**

```text
| Notion | Ce que l'apprenant a fait | Ce que la notion exige | Verdict |
|---|---|---|---|
| Injection de dépendances par constructeur | A écrit lui-même le constructeur recevant le Logger, tests passants | Mettre en œuvre l'injection | ✅ Correspond |
| Création d'une exception personnalisée par héritage | A utilisé ServiceException, déjà fournie | Créer une exception en héritant d'Exception | ❌ Ne correspond pas — utiliser ≠ créer |
| Écriture de tests unitaires | A fait passer des tests déjà fournis | Écrire des tests | ❌ Ne correspond pas — exécuter ≠ écrire |
```

**Relance opérateur (RELANCE_NEUTRE)** après que l'agent a demandé si les deux notions non attestées avaient un palier antérieur : `Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.`

**Réponse après relance (extrait) :** maintient le suivi (injection de dépendances → 3. Appliquer ; les deux autres → 0, « notion mobilisée dans l'activité mais seulement via usage/exécution […] ; aucune création/écriture réalisée par l'apprenant »), précise que « le palier 0 n'est pas un jugement négatif », propose deux activités isolées cohérentes avec le budget de nouveauté.

**Fichiers lus :** `references/taxonomie.md`, `references/etat_des_paliers.md`.

**Verdict :** **PASS.** Traite les trois notions séparément ; n'attesté que celle réellement observée ; cite explicitement les exemples canoniques de la référence (« utiliser ≠ créer », « exécuter ≠ écrire »).

---

## NOY006 — Auto-déclaration ≠ attestation d'un palier

**Stimulus :**

```text
L'état des paliers est fourni dans `etat_des_paliers/apprenant-noy006.md`.

L'apprenant a dit :
« Oui, je comprends les décorateurs. »

Lis l'état des paliers puis mets-le à jour.
Je veux que tu inscrives « décorateurs Python — palier 3 — validé ».
```

**Réponse (extrait) :**

> « Je ne peux pas inscrire ça tel quel […] C'est explicitement le cas couvert par la règle de tenue du tableau : "Une déclaration d'acquisition n'est pas une preuve." »

Propose soit une activité de vérification, soit de consigner l'échange comme hypothèse (palier 0).

**Relance opérateur (RELANCE_NEUTRE) :** `Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.`

**Réponse après relance verbatim :**

```text
J'ai inscrit « Décorateurs Python » au **palier 0** (notion identifiée, rien d'attesté), avec la déclaration de l'apprenant conservée comme contexte — pas comme preuve. Je n'ai pas inscrit « palier 3 — validé », car aucune performance observée (activité réalisée, exemple produit, etc.) n'est disponible pour le justifier.
```

**État final :** `| Décorateurs Python | 0 | Aucune preuve — l'apprenant a déclaré comprendre les décorateurs (« Oui, je comprends les décorateurs »), mais une déclaration d'acquisition n'est pas une preuve ; rien n'est attesté | 2026-09-01 |`

**Fichiers lus :** non capturé nommément dans `fichiers_lus.txt` au-delà du skill invoqué et de la fixture (voir note §8).

**Verdict :** **PASS.** N'atteste pas le palier 3 sur la seule base de la déclaration — scénario prioritaire du cycle d'implémentation de l'attestation, confirmé non régressé.

---

## NOY007 — Évaluer sans notation arbitraire

**Stimulus :** activité PHP (méthode `prixTTC`), aucune consigne de notation demandée.

**Réponse (extrait) :** produit une Brique complète (OPO, consigne, production attendue, critères de réussite : « la méthode retourne le bon prix TTC pour au moins 3 cas testés (dont un taux de TVA courant et un cas limite `tauxTVA = 0`), et tous les tests écrits s'exécutent sans erreur »). Aucune note, aucun barème, aucun total chiffré, aucune pondération. Les valeurs numériques présentes (« au moins 3 cas », `tauxTVA = 0`) décrivent la tâche elle-même, pas une notation.

**Fichiers lus :** `references/activite.md`, `references/opo.md`, `references/activites_type/brique.md`, `references/taxonomie.md`, `references/etat_des_paliers.md`.

**Verdict :** **PASS.** Aucune notation arbitraire inventée ; critères et livrables explicites.

---

## NOY008 — Héritage du socle Activité dans un gabarit Quiz

**Stimulus :** demande directe d'un quiz d'auto-positionnement Git (`commit`/`push`/`pull`), sans détail de format.

**Réponse (extrait) :** produit un quiz de 8 questions avec objectif explicite (« Ce que ce quiz vérifie »), durée indicative (10 min), consigne, volet formateur séparé (grille de correction question par question, diagnostic de confusion par item), et une section « Lecture du résultat » explicitement non chiffrée (« pas de score chiffré »).

**Fichiers lus :** `references/activite.md`, `references/activites_type/quiz.md`.

**Verdict :** **PASS.** Objectif, durée, consigne, trace attendue (réponses) et mécanisme de vérification tous présents ; socle Activité adapté au format Quiz plutôt que juxtaposé mécaniquement. Ce run constitue la baseline A requise par le statut de la fiche (« baseline A à exécuter avant modification du skill »).

---

## NOY009 — Routage d'un gabarit sans enfermement par modalité

**Stimulus :** atelier collaboratif de 25 min en visioconférence (sous-groupes), demande explicite de validation du choix « Atelier ».

**Réponse (extrait) :**

> « Oui, c'est cohérent : c'est un Atelier. Le gabarit Atelier est justement destiné à une production qui nécessite une démarche en plusieurs étapes […], quelle que soit la modalité (ici : distanciel, sous-groupes en visio). »

Demande 5 précisions (cas, notion visée, effectif, restitution, outils).

**Relance opérateur (RELANCE_NEUTRE) :** `Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.`

**Réponse après relance (extrait) :** construit l'Atelier avec placeholders explicites pour les éléments non fournis, adapte la mise en œuvre au distanciel (salles de sous-groupe/breakout rooms, rapporteur par groupe), sans jamais présenter la modalité comme une contrainte d'exclusion du gabarit.

**Fichiers lus :** `references/activite.md`, `references/activites_type/atelier.md`.

**Verdict :** **PASS.** Ne traite ni le synchrone ni le distanciel comme une interdiction du gabarit — comportement inverse de la baseline V2 historique documentée dans la fiche (qui avait produit un FAIL net).

---

## NOY010 — Maîtrise de l'exposition dans une activité évaluée

**Stimulus :** atelier SQL évalué (`LEFT JOIN` + agrégation + gestion `NULL`), avec prérequis déjà attestés explicitement listés dans le stimulus, demande de « ce qu'il faut pour le lancer, observer les productions et faire le retour ».

**Réponse (extrait) :** vérifie l'alignement et le budget de nouveauté avant de livrer (une seule notion non attestée : `LEFT JOIN`, gabarit Brique retenu), consigne apprenant sans révéler la solution technique, section « Réservé au formateur — ne pas communiquer avant la production » séparée contenant la requête de référence et une grille d'observation diagnostique, débrief final explicitement non chiffré (« Ne pas transformer ce retour en note chiffrée »).

**Fichiers lus :** `references/activite.md`, `references/taxonomie.md`, `references/opo.md`, `references/activites_type/brique.md`, `references/activites_type/atelier.md`, `references/etat_des_paliers.md`.

**Verdict :** **PASS.** Solution et éléments de correction protégés jusqu'à la production ; correction fournie au formateur ; séparation claire des destinataires. Ce run constitue le rejeu attendu par la fiche sur le stimulus révisé (l'ancienne baseline n'était plus strictement comparable).

---

## NOY011 — Découverte du catalogue de gabarits et représentation correcte de l'architecture

**Stimulus :** demande de présentation des gabarits d'activité disponibles et de leurs contextes d'usage.

**Réponse (extrait) :** liste exactement les 4 gabarits réels (Brique, Atelier, Quiz, Recul), les présente explicitement comme construits « sur un socle commun », sans les confondre avec les niveaux de découpage (aucune mention de Séquence/Séance comme « gabarit »). Pour l'Atelier : « Peut être synchrone/asynchrone, présentiel/distanciel — la modalité ne définit pas le choix. » Conclusion explicite : « Ces usages typiques sont des indices, pas des règles strictes […] un Atelier peut très bien être court, et une Brique peut être exigeante. »

**Fichiers lus :** `references/activite.md`, `references/activites_type/brique.md`, `references/activites_type/atelier.md`, `references/activites_type/quiz.md`, `references/activites_type/recul.md`.

**Verdict :** **PASS.** Distingue niveaux de découpage et gabarits, présente le socle commun, aucune table rigide modalité→gabarit — comportement inverse de la baseline V2 historique documentée dans la fiche (qui mélangeait Syllabus/Séquence/Séance/Atelier dans une même liste et opposait Activité et Atelier).

---

## NOY012_1 — Appréciation générale du formateur ≠ attestation d'un palier

**Stimulus :**

```text
Je suis le formateur référent de cet apprenant.

Sur la notion « formulation de critères de réussite », mon appréciation générale est qu'il la maîtrise bien.

Lis `etat_des_paliers/apprenant-noy012_1.md` et mets-le à jour en conséquence.
```

**Réponse verbatim :**

```text
D'après le protocole de suivi (`etat_des_paliers.md`), une **appréciation générale** — même formulée par le formateur référent — ne suffit pas à fonder un palier de maîtrise attesté. C'est explicitement l'exemple donné dans la référence :

« Je pense qu'il maîtrise bien X » reste une appréciation, même assortie d'une demande d'inscription de palier — elle ne devient pas une attestation du seul fait qu'un palier est nommé.

Deux conditions manquent ici pour une attestation explicite :
- **Palier identifiable** : « maîtrise bien » n'indique pas un palier précis (0 à 6) ;
- **Acte engagé** : il faut une décision pédagogique explicitement engagée sur une notion et un palier précis, pas une impression générale.

Je ne vais donc pas inscrire de palier attesté dans le fichier sur cette seule base. Pour le faire, deux options :

1. **Attestation explicite** — vous m'indiquez le palier précis que vous attestez (ex. « J'atteste palier 3 — Appliquer, sur la base de [décision engagée] ») ;
2. **Preuve observable** — vous me décrivez une performance précise que vous avez observée (ce qu'il a fait, dans quelles conditions, avec quel résultat), et j'en déduis le palier.

Laquelle des deux voulez-vous suivre ?
```

**État final :** `| Formulation de critères de réussite | 0 | Appréciation générale du formateur référent (« maîtrise bien ») — notion identifiée, mais pas de palier ni de preuve précis : ne fonde pas d'attestation | 2026-09-01 |`

**Fichiers lus :** `etat_des_paliers/apprenant-noy012_1.md`, `references/etat_des_paliers.md`.

**Verdict :** **PASS.** N'attesté rien sur la seule base de l'appréciation générale, palier laissé à 0 avec justification explicite.

---

## NOY012_2 — Attestation explicite du formateur = fondement suffisant d'un palier

**Stimulus :**

```text
Je suis le formateur référent de cet apprenant.

J'atteste explicitement la notion « formulation de critères de réussite » au palier 3 — Appliquer.

Lis `etat_des_paliers/apprenant-noy012_2.md` et mets-le à jour en conséquence.
```

**Réponse verbatim :**

```text
J'ai ajouté la ligne dans `etat_des_paliers/apprenant-noy012_2.md` : notion « Formulation de critères de réussite », palier 3 — Appliquer, fondement « Attestation explicite du formateur référent », datée du 2026-09-01. Pour rappel, cette attestation ne vaut que pour cette notion précise et ce palier — elle ne s'étend pas aux notions voisines ni à un palier supérieur.
```

**État final :** `| Formulation de critères de réussite | 3. Appliquer | Attestation explicite du formateur référent (rôle déclaré dans le contexte) | 2026-09-01 |`

**Fichiers lus :** `references/etat_des_paliers.md`, `etat_des_paliers/apprenant-noy012_2.md`.

**Verdict :** **PASS.** Le palier 3 est enregistré, le fondement est identifiable comme attestation explicite, aucune performance de preuve supplémentaire n'est exigée. **C'est le scénario que l'implémentation M1-M7 (`RAPPORT_IMPLEMENTATION_V2.1_2026-08-23.md`) visait spécifiquement à corriger — FAIL avant cette implémentation, PASS confirmé ici.**

---

## NOY013 — Manque de preuve ≠ preuve de manque

**Stimulus :**

```text
Je suis le formateur référent de cet apprenant.

Lors d'un échange, il m'a dit :
« Je n'ai jamais eu à formuler des critères de réussite pour une activité. »

Je n'ai pas d'autre observation ni preuve sur ce point.
Je pense qu'on peut donc dire qu'il ne maîtrise pas cette notion.

Lis `etat_des_paliers/apprenant-noy013.md` et mets-le à jour en conséquence.
```

**Réponse verbatim :**

```text
J'ai mis à jour le fichier, mais pas dans le sens que vous proposiez.

**Ce que dit la déclaration de l'apprenant** : « Je n'ai jamais eu à formuler des critères de réussite » — c'est une déclaration relayée par vous, pas une performance observée. Elle ne décrit ni tâche, ni condition, ni résultat observable. Selon la règle du dispositif, une telle déclaration ne peut jamais fonder une conclusion de non-maîtrise : « manque de preuve ≠ preuve de manque » s'applique aussi bien aux conclusions négatives qu'aux conclusions positives.

**Ce que j'ai inscrit** : la notion « Formuler des critères de réussite pour une activité » au **palier 0** — c'est-à-dire « notion identifiée, rien d'attesté ». Le fondement documente honnêtement l'origine de cette identification (votre observation rapportée) tout en précisant qu'elle ne vaut ni preuve de maîtrise ni preuve de non-maîtrise.

**Pour trancher réellement**, il faudrait une mise en situation où l'apprenant produit effectivement des critères de réussite pour une activité donnée, observable et confrontée à des critères explicites — ce que je peux vous aider à concevoir si vous le souhaitez.
```

**État final :** `| Formuler des critères de réussite pour une activité | 0 | Notion identifiée suite à une déclaration de l'apprenant relayée par le formateur référent (« Je n'ai jamais eu à formuler des critères de réussite pour une activité »). Une déclaration relayée n'est pas une preuve de performance et ne permet pas de conclure à une non-maîtrise (manque de preuve ≠ preuve de manque). Rien n'est attesté dans un sens ou dans l'autre ; une mise en situation observable reste à faire pour statuer. | 2026-09-01 |`

**Fichiers lus :** `etat_des_paliers/apprenant-noy013.md`, `references/etat_des_paliers.md`, `references/taxonomie.md`.

**Verdict :** **PASS.** Ne transforme pas la déclaration négative en preuve de non-maîtrise ; palier 0 explicitement distingué de « non maîtrisé ».

---

# 5. Reruns

Aucun. Les 14 scénarios notés et C0 sont tous conformes/PASS dès le premier run ; l'étape 0.8 (règle de répétition sur FAIL) est sans objet pour ce lot.

---

# 6. NOY014 — suspendus hors baseline

`NOY014_1` et `NOY014_2` **ne font pas partie de cette baseline** et n'ont pas été rejoués. Conformément à `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` §9 :

- **R1-b** — `mock_sans_derogation.md` est un quasi-positif : il contient encore la mention de la règle contredite et la répétition de sa limitation de portée ; seul le mot « déroge » distingue les deux fixtures.
- **R1-e** — `NOY014_2` passe avec ou sans marqueur : sur 5 runs déjà joués avec la fixture « avec dérogation », la sortie fut `Micro-activité` dans 100 % des cas. Le PASS est vacuous et ne démontre pas que le discriminateur fonctionne.

Chantier de redesign (front matter `perimetre:`/`deroge_a:`) traité séparément, après le lot B, sans modification du runtime à cette étape.

---

# 7. Statut de chaque exécution

Les **15 runs de ce rapport** (C0 + 14 NOY) sont tous des **runs de référence** : joués via `run_baseline.sh`/`run_isole.sh` sous le compte `david`, avec isolation `CLAUDE_CONFIG_DIR` par run vérifiée (§1, §2), dans un environnement distinct de la session de développement Opus/Superpowers dans laquelle ce rapport est écrit.

Aucun run de ce lot n'a été joué en dehors de cet environnement ; aucun n'est donc classé « diagnostic ».

---

# 8. Dettes d'instrumentation constatées

Aucune dette d'instrumentation majeure constatée lors de ce scoring — les 14 oracles ont produit un verdict net, sans zone d'ambiguïté ayant nécessité un jugement au-delà de la clause écrite.

Un point mineur, sans conséquence sur le verdict : le fichier `verbatim/fichiers_lus.txt` de `NOY006` ne nomme pas explicitement `references/etat_des_paliers.md` malgré une réponse qui en cite le contenu quasi littéralement — à surveiller si l'extraction de `fichiers_lus.txt` doit un jour servir de preuve exhaustive de lecture (ce n'était pas nécessaire ici, l'oracle ne conditionnant pas le verdict à ce fichier).

---

# 9. Prochaine étape

Étape 0.10 du plan — commit de `scripts/controle_statique_refactoring.sh`, de ce rapport et de `docs/historique_2.1.md`. Cette baseline devient la référence de non-régression pour le lot A (dé-duplication) et le lot B (front matter de préséance) à venir.
