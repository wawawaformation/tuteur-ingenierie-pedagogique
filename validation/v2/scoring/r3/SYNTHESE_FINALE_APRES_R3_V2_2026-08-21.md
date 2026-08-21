# Synthèse finale après R3 — Validation V2

Date : 2026-08-21

## 1. Périmètre

La campagne comporte :
- **40 runs de base** définis avant exécution ;
- **3 répétitions comportementales R3 conditionnelles**, déclenchées uniquement après scoring, adjudication, gel et désaveuglement des 40 runs de base.

Les trois R3 ne sont pas des reruns techniques. Ils ont été déclenchés parce que R1 et R2 d'une même cellule présentaient des verdicts comportementaux différents.

Le plan expérimental gelé précise que R3 sert à **caractériser la stabilité du comportement, pas à effacer un résultat défavorable**.

En conséquence, les 40 verdicts de base restent intacts. Les trois R3 sont rapportés séparément et ne sont pas ajoutés mécaniquement aux 40 runs pour fabriquer un nouveau taux global sur 43 runs.

## 2. Résultats des 40 runs de base

### Condition avec skill

24 runs de base :
- PASS : **23**
- FAIL : **1**
- INDÉTERMINÉ : **0**

Taux descriptif de PASS : **23/24 = 95,8 %**.

### Condition sans skill

16 runs de base :
- PASS : **2**
- FAIL : **13**
- INDÉTERMINÉ : **1**

Taux descriptif de PASS : **2/16 = 12,5 %** si l'INDÉTERMINÉ est conservé au dénominateur.

Ces taux sont descriptifs. Le plan expérimental impose de privilégier l'analyse par scénario et par cellule.

## 3. Cellules ayant déclenché R3

| Scénario | Condition | R1 | R2 | R3 humain officiel | Lecture après R3 |
|---|---|---|---|---|---|
| NOY001 | avec skill (A) | FAIL | PASS | PASS | 2 PASS / 1 FAIL ; instabilité localisée, R3 favorable |
| NOY002 | sans skill (B') | PASS | INDÉTERMINÉ | PASS | 2 PASS / 1 INDÉTERMINÉ ; R3 comportemental favorable |
| NOY003 | sans skill (B') | PASS | FAIL | PASS | 2 PASS / 1 FAIL ; instabilité localisée, R3 favorable |

Les trois répétitions supplémentaires sont donc **PASS**.

Elles ne suppriment ni le FAIL initial de NOY001 avec skill, ni le FAIL initial de NOY003 sans skill, ni l'INDÉTERMINÉ initial de NOY002 sans skill. Elles apportent une troisième observation favorable dans chacune des trois cellules qui avaient justifié une répétition supplémentaire.

## 4. Lecture par scénario après R3

### NOY001 — élicitation du point de départ

Avec skill : `FAIL / PASS / PASS`.

Le R3 confirme qu'un comportement conforme peut être reproduit, mais la cellule n'est pas parfaitement stable puisque le FAIL de base reste un résultat valide.

Le scoring humain du R3 a également mis en évidence un point de vigilance méthodologique : « avant exposition substantielle » ne doit pas être durci en une règle implicite interdisant tout cadrage ou toute amorce pédagogique avant la réponse diagnostique.

Sans skill : `FAIL / FAIL`.

Le contraste avec la condition avec skill reste descriptivement favorable au candidat.

### NOY002 — exposition / auto-déclaration / preuve

Avec skill : `PASS / PASS`.

Sans skill : `PASS / INDÉTERMINÉ / PASS`.

Le R3 montre un comportement conforme en condition sans skill lorsque toute la trajectoire est observable. Le résultat de base INDÉTERMINÉ reste toutefois conservé comme tel.

### NOY003 — QCM et capacité d'application

Avec skill : `PASS / PASS`.

Sans skill : `PASS / FAIL / PASS`.

Le R3 est conforme : le QCM 10/10 est reconnu comme preuve de compréhension théorique, sans attestation de la capacité à appliquer.

### NOY004 à NOY008

Les cellules avec skill sont stables en PASS sur les deux répétitions de base.

Les cellules sans skill sont stables en FAIL sur les deux répétitions de base.

Aucun R3 n'était autorisé pour ces cellules.

### NOY009 à NOY012

Ces quatre tests propriétaires, exécutés uniquement avec skill, sont chacun stables en `PASS / PASS`.

Ils satisfont donc le premier critère de stabilisabilité défini par le plan expérimental.

## 5. Scoring des R3

Une décision méthodologique spécifique a été prise avant la fixation des verdicts R3 : leur scoring officiel est **humain uniquement** et cette règle est gelée pour la campagne.

Motif : l'analyse de R3-NOY001-A a montré qu'un agent scoreur pouvait durcir l'oracle au-delà de son texte en transformant « avant exposition substantielle » en une exigence implicite de quasi-absence de contenu avant diagnostic.

Les agents IA ont pu assister l'opérateur pendant l'exécution et fournir des avis consultatifs, mais ils n'ont aucune autorité sur les trois verdicts officiels R3.

## 6. Interprétation au regard des critères de décision V2

Le plan expérimental définit notamment comme critères d'un candidat stabilisable :
- NOY009 à NOY012 stables en PASS ;
- absence de défaut bloquant établi sur NOY001 à NOY008 ;
- instabilités éventuelles localisées et interprétables ;
- intégrité du candidat, des scénarios et du protocole préservée.

À l'issue des données actuellement disponibles :

- **NOY009 à NOY012 : critère satisfait** — 8 PASS sur 8 ;
- **NOY001 à NOY008 : aucun défaut bloquant reproductible du candidat n'est établi par les résultats** ;
- les trois cellules discordantes ont été localisées avant R3 et les trois R3 sont PASS ;
- NOY001 avec skill reste une cellule imparfaitement stable (`FAIL / PASS / PASS`) et doit être conservée comme telle dans l'interprétation ;
- les résultats de base ne sont pas réécrits après R3.

L'ensemble des résultats est donc **compatible avec le statut “candidat stabilisable” au sens du plan expérimental**.

Cette formulation ne constitue pas à elle seule une promotion de V2 vers `stable/` ou `dist/stable/`. Une éventuelle promotion reste une décision explicite distincte.

## 7. Résumé final

### Base gelée
- 40 runs
- avec skill : **23 PASS / 1 FAIL**
- sans skill : **2 PASS / 13 FAIL / 1 INDÉTERMINÉ**

### R3 conditionnels
- R3 autorisés : **3**
- R3 exécutés et scorés humainement : **3**
- PASS : **3**
- FAIL : **0**
- INDÉTERMINÉ : **0**

### Conclusion méthodologique
Les R3 renforcent l'observation favorable sur les trois cellules instables, sans effacer les résultats antérieurs. Les contrats propres à la V2 sont stables en PASS et les instabilités restantes sont localisées et interprétables. Le résultat est compatible avec un **candidat stabilisable**, sous réserve d'une décision explicite séparée pour toute promotion.
