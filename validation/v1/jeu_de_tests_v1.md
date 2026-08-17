# Jeu de tests précis — Skill « tuteur-ingenierie-pedagogique » pour Claude

## 0. Objectif du jeu de tests

Ce jeu de tests sert à vérifier que le skill `tuteur-ingenierie-pedagogique` **modifie effectivement le comportement de Claude** et ne se contente pas d'énoncer de bonnes intentions pédagogiques.

Le test porte donc sur le comportement observable du modèle :

- identification des notions mobilisées ;
- distinction entre notion exposée et notion attestée ;
- suivi du palier **par notion** ;
- respect du **budget de nouveauté = 1** pour les activités évaluées ;
- distinction entre exposition/démonstration et activité évaluée ;
- alignement objectif → tâche → critère ;
- respect des formats ;
- posture andragogique ;
- prise en compte de la modalité ;
- gestion de l'état des paliers ;
- absence de fausse persistance ;
- signalement des contradictions entre fichiers.

---

# 1. Protocole général

## 1.1 Conditions de test

Chaque test doit être exécuté :

1. dans une conversation neuve ;
2. avec le skill `tuteur-ingenierie-pedagogique` activé ;
3. avec les fichiers du skill accessibles ;
4. sans donner à Claude la réponse attendue ;
5. avec la formulation exacte du prompt indiquée ci-dessous.

Pour les tests de suivi d'état, plusieurs messages successifs sont nécessaires. Ils constituent alors **un seul scénario de test**.

## 1.2 Ce qui est évalué

On ne cherche pas à obtenir une formulation exacte.

On vérifie des **invariants comportementaux**.

Chaque test est classé :

- **PASS** : tous les invariants obligatoires sont respectés ;
- **PARTIAL** : le comportement va dans la bonne direction mais un invariant secondaire manque ;
- **FAIL** : Claude produit ou recommande directement le comportement interdit.

## 1.3 Règle importante

Un résultat doit être évalué sur le comportement, pas sur le fait que Claude cite ou non les noms `A1`, `A2`, `A3`.

Le modèle peut appliquer correctement une règle sans la nommer.

---

# 2. Matrice de couverture

| ID | Domaine | Règle principalement testée | Priorité |
|---|---|---|---|
| T01 | Déclenchement | Activation du skill | P0 |
| T02 | A1 | Démonstration libre | P0 |
| T03 | A1 | Pair-programming guidé | P0 |
| T04 | A1 | Activité évaluée = contrainte | P0 |
| T05 | A2 | Palier par notion | P0 |
| T06 | A2 | Preuve ≠ impression | P0 |
| T07 | A2 | Quiz plafonné à 2 | P0 |
| T08 | A3 | Une notion nouvelle | P0 |
| T09 | A3 | Trois nouveautés : refus/découpage | P0 |
| T10 | A3 | Une nouveauté + prérequis attestés | P0 |
| T11 | A3 | Faux positif : notion non nouvelle | P0 |
| T12 | 3C | Alignement objectif/critère | P0 |
| T13 | Formats | Activité vs Atelier | P1 |
| T14 | Formats | Quiz d'auto-positionnement | P1 |
| T15 | Modalité | Synchrone vs asynchrone | P1 |
| T16 | Andragogie | Posture face à l'erreur | P1 |
| T17 | Andragogie | Ancrage concret | P1 |
| T18 | Tutoriel direct | Élicitation avant exposition | P0 |
| T19 | État | Mise à jour après preuve | P0 |
| T20 | État | Redescente d'un palier | P1 |
| T21 | Persistance | Ne pas inventer une persistance | P0 |
| T22 | Contradiction | Signaler une contradiction | P1 |
| T23 | Paliers | Ne pas imposer Bloom comme barrière absolue | P1 |
| T24 | Robustesse | Cas fondateur middleware | P0 |

---

# 3. Tests détaillés

## T01 — Déclenchement sur demande pédagogique

### But

Vérifier que Claude adopte le comportement du skill lorsqu'on lui demande de concevoir une activité pédagogique.

### Prompt exact

```text
Je forme des développeurs Python adultes.
Crée-moi un exercice de 15 minutes pour leur apprendre les décorateurs Python.
```

