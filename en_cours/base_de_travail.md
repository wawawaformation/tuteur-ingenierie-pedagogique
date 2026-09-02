# Base de travail — passage de la V2.1 à la V3

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-09-02  
**Statut :** base de travail V3 — V2.1 stabilisée et validée

---

# 1. État de départ

La **V2.1** constitue désormais le socle stable du projet.

Son noyau a été :

- corrigé et allégé ;
- documenté ;
- soumis aux tests de non-régression ;
- validé, y compris sur le mécanisme de dérogation locale ;
- promu comme version publique stable.

La V3 ne repart donc ni de la V2 ni de l'ancienne V3 expérimentale.

Elle part de :

```text
V2.1 stable et validée
        ↓
V3 = extension du socle
```

La V3 expérimentale reste une **source d'enseignements** :

- bonnes idées ;
- comportements utiles ;
- formulations doctrinales intéressantes ;
- erreurs d'architecture et de sédimentation à ne pas reproduire.

Elle n'est pas une base de code à nettoyer ou à restaurer.

---

# 2. Principe principal

> **Doctrine avant procédure.**

Avant d'ajouter une règle, un gate, une séquence ou un contrôle, on doit savoir :

1. quel principe pédagogique on veut défendre ;
2. pourquoi ce principe est important ;
3. quel comportement permet de voir s'il est respecté ;
4. seulement ensuite, quelle procédure minimale peut aider le modèle à l'appliquer.

On évite :

```text
un comportement nous gêne
→ ajout d'un gate
→ ajout d'une exception
→ duplication de la règle
→ justification après coup
```

Le but reste :

> **moins de texte, plus de structure, des comportements observables et testables.**

---

# 3. Ce que la V3 hérite de la V2.1

La V3 doit préserver les acquis validés de la V2.1.

Elle ne redéfinit pas sans nécessité :

- la distinction entre déclaration, preuve et attestation ;
- le principe « manque de preuve ≠ preuve de manque » ;
- la portée limitée d'une preuve à ce qu'elle montre réellement ;
- le suivi notion → palier → fondement ;
- l'attestation explicite du formateur ;
- les paliers cognitifs et leurs usages ;
- l'alignement objectif → tâche → production/performance → critères → preuve → conclusion ;
- la granularité pédagogique ;
- le socle Activité et ses spécialisations ;
- l'absence de notation arbitraire ;
- le mécanisme de dérogation locale explicite ;
- les règles de routage et de priorité documentaires.

La V2.1 devient la **baseline de non-régression** de la V3.

Une modification du noyau V2.1 ne doit intervenir que si un besoin V3 réel la rend nécessaire et si cette modification est explicitement justifiée.

---

# 4. Les trois chantiers de la V3

La V3 est organisée autour de trois chantiers distincts mais complémentaires.

```text
                    V3
                     │
        ┌────────────┼────────────┐
        │            │            │
   Activités      Leviers       Tutorat
   pédagogiques   cognitifs
        │            │            │
        └────────────┼────────────┘
                     │
             décision pédagogique
```

Les trois chantiers ne sont pas trois silos.

- Le tutorat peut mobiliser une activité du catalogue.
- Une activité peut mettre en œuvre un ou plusieurs leviers cognitifs.
- Un levier cognitif peut influencer le choix ou l'adaptation d'une activité.
- Le catalogue et les leviers restent au service de la décision pédagogique.

---

# 5. Chantier 1 — Étoffer le catalogue des activités

## 5.1 Objectif

Enrichir `references/activites_type/` afin de donner à l'agent une boîte à outils pédagogique plus variée.

Le catalogue doit permettre de répondre à davantage de besoins sans transformer le noyau en table de décision.

> **`activites_type/` est une boîte à outils, pas un parcours à dérouler.**

---

## 5.2 Principes à conserver

Une activité est choisie en fonction :

- de l'objectif ;
- du contexte ;
- de la granularité ;
- de l'étape pédagogique ;
- de ses caractéristiques propres ;
- des informations pertinentes disponibles dans ses métadonnées.

L'existence d'une activité dans le catalogue ne suffit jamais à imposer son usage.

Si aucun type existant ne convient, l'agent peut construire une activité adaptée à partir du socle commun.

---

## 5.3 Métadonnées

Les activités V3 disposent de métadonnées plus riches que les seuls champs historiquement cités dans `SKILL.md` (`purpose`, `typical_uses`).

Le noyau ne doit pas recopier la liste de toutes les métadonnées.

La direction retenue est plutôt :

> **le noyau explique comment chercher et départager ; les métadonnées fournissent les informations permettant de départager.**

