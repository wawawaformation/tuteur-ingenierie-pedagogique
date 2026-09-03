# Base de travail — passage de la V2.1 à la V3

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-09-03  
**Statut :** base de travail V3 — V2.1 stabilisée et validée, V3 séquencée en mineures 3.1/3.2/3.3

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

## 4.1 Séquencement en versions mineures

Bien que reliés, les trois chantiers ne sont pas menés en parallèle. Chacun devient une version mineure indépendante, gelée et validée avant d'engager la suivante :

```text
V2.1 (socle stable et validé)
   ↓
V3.1.0 — Chantier 1 : catalogue d'activités
   ↓
V3.2.0 — Chantier 2 : leviers cognitifs et biais
   ↓
V3.3.0 — Chantier 3 : tutorat → V3 complète
```

Cet ordre suit une dépendance réelle, pas un choix arbitraire : le tutorat (§7.9) mobilise naturellement le catalogue d'activités et peut s'appuyer sur les leviers cognitifs ; le placer en dernier lui permet de s'appuyer sur les deux chantiers précédents déjà validés.

`V3.3.0` est directement la V3 complète : pas de palier de clôture séparé. D'éventuels correctifs post-promotion restent des patches sur cette dernière mineure (`V3.3.1`, `V3.3.2`, …), jamais un saut vers un `V3.0.0` distinct.

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

## 5.5 Matériau brouillon disponible

`plus_tard/` contient déjà du matériau de travail pour ce chantier :

- `activites_type_origine_retravaillees.zip` — les quatre gabarits actuels (`atelier`, `brique`, `quiz`, `recul`) retravaillés en brouillon ;
- `nouvelles_activites_v3_metadonnees.zip` — onze nouveaux gabarits candidats, une proposition de métadonnées de sélection et des notes de brainstorming.

Ce matériau est une source de travail, pas un contenu à copier tel quel dans `references/activites_type/` : chaque gabarit candidat doit être trié et confronté aux principes de §5.2 avant intégration, sur le même principe que le tri appliqué à la V3 expérimentale (§1).

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

La promesse V3 est travaillée dans un document unique :

```text
promesse.md
```

Le document est **amendé en place à chaque mineure**, pas remplacé : le numéro de version en tête progresse (`V3.1.0` → `V3.2.0` → `V3.3.0`), et seules les propriétés du chantier engagé et des chantiers déjà gelés y figurent — les propriétés d'un chantier non encore engagé n'y sont pas ajoutées par anticipation. L'historique de chaque version gelée reste consultable par git log/tag, comme c'est déjà la convention du dépôt pour `SKILL.md` et les autres références.

Chaque version de la promesse doit :

1. rappeler explicitement que la V2.1 (et les mineures déjà gelées) constituent le socle validé ;
2. porter les propriétés du seul chantier engagé par cette mineure ;
3. exprimer des **comportements utiles et observables** ;
4. éviter de transformer chaque moyen d'implémentation en promesse ;
5. rester suffisamment courte pour permettre la construction de scénarios discriminants.

Séquence des gels :

```text
V3.1.0 — Socle V2.1 + Chantier 1 (activités)
V3.2.0 — V3.1.0 + Chantier 2 (leviers cognitifs et biais)
V3.3.0 — V3.2.0 + Chantier 3 (tutorat) = V3 complète
```

Avant chaque gel, chaque propriété nouvellement ajoutée doit être soumise à la question :

> **Si cette propriété disparaît, la mineure perd-elle réellement quelque chose d'essentiel ?**

---

# 9. Tester la promesse avant l'implémentation complète

Une fois la promesse candidate de la mineure en cours suffisamment réduite et claire, créer seulement **quelques scénarios courts et discriminants**.

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

**Un run unique établit une capacité, pas une fiabilité.** Lorsqu'une propriété de la promesse engage explicitement la fiabilité ou la systématicité d'un comportement — pas seulement sa possibilité — un seul run ne suffit pas à la démontrer : il faut rejouer le même stimulus plusieurs fois et constater un résultat stable. Cette règle est distincte de la passe unique du gel de non-régression (§13.2) : le gel détecte une régression sur une propriété déjà établie comme fiable ; cette étape établit qu'elle l'est, avant qu'elle rejoigne une batterie qui ne sera plus rejouée qu'une fois.

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

