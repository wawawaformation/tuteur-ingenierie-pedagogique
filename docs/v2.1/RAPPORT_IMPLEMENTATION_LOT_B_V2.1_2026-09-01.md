# Rapport d'implémentation — LOT B « Périmètre et préséance » (V2.1)

**Date :** 2026-09-01
**Plan appliqué :** `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md`, §LOT B (étapes B.1 à B.6)
**Rôle :** implémenteur strict. Aucune doctrine créée ni arbitrée ; aucun oracle, fixture ou kit modifié.
**Référence de non-régression :** `RAPPORT_BASELINE_COMPORTEMENTALE_V2.1_2026-09-01.md` (14/14 PASS + C0 conforme).

---

## 1. Nature du changement

Ce lot change **la doctrine d'implémentation** de la préséance, pas la doctrine G02 elle-même.

Avant, la préséance reposait sur une règle en prose : une référence « spécialisée » dont le périmètre « s'applique » et qui « signale explicitement déroger » prévalait. Trois notions devaient être inférées à l'exécution : la spécialisation du fichier, l'applicabilité de son périmètre, et le caractère explicite du signalement.

Après, la dérogation est **déclarée** : un fichier ne déroge que s'il porte `deroge_a:` dans son front matter, borné par `perimetre:`, et citant un identifiant présent dans un index fermé. En l'absence de déclaration, la règle contredite tient — quel que soit le degré de spécialisation du fichier.

La clause de signalement des contradictions non résolues est conservée **mot pour mot**.

---

## 2. Étapes exécutées

| Étape | Fichier | Changement |
|---|---|---|
| B.1 | `en_cours/SKILL.md` (l. 99) | « la référence normative spécialisée fait foi » remplacé par une formulation bornée au seul axe glossaire/norme, avec renvoi explicite à la section « Périmètre et préséance ». Supprime « fait foi » et « spécialisée », qui portaient une transposition implicite de *lex specialis* (P5). |
| B.2 | `en_cours/SKILL.md` | Le bloc « Préséance entre règles » quitte la section « Contrôles avant réponse ou livraison » (P12) et devient une section propre `## Périmètre et préséance` en fin de fichier, portant le mécanisme `deroge_a:` / `perimetre:`, la règle de déclaration invalide, et l'index des règles dérogeables (`A3`, `R-GRAN`). |
| B.3 | `en_cours/references/decoupage_pedagogique.md` (§1, sous-section `Activité`) | Suffixe `*(règle R-GRAN)*` ajouté. La proposition de la règle est strictement inchangée. |
| B.4 | `en_cours/references/activite.md` (« Rôle du front matter ») | Puce ajoutée : « une éventuelle dérogation déclarée et son périmètre ». Mentionne l'existence du champ sans redire la règle de préséance. |

**Neutralité sur l'existant :** aucune référence du runtime ne porte `deroge_a:` après ce lot. Le mécanisme est posé mais n'est activé nulle part ; aucune référence en place n'est reclassifiée.

---

## 3. Contrôles statiques

Contrôles obligatoires de B.2, B.3, B.4 :

| Contrôle | Attendu | Mesuré |
|---|---|---|
| `"ne pas arbitrer silencieusement ; la signaler"` dans `SKILL.md` | 1 | **1** ✓ |
| `"règle générale du skill"` dans `SKILL.md` | 0 | **0** ✓ |
| `"avant toute décision\|vérifier s'il existe\|rechercher"` dans `SKILL.md` | vide | **vide** ✓ |
| `"deroge_a"` dans `SKILL.md` | ≥ 1 | **4** ✓ |
| `"deroge_a"` dans `references/` | vide | **vide** ✓ |
| `"R-GRAN"` dans `SKILL.md` | 1 | **1** ✓ |
| `"granularité la plus fine"` dans `decoupage_pedagogique.md` | inchangé (1) | **1** ✓ |
| `"prévaut\|préséance"` dans `activite.md` | 0 | **0** ✓ |

Contrôle statique global (B.5, `./scripts/controle_statique_refactoring.sh`) :

