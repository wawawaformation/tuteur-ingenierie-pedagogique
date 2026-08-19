# Plan d’implémentation V2

**Projet :** `tuteur-ingenierie-pedagogique`  
**Version cible :** V2  
**Document associé :** `SPECIFICATIONS_NOYAU_V2_2026-08-19.md`  
**Statut :** plan de travail évolutif

---

# 1. Principe général

La V2 sera construite **test par test**, et non en séparant une phase de conception des tests d’une phase ultérieure de modification du skill.

Chaque test de non-régression `NOYxxx` déclenche une boucle complète :

```text
NOYxxx
→ rédaction / revue selon MODELE_FICHE_VALIDATION.md
→ contre-revue Opus
→ dry-run A / B'
→ analyse du comportement
→ modification du noyau si nécessaire
→ nouveau dry-run
→ vérification des contre-garde-fous
→ régression cumulative
→ stabilisation
```

Le principe directeur est :

> **Le test observe d’abord. La règle change ensuite.**

On ne modifie pas un oracle pour faire passer le candidat.

Si un test pédagogiquement légitime révèle une faiblesse du skill, c’est le noyau qui doit être modifié.

---

# 2. Deux phases distinctes

La V2 comporte deux grandes phases.

## Phase A — Développement itératif

Objectif :

> construire et calibrer le candidat V2.

Cette phase utilise les dry-runs `A / B'`.

Elle est volontairement exploratoire et peut conduire à modifier :

- les fiches de test ;
- les observables ;
- les oracles ;
- le noyau du skill ;
- les contre-garde-fous.

Les résultats de cette phase servent à **construire** la V2.

Ils ne constituent pas la validation finale.

---

## Phase B — Validation expérimentale indépendante

Objectif :

> vérifier le candidat V2 une fois celui-ci gelé.

À ce stade :

- le skill ne change plus ;
- les tests ne changent plus ;
- les prompts ne changent plus ;
- les oracles ne changent plus.

La validation repose alors sur :

```text
runs opérateur
→ collecte
→ gel
→ anonymisation
→ scoring externe
→ désaveuglement
→ analyse finale
```

---

# 3. État de départ

La V1 validée reste intacte.

```text
stable/
→ dernière version validée

dist/stable/
→ distribution publique de la dernière stable

en_cours/
→ candidat V2 en développement

validation/
→ tests, procédures, collectes et résultats
```

`en_cours/VERSION` indique :

```text
V2
```

La spécification V2 et le présent plan sont conservés dans `en_cours/`.

Aucune modification de la V2 ne doit être propagée vers `stable/` ou `dist/stable/` avant la validation finale.

---

# 4. Boucle de développement pour chaque NOY

Pour chaque fiche `NOYxxx`, appliquer la même séquence.

## Référence obligatoire — modèle général de fiche

Chaque test doit être conçu, relu et stabilisé en référence explicite à :

```text
validation/MODELE_FICHE_VALIDATION.md
```

Ce fichier constitue le **modèle méthodologique de référence** pour la rédaction des NOY.

Il faut notamment vérifier que la fiche contient ou traite correctement, selon le cas :

- l’**objectif du test** ;
- l’invariant testé ;
- le contexte / la fixture ;
- la trajectoire opérateur ;
- la consigne opérateur ;
- le périmètre de notation ;
- la règle de canal lorsqu’il existe plusieurs sources observables ;
- le traitement des libellés ambigus ;
- les observables ;
- l’oracle ;
- la validité technique ;
- le contrôle des interventions opérateur ;
- les limites reconnues.

Les principes du modèle doivent également être appliqués :

```text
observable plutôt qu’intention supposée
PASS / FAIL / INDÉTERMINÉ = partition
invalidité technique ≠ INDÉTERMINÉ
fixture sans fuite de l’attendu
opérateur humain mais traçable
contre-garde-fous contre la rigidité
```

Une fiche NOY ne doit pas être considérée comme stabilisée si elle s’écarte du modèle sans justification explicite.

