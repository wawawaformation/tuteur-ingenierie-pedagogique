# Spécification V2 — Consolidation du noyau pédagogique et des gabarits

**Projet :** `tuteur-ingenierie-pedagogique`  
**Version cible :** V2  
**Origine :** constats expérimentaux de la V1 et travaux de stabilisation V2  
**Statut :** spécification de travail de la V2

---

# 0. Objectif et périmètre de la V2

L'objectif de la V2 est **d'améliorer, fiabiliser, clarifier et simplifier le produit existant sans étendre son périmètre fonctionnel**.

La V2 n'a pas pour objet d'ajouter de nouvelles familles de fonctionnalités ni de nouveaux formats pédagogiques. Elle doit :

- consolider les comportements déjà présents ;
- corriger les incohérences internes ;
- clarifier l'architecture du skill ;
- épurer le noyau des explications générales que le modèle sait déjà traiter correctement ;
- rendre plus explicites les contrats propres au produit ;
- protéger ces contrats par des tests de non-régression.

La V2 reste donc une version de **consolidation**, pas une version d'enrichissement fonctionnel.

L'enrichissement de la bibliothèque avec de nouvelles formes d'activités relève d'une version ultérieure, notamment de la V3.

Principe directeur :

```text
V2
→ mieux faire ce que le skill sait déjà faire
→ sans ajouter de nouvelle capacité fonctionnelle

V3+
→ enrichir progressivement la bibliothèque d'activités et explorer de nouveaux usages
```

---

# 1. Les trois fonctions structurantes du skill

La V2 organise le produit autour de trois fonctions déjà présentes dans le skill.

## 1.1. Piloter la progression par notions, paliers et preuves

Le skill suit la progression à partir d'une chaîne explicite :

```text
notion
→ palier
→ preuve
→ attestation
→ progression
```

Une attestation ne repose pas sur une impression générale de réussite mais sur une preuve compatible avec la notion et le palier visés.

Cette fonction couvre notamment :

- le suivi notion par notion ;
- la qualification des preuves ;
- l'attestation des paliers ;
- l'utilisation des acquis attestés comme prérequis ;
- les contre-garde-fous évitant de confondre exposition, déclaration et preuve.

## 1.2. Concevoir des activités évaluées interprétables

Une activité évaluée doit permettre de comprendre ce qui a réellement été démontré.

Chaîne de référence :

```text
objectif observable
→ activité / tâche
→ livrable ou comportement observable
→ critères de réussite / performance
→ preuve
→ portée de la preuve
→ conclusion / attestation / remédiation
```

Cette fonction couvre notamment :

- le budget de nouveauté ;
- l'alignement entre objectif, tâche, livrable, critères et conclusion ;
- la portée réelle d'une preuve ;
- l'évaluation critériée par défaut ;
- l'absence de notation arbitraire lorsque rien ne l'impose.

## 1.3. Structurer la formation et produire les activités à partir d'une bibliothèque de gabarits

Le découpage pédagogique de référence reste :

```text
Module
└── Séquence
    └── Séance
        └── Activité
```

**Activité est le niveau de granularité le plus fin du découpage.**

Une activité peut ensuite prendre différentes formes documentées par des gabarits, par exemple :

```text
Activité
├── Brique
├── Atelier
├── Quiz
├── Recul
└── autres gabarits futurs
```

Les gabarits spécialisés ne constituent pas des niveaux concurrents de `Activité`. Ils représentent des **formes particulières d'activité**.

La bibliothèque de gabarits doit être **auto-descriptive** : chaque gabarit expose dans ses métadonnées les éléments qui permettent à l'agent de comprendre sa finalité et d'estimer sa pertinence pour le besoin courant.

Dans une lecture agentique de l'architecture, les gabarits jouent ainsi le rôle d'**outils de conception spécialisés mis à disposition de l'agent** : le noyau ne doit pas mémoriser toutes les situations d'usage de chaque gabarit, mais savoir les découvrir, les sélectionner et appliquer leur contrat. Cette analogie ne signifie pas que les gabarits sont des `tool calls` techniques ; ils restent des ressources documentaires du skill.

