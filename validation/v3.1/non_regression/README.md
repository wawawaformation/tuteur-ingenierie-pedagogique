# Scénarios candidats — V3.1.0

**Projet :** `tuteur-ingenierie-pedagogique`
**Mineure :** V3.1.0 — catalogue d'activités
**Statut :** scénarios candidats de validation de la promesse V3.1.0 — pas encore batterie de non-régression
**Condition :** A uniquement — avec candidat V3.1.0

---

## Finalité

Cette batterie couvre les deux propriétés nouvelles de `en_cours/promesse.md` :

- **ACT01 — Mobiliser le catalogue enrichi**
- **ACT02 — Choisir une activité pour sa pertinence pédagogique**

ainsi que ce que la promesse **disclaime** explicitement : ne pas imposer une activité existante lorsqu'aucune ne convient.

Le but n'est pas de vérifier qu'un gabarit figure dans le catalogue, mais qu'il est effectivement choisi, ou écarté, pour la bonne raison.

---

## Pourquoi aucune comparaison A / B′

Choix assumé, appuyé sur une règle déjà posée par le projet (`README.md`, section « Validation ») :

> Les contrats propres au produit — par exemple l'héritage du socle `Activité` ou **la représentation du catalogue de gabarits** — sont contrôlés directement sur le candidat, car un témoin sans skill ne connaît pas ces contrats.

Un témoin B′ ne connaît ni les noms, ni les finalités déclarées, ni le contrat de sélection du catalogue : le comparer sur le choix d'un gabarit nommé n'informerait sur rien.

**Conséquence à assumer.** La note SPEC d'ACT01 dans `promesse.md` signalait que le pouvoir discriminant tient à l'observable négatif *et* au contraste A / B′. En retirant le second, le contrôle de valeur ajoutée repose entièrement sur les scénarios négatifs (`V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3`, `V31-ACT02-4`) et sur la paire contrastive (`V31-ACT02-1` / `V31-ACT02-2`). Ceux-là portent donc la charge de preuve de la mineure ; un `PASS` sur le seul `V31-ACT01-1` ne démontrerait presque rien.

**Exigence de répétition.** `V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3`, `V31-ACT02-4` et `V31-ACT02-5` protègent une propriété de fiabilité, pas seulement de capacité (`promesse.md`, tête du Chantier 1) : chacun doit être rejoué **trois fois** (même stimulus, workspace neuf, majorité stable) avant de conclure — un `PASS` isolé ne suffit pas. Distinct de la passe unique du gel de non-régression (`base_de_travail.md` §13.2), qui porte sur la détection de régression d'une propriété déjà établie, pas sur sa validation initiale.

---

## Couverture du catalogue — limite connue, assumée

Ces scénarios vérifient un **mécanisme** de sélection (ACT01, ACT02), pas chaque gabarit un par un — c'est cohérent avec l'invariant d'architecture de la promesse : un gabarit ajouté doit rester mobilisable sans traitement spécifique ajouté au noyau, donc une couverture exhaustive gabarit par gabarit ne serait pas seulement coûteuse, elle contredirait cet invariant.

Constat au 2026-09-04, en comptant les occurrences de chaque gabarit dans les 8 fiches : 12 des 14 gabarits sont ouverts par au moins un run (comme réponse attendue, comme repli admis, ou comme distracteur explicitement mis sous tension). `Brainstorming` est nommé sans jamais être mis sous tension ; `Carte conceptuelle` et `Évaluation par les pairs` ne sont ouverts par aucune fiche.

Ce n'est pas un trou de propriété (le mécanisme reste vérifié), mais un trou de **conformité d'artefact** : un défaut structurel isolé sur ces deux derniers gabarits (champ de front matter mal nommé, section discriminante absente, référence obsolète) ne serait détecté par aucun scénario comportemental — c'est exactement la classe de défaut trouvée et corrigée le 2026-09-04 sur `atelier.md`/`quiz.md`/`recul.md` (voir `docs/v3.1/RAPPORT_INSTABILITE_V31-ACT02-3_2026-09-03.md` §9). C'est pour cette classe de défaut, pas pour la couverture comportementale, que `scripts/controle_conformite_gabarits.sh` a été ajouté : il vérifie mécaniquement les 14 gabarits (schéma de front matter, présence du discriminant, absence de référence obsolète, cohérence énumération/dossier), à faire tourner avant toute campagne.

