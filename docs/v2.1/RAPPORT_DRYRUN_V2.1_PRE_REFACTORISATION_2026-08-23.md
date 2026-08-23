# Rapport rapide — dry-run V2.1 avant refactorisation

**Projet :** `tuteur-ingenierie-pedagogique`
**Version testée :** candidat V2.1 (post-implémentation G02, cf. `RAPPORT_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23.md`)
**Date :** 2026-08-23
**Statut :** dry-run de photographie, **pas une validation officielle ni un gel expérimental**. Sert de référence de non-régression pour la refactorisation à venir du noyau.

---

## 1. Objet

Photographier le comportement actuel de V2.1 avant remaniement/allègement du noyau.

## 2. Résultat global

16 scénarios NOY exécutés.

| Résultat | Compte |
|---|---|
| PASS | 15/16 |
| FAIL | 1/16 |

| Scénario | Résultat |
|---|---|
| NOY001 | PASS |
| NOY002 | PASS |
| NOY003 | PASS |
| NOY004 | PASS |
| NOY005 | PASS |
| NOY006 | PASS |
| NOY007 | PASS |
| NOY008 | PASS |
| NOY009 | PASS |
| NOY010 | PASS |
| NOY011 | PASS |
| NOY012_1 | PASS |
| NOY012_2 | PASS |
| NOY013 | PASS |
| NOY014_1 | **FAIL** |
| NOY014_2 | PASS |

`NOY014_1` a été rejoué conformément au protocole après le premier FAIL :

- run initial : FAIL
- rerun R1 : FAIL
- rerun R2 : FAIL

→ FAIL reproductible **3/3**.

## 3. Diagnostic NOY014

`NOY014` teste la règle de préséance entre règle générale et référence spécialisée (G02).

**NOY014_1** — la référence spécialisée `MOCK-GRANULARITE` contredit la règle générale sans signaler explicitement de dérogation. Attendu : la règle générale prévaut → structure `Activité → étapes`, sans niveau « Micro-activité ».

Observé 3/3 : Claude applique la règle spécialisée →

```
Activité
├── Micro-activité ...
└── Micro-activité ...
```

Sur deux exécutions, Claude qualifie lui-même le mock de « dérogation explicite », alors que le fichier ne contient aucune déclaration explicite de dérogation. Le mock injecté a été vérifié : ce n'est pas une inversion d'overlay.

**NOY014_2** — même conflit, mais la référence spécialisée signale explicitement la dérogation. Résultat : PASS, `Activité → Micro-activités` correctement produit.

## 4. Correspondance avec le risque R1 déjà documenté

Ce FAIL correspond exactement au risque **R1** identifié dans `RAPPORT_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23.md` (§6) et dans `PLAN_IMPLEMENTATION_PRESEANCE_V2.1_2026-08-23_CORRIGE.md` (§R1, l. 218-223) : `SKILL.md` l. 99 (« la référence normative spécialisée fait foi ») risquait d'être lue comme une préséance générale des références spécialisées, indépendamment d'un marqueur de dérogation explicite — motif d'ailleurs déjà présent dans le verbatim attendu (« spécialisée dans les deux cas »).

Le plan recommandait de ne désambiguïser l. 99 **que si** `NOY014_1` échouait effectivement avec ce motif, et dans un **cycle séparé**, jamais simultanément à un ajustement d'oracle. C'est désormais le cas : le motif prédit se retrouve dans les deux justifications verbatim relevées (« dérogation explicite » attribuée à tort au mock).

## 5. Conclusion fonctionnelle

Le mécanisme positif de dérogation locale fonctionne : « avec dérogation explicite » → comportement spécialisé correctement appliqué (NOY014_2).

La faiblesse porte sur le discriminateur négatif : « absence de dérogation explicite » n'est pas respectée. Claude interprète actuellement une règle spécialisée applicable et contradictoire comme une dérogation implicite/de facto.

## 6. Contraintes pour la refactorisation à venir

1. Préserver les comportements couverts par NOY001 à NOY013.
2. Préserver la branche positive NOY014_2.
3. Rendre réellement discriminante la condition « pas de dérogation explicitement signalée ⇒ règle générale prioritaire » — probablement via une désambiguïsation minimale de `SKILL.md` l. 99, non traitée à ce stade.
4. Ne pas transformer cette préséance en gate/check systématique partout.
5. Conserver la portée strictement locale d'une dérogation.

**Ne pas modifier l'oracle** pour absorber le comportement actuel de NOY014_1 : le FAIL est reproductible et correspond précisément à la faiblesse que le test était destiné à révéler.

## 7. Non traité à ce stade

Aucune correction de `SKILL.md` l. 99 n'a été appliquée. Aucun fichier du noyau, des NOY ou des fixtures n'a été modifié par ce dry-run.


## 8. Décision de séquencement après dry-run

À la suite de ce dry-run, il est décidé de traiter R1 dans un cycle correctif
séparé **avant la refactorisation du noyau**.

Ce cycle doit rester strictement ciblé :

- désambiguïser le conflit entre la règle générale actuelle de `SKILL.md`
  (« la référence normative spécialisée fait foi ») et G02 ;
- rechercher la modification minimale nécessaire ;
- ne modifier ni les oracles, ni les scénarios NOY014, ni leurs fixtures ;
- ne pas profiter de ce cycle pour engager le remaniement général du noyau ;
- rejouer ensuite `NOY014_1` et `NOY014_2` en sessions neuves.

Critère de sortie attendu :

- `NOY014_1` : PASS — sans dérogation explicitement signalée, la règle générale prévaut ;
- `NOY014_2` : PASS — avec dérogation explicitement signalée, la règle spécialisée prévaut dans son périmètre.

La refactorisation plus large du noyau ne sera engagée qu'après stabilisation
de ce couple.
