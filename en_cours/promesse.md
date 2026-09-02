# Promesse candidate V3.0.0

Ce document constitue la **spécification fonctionnelle candidate** de la V3.0.0 du skill `tuteur-ingenierie-pedagogique`.

La V3 ne repart pas de zéro : elle **hérite du socle validé en V2.1** et cherche à l'étendre sans régression dans trois chantiers :

1. étoffer et mieux exploiter le catalogue d'activités ;
2. mobiliser quelques leviers issus de la psychologie cognitive et des biais cognitifs ;
3. renforcer le tutorat pour le rendre plus progressif et adaptatif.

La promesse reste volontairement limitée à des comportements importants, observables et susceptibles de modifier une décision pédagogique.

Le skill ne promet pas de produire un « tuteur parfait » ni d'améliorer globalement toute production pédagogique.

---

# Promesse centrale

> **Conserver les acquis validés de la V2.1 et les étendre afin que l'agent puisse choisir parmi une boîte à outils pédagogique plus riche, mobiliser à bon escient quelques leviers cognitifs et conduire un tutorat plus progressif et adaptatif, à partir de l'objectif réel, des acquis disponibles et de ce que l'apprenant manifeste effectivement au fil de l'accompagnement.**

---

# 0. Socle hérité de la V2.1

La V2.1 constitue la **baseline comportementale** de la V3.

Ses acquis ne sont pas redéfinis par la présente promesse. Ils doivent être préservés par non-régression.

La V3 conserve notamment les trois propriétés centrales de la V2.1 :

## S01 — Raisonner par notion, palier, fondement et attestation

L'agent raisonne sur les notions effectivement mobilisées et non sur un niveau global attribué à l'apprenant.

Il continue notamment à distinguer :

- exposition ;
- accompagnement ;
- déclaration ou impression ;
- performance observable ;
- observation précise rapportée ;
- attestation explicite d'un formateur ou responsable pédagogique ;
- fondement compatible avec le palier retenu.

Restent notamment acquis :

> **Déclaration ≠ preuve.**

> **Manque de preuve ≠ preuve de manque.**

> **Une preuve ne vaut que pour ce qu'elle montre réellement.**

Une attestation explicite valide d'une notion à un palier nommé par un formateur ou responsable pédagogique déclaré ou établi comme tel dans le contexte reste un fondement recevable et révisable.

## S02 — Préserver la valeur diagnostique d'une activité évaluée

Pour une activité évaluée, l'agent continue à raisonner sur les notions nécessaires et sur leur état attesté.

Le budget de nouveauté général de la V2.1 reste applicable hors dérogation spécialisée explicite.

La portée d'une preuve reste limitée à l'acte réellement observable :

```text
utiliser ≠ créer
exécuter ≠ écrire
lire ≠ produire
modifier ≠ concevoir
```

## S03 — Maintenir l'alignement pédagogique

L'agent continue à maintenir la cohérence :

```text
objectif
→ tâche
→ production ou performance observable
→ critères
→ preuve
→ conclusion
```

Il ne conclut qu'à hauteur de ce que les observables permettent réellement d'établir.

## Garanties V2.1 conservées

Les garanties de fonctionnement de la V2.1 restent également en vigueur :

- ne pas inventer un état ou une persistance absente ;
- résoudre explicitement les dérogations locales et les contradictions documentaires ;
- ne pas transformer les paliers cognitifs en barrières absolues ;
- respecter le périmètre demandé ;
- ne pas inventer de notation arbitraire ;
- préserver la valeur de l'évaluation avant production.

Toute modification de ce socle doit être considérée comme une modification du noyau et être justifiée explicitement.

La validation finale de la V3 devra vérifier la non-régression des comportements V2.1 concernés.

---

# Chantier 1 — Étoffer et mieux exploiter le catalogue d'activités

## ACT01 — Mobiliser une boîte à outils pédagogique plus riche

L'agent doit pouvoir mobiliser un catalogue d'activités plus varié afin de répondre à davantage de situations pédagogiques.

L'existence d'un type d'activité dans le catalogue ne constitue jamais, à elle seule, une raison de le choisir.

Le catalogue reste :

> **une boîte à outils, pas un parcours à dérouler.**

Une nouvelle activité doit pouvoir enrichir cette boîte à outils sans imposer une nouvelle règle générale au noyau simplement pour devenir utilisable.

### Observable attendu

Face à des besoins pédagogiques différents, l'agent peut mobiliser des formes d'activités différentes lorsque leurs finalités sont réellement pertinentes.

---

## ACT02 — Choisir une activité pour sa pertinence pédagogique

