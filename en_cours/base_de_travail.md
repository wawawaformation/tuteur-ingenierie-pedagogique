# Base de travail — de la V2 vers la V3

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-08-23  
**Statut :** base de travail actuelle

---

## 1. Idée générale

On repart de la **V2**, parce qu’elle est validée et qu’elle constitue notre base fiable.

On ne cherche pas à nettoyer la V3 expérimentale telle quelle.

La V3 expérimentale nous sert surtout à récupérer :

- les bonnes idées ;
- les comportements qui ont bien fonctionné ;
- les formulations doctrinales utiles ;
- les erreurs à ne pas reproduire.

La reconstruction se fera en deux temps :

```text
V2
→ V2.1 : noyau légèrement corrigé et allégé
→ V3 : tutorat amélioré
```

---

# 2. Principe principal

> **Doctrine avant procédure.**

Avant d’ajouter une règle, un gate, une séquence ou un contrôle, on doit d’abord savoir clairement :

1. quel principe pédagogique on veut défendre ;
2. pourquoi ce principe est important ;
3. quel comportement permet de voir s’il est respecté ;
4. seulement ensuite, quelle procédure minimale peut aider le modèle à l’appliquer.

On évite donc :

```text
un comportement nous gêne
→ on ajoute un gate
→ puis un autre
→ puis une exception
→ puis on essaie de justifier le tout
```

C’est précisément ce qui a commencé à alourdir la V3 expérimentale.

---

# 3. Les doctrines que l’on veut conserver

## 3.1 Partir de l’apprenant

Le tutorat part :

- de l’objectif réel de l’apprenant ;
- de ce qu’il sait réellement sur les prérequis utiles ;
- du chemin le plus court et le plus pertinent vers son objectif.

On ne déroule pas un programme générique si ce n’est pas nécessaire.

---

## 3.2 Déclaration et preuve

Quelques règles doivent rester très claires :

> **Déclaration ≠ preuve.**

> **Manque de preuve ≠ preuve de manque.**

Une personne peut dire :

> « J’ai déjà utilisé l’injection de dépendances. »

Cela peut orienter le diagnostic, mais cela ne suffit pas à prouver un palier d’application.

Inversement :

> « Je n’ai jamais utilisé cette notion. »

ne prouve pas à lui seul une incapacité.

La preuve doit rester limitée à ce qui est réellement observable.

---

## 3.3 Une preuve ne vaut que pour ce qu’elle montre

On ne doit pas transformer une réussite générale en maîtrise de tout ce qui a été mobilisé.

Exemples :

```text
utiliser ≠ créer
exécuter ≠ écrire
lire ≠ produire
modifier ≠ concevoir
```

Si une personne réussit une tâche, on atteste uniquement ce que cette tâche permet réellement de démontrer.

---

## 3.4 Attestation explicite du formateur

C’est une évolution à intégrer dans le **noyau V2.1** :

> **Une attestation explicite d’un palier par un formateur identifié fait foi.**

Il faut distinguer quatre choses :

1. **l’apprenant déclare** quelque chose sur lui-même ;
2. **l’apprenant agit** et produit une performance observable ;
3. **le formateur rapporte une observation précise** ;
4. **le formateur atteste explicitement une notion à un palier donné**.

Ces quatre sources n’ont pas la même valeur.

Exemple :

> « Je pense qu’il maîtrise bien cette notion. »

n’est pas encore une attestation précise.

En revanche :

> « J’atteste explicitement l’injection de dépendances par constructeur au palier 3 — Appliquer. »

est une décision pédagogique explicite du formateur et doit être enregistrée comme telle.

Cette évolution doit avoir un **NOY dédié** avant de considérer V2.1 comme stabilisée.

---

# 4. Ce qui appartient au tutorat, pas au noyau

Nous avons décidé de sortir **P01** du noyau général.

P01 est une règle de tutorat :

> **Établir le point de départ utile avant de prendre une décision pédagogique qui en dépend.**

Autrement dit :

si le tuteur reconnaît qu’une information peut changer la suite, il ne doit pas continuer en inventant ou en supposant la réponse.

Exemple de mauvais comportement :

```text
« Ta réponse va déterminer la suite. »

→ le tuteur pose la question

→ il n’attend pas la réponse

→ « En attendant, je pars du principe que tu connais déjà X. »
```

Le problème n’est pas qu’il ait expliqué quelque chose.

Le problème est qu’il a pris une décision qui dépendait d’une information qu’il n’avait pas encore.

P01 sera donc traité dans la **promesse tutorat V3**, pas comme une règle générale du noyau V2.1.

