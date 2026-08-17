# Règle de répétitions — validation V1

## Principe

Pour chaque couple `test × condition` :

1. exécuter deux répétitions indépendantes ;
2. scorer chaque trajectoire séparément ;
3. si les deux verdicts sont identiques, arrêter pour ce couple ;
4. si les deux verdicts diffèrent, exécuter obligatoirement la troisième
   répétition pré-déclarée dans `RUNS_CONDITIONNELS.csv`.

Il n'y a pas de quatrième répétition comportementale.

## Synthèse

- deux verdicts identiques : résultat concordant 2/2 ;
- après troisième répétition : retenir la majorité 2/3 et conserver
  explicitement la présence d'une instabilité ;
- si trois catégories différentes sont observées, aucune majorité n'est
  établie et le résultat reste non conclusif.

Une invalidité purement technique n'est pas une répétition comportementale.
Son éventuel rerun doit être identifié séparément.

La troisième répétition ne doit jamais être déclenchée en fonction du fait que
le résultat favorise ou défavorise le skill. Son seul déclencheur est le
désaccord entre les deux verdicts initiaux du même couple test × condition.