Une micro-évolution du `SKILL.md` pourra donc être envisagée pour parler plus généralement des **métadonnées de sélection disponibles dans le front matter**, sans créer de table de décision ni coupler le noyau au schéma exact des activités.

Cette évolution doit rester légère.

---

## 5.4 Extensibilité attendue

Ajouter une nouvelle activité doit pouvoir se faire principalement par :

```text
nouveau gabarit
+ métadonnées adaptées
+ référencement/découvrabilité
```

sans devoir ajouter une nouvelle règle générale au noyau uniquement pour rendre cette activité utilisable.

---

# 6. Chantier 2 — Ajouter quelques leviers issus de la psychologie cognitive et des biais cognitifs

## 6.1 Intention

Le chantier ne consiste pas à ajouter un glossaire de psychologie cognitive au runtime.

La logique recherchée est :

```text
connaissance étayée
→ conséquence pédagogique
→ levier possible
→ décision contextualisée
```

Le phénomène ou le biais sert à **justifier et éclairer un levier**, pas à enrichir artificiellement le vocabulaire du skill.

---

## 6.2 Sélection volontairement limitée

On ne cherche pas à intégrer toutes les notions disponibles dans le document de fond.

On sélectionne seulement quelques leviers :

- suffisamment documentés ;
- utiles à une décision pédagogique réelle ;
- observables dans le comportement de l'agent ;
- non redondants avec une règle V2.1 déjà suffisante.

Mieux vaut quelques leviers robustes et réellement utilisés qu'un catalogue théorique exhaustif.

---

## 6.3 Mécanismes cognitifs

Les leviers retenus pourront notamment aider à décider de :

- réduire ou fractionner une difficulté ;
- éviter une surcharge inutile ;
- ajuster le niveau de guidage ;
- faire produire avant de donner une réponse complète ;
- montrer un exemple lorsque la recherche autonome n'est plus productive ;
- retirer progressivement l'aide ;
- favoriser récupération, consolidation ou transfert.

Aucun de ces mécanismes ne doit devenir une recette universelle.

---

## 6.4 Biais cognitifs et métacognitifs

Les biais ne servent pas à étiqueter psychologiquement l'apprenant.

Ils doivent surtout rendre l'interprétation plus prudente.

Ils peuvent rappeler notamment que :

- une première impression ne doit pas figer le diagnostic ;
- une hypothèse doit pouvoir être contredite ;
- une impression générale ne remplace pas une preuve spécifique ;
- une erreur n'indique pas automatiquement sa cause ;
- une déclaration de confiance ne constitue pas une preuve de maîtrise ;
- le tuteur lui-même est exposé aux biais.

La formulation recherchée porte donc sur les **observables et les décisions**, pas sur des étiquettes appliquées aux personnes.

---

## 6.5 Provenance des leviers

La V3 doit continuer à distinguer :

```text
établi
observé
choisi
```

Une source scientifique peut étayer un mécanisme sans prescrire la règle exacte du skill.

Il faut conserver la distinction :

```text
résultat ou cadre documenté
≠
levier dérivé
≠
choix d'implémentation du produit
```

Le document `dossier-pedagogique/psychologie_cognitive_formation_tutorat.md` reste à ce stade un matériau de fond hors runtime.

---

# 7. Chantier 3 — Renforcer le tutorat

Le fichier spécialisé `references/tutorat.md` existe déjà.

Le chantier tutorat doit donc principalement travailler **dans cette extension spécialisée**, et non rouvrir le noyau V2.1.

Le mécanisme de portée et de dérogation nécessaire à ce travail existe désormais dans le socle et a été validé.

---

## 7.1 Partir de l'apprenant

Le tutorat part :

- de l'objectif réel de l'apprenant ;
- de ce qui est suffisamment établi sur les prérequis utiles ;
- du chemin le plus court et le plus pertinent vers l'objectif.

On ne déroule pas un programme générique si ce n'est pas nécessaire.

---

## 7.2 Diagnostic minimal

On ne cherche pas à tout savoir sur l'apprenant.

On cherche les informations qui peuvent réellement changer la décision pédagogique.

Quand on en sait assez pour choisir la prochaine étape, on arrête le diagnostic.

Si une information manque et que le tuteur reconnaît qu'elle peut modifier sa décision, il ne transforme pas cette inconnue en hypothèse de fait.

---

## 7.3 Pas de plan détaillé fondé sur une inconnue

Le tuteur peut expliquer, cadrer ou présenter ce qui est déjà certain.

En revanche, il ne fige pas une décision ou un parcours détaillé qui dépend explicitement d'une information qu'il n'a pas encore.

Le problème n'est donc pas de « parler avant la réponse ».

