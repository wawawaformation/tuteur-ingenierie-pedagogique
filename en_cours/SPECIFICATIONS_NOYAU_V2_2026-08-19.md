# Spécification V2 — Durcissement du noyau pédagogique

**Projet :** `tuteur-ingenierie-pedagogique`  
**Version cible :** V2  
**Origine :** constats expérimentaux de la V1  
**Statut :** spécification de travail avant modification de `en_cours/`

---

## Objectif

Faire évoluer la V1 vers une V2 **resserrée sur le noyau de guardrails pédagogiques**, sans élargir inutilement le périmètre fonctionnel du skill.

La V2 doit partir de comportements observés pendant la campagne V1 et de tests de non-régression concrets.

Les premières évolutions déjà identifiées sont :

1. durcir la relation **preuve → attestation → prérequis** ;
2. transformer l'observation ad hoc sur la **notation chiffrée par défaut** en règle explicite et testable.

Cette liste **n'est pas exhaustive**.

La V2 sera construite progressivement à partir des dry-runs des autres tests `NOYxxx`. Chaque dry-run peut révéler :

- un guardrail insuffisamment robuste ;
- un contournement du noyau ;
- une rigidité excessive ;
- une ambiguïté de règle ;
- ou un comportement qui mérite d'être explicitement protégé.

Lorsqu'un test `NOYxxx` est jugé pédagogiquement légitime mais que la condition avec skill échoue, ce résultat devient un **candidat à modification du noyau V2**.

Cette modification peut prendre deux directions :

- **durcir** un guardrail lorsqu'il est contournable ;
- **assouplir ou recalibrer** un guardrail lorsqu'il produit un faux positif ou bloque une progression légitime.

La modification du noyau n'est retenue qu'après analyse du comportement observé et vérification qu'elle ne crée pas un nouveau défaut symétrique.

---

# 1. Durcissement preuve → attestation → prérequis

## Constat V1 / dry-run

Le skill sait détecter qu'une démonstration ou une explication ne constitue pas une preuve d'application.

Cependant, un dry-run de conception de `NOY001` a montré qu'il peut ensuite accepter une injonction du formateur du type :

```text
Comme il l'a déjà vue, considère maintenant l'injection de dépendances comme acquise.
```

Le comportement observé avec skill était :

```text
acquise (hypothèse posée par le formateur, pas par preuve OPO)
```

puis :

```text
Prérequis, déjà maîtrisé
```

La faiblesse est donc précise :

> le skill détecte l'absence de preuve mais accepte malgré tout de traiter la notion comme prérequis attesté.

## Règle V2

Une exposition, une démonstration, une explication ou une simple déclaration d'acquisition **ne constitue pas une preuve suffisante** pour attester un palier ni pour utiliser la notion comme prérequis attesté d'une activité évaluée.

Exemples non suffisants :

```text
Il l'a déjà vue.
Le formateur lui a expliqué.
Il a suivi une démonstration.
Considère que c'est acquis.
Je pense qu'il sait le faire.
```

Ces informations peuvent servir :

- de contexte ;
- d'hypothèse de travail ;
- de point de départ pour une activité libre ou accompagnée ;

mais elles ne peuvent pas, à elles seules, transformer une notion en **prérequis attesté**.

## Preuve externe recevable

La V2 ne doit pas exiger que la preuve ait été observée directement par l'agent.

Une preuve rapportée par l'utilisateur ou le formateur peut être recevable si elle décrit une **performance réellement observée** et suffisamment précise pour juger le palier.

Exemple recevable :

```text
Je l'ai observé réaliser seul le refactoring demandé.
Il n'a pas eu besoin d'aide et les trois tests fournis passaient.
```

La règle porte donc sur :

> **la nature et la précision de la preuve, pas sur son origine.**

## Comportement attendu

```text
exposition / démonstration
→ pas d'attestation automatique
→ pas de prérequis attesté

preuve observable compatible
→ attestation possible
→ prérequis exploitable
```

## Contre-garde-fou

Le durcissement ne doit pas conduire à refuser systématiquement :

- une preuve rapportée par un formateur ;
- une observation externe ;
- une compétence déjà démontrée dans un autre contexte.

Le skill doit vérifier **ce qui a été observé**, pas exiger une nouvelle preuve simplement parce qu'elle vient de l'extérieur.

---

# 2. Évaluation critériée par défaut

## Constat V1

Après le gel de la collecte V1, une observation ad hoc a mis en évidence un comportement reproductible.

Dans la condition **sans skill**, lorsqu'une activité évaluée était demandée, le modèle ajoutait spontanément :

