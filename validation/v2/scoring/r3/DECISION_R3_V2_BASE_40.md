# Décision R3 — Validation V2

Date : 2026-08-21

## État

Décision gelée après scoring aveugle, adjudication, gel des 40 verdicts
comportementaux et désaveuglement des deux répétitions de base.

Aucun run R3 n'a été exécuté au moment de cette décision.

## Références gelées

- Verdicts aveugles finaux :
  `1f33538dd7759c2add3515360ae4aa6946f4362b7eb8309e09952459e53c46a5`
- Synthèse désaveuglée :
  `74621b64458f639cf2d9d0eb13120e51995230266e503612b0e001d597b0a67e`

## Règle appliquée

Un R3 est déclenché uniquement lorsqu'une même cellule
`scenario_id + condition` présente des verdicts comportementaux finaux
différents entre R1 et R2.

Un désaccord entre scoreurs ne constitue pas à lui seul un motif de R3.

## Cellules déclenchant un R3

| Scénario | Condition | R1 | R2 | Décision |
|---|---|---|---|---|
| NOY001 | avec skill (A) | TRAJ-0020 / RUN-V2-010 / FAIL / ACCORD_S1_S2 | TRAJ-0039 / RUN-V2-014 / PASS / ACCORD_S1_S2 | R3=OUI |
| NOY002 | sans skill (B') | TRAJ-0029 / RUN-V2-015 / PASS / ACCORD_S1_S2 | TRAJ-0002 / RUN-V2-005 / INDÉTERMINÉ / ACCORD_S1_S2 | R3=OUI |
| NOY003 | sans skill (B') | TRAJ-0030 / RUN-V2-029 / PASS / ACCORD_S1_S2 | TRAJ-0004 / RUN-V2-033 / FAIL / ACCORD_S1_S2 | R3=OUI |

## Contrôle

- Cellules expérimentales examinées : 20
- Cellules stables R1/R2 : 17
- Cellules discordantes : 3
- R3 autorisés : 3

Les trois trajectoires ayant nécessité une adjudication inter-scoreurs
(TRAJ-0024, TRAJ-0035 et TRAJ-0038) ne participent à aucune des trois
discordances déclenchant un R3.

La décision de lancer ces trois R3 est donc indépendante des trois verdicts
issus de l'adjudication S3.

## Décision

R3 autorisé uniquement pour :

1. NOY001 — condition A — avec skill
2. NOY002 — condition B' — sans skill
3. NOY003 — condition B' — sans skill

Aucun autre R3 n'est autorisé à ce stade.
