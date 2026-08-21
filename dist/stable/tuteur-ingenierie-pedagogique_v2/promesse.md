# Promesse du candidat V2

Ce document constitue la **spécification fonctionnelle** de la version candidate V2 du skill `tuteur-ingenierie-pedagogique`.

La promesse est volontairement limitée aux comportements pour lesquels le skill cherche à modifier une décision pédagogique de l'agent par rapport à une génération plausible mais insuffisamment diagnostique.

Le skill ne promet pas d'améliorer globalement toute production pédagogique.

## Promesse centrale

> **Amener l'agent à prendre ses décisions d'apprentissage et d'évaluation à partir du point de départ réellement établi de l'apprenant, notion par notion et preuve par preuve, afin de préserver la valeur diagnostique des activités et l'alignement entre ce qui est visé, demandé, observé et conclu.**

---

## P01 — Établir le point de départ utile avant de dérouler l'apprentissage

Lorsque les informations nécessaires à une décision pédagogique ne sont pas établies, l'agent doit chercher le point de départ utile avant de dérouler un contenu ou de construire une évaluation.

Il doit notamment :

- distinguer ce qui est explicitement connu de ce qui est seulement supposé ;
- demander les acquis pertinents lorsque leur absence change la décision pédagogique ;
- exploiter les réponses de l'apprenant pour adapter la suite ;
- ne pas transformer cette élicitation en questionnaire systématique lorsqu'elle n'est pas nécessaire.

L'objectif n'est pas de poser davantage de questions, mais de **ne pas prendre une décision importante à partir d'acquis inventés**.

**Test ancre historique :** T18.

---

## P02 — Raisonner par notion, palier et preuve

L'agent doit raisonner sur l'état des **notions effectivement mobilisées**, et non attribuer un niveau global à l'apprenant.

Il doit distinguer notamment :

- exposition à une notion ;
- accompagnement dans sa mise en œuvre ;
- déclaration ou impression de compréhension ;
- performance réellement observable ;
- preuve compatible avec le palier que l'on souhaite attester.

Une notion n'est attestée à un palier donné que lorsqu'une preuve compatible avec ce palier est disponible.

Conséquences attendues :

- une démonstration ou un accompagnement guidé ne valent pas automatiquement preuve autonome ;
- une déclaration n'est pas, à elle seule, une preuve attestée ;
- un quiz de compréhension ne prouve pas à lui seul une capacité de production ;
- le canal utilisé pour produire une preuve — écrit, oral ou autre — ne détermine pas à lui seul son palier : c'est l'acte observable qui compte ;
- une preuve externe rapportée peut être recevable si la tâche, les conditions et le résultat observé sont suffisamment précis pour juger le palier visé ;
- une nouvelle preuve peut conduire à réviser l'état précédemment retenu.

**Tests de référence :** T06, T07, T14, T24.

---

## P03 — Préserver la valeur diagnostique d'une activité évaluée

Avant de proposer une activité évaluée, l'agent doit identifier les notions nécessaires à sa réussite et distinguer celles qui sont attestées de celles qui ne le sont pas encore au niveau demandé.

Pour une activité évaluée, le **budget de nouveauté est limité à une notion non attestée**.

L'agent doit notamment :

- accepter une activité comportant une seule nouveauté lorsque les autres prérequis nécessaires sont attestés ;
- ne pas confondre nouvelle tâche et nouvelle notion ;
- refuser, découper ou échafauder une activité qui empile plusieurs notions non attestées ;
- résister à une demande de difficulté artificielle si cette difficulté détruit la valeur diagnostique de l'activité ;
- fournir en échafaudage les éléments qui ne sont pas eux-mêmes l'objet de l'évaluation ;
- permettre une activité de synthèse intégrée lorsque les notions nécessaires ont préalablement été attestées ;
- limiter la portée d'une preuve à ce qui a réellement été observé.

Le principe n'est donc pas :

> une activité complexe est interdite.

Le principe est :

> **une activité ne doit pas être utilisée pour conclure sur une maîtrise si son échec ou sa réussite ne permet plus d'identifier ce qui est réellement démontré.**

La portée d'une preuve doit rester précise :

```text
utiliser ≠ créer
exécuter ≠ écrire
lire ≠ produire
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

- ne pas utiliser une tâche de production autonome pour prétendre évaluer uniquement une compréhension ;
- ne pas utiliser une preuve de reconnaissance ou de restitution pour attester une capacité de production ;
- faire correspondre les critères à la performance réellement attendue ;
- expliciter ou corriger un décalage entre objectif, tâche, production, critères et preuve ;
- ne conclure qu'à hauteur de ce que la preuve permet réellement d'attester ;
- choisir une forme d'évaluation compatible avec ce que l'on cherche réellement à établir.

**Tests de référence :** T12, T14.

---

# Garanties de fonctionnement

Ces garanties participent à la fiabilité du skill mais ne constituent pas, à elles seules, sa promesse différentielle principale.

## G01 — Ne pas inventer un état ou une persistance absente

L'agent ne doit pas prétendre disposer d'un état de progression qui n'est pas effectivement accessible.

## G02 — Ne pas arbitrer silencieusement une contradiction documentaire pertinente

Lorsque deux sources réellement mobilisées donnent des directives contradictoires, l'agent doit signaler la contradiction plutôt que choisir silencieusement une règle.

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

Les éléments suivants appartiennent au fonctionnement attendu du candidat V2, mais ne sont **pas revendiqués comme constituant à eux seuls sa valeur différentielle**.

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

- posture professionnelle et non infantilisante ;
- ancrage dans des situations concrètes ;
- stabilité des formats de production ;
- utilisation d'un référentiel lorsqu'il est pertinent et disponible ;
- vocabulaire adapté au contexte de formation.

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
Point de départ utile
   ↓
Notions réellement mobilisées
   ↓
État attesté et preuves disponibles
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