- **CS6** (aucun « fait foi » sur l'axe de préséance) : **0 occurrence** ✓
- **CS9** (aucun gate de dérogation) : **OK** ✓
- CS7 (ancrages `taxonomie.md §2`) et CS8 (invariants gelés) inchangés par rapport à l'état de sortie du lot A, à l'exception de `SKILL.md` qui passe de 2 à 3 ancrages `taxonomie.md §2` — le troisième est la ligne d'index de la règle `A3` introduite en B.2, conforme à l'attendu du plan.

---

## 4. Non-régression comportementale (B.6)

15 runs joués en contextes neufs et aveugles (`tmp/run_check.sh` sur les kits de `validation/v2.1/baseline/kits/`), séquentiellement, contre l'état WIP du candidat. Scoring appliqué contre les oracles de `validation/v2.1/non_regression/`.

**Résultat : 14/14 PASS, 0 FAIL, 0 INDÉTERMINÉ, C0 conforme.**

| Scénario | Verdict | Fondement |
|---|---|---|
| C0 | conforme | aucune granularité `Micro-activité` introduite sous `Activité` |
| NOY001 | PASS | refus d'attester sur la seule déclaration ; attestation après description suffisante |
| NOY002 | PASS | palier 2 inscrit sur preuve Quiz, palier 3 refusé |
| NOY003 | PASS | refus du bloc à 3 nouveautés, découpage en 3 Briques |
| NOY004 | PASS | signalement du critère purement structurel + critère d'alignement ajouté |
| NOY005 | PASS | traitement notion par notion, aucune attestation globale |
| NOY006 | PASS | inscription refusée, notion conservée non attestée |
| NOY007 | PASS | critères en toutes lettres, aucun barème inventé |
| NOY008 | PASS | socle d'Activité adapté au format Quiz |
| NOY009 | PASS | contraintes de modalité non transformées en interdiction |
| NOY010 | PASS | solution et éléments décisifs protégés côté apprenant |
| NOY011 | PASS | gabarits présentés comme formes d'Activité, sans exclusivité artificielle |
| NOY012_1 | PASS | notion ajoutée au palier 0, appréciation non convertie en preuve |
| NOY012_2 | PASS | palier 3 fondé sur l'attestation explicite du formateur, sans preuve supplémentaire |
| NOY013 | PASS | palier 0 explicitement distingué de « ne maîtrise pas » |

Aucun incident technique : tous les runs sortis avec `rc=0` au premier essai, aucune invalidation d'intégrité du candidat, aucun rerun nécessaire. Cinq scénarios (NOY003, NOY005, NOY006, NOY009, NOY012_1) ont donné lieu à une relance neutre de la couche opérateur aveugle, conformément au protocole.

Artefacts : `/projets/skill/tests/lotB_checks_2026-09-01/<SCENARIO>/verbatim/`.

**NOY014_1 / NOY014_2 non joués**, conformément à la consigne explicite de B.6 : leurs fixtures signalent la dérogation en prose et non en front matter, donc elles ne testent plus le mécanisme cible depuis B.2. Elles sont hors critère de succès de ce lot et devront être réinstrumentées (§9 du plan) dans un **cycle séparé** — jamais dans le même cycle que ce lot.

---

## 5. Écarts et réserves

**Écart de procédure (B.3).** Le plan demandait de rejouer C0 *immédiatement après B.3 seule*, cette étape touchant la ligne porteuse du contraste I25. B.4 a été appliquée avant le lancement des runs. B.4 ne modifie ni `decoupage_pedagogique.md` ni aucune ligne lue par C0 : elle ajoute une puce descriptive dans `activite.md`. Le C0 joué reste donc interprétable comme contrôle de B.3, mais il couvre en réalité l'état B.1-B.4. Écart consigné, sans effet constaté : C0 conforme.

**Réserve sur la portée de la vérification.** Les 14 scénarios de non-régression testent que le mécanisme déclaratif n'a **rien cassé**. Ils ne testent pas qu'il **fonctionne** : aucune référence ne portant `deroge_a:`, aucun run n'exerce le chemin « dérogation déclarée valide ». Cette vérification-là dépend de la réinstrumentation de NOY014 (§9 du plan) et reste à faire.

**Point non couvert par le plan, signalé sans décision.** L'index des règles dérogeables est fermé à deux entrées (`A3`, `R-GRAN`). Le plan ne dit pas quelle procédure suivre pour y ajouter une règle ultérieurement. Aucune décision prise ici.

---

## 6. Contrôle de sortie du lot B

> « Aucun comportement conforme de NOY001-NOY013 dans la baseline ne régresse et C0 reste conforme. »

**Satisfait.** Les 14 comportements conformes de la baseline le restent, C0 reste conforme, aucun scénario n'a régressé ni n'a eu besoin d'être amélioré.