---

# Axes de travail V3

Distinct de la liste de propriétés candidates du §12 : il s'agit ici de grands axes de travail, pas encore de règles ni de propriétés de promesse.

- Travailler le volet tutorat.
- Travailler les activités possibles (ex. : pouvoir ajouter une activité sans devoir modifier le noyau).
- Travailler sur la psychologie cognitive et les biais cognitifs (voir [`dossier-pedagogique/psychologie_cognitive_formation_tutorat.md`](../dossier-pedagogique/psychologie_cognitive_formation_tutorat.md)).

Cette liste n'est pas encore développée ni priorisée.

---

# 5. Les règles fortes du futur tutorat V3

Ces idées viennent du travail expérimental déjà réalisé.

Elles devront être triées et testées avant d’être réimplémentées.

## 5.1 Diagnostic minimal

On ne cherche pas à tout savoir sur l’apprenant.

On cherche uniquement les informations qui peuvent changer la suite.

Quand on en sait assez pour choisir la prochaine étape, on arrête le diagnostic.

---

## 5.2 Pas de plan détaillé trop tôt

Si une information importante manque encore, on ne construit pas un plan détaillé comme si cette information était connue.

Une fois le point de départ suffisamment établi :

1. on met à jour l’état des paliers ;
2. on construit le repère de progression ;
3. on le présente à l’apprenant ;
4. on attend sa validation avant de démarrer.

---

## 5.3 Chemin minimal

Le repère de progression n’est pas un catalogue du sujet.

Il doit être :

> **le chemin minimal pertinent entre le point de départ réel et l’objectif réel.**

Une notion intéressante mais non nécessaire n’a pas à être ajoutée automatiquement.

---

## 5.4 Une nouveauté = une activité

Le tutorat doit être très progressif.

> **Une nouveauté = une activité.**

Si une notion est nouvelle pour l’apprenant, on évite de lui demander de gérer en même temps plusieurs autres nouveautés.

Les éléments périphériques doivent autant que possible être :

- déjà connus ;
- fournis ;
- guidés ;
- ou neutralisés.

Cette règle de tutorat ne doit pas être confondue avec A3 de la V2, qui concerne le budget de nouveauté d’une activité évaluée.

---

## 5.5 Les exemples doivent être expliqués

Un exemple ne doit pas être simplement posé devant l’apprenant.

Le tuteur doit préciser :

- ce qu’il faut regarder ;
- ce que l’exemple illustre ;
- pourquoi il est présenté à ce moment-là.

---

## 5.6 La théorie doit servir quelque chose

On n’ajoute pas de théorie uniquement parce qu’elle est intéressante.

Elle doit avoir une fonction utile :

- comprendre ;
- éviter une erreur ;
- transférer ;
- devenir plus autonome.

---

## 5.7 Le tutorat doit s’adapter

Le plan n’est pas figé.

On avance :

```text
activité
→ observation
→ mise à jour de ce que l’on sait
→ adaptation éventuelle de la suite
```

## 5.8 Utiliser les activités déjà disponibles

Le tuteur dispose d’une boîte à outils dans `activites_type/`.

> **Lorsqu’une activité existante est adaptée à l’objectif et à l’étape en cours, le tuteur n’hésite pas à l’utiliser.**

Il n’a pas besoin de réinventer systématiquement une activité si un type déjà disponible convient.

La logique est :

```text
objectif de l’apprenant
→ étape actuelle
→ activité pertinente
→ si un type adapté existe dans activites_type/, s’en servir
→ sinon construire une activité adaptée
```

Ce n’est pas une obligation mécanique.

Le tuteur ne choisit pas une activité simplement parce qu’elle existe dans `activites_type/`.

L’activité reste au service :

- de l’objectif réel ;
- du point de départ de l’apprenant ;
- de la progression ;
- de la doctrine du tutorat.

`activites_type/` est donc une **boîte à outils**, pas un catalogue à dérouler.

---

# 6. Noyau et règles spécifiques au tutorat

Le **noyau** contient les règles générales.

`tutorat.md` contient les règles spécifiques au tutorat.

Une fois V2.1 stabilisée, on souhaite toucher le moins possible au noyau.

## 6.1 Le noyau doit autoriser explicitement les dérogations locales

Il ne suffit pas d’écrire dans `tutorat.md` qu’une règle locale remplace une règle du noyau.

Le noyau doit lui-même préciser que ce mécanisme existe.

Une règle courte suffit, par exemple :

