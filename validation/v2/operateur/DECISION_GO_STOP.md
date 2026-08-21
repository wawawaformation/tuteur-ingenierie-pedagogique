# Décisions GO / STOP — campagne V2

## GO de lancement

Aucun run officiel tant que le paquet n'est pas explicitement gelé.

Le GO de lancement exige au minimum : intégrité SHA-256 vérifiée, 40 lignes de base cohérentes dans `RUNS.csv`, 12 scénarios présents, candidat et personas présents, tests du collector au vert, paramètres Claude Code vérifiés et absence de collision avec une campagne déjà commencée.

## Pendant l'exécution

Un FAIL pédagogique n'est pas un motif pour modifier le protocole ou relancer le run.

STOP technique uniquement si l'intégrité du candidat/protocole est compromise, si l'isolation expérimentale ne peut plus être garantie, ou si un défaut d'instrumentation rend les données nouvelles non fiables.

## Après les runs de base

Construire le paquet aveugle, scorer indépendamment, adjudication éventuelle, puis appliquer la règle R3 aux seules cellules comportementalement discordantes.

## Décision V2

La décision de stabilisation/promotion suit `PLAN_EXPERIMENTAL.md`. Elle ne dépend pas d'un seuil numérique unique et la condition sans skill n'est pas obligée d'échouer.
