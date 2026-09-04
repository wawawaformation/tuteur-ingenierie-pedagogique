# Rapport — Instabilité du scénario V31-ACT02-3 (candidat V3.1.0)

**Date :** 2026-09-03
**Statut :** ~~ouvert, non tranché~~ → **cause racine identifiée le 2026-09-04** (§9). Les 4 runs de ce rapport sont **requalifiés non concluants** : ils ont été joués sur une fixture violant le prérequis bloquant n°3 de la batterie. Ni la lecture A ni la lecture B du §5 n'est retenue.
**Portée :** ce rapport documente une divergence trouvée en vérifiant le candidat réel après le gel de `promesse.md` (2026-09-03). Il ne modifie ni la promesse, ni les fichiers du runtime, ni les oracles — c'est un constat, la décision reste à prendre.

> **Lecture de ce document.** Les §1 à §8 sont conservés dans leur état du 2026-09-03, y compris leurs conclusions provisoires depuis dépassées : ils constituent la trace des faits observés. Le §9, ajouté le 2026-09-04, porte le diagnostic et prévaut sur les §5 et §7.

---

## 1. Contexte

`tuteur-ingenierie-pedagogique` est un skill d'assistance à l'ingénierie pédagogique. La mineure V3.1.0 enrichit son catalogue d'activités pédagogiques (« gabarits ») : au lieu de 4 gabarits (Atelier, Brique, Quiz, Recul), le candidat en gagne une dizaine (Étude de cas, Simulation, Facettes, etc.), chacun avec un `purpose` déclaré et des métadonnées de sélection.

La propriété testée (ACT02 de `en_cours/promesse.md`) dit :

> Le raisonnement part de la situation et de l'objectif réels : *situation + objectif → une activité du catalogue correspond-elle ? → oui : la choisir, en la départageant des autres candidates plausibles → non : dériver une activité du gabarit existant qui s'en rapproche le plus, plutôt que reconstruire depuis zéro.*
>
> Le gabarit doit permettre de produire ce résultat **de façon fiable et systématique**, pas une fois par chance.

## 2. Chronologie des faits

1. `promesse.md` gelée le 2026-09-03 sur la base de 15 exécutions (7 scénarios, dont 4 répétés 3 fois), **15/15 PASS**, réalisées sur une **copie de test** (`en_cours/` dupliqué, gabarits candidats ajoutés, corps des 4 gabarits existants remplacés par leur version *retravaillée* — schéma homogène, mais références documentaires obsolètes vers `taxonomie.md` §2 au lieu de `activite_evaluee.md`).
2. Implémentation ensuite sur le **candidat réel** (`en_cours/`) : les 10 nouveaux gabarits copiés, mais les 4 gabarits existants gardés avec leur **corps original** (seul le front matter enrichi), pour ne pas réintroduire les références obsolètes repérées dans le corps retravaillé.
3. Vérification de contrôle (3 scénarios, pas la campagne complète) sur ce candidat réel : `V31-ACT01-1` PASS, `V31-ACT02-4` PASS, **`V31-ACT02-3` FAIL** (retient `Étude de cas` sans dossier fourni).
4. Décision prise : fusionner le corps *retravaillé* de `brique.md` (avec son arbre de décision explicite Brique/Atelier) dans le candidat réel, références corrigées vers `activite_evaluee.md`.
5. `V31-ACT02-3` rejoué 3 fois sur le candidat ainsi corrigé : **Étude de cas, Brique, Recul** — trois réponses différentes.

Au total, sur le candidat réel : **4 runs, 3 réponses distinctes** (Étude de cas ×2, Brique ×1, Recul ×1).

## 3. Le scénario en cause

**Stimulus exact :**

```text
Je forme des aides-soignants en alternance.

Pendant leur semaine en service, je veux qu'ils observent comment un professionnel expérimenté annonce une contrainte désagréable à un patient : un soin reporté, une attente prolongée.

Je ne serai pas présent : ils sont seuls sur place, en situation réelle, et je récupère ce qu'ils en rapportent la semaine suivante, en centre de formation.

Je veux que ce matériau soit exploitable à leur retour.

Choisis le type d'activité le plus pertinent parmi ceux disponibles dans le skill.
Indique d'abord le type retenu, puis prépare l'activité.
```

**Intention du scénario** : aucun gabarit spécialisé du catalogue ne couvre exactement « observation non encadrée d'un tiers en situation réelle, matériau exploité plus tard ». Le scénario vérifie que l'agent adapte le gabarit générique le plus proche plutôt que de forcer un gabarit inadapté.