Décision assumée : ne pas ajouter de scénario comportemental pour `Brainstorming` et `Carte conceptuelle` par la seule positive. Le contrôle mécanique couvre le risque de conformité ; un scénario de plus par gabarit non encore mis sous tension déplacerait la batterie de « suffisant » vers « exhaustif » sans gain proportionné.

---

## Prérequis d'exécution — bloquant

**Aucun de ces scénarios n'est jouable sur le candidat dans son état actuel.** `en_cours/references/activites_type/` ne contient que `atelier`, `brique`, `quiz`, `recul` ; les gabarits visés sont encore des brouillons dans `plus_tard/`.

Trois points à trancher avant tout run :

1. **Énumération du catalogue.** `en_cours/references/activite.md` l. 21-24 énumère les gabarits et se déclare « premier niveau de sélection » (l. 40). Tout gabarit joué doit y être référencé, sinon il reste invisible à l'agent quelle que soit la qualité de son front matter.

2. **Noms de champs dans le noyau.** `en_cours/SKILL.md` l. 72 nomme `purpose` et `typical_uses`. Les gabarits de `plus_tard/` (nouveaux comme retravaillés) n'ont plus `typical_uses` : ils portent `selection_keywords`, `participation`, `properties`, `taxonomy_levels`. Sans la micro-évolution prévue en `base_de_travail.md` §5.3, le noyau pointe un champ inexistant et ACT02 est insatisfiable tel qu'il est écrit.

3. **Homogénéité du schéma.** Les quatre gabarits du candidat sont sur l'ancien schéma, les onze nouveaux et les quatre retravaillés sur le nouveau. Un catalogue mixte rend certains contrastes asymétriques : `V31-ACT01-2` départage sur `participation` et `properties.ludique`, champs que le `quiz.md` actuel ne déclare pas.

### Deux voies d'exécution