### Attendus obligatoires

Claude ne doit pas produire immédiatement un exercice évalué complet comme si le niveau de l'apprenant était connu.

Il doit au minimum chercher à établir :

- le niveau de départ ;
- la notion précise concernée ;
- le palier visé ;
- les éventuelles notions préalables.

Il peut proposer une activité de découverte/exposition sans preuve préalable, mais ne doit pas présenter une activité évaluée comme si la maîtrise était déjà attestée.

### FAIL

> « Voici un exercice : écrivez votre propre décorateur Python... »

sans aucune vérification ou hypothèse explicite sur les notions préalables.

---

# 4. Tests A1 — Périmètre des contraintes

## T02 — Une démonstration peut introduire une notion nouvelle

### But

Vérifier qu'A1 n'est pas interprété comme une interdiction d'exposer une notion nouvelle.

### Prompt exact

```text
L'apprenant n'a jamais vu les décorateurs Python.
Montre-lui un exemple concret de décorateur déjà écrit et explique ce qu'il fait.
Ne lui demande pas de produire du code.
```

### Attendus

Claude doit pouvoir :

- présenter le concept ;
- utiliser un exemple ;
- expliquer le fonctionnement ;
- éventuellement partir d'un problème concret.

Il ne doit pas refuser au motif que le décorateur n'est pas attesté.

### FAIL

> « Je ne peux pas parler des décorateurs car cette notion n'est pas encore attestée. »

---

## T03 — Pair-programming guidé libre

### Prompt exact

```text
L'apprenant ne connaît pas encore les décorateurs.
Fais un pair-programming guidé : tu écris le décorateur avec lui et tu lui expliques chaque étape.
```

### Attendus

Claude peut accompagner la construction, donner les lignes suivantes et expliquer.

Mais cette activité ne doit pas être présentée comme une preuve autonome du palier 3.

### FAIL

Claude affirme que cette séance suffit à attester « Appliquer » simplement parce que le code fonctionne.

---

## T04 — Une activité évaluée est soumise aux contraintes

### Prompt exact

```text
L'apprenant n'a jamais utilisé les décorateurs Python.
Donne-lui une activité évaluée dans laquelle il doit écrire seul un décorateur.
```

### Attendus

Claude doit :

1. identifier que l'activité est évaluée ;
2. considérer la notion comme non attestée ;
3. ne pas faire comme si le palier était acquis ;
4. proposer une étape préalable ou une activité adaptée ;
5. si une nouvelle notion est introduite, respecter le budget de nouveauté.

### FAIL

Donner directement l'exercice autonome comme si l'exposition précédente suffisait.

---

# 5. Tests A2 — Palier attaché à une notion

## T05 — Pas de « niveau global » de l'apprenant

### Contexte fourni

```text
État connu :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonctions Python | 3. Appliquer | activité F3 : fonction écrite et 5 tests passent | aujourd'hui |
| décorateurs Python | 0 | notion identifiée mais aucune preuve | aujourd'hui |
```

### Prompt exact

```text
Quel est le niveau de l'apprenant ?
Et peut-il écrire un décorateur Python ?
```

### Attendus

Claude doit répondre de manière **notionnelle**, par exemple :

- fonctions Python : palier 3 ;
- décorateurs Python : palier 0.

Il ne doit pas répondre :

> « L'apprenant est niveau 3. »

Concernant le décorateur, il doit distinguer le niveau de la notion de celui des fonctions.

### FAIL

Attribuer un niveau global à l'apprenant.

---

## T06 — Une impression n'est pas une preuve

### Contexte

```text
L'apprenant a dit :
« Oui, je comprends les décorateurs. »
```

### Prompt exact

```text
Peux-tu maintenant inscrire « décorateurs Python — palier 3 — validé » dans l'état des paliers ?
```

### Attendus

Refus ou correction.

Claude doit expliquer que la reconnaissance verbale ne suffit pas à attester le palier 3.

Il peut proposer une activité ou une preuve appropriée.

### FAIL

Ajouter directement :

> décorateurs Python | 3. Appliquer | l'apprenant dit comprendre

---

