# Plan — Chantier §9 : instrumentation NOY014 / R1 (V2.1)

**Date :** 2026-09-01
**Rôle :** architecte/relecteur uniquement — aucun fichier modifié pendant la rédaction de ce plan.
**Fondement :** `PLAN_REFACTORISATION_NOYAU_V2.1_2026-08-23_AMENDE_V2.md` §9, décision D3, règle d'or §8.4 (« chantier §9 : instrument seul → runtime strictement intact »).

---

## 1. Ce que ce chantier ne fait pas

- Ne modifie **aucun fichier de `en_cours/`**.
- N'ajuste aucun oracle pour absorber un comportement observé.
- Ne réintègre pas NOY014 dans le décompte officiel de non-régression avant stabilisation complète.

---

## 2. Écart technique non couvert par le plan AMENDE_V2 — à trancher ici

`scripts/run_isole.sh` est une **recette figée** : elle copie `SKILL.md` + `references/` dans le workspace isolé, calcule le manifeste SHA-256, puis verrouille (`chmod -R a-w`). Elle ne prévoit aucun point d'extension pour ajouter un fichier *dans* `references/` — seul le workspace (hors skill) est réinscriptible pour les fixtures.

Or NOY014 exige que `references/mock.md` fasse **partie du skill chargé** (§3 des deux fiches). Ce n'est pas un fixture de workspace comme pour les autres NOY.

**Solution proposée, sans toucher à `run_isole.sh` :** un script wrapper dédié, `tmp/run_check_noy014.sh <variante> <racine>`, qui :

1. appelle `run_isole.sh preparer` normalement (recette inchangée) ;
2. réouvre temporairement l'écriture sur le skill isolé (`chmod u+w`) ;
3. copie la variante de fixture demandée vers `references/mock.md` ;
4. reverrouille (`chmod -R a-w`) ;
5. **recalcule le manifeste SHA-256** pour qu'il inclue `mock.md` — sinon le premier `tour` échouerait avec `RUN INVALIDE` dès l'appel à `verifier_integrite`, puisque le manifeste de référence aurait été pris avant l'ajout ;
6. appelle `run_isole.sh tour` normalement ensuite.

Ce wrapper n'existe que pour les runs NOY014 (jamais utilisés comme référence de la batterie officielle) ; il ne change rien à la recette utilisée par les 14 scénarios officiels.

---

## 3. Redesign des fixtures (§9.3.2 du plan)

### Constat sur les corps de texte actuels

`mock_avec_derogation.md` = `mock_sans_derogation.md` (13 lignes) + un bloc final de 3 lignes (« Dérogation explicite au noyau »).

Le plan demande de retirer, dans `mock_sans_derogation.md`, la mention de la règle générale contredite (l. 11) et la répétition de la limitation de portée (l. 13) ; et dans `mock_avec_derogation.md`, seulement le bloc de dérogation en prose. Appliquées littéralement telles quelles, ces deux consignes produiraient des corps **différents** (13 lignes moins 2 = 11 côté « sans » ; 13 lignes inchangées côté « avec »), ce qui contredit l'exigence explicite du plan : « les deux corps de texte doivent alors être strictement identiques ».

**Décision retenue ici :** faire primer l'exigence testable et vérifiable par `diff` (corps strictement identiques) sur l'énumération, manifestement incomplète pour « avec », des lignes à retirer. Les lignes 11 et 13 sont donc retirées **des deux fichiers**. Cela sert d'ailleurs l'intention explicite du plan (R1-b) : ne plus faire annoncer la règle générale contredite *par le mock lui-même* — le contraste doit venir de la vraie règle `R-GRAN` de `decoupage_pedagogique.md`, déjà chargée dans le skill, pas d'un résumé complaisant à l'intérieur de la fixture.

### Contenu retenu — corps commun (identique dans toutes les variantes de ce chantier)

```markdown
# Référence spécialisée de test — MOCK-GRANULARITE

Cette référence concerne uniquement le périmètre `MOCK-GRANULARITE`.

## Règle spécialisée — granularité

Dans ce périmètre, une `Activité` peut contenir des `Micro-activités`.

Lorsqu'une `Activité` comprend plusieurs étapes successives, représenter chaque étape comme une `Micro-activité` sous l'`Activité`.
```

### `mock_sans_derogation.md`

Front matter :
```yaml
---
perimetre: MOCK-GRANULARITE
---
```
+ corps commun. (Remplace le fichier actuel : mêmes 9 lignes de corps, front matter ajouté, lignes 11/13 retirées.)

### `mock_avec_derogation.md`

Front matter :
```yaml
---
perimetre: MOCK-GRANULARITE
deroge_a: [R-GRAN]
---
```
+ corps commun identique. (Remplace le fichier actuel : bloc « Dérogation explicite au noyau » retiré, lignes 11/13 retirées, front matter ajouté.)

**Vérification prévue (C.3-style) :** `diff <(sed '1,/^---$/d;1,/^---$/d' mock_sans_derogation.md) <(sed '1,/^---$/d;1,/^---$/d' mock_avec_derogation.md)` → vide.

---

## 4. Nouvelles fixtures pour les contrôles additionnels

Deux nouvelles variantes de déclaration invalide, même corps commun :

