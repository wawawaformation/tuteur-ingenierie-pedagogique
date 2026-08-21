# Fiche de synthèse — utilité pratique du skill V2

**Projet :** `tuteur-ingenierie-pedagogique`  
**Date :** 2026-08-21  
**Objet :** appréciation synthétique de l'utilité, de l'utilisabilité et du rapport apport / coût du candidat V2.

---

## Conclusion en une phrase

> **Le skill V2 est utile et utilisable malgré ses défauts : il apporte des garde-fous pédagogiques observables et reproductibles sur plusieurs décisions critiques, avec un coût en tokens important en relatif mais encore raisonnable en pratique.**

---

## 1. Est-ce que le skill est utile ?

**Oui.**

Son intérêt ne tient pas principalement à la qualité rédactionnelle des réponses, mais à sa capacité à éviter certains raccourcis pédagogiques plausibles mais fragiles.

Les résultats les plus nets portent sur des décisions comme :

- ne pas confondre **compréhension déclarée** et **preuve d'application** ;
- ne pas transformer un **QCM réussi** en preuve automatique de capacité à produire ;
- ne pas considérer qu'une **activité globalement réussie** atteste automatiquement toutes les notions qu'elle mobilise ;
- préserver le **budget de nouveauté** et la valeur diagnostique d'une activité évaluée ;
- maintenir l'alignement entre **objectif, tâche, production, critères, preuve et conclusion** ;
- ne pas transformer spontanément une **évaluation en notation chiffrée arbitraire**.

Sur `NOY004` à `NOY008`, le contraste est particulièrement net :

```text
avec skill : PASS / PASS
sans skill : FAIL / FAIL
```

Ce n'est donc pas seulement un changement de style : le skill modifie certaines **décisions pédagogiques**.

---

## 2. Quel est son apport réel ?

Le modèle sans skill possède déjà de bonnes capacités pédagogiques.

La campagne montre trois situations différentes.

### Le skill apporte un garde-fou que le modèle nu ne maintient pas de manière fiable

Exemples :

- `NOY004` — budget de nouveauté ;
- `NOY005` — alignement pédagogique ;
- `NOY006` — portée exacte d'une preuve ;
- `NOY007` — auto-déclaration ≠ attestation ;
- `NOY008` — absence de notation arbitraire.

### Le skill stabilise un comportement que le modèle nu sait parfois produire

Exemple :

```text
NOY003
avec skill : PASS / PASS
sans skill : PASS / FAIL / PASS(R3)
```

Le modèle sans skill sait parfois distinguer un QCM de compréhension d'une preuve d'application, mais ne le fait pas systématiquement.

Le skill apporte ici surtout une **réduction de la variance comportementale**.

### Certaines capacités existent déjà sans skill

Exemple :

```text
NOY002
avec skill : PASS / PASS
sans skill : PASS / INDÉTERMINÉ / PASS(R3)
```

Le modèle sans skill sait également distinguer une auto-déclaration d'une preuve autonome lorsque la trajectoire est complète.

C'est un résultat utile : le skill ne doit pas être présenté comme la source exclusive de toute bonne décision pédagogique.

---

## 3. À quoi sert donc principalement le skill ?

La meilleure description est :

> **un système de garde-fous qui pousse un bon modèle généraliste à raisonner davantage comme un formateur / concepteur pédagogique lorsqu'il doit prendre une décision engageante.**

Son rôle principal est d'éviter des raccourcis du type :

```text
"j'ai compris"
→ maîtrise attestée

10/10 au QCM
→ sait appliquer

activité réussie
→ toutes les notions sont maîtrisées

livrable complet
→ objectif atteint

activité évaluée
→ barème sur 20
```

Le cadre attendu devient plutôt :

```text
point de départ
→ notions mobilisées
→ état attesté
→ preuve disponible
→ activité
→ critères
→ portée de la preuve
→ conclusion
```

---

## 4. Est-il utilisable malgré ses défauts ?

**Oui.**

Aucun défaut observé dans la campagne V2 ne paraît suffisamment grave pour rendre le skill inutilisable.

Le principal point de vigilance reste `NOY001` :

```text
avec skill : FAIL / PASS / PASS(R3)
sans skill : FAIL / FAIL
```

Le skill améliore nettement l'élicitation du point de départ, mais le comportement n'est pas encore parfaitement stable.

Ce défaut doit rester un **test de non-régression prioritaire**.

Il faut également éviter de rigidifier cette règle.

L'objectif n'est pas :

```text
ne rien dire avant que l'apprenant ait répondu
```

mais :

```text
ne pas prendre une décision pédagogique importante
à partir d'acquis supposés ou inventés
```

Un cadrage, une accroche ou l'annonce d'un plan restent compatibles avec cette logique.

---

## 5. Le skill est-il trop rigide ?

La campagne ne montre pas une rigidité générale bloquante.

Au contraire, certains résultats sont rassurants :

- le modèle peut conserver de bons comportements déjà présents sans skill ;
- le skill n'a pas besoin de prétendre apporter quelque chose sur tous les scénarios ;
- les contrats propres à V2 sont stables ;
- les R3 n'ont pas révélé de défaut bloquant reproductible.

Le risque de rigidité existe néanmoins et doit rester surveillé, notamment sur :

- l'élicitation du point de départ ;
- la qualification de ce qui constitue réellement une nouvelle notion ;
- l'application trop mécanique de règles conçues comme des garde-fous.

---

## 6. Coût en tokens

Sur les **16 paires directement comparables** :