## T07 — Un quiz ne peut pas attester le palier 3

### Contexte

```text
L'apprenant a obtenu 10/10 à un QCM sur les décorateurs Python.
```

### Prompt exact

```text
Mets à jour son état des paliers et considère qu'il sait maintenant appliquer les décorateurs Python.
```

### Attendus

Claude doit limiter la preuve du quiz aux paliers 1 ou 2.

Il peut attester au maximum un niveau de compréhension compatible avec les questions posées.

Il doit demander une production pour attester « Appliquer ».

### FAIL

> « 10/10 au quiz = palier 3 validé. »

---

# 6. Tests A3 — Budget de nouveauté

## T08 — Une seule notion nouvelle est acceptable

### Contexte

```text
État :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonction Python | 3. Appliquer | activité F1 réussie | J1 |
| paramètres de fonction | 3. Appliquer | activité F2 réussie | J1 |
| tests unitaires | 3. Appliquer | activité T1 réussie | J2 |
| décorateurs Python | 0 | aucune preuve | J2 |
```

### Prompt exact

```text
Crée une activité évaluée où l'apprenant doit utiliser une fonction existante
pour lui ajouter un décorateur Python simple.
```

### Attendus

Claude doit identifier :

- fonction existante : attestée ;
- paramètres : attestés si mobilisés ;
- tests unitaires : attestés s'ils sont nécessaires ;
- décorateur : non attesté.

Il doit conclure que le budget de nouveauté est de **1**.

L'activité peut donc être acceptable si elle ne mobilise pas d'autre notion non attestée.

### PASS fort

Claude affiche explicitement les notions mobilisées et leur état avant l'activité.

---

## T09 — Trois notions nouvelles : activité interdite telle quelle

### Prompt exact

```text
L'apprenant n'a jamais utilisé les décorateurs Python.

Donne-lui cette activité évaluée :

« Écris ton propre middleware LangChain en héritant de la classe de base,
utilise le décorateur approprié et configure la clé de redirection du graphe. »
```

### Attendus

Claude doit refuser l'activité **telle quelle** ou la découper.

Il doit identifier les différentes notions nouvelles.

Le cas fondateur documenté dans le skill doit être détecté comme un cas de budget de nouveauté dépassé.

### FAIL critique

Claude fournit directement l'activité.

### PASS fort

Claude propose un découpage du type :

1. notion A ;
2. notion B ;
3. notion C ;

avec une activité évaluée par étape.

---

## T10 — Une nouveauté + prérequis attestés

### Contexte

```text
État :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonctions Python | 3. Appliquer | activité F1 | J1 |
| paramètres | 3. Appliquer | activité F2 | J1 |
| tests | 3. Appliquer | activité T1 | J1 |
| décorateur Python | 0 | aucune preuve | J2 |
```

### Prompt exact

```text
Crée une activité évaluée :
« À partir de cette fonction et de ces tests fournis,
ajoute un décorateur simple qui journalise l'appel. »
```

### Attendus

Cette activité doit être considérée comme potentiellement valide au regard d'A3 :

- une seule notion non attestée : décorateur ;
- les autres notions nécessaires sont attestées.

Claude doit toutefois vérifier que le palier demandé correspond bien à la tâche.

---

## T11 — Faux positif : une notion n'est pas « nouvelle » parce qu'elle porte un nouveau nom

### Contexte

```text
État :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonctions Python | 3. Appliquer | plusieurs fonctions produites avec tests | J1 |
```

### Prompt exact

```text
L'activité demande simplement :
« Écris une fonction Python qui prend deux nombres et retourne leur somme. »

Est-ce une nouvelle notion ?
```

### Attendus

Claude ne doit pas compter « écrire une fonction » comme une nouvelle notion si la notion de fonction est déjà attestée au palier requis.

Il doit raisonner sur la **notion**, pas sur le fait que l'exercice soit nouveau.

---

# 7. Tests d'alignement 3C

## T12 — Critère désaligné avec le palier

### Prompt exact

```text
Crée une activité dont l'objectif est :
« Expliquer avec ses propres mots ce qu'est une fonction Python. »

Le critère de réussite sera :
« L'apprenant écrit seul une fonction fonctionnelle avec trois tests. »
```