> **Dérogations locales**  
> Une référence spécialisée peut explicitement déroger à une règle du noyau pour son seul périmètre. Une dérogation n’est valide que si elle est signalée comme telle dans la référence spécialisée. En l’absence de dérogation explicite, le noyau prévaut.

Cette règle ne sert pas à ajouter un nouveau gate.

Elle sert uniquement à donner au modèle une règle claire pour résoudre une contradiction entre :

```text
règle générale du noyau
et
règle spécialisée du tutorat
```

Sans cette règle, le modèle pourrait arbitrer silencieusement entre les deux.

## 6.2 Marqueur uniforme dans `tutorat.md`

Chaque dérogation doit utiliser le même marqueur, par exemple :

```markdown
### Dérogation au noyau — A3

En contexte tutorat, la règle suivante remplace A3 :
...
```

ou :

```markdown
**Dérogation au noyau : A3**

En tutorat, cette règle remplace A3 :
...
```

La forme exacte sera choisie au moment de l’implémentation, mais elle devra rester uniforme.

## 6.3 Les dérogations doivent rester finies et visibles

La liste des dérogations doit être facile à retrouver et à compter.

`tutorat.md` pourra donc contenir une petite section dédiée :

```markdown
## Dérogations au noyau

- A3 : ...
- règle X : ...
```

L’objectif est que les dérogations restent :

- explicites ;
- limitées au contexte tutorat ;
- peu nombreuses ;
- faciles à auditer.

Si leur nombre devient important, cela doit être considéré comme un signal d’architecture à réexaminer.

## 6.4 Règle de priorité

La priorité devient donc :

```text
pas de dérogation explicite
→ le noyau prévaut

dérogation explicite dans tutorat.md
→ la règle tutorat prévaut
→ uniquement dans le contexte tutorat
```

Le but n’est pas de créer un système compliqué.

Le but est d’éviter les arbitrages implicites et la duplication de règles.

---

# 7. Ce que l’on récupère de la V3 expérimentale

Le diff V2 → V3 montre que tout n’est pas à jeter.

La majorité de la sédimentation est concentrée dans `references/tutorat.md`.

Plusieurs petits ajouts du noyau sont au contraire intéressants et assez propres.

## À reporter ou à retravailler pour V2.1

Notamment :

- distinction plus claire entre auto-déclaration et preuve ;
- « manque de preuve ≠ preuve de manque » ;
- palier 0 ≠ « non maîtrisé » ;
- hiérarchie des sources d’attestation ;
- attestation explicite du formateur ;
- appréciation générale du formateur ≠ attestation précise ;
- protection contre l’effet de vocabulaire riche, assurance ou fluidité ;
- cohérence de la taxonomie avec la nouvelle attestation formateur ;
- petites corrections de routage utiles.

Le tableau de hiérarchie des sources produit en V3 est particulièrement intéressant, parce qu’il est compact et doctrinal.

## À ne pas reporter tel quel

Notamment :

- gates longs et répétés ;
- même règle réécrite dans plusieurs fichiers ;
- procédures en 7 étapes quand une doctrine claire suffit ;
- contrôles tutorat dupliqués dans le noyau ;
- sections très longues de `tutorat.md` ;
- narration libre qui transforme « non attesté » en « non maîtrisé ».

L’idée est :

> **récupérer la doctrine et les bons comportements, pas la sédimentation textuelle.**

---

# 8. Ce qu’il faut faire avant V3 : construire V2.1

## 8.1 Version

La version intermédiaire sera :

> **V2.1.0**

Pourquoi ?

Parce qu’il ne s’agit pas uniquement d’un correctif de texte.

La V2.1 introduira au moins une évolution fonctionnelle du noyau :

> l’attestation explicite d’un palier par un formateur identifié.

Un simple nettoyage sans changement fonctionnel aurait plutôt été un patch `2.0.x`.

---

## 8.2 Construire V2.1 à partir de V2

On repart physiquement de la V2 stable.

On récupère aussi les fichiers de référence disparus pendant l’expérimentation, notamment :

- `promesse.md` ;
- `README.md` ;
- `VERSION` ;
- `LICENSE.md`.

Puis on reporte uniquement les petits éléments V3 que nous avons décidé de conserver.

---

## 8.3 Sortir P01 du noyau

La règle générale V2 :

> « élicitation en premier, avant d’exposer quoi que ce soit »

ne doit pas être reprise telle quelle dans le noyau V2.1 si nous décidons que P01 appartient au tutorat.

P01 sera redéfini et testé dans la future promesse V3.

---

## 8.4 Intégrer l’attestation explicite du formateur