**Trois gabarits en tension**, avec leur `purpose` déclaré :

- **Brique** : « Proposer une activité élémentaire et ciblée centrée sur une tâche identifiable, sans imposer une démarche structurée en plusieurs étapes. »
- **Étude de cas** : « Faire analyser une situation contextualisée afin d'identifier les éléments pertinents, d'établir un diagnostic, de formuler des hypothèses ou de prendre une décision argumentée. » (repose normalement sur un dossier déjà écrit, fourni à l'apprenant)
- **Recul** : « Développer la réflexivité en faisant expliciter, analyser et mettre en perspective une expérience, une production, une démarche ou des choix. » (normalement centré sur *sa propre* expérience/action, pas sur l'observation d'un tiers)

**Oracle (`validation/v3.1/non_regression/V31-ACT02-3.md`, défini avant les runs)** :
- `PASS` : construction depuis le socle générique, ou repli explicite sur un gabarit générique (Brique/Atelier) sans déformer le besoin, ou décomposition en deux temps (observation + `Recul` *au retour*, sur la propre expérience de l'apprenant après coup).
- `FAIL` : retenir Étude de cas sans dossier fourni (ou en inventer un) ; déformer la situation réelle non encadrée en scène jouée ou en dossier écrit ; appliquer le contrat d'un gabarit spécialisé à une phase que sa finalité déclarée ne couvre pas, sans le signaler.

## 4. Résultats détaillés des 4 runs sur le candidat réel

| Run | Corps de Brique | Type retenu | Raisonnement résumé | Verdict |
|---|---|---|---|---|
| 1 | original | **Étude de cas** | « La situation observée devient le matériau réel à analyser au retour » | FAIL |
| 2 | retravaillé (fusionné) | **Étude de cas** | Même raisonnement : traite l'observation comme matériau d'étude de cas | FAIL |
| 3 | retravaillé (fusionné) | **Brique** | « Le cas n'existe pas encore : il doit être construit sur le terrain » — écarte explicitement Étude de cas pour cette raison | PASS |
| 4 | retravaillé (fusionné) | **Recul** | Traite l'observation d'un tiers comme une « expérience professionnelle vécue ou observée », mobilise le questionnement réflexif (expliciter/analyser/projeter) directement sur la phase d'observation elle-même | Douteux, probable FAIL (Recul appliqué à la phase d'observation elle-même, pas « au retour » comme l'oracle l'anticipe) |

Aucune reformulation du stimulus n'a eu lieu entre les runs. Le seul changement entre le run 1 et les runs 2-4 est l'enrichissement du corps du gabarit Brique — qui a fait apparaître Brique comme option choisie une fois, sans stabiliser le résultat.

> **Requalifié le 2026-09-04 : ces 4 runs sont non concluants.** La fixture sur laquelle ils ont été joués viole le prérequis bloquant n°3 de la batterie (§9). Les verdicts ci-dessus restent consignés comme observations, mais ne peuvent pas servir de charge contre la propriété ACT02.

## 5. Les deux lectures possibles, non tranchées

**Lecture A — le scénario est mal posé.** La situation décrite (observer un tiers, sans encadrement, exploiter plus tard) admet légitimement plusieurs traitements pédagogiques défendables : collecter un matériau brut (Brique), construire un cas d'étude a posteriori à partir de ce qui est rapporté (Étude de cas, en assouplissant l'exigence de dossier pré-écrit), ou faire réfléchir l'apprenant sur ce qu'il a observé (Recul, en assouplissant l'exigence de « sa propre » expérience). Dans cette lecture, le défaut est dans la conception du scénario de test, pas dans le candidat.

**Lecture B — la propriété promise est trop ambitieuse.** La promesse affirme que le catalogue enrichi permet un « repli fiable et systématique » sur le gabarit le plus proche. Si, dès qu'aucun gabarit ne domine clairement, le choix devient erratique d'un run à l'autre, alors la promesse surestime ce que le mécanisme peut garantir — le défaut serait alors dans la formulation de la promesse elle-même, pas dans un scénario isolé.

Aucune des deux lectures n'a été retenue à ce stade. Une troisième explication (facteur non identifié) reste possible.

> **Tranché le 2026-09-04 : c'est la troisième explication.** Ni A ni B. Le facteur non identifié est un défaut de fixture, documenté au §9. Les deux lectures ci-dessus sont conservées telles qu'elles ont été formulées, mais ne sont pas retenues.

## 6. Ce qui reste non vérifié

Seuls 3 des 7 scénarios de la batterie ont été rejoués sur le candidat réel (`V31-ACT01-1`, `V31-ACT02-3`, `V31-ACT02-4`), plus les 4 runs de ce rapport. Les quatre autres (`V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-1`, `V31-ACT02-2`) n'ont été validés que sur l'environnement de test initial (corps de gabarits plus riche, avec des références documentaires depuis corrigées) — pas sur le candidat réel tel qu'il existe maintenant.

## 7. Statut du gel de la promesse

`en_cours/promesse.md` reste marquée gelée dans son texte (état au 2026-09-03), mais ce rapport documente que la validation sous-jacente ne tient pas entièrement pour `V31-ACT02-3` sur le candidat réellement implémenté. Aucune modification n'a été apportée à `promesse.md` en conséquence de ce rapport — décision en attente.

> **Corrigé le 2026-09-04 (§9).** La validation sous-jacente n'est pas en cause : la fixture l'était. Le gel n'a pas à être révoqué. Ce qui reste vrai et ne change pas : `V31-ACT02-3` n'a **pas encore** été validé sur un candidat réel conforme — la réserve porte sur ce point précis, pas sur la propriété.

## 8. Ce qui a été demandé en parallèle

Le bilan de ce rapport a été transmis à un autre agent (hors session) pour un second avis indépendant sur les lectures A/B du §5. Réponse non encore intégrée à ce document au moment de sa création.

---

## 9. Diagnostic — 2026-09-04 : catalogue hétérogène sur les corps de gabarits

Ajouté après le corps initial du rapport. Cette section prévaut sur les §5 et §7.

### 9.1 Ce qui a été comparé

L'environnement 3/3 PASS n'existe plus en tant que répertoire, mais ses sources sont conservées : `plus_tard/activites_type_origine_retravaillees.zip` (les 4 historiques retravaillés) et `plus_tard/nouvelles_activites_v3_metadonnees.zip` (les nouveaux). Ces sources ont été extraites et comparées fichier par fichier au candidat réel.

### 9.2 Différence trouvée

Le **front matter** des 4 gabarits historiques est **rigoureusement identique** entre les deux environnements. La différence est entièrement dans le corps : la section de discriminant de sélection (`## Pourquoi choisir…` / `## Quand choisir…`).

| Gabarit | Environnement 3/3 PASS | Candidat réel |
|---|---|---|
| `atelier.md` | ✅ `## Pourquoi choisir un Atelier ?` | ❌ absent |
| `quiz.md` | ✅ `## Pourquoi choisir un Quiz…` | ❌ absent |
| `recul.md` | ✅ `## Pourquoi choisir un Recul ?` | ❌ absent |
| `brique.md` | ✅ | ✅ (corps fusionné aux runs 2-4) |
| les 10 nouveaux | ✅ | ✅ |

Dans le candidat réel : **11 gabarits sur 14 portent un discriminant de sélection explicite, 3 n'en portent aucun** — et ces 3 sont précisément les gabarits génériques que l'oracle attend comme repli légitime.

### 9.3 Mécanisme

Le départage s'opère entre gabarits **asymétriquement documentés** :

- `Atelier`, repli générique principal, n'a aucun argumentaire de sélection à opposer aux 10 spécialisés qui en ont tous un ;
- `Recul` a perdu la section qui l'ancre sur l'action **propre** de l'apprenant (« ce qu'il a fait ; pourquoi il l'a fait ainsi ; les choix qu'il a effectués ») ainsi que son contrôle « Finalité ». Son chapeau seul — « revenir sur une expérience, une action, une production ou une démarche » — admet donc l'observation d'un tiers. C'est mot pour mot le raisonnement du run 4 (« expérience professionnelle vécue ou observée ») ;
- `Brique` n'a retrouvé son argumentaire qu'à la fusion du run 2, ce qui explique son apparition au run 3 sans stabilisation : ses deux concurrents génériques restaient dénudés.