### Attendus

Claude doit détecter le désalignement.

Objectif :

- Comprendre.

Critère :

- Appliquer.

Il doit corriger le critère ou changer le palier visé.

### FAIL

Accepter la fiche telle quelle.

---

# 8. Tests de format

## T13 — Activité versus Atelier

### Prompt exact

```text
Crée une activité asynchrone dans laquelle l'apprenant :
1. analyse le problème ;
2. choisit une solution ;
3. implémente ;
4. teste ;
5. rédige un court bilan.

La production doit durer environ 2 heures.
```

### Attendus

Claude doit reconnaître qu'il ne s'agit pas d'une petite Activité.

Le format attendu est **Atelier**.

Il doit utiliser les huit sections du gabarit `atelier.md`, dans l'ordre.

### FAIL

Produire une fiche d'Activité de 5 à 15 minutes.

---

## T14 — Quiz d'auto-positionnement

### Prompt exact

```text
Crée un quiz d'auto-positionnement Python avant une séquence sur les décorateurs.
```

### Attendus obligatoires

Le quiz doit :

- être présenté comme non noté ;
- contenir 8 à 12 questions ;
- avoir une seule bonne réponse par question ;
- utiliser des situations concrètes ;
- fournir un feedback après chaque question ;
- rester aux paliers 1 et 2 ;
- ne pas utiliser de question piège ;
- proposer une clôture indiquant quoi faire du résultat.

### FAIL critique

Un quiz qui prétend certifier le palier 3.

---

# 9. Test de modalité

## T15 — Synchrone versus asynchrone

### Prompt A

```text
Je veux construire une formation synchrone en présentiel.
Découpe une séquence de 3 heures.
```

### Attendus

Le découpage doit pouvoir inclure :

**Séquence → Séance → Activité**

La Séance est pertinente en modalité synchrone.

### Prompt B

```text
Je veux construire la même formation entièrement asynchrone.
Découpe une séquence de 3 heures.
```

### Attendus

La Séance ne doit pas être introduite comme unité obligatoire.

Le découpage doit privilégier :

**Séquence → Atelier / Quiz / Recul**

### FAIL

Produire exactement le même découpage pour les deux modalités.

---

# 10. Tests andragogiques

## T16 — Gestion professionnelle de l'erreur

### Prompt exact

```text
L'apprenant écrit :

def total(prix, quantite):
    return prix + quantite

alors que le besoin est de calculer un prix total.

Réponds-lui comme tuteur.
```

### Attendus

Claude ne doit pas répondre :

> « C'est faux. »

Il doit diagnostiquer le problème, par exemple en faisant remarquer la relation entre prix, quantité et opération attendue.

La réponse doit rester professionnelle et non infantilisante.

---

## T17 — Ancrage concret

### Prompt exact

```text
Explique les décorateurs Python à un développeur adulte qui travaille sur une application de réservation.
```

### Attendus

Claude doit ancrer immédiatement la notion dans un problème concret.

Il peut utiliser par exemple :

- journalisation ;
- authentification ;
- mesure du temps ;
- contrôle d'accès.

Il doit éviter un exemple abstrait du type :

```python
class Truc:
    ...
```

---

# 11. Tests du tutorat en direct

## T18 — Élicitation avant exposition

### Prompt exact

```text
Je suis développeur PHP et je veux apprendre les décorateurs Python.
Commence la séance.
```

### Attendus

Claude doit privilégier une question diagnostique ouverte avant de déverser un cours complet.

Exemple de comportement acceptable :

> « Avant de partir sur Python, comment tu utiliserais aujourd'hui en PHP un mécanisme qui ajoute un comportement autour d'une fonction sans modifier son code ? »

Le modèle peut ensuite exploiter la réponse.

### FAIL

Commencer immédiatement par un long cours théorique sans chercher à connaître le point de départ.

---

# 12. État des paliers

## T19 — Mise à jour après preuve

### Contexte

```text
État avant activité :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonction Python | 2. Comprendre | reformulation correcte | J1 |
| décorateur Python | 0 | aucune preuve | J1 |
```

### Prompt exact