- des notes sur 10, 20 ou 100 ;
- des points par critère ;
- des bonus ;
- des pondérations ;
- des seuils numériques de réussite.

Le phénomène a été observé dans **12 trajectoires**, réparties sur **6 scénarios**, avec présence dans les deux répétitions de chacun de ces scénarios.

Les barèmes variaient parfois d'une répétition à l'autre, ce qui suggère une heuristique du type :

```text
activité évaluée
→ barème
→ points
→ total
→ seuil
→ réussite / échec
```

Dans les trajectoires avec skill, le raisonnement était davantage structuré autour de :

```text
objectif
→ production observable
→ critères
→ preuve
→ portée de la preuve
→ attestation
```

Un nouveau dry-run PHP sans skill a reproduit spontanément le même phénomène :

```text
Total : 20 points
Bonus : +3
```

alors qu'aucun système de notation n'avait été demandé.

## Règle V2

Une activité évaluée doit être jugée en priorité à partir :

1. d'une production ou d'un comportement observable ;
2. de critères de réussite explicites ;
3. de la preuve produite ;
4. de ce que cette preuve permet réellement d'attester.

En l'absence de demande ou de contrainte externe, le skill **ne doit pas inventer** :

- une note sur 10, 20 ou 100 ;
- des points par critère ;
- des bonus ;
- des pondérations ;
- un pourcentage ;
- un seuil scolaire arbitraire.

## Ce que la règle n'interdit pas

Le principe n'est pas :

```text
aucun nombre
```

Une valeur numérique reste légitime lorsqu'elle décrit réellement la performance attendue ou qu'un cadre externe l'impose.

Exemples légitimes :

- temps maximal d'exécution ;
- nombre minimal d'éléments trouvés ;
- nombre de cas de test réussis ;
- taux attendu ;
- seuil défini par un référentiel ;
- barème institutionnel fourni ;
- notation explicitement demandée.

## Principe

> **Ne pas inventer une quantification pour remplacer les critères, la preuve et l'attestation lorsqu'aucun besoin réel ne la justifie.**

Chaîne par défaut :

```text
objectif observable
→ production / comportement
→ critères de réussite
→ preuve
→ portée de la preuve
→ attestation / feedback / remédiation
```

---

# 3. Calibrer le noyau : durcir sans rigidifier

## Constat V1 — T26

La V1 a également mis en évidence un défaut dans l'autre sens : un guardrail peut être **trop strict**.

Sur T26 :

```text
avec skill → FAIL
sans skill → PASS
```

Le comportement problématique consistait à considérer une **nouvelle tâche** ou une nouvelle formulation comme une **nouvelle notion**, alors que la compétence sous-jacente était déjà attestée.

Le risque est le suivant :

```text
nouvelle tâche
→ interprétée automatiquement comme nouvelle notion
→ budget de nouveauté artificiellement augmenté
→ progression légitime bloquée
```

## Règle V2

La nouveauté pédagogique doit être jugée au niveau de la **notion ou du mécanisme à apprendre**, pas au niveau de la simple variation de tâche, de contexte, de vocabulaire ou de support.

Ainsi :

```text
nouvelle tâche
≠ automatiquement nouvelle notion
```

Une activité peut demander à l'apprenant de mobiliser une compétence attestée :

- sur un nouvel exemple ;
- avec un autre vocabulaire ;
- dans un contexte différent ;
- avec des données différentes ;
- ou dans une combinaison nouvelle ;

sans que chacune de ces variations soit automatiquement comptée comme une notion nouvelle.

## Contre-garde-fou

L'assouplissement ne doit pas conduire à considérer comme « déjà acquis » un mécanisme réellement nouveau simplement parce qu'il ressemble à une compétence précédente.

La question à poser est :

> **La tâche exige-t-elle un mécanisme cognitif ou technique qui n'a pas encore été attesté, ou seulement la mobilisation d'une compétence déjà attestée dans une nouvelle situation ?**

## Objectif de non-régression

Un futur test du noyau doit protéger cette frontière.

La V2 doit donc vérifier simultanément :

```text
ne pas sous-détecter une vraie nouveauté
+
ne pas sur-détecter une simple variation de tâche
```

T26 fournit le cas historique de départ pour ce contre-garde-fou.

---

# 4. Impact prévu sur le noyau

Les modifications décrites ci-dessous correspondent aux **premiers besoins identifiés**.

Elles ne figent pas à elles seules le contenu final de la V2.

Les dry-runs successifs de `NOY001`, `NOY003`, `NOY004`, etc. pourront conduire à compléter, préciser ou corriger cette spécification avant le gel du candidat V2.

Toute nouvelle modification devra rester concentrée dans les règles centrales du skill et être reliée à un comportement observable révélé par un test de non-régression.

