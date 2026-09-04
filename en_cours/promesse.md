# Promesse candidate V3.1.0

Ce document constitue la **spécification fonctionnelle candidate** de la mineure V3.1.0 du skill `tuteur-ingenierie-pedagogique`.

V3.1.0 est la première mineure de la V3 (voir `base_de_travail.md` §4.1 pour le séquencement complet). Elle hérite du socle validé en V2.1 et engage un seul chantier :

1. étoffer et mieux exploiter le catalogue d'activités.

Les chantiers 2 (leviers cognitifs et biais) et 3 (tutorat) sont prévus par la feuille de route mais ne sont pas engagés par cette promesse ; ils feront l'objet des mineures V3.2.0 et V3.3.0.

La promesse reste volontairement limitée à des comportements importants, observables et susceptibles de modifier une décision pédagogique. Elle ne promet pas d'améliorer globalement toute production pédagogique.

---

# Promesse centrale

> **Conserver les acquis validés de la V2.1 et les étendre afin que l'agent puisse identifier et choisir, parmi une boîte à outils pédagogique plus riche, l'activité la plus pertinente au regard de l'objectif, du contexte et du besoin pédagogique effectif.**

---

# 0. Socle hérité de la V2.1

La V2.1 constitue la **baseline comportementale** de V3.1.0.

Ses propriétés validées restent acquises et leur source normative demeure la V2.1 gelée (`SKILL.md` et `references/` du candidat, non-régressés) — cette promesse ne les redéfinit pas, elle les rappelle pour mémoire :

- raisonnement notion → palier → fondement → attestation, avec déclaration ≠ preuve et manque de preuve ≠ preuve de manque ;
- valeur diagnostique d'une activité évaluée préservée (budget de nouveauté, portée limitée d'une preuve) ;
- alignement objectif → tâche → production → critères → preuve → conclusion ;
- garde-fous validés (pas de notation arbitraire, pas de persistance inventée, dérogations locales résolues explicitement).

Toute modification de ce socle doit être considérée comme une modification du noyau et être justifiée explicitement. La validation de V3.1.0 devra vérifier la non-régression des comportements V2.1 concernés.

---

# Chantier 1 — Étoffer et mieux exploiter le catalogue d'activités

Les activités ajoutées ne sont pas des formats que l'agent improvise ou invente : ce sont des formats **courants, éprouvés par un formateur expérimenté**, mis à disposition pour que l'agent les mobilise directement plutôt que de reconstruire à chaque fois une structure équivalente par improvisation. La plupart existent déjà, sous des noms proches, dans les LMS courants (quiz, étude de cas, simulation…) — ce n'est donc pas un vocabulaire propre au skill, mais un vocabulaire partagé avec le terrain, auquel un formateur est déjà familiarisé.

La valeur n'est donc pas seulement « l'agent sait-il produire quelque chose de correct sans le gabarit » — un socle générique bien utilisé peut souvent s'en approcher, les runs exploratoires de V3.1.0 l'ont déjà montré (`Atelier` seul s'approche de `Facettes` ou d'`Étude de cas`) — mais « le gabarit lui permet-il de produire ce résultat de façon fiable et systématique, plutôt qu'une fois, avec un modèle capable, au prix d'une improvisation ». C'est cette fiabilité, pas la seule capacité brute, que les scénarios doivent viser.

**Ce que « fiable et systématique » implique pour la validation, précisément parce que c'est ce que la promesse engage.** Un scénario qui vérifie qu'un choix est correct une seule fois ne teste pas la fiabilité — il teste la capacité, ce que les runs exploratoires ont déjà fait sans qu'un gabarit existe. Vérifier la fiabilité suppose de rejouer le **même stimulus plusieurs fois** et de constater que le choix reste stable, plutôt que de varier selon le tirage du modèle.

Cette exigence de répétition porte spécifiquement sur les scénarios qui protègent une propriété de fiabilité (les scénarios ACT01/ACT02 qui portent la charge de preuve — voir `validation/v3.1/non_regression/README.md`). Elle est **distincte** de la règle de passe unique du gel de non-régression (`base_de_travail.md` §13.2), qui porte sur la détection de régression d'une propriété déjà validée, pas sur la validation initiale d'une propriété nouvelle : le gel rejoue une fois une batterie déjà éprouvée ; la validation d'ACT01/ACT02 doit d'abord établir qu'elle est éprouvable. Repère minimal retenu : trois exécutions indépendantes du même stimulus, majorité stable pour conclure à la fiabilité — à ajuster si l'expérience montre que ce seuil est mal calibré.

## Invariant d'architecture hérité de la V2.1