```text
L'apprenant réalise l'activité D1.
Il écrit un décorateur qui journalise correctement les appels.
Les 4 tests fournis passent.

Mets à jour l'état des paliers.
```

### Attendus

Claude doit :

- mettre à jour la ligne décorateur ;
- associer un palier compatible avec l'activité ;
- citer une preuve concrète ;
- conserver les autres lignes ;
- afficher l'état mis à jour.

Il ne doit pas écrire :

> « décorateurs : bonne compréhension »

mais référencer l'activité et ses critères.

---

## T20 — Redescente d'un palier

### Contexte

```text
État :

| Notion | Palier attesté | Preuve | Quand |
|---|---|---|---|
| fonctions Python | 3. Appliquer | activité F1 réussie | J1 |
```

### Prompt exact

```text
Lors d'une nouvelle activité, l'apprenant n'arrive plus à écrire
une fonction simple sans aide et échoue sur les deux cas de test.

Que fais-tu de l'état des paliers ?
```

### Attendus

Claude doit accepter la possibilité de **redescendre le palier attesté**.

Il doit traiter cette information comme une donnée diagnostique, pas comme une sanction.

---

# 13. Persistance

## T21 — Ne pas inventer une persistance

### Prompt exact

```text
Nous avons travaillé hier sur mon état des paliers.
Tu dois t'en souvenir.

Quelle est la liste exacte de mes notions et de mes paliers attestés ?
```

### Attendus

Si aucun état persistant n'est effectivement disponible, Claude ne doit pas inventer les données.

Il doit :

- signaler qu'il ne dispose pas de l'état ;
- demander le fichier ou le tableau ;
- ou proposer de repartir de l'état fourni.

### FAIL critique

Inventer un état des paliers à partir de suppositions.

---

# 14. Test de contradiction documentaire

## T22 — Contradiction entre deux fichiers

### But

Vérifier la directive :

> « Pour toute autre contradiction rencontrée entre deux fichiers en usage réel : ne pas trancher silencieusement, la signaler. »

### Mise en place

Créer volontairement une copie de l'un des fichiers du skill avec une contradiction explicite.

Exemple :

`test-contradiction.md`

```text
Une Activité peut viser deux paliers cognitifs simultanément.
```

### Prompt exact

```text
À partir des fichiers disponibles, rédige une activité conforme au skill.
```

### Attendus

Claude doit signaler la contradiction au lieu de choisir silencieusement une règle.

### FAIL

Appliquer une version sans signaler qu'une contradiction existe.

---

# 15. Test sur l'ordre des paliers

## T23 — Bloom n'est pas une barrière absolue

### Prompt exact

```text
L'apprenant doit comprendre pourquoi son API Python renvoie une erreur 422.
Il ne sait pas encore expliquer précisément le fonctionnement de Pydantic.

Je lui donne un bug réel à diagnostiquer.

Le skill m'autorise-t-il à commencer par une activité d'analyse ?
```

### Attendus

Claude doit reconnaître que l'ordre Bloom est une **heuristique**, pas une barrière séquentielle absolue.

Il doit pouvoir utiliser une situation d'analyse comme point d'entrée, notamment dans l'esprit andragogique du skill.

Il doit en revanche distinguer cette exploration d'une validation formelle d'un palier supérieur.

### FAIL

> « Non, il doit obligatoirement passer par les niveaux 1, 2 puis 3 avant toute analyse. »

---

# 16. Test fondateur — Middleware

## T24 — Reproduction du bug d'origine

### Contexte exact

```text
L'apprenant est développeur Python mais n'a jamais utilisé
les middlewares LangChain.

Il sait utiliser une classe Python existante.
Il sait utiliser des fonctions Python.
Il sait lire du code.

Il ne connaît pas :
- l'héritage de la classe de base du middleware ;
- le décorateur de contrôle de flux ;
- la clé de redirection du graphe.
```

### Prompt exact

```text
Explique les middlewares LangChain puis donne immédiatement
une spécification complète :

« Écris ton propre middleware qui hérite de la classe de base,
utilise le décorateur approprié et configure la clé de redirection du graphe. »

Je veux une activité évaluée et autonome.
```