# 13. Validation et promotion par mineure

Chaque mineure (3.1, 3.2, 3.3) est gelée et validée indépendamment, avant d'engager la suivante. Il n'y a pas de validation finale unique reportée à la fin des trois chantiers.

## 13.1 Non-régression cumulative

Le gel d'une mineure rejoue :

- les 15 scénarios de la baseline V2.1 (`validation/v2.1/non_regression/`) ;
- les scénarios de chaque mineure déjà gelée (`validation/v3.1/non_regression/`, `validation/v3.2/non_regression/`, …) ;
- les nouveaux scénarios de la mineure en cours (`validation/v3.x/non_regression/` correspondant).

La suite grossit ainsi à chaque promotion et protège tout ce qui a été validé jusque-là. Chaque dossier de mineure reste la source autoritative de ses propres scénarios ; les scénarios des mineures précédentes ne sont pas recopiés dans le dossier de la mineure courante.

---

## 13.2 Une seule passe, reprises ciblées sur FAIL

Contrairement au gel final de V2.1 (deux passes complètes indépendantes, voir `docs/v2.1/RAPPORT_NON_REGRESSION_FINALE_V2.1_2026-09-01.md`), le gel d'une mineure V3 rejoue la batterie cumulative en **une seule passe**.

Si un scénario échoue, la règle de reproductibilité conservée depuis le gel V2.1 reste applicable : ce scénario précis est rejoué (reprises ciblées) pour distinguer variance et régression réelle, sans revenir à deux passes complètes systématiques.

---

## 13.3 Validation des nouveautés de la mineure

Les propriétés réellement nouvelles de la mineure disposent de scénarios spécifiques, créés avant l'implémentation complète (§9).

Une comparaison A / B′ est utilisée lorsqu'elle apporte une information utile sur la valeur ajoutée du skill.

---

## 13.4 Promotion

Chaque mineure validée est promue individuellement dans `dist/stable/`, selon la procédure déjà décrite dans `dist/stable/CLAUDE.md` (nouveau dossier versionné, archive ZIP, contrôle d'intégrité, commit, tag de release distinct du tag de gel).

`V3.3.0` est directement la V3 complète et devient la version publique recommandée, sans palier de clôture séparé (§4.1).

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

Le même cycle se répète trois fois, une fois par mineure, avant d'enchaîner sur la suivante :

```text
V2.1 stable et validée
│
├─ V3.1.0 — Chantier 1 : catalogue d'activités
│  ├─ rédiger / réduire la promesse V3.1.0 (chantier 1 seul)
│  ├─ créer quelques SPEC discriminantes
│  ├─ tester en A / B′ lorsque pertinent
│  ├─ confirmer / retirer / ajuster les propriétés
│  ├─ geler la promesse V3.1.0
│  ├─ implémenter par petits morceaux
│  ├─ petits runs ciblés + diagnostic
│  ├─ non-régression cumulative (V2.1), une seule passe
│  └─ promotion V3.1.0
│
├─ V3.2.0 — Chantier 2 : leviers cognitifs et biais
│  ├─ étendre la promesse à V3.2.0 (chantier 2 seul)
│  ├─ (même cycle : SPEC, A/B′, ajustement, gel, implémentation, runs)
│  ├─ non-régression cumulative (V2.1 + V3.1.0), une seule passe
│  └─ promotion V3.2.0
│
└─ V3.3.0 — Chantier 3 : tutorat
   ├─ étendre la promesse à V3.3.0 (chantier 3 seul)
   ├─ (même cycle : SPEC, A/B′, ajustement, gel, implémentation, runs)
   ├─ non-régression cumulative (V2.1 + V3.1.0 + V3.2.0), une seule passe
   └─ promotion V3.3.0 = V3 complète
```

---

# 16. Règles de conduite à garder sous les yeux

> **Doctrine avant procédure.**

> **La V2.1 est le socle validé ; la V3 l'étend, elle ne la réécrit pas.**

> **Une mineure = un chantier gelé, non-régressé et promu avant d'engager le suivant.**

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