---

## Étape 1 — Revue interne du test

Vérifier la fiche contre `validation/MODELE_FICHE_VALIDATION.md`.

Vérifier en particulier :

- la pertinence de l’objectif ;
- la précision de l’invariant ;
- le réalisme du stimulus ;
- l’absence de fuite de la réponse attendue ;
- la qualité des observables ;
- la frontière entre comportement et validité technique ;
- la complétude et la disjonction de l’oracle ;
- la marge de jugement opérateur ;
- les contre-cas et contre-garde-fous ;
- les limites reconnues.

Le stimulus ne doit pas contenir artificiellement la réponse attendue.

Les catégories :

```text
PASS
FAIL
INDÉTERMINÉ
```

doivent couvrir l’espace observable sans chevauchement.

---

## Étape 2 — Contre-revue méthodologique avec Opus

Avant le premier dry-run d’un nouveau test, faire intervenir **Opus** lorsque cela est utile — et, par défaut, ne pas hésiter à le faire pour chaque NOY.

Son rôle est celui d’un **contre-relecteur méthodologique**, pas d’un scoreur du candidat.

Lui demander de challenger notamment :

- la pertinence réelle du test pour le noyau ;
- la clarté de l’objectif ;
- la correspondance entre invariant et stimulus ;
- le risque que le prompt souffle le comportement attendu ;
- la qualité et l’observabilité des critères ;
- la partition PASS / FAIL / INDÉTERMINÉ ;
- les cas limites ;
- le périmètre de notation ;
- la validité technique ;
- la contamination possible par l’opérateur ;
- les contre-garde-fous ;
- les rigidités que le test pourrait involontairement encourager ;
- la reproductibilité probable entre deux scoreurs externes.

La contre-revue doit elle-même prendre comme référence :

```text
validation/MODELE_FICHE_VALIDATION.md
```

### Règle d’indépendance

Opus peut :

- signaler une ambiguïté ;
- proposer une reformulation ;
- relever un cas non couvert ;
- identifier une fuite ;
- contester la pertinence méthodologique du scénario.

Mais il ne doit pas devenir une autorité qui dicte le verdict expérimental.

La décision finale sur la fiche reste motivée et documentée.

Si la contre-revue conduit à une réécriture substantielle du test, une nouvelle contre-revue Opus peut être demandée avant stabilisation.

---

## Étape 3 — Dry-run A / B'

Exécuter le même scénario :

```text
A  = avec skill
B' = sans skill
```

Le dry-run sert à observer le comportement réel.

Il ne faut pas chercher à obtenir artificiellement :

```text
A PASS / B' FAIL
```

---

## Étape 4 — Interprétation

### Cas 1 — A PASS / B' FAIL

Le skill apporte déjà le comportement attendu.

Action :

- stabiliser le test ;
- l’ajouter à la suite de non-régression.

---

### Cas 2 — A PASS / B' PASS

Le modèle de base semble déjà produire le comportement attendu.

Action :

- vérifier la valeur du test pour le noyau ;
- conserver le test uniquement s’il protège un comportement important ou une future régression.

---

### Cas 3 — A FAIL / B' FAIL

Le comportement souhaité n’est assuré ni par le skill ni par le modèle de base.

Action :

- si le test est légitime, modifier le noyau ;
- rejouer le test après correction.

---

### Cas 4 — A FAIL / B' PASS

Le skill dégrade le comportement.

C’est un signal prioritaire de :

- rigidité ;
- faux positif ;
- règle trop large ;
- conflit entre garde-fous.

Action :

- recalibrer ou assouplir le noyau ;
- créer ou renforcer un contre-garde-fou.

T26 constitue le cas historique de référence.

---

### Cas 5 — résultat ambigu

Si le verdict dépend d’une interprétation incertaine :

- ne pas modifier immédiatement le skill ;
- retravailler la fiche ou l’oracle ;
- refaire le dry-run.

---

# 5. Modification du noyau