C’est le principal changement fonctionnel du noyau V2.1.

Il faut :

1. choisir la formulation doctrinale ;
2. la mettre à une seule source normative claire ;
3. mettre les autres fichiers en cohérence ;
4. créer un NOY spécifique ;
5. stabiliser ce NOY avant de continuer.

---

## 8.5 Alléger le noyau

Une fois les règles choisies :

- supprimer les répétitions ;
- supprimer les gates qui ne font que raconter une doctrine déjà écrite ;
- garder les formulations courtes ;
- garder une seule source de vérité par règle ;
- ne pas changer la doctrine pendant l’allègement.

Pendant cette étape, ajouter au noyau **une seule règle courte de priorité** autorisant les dérogations explicites des références spécialisées. Cette règle fait partie du mécanisme d’architecture de V2.1 et évite que le modèle arbitre silencieusement entre noyau et tutorat.

---

# 9. Non-régression de V2.1

Quand V2.1 est prête, on gèle le candidat et on rejoue les tests de noyau.

Pour cette passe :

- **condition A uniquement** ;
- **une répétition par scénario** ;
- seulement les NOY qui protègent encore des règles du noyau V2.1.

Les B′ historiques n’ont pas besoin d’être rejoués : le modèle sans skill n’a pas changé.

P01 ayant quitté le noyau, **NOY001 ne doit pas être utilisé comme test de non-régression du noyau V2.1** sous sa fonction historique.

Son enseignement sera réutilisé plus tard dans les SPEC tutorat V3.

## Si un test A échoue

On ne conclut pas immédiatement à une régression.

On rejoue d’abord le scénario **deux fois**.

Ces répétitions servent à savoir si le problème est reproductible.

Elles ne servent pas à faire un vote mécanique.

Ensuite seulement, si nécessaire, on ouvre le diagnostic.

---

# 10. Méthode pour analyser un comportement douteux

On conserve la méthode qui a bien fonctionné pendant l’expérimentation V3 :

> **petit stimulus → résultat observable → méta-discussion → diagnostic → éventuelle modification**

Quand le résultat semble mauvais, on demande par exemple :

> « Pourquoi as-tu fait cela au regard du skill que tu as lu ? »

> « Quelle règle as-tu appliquée ? »

> « Quel acte as-tu réellement observé ? »

> « Quelle information estimais-tu disponible au moment de décider ? »

> « À quel moment as-tu pris cette décision ? »

Ensuite on classe le problème.

Il peut venir de :

- règle absente ;
- règle ambiguë ;
- contradiction entre règles ;
- mauvais routage ;
- règle connue mais non appliquée ;
- mauvaise classification de l’observable ;
- variance du modèle ;
- mauvais scénario ;
- environnement de test contaminé.

On ne modifie le skill qu’après ce diagnostic.

---

# 11. Ne pas modifier le test et le skill en même temps

C’est une règle méthodologique importante.

Si un oracle semble mauvais et que le skill semble mauvais également, on ne change pas les deux dans le même cycle.

La séquence doit être :

```text
doctrine claire
→ scénario / oracle dérivé de cette doctrine
→ oracle gelé
→ run
→ observation
→ diagnostic
→ éventuelle modification du skill
→ nouveau run avec le même oracle
```

Si l’oracle doit finalement être corrigé, on le corrige explicitement puis on démarre un nouveau cycle.

Cela permet de savoir ce que le test démontre réellement.

---

# 12. Avant d’implémenter V3 : définir sa promesse minimale

Une fois V2.1 stabilisée et gelée, on ne se jette pas immédiatement dans l’écriture de `tutorat.md`.

On commence par définir la **promesse minimale de V3**.

La question n’est pas :

> « Que ferait un tuteur parfait ? »

La question est :

> **« Qu’est-ce que notre skill doit obligatoirement apporter pour que le tutorat soit réellement utile et efficace ? »**

On cherche peu de propriétés, mais des propriétés importantes.

Parmi les candidates déjà identifiées :

- établir un point de départ utile ;
- ne pas prendre une décision dépendante d’une information encore inconnue ;
- construire un chemin minimal vers l’objectif ;
- progresser de manière très graduelle ;
- attendre la validation du repère avant de commencer ;
- observer puis adapter la suite ;
- conserver correctement les informations sur les paliers.

Cette liste n’est pas encore la promesse définitive.

Elle doit être réduite au minimum réellement nécessaire.

