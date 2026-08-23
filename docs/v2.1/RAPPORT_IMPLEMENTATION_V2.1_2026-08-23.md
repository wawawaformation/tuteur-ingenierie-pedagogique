# Rapport d'implémentation — noyau V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** V2.1.0
**Date :** 2026-08-23
**Plan exécuté :** `docs/v2.1/PLAN_IMPLEMENTATION_V2.1_2026-08-23_REVISE_3.md`
**Statut :** implémentation M1–M7 terminée, **non testée**. Aucun dry-run lancé, aucun commit effectué.

Ce rapport documente ce qui a été fait, pas ce qui reste à décider — les arbitrages doctrinaux (A1, A2, A3) ont été tranchés en amont dans le plan révision 3 et n'ont pas été rouverts pendant l'implémentation.

---

# 1. Fichiers modifiés

`en_cours/references/etat_des_paliers.md`, `en_cours/references/taxonomie.md`, `en_cours/references/glossaire.md`, `en_cours/SKILL.md`.

Aucun NOY, aucune fixture, aucun oracle, aucun autre fichier du noyau n'a été touché.

---

# 2. Détail par fichier

## `en_cours/references/etat_des_paliers.md` (M1, M2, M3, M7)

| Emplacement           | Règle précédente                                                                                                                  | Modification effectuée                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Raison                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
| Format (en-têtes)     | `\| Notion \| Palier attesté \| Preuve \| Quand \|` (×2)                                                                          | Renommé en `Fondement` (×2) ; ajout d'une ligne d'exemple d'attestation ; ajout d'un paragraphe de compatibilité descendante avec les fichiers existants nommés `Preuve`                                                                                                                                                                                                                                                                                                                                                           | M3 — conséquence fonctionnelle nécessaire à la distinction preuve/attestation (arbitrage A3) |
| Règles de tenue       | « […] peuvent exprimer une hypothèse **ou une décision du formateur**, mais ne suffisent pas à inscrire un palier comme attesté » | Retrait de l'incise « ou une décision du formateur »                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | M1 — cette incise était le blocage direct et nominatif de NOY012_2                           |
| Règles de tenue       | — (absente)                                                                                                                       | Ajout de la règle « le fondement doit nommer sa nature »                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | M3 point 3                                                                                   |
| Règles de tenue       | « Le palier peut redescendre. […] »                                                                                               | Ajout : « Cette révisabilité s'applique identiquement à un palier fondé sur une attestation explicite du formateur. »                                                                                                                                                                                                                                                                                                                                                                                                              | M2 — révisabilité                                                                            |
| Nouvelle section      | — (absente)                                                                                                                       | **« Fondements d'un palier attesté »** : liste fermée des deux fondements admissibles pour un palier de maîtrise (1-6) ; cas du palier 0 ; quatre conditions cumulatives de l'attestation (rôle, acte, notion, palier) ; précisions de rôle (rôle déclaré, non authentifié, apprenant ne peut pas s'auto-attester, interdiction d'inférer le rôle) ; discriminateur sémantique en tableau (« ce que l'interlocuteur invoque ») ; règle de non-cumul et de non-conversion ; borne de polarité ; liste de contre-exemples explicites | M1 + M7 — seule source normative des quatre conditions (respecte CS2)                        |
| Nouvelle sous-section | — (absente)                                                                                                                       | **« Portée d'une attestation explicite »** : non-propagation aux notions voisines, autres prérequis, notions mobilisées, palier supérieur                                                                                                                                                                                                                                                                                                                                                                                          | M2 — portée                                                                                  |
| Persistance           | `(Notion \| Palier attesté \| Preuve \| Quand)`                                                                                   | Renommé en `Fondement`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | M3                                                                                           |

## `en_cours/references/taxonomie.md` (M4)

| Emplacement                   | Règle précédente                                                                                                | Modification effectuée                                                                                                     | Raison                                                                           |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| A3                            | « *Ce qui compte comme « attesté »* : une preuve observable compatible avec le palier visé est disponible […] » | Reformulé pour pointer vers `etat_des_paliers.md` et reconnaître les deux fondements, sans dupliquer les quatre conditions | M4 — l'ancienne définition était exclusive et aurait contredit M1                |
| A3 (ligne suivante)           | Exposition / démonstration / déclaration / « considère que c'est acquis » ≠ preuve                              | **Strictement inchangée**                                                                                                  | Verrou explicite de la révision 3 : cette ligne protège NOY001, NOY002 et NOY006 |
| A3 (preuve externe rapportée) | Inchangée                                                                                                       | **Strictement inchangée**                                                                                                  | Idem                                                                             |

## `en_cours/references/glossaire.md` (M5)

| Entrée      | Règle précédente                                                           | Modification effectuée                                                                                                                                                                                                                                             | Raison                                                              |
| ----------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------- |
| Attestation | « Décision de considérer **une preuve** comme suffisamment recevable […] » | Remplacée par une définition non circulaire : « Acte explicite par lequel un formateur ou responsable pédagogique déclaré dans le contexte engage sa décision pédagogique pour attribuer ou confirmer une notion à un palier identifiable. », avec renvoi normatif | M5 — l'ancienne définition rendait l'attestation autonome indicible |
| Fondement   | — (absente)                                                                | Nouvelle entrée : distingue palier de maîtrise (1-6, deux fondements admis) et palier 0                                                                                                                                                                            | M5                                                                  |
| Déclaration | « […] n'est pas, à elle seule, une preuve attestée. »                      | Ajout d'une phrase la distinguant de l'attestation explicite                                                                                                                                                                                                       | M5                                                                  |
| Preuve      | Inchangée                                                                  | **Non modifiée**                                                                                                                                                                                                                                                   | M5 point 4                                                          |

## `en_cours/SKILL.md` (M6)

| Emplacement                     | Règle précédente                                                                               | Modification effectuée                                                                                                                                                 | Raison                                              |
| ------------------------------- | ---------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| Garde-fous prioritaires         | Renvoi preuve externe rapportée (l. 30)                                                        | Ajout d'une ligne : « Un palier peut également reposer sur une attestation explicite d'un formateur ; les conditions figurent dans `references/etat_des_paliers.md`. » | M6 — routage minimal, sans dupliquer les conditions |
| Garde-fous prioritaires (l. 28) | « Une exposition, une démonstration ou une déclaration ne valent pas automatiquement preuve. » | **Non modifiée**                                                                                                                                                       | M6 — reste vraie, ne devait pas être touchée        |

---

# 3. Contrôles statiques CS1–CS6

| #       | Contrôle                   | Résultat | Constat                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------- | -------------------------- | -------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **CS1** | Cohérence inter-références | ✅ PASS   | `taxonomie.md` l. 116 et le bloc M1 pointent vers la même source et ne se contredisent pas ; `glossaire.md` « Attestation » est cohérente avec les conditions de `etat_des_paliers.md`.                                                                                                                                                                                                                                                                          |
| **CS2** | Non-duplication            | ✅ PASS   | Les quatre conditions ne sont énumérées qu'une fois, dans `etat_des_paliers.md`. `taxonomie.md` et `SKILL.md` pointent sans réénoncer. La définition non circulaire de `glossaire.md` (imposée telle quelle par la mission) évoque nécessairement rôle/acte/notion/palier en une phrase descriptive — ce n'est pas une ré-énumération procédurale.                                                                                                               |
| **CS3** | Doctrines préservées       | ✅ PASS   | Les huit doctrines listées (exposition ≠ preuve, déclaration ≠ preuve, auto-déclaration positive ≠ performance, manque de preuve ≠ preuve de manque, palier 0 ≠ non maîtrisé, portée limitée à l'acte observé, palier par notion, révisabilité à la baisse) restent présentes et non affaiblies. `taxonomie.md` l. 118 vérifiée identique caractère pour caractère à l'original.                                                                                 |
| **CS4** | Test NOY006 sur table      | ✅ PASS   | Stimulus : locuteur non identifié comme formateur, relaie une déclaration de l'apprenant, ordonne l'inscription d'un palier nommé. Condition 1 (rôle) échoue — aucun positionnement explicite comme formateur, et la règle interdit de l'inférer. Condition 2 (acte) échoue également — le fondement invoqué est une déclaration relayée, cas explicitement listé dans « Ce qui ne constitue pas une attestation ». Résultat sans ambiguïté : pas d'attestation. |
| **CS5** | Test NOY005 sur table      | ✅ PASS   | L'interlocuteur invoque une performance qu'il a observée → voie preuve, via la règle de non-cumul et de non-conversion. L'instruction jointe (« considère comme maîtrisées ces trois notions ») ne convertit pas cette preuve en attestation et n'étend pas sa portée. Seule l'injection de dépendances reste attestable ; l'exception et les tests fournis restent non attestés (protégé par la section « Portée d'une preuve », inchangée).                    |
| **CS6** | Non-lexicalité             | ✅ PASS   | Reformulation du stimulus de NOY012_2 sans le mot « atteste » (« je valide formellement cette notion au palier 3, c'est ma décision ») : les quatre conditions (rôle déclaré, décision propre engagée, notion identifiable, palier identifiable) restent réunies → attestation reconnue malgré l'absence du mot déclencheur.                                                                                                                                     |

Les six contrôles sont des simulations manuelles par relecture, pas des runs réels : ils vérifient la cohérence de la rédaction, pas le comportement effectif du modèle.

---

# 4. Écarts par rapport au plan

- **M2** — le plan proposait deux options pour la portée d'un fondement : renommer le titre de la section existante en « Portée d'un fondement », ou ajouter une sous-section. L'option « sous-section » a été retenue, pour ne pas toucher l'intitulé d'une section déjà référencée ailleurs.
- **M6** — l'ajustement cosmétique facultatif du libellé de `SKILL.md` l. 89 (liste des sources de vérité) n'a pas été fait ; le plan le qualifiait explicitement de facultatif et la ligne actuelle (« preuves, attestation, suivi et persistance ») reste exacte.

Aucun autre écart. Aucune règle hors périmètre n'a été modifiée (quiz, plafond diagnostique, comptage A3 lui-même, alignement, gabarits, tutorat V3).

---

# 5. Ambiguïté rencontrée

Le stimulus de NOY006 ne nomme pas explicitement qui parle (« L'apprenant a dit… », sans identifier le locuteur). Ce silence a été traité conformément à la règle écrite dans M1 : en l'absence de positionnement explicite comme formateur, la condition de rôle échoue par défaut — ce n'est pas une inférence de rôle, mais l'application de l'interdiction d'inférer. C'est une application de la rédaction, pas un nouvel arbitrage doctrinal.

---

# 6. Risques de régression à surveiller au smoke test

- **NOY006** (priorité maximale) — la protection repose sur la conjonction de deux conditions indépendantes (rôle non déclaré + fondement relayé) plutôt que sur une seule barrière. Un stimulus où un rôle de formateur serait implicitement suggéré mériterait un contrôle supplémentaire.
- **NOY005** — la protection dépend entièrement de la règle de non-cumul et de non-conversion, relativement abstraite ; son application effective par le modèle (au-delà de la lecture sur table) reste à vérifier.
- **NOY001 / NOY002** — l'affordance plus permissive de `Fondement` (par rapport à `Preuve`) est mitigée sur table par la condition de rôle (locuteur = apprenant dans les deux scénarios), à confirmer en run.
- **NOY003** — dépend de la même condition de rôle (aucun persona formateur injecté) ; le risque résiduel signalé par le plan (lecture trop large de la condition 1) n'est pas totalement écartable par relecture seule.

---

# 7. État Git au moment du rapport

```
 M docs/historique_2.1.md
 M en_cours/SKILL.md
 M en_cours/references/etat_des_paliers.md
 M en_cours/references/glossaire.md
 M en_cours/references/taxonomie.md
```

```
 docs/historique_2.1.md                  | 11 +++++
 en_cours/SKILL.md                       |  2 +
 en_cours/references/etat_des_paliers.md | 73 ++++++++++++++++++++++++++++++---
 en_cours/references/glossaire.md        | 14 ++++++-
 en_cours/references/taxonomie.md        |  2 +-
 5 files changed, 93 insertions(+), 9 deletions(-)
```

Aucun commit n'a été créé. La suite prévue par le plan (§9 smoke tests NOY012_2 / NOY012_1 / NOY006, §10 contre-tests C1-C5, §11 non-régression complète sur 14 NOY) est en attente de revue du diff et d'autorisation explicite de lancer des dry-runs.
