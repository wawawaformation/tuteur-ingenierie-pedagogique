# Protocole opérateur — validation V1

## 1. Objet

Ce document décrit la mécanique opératoire à conserver pour l'exécution de la
campagne de validation V1.

Le principe général est le suivant :

> La nouvelle campagne ne doit pas réinventer l'opérateur.
> On conserve la mécanique opérationnelle qui a déjà fonctionné et on ne
> modifie que ce qui est nécessaire pour exécuter les tests historiques
> `T01` à `T30`.

Ce protocole complète `docs/procedure_en_cours.md`.

---

## 2. Deux blocs shell maximum par run

Chaque run est exécuté en deux blocs principaux.

### BLOC 1 — préparation et lancement

Le BLOC 1 réalise notamment :

- les vérifications préalables du run ;
- la vérification des gels et manifestes applicables ;
- la préparation d'un workspace neuf ;
- la copie éventuelle du skill dans la condition `avec skill` ;
- l'absence de skill dans la condition `sans skill` ;
- la matérialisation du prompt exact ;
- la mise en place de la persona si le test en utilise une ;
- le démarrage du collecteur ;
- le lancement de Claude.

Le BLOC 1 s'arrête ensuite sur l'interaction avec Claude.

### BLOC 2 — collecte et archivage

Après la fin de la session Claude et la commande `exit`, le BLOC 2 réalise :

- la collecte de la session ;
- le contrôle minimal de présence des artefacts ;
- l'archivage du run ;
- le calcul du SHA-256 de l'archive.

On évite d'ajouter des blocs intermédiaires de contrôle ou de réparation sauf
incident technique réellement nécessaire.

---

## 3. Rôle de l'opérateur

L'opérateur interprète la nature des interactions de Claude.

Il ne répond pas mécaniquement de la même manière à toutes les demandes.

Il distingue au minimum :

### Question pédagogique couverte par le test

Si le test ou sa fiche prévoit explicitement une information opérateur, la
réponse prévue doit être utilisée.

### Demande d'information non couverte

Si Claude demande une information qui n'est pas fournie par le test et qui
n'est pas nécessairement prévue par une branche opérateur, utiliser la réponse
neutre :

> Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.

L'opérateur ne doit jamais inventer une information pour aider Claude.

### Question de continuation facultative

Si Claude a fourni une réponse complète puis termine par une proposition du
type « voulez-vous que je continue ? », « souhaitez-vous un exemple ? » ou
équivalent, l'opérateur ne joue pas l'apprenant.

Le run peut être terminé.

### Interaction purement technique

Les écrans de confiance du workspace, demandes de permission, confirmations
d'accès ou autres interactions de Claude Code sont des interactions techniques.

Elles ne doivent pas être interprétées comme des tours pédagogiques.

---

## 4. Les tests historiques restent la référence

Les fiches présentes dans :

```text
validation/v1/tests/
```

sont gelées.

L'opérateur ne doit pas ajouter en cours d'exécution une règle plus stricte que
celle écrite dans le test.

Exemple : `T18` demande de privilégier une question diagnostique avant de
déverser un cours complet.

Il ne doit pas être transformé pendant l'exécution en une règle différente
interdisant toute phrase de cadrage ou toute hypothèse prudente avant la
question diagnostique.

Principe :

> ancien test → exécution fidèle → trajectoire observée → scoring selon la
> fiche gelée.

---

## 5. Un seul run à la fois

L'exécution se fait run par run.

Séquence opératoire :

```text
BLOC 1
↓
interaction avec Claude
↓
éventuelle décision opérateur
↓
exit
↓
BLOC 2
↓
collecte et archivage
↓
run suivant
```

Cette règle vise à limiter les erreurs de session, de condition, de workspace
ou de collecte.

---

## 6. Aucun scoring pendant l'exécution

L'exécution et le scoring sont deux phases séparées.

Pendant les runs :

