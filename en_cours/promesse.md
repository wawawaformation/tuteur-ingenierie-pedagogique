# Promesse du candidat V2.1.0

Ce document constitue la **spécification fonctionnelle** de la version candidate V2.1.0 du skill `tuteur-ingenierie-pedagogique`.

La promesse est volontairement limitée aux comportements pour lesquels le skill cherche à modifier une décision pédagogique de l'agent par rapport à une génération plausible mais insuffisamment diagnostique.

Le skill ne promet pas d'améliorer globalement toute production pédagogique.

La numérotation historique est conservée. **P01 n'appartient plus à la promesse générale du noyau V2.1.0** ; son enseignement sera repris dans la future promesse spécifique au tutorat V3.

## Promesse centrale

> **Amener l'agent à raisonner ses décisions d'apprentissage et d'évaluation notion par notion, à partir de ce qui est réellement attesté et des sources disponibles, afin de préserver la valeur diagnostique des activités et l'alignement entre ce qui est visé, demandé, observé et conclu.**

---

## P02 — Raisonner par notion, palier, preuve et attestation

L'agent doit raisonner sur l'état des **notions effectivement mobilisées**, et non attribuer un niveau global à l'apprenant.

Il doit distinguer notamment :

* exposition à une notion ;
* accompagnement dans sa mise en œuvre ;
* déclaration ou impression de compréhension ;
* performance réellement observable ;
* observation précise rapportée par un formateur ;
* attestation explicite d'une notion à un palier nommé par un formateur identifié ;
* preuve compatible avec le palier que l'on souhaite attester.

Les différentes sources ne possèdent pas automatiquement la même valeur d'attestation.

| Source                                                          | Valeur                                                                           |
| --------------------------------------------------------------- | -------------------------------------------------------------------------------- |
| L'apprenant déclare quelque chose sur lui-même                  | Contexte ou information diagnostique ; pas d'attestation automatique             |
| L'apprenant réalise un acte observable                          | Preuve limitée à ce que l'acte montre réellement                                 |
| Le formateur rapporte une observation précise                   | Preuve externe à qualifier selon la tâche, les conditions et le résultat observé |
| Le formateur atteste explicitement une notion à un palier nommé | Attestation autoritative à enregistrer comme telle                               |

Une appréciation générale du formateur ne vaut pas automatiquement attestation d'un palier.

> « Je pense qu'il maîtrise bien cette notion. »

ne constitue pas, à elle seule, une attestation précise.

En revanche :

> **une attestation explicite d'une notion à un palier nommé par un formateur identifié fait foi et doit être enregistrée comme telle.**

Conséquences attendues :

* une démonstration ou un accompagnement guidé ne valent pas automatiquement preuve autonome ;
* une auto-déclaration positive ne prouve pas à elle seule la performance racontée ;
* une auto-déclaration négative ne prouve pas à elle seule une incapacité ;
* le manque de preuve ne constitue pas une preuve de manque ;
* le palier 0 signifie qu'aucun palier n'est encore attesté pour la notion ; il ne signifie pas que l'apprenant ne maîtrise pas la notion ;
* ce que l'apprenant manifeste réellement dans son message peut constituer une preuve, mais uniquement à hauteur de l'acte effectivement observable ;
* la richesse du vocabulaire, la fluidité du discours ou l'assurance exprimée ne suffisent pas à augmenter un palier ;
* un quiz de compréhension ne prouve pas à lui seul une capacité de production ;
* le canal utilisé pour produire une preuve — écrit, oral ou autre — ne détermine pas à lui seul son palier : c'est l'acte observable qui compte ;
* une preuve externe rapportée peut être recevable si la tâche, les conditions et le résultat observé sont suffisamment précis pour juger le palier visé ;
* une appréciation générale du formateur ne doit pas être transformée implicitement en attestation de palier ;
* une attestation explicite du formateur doit rester attachée à la notion et au palier effectivement nommés ;
* une nouvelle preuve peut conduire à réviser, y compris à la baisse, l'état précédemment retenu.

**Tests de référence :** T06, T07, T14, T24.

---

## P03 — Préserver la valeur diagnostique d'une activité évaluée

Avant de proposer une activité évaluée, l'agent doit identifier les notions nécessaires à sa réussite et distinguer celles qui sont attestées de celles qui ne le sont pas encore au niveau demandé.

Pour une activité évaluée, le **budget de nouveauté est limité à une notion non attestée**.

L'agent doit notamment :

* accepter une activité comportant une seule nouveauté lorsque les autres prérequis nécessaires sont attestés ;
* ne pas confondre nouvelle tâche et nouvelle notion ;
* refuser, découper ou échafauder une activité qui empile plusieurs notions non attestées ;
* résister à une demande de difficulté artificielle si cette difficulté détruit la valeur diagnostique de l'activité ;
* fournir en échafaudage les éléments qui ne sont pas eux-mêmes l'objet de l'évaluation ;
* permettre une activité de synthèse intégrée lorsque les notions nécessaires ont préalablement été attestées ;
* limiter la portée d'une preuve à ce qui a réellement été observé.

Le principe n'est donc pas :

> une activité complexe est interdite.

Le principe est :

> **une activité ne doit pas être utilisée pour conclure sur une maîtrise si son échec ou sa réussite ne permet plus d'identifier ce qui est réellement démontré.**

La portée d'une preuve doit rester précise :

```text
utiliser ≠ créer
exécuter ≠ écrire
lire ≠ produire
modifier ≠ concevoir
```

**Tests ancres historiques :** T09, T24, T27.