La V2.1 permet déjà d'ajouter un gabarit d'activité sans introduire de règle générale nouvelle dans le noyau : `SKILL.md` décrit un mécanisme de sélection générique (lecture du front matter des candidats pour départager) et ne nomme aucun gabarit particulier.

V3.1.0 ne revendique donc pas cette extensibilité comme une propriété nouvelle. Elle doit la **préserver** pendant l'enrichissement effectif du catalogue.

Précision vérifiée sur le runtime : la découvrabilité repose aujourd'hui sur le catalogue énuméré de `references/activite.md`, présenté comme « premier niveau de sélection ». Référencer un nouveau gabarit à cet endroit relève du **référencement attendu** (`base_de_travail.md` §5.4), pas d'une règle générale ajoutée au noyau — mais cela reste une opération nécessaire, et le passage à un catalogue nettement plus fourni pose une question de conception à trancher pendant la mineure, non par cette promesse.

Cet invariant relève principalement de la conception et de la revue du diff. Les scénarios de V3.1.0 peuvent toutefois vérifier indirectement qu'un nouveau gabarit reste découvrable et mobilisable sans traitement spécifique ajouté au noyau.

---

## ACT01 — Mobiliser le catalogue enrichi

L'agent doit pouvoir mobiliser les activités ajoutées au catalogue V3.1.0 lorsqu'elles sont pertinentes pour la situation pédagogique.

Les nouveaux gabarits ne bénéficient d'aucune priorité du seul fait de leur nouveauté. Ils rejoignent la même boîte à outils que les activités déjà présentes.

Le catalogue reste :

> **une boîte à outils, pas un parcours à dérouler.**

L'existence d'un type d'activité dans le catalogue ne constitue jamais, à elle seule, une raison de le choisir.

### Observable attendu

Face à une situation pour laquelle un nouveau gabarit V3.1.0 est plus pertinent que les activités historiques, l'agent peut l'identifier et le mobiliser.

Face à une situation où ce nouveau gabarit n'est pas pertinent, il ne le choisit pas simplement parce qu'il est disponible.

> **Note pour la phase SPEC :** la moitié positive de cet observable risque d'être satisfaite trivialement (un fichier pertinent existe, l'agent l'utilise). Le pouvoir discriminant tient surtout à la moitié négative — absence de biais de nouveauté — et au contraste A / B′, où un agent sans skill tend à inventer un format plutôt qu'à exploiter un catalogue existant. Les scénarios doivent viser ces deux angles.

**Risque symétrique : le biais de familiarité, protégé par `V31-ACT01-3`.** Se rabattre sur un gabarit connu (`Atelier`, `Quiz`) par habitude, alors qu'un gabarit plus récent répond plus précisément au besoin, produit le même défaut que le biais de nouveauté — l'enrichissement du catalogue ne change alors rien en pratique. Exemple : un besoin de connaître l'état du moment de chaque apprenant (disponibilité, énergie, ressenti) doit faire reconnaître `Planche météo`, pas un tour de table improvisé en `Atelier` ni un diagnostic de connaissances en `Quiz`. « Le plus proche » ou « le plus pertinent » se détermine sur la finalité déclarée, dans **tout** le catalogue — pas par défaut vers ce qui est déjà familier.

---

## ACT02 — Choisir une activité pour sa pertinence pédagogique

Le raisonnement part de la situation et de l'objectif réels, pas du catalogue :

```text
situation + objectif
→ une activité du catalogue correspond-elle ?
→ oui : la choisir, en la départageant des autres candidates plausibles
→ non : dériver une activité du gabarit existant qui s'en rapproche le plus, plutôt que reconstruire depuis zéro
```

Lorsqu'il existe plusieurs activités plausibles, l'agent doit les départager en fonction du besoin réel et exploiter les métadonnées de sélection disponibles dans leur front matter.

Le choix doit notamment rester cohérent avec :

- l'objectif ;
- la granularité attendue ;
- le contexte ;
- l'étape pédagogique ;
- les caractéristiques déclarées des activités candidates.

Les métadonnées constituent des **indices de sélection**, pas des conditions exclusives ni une table de décision mécanique — protégé par `V31-ACT02-4` : un vocabulaire de surface qui recoupe les `selection_keywords` d'un gabarit ne doit pas l'emporter sur la fonction réellement décrite.

Si aucun type existant ne correspond exactement, l'agent adapte le gabarit existant le plus proche plutôt que de repartir d'une page blanche — c'est ce que les runs exploratoires ont déjà montré (`Atelier` adapté pour une analyse de dossier ou pour un jeu de rôle, `Brique` adapté pour une observation ciblée). Une construction entièrement nouvelle depuis le seul socle `Activité`, sans prendre appui sur aucun gabarit existant, reste possible mais n'est pas le premier réflexe attendu.