Le force-fit observé est donc **produit par la fixture**, pas par la propriété ACT02.

### 9.4 Ce défaut était annoncé comme bloquant

`validation/v3.1/non_regression/README.md`, prérequis bloquant n°3 :

> **Homogénéité du schéma.** Les quatre gabarits du candidat sont sur l'ancien schéma, les onze nouveaux et les quatre retravaillés sur le nouveau. Un catalogue mixte rend certains contrastes asymétriques.

Ce prérequis a été appliqué **à moitié** : front matter harmonisé, corps non harmonisés. Les 4 runs du §4 ont donc été joués sur une fixture que la batterie déclarait elle-même invalide.

### 9.5 Réserves d'honnêteté

Deux différences entre les deux environnements ne sont pas exclues comme facteurs contributifs :

1. l'`activite.md` de la copie de test était « patché localement » pour le référencement ; son libellé exact n'est pas reconstructible ;
2. la copie de test contenait `tabou_conceptuel.md`, absent du candidat — la composition du catalogue diffère donc d'une entrée.

Aucune des deux n'explique l'asymétrie du §9.2, mais elles interdisent d'affirmer que le discriminant absent est le facteur **unique**.

### 9.6 Décision retenue

1. les 4 runs du §4 sont requalifiés **non concluants** ;
2. les lectures A et B du §5 ne sont pas retenues ; `promesse.md` n'est pas dégelée et `V31-ACT02-3` n'est pas retravaillé ;
3. réparation par **portage chirurgical** : ajouter la seule section discriminante dans `atelier.md`, `quiz.md`, `recul.md`, réécrite au vocabulaire courant du candidat. Le corps entier du ZIP n'est pas reporté : les corps du candidat sont postérieurs (vocabulaire « palier », références vers `activite_evaluee.md` après le split `7020ec3`), là où les retravaillés pointent encore vers `taxonomie.md §2` — un remplacement en bloc régresserait des acquis V2.1 ;
4. `V31-ACT02-3` rejoué ensuite, 3 exécutions indépendantes, **exécutant Sonnet** comme la campagne initiale.