Le problème est :

> **prendre une décision dépendante d'une information reconnue comme manquante.**

---

## 7.4 Chemin minimal

Le repère de progression n'est pas un catalogue du sujet.

Il cherche :

> **le chemin minimal pertinent entre le point de départ réel et l'objectif réel.**

Une notion intéressante mais non nécessaire n'est pas ajoutée automatiquement.

---

## 7.5 Une nouveauté = une activité

Le tutorat doit être très progressif.

> **Une nouveauté = une activité, autant que possible.**

Lorsqu'une notion est nouvelle, on évite de demander simultanément la maîtrise autonome de plusieurs autres nouveautés.

Les difficultés périphériques doivent autant que possible être :

- déjà connues ;
- fournies ;
- guidées ;
- ou temporairement neutralisées.

Cette règle de tutorat reste distincte du budget de nouveauté A3 du noyau V2.1.

---

## 7.6 Les exemples doivent être expliqués

Un exemple ne doit pas être simplement posé devant l'apprenant.

Le tuteur précise, lorsque cela est utile :

- ce qu'il faut regarder ;
- ce que l'exemple illustre ;
- pourquoi il est présenté à ce moment-là.

---

## 7.7 La théorie doit servir quelque chose

On n'ajoute pas de théorie uniquement parce qu'elle est intéressante.

Elle doit servir une fonction pédagogique identifiable, par exemple :

- comprendre ;
- éviter une erreur ;
- transférer ;
- devenir plus autonome.

---

## 7.8 Observer puis adapter

Le plan tutoriel reste révisable.

La boucle générale est :

```text
activité
→ observation
→ mise à jour de ce que l'on sait
→ adaptation éventuelle
→ activité suivante
```

La prochaine étape doit pouvoir changer selon ce que l'apprenant manifeste réellement.

---

## 7.9 Utiliser naturellement les activités disponibles

Le tuteur dispose de `activites_type/`.

Lorsqu'une activité existante sert réellement l'objectif et l'étape en cours, il peut et doit l'utiliser naturellement.

Il ne réinvente pas systématiquement une activité si un gabarit existant convient.

Inversement, il ne choisit pas un gabarit simplement parce qu'il existe.

---

# 8. Promesse V3

La promesse V3 est désormais travaillée dans un document dédié :

```text
promesse.md
```

Elle doit :

1. rappeler explicitement que la V2.1 constitue le socle validé ;
2. distinguer les trois chantiers de la V3 ;
3. exprimer des **comportements utiles et observables** ;
4. éviter de transformer chaque moyen d'implémentation en promesse ;
5. rester suffisamment courte pour permettre la construction de scénarios discriminants.

La promesse candidate actuelle distingue :

```text
Socle V2.1
│
├── Chantier 1 : activités
├── Chantier 2 : leviers cognitifs et biais
└── Chantier 3 : tutorat
```

Elle n'est pas encore considérée comme gelée.

Avant gel, chaque propriété doit être soumise à la question :

> **Si cette propriété disparaît, la V3 perd-elle réellement quelque chose d'essentiel ?**

---

# 9. Tester la promesse avant l'implémentation complète

Une fois la promesse candidate suffisamment réduite et claire, créer seulement **quelques scénarios courts et discriminants**.

Les scénarios doivent être :

- directement reliés à une propriété de promesse ;
- observables ;
- faciles à scorer ;
- suffisamment courts pour limiter les facteurs parasites.

Les comportements réellement nouveaux pourront être testés en :

> **A / B′**

lorsque cette comparaison permet de vérifier leur valeur ajoutée.

Le but est de vérifier avant l'investissement d'implémentation que les comportements :

1. sont réellement utiles ;
2. sont observables ;
3. ne sont pas déjà produits naturellement de façon suffisamment fiable sans skill ;
4. justifient donc l'évolution.

Une propriété non discriminante ou sans valeur ajoutée démontrable peut être retirée de la promesse.

---

# 10. Implémenter ensuite par petits morceaux

Une fois la promesse suffisamment stabilisée :

```text
petit comportement
→ petite implémentation
→ run ciblé
→ observation
→ diagnostic
→ correction éventuelle
→ comportement suivant
```

On évite de modifier simultanément :

- le noyau ;
- le tutorat ;
- plusieurs activités ;
- les leviers cognitifs ;
- les scénarios ;
- les oracles.

L'objectif est de conserver la capacité à expliquer la cause d'un changement de comportement.

---

# 11. Méthode pour analyser un comportement douteux

On conserve la méthode qui a bien fonctionné pendant les campagnes précédentes :

> **petit stimulus → résultat observable → méta-discussion → diagnostic → éventuelle modification**