La bibliothèque est conçue pour être évolutive, mais la V2 consolide uniquement les gabarits déjà présents. L'ajout de nouveaux gabarits est hors périmètre de cette version.

---

# 2. Socle commun d'une Activité

Toute activité repose sur un **socle commun minimal**.

Les gabarits spécialisés — Brique, Atelier, Quiz, Recul, etc. — héritent de ce socle et peuvent le **compléter, le préciser ou l'adapter** selon leur finalité pédagogique.

Le socle commun doit rendre explicites, selon le contexte et avec le niveau de détail adapté :

- au moins un **OPO / objectif pédagogique observable** ;
- une **durée** ou une durée indicative ;
- une **consigne / brief** ;
- les **conditions, contraintes ou modalités utiles** ;
- les **ressources / le matériel de départ** lorsqu'ils sont nécessaires ;
- le **livrable ou la trace attendue**, lorsque l'activité en produit un ;
- les **critères de réussite / critères de performance** lorsque l'activité donne lieu à une évaluation ou à une vérification explicite.

Le gabarit spécialisé peut adapter ce socle à sa finalité.

Exemples :

```text
Quiz
→ reprend le socle Activité
→ adapte le livrable en réponses
→ précise questions, feedback et correction

Recul
→ reprend le socle Activité
→ adapte la trace attendue en production réflexive
→ précise l'explicitation, la justification et le transfert

Atelier
→ reprend le socle Activité
→ développe l'organisation, la méthode et le livrable
```

La structure exacte de chaque gabarit reste définie dans son fichier de référence.

---

# 3. Gabarits : choix contextuel, auto-descriptif, non exclusif et évolutif

Le choix d'un gabarit dépend du besoin pédagogique, de la granularité recherchée, du contexte de mise en œuvre et, lorsqu'elle est connue, de la modalité.

La modalité **oriente** la conception mais ne crée pas une table d'interdiction rigide entre un gabarit et un contexte.

Ainsi :

```text
Quiz
→ peut être utilisé en synchrone ou en asynchrone

Recul
→ peut être utilisé en synchrone ou en asynchrone

Atelier
→ peut être mobilisé dès lors que son format est pertinent pour le besoin
```

## 3.1. Métadonnées de routage des gabarits

Chaque gabarit doit disposer d'un **front matter utile au routage**.

Ces métadonnées doivent permettre à l'agent d'identifier rapidement, sans charger dans le noyau toutes les règles propres au format :

- l'identité du gabarit ;
- sa nature de gabarit d'activité ;
- sa finalité pédagogique principale ;
- son rattachement au socle commun `Activité` ;
- un ou deux **usages types** ;
- les éventuelles indications réellement nécessaires pour éviter un mauvais emploi.

Les usages types sont **des exemples d'orientation**, pas des conditions exclusives.

En particulier, le front matter ne doit pas créer artificiellement des règles du type :

```text
Quiz = asynchrone uniquement
Recul = asynchrone uniquement
Atelier = présentiel uniquement
```

sauf si une contrainte réelle, explicitement documentée et propre au gabarit l'impose.

Le détail syntaxique et les clés exactes du front matter relèvent du plan d'implémentation ; la présente spécification impose seulement que les métadonnées soient suffisantes, cohérentes et exploitables pour orienter le choix de l'agent.

## 3.2. Routage attendu

Le noyau agit comme un **orchestrateur** : il analyse le besoin, identifie le bon niveau de granularité, puis s'appuie sur les métadonnées des gabarits disponibles pour sélectionner la forme d'activité pertinente.

Le principe attendu devient :

```text
besoin pédagogique
+ niveau de granularité
+ contexte / modalité
→ consultation des gabarits disponibles et de leurs métadonnées
→ sélection d'un gabarit pertinent
→ chargement de son contrat
→ production
→ contrôles avant livraison
```

Le noyau ne doit donc pas accumuler une table exhaustive de correspondances `situation → gabarit`.

