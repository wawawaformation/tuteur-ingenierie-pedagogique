# CLAUDE.md — `en_cours/`

Ce dossier est la **zone de développement du candidat courant**.

## État actuel

- `VERSION` indique actuellement **V2.1**.
- `promesse.md` porte la spécification fonctionnelle du candidat V2.1.0 : promesse centrale + P01–P03, garanties G01–G06.
- `base_de_travail.md` est la feuille de route actuelle de la trajectoire V2 → V2.1 → V3 ; elle fait foi pour le séquencement du travail.
- Le contenu de `en_cours/` n'est pas la version publique recommandée.
- La version publique reste dans `../dist/stable/` jusqu'à promotion explicite.

## Règles de modification

Avant de modifier `SKILL.md` ou une référence :

1. lire `promesse.md` ;
2. lire les références directement concernées ;
3. identifier les scénarios de non-régression potentiellement affectés ;
4. préserver la cohérence entre orchestration et contrats des références.

Le candidat V2.1 repart physiquement de la V2 stable. Les acquis de la V3 expérimentale ne sont reportés qu'après le tri explicite décrit dans `base_de_travail.md` — ne pas les recopier automatiquement.

## Architecture du runtime

Le runtime comprend notamment :

```text
SKILL.md
references/
├── activite.md
├── activites_type/
│   ├── atelier.md
│   ├── brique.md
│   ├── quiz.md
│   └── recul.md
├── andragogie.md
├── decoupage_pedagogique.md
├── etat_des_paliers.md
├── glossaire.md
├── opo.md
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

Ces points sont désormais repris explicitement dans la promesse V2.1.0 (`promesse.md`, P01–P03 et garanties G01–G06).

## Publication

Ne jamais copier ou synchroniser ce dossier vers `dist/stable/` de sa propre initiative.

Une promotion doit être une opération explicite après validation, avec contrôle de copie, archive distribuable, commit et traçabilité.