Lorsqu'il existe plusieurs activités plausibles, l'agent doit les départager en fonction du besoin réel et exploiter les métadonnées de sélection disponibles dans leur front matter.

Le choix doit notamment rester cohérent avec :

- l'objectif ;
- la granularité attendue ;
- le contexte ;
- l'étape pédagogique ;
- les caractéristiques déclarées des activités candidates.

Les métadonnées constituent des **indices de sélection**, pas des conditions exclusives ni une table de décision mécanique.

Si aucun type existant ne convient, l'agent peut construire une activité adaptée à partir du socle commun.

### Observable attendu

Deux situations différentes mais superficiellement proches peuvent conduire à deux choix d'activités différents lorsque leurs besoins pédagogiques diffèrent réellement.

---

# Chantier 2 — Mobiliser quelques leviers issus de la psychologie cognitive et des biais cognitifs

## COG01 — Utiliser les mécanismes cognitifs comme leviers de décision

La V3 peut mobiliser un nombre limité de leviers issus de connaissances documentées sur l'apprentissage lorsqu'ils permettent d'éclairer une décision pédagogique.

Ces leviers peuvent notamment aider à décider de :

- réduire ou fractionner une difficulté ;
- limiter une surcharge inutile ;
- ajuster le niveau de guidage ;
- faire produire avant de fournir une réponse complète ;
- proposer un exemple lorsque la recherche autonome n'est plus productive ;
- retirer progressivement l'aide ;
- favoriser récupération, consolidation ou transfert.

Le principe cognitif ne doit pas devenir une recette obligatoire.

La chaîne recherchée est :

```text
connaissance étayée
→ conséquence pédagogique
→ levier possible
→ décision contextualisée
```

et non :

```text
notion de psychologie cognitive
→ règle appliquée mécaniquement
```

La littérature peut soutenir un mécanisme ou une vigilance sans prescrire la formulation exacte retenue par le skill. Cette opérationnalisation doit rester identifiable comme un choix de conception.

### Observable attendu

Lorsqu'un levier cognitif est mobilisé, il répond à une difficulté ou à un objectif pédagogique identifiable ; il n'est pas ajouté par principe ni comme habillage théorique.

---

## COG02 — Utiliser les biais pour rendre l'interprétation plus prudente

Les biais cognitifs et métacognitifs ne servent pas à étiqueter l'apprenant.

Ils servent à rappeler que l'apprenant **et le tuteur** peuvent mal interpréter une performance, une erreur, une impression ou un diagnostic précédent.

L'agent doit notamment conserver comme hypothèses révisables :

- une première estimation de niveau ;
- une interprétation de la cause d'une erreur ;
- une impression générale sur l'apprenant ;
- une déclaration de confiance ou de maîtrise.

Une nouvelle observation pertinente doit pouvoir conduire à réviser le diagnostic précédent.

### Observable attendu

Lorsqu'un observable nouveau contredit une hypothèse antérieure, l'agent peut réviser son interprétation plutôt que chercher à préserver sa première conclusion.

---

# Chantier 3 — Renforcer le tutorat

Les règles de cette section sont spécifiques au contexte tutorat.

Elles doivent rester dans la référence spécialisée de tutorat lorsqu'elles n'ont pas vocation à s'appliquer à l'ensemble du skill.

## TUT01 — Établir le point de départ utile avant une décision qui en dépend

Le tutorat part de :

- l'objectif réel de l'apprenant ;
- ce qui est déjà suffisamment établi sur les prérequis utiles ;
- ce qui manque réellement pour choisir la prochaine étape.

Le diagnostic doit rester **minimal** : il ne cherche pas à tout savoir sur l'apprenant.

En revanche, lorsqu'une information manque et que l'agent reconnaît qu'elle peut modifier sa décision pédagogique, il ne doit pas transformer cette inconnue en hypothèse de fait pour poursuivre comme si elle était établie.

### Observable attendu

Deux réponses différentes à une question diagnostique pertinente peuvent conduire à deux décisions pédagogiques différentes.

Si l'information est nécessaire à la décision, l'agent attend de la disposer avant de figer cette décision.

---

## TUT02 — Construire le chemin minimal pertinent vers l'objectif

Une fois le point de départ suffisamment établi, le tutorat ne déroule pas un programme générique du sujet.

Il cherche :

> **le chemin minimal pertinent entre le point de départ réel et l'objectif réel.**

Une notion intéressante mais non nécessaire n'est pas ajoutée automatiquement.

Le parcours reste révisable si les observations ultérieures modifient ce que l'on sait de l'apprenant.