Chaque gabarit peut documenter **un ou deux usages types** afin d'aider l'agent à choisir et à expliquer son choix, sans présenter ces exemples comme des conditions exclusives d'utilisation.

La V2 ne doit pas transformer la bibliothèque en taxonomie fermée des situations pédagogiques.

---

# 4. Modalités : épurer le noyau, conserver les invariants utiles

Les définitions générales de :

```text
synchrone
asynchrone
présentiel
distanciel
```

n'ont pas à être développées longuement dans le noyau normatif.

Elles relèvent du glossaire commun.

Le noyau conserve uniquement les invariants qui influencent réellement le comportement du produit :

- **synchrone / asynchrone** et **présentiel / distanciel** sont deux axes distincts ;
- ne pas déduire automatiquement l'un de l'autre ;
- la modalité influence les choix de conception, mais ne suffit pas à imposer ou interdire un gabarit ;
- le découpage `Module → Séquence → Séance → Activité` reste la structure de référence du produit.

Le glossaire précisera notamment :

```text
Synchrone
→ interaction en même temps.

Asynchrone
→ interaction ou travail en temps différé.

Présentiel
→ participants réunis dans un même lieu physique.

Distanciel
→ participants situés à distance, avec médiation par un outil ou un support numérique.
```

Il rappellera aussi que l'attention et la concentration **peuvent être plus fragiles en distanciel** selon la durée, l'environnement, les sollicitations numériques et le niveau d'interaction ; cette vigilance doit rester une indication pratique, pas une règle absolue.

---

# 5. Durcissement preuve → attestation → prérequis

## 5.1. Règle V2

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

## 5.2. Preuve externe recevable

La V2 ne doit pas exiger que la preuve ait été observée directement par l'agent.

Une preuve rapportée par l'utilisateur ou le formateur peut être recevable si elle décrit une **performance réellement observée** et suffisamment précise pour juger le palier.

Exemple recevable :

```text
Je l'ai observé réaliser seul le refactoring demandé.
Il n'a pas eu besoin d'aide et les trois tests fournis passaient.
```

La règle porte donc sur :

> **la nature et la précision de la preuve, pas sur son origine.**

## 5.3. Comportement attendu

```text
exposition / démonstration / déclaration
→ pas d'attestation automatique
→ pas de prérequis attesté

preuve observable compatible
→ attestation possible
→ prérequis exploitable
```

## 5.4. Contre-garde-fou

Le durcissement ne doit pas conduire à refuser systématiquement :

- une preuve rapportée par un formateur ;
- une observation externe ;
- une compétence déjà démontrée dans un autre contexte.

Le skill doit vérifier **ce qui a été observé**, pas exiger une nouvelle preuve simplement parce qu'elle vient de l'extérieur.

---

# 6. Évaluation critériée par défaut

Une activité évaluée doit être jugée en priorité à partir :

1. d'une production ou d'un comportement observable ;
2. de critères de réussite ou de performance explicites ;
3. de la preuve produite ;
4. de ce que cette preuve permet réellement d'attester.

En l'absence de demande ou de contrainte externe, le skill **ne doit pas inventer** :

- une note sur 10, 20 ou 100 ;
- des points par critère ;
- des bonus ;
- des pondérations ;
- un pourcentage ;
- un seuil scolaire arbitraire.

## 6.1. Ce que la règle n'interdit pas

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

Principe :

> **Ne pas inventer une quantification pour remplacer les critères, la preuve et l'attestation lorsqu'aucun besoin réel ne la justifie.**

---

# 7. Calibrer le noyau : durcir sans rigidifier

La V2 ne doit pas seulement durcir les guardrails. Elle doit également supprimer les faux positifs et les rigidités inutiles.

## 7.1. Nouvelle tâche ≠ automatiquement nouvelle notion

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

## 7.2. Contre-garde-fou

L'assouplissement ne doit pas conduire à considérer comme « déjà acquis » un mécanisme réellement nouveau simplement parce qu'il ressemble à une compétence précédente.

La question à poser est :