« Le plus proche » se détermine sur la finalité déclarée, dans tout le catalogue — pas par défaut vers un gabarit générique déjà familier. Le risque symétrique, quand une correspondance exacte existe plutôt qu'un simple repli, relève d'ACT01 (biais de familiarité, ci-dessus) : les deux s'appuient sur la même exigence, comparer sur toute la surface du catalogue.

### Observable attendu

Lorsque plusieurs activités sont plausibles, une différence pédagogique pertinente entre deux situations peut conduire à un choix différent, et ce choix reste justifiable par l'objectif, le contexte et les caractéristiques déclarées des activités candidates.

---

# Ce que V3.1.0 ne promet pas

V3.1.0 ne promet pas :

- de dérouler toutes les activités du catalogue ;
- d'imposer une activité existante lorsqu'aucune ne convient ;
- de rendre toute activité simple ou facile ;
- de remplacer le jugement pédagogique d'un formateur ;
- de modifier les acquis validés de la V2.1 sans justification et validation explicites ;
- de mobiliser des leviers cognitifs ou d'adapter le tutorat : ces comportements relèvent des mineures V3.2.0 et V3.3.0, non encore engagées.

---

# Critère comportemental central de V3.1.0

Le critère central de la V2.1 reste valide :

> **Une information pédagogique pertinente différente doit pouvoir conduire l'agent à une décision différente lorsque cette information devrait effectivement modifier l'apprentissage ou l'évaluation.**

V3.1.0 étend ce critère au choix d'activité :

> **L'agent doit également pouvoir identifier et choisir une activité plus pertinente en fonction de l'objectif, du contexte et du besoin pédagogique effectif, plutôt que dérouler une réponse ou un format plausible mais générique.**

Le comportement recherché devient notamment :

```text
Demande / objectif
   ↓
Contexte et informations pédagogiques pertinentes
(dont l'état V2.1 disponible)
   ↓
Besoin pédagogique actuel
   ↓
Activités candidates
   ↓
Choix d'une activité pertinente
   ↓
Activité
```

et non :

```text
Demande
   ↓
Choix automatique d'un format
   ↓
Application mécanique d'une recette
```

---

# Statut de cette promesse

Cette promesse est **gelée pour V3.1.0**, le 2026-09-03, à l'issue du cycle complet prévu par `base_de_travail.md` §15 :