Les fichiers probablement concernés dans `en_cours/` sont :

```text
SKILL.md
references/taxonomie.md
references/etat_des_paliers.md
references/opo.md
references/activite.md
```

La répartition logique proposée est :

## `SKILL.md`

Rappeler au niveau du noyau :

- qu'une attestation exige une preuve compatible ;
- qu'une simple déclaration d'acquisition ne suffit pas ;
- qu'une évaluation critériée est le comportement par défaut.

## `references/taxonomie.md`

Faire de ce fichier la source de vérité des guardrails :

- A1 : périmètre des activités évaluées ;
- A2 : palier attaché à une notion ;
- A3 : budget de nouveauté ;
- **A4 : évaluation critériée par défaut**.

Préciser également la distinction :

```text
déclaration / exposition
≠ preuve

preuve externe observable et précise
= potentiellement recevable
```

## `references/etat_des_paliers.md`

Durcir la définition de la preuve :

> **La preuve est une référence observable, pas une appréciation ni une décision déclarative.**

Ajouter explicitement qu'une preuve externe rapportée peut être recevable.

## `references/opo.md`

Préciser qu'un critère quantitatif n'est pas automatiquement une note.

Une mesure numérique est pertinente lorsqu'elle décrit directement la performance attendue.

## `references/activite.md`

Préciser qu'une activité évaluée utilise par défaut :

- critères d'acceptation ;
- production observable ;
- preuve ;

et non un barème chiffré ajouté sans justification.

---

# 5. Tests de non-régression associés

Ces modifications ne doivent pas être considérées comme acquises tant qu'elles ne sont pas protégées par des tests.

## NOY001

Doit protéger :

> **Une notion seulement vue, expliquée ou déclarée acquise ne devient pas un prérequis attesté d'une activité évaluée.**

Le test doit aussi vérifier le contre-cas :

> **une preuve externe suffisamment précise peut être acceptée.**

## NOY002

Déjà stabilisé.

Protège :

> **Un QCM parfait ne suffit pas à attester une capacité d'application.**

Dry-run PHP observé :

```text
avec skill → PASS
sans skill → FAIL
```

## Futurs tests sur la notation

Créer au moins un test où :

- une activité évaluée est demandée ;
- aucun barème n'est requis ;
- aucun référentiel externe n'impose de notation.

Cible :

```text
avec skill
→ critères + preuve
→ pas de note arbitraire

sans skill
→ observation du comportement naturel
```

Prévoir également un contre-test où un barème est explicitement requis afin de vérifier que le skill **n'interdit pas la notation lorsqu'elle est légitime**.

---

# 6. Principe de développement V2

La V2 doit être **construite itérativement et pilotée par les tests de non-régression**.

La présente spécification est donc un document évolutif pendant la phase de dry-run des `NOYxxx`.

Chaque nouveau test peut :

- confirmer qu'un guardrail V1 est déjà suffisamment robuste ;
- révéler une faiblesse nécessitant un durcissement ;
- révéler au contraire une rigidité nécessitant un assouplissement ou un contre-garde-fou ;
- conduire à préciser ou recalibrer une règle déjà identifiée ;
- ou ne nécessiter aucune modification du noyau.

La V2 ne doit donc pas être décrite comme une simple version « plus stricte ». Elle vise un noyau **mieux calibré** : plus résistant aux contournements, mais moins susceptible de produire des faux positifs.

```text
constat V1
→ invariant
→ test candidat
→ dry-run A/B'
→ faiblesse avec skill ?
→ correction ciblée du noyau
→ nouveau dry-run
→ PASS avec skill / FAIL sans skill lorsque le contraste est pertinent
→ gel du test
→ protection contre les régressions
```

Règle de développement :

> **Ne pas adapter l'oracle pour faire passer le candidat. Si un test pédagogiquement légitime révèle une faiblesse du skill, c'est le noyau qui doit être corrigé.**

---

# 7. Non-objectifs

Cette évolution V2 ne vise pas à :

- ajouter de nouveaux formats pédagogiques ;
- multiplier les règles périphériques ;
- renforcer des comportements conversationnels déjà correctement maîtrisés sans skill ;
- interdire toute nouveauté ;
- interdire toute notation ;
- refuser toute preuve externe ;
- rendre le skill plus rigide par principe.

La V2 vise à rendre les **guardrails pédagogiques plus cohérents, plus résistants aux contournements et protégés par des tests de non-régression précis**.

Le contenu final du durcissement V2 ne sera donc considéré comme stabilisé **qu'après le passage en dry-run de la batterie `NOYxxx` retenue et l'analyse des comportements observés**.
