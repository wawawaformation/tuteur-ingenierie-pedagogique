# CLAUDE.md — `en_cours/`

Ce dossier est la **zone de développement du candidat courant**.

## État actuel

- `VERSION` indique actuellement **V3**.
- `promesse.md` indique actuellement **« À déterminer »**.
- Le contenu de `en_cours/` n'est pas la version publique recommandée.
- La version publique reste dans `../dist/stable/` jusqu'à promotion explicite.

## Règles de modification

Avant de modifier `SKILL.md` ou une référence :

1. lire `promesse.md` ;
2. lire les références directement concernées ;
3. identifier les scénarios de non-régression potentiellement affectés ;
4. préserver la cohérence entre orchestration et contrats des références.

Ne pas recopier automatiquement les objectifs ou conclusions de V2 dans V3. La V3 doit acquérir sa propre promesse avant qu'une validation confirmatoire puisse être interprétée proprement.

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

Ces points décrivent l'héritage actuel du projet ; ils ne doivent pas être déclarés comme promesse V3 tant que `promesse.md` ne les a pas explicitement retenus.

## Publication

Ne jamais copier ou synchroniser ce dossier vers `dist/stable/` de sa propre initiative.

Une promotion doit être une opération explicite après validation, avec contrôle de copie, archive distribuable, commit et traçabilité.