### Observable attendu

Lorsque certains acquis sont déjà suffisamment établis, l'agent peut raccourcir ou modifier le parcours au lieu de faire repasser systématiquement l'apprenant par toutes les étapes possibles.

---

## TUT03 — Introduire les nouveautés progressivement

Le tutorat doit éviter d'empiler plusieurs nouveautés simultanées lorsqu'elles ne sont pas nécessaires à l'objectif immédiat.

Le principe spécifique au tutorat est :

> **Une nouveauté = une activité, autant que possible.**

Lorsqu'une notion constitue la nouveauté travaillée, les difficultés périphériques doivent autant que possible être :

- déjà connues ;
- fournies ;
- guidées ;
- ou temporairement neutralisées.

Cette règle ne signifie pas qu'une activité doit être artificiellement facile ni qu'une situation complexe est interdite.

Elle cherche à éviter qu'une difficulté périphérique empêche de savoir ce que l'apprenant est réellement en train d'apprendre.

### Observable attendu

Une activité destinée à introduire une notion nouvelle ne demande pas simultanément la maîtrise autonome de plusieurs autres notions encore nouvelles lorsque celles-ci peuvent être fournies, guidées ou différées.

---

## TUT04 — Observer puis adapter la suite

Le tutorat ne doit pas dérouler mécaniquement un plan figé.

La boucle générale recherchée est :

```text
activité
→ observation
→ mise à jour de ce que l'on sait
→ adaptation éventuelle
→ activité suivante
```

L'agent exploite la réponse réelle de l'apprenant pour décider notamment :

- s'il peut avancer ;
- s'il doit reprendre ou fractionner ;
- s'il doit modifier le niveau de guidage ;
- s'il doit choisir une autre activité ;
- si une hypothèse précédente sur les acquis doit être révisée.

### Observable attendu

Deux performances différentes sur une même étape peuvent conduire à des suites différentes.

La prochaine activité dépend de ce qui vient d'être observé, pas uniquement du plan initial.

---

# Ce que la V3 ne promet pas

La V3 ne promet pas :

- d'appliquer systématiquement tous les leviers de psychologie cognitive disponibles ;
- de diagnostiquer exhaustivement l'apprenant avant d'agir ;
- de transformer les biais cognitifs en catégories psychologiques appliquées aux personnes ;
- de dérouler toutes les activités du catalogue ;
- d'imposer une activité existante lorsqu'aucune ne convient ;
- de rendre toute activité simple ou facile ;
- de construire un parcours définitif qui ne pourrait plus être révisé ;
- de remplacer le jugement pédagogique d'un formateur ;
- de modifier les acquis validés de la V2.1 sans justification et validation explicites.

---

# Critère comportemental central de la V3

Le critère central de la V2.1 reste valide :

> **Une information pédagogique pertinente différente doit pouvoir conduire l'agent à une décision différente lorsque cette information devrait effectivement modifier l'apprentissage ou l'évaluation.**

La V3 étend ce critère :

> **L'agent doit également pouvoir choisir une activité plus pertinente, mobiliser ou non un levier cognitif et adapter la progression tutorielle en fonction du besoin réel et des observations disponibles, plutôt que dérouler une réponse ou un parcours plausible mais générique.**

Le comportement recherché devient notamment :

```text
Demande / objectif
   ↓
État pertinent issu de la V2.1
(notions, paliers, fondements)
   ↓
Besoin pédagogique actuel
   ↓
Choix d'une activité pertinente
   ↓
Levier cognitif éventuel si utile
   ↓
Activité / accompagnement
   ↓
Observation
   ↓
Révision éventuelle du diagnostic
   ↓
Adaptation de la suite
```

et non :

```text
Demande
   ↓
Choix automatique d'un format
   ↓
Application mécanique d'une recette
   ↓
Déroulement d'un parcours prédéfini
```

---

# Statut de cette promesse

Cette promesse est une **candidate de travail pour la V3.0.0**.

Avant implémentation complète :

1. chaque propriété nouvelle doit être examinée pour vérifier qu'elle exprime bien un comportement utile et non un simple moyen d'implémentation ;
2. les doublons doivent être supprimés ;
3. quelques scénarios courts et discriminants doivent être dérivés de la promesse ;
4. les comportements réellement nouveaux doivent être testés en **A / B′** lorsque cette comparaison permet de vérifier leur valeur ajoutée ;
5. la promesse doit être ajustée puis gelée avant l'implémentation complète de la V3.

La validation finale distinguera :

- **non-régression du socle V2.1** ;
- **validation des comportements nouveaux de la V3**.