### Attendus

C'est le test le plus important.

Claude doit reconnaître que l'activité finale mobilise plusieurs notions non attestées.

Il doit donc :

- refuser l'activité telle quelle ;
- expliciter les notions manquantes ;
- découper l'apprentissage ;
- introduire les notions progressivement ;
- éventuellement conserver l'exemple initial comme exposition ;
- ne pas confondre « avoir vu un middleware » et « savoir en écrire un ».

### FAIL CRITIQUE

Si Claude produit directement la spécification demandée, le garde-fou central du skill ne fonctionne pas.

---

# 17. Tests complémentaires de robustesse

## T25 — Reformulation sans mots-clés

### Prompt exact

```text
L'apprenant sait faire des fonctions simples et des tests.

Je voudrais qu'il construise seul un mécanisme qui ajoute automatiquement
un comportement avant et après l'exécution d'une fonction.

Fais-moi une activité évaluée.
```

### But

Le prompt ne dit jamais « décorateur ».

### Attendu

Claude doit identifier la notion réelle mobilisée et appliquer A2/A3.

Ce test vérifie que le modèle applique les règles **sémantiquement**, et pas uniquement par recherche de mots comme « décorateur », « palier » ou « notion nouvelle ».

---

## T26 — Même compétence, vocabulaire différent

### Prompt exact

```text
L'apprenant sait écrire et tester une fonction Python.

Propose une tâche où il doit créer une nouvelle fonction qui reçoit
deux nombres et retourne leur produit.
```

### Attendu

Ne pas considérer automatiquement cette tâche comme une nouvelle notion.

Le modèle doit distinguer :

- nouvelle tâche ;
- nouvelle notion.

---

## T27 — Demande d'exercice « très difficile »

### Prompt exact

```text
Je veux un exercice très difficile pour un débutant.
Il doit utiliser FastAPI, SQLAlchemy, Pydantic, async et Docker.
Fais-le en une seule activité évaluée.
```

### Attendu

Claude doit résister à la demande de difficulté artificielle.

Il doit analyser les notions mobilisées et détecter un budget de nouveauté manifestement dépassé si elles ne sont pas attestées.

---

## T28 — Demande de solution avant production

### Prompt exact

```text
Crée une fiche d'activité avec l'énoncé et, juste sous l'énoncé,
mets la solution complète pour que l'apprenant puisse vérifier
pendant qu'il travaille.
```

### Attendu

Le modèle doit maintenir la séparation :

- volet apprenant ;
- volet formateur/interne.

La solution et les critères d'acceptation ne doivent pas être mélangés avec ce qui est remis à l'apprenant si la fiche respecte le gabarit.

---

# 18. Test de stabilité des formats

## T29 — Atelier avec les huit sections

### Prompt exact

```text
Crée un Atelier asynchrone sur les tests unitaires en Python.
```

### Attendus

Les sections doivent apparaître exactement dans cet ordre :

1. Documents fournis
2. Objectifs de l'atelier
3. Durée estimée
4. Organisation et outils
5. Méthode proposée
6. Ce qui est supposé par défaut
7. Livrable attendu
8. Critère simple

Le contenu peut être différent, mais l'architecture doit rester stable.

---

# 19. Test de non-surproduction

## T30 — Respect du périmètre demandé

### Prompt exact

```text
Rédige uniquement une fiche de Séance de 45 minutes
sur la validation des données avec Pydantic.
```

### Attendus

Claude ne doit pas produire :

- le module complet ;
- toute la séquence ;
- un syllabus ;
- plusieurs fiches d'activité complètes.

La réponse doit rester centrée sur la Séance demandée.

---

# 20. Grille de notation

## 20.1 Score par test

Chaque test P0 ou P1 reçoit :

- **2 points** : comportement conforme à tous les invariants ;
- **1 point** : comportement globalement correct mais incomplet ;
- **0 point** : comportement contraire au skill.

Les tests P0 sont les tests critiques.

### Score maximal

30 tests × 2 = **60 points**.

### Interprétation proposée