> ⚠️ **Réserve tranchée le 2026-09-04 — le gel est maintenu.** Une vérification sur le candidat réel, postérieure à ce gel, avait trouvé `V31-ACT02-3` instable (4 réponses en 4 runs). Le diagnostic a établi que ces runs portaient sur une fixture non conforme au prérequis bloquant n°3 de la batterie (catalogue hétérogène : 3 gabarits génériques privés de leur discriminant de sélection) ; ils sont requalifiés **non concluants** et ne constituent pas une charge contre ACT02. Voir `docs/v3.1/RAPPORT_INSTABILITE_V31-ACT02-3_2026-09-03.md` §9.
>
> **Réparé et vérifié le 2026-09-04** : le discriminant de sélection manquant a été porté dans `atelier.md`, `quiz.md` et `recul.md` (catalogue homogène, 14/14), puis la **batterie entière rejouée sur le candidat corrigé — 15/15 PASS**, résultats identiques type par type à la validation d'origine. La réserve est levée : ACT01 et ACT02 tiennent sur le candidat versionné, pas seulement sur une copie de test.
>
> **Ce qui reste dû** : la non-régression de la baseline V2.1 (`../validation/v2.1/non_regression/`) n'a pas été jouée sur ce candidat, alors que le portage a touché trois gabarits du socle hérité. Exigence distincte, posée au §0 ci-dessus et par `base_de_travail.md` §13 — V3.1.0 n'est donc pas encore validée au sens du gel de non-régression.
>
> **Catalogue étendu le 2026-09-04, gel maintenu.** Trois gabarits d'ouverture (`interview_croisee.md`, `objet_express.md`, `barometre_humain.md` — Interview croisée, Objet express, Baromètre humain) ajoutés au chantier 1 et référencés dans `activite.md` (catalogue à 17 entrées). Décision du même ordre que l'extension `V31-ACT02-5` : contrôle mécanique de conformité seul jugé suffisant (`scripts/controle_conformite_gabarits.sh`, 17/17), sans rejouer la batterie NOY comportementale. Raison : ces trois gabarits ne recoupent la finalité d'aucun des 14 existants (mise en relation de début de formation, non évaluée), donc n'introduisent aucun distracteur nouveau pour les 8 scénarios ACT01/ACT02 déjà établis. Ce raisonnement porte spécifiquement sur ces trois gabarits ; un futur ajout dont la finalité recoupe un gabarit existant devrait être rejugé au cas par cas, pas couvert automatiquement par ce précédent.
>
> **`V31-ACT02-5` diagnostiqué et réparé le 2026-09-04.** Son résultat 2/3 n'était pas une erreur de raisonnement mais une asymétrie d'artefact — même classe de défaut que `V31-ACT02-3` (ci-dessus) : `planche_meteo.md` ne mentionnait `En un mot` nulle part, alors que la réciproque existait. Un contrôle mécanique `CG5` (réciprocité des sections `## Distinction avec X`) a été ajouté à `scripts/controle_conformite_gabarits.sh` et a révélé 7 paires asymétriques sur les 17 gabarits, toutes corrigées. `V31-ACT02-5` rejoué : **3/3 PASS, `En un mot` unanime** — les 8 scénarios de la batterie sont désormais tous unanimes. Détail dans `validation/v3.1/non_regression/V31-ACT02-5.md`.
>
> ⚠️ **Incident méthodologique le 2026-09-04 — fiabilité de toutes les exécutions de sous-agents remise en cause.** Toutes les exécutions de scénarios NOY de cette session (les 8 de cette batterie V3.1, et une tentative séparée de non-régression V2.1 à 14 scénarios) ont été jouées par des sous-agents dispatchés via l'outil `Agent`, **pas** via les harnais officiels du dépôt (`scripts/run_baseline.sh`/`run_isole.sh` sous `david`, ou `validation/collector-kit/` sous `claude-test`). Un `FAIL` obtenu ainsi sur `NOY004` (batterie V2.1) s'est révélé faux dès rejeu avec le vrai harnais — `PASS` confirmé sur V2.1 publiée et sur V3.1.0. Détail : `docs/v3.1/RAPPORT_INCIDENT_METHODOLOGIE_VALIDATION_2026-09-04.md`.
>
> **Conséquence pour cette promesse** : le 15/15 et les diagnostics `ACT02-3`/`ACT02-5` ci-dessus doivent être considérés comme **non confirmés par le harnais officiel** tant qu'ils n'ont pas été rejoués avec l'outillage documenté. Rien n'a été promu sur cette base ; le gel du texte de la promesse reste inchangé, mais la validation comportementale qui le sous-tend est à refaire proprement avant de considérer V3.1.0 réellement établie.

1. ~~chaque propriété nouvelle (ACT01, ACT02) examinée pour vérifier qu'elle exprime bien un comportement utile et non un simple moyen d'implémentation~~ — fait, deux passes de revue (interne puis externe, vérifiées point par point) ;
2. ~~doublons supprimés~~ — fait ;
3. ~~sept scénarios courts et discriminants dérivés de la promesse, dans `validation/v3.1/non_regression/`~~ — faits ;
4. ~~les quatre scénarios qui portent la charge de preuve de la fiabilité (`V31-ACT01-2`, `V31-ACT01-3`, `V31-ACT02-3`, `V31-ACT02-4`) rejoués trois fois chacun~~ — fait, sur une copie isolée du catalogue réel (fixture, candidat versionné non modifié) : **15 exécutions au total, 15/15 PASS**, unanimité (3/3) sur les quatre scénarios répétés. Aucune propriété n'a nécessité d'ajustement. Détail dans `validation/v3.1/non_regression/CLAUDE.md` et `docs/historique_3.md`. Test A / B′ resté sans objet, conformément à la décision documentée en tête de `validation/v3.1/non_regression/README.md` ;
5. ~~la promesse ajustée si nécessaire puis gelée~~ — aucun ajustement nécessaire ; gelée telle quelle.

La validation de V3.1.0 rejouera, en une seule passe pour la détection de régression (`base_de_travail.md` §13) :

- les 15 scénarios de la baseline V2.1 ;
- les 8 scénarios V3.1.0 ci-dessus (`V31-ACT02-5` ajouté le 2026-09-04), désormais établis comme fiables.

Reste non couvert avant l'implémentation réelle du catalogue (candidat versionné, pas la copie de test) : les prérequis bloquants documentés dans `validation/v3.1/non_regression/README.md` (référencement dans `activite.md`, évolution de `SKILL.md` sur les métadonnées de sélection) doivent encore être appliqués au candidat lui-même — la validation ci-dessus porte sur une copie isolée, conformément à la voie (a) documentée.

Une fois V3.1.0 validée et promue, `promesse.md` sera étendu en V3.2.0 (chantier 2 — leviers cognitifs et biais).