Lorsqu’une faiblesse est confirmée, effectuer une modification **minimale et localisée**.

Fichiers centraux susceptibles d’être concernés :

```text
en_cours/SKILL.md
en_cours/references/taxonomie.md
en_cours/references/etat_des_paliers.md
en_cours/references/opo.md
en_cours/references/activite.md
```

Principe :

> **une règle possède une source de vérité principale.**

Éviter de recopier la même règle détaillée dans plusieurs fichiers.

`SKILL.md` porte surtout :

- les garde-fous structurants ;
- les priorités comportementales ;
- les renvois vers les références.

Les fichiers de référence portent le détail.

---

# 6. Vérification après modification

Après chaque modification du noyau :

1. rejouer le NOY qui a motivé la modification ;
2. vérifier son contre-garde-fou ;
3. rejouer les NOY déjà stabilisés susceptibles d’être affectés ;
4. vérifier qu’aucune nouvelle rigidité n’a été introduite ;
5. vérifier le diff du skill ;
6. stabiliser la fiche et la règle ;
7. commit lorsque l’ensemble est cohérent.

La suite de régression devient donc progressivement cumulative.

Exemple :

```text
NOY001
→ correction
→ PASS
→ gel

NOY002
→ contrôle
→ PASS

NOY003
→ correction éventuelle
→ rejouer NOY001 + NOY002 si concernés

NOY004
→ etc.
```

---

# 7. Batterie de départ

Les NOY actuellement retenus couvrent le noyau pédagogique.

```text
NOY001
→ exposition / démonstration ≠ preuve attestée

NOY002
→ qualité du résultat ≠ nature de la preuve

NOY003
→ budget de nouveauté

NOY004
→ alignement objectif / tâche / critère / preuve

NOY005
→ réussite intégratrice ≠ maîtrise automatique de chaque notion

NOY006
→ impression ≠ preuve

NOY007
→ nouvelle preuve pouvant réviser un état antérieur

NOY008
→ démonstration pouvant introduire de la nouveauté

NOY009
→ activité guidée autorisée sans constituer une preuve d’autonomie

NOY010
→ autre garde-fou retenu dans la batterie actuelle
```

La numérotation et le contenu exact pourront encore évoluer pendant la phase de dry-run.

---

# 8. Sentinelle anti-rigidité issue de T26

Ajouter une sentinelle dédiée au principe :

> **nouvelle tâche ≠ automatiquement nouvelle notion**

Elle doit distinguer :

```text
nouveau contexte
nouvel exemple
nouvelle donnée
nouvelle formulation
```

de :

```text
nouveau mécanisme réellement nécessaire
```

Le noyau doit protéger les deux côtés :

```text
ne pas sous-détecter une vraie nouveauté
+
ne pas sur-détecter une simple variation
```

Ce test constitue un contre-garde-fou important du budget de nouveauté.

Nom provisoire :

```text
NOY011
```

---

# 9. Transformer la notation ad hoc en propriété testée

L’observation V1 sur la notation chiffrée doit devenir une propriété pré-spécifiée.

Deux tests complémentaires sont nécessaires.

## Test sans notation arbitraire

Contexte :

- activité évaluée demandée ;
- aucun barème fourni ;
- aucune note demandée ;
- aucune mesure numérique nécessaire.

Attendu avec skill :

```text
objectif
→ production observable
→ critères
→ preuve
→ attestation
```

sans invention spontanée de :

```text
/10
/20
/100
points
bonus
pondérations
seuil scolaire
```

Nom provisoire :

```text
NOY012
```

---

## Contre-test avec quantification légitime

Le contexte impose ou justifie une mesure numérique.

Exemples :

- temps maximal ;
- nombre minimal d’éléments ;
- taux attendu ;
- nombre de tests réussis ;
- seuil de référentiel ;
- barème institutionnel ;
- demande explicite d’une note.

Le skill doit accepter la quantification.

Nom provisoire :

```text
NOY013
```

Le principe testé est :

