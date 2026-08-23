# Historique — candidat V2.1

Journal court des étapes réalisées sur le candidat V2.1. Mis à jour avant chaque commit touchant à ce candidat. Ordre chronologique inverse (le plus récent en premier).

---

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