| Mesure | Avec skill | Sans skill |
|---|---:|---:|
| Total tokens | **4 174 595** | **1 674 701** |
| Ratio | **2,49×** | — |
| Surcoût agrégé | **+149,3 %** | — |

Le skill consomme davantage dans :

> **16 paires sur 16**

Le surcoût est donc structurel dans cette campagne.

---

## 7. D'où vient ce coût ?

Le surcoût provient surtout de l'entrée et du contexte/cache, beaucoup plus que de la longueur des réponses finales.

Environ :

- **98,2 % du delta total** provient des tokens d'entrée ;
- **90,5 % du delta total** provient de la lecture de cache ;
- **1,8 % seulement** du delta provient des tokens de sortie.

La lecture pratique est donc :

> **le skill coûte principalement parce qu'il fournit et mobilise un cadre pédagogique plus riche, pas simplement parce qu'il produit des réponses plus bavardes.**

---

## 8. Ce coût est-il acceptable ?

**En relatif, il est élevé.**

Un facteur `2,49×` n'est pas négligeable.

Mais il faut le mettre en regard de l'usage.

Payer ce surcoût uniquement pour améliorer légèrement la formulation d'une réponse serait peu intéressant.

En revanche, le coût devient beaucoup plus défendable lorsqu'il sert à éviter des erreurs de décision comme :

```text
preuve insuffisante
→ attestation excessive

activité mal construite
→ conclusion non diagnostique

évaluation
→ notation arbitraire

objectif
≠
preuve réellement recueillie
```

Par ailleurs, l'observation opérateur pendant la campagne indique que les **20 derniers runs ont représenté environ 11 points du quota d'utilisation affiché par Claude**.

Ce pourcentage ne doit pas être assimilé directement à des tokens, à un prix ou à du temps de calcul, mais il donne une information pratique :

> **le surcoût mesuré n'a pas rendu l'utilisation ou la campagne opérationnellement difficile.**

---

## 9. Rapport apport / coût

### Apport

- garde-fous pédagogiques observables ;
- meilleurs résultats sur plusieurs scénarios centraux ;
- stabilisation de comportements que le modèle nu possède de façon irrégulière ;
- architecture V2 conforme sur les tests spécifiques ;
- meilleure discipline autour de la preuve, de l'évaluation et de l'alignement.

### Coût

- environ **2,49× plus de tokens** sur la batterie comparative ;
- davantage de contexte à charger et à relire ;
- quelques risques résiduels de rigidification ;
- `NOY001` encore imparfaitement stable.

### Appréciation

> **Le rapport apport / coût est positif pour un usage pédagogique substantiel.**

Il serait moins évident pour de petites demandes simples où aucun des garde-fous du skill n'est réellement nécessaire.

---

## 9.1 Intérêt pratique : rester sur un modèle et un effort plus économiques

Un autre intérêt pratique du skill est qu'il peut permettre de **conserver un modèle relativement économique avec un niveau d'effort modéré**, plutôt que de chercher systématiquement à compenser l'absence de garde-fous par un modèle plus coûteux ou un effort de raisonnement supérieur.

Dans l'usage visé, cela correspond par exemple à rester sur **Sonnet avec un effort autour de 2/6**, au lieu de monter par défaut vers **Opus** ou vers un effort **3/6 ou supérieur**, qui consomment davantage de ressources.

L'intérêt potentiel est donc double :

```text
modèle généraliste économique + effort modéré + skill ciblé
→ garde-fous pédagogiques explicites
```

plutôt que :

```text
modèle plus coûteux / effort plus élevé
→ espérer obtenir les mêmes garde-fous par davantage de capacité générale
```

Cette lecture doit cependant rester **une appréciation pratique et une hypothèse d'efficience**, pas un résultat causal de la campagne V2 : la campagne n'a pas comparé expérimentalement Sonnet 2/6, Sonnet 3/6 et Opus à stimuli identiques.

Elle renforce néanmoins l'intérêt du rapport apport / coût : le surcoût contextuel du skill peut rester pertinent s'il évite de devoir augmenter systématiquement le niveau de modèle ou d'effort pour obtenir une discipline pédagogique comparable.

---

## 10. Appréciation globale

| Dimension | Appréciation |
|---|---|
| Utilité réelle | **Oui** |
| Apport différentiel | **Net sur plusieurs comportements centraux** |
| Stabilisation | **Bonne globalement** |
| Défaut principal | **NOY001 à surveiller** |
| Architecture V2 | **Conforme sur les tests prévus** |
| Coût en tokens | **Élevé en relatif (~2,49×)** |
| Coût pratique observé | **Supportable** |
| Rapport apport / coût | **Positif pour un usage pédagogique substantiel** |
| Modèle / effort | **Peut permettre de rester sur une configuration plus économique ; hypothèse pratique non testée causalement** |
| Utilisable maintenant | **Oui** |
| Candidat à `stable/` | **Oui, sur la base du périmètre testé** |

---

## 11. Position finale

> **Le candidat V2 a dépassé le stade d'une simple collection de bonnes pratiques.**

La campagne montre un **effet comportemental identifiable** : le skill rend plusieurs garde-fous pédagogiques plus présents ou plus stables.

Il conserve des défauts et son coût en contexte est réel, mais ces limites sont :

- connues ;
- localisées ;
- documentées ;
- compatibles avec une utilisation pratique.

La décision raisonnable est donc de le considérer comme :

> **utile, utilisable, imparfait mais suffisamment stabilisé pour être employé et promu, tout en maintenant une batterie de non-régression sur ses zones sensibles.**

