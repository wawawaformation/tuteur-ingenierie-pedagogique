# Rapport — Chantier §9 : instrumentation NOY014 / R1 (V2.1)

**Date :** 2026-09-01
**Plan appliqué :** `PLAN_CHANTIER_NOY014_V2.1_2026-09-01.md`
**Rôle :** implémenteur/exécutant. **Aucun fichier de `en_cours/` modifié** — chantier d'instrument seul, conformément à la règle d'or de séquencement (§8.4 du plan AMENDE_V2).

---

## 1. Ce qui a été fait

- Réinstrumentation de `mock_sans_derogation.md` / `mock_avec_derogation.md` sur le mécanisme front matter (`perimetre:`/`deroge_a:`), corps de texte rendus strictement identiques (vérifié par `diff`).
- 3 nouvelles fixtures : `mock_derogation_sans_perimetre.md`, `mock_derogation_id_invalide.md`, `mock_perimetre_neutre.md`.
- Wrapper technique `tmp/run_check_noy014.sh` : injecte `references/mock.md` dans le skill isolé (impossible avec `run_isole.sh` seul, qui ne permet d'écrire que dans le workspace) et recalcule le manifeste SHA-256 après injection, sans modifier le script figé.
- Mise à jour de `NOY014_1.md` / `NOY014_2.md` (description de fixture) et nouveau `CONTROLES_COMPLEMENTAIRES_NOY014.md` (5 contrôles courts).
- 6 runs joués (NOY014_1 par moi-même en pilote, les 5 autres par un sous-agent Sonnet dédié), plus relecture du verbatim NOY009 existant pour l'anti-gate.

---

## 2. Résultats

| Contrôle | Verdict | Tours | Fondement |
|---|---|---|---|
| **NOY014_1** (sans dérogation) | **PASS** | 2 (relance envoyée) | signalement de la contradiction au tour 1, puis décision autonome au tour 2 : R-GRAN tient, aucun `Micro-activité` |
| **NOY014_2** (avec dérogation valide) | **PASS** | 1 | dérogation appliquée explicitement, `Micro-activité` utilisé comme prévu |
| **C0-bis** (périmètre neutre, sans conflit) | **conforme** | 1 | comportement inchangé par rapport à C0, aucun surcoût observable |
| **Anti-gate** (relecture NOY009) | **conforme** | — | aucune trace de vérification de dérogation sur un scénario sans référence à périmètre |
| **Déclaration invalide — sans `perimetre:`** | **PASS** | 1 | déclaration invalide reconnue, aucune dérogation, noyau tient |
| **Déclaration invalide — ID absent** | **PASS** | 2 (relance envoyée) | idem, tranché après relance |
| **Non-extension hors périmètre (D3)** | **FAIL** | 1 | la dérogation valide de `mock.md` s'est appliquée à une tâche ne mentionnant pas son périmètre |

**5 PASS/conforme sur 6, 1 FAIL.**

Aucun incident technique : tous les runs `rc=0` au premier essai. Le mécanisme d'injection (wrapper + recalcul de manifeste) fonctionne conformément à la conception.

---

## 3. Le FAIL : non-extension hors périmètre (I30)

### Ce qui a été observé

Stimulus (`tmp/noy014_stimuli/hors_perimetre.txt`) :

```text
La référence `references/mock.md` fait partie du skill chargé.

Structure une Activité composée de deux étapes successives :
1. lire une consigne ;
2. produire une réponse.

Donne uniquement la structure hiérarchique.
```

Ce stimulus ne mentionne à aucun moment le périmètre `MOCK-GRANULARITE`. Réponse obtenue :

```text
Activité
├── Micro-activité — Lire une consigne
└── Micro-activité — Produire une réponse

Cette structure applique la règle spécialisée de `references/mock.md` (périmètre `MOCK-GRANULARITE`,
dérogation à `R-GRAN`)...
```

L'agent a appliqué la dérogation valide de `mock.md` à une tâche dont rien n'indiquait qu'elle relevait du périmètre `MOCK-GRANULARITE`, allant jusqu'à nommer explicitement ce périmètre dans sa justification alors que le stimulus ne le mentionnait pas.

### Ce que ça démontre

Le mécanisme déclaratif (`deroge_a:`/`perimetre:`) fonctionne pour les branches déjà testées (dérogation absente → noyau ; dérogation valide et périmètre concerné → règle spécialisée ; déclaration invalide → noyau). Il ne démontre **pas** encore que la dérogation reste bornée à son périmètre lorsque la tâche elle-même ne précise pas son périmètre : l'agent semble avoir traité « la référence fait partie du skill chargé » comme suffisant pour l'appliquer, sans vérifier que la tâche en cours relève effectivement de `MOCK-GRANULARITE`.

### Ce que ce n'est probablement pas

Un artefact de conception du test a été considéré et écarté : la contrainte méthodologique héritée de NOY014_1/NOY014_2 (« désigner la référence dans le stimulus pour ne pas tester sa découverte », §4 des fiches) impose de mentionner `mock.md` dans le stimulus. Un stimulus qui ne le mentionnerait pas du tout ne testerait rien (l'agent n'aurait aucune raison de consulter `mock.md`). Le stimulus utilisé est donc conforme à cette contrainte ; il ne semble pas artificiellement piégeur.

### Ce que ce chantier ne fait pas avec ce résultat

Conformément à §9.4 du plan AMENDE_V2 : **aucun ajustement de l'oracle pour absorber ce comportement, aucune modification du runtime pour faire passer le test**. Le FAIL est consigné tel quel.

---

## 4. Conséquence sur les critères de sortie (§11 du plan AMENDE_V2)

Le point 5 des critères de sortie exige que **toutes** les branches du mécanisme soient PASS, y compris le test de non-extension (point 7, décision D3). Ce n'est pas le cas : **le mécanisme de préséance reste non démontré dans son ensemble**.

Concrètement :

- Le Lot D (split de `taxonomie.md`) reste à juste titre en attente : la décision D2 le conditionnait déjà à ce point 5.
- La V3 tutorat, dont `tutorat.md` dépendra précisément de ce mécanisme (§11, dernière ligne du plan AMENDE_V2), ne peut pas s'appuyer sur la non-extension hors périmètre tant que ce point n'est pas corrigé et re-vérifié.
- Le noyau V2.1 reste correct et non régressé sur tout ce qui a été testé jusqu'ici (Lots 0, A, B, C) : ce FAIL ne remet en cause aucun des 14 PASS officiels ni C0.

**Ce rapport ne propose pas de correction.** Une correction toucherait `SKILL.md` (formulation de la section « Périmètre et préséance »), donc le runtime — hors du périmètre de ce chantier d'instrument seul, et une décision de conception à part entière (comment faire respecter la borne de périmètre sans réintroduire un verbe de gate proscrit par R5).

---

## 5. Statut de NOY014 dans le décompte

`NOY014_1` et `NOY014_2` restent **suspendus** du décompte officiel de non-régression (14/14 sur les 14 scénarios NOY001-013 n'inclut toujours pas NOY014). Leur réintégration reste conditionnée à la résolution du point 5 des critères de sortie, désormais explicitement bloqué par le résultat de la section 3.

---

## 6. Artefacts

- Fixtures : `validation/v2.1/non_regression/mock_*.md` (5 fichiers).
- Fiches : `NOY014_1.md`, `NOY014_2.md` (mises à jour), `CONTROLES_COMPLEMENTAIRES_NOY014.md` (nouveau).
- Outillage : `tmp/run_check_noy014.sh`, `tmp/noy014_stimuli/` (non versionnés).
- Verbatims complets : `/projets/skill/tests/chantierNOY014_2026-09-01/<CONTROLE>/verbatim/`.