- ne pas attribuer de PASS ou FAIL ;
- ne pas conclure que le skill gagne ou perd ;
- ne pas comparer les conditions ;
- ne pas modifier le comportement opérateur en fonction des réponses déjà vues.

Les trajectoires sont collectées telles quelles.

Le scoring intervient ultérieurement à partir des fiches gelées.

---

## 7. Contrôle technique groupé

Pendant l'exécution, on privilégie :

- préparation correcte ;
- collecte correcte ;
- archivage correct ;
- absence d'incident bloquant.

Les contrôles techniques détaillés sont regroupés à des moments prévus plutôt
que réalisés après chaque run.

Un compteur brut de `human_turns` ne doit pas être utilisé seul pour conclure
qu'un run est invalide : une permission ou une interaction technique peut
ajouter un tour humain sans constituer un tour pédagogique.

---

## 8. Isolation des deux conditions

### Condition avec skill

Le run utilise :

- un workspace neuf ;
- une copie exacte de `en_cours/` dans le répertoire de skill prévu ;
- la mémoire automatique désactivée.

### Condition sans skill

Le run utilise :

- un workspace neuf ;
- aucun skill installé ;
- la mémoire automatique désactivée.

### Paramètres communs

Les deux conditions doivent partager autant que possible :

- la même version de Claude Code ;
- le même modèle ;
- le même niveau d'effort ;
- le même mode de permission ;
- le même prompt ;
- la même persona éventuelle ;
- le même collecteur ;
- les mêmes règles d'isolation.

La présence ou l'absence du skill doit rester la principale différence entre
les deux conditions.

---

## 9. Interactions techniques

### Confiance du workspace

Un écran du type :

```text
Do you trust this folder?
```

est une interaction technique.

Il ne constitue pas une information pédagogique.

### Permission ou accès hors workspace

Une demande d'accès technique qui sortirait du périmètre prévu doit être
traitée selon la politique d'isolation du run.

Le refus ou l'autorisation d'une permission technique ne doit jamais fournir
d'information pédagogique supplémentaire.

Si une interaction technique perturbe réellement la trajectoire, elle doit
être conservée et documentée comme incident technique.

---

## 10. Réponse neutre

Réponse neutre de référence :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Elle est utilisée uniquement lorsqu'aucune information supplémentaire n'est
prévue ou autorisée.

Elle ne doit pas remplacer une réponse spécifique explicitement prévue par un
test.

---

## 11. Reruns techniques

Un rerun n'est autorisé que pour une invalidité technique réelle.

Un rerun technique :

- est identifié explicitement comme tel ;
- ne remplace le run d'origine que selon la règle définie par le protocole ;
- ne constitue pas une répétition comportementale ;
- ne doit jamais être déclenché parce que la réponse observée est
  comportementalement défavorable.

---

## 12. Répétitions comportementales

Pour chaque couple `test × condition` :

- répétition 1 ;
- répétition 2 ;
- répétition 3 uniquement si les verdicts des répétitions 1 et 2 diffèrent.

La troisième répétition est déterminée par le désaccord des verdicts, jamais par
le fait qu'un résultat favorise ou défavorise le skill.

---

## 13. Principe de stabilité

Les éléments qui ont déjà montré leur utilité opérationnelle sont conservés
tant qu'ils ne créent pas de défaut identifié.

La reprise de validation doit donc privilégier :

- la continuité du protocole opérateur ;
- les modifications minimales ;
- la traçabilité ;
- la séparation entre incident technique et comportement pédagogique ;
- la fidélité aux tests historiques gelés.

La nouvelle campagne change le corpus et le plan de répétitions, pas la
mécanique fondamentale de l'opérateur.

---

## 14. Statut

Ce document doit être finalisé et gelé avant le lancement du premier run.

Aucun run de la nouvelle campagne V1 n'est autorisé tant que le protocole
opérateur et ses paramètres techniques communs n'ont pas été vérifiés.