> **La tâche exige-t-elle un mécanisme cognitif ou technique qui n'a pas encore été attesté, ou seulement la mobilisation d'une compétence déjà attestée dans une nouvelle situation ?**

---

# 8. Cohérence interne du paquet runtime

La V2 doit également améliorer la fiabilité documentaire du skill sans ajouter de fonctionnalité.

Le paquet runtime doit respecter les principes suivants :

- aucun renvoi nécessaire au fonctionnement ne doit pointer vers une ressource absente ou inaccessible ;
- chaque règle normative doit avoir une **source de vérité identifiable** ;
- un résumé opérationnel peut exister dans un autre fichier, mais il doit indiquer explicitement quelle source fait foi en cas d'écart ;
- deux références runtime ne doivent pas prescrire des comportements incompatibles pour une même situation ;
- les chemins entre fichiers doivent être cohérents avec l'organisation réelle du paquet ;
- les fichiers historiques encore utiles doivent être harmonisés suffisamment pour ne pas créer d'ambiguïté de lecture ou de maintenance ;
- les métadonnées de routage des gabarits doivent rester cohérentes avec leur contenu réel et ne pas contredire leur contrat ;
- le noyau ne doit pas dupliquer inutilement les informations de sélection déjà portées par les gabarits eux-mêmes.

Cette exigence concerne la **cohérence de ce qui existe déjà**, pas l'ajout de nouvelles règles.

---

# 9. Glossaire commun

La V2 introduit un glossaire commun destiné à stabiliser le vocabulaire du skill et à alléger les fichiers normatifs.

Le glossaire :

- donne des définitions courtes ;
- aide à distinguer des termes proches ;
- peut fournir un exemple d'usage ou une vigilance pratique ;
- ne constitue **pas** une seconde source normative ;
- renvoie vers le fichier normatif lorsqu'un terme implique une règle comportementale.

Il doit notamment couvrir :

- activité ;
- gabarit ;
- modalité ;
- OPO ;
- notion ;
- compétence ;
- savoir / savoir-faire / savoir-être ;
- palier ;
- preuve ;
- attestation ;
- exposition ;
- démonstration ;
- activité guidée ;
- activité évaluée ;
- brief ;
- livrable ;
- critère de réussite ;
- critère de performance ;
- évaluation ;
- notation ;
- synchrone / asynchrone ;
- présentiel / distanciel ;
- module ;
- séquence ;
- séance ;
- atelier ;
- quiz ;
- recul ;
- référentiel ;
- front matter / métadonnées de routage.

Deux distinctions doivent être particulièrement explicites :

```text
Activité
→ niveau de granularité et socle commun

Gabarit
→ forme particulière donnée à une activité
```

et :

```text
brief
→ ce que le formateur demande

livrable
→ ce que l'apprenant rend
```

---

# 10. Tests de non-régression NOY

La batterie `NOYxxx` couvre les invariants devant être protégés en non-régression, **y compris les gabarits**.

La V2 ne considère donc pas la couverture comme complète tant que les gabarits existants ne disposent pas de quelques contrôles dédiés dans cette même batterie.

## 10.1. Deux méthodes de construction des NOY

### Comportements dont on veut démontrer l'apport propre du skill

Pendant la conception ou l'évolution d'une capacité comportementale :

```text
A  = avec skill
B' = sans skill
```

Lorsque le contraste est pertinent, la cible de conception est idéalement :

```text
A  → PASS
B' → FAIL
```

Une fois le test stabilisé, la non-régression est ensuite exécutée en **A uniquement**.

### Contrats internes propres au skill, notamment les gabarits

Pour un contrat qui n'existe que dans le skill, la condition sans skill n'est pas informative.

Exemple : un modèle sans skill n'a aucune raison de connaître la structure exacte d'un gabarit `Atelier`, `Quiz` ou `Recul` propre au produit.

Ces NOY sont donc :

```text
conçus en A uniquement
+
exécutés en non-régression en A uniquement
```

Cette règle vaut **dès le développement de la V2** pour les tests de conformité des gabarits.

## 10.2. Couverture gabarits à ajouter en V2