Matériau de fond disponible pour cette étape : [`dossier-pedagogique/psychologie_cognitive_formation_tutorat.md`](../dossier-pedagogique/psychologie_cognitive_formation_tutorat.md) (principes et biais cognitifs pouvant éclairer le choix des propriétés retenues).

---

# 13. Tester la promesse V3 avant de l’implémenter

Une fois la promesse minimale écrite, on crée seulement **quelques scénarios**.

Pas besoin d’une grosse campagne.

Ces scénarios doivent être :

- courts ;
- discriminants ;
- faciles à scorer ;
- directement liés à la promesse.

Ils sont joués en :

> **A / B′**

Le but est de vérifier, avant d’investir dans l’implémentation, que les comportements que nous voulons ajouter :

1. sont réellement utiles ;
2. sont observables ;
3. ne sont pas déjà produits naturellement de façon fiable sans skill ;
4. justifient donc une évolution du skill.

Si une propriété n’apporte rien ou ne discrimine pas, on peut décider de ne pas l’implémenter.

---

# 14. Ensuite seulement : implémenter V3

Quand la promesse minimale est stabilisée :

1. implémenter un petit morceau ;
2. faire un petit run ciblé ;
3. observer ;
4. méta-discuter si nécessaire ;
5. corriger seulement si le diagnostic le justifie ;
6. passer au comportement suivant.

On évite les grosses sessions où dix variables changent en même temps.

---

# 15. Validation finale de V3

Quand le candidat V3 est suffisamment stable, on construit une validation plus complète.

Elle devra distinguer :

## Non-régression

Les comportements du noyau hérités de V2.1 :

- **A uniquement** ;
- parce que le but est seulement de vérifier qu’ils n’ont pas régressé.

## Validation de la nouvelle promesse V3

Les comportements réellement nouveaux du tutorat :

- scénarios spécifiques ;
- comparaison **A / B′** quand elle est utile pour démontrer la valeur ajoutée du skill.

Le protocole final sera défini une fois que la promesse V3 et le candidat seront stabilisés.

---

# 16. Ce que l’on ne décide pas maintenant

## Plugin

On ne migre pas vers un plugin pour résoudre le problème actuel.

À ce stade, le problème identifié est surtout :

- du tri ;
- de la duplication ;
- de la sédimentation dans `tutorat.md` ;
- quelques arbitrages doctrinaux.

La solution actuelle est donc :

> **moins de texte, plus de structure, et un skill compact.**

Un plugin reste une hypothèse future uniquement si une version compacte et testée du skill montre une limite architecturale réelle.

## LangChain / LangGraph / multi-agent

Même principe : aucune décision maintenant.

On ne change pas d’architecture tant que le besoin n’est pas démontré.

---

# 17. Séquence complète retenue

```text
V2 stable
│
├─ récupérer les artefacts V2 utiles
│
├─ trier les acquis de la V3 expérimentale
│
├─ construire V2.1
│  ├─ sortir P01 du noyau
│  ├─ intégrer l’attestation explicite du formateur
│  ├─ reporter les petits acquis doctrinaux utiles
│  └─ alléger et dédupliquer
│
├─ créer / stabiliser le NOY attestation formateur
│
├─ non-régression du noyau V2.1
│  └─ A × 1
│     └─ tout FAIL est rejoué ×2 avant diagnostic
│
├─ geler V2.1
│
├─ relire la promesse V2
│
├─ écrire une promesse tutorat V3 minimale
│
├─ créer quelques SPEC discriminantes
│
├─ tester ces SPEC en A / B′
│
├─ ajuster et geler la promesse V3
│
├─ implémenter V3 par petits morceaux
│
├─ petits runs + méta-discussion
│
└─ validation finale V3
```

---

# 18. Règles de conduite à garder sous les yeux

> **Doctrine avant procédure.**

> **Une seule source normative claire par règle.**

> **Une règle spécifique au tutorat reste dans le tutorat.**

> **Une dérogation au noyau doit être explicitement autorisée par le noyau, signalée avec un marqueur uniforme dans la référence spécialisée, et rester limitée à son périmètre.**

> **Un échec de run ne déclenche pas automatiquement une nouvelle règle.**

> **On ne modifie pas l’oracle et le skill dans le même cycle.**

> **On cherche le minimum obligatoire pour un tutorat utile et efficace, pas le tuteur parfait.**

> **La V3 expérimentale est une source d’enseignements, pas la nouvelle base de code.**

> **Le tuteur utilise volontiers `activites_type/` quand une activité existante sert réellement l’objectif et l’étape en cours.**

---

**Cette fiche constitue la base de travail actuelle pour construire V2.1 puis V3.**
