# Fiche de désaveuglement — Validation V2

**Projet :** `tuteur-ingenierie-pedagogique`  
**Campagne :** V2 — 40 runs de base  
**Statut :** procédure post-scoring

## 1. Principe

Le désaveuglement est une opération **postérieure au gel des scorings**.

La table privée de correspondance produite lors de la construction du paquet aveugle
ne doit jamais être remise à un scoreur et ne doit jamais être incluse dans le paquet
aveugle.

Le désaveuglement sert uniquement à rattacher les identifiants `TRAJ-xxxx` aux
cellules expérimentales réelles après que les jugements aveugles ont été fixés.

## 2. Conditions obligatoires avant ouverture du mapping

Ne pas ouvrir ni exploiter la table privée tant que les conditions suivantes ne sont
pas toutes remplies :

- le paquet aveugle de base est gelé et son SHA-256 est conservé ;
- le scoring S1 couvre toutes les trajectoires et est gelé ;
- le scoring S2 couvre toutes les trajectoires et est gelé ;
- les SHA-256 des livrables S1 et S2 sont conservés ;
- la comparaison inter-scoreurs a été effectuée **sans mapping** ;
- les éventuels désaccords de scoring ont été traités par la procédure prévue,
  uniquement sur les trajectoires aveugles existantes ;
- les verdicts comportementaux retenus pour R1/R2 sont figés.

Un désaccord entre scoreurs ne déclenche jamais directement une répétition R3.

## 3. Localisation des pièces privées

La construction du paquet aveugle conserve les pièces de correspondance sous :

```text
/projets/skill/tests/validation_v2_40runs_2026-08-21/execution/private/
```

La fiche présente ne contient volontairement **aucune correspondance réelle**.

Avant désaveuglement, identifier les fichiers privés produits par
`OUTILS/build_blind_package.py` et vérifier leur empreinte.

## 4. Désaveuglement

Après franchissement du verrou décrit au §2 :

1. conserver une copie gelée des scorings aveugles ;
2. utiliser l’outil gelé `OUTILS/unblind_scores.py` ;
3. joindre la table privée aux verdicts par `blind_id` ;
4. rattacher chaque trajectoire au `planned_run_id`, au `scenario_id` et à la
   `condition` ;
5. récupérer la répétition depuis `RUNS.csv` si elle n’est pas directement portée
   par le mapping ;
6. écrire le résultat dans un **nouvel artefact** ; ne jamais réécrire les TSV
   aveugles d’origine.

Le CLI exact du script gelé fait foi. Vérifier son aide avant exécution :

```bash
python3 OUTILS/unblind_scores.py --help
```

## 5. Décision sur les R3

Après désaveuglement des verdicts R1/R2, construire les cellules :

```text
scenario_id + condition
```

Puis comparer les deux répétitions de base :

```text
R1 vs R2
```

Une R3 est déclenchable uniquement lorsque les deux trajectoires de la même cellule
sont techniquement valides et que leurs **verdicts comportementaux figés diffèrent**.

Exemple :

```text
R1 = PASS
R2 = FAIL
→ R3 peut être décidée
```

Ne pas lancer de R3 pour :

- résoudre un désaccord entre scoreurs ;
- améliorer un résultat défavorable ;
- augmenter artificiellement le contraste A/B′ ;
- remplacer un run techniquement valide.

La décision de lancer chaque R3 doit être consignée **avant connaissance de son
résultat**.

## 6. Si des R3 sont déclenchées

Les R3 autorisées sont exécutées conformément à `RUNS_CONDITIONNELS.csv`.

Elles sont ensuite collectées et scorées selon le même principe de séparation :

```text
collecte R3
→ gel
→ paquet aveugle conditionnel
→ scoring aveugle
→ gel des verdicts R3
→ désaveuglement R3
```

Ne pas mélanger les trajectoires R3 non scorées avec les verdicts de base.

## 7. Analyse finale

Une fois la base et les éventuelles R3 définitivement scorées et désaveuglées :

- analyser NOY001–NOY008 par scénario et condition ;
- analyser NOY009–NOY012 comme contrats A-only ;
- conserver les résultats nuls A≈B′ comme résultats expérimentaux recevables ;
- analyser séparément la consommation de tokens ;
- ne jamais modifier un oracle ou un verdict pour améliorer le contraste.

## 8. Traçabilité minimale à conserver

Conserver ensemble, mais dans des espaces clairement séparés :

```text
corpus brut gelé
paquet aveugle gelé
mapping privé
scoring S1 gelé
scoring S2 gelé
comparaison inter-scoreurs
adjudication éventuelle
décisions R3
résultats désaveuglés
analyse finale
```

La table privée de correspondance n’est jamais incluse dans un artefact remis aux
scoreurs.
