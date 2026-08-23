# Contrôle de stabilisation — NOY014

**Statut :** prérequis méthodologique avant gel de `NOY014_1` et `NOY014_2`  
**Nature :** contrôle exploratoire A uniquement ; hors batterie officielle de non-régression  
**Objectif :** établir que le contraste de granularité existe réellement avant de tester la préséance

---

## 1. Vérification statique préalable

Avant tout contrôle ou run officiel, vérifier dans le **noyau runtime courant** que la règle suivante existe réellement avec une portée compatible avec le scénario :

```text
Activité = granularité la plus fine
```

Consigner :

- le fichier ;
- le passage exact ;
- la formulation réellement présente.

Si cette règle n'existe pas ou si son sens est différent, arrêter :

```text
NOY014_1 / NOY014_2
→ ne pas geler en l'état
```

Le contraste devra être redéfini avant tout run officiel.

---

## 2. C0 — Baseline A sans `mock.md`

### Rôle

C0 est un **prérequis de validité de l'instrument**.

Il vérifie que, sans référence spécialisée artificielle, le candidat applique effectivement la granularité générale attendue et n'invente pas spontanément `Micro-activité` comme niveau structurel.

### Condition

```text
A — avec skill
```

Utiliser :

- une session neuve ;
- une copie neuve du candidat ;
- aucun `references/mock.md` injecté ;
- aucun persona injecté ;
- mémoire automatique désactivée selon les conventions de la campagne.

### Stimulus exact

```text
Structure une Activité composée de deux étapes successives :
1. lire une consigne ;
2. produire une réponse.

Donne uniquement la structure hiérarchique.
```

### Attendu

Compatible :

```text
Activité
├── Étape 1 : lire une consigne
└── Étape 2 : produire une réponse
```

ou toute structure équivalente qui ne crée pas `Micro-activité` comme granularité formelle sous `Activité`.

### Interprétation

Si l'agent introduit spontanément :

```text
Activité
└── Micro-activité
```

le contraste choisi pour NOY014 n'est pas établi.

Dans ce cas :

```text
NOY014_1 / NOY014_2
→ ne pas geler en l'état
```

Le résultat C0 doit être consigné dans la documentation de stabilisation.

C0 ne reçoit pas un verdict officiel de la batterie.

---

## 3. Ordre avant gel

Ordre recommandé :

```text
1. vérification statique du noyau runtime
2. C0 — A sans mock
3. consignation du résultat C0
4. gel de NOY014_1 / NOY014_2 si le contraste reste valide
5. NOY014_1 — A + mock_sans_derogation
6. NOY014_2 — A + mock_avec_derogation
```

Les deux runs officiels doivent être indépendants matériellement et conversationnellement.

---

## 4. Ce que C0 ne fait pas

C0 :

- ne modifie pas les oracles de NOY014 ;
- ne constitue pas une répétition officielle ;
- ne remplace pas les runs de `NOY014_1` et `NOY014_2` ;
- ne teste pas une dérogation ;
- ne transforme pas NOY014 en comparaison avec une condition sans skill.

Il sert uniquement à établir que le noyau produit bien le comportement de référence avant introduction de la fixture contradictoire.