| Score | Interprétation |
|---:|---|
| 57–60 | Excellent — comportement très robuste |
| 52–56 | Très bon — quelques écarts secondaires |
| 45–51 | Correct — garde-fous présents mais fragiles |
| 35–44 | Insuffisant — plusieurs règles ne sont pas fiables |
| < 35 | Échec — le skill n'impose pas suffisamment son comportement |

## 20.2 Règle spécifique aux tests critiques

Indépendamment du score global :

> **Un FAIL critique sur T09 ou T24 doit être considéré comme un échec fonctionnel du cœur du skill.**

Pourquoi ?

Parce que ces tests vérifient directement la raison historique de création du skill :

**empêcher Claude de transformer une exposition superficielle en activité autonome mobilisant plusieurs notions non attestées.**

---

# 21. Test comparatif recommandé : Claude avec / sans skill

Pour démontrer l'efficacité du dispositif, exécuter au minimum les tests :

- T09 ;
- T12 ;
- T14 ;
- T18 ;
- T24 ;
- T25 ;
- T27.

Une première fois **sans le skill**.

Une deuxième fois **avec le skill**.

Comparer :

| Critère | Sans skill | Avec skill |
|---|---|---|
| Notions mobilisées explicitées | | |
| État des paliers pris en compte | | |
| Budget A3 respecté | | |
| Activité refusée si nécessaire | | |
| 3C alignés | | |
| Posture andragogique | | |
| Format respecté | | |

Le résultat recherché n'est pas nécessairement que la réponse « avec skill » soit plus longue.

Le résultat recherché est qu'elle soit **plus contrainte et plus diagnostique**.

---

# 22. Test métamorphique particulièrement important

Un excellent test de robustesse consiste à changer **un seul paramètre** d'un scénario et vérifier que le comportement change uniquement lorsque ce paramètre le justifie.

### Version A

```text
L'apprenant ne connaît pas les décorateurs Python.
Il connaît les fonctions et les tests.
Crée une activité évaluée pour ajouter un décorateur.
```

Attendu :

**acceptable au regard d'A3**, si le palier et les autres notions sont cohérents.

### Version B

Modifier uniquement :

```text
L'apprenant ne connaît pas les décorateurs Python
et ne connaît pas non plus les fonctions Python.
```

Attendu :

**activité refusée ou découpée**, car deux notions non attestées sont maintenant mobilisées.

### Version C

Modifier uniquement :

```text
L'apprenant connaît les décorateurs Python au palier 3.
```

Attendu :

Le décorateur ne doit plus être compté comme nouveauté.

Ce test permet de vérifier que le modèle **calcule réellement à partir de l'état fourni**, plutôt que d'appliquer mécaniquement une interdiction.

---

# 23. Les cinq tests à absolument réussir

Si le temps de test est limité, retenir :

### 1. T24 — Cas fondateur middleware

**Question :** Claude reproduit-il le bug historique ?

### 2. T09 — Trois nouveautés

**Question :** Claude bloque-t-il réellement A3 ?

### 3. T07 — Quiz → palier

**Question :** Claude évite-t-il de transformer un QCM en preuve de production ?

### 4. T06 — Impression → preuve

**Question :** Claude distingue-t-il une affirmation de l'apprenant d'une preuve ?

### 5. T18 — Élicitation

**Question :** Claude sait-il utiliser le dialogue pour diagnostiquer plutôt que supposer ?

---

# 24. Conclusion du jeu de tests

Le succès du skill ne doit pas être évalué à la qualité littéraire de ses réponses.

Le critère central est :

> **Claude prend-il des décisions différentes lorsqu'une contrainte pédagogique pertinente change ?**

Le test le plus convaincant est donc celui où une modification minime de l'état de l'apprenant provoque une modification cohérente de la réponse du modèle.

Le comportement recherché est :

```text
Demande
   ↓
Identification des notions
   ↓
État des paliers par notion
   ↓
Détermination de ce qui est attesté
   ↓
Comptage des nouveautés
   ↓
Vérification du palier visé
   ↓
Vérification 3C
   ↓
Choix du format
   ↓
Production
```

Et non :

```text
Demande
   ↓
Génération immédiate d'une activité plausible
```

C'est cette différence que le jeu de tests doit permettre de démontrer.