> **pas de notation arbitraire par défaut, mais pas d’interdiction générale des nombres.**

---

# 10. Ordre de travail

L’ordre proposé est désormais vertical.

```text
1. NOY001
   → revue selon MODELE_FICHE_VALIDATION.md
   → contre-revue Opus
   → dry-run
   → correction du noyau si nécessaire
   → rerun
   → stabilisation

2. NOY002
   → contrôle de non-régression

3. NOY003
   → boucle complète

4. NOY004
   → boucle complète

5. NOY005
   → boucle complète

6. NOY006
   → boucle complète

7. NOY007
   → boucle complète

8. NOY008
   → boucle complète

9. NOY009
   → boucle complète

10. NOY010
    → boucle complète

11. Sentinelle anti-rigidité T26
    → boucle complète

12. Tests sur la notation
    → boucle complète

13. Rejouer toute la batterie NOY

14. Nettoyer et harmoniser le noyau

15. Rejouer toute la batterie après nettoyage

16. Geler le candidat V2
```

Cet ordre peut être adapté si un dry-run révèle une faiblesse structurante qui doit être traitée immédiatement.

---

# 11. Porte de stabilisation de chaque test

Un `NOYxxx` est considéré comme stabilisé uniquement lorsque :

- sa fiche est conforme à `validation/MODELE_FICHE_VALIDATION.md`, ou tout écart est explicitement justifié ;
- sa pertinence pour le noyau est établie ;
- le stimulus ne souffle pas artificiellement l’attendu ;
- les observables permettent réellement de scorer ;
- PASS / FAIL / INDÉTERMINÉ couvrent les comportements observables sans chevauchement ;
- invalidité technique et verdict comportemental sont séparés ;
- la marge opérateur est définie et traçable ;
- les contre-garde-fous nécessaires sont présents ;
- le dry-run A / B' a été analysé ;
- toute modification du noyau motivée par le test a été rejouée ;
- les NOY antérieurs potentiellement affectés ont été rejoués ;
- une contre-revue Opus a été réalisée lorsque le test est nouveau, sensible, ambigu ou substantiellement réécrit.

La contre-revue Opus est fortement recommandée pour chaque test ; elle devient particulièrement importante avant de considérer une fiche comme prête à rejoindre la batterie gelée.

---

# 12. Gel du candidat V2

La phase de développement se termine lorsque :

- les NOY retenus sont stabilisés ;
- les guardrails nécessaires ont été corrigés ;
- les contre-garde-fous sont présents ;
- la suite de régression est satisfaisante ;
- les tests de notation sont formalisés ;
- les oracles sont suffisamment précis ;
- le candidat `en_cours/` est cohérent.

À ce moment :

```text
candidat V2
→ gel
```

Après le gel :

> aucune modification du skill, des tests, des prompts ou des oracles pendant la campagne de validation.

---

# 13. Préparation de la campagne opérateur

La validation finale doit être indépendante de la phase de dry-run.

Préparer :

- la liste définitive des scénarios ;
- les prompts exacts ;
- les conditions A / B' ;
- les répétitions ;
- les règles opérateur ;
- les règles de validité technique ;
- les procédures de collecte ;
- les oracles gelés ;
- les règles de scoring ;
- le dispositif d’anonymisation.

Les dry-runs de développement ne doivent pas être mélangés aux trajectoires de validation finale.

---

# 14. Exécution opérateur

La campagne finale est exécutée avec le candidat gelé.

Pour chaque run :

- condition définie ;
- environnement contrôlé ;
- prompt exact ;
- intervention opérateur limitée au protocole ;
- collecte complète ;
- aucune correction en cours de campagne.

Les incidents techniques sont traités selon une règle définie avant la campagne.

---

# 15. Gel des collectes

Une fois les runs terminés :

```text
collectes complètes
→ contrôle d’intégrité
→ gel
```

Après ce gel :

- aucune trajectoire n’est réécrite ;
- aucune sortie n’est corrigée ;
- les éventuels runs invalides restent conservés pour audit mais sont exclus du scoring officiel selon la procédure.