La V2 doit ajouter **2 à 3 NOY** ciblés sur la partie gabarits, sans chercher une couverture exhaustive de tous les formats.

Ils doivent protéger au minimum :

- le socle commun d'une activité ;
- la conformité au gabarit choisi ;
- l'utilisation cohérente des métadonnées de routage ;
- le caractère non exclusif des gabarits vis-à-vis de la modalité ;
- la séparation entre le volet remis à l'apprenant et le volet conservé par le formateur lorsqu'elle est prévue par le gabarit.

Les oracles doivent éviter de figer une table rigide `modalité → gabarit` ou une liste fermée de déclencheurs.

Ils évaluent plutôt :

```text
le choix est-il cohérent avec le besoin ?
+
le gabarit retenu respecte-t-il son contrat ?
```

---

# 11. Principe de développement et de non-régression

La V2 reste pilotée par les tests, mais la phase actuelle n'est plus une exploration ouverte du périmètre.

Le périmètre fonctionnel est fermé : les modifications doivent correspondre à la consolidation des trois fonctions structurantes décrites dans cette spécification.

Pour une capacité comportementale nouvelle ou substantiellement modifiée dans une version future :

```text
invariant
→ test candidat
→ dry-run A/B' lorsque le contraste est pertinent
→ correction ciblée
→ A PASS / B' FAIL si le baseline permet un contraste utile
→ gel du test
→ non-régression A uniquement
```

Pour les contrats internes de gabarits :

```text
contrat du gabarit
→ test A uniquement
→ PASS
→ gel du test
→ non-régression A uniquement
```

Règle générale :

> **Ne pas adapter l'oracle pour faire passer le candidat. Si un test pédagogiquement légitime révèle une faiblesse du skill, c'est le produit qui doit être corrigé.**

---

# 12. Non-objectifs de la V2

La V2 ne vise pas à :

- ajouter de nouveaux gabarits pédagogiques ;
- enrichir la bibliothèque avec de nouvelles formes d'activités ;
- construire une taxonomie fermée liant chaque gabarit à une modalité ;
- transformer les exemples d'usage des gabarits en règles d'exclusivité ;
- multiplier les règles périphériques ;
- renforcer des explications générales déjà correctement maîtrisées par le modèle lorsqu'elles peuvent être déplacées dans le glossaire ;
- interdire toute nouveauté ;
- interdire toute notation ;
- refuser toute preuve externe ;
- rendre le skill plus rigide par principe ;
- redéfinir en profondeur la portée pédagogique ou probante du format `Recul`.

Le format `Recul` reste une activité de réflexivité pouvant notamment aider l'apprenant à expliciter ce qu'il a appris et réalisé, à préparer la manière de l'expliquer à un jury et à envisager son transfert dans le métier. Son approfondissement théorique et l'extension de ses usages relèvent d'une version ultérieure.

La V2 vise à rendre le produit **plus cohérent, plus lisible, plus fiable et mieux protégé**, sans changer sa promesse fonctionnelle.

---

# 13. Perspective V3

La V3 pourra notamment enrichir la bibliothèque avec des activités plus diverses et variées.

Cette extension devra respecter l'architecture stabilisée en V2 :

```text
Module
→ Séquence
→ Séance
→ Activité
→ choix d'un gabarit adapté
```

Chaque nouveau gabarit devra :

- partir du socle commun d'une activité ;
- le compléter, le préciser ou l'adapter selon sa finalité ;
- exposer dans son front matter des métadonnées suffisantes pour orienter l'agent vers son usage ;
- documenter quelques usages types sans créer d'exclusivité artificielle ;
- définir son contrat et ses contrôles avant livraison ;
- être protégé par un test de conformité A uniquement.

L'objectif est qu'en V3 l'enrichissement de la bibliothèque puisse se faire principalement en ajoutant ou en faisant évoluer des gabarits auto-descriptifs, **sans gonfler le noyau d'une nouvelle logique de routage à chaque ajout**.

La V2 prépare donc une architecture extensible ; la V3 pourra l'enrichir sans remettre en cause le noyau.