Quand un résultat paraît mauvais, on cherche notamment à déterminer :

- quelle règle l'agent a appliquée ;
- quel observable il a réellement utilisé ;
- quelle information il estimait disponible ;
- à quel moment il a pris sa décision.

Un problème peut venir de :

- règle absente ;
- règle ambiguë ;
- contradiction entre règles ;
- mauvais routage ;
- règle connue mais non appliquée ;
- mauvaise classification de l'observable ;
- variance du modèle ;
- mauvais scénario ;
- environnement de test contaminé.

> **Un échec de run ne déclenche pas automatiquement une nouvelle règle.**

---

# 12. Ne pas modifier le test et le skill en même temps

Si un oracle et le skill semblent tous deux problématiques, ne pas les modifier dans le même cycle.

Séquence :

```text
doctrine claire
→ scénario / oracle dérivé
→ oracle gelé
→ run
→ observation
→ diagnostic
→ éventuelle modification du skill
→ nouveau run avec le même oracle
```

Si l'oracle doit être corrigé, la correction est explicite et ouvre un nouveau cycle.

---

# 13. Validation finale de la V3

La validation finale devra distinguer deux objectifs.

## 13.1 Non-régression V2.1

Les comportements hérités du socle V2.1 sont vérifiés en condition A.

Le but est de confirmer que les extensions V3 n'ont pas dégradé les comportements déjà validés.

---

## 13.2 Validation des nouveautés V3

Les propriétés réellement nouvelles disposent de scénarios spécifiques.

Une comparaison A / B′ est utilisée lorsqu'elle apporte une information utile sur la valeur ajoutée du skill.

Le protocole final sera défini lorsque :

- la promesse V3 sera gelée ;
- les comportements auront été implémentés ;
- les petits runs auront permis de stabiliser le candidat.

---

# 14. Architecture et périmètre

## Noyau

La V2.1 reste la référence générale.

On cherche à la modifier le moins possible.

## Activités

Le catalogue peut évoluer de manière indépendante, à condition de respecter le contrat du socle Activité et la découvrabilité attendue.

## Psychologie cognitive et biais

Les connaissances de fond restent documentées hors runtime.

Le runtime ne reçoit que les leviers réellement retenus et opérationnalisés.

## Tutorat

Les règles spécifiques restent dans `references/tutorat.md`.

Les dérogations au noyau restent :

- explicites ;
- limitées à leur périmètre ;
- peu nombreuses ;
- faciles à auditer.

---


# 15. Séquence de travail actuelle

```text
V2.1 stable et validée
│
├─ définir les trois chantiers V3
│  ├─ catalogue d'activités
│  ├─ leviers cognitifs et biais
│  └─ tutorat
│
├─ rédiger la promesse V3 candidate
│
├─ réduire / clarifier les propriétés
│
├─ geler la promesse V3
│
├─ créer quelques SPEC discriminantes
│
├─ tester les nouveautés en A / B′ lorsque pertinent
│
├─ confirmer / retirer / ajuster les propriétés
│
├─ implémenter par petits morceaux
│  ├─ activités
│  ├─ leviers retenus
│  └─ tutorat
│
├─ petits runs ciblés + diagnostic
│
├─ stabiliser le candidat V3
│
├─ non-régression V2.1
│
├─ validation des nouveautés V3
│
└─ promotion V3
```

---

# 16. Règles de conduite à garder sous les yeux

> **Doctrine avant procédure.**

> **La V2.1 est le socle validé ; la V3 l'étend, elle ne la réécrit pas.**

> **Une seule source normative claire par règle.**

> **Une règle spécifique au tutorat reste dans le tutorat.**

> **Le catalogue d'activités est une boîte à outils, pas un parcours imposé.**

> **Les métadonnées aident à choisir ; elles ne constituent pas une table de décision mécanique.**

> **La psychologie cognitive fournit des leviers, pas un glossaire à injecter dans le runtime.**

> **Un cadre établi ne prescrit pas automatiquement la règle exacte du produit.**

> **Les biais servent à rendre l'interprétation prudente, pas à étiqueter les personnes.**

> **Une nouveauté = une activité, autant que possible, en contexte tutorat.**

> **Le tutorat observe puis adapte ; il ne déroule pas mécaniquement un plan.**

> **Un échec de run ne déclenche pas automatiquement une nouvelle règle.**

> **On ne modifie pas l'oracle et le skill dans le même cycle.**

> **On cherche le minimum qui apporte une valeur pédagogique observable, pas le tuteur parfait.**

---

**Cette fiche constitue la base de travail actuelle pour construire et valider la V3 à partir de la V2.1 stable.**