---

# 16. Anonymisation

Préparer un paquet aveugle qui ne permet pas au scoreur de savoir :

- si le skill était présent ;
- quelle condition correspond à quelle trajectoire ;
- quelle répétition il évalue ;
- quel résultat était attendu par l’équipe de développement.

Le mapping reste privé jusqu’au désaveuglement.

---

# 17. Scoring externe indépendant

Le scoring final ne doit pas être réalisé par les personnes ou agents ayant participé à la construction des tests et aux dry-runs.

Le scoreur reçoit uniquement :

- la procédure ;
- les fiches/oracles nécessaires ;
- les trajectoires anonymisées.

Il ne reçoit pas :

- les résultats des dry-runs ;
- les hypothèses de développement ;
- la condition expérimentale ;
- les conclusions attendues.

Idéalement, utiliser **deux scoreurs indépendants**.

Objectifs :

- mesurer l’accord inter-scoreurs ;
- détecter les oracles encore ambigus ;
- éviter de faire dépendre la conclusion d’un seul jugement.

Les verdicts sont figés avant désaveuglement.

---

# 18. Désaveuglement

Le désaveuglement intervient uniquement après :

```text
scoring terminé
+
verdicts figés
```

On peut alors reconstruire :

- avec skill ;
- sans skill ;
- répétitions ;
- paires ;
- tests.

Aucune modification rétroactive du scoring ne doit être faite pour améliorer le contraste expérimental.

---

# 19. Analyse finale V2

L’analyse finale doit répondre séparément à plusieurs questions.

## Non-régression

Les comportements du noyau que la V2 devait protéger sont-ils maintenus ?

## Corrections

Les faiblesses identifiées en V1 ont-elles été corrigées ?

## Rigidité

Les contre-garde-fous empêchent-ils les corrections de rendre le skill excessivement strict ?

## Contribution

Le skill apporte-t-il un comportement meilleur que la condition sans skill sur les scénarios où sa contribution est attendue ?

## Scoring

Les oracles sont-ils suffisamment reproductibles entre scoreurs ?

## Généralisation

Les résultats observés sont-ils limités aux stimuli de développement ou se maintiennent-ils sur des variantes indépendantes ?

---

# 20. Promotion vers stable

La promotion n’intervient qu’après conclusion favorable de la validation.

Si la V2 est acceptée :

```text
en_cours/
→ stable/
→ dist/stable/
```

Puis :

- construire la distribution publique ;
- mettre à jour le numéro/version ;
- documenter les changements ;
- créer le tag correspondant à la release stable.

Si la V2 n’est pas suffisamment validée :

```text
stable/
```

reste sur la dernière version validée.

---

# 21. Résumé du workflow

```text
V1 validée
        ↓
spec V2
        ↓
NOY001
→ fiche selon MODELE_FICHE_VALIDATION.md
→ contre-revue Opus
→ dry-run
→ correction
→ rerun
        ↓
NOY002
→ contrôle / correction éventuelle
        ↓
NOY003
→ même boucle
        ↓
...
        ↓
sentinelles anti-rigidité
        ↓
tests notation
        ↓
suite NOY complète
        ↓
candidat V2 gelé
        ↓
campagne opérateur indépendante
        ↓
collectes gelées
        ↓
anonymisation
        ↓
scoring externe
        ↓
accord / arbitrage prévu par procédure
        ↓
désaveuglement
        ↓
analyse V2
        ↓
validation ?
   oui         non
    ↓           ↓
 stable/    stable/ inchangé
    ↓
dist/stable/
```

---

# 22. Règle méthodologique finale

La séparation à préserver est :

```text
dry-runs
= développement

campagne opérateur
= observation expérimentale

scoring externe
= jugement indépendant

désaveuglement
= comparaison

stable
= version validée
```

C’est cette séparation qui permet à la V2 d’être à la fois construite de manière itérative et évaluée ensuite sans confondre développement et validation.