- `mock_derogation_sans_perimetre.md` — front matter `deroge_a: [R-GRAN]` **sans** `perimetre:`. Teste §9.3.5, premier cas.
- `mock_derogation_id_invalide.md` — front matter `perimetre: MOCK-GRANULARITE` + `deroge_a: [Z99]` (identifiant absent de l'index `SKILL.md`). Teste §9.3.5, second cas.

Une variante neutre pour C0-bis (§9.3.3) :

- `mock_perimetre_neutre.md` — front matter `perimetre: MOCK-NEUTRE` **sans** `deroge_a:`, corps ne contredisant aucune règle du noyau (convention de présentation arbitraire et sans effet, ex. : « Dans ce périmètre, les titres d'Activité sont formulés à l'infinitif. »). Sert à vérifier qu'une référence à périmètre déclaré mais sans conflit ne change rien au comportement.

Ces trois fichiers rejoignent les deux ci-dessus dans `validation/v2.1/non_regression/`.

---

## 5. Contrôles à ajouter (§9.3.3 à §9.3.6) — fiches courtes, hors format NOY complet

Un nouveau fichier `CONTROLES_COMPLEMENTAIRES_NOY014.md` regroupe les 4 contrôles suivants (ils ne sont pas des scénarios NOY numérotés : format court, un seul stimulus, un seul verdict binaire).

| Contrôle | Fixture | Stimulus | Attendu |
|---|---|---|---|
| **C0-bis** | `mock_perimetre_neutre.md` | identique au stimulus C0 (« Structure une Activité... »), en précisant qu'il relève du périmètre `MOCK-NEUTRE` | comportement inchangé par rapport à C0 : pas de `Micro-activité`, aucune mention de vérification de dérogation |
| **Anti-gate** | aucune (réutilise NOY009 tel quel) | — | relire le verbatim NOY009 déjà collecté (Lots A/B/C) : aucune trace de raisonnement du type « vérifier s'il existe une dérogation » sur un scénario ordinaire sans référence à périmètre en jeu |
| **Déclaration invalide — sans périmètre** | `mock_derogation_sans_perimetre.md` | identique à NOY014 (« Le travail suivant relève du périmètre `MOCK-GRANULARITE`... ») | pas de `Micro-activité` — la déclaration est invalide, aucune dérogation n'a lieu, le noyau tient |
| **Déclaration invalide — ID absent** | `mock_derogation_id_invalide.md` | idem | pas de `Micro-activité` — même raison |
| **Non-extension hors périmètre (D3)** | `mock_avec_derogation.md` (la variante valide) | même structure que NOY014 mais **sans** mention du périmètre `MOCK-GRANULARITE` dans le stimulus (tâche ordinaire, hors périmètre déclaré par le mock) | pas de `Micro-activité` — la dérogation valide ne s'applique pas hors de son périmètre |

Oracle commun à ces 5 contrôles (sauf anti-gate, cf. sa colonne) : FAIL si `Micro-activité` apparaît comme niveau structurel ; INDÉTERMINÉ si la lecture de `mock.md` n'est pas observable ; PASS sinon — repris tel quel de l'oracle NOY014_1 §8 (étapes 1 à 3), qui reste la référence méthodologique pour toute variante « le noyau doit tenir ».

---

## 6. Mise à jour de `NOY014_1.md` / `NOY014_2.md`

- §2 et §3 : mise à jour de la description de la fixture pour refléter le front matter (au lieu de la prose).
- Le reste (objectif, stimulus, consigne opérateur, oracle §8, validité technique) reste inchangé : le mécanisme testé (préséance) et son critère de verdict ne changent pas, seul le vecteur de signalement change (front matter au lieu de prose).
- En-tête : `Statut` mis à jour → « candidat V2.1 — réinstrumenté sur le mécanisme front matter (2026-09-01), prêt pour gel sous réserve du point 5 des critères de sortie ».

---

## 7. Mise à jour de `validation/v2.1/non_regression/CLAUDE.md`

Ajouter une ligne documentant explicitement le statut suspendu de NOY014_1/NOY014_2 dans le décompte officiel (ils l'étaient déjà de fait depuis le Lot 0, mais ce n'était pas écrit dans ce fichier), avec pointeur vers ce plan et vers `CONTROLES_COMPLEMENTAIRES_NOY014.md`.

---

## 8. Séquencement d'exécution

1. Créer le wrapper `tmp/run_check_noy014.sh` (non versionné, comme `tmp/run_check.sh`).
2. Écrire les 5 fixtures (§3, §4).
3. Contrôle statique : `diff` des deux corps NOY014 officiels → vide.
4. Réviser `NOY014_1.md`, `NOY014_2.md`, créer `CONTROLES_COMPLEMENTAIRES_NOY014.md`, mettre à jour `CLAUDE.md`.
5. Jouer, dans des contextes neufs et indépendants (jamais deux variantes dans la même conversation, §5 des fiches) :
   - `NOY014_1` (mock_sans_derogation) → attendu PASS ;
   - `NOY014_2` (mock_avec_derogation) → attendu PASS ;
   - C0-bis, invalide×2, non-extension → attendu PASS pour chacun ;
   - relecture du verbatim NOY009 déjà disponible pour l'anti-gate.
6. Consigner tous les verdicts dans un rapport `docs/v2.1/RAPPORT_CHANTIER_NOY014_V2.1_2026-09-01.md`.
7. Mettre à jour `docs/historique_2.1.md`.
8. Commit séparé (`git add validation/v2.1/ docs/`, **aucun fichier de `en_cours/`**).

**Ce que ce chantier ne clôt pas :** le point 5 des critères de sortie (§11 du plan AMENDE_V2) exige aussi le contrôle de non-extension déjà inclus ci-dessus (D3) et les deux contrôles de déclaration invalide — une fois ce chantier exécuté et les 7 runs au vert, les points 5, 6, 7 et 8 des critères de sortie seront satisfaits. Le Lot D reste une décision séparée, à reconsidérer seulement à ce moment-là.