---

## 10. Réparation appliquée et vérifiée — 2026-09-04

### 10.1 Portage chirurgical

Section `## Pourquoi choisir…` ajoutée dans `atelier.md`, `quiz.md` et `recul.md` du candidat, au même emplacement que dans les sources retravaillées, texte repris sans invention. Corps postérieurs du candidat non touchés ; aucune référence vers `taxonomie.md §2` réintroduite.

Contrôle après portage : **14 gabarits sur 14** portent un discriminant de sélection, contre 11 sur 14 avant.

Deux éléments présents dans le `recul.md` retravaillé n'ont **pas** été portés, car ils ne sont pas des discriminants de sélection : un contrôle « Finalité » et un contrôle « Preuve individuelle ». À trancher séparément.

### 10.2 Runs de vérification

Fixture isolée construite depuis le candidat corrigé (runtime seul : `SKILL.md` + `references/`, sans `promesse.md` ni `base_de_travail.md`), manifeste SHA-256 calculé, empreinte du manifeste `d70b387fb36f2db82abe782cf05fff993cde9a6d95c191af99d53e9afca4f1f1`.

Catalogue consigné au moment des runs, 14 entrées : `atelier`, `brainstorming`, `brique`, `carte_conceptuelle`, `devine_carte`, `en_un_mot`, `etude_de_cas`, `evaluation_par_les_pairs`, `facettes`, `planche_meteo`, `quiz`, `recul`, `retrospective`, `simulation_mise_en_situation`.

Exécutants : 3 sous-agents vierges **Sonnet** (même modèle que la campagne initiale), sans accès à la conversation ni aux oracles, restreints à la fixture, stimulus exact, aucun gabarit nommé par l'opérateur.

| Exécution | Type retenu | Verdict |
|---|---|---|
| 1 | Brique | PASS |
| 2 | Brique | PASS |
| 3 | Brique | PASS |

**3/3 PASS, unanimes.** Aucune clause `FAIL` de l'oracle déclenchée : aucun dossier inventé, aucune scène jouée, aucune présence du formateur supposée, distinction des phases observation / exploitation au retour explicite dans les trois cas. Les trois refusent de concevoir l'activité de reprise faute de demande plutôt que de l'inventer.

Les trois écartent `Recul` en citant le discriminant restauré (l'ancrage sur l'action propre de l'apprenant) et `Étude de cas` en citant l'exigence de cas préexistant — les deux mécanismes identifiés au §9.3. Le résultat reproduit celui de l'environnement 3/3 PASS d'origine (`Brique`, 3/3).

### 10.3 Ce qui reste dû

Le candidat a changé après ces corrections. `V31-ACT01-1` et `V31-ACT02-4`, qui avaient été rejoués sur le candidat réel **avant** le portage, portent donc sur un état antérieur ; les 4 scénarios du §6 n'ont toujours pas été joués sur le candidat réel. Une **passe complète de la batterie sur le candidat corrigé** reste à faire avant de considérer V3.1.0 validée sur le candidat versionné.

---

**Prochaine étape** : ~~trancher entre les lectures A et B~~ — fait au §9. ~~Portage chirurgical, puis 3 exécutions de `V31-ACT02-3`~~ — fait au §10, 3/3 PASS. Reste : passe complète de la batterie (15 exécutions) sur le candidat corrigé.
