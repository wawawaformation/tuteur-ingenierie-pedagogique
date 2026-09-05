# CLAUDE.md — `en_cours/`

Ce dossier est la **zone de développement du candidat courant**.

## État actuel

- `VERSION` indique actuellement **V3.1**.
- La V3 est séquencée en mineures indépendantes, gelées et promues l'une après l'autre : V3.1.0 (chantier 1) → V3.2.0 (chantier 2) → V3.3.0 (chantier 3, = V3 complète). Voir `base_de_travail.md` §4.1.
- `promesse.md` porte la spécification fonctionnelle candidate de la mineure **V3.1.0** : elle hérite du socle V2.1 (S01–S03, garanties conservées) et engage le seul chantier 1 (ACT01–02, catalogue d'activités). Les chantiers 2 (COG01–02) et 3 (TUT01–04) ne sont pas encore engagés ; ils seront ajoutés au document lors des mineures V3.2.0 et V3.3.0. **Gelée le 2026-09-03** après validation complète (7 scénarios, 15 exécutions, 15/15 PASS sur une copie de test — voir `promesse.md` « Statut de cette promesse »).
- **Catalogue enrichi implémenté sur ce candidat le 2026-09-04** (14 gabarits, puis 17 le même jour avec l'ajout de trois gabarits d'ouverture). La batterie V3.1 a été rejouée sur le candidat corrigé à 14 gabarits : 15/15 PASS, résultats identiques type par type à la copie de test. Détail et diagnostic du défaut corrigé au passage : `../docs/v3.1/RAPPORT_INSTABILITE_V31-ACT02-3_2026-09-03.md`. L'extension à 17 n'a été revalidée que par contrôle mécanique (`scripts/controle_conformite_gabarits.sh`, 17/17) — voir `promesse.md`, « Statut de cette promesse », pour le raisonnement.
- **Non-régression close** : la non-régression de la baseline V2.1 (`../validation/v2.1/non_regression/`) a été rejouée sur ce candidat le 2026-09-05 : 14/14 PASS (voir `../docs/v3.1/RAPPORT_NON_REGRESSION_V2.1_SUR_CANDIDAT_V3.1_2026-09-05.md`). Avec les 15/15 PASS de la batterie propre à la mineure, V3.1.0 est validée au sens de `base_de_travail.md` §13.
- `base_de_travail.md` est la feuille de route actuelle de la trajectoire V2.1 → V3 ; elle fait foi pour le séquencement du travail.
- **V3.1.0 promue** vers `../dist/stable/tuteur-ingenierie-pedagogique_v3.1/` : c'est désormais la version publique recommandée. `en_cours/` contient toujours ce même runtime (VERSION `V3.1`) dans l'attente de l'ouverture de la mineure V3.2.0 (chantier 2).

## Règles de modification

Avant de modifier `SKILL.md` ou une référence :

1. lire `promesse.md` ;
2. lire les références directement concernées ;
3. identifier les scénarios de non-régression potentiellement affectés ;
4. préserver la cohérence entre orchestration et contrats des références.

Le candidat V3 hérite du socle V2.1 validé ; il ne repart ni de la V2 ni de l'ancienne V3 expérimentale (voir `base_de_travail.md` §1). Les acquis de la V3 expérimentale ne sont reportés qu'après le tri explicite décrit dans `base_de_travail.md` — ne pas les recopier automatiquement.

## Architecture du runtime

Le runtime comprend notamment :

```text
SKILL.md
references/
├── activite.md
├── activite_evaluee.md
├── activites_type/          # 17 gabarits depuis V3.1.0
│   ├── atelier.md
│   ├── barometre_humain.md
│   ├── brainstorming.md
│   ├── brique.md
│   ├── carte_conceptuelle.md
│   ├── devine_carte.md
│   ├── en_un_mot.md
│   ├── etude_de_cas.md
│   ├── evaluation_par_les_pairs.md
│   ├── facettes.md
│   ├── interview_croisee.md
│   ├── objet_express.md
│   ├── planche_meteo.md
│   ├── quiz.md
│   ├── recul.md
│   ├── retrospective.md
│   └── simulation_mise_en_situation.md
├── andragogie.md
├── decoupage_pedagogique.md
├── etat_des_paliers.md
├── glossaire.md
├── opo.md
├── production_documentaire.md
├── seance.md
├── sequence.md
├── syllabus.md
└── taxonomie.md
```

`SKILL.md` orchestre ; les références portent les contrats détaillés. Éviter de dupliquer dans `SKILL.md` tout le contenu normatif d'une référence.

## Garde-fous de conception

Lorsqu'un changement touche l'évaluation ou la progression, vérifier notamment :

- exposition ≠ preuve ;
- déclaration ≠ preuve attestée ;
- palier attaché à une notion, pas niveau global de l'apprenant ;
- preuve compatible avec ce que l'on veut attester ;
- valeur diagnostique de l'activité évaluée ;
- portée de la preuve limitée à ce qui est réellement observé ;
- alignement objectif → tâche → production → critères → preuve → conclusion ;
- pas de notation arbitraire par défaut ;
- critères apprenant visibles sans révéler prématurément solution/correction décisive.

Ces points restent repris dans le socle hérité de la promesse V3.1.0 (`promesse.md`, S01–S03 et garanties conservées de la V2.1).

## Publication

Ne jamais copier ou synchroniser ce dossier vers `dist/stable/` de sa propre initiative.

Une promotion doit être une opération explicite après validation, avec contrôle de copie, archive distribuable, commit et traçabilité.