- **(a) Fixture par injection** — précédent `NOY014` de la campagne V2.1 : injecter les gabarits nécessaires dans la copie isolée du candidat et recalculer le manifeste SHA-256, sans modifier le candidat versionné. Permet de tester la promesse **avant** l'implémentation, conformément à `base_de_travail.md` §9 et §15.
- **(b) Implémenter d'abord** un sous-ensemble minimal du catalogue, puis jouer. Plus simple à outiller, mais sort de l'ordre du §15 (test avant investissement d'implémentation).

Voie (a) recommandée pour cette phase ; la voie (b) devient naturelle au moment de la non-régression de la mineure.

---

## Scénarios

| ID | Propriété | Fonction |
|---|---|---|
| `V31-ACT01-1` | ACT01 | Mobiliser un nouveau gabarit clairement pertinent : `Facettes` |
| `V31-ACT01-2` | ACT01 | Ne pas favoriser un nouveau gabarit quand `Quiz` est plus pertinent |
| `V31-ACT01-3` | ACT01 | Ne pas se rabattre sur un gabarit familier (`Atelier`, `Quiz`) quand `Planche météo` est plus précisément pertinent |
| `V31-ACT02-1` | ACT02 | Situation à analyser → `Étude de cas` |
| `V31-ACT02-2` | ACT02 | Situation à jouer → `Simulation / mise en situation` |
| `V31-ACT02-3` | ACT02 | Besoin non couvert → adapter le gabarit existant le plus proche sans forcer un gabarit inadapté |
| `V31-ACT02-4` | ACT02 | Piège de mots-clés (`En un mot` vs `Rétrospective`) → suivre la fonction réelle, pas le vocabulaire de surface |
| `V31-ACT02-5` | ACT02 | Symétrique de `V31-ACT02-4` : besoin individuel et sans négociation → `En un mot` reste le bon choix, ne pas généraliser à tort vers `Rétrospective` |

`V31-ACT02-1` et `V31-ACT02-2` forment une **paire contrastive** : domaine, public, durée et taille de groupe identiques, seule la nature de la performance attendue change. Les verdicts restent attribués séparément ; un résultat identique sur les deux signale que l'agent ne départage pas sur la finalité.

`V31-ACT02-4` et `V31-ACT02-5` forment une **paire contrastive symétrique** : même moment typique (fin de journée), même risque de surface (« feedback », « retour »), fonction opposée (collective vs individuelle). Ajoutée le 2026-09-04 : la batterie d'origine ne couvrait que le sens `En un mot` → `FAIL`, jamais le sens `En un mot` → `PASS`.

**`V31-ACT02-5` : PASS unanime (3/3), après diagnostic et réparation d'un défaut d'artefact.** La première campagne donnait 2/3 (`Planche météo` une fois) ; en croisant les traces de lecture, le run divergent n'avait tout simplement jamais eu `En un mot` sous les yeux — `planche_meteo.md` ne le mentionnait nulle part comme concurrent, alors que la réciproque existait dans `en_un_mot.md`. Un contrôle mécanique `CG5` (réciprocité des sections `## Distinction avec X`) a été ajouté à `scripts/controle_conformite_gabarits.sh` et a révélé 7 paires asymétriques sur tout le catalogue, corrigées. Rejoué ensuite : 3/3 `En un mot`, mêmes 4 fichiers ouverts par les 3 runs — seule variable ayant changé, le contenu de `planche_meteo.md`. Détail complet dans la fiche.

`V31-ACT02-3` protège ce que la promesse disclaime : avec un catalogue passant de 4 à ~15 entrées, le risque nouveau n'est pas de manquer un gabarit mais d'en forcer un.

`V31-ACT01-3` protège le risque symétrique de `V31-ACT01-2` : ne pas favoriser un gabarit *parce qu'il est nouveau* (ACT01-2) n'est pas la même chose que ne pas l'*écarter* parce qu'un gabarit familier suffit superficiellement (ACT01-3). Les deux biais jouent en sens opposé.

---

## Convention d'exécution partagée

Source unique pour les règles communes : les fiches ne répètent que ce qui leur est propre.

Pour chaque scénario :

- workspace neuf, candidat V3.1.0 chargé avec l'état de catalogue précisé par la fiche ;
- aucun persona injecté sauf mention explicite de la fiche ;
- stimulus envoyé exactement tel qu'il est défini ;
- verbatim complet conservé, avec les traces de lecture de fichiers ;
- **l'opérateur ne nomme jamais un gabarit, ni ne suggère le type attendu**, y compris par la négative.

Si l'agent demande une précision, répondre d'abord à partir des informations déjà présentes dans le scénario. Lorsqu'aucune information pertinente supplémentaire n'existe :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Si la décision opérateur exigerait de connaître un critère volontairement masqué, rendre `AMBIGU_OPERATEUR` plutôt que de supposer (formulation reprise de la neutralisation appliquée à `NOY005` en V2.1).

L'opérateur fait au mieux, à partir des informations disponibles, pour permettre de confirmer ou d'invalider l'objectif du test, sans introduire artificiellement de nouveaux éléments.

---

## Verdicts

`PASS`, `FAIL`, `INDÉTERMINÉ` — conformément à `validation/CLAUDE.md`.

Rappels de scoring applicables ici :

- juger les observables réellement présents, ne pas ajouter de règle implicite plus stricte que l'oracle ;
- ne pas transformer une préférence pédagogique en critère de `FAIL` ;
- un défaut de chargement du skill ou de collecte est une **invalidité technique**, pas un `INDÉTERMINÉ` ;
- une réponse qui nomme un type retenu puis mentionne une alternative reste scorable sur le type retenu ; une réponse qui n'en retient aucun est `INDÉTERMINÉ`.

---

## Après validation

Ces fiches sont d'abord des scénarios de validation de la promesse V3.1.0.

Si elles sont retenues après stabilisation et promotion de la mineure, elles deviennent la batterie de non-régression propre à V3.1.0, rejouée ensuite à chaque mineure suivante (`base_de_travail.md` §13.1).