---

## P04 — Aligner objectif, tâche, production, critères, preuve et conclusion

L'agent doit maintenir la cohérence entre :

```text
objectif
→ tâche
→ production ou performance observable
→ critères
→ preuve
→ conclusion
```

Il doit notamment :

* ne pas utiliser une tâche de production autonome pour prétendre évaluer uniquement une compréhension ;
* ne pas utiliser une preuve de reconnaissance ou de restitution pour attester une capacité de production ;
* faire correspondre les critères à la performance réellement attendue ;
* expliciter ou corriger un décalage entre objectif, tâche, production, critères et preuve ;
* ne conclure qu'à hauteur de ce que la preuve permet réellement d'attester ;
* choisir une forme d'évaluation compatible avec ce que l'on cherche réellement à établir.

**Tests de référence :** T12, T14.

---

# Garanties de fonctionnement

Ces garanties participent à la fiabilité du skill mais ne constituent pas, à elles seules, sa promesse différentielle principale.

## G01 — Ne pas inventer un état ou une persistance absente

L'agent ne doit pas prétendre disposer d'un état de progression qui n'est pas effectivement accessible.

## G02 — Résoudre explicitement les dérogations locales et les contradictions documentaires

Le noyau constitue la règle générale.

Une référence spécialisée peut explicitement déroger à une règle du noyau pour son seul périmètre.

Une dérogation n'est valide que si elle est **signalée explicitement comme telle dans la référence spécialisée**.

La règle de priorité est :

```text
pas de dérogation explicite
→ le noyau prévaut

dérogation explicite dans une référence spécialisée
→ la règle spécialisée prévaut
→ uniquement dans son périmètre
```

Une dérogation locale n'autorise pas à modifier implicitement la règle générale ni à l'étendre à d'autres contextes.

Lorsqu'une contradiction pertinente entre deux sources mobilisées n'est pas résolue par une dérogation explicite, l'agent doit la signaler plutôt que choisir silencieusement une règle.

## G03 — Ne pas transformer les paliers cognitifs en barrières absolues

Les paliers servent à raisonner sur l'objectif et sur la preuve.

Ils ne doivent pas interdire l'utilisation d'une situation complexe, d'une analyse ou d'un problème réel comme point d'entrée pédagogique.

## G04 — Respecter le périmètre demandé

L'agent doit répondre au besoin demandé sans élargir inutilement la production.

## G05 — Ne pas inventer de notation arbitraire

Une évaluation n'implique pas nécessairement une note.

Lorsque aucun barème, score, système de points ou règle de notation réelle n'est fourni ou demandé, l'agent ne doit pas en créer spontanément.

## G06 — Préserver la valeur de l'évaluation avant production

Lorsque l'activité est évaluée, les critères de réussite ou de performance restent explicites pour l'apprenant, mais les éléments réservés à la correction, une production de référence donnant la solution ou les attendus détaillés de correction ne doivent pas être révélés avant sa production.

---

# Principes d'architecture et de qualité hors promesse différentielle

Les éléments suivants appartiennent au fonctionnement attendu du candidat V2.1.0, mais ne sont **pas revendiqués comme constituant à eux seuls sa valeur différentielle**.

## Granularité

Le découpage interne de référence est :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité directement rattachée si pertinent
```

`Activité` est la granularité la plus fine.

Ce découpage est un cadre interne de travail, pas une taxonomie universelle : les appellations peuvent varier selon les organismes ou référentiels.

## Modalités

Deux axes doivent rester distincts :

```text
synchrone / asynchrone
≠
présentiel / distanciel
```

La modalité influence la conception, mais ne détermine pas automatiquement la granularité ou le gabarit.

## Gabarits d'Activité

`Activité` constitue le socle commun.

Les spécialisations actuellement disponibles sont :

```text
Brique
Atelier
Quiz
Recul
```

Leur finalité et leurs usages typiques servent à orienter le choix sans créer d'équivalences rigides du type :

```text
court → Brique
asynchrone → Atelier
présentiel → Séance
difficile → Atelier
```

Les gabarits sont des contrats de production spécialisés ; ils ne sont pas des niveaux concurrents de `Module`, `Séquence`, `Séance` ou `Activité`.

## Autres qualités attendues

Restent également souhaitables :

* posture professionnelle et non infantilisante ;
* ancrage dans des situations concrètes ;
* stabilité des formats de production ;
* utilisation d'un référentiel lorsqu'il est pertinent et disponible ;
* vocabulaire adapté au contexte de formation.

Ces éléments peuvent faire l'objet de tests de non-régression ou de conformité, mais leur réussite ne suffit pas à démontrer l'apport propre du skill.

---

# Critère comportemental central

Le succès du skill ne se mesure pas à la longueur de la réponse ni au fait que l'agent cite ses règles.

La question centrale est :

> **Une information pédagogique pertinente différente conduit-elle l'agent à prendre une décision différente lorsque cette information devrait effectivement modifier l'apprentissage ou l'évaluation ?**

Le comportement recherché est :

```text
Demande
   ↓
Notions réellement mobilisées
   ↓
Sources disponibles
(déclarations, actes observables,
observations rapportées, attestations explicites)
   ↓
État attesté notion par notion
   ↓
Nouveautés nécessaires
   ↓
Valeur diagnostique de l'activité
   ↓
Alignement objectif / tâche / production / critères / preuve
   ↓
Conclusion et décision pédagogique
```

et non :

```text
Demande
   ↓
Génération immédiate d'une activité plausible
```
