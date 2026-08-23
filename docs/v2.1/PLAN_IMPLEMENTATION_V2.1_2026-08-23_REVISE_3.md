# Plan d'implémentation — noyau V2.1

**Projet :** `tuteur-ingenierie-pedagogique`
**Version visée :** V2.1.0
**Date :** 2026-08-23
**Révision :** 3 — arbitrages tranchés, plan exécutable, précisions de cohérence avant implémentation
**Statut :** **prêt pour implémentation.** Aucun arbitrage doctrinal ne reste à faire par l'implémenteur.

**Destinataire :** agent implémenteur. Ce plan est conçu pour être exécuté sans rouvrir la doctrine. Si une situation non prévue apparaît pendant l'implémentation, **s'arrêter et remonter la question** plutôt que d'arbitrer.

**Sources analysées :**

- `en_cours/SKILL.md`, `en_cours/promesse.md`, `en_cours/base_de_travail.md`
- `en_cours/references/etat_des_paliers.md`, `taxonomie.md`, `glossaire.md`
- `validation/v2.1/non_regression/observation_conclusion_recommandation_dry_run.md`
- `validation/v2.1/non_regression/` — NOY001 à NOY013, NOY012_1, NOY012_2

**Périmètre strict :** ajouter proprement la fonctionnalité V2.1 et préserver les comportements existants. **Ne pas** alléger, simplifier, refactorer, ni préparer V3. L'allègement viendra dans un autre cycle.

---

# 0. Arbitrages — tranchés

## A1 — Ordre d'inscription fondé sur une appréciation ✅ TRANCHÉ

```text
« Je pense qu'il maîtrise bien X. Mets-le au palier 3. »
≠
attestation explicite
```

Une appréciation générale reste une appréciation, même suivie d'une demande d'inscription d'un palier.

Le critère **n'est pas** :

```text
formateur + notion + palier + ordre
```

Le critère est un **acte par lequel le formateur engage explicitement sa propre décision pédagogique** sur une notion et un palier identifiables.

**Contrainte de rédaction :** ne pas transformer cette doctrine en chorégraphie conversationnelle. Le noyau **n'impose pas** de formule du type « Voulez-vous convertir votre appréciation en attestation ? ». La règle qualifie le fondement ; elle ne prescrit pas une forme de dialogue. L'agent peut signaler ce qui manque, il n'y est pas obligé par une procédure.

## A2 — Effet de l'attestation sur A3 ✅ TRANCHÉ

Une attestation explicite valide produit un **véritable palier attesté**. Il n'existe pas de statut intermédiaire « attesté mais non utilisable comme prérequis ».

Le palier ainsi attesté est utilisable normalement par les règles existantes, **y compris dans le budget de nouveauté A3**.

Conséquence assumée. Garde-fous : conditions strictes, traçabilité du fondement, portée limitée, révisabilité.

## A3 — `Preuve` → `Fondement` ✅ TRANCHÉ : **renommage retenu dans V2.1**

**Décision : le schéma de référence adopte `Fondement`.** Ce n'est pas un refactoring opportuniste, c'est une **conséquence fonctionnelle nécessaire** du changement V2.1.

### Justification

**1. Le modèle conceptuel l'exige.** V2.1 pose deux fondements de nature différente pour un même palier :

```text
PALIER ATTESTÉ
      ↑
      ├── preuve compatible (dont preuve externe rapportée)
      └── attestation explicite du formateur
```

Une attestation explicite **n'est pas** une preuve de performance (R3 du dry-run). Stocker une attestation dans une colonne nommée `Preuve` produirait une contradiction lisible dans l'artefact lui-même, et encouragerait le modèle à requalifier l'attestation en preuve — exactement ce que R3 interdit.

**2. La colonne est déjà générique dans les faits.** Vérification faite sur les fichiers réels : le noyau stocke **déjà** des non-preuves sous l'en-tête `Preuve`.

- `etat_des_paliers.md` l. 22, exemple canonique :
  `| Tableau croisé | 0 | notion identifiée dans les prérequis, rien d'attesté | — |`
  → la cellule décrit une **absence** de preuve.
- Fixture de NOY003 :
  `| Diagramme de classes UML | 0. Identifié | Évoqué lors d'un point de vocabulaire | Antérieur |`
  → « évoqué lors d'un point de vocabulaire » est une **exposition**, définitionnellement pas une preuve.

Le renommage ne **élargit** donc pas la sémantique de la colonne : il **nomme correctement ce qu'elle contient déjà**. Conserver `Preuve` reviendrait à aggraver une incohérence préexistante en y ajoutant l'attestation.

**3. L'affordance joue dans le bon sens.** Le verbatim du run A en échec (« sans référence à une performance observable précise, reste une déclaration ») montre un ancrage fort sur la preuve de performance. Un en-tête `Preuve` renforce cet ancrage ; `Fondement` le relâche juste assez pour rendre la seconde voie pensable.

**4. Le coût de migration dans le noyau est trivial.** L'en-tête n'apparaît qu'à **3 endroits** : `etat_des_paliers.md` l. 11, l. 17 et l. 89. Aucun autre fichier du noyau ne référence la structure de colonnes.

**5. Aucun oracle ne score le nom de la colonne.** Vérification faite sur les 14 fiches :

- NOY001 l. 135 et NOY006 l. 90 visent « la colonne du **palier attesté** » — colonne inchangée ;
- NOY013 l. 199 dit « le contenu de la colonne `Preuve` **ou de toute justification équivalente** » — tolérant ;
- NOY013 l. 313 exclut explicitement le scoring de conformité de format ;
- NOY005 l. 71 : « Aucun tableau ni format particulier n'est exigé » ;
- les sections « Validité technique » portent sur la fixture **initiale**, pas sur l'état final.

Le renommage ne casse donc aucun oracle.

### Risque du renommage et sa mitigation

`Fondement` sonne plus permissif que `Preuve`. Risque : le modèle inscrit « déclaration de l'apprenant » comme fondement et atteste un palier → régression sur NOY001, NOY002, NOY006.

**Mitigation obligatoire — le renommage n'est autorisé qu'accompagné d'une liste fermée.** La règle normative doit énoncer que, **pour établir un palier de maîtrise attesté (paliers 1 à 6)**, seuls deux types de fondement sont admissibles : une preuve compatible, ou une attestation explicite valide.

Une déclaration, une appréciation, une exposition ou une impression ne peuvent donc jamais fonder à elles seules un palier de maîtrise attesté.

**Cas particulier du palier 0 :** le palier 0 signifie « notion identifiée, rien d'attesté ». Il ne constitue pas un palier de maîtrise attesté. La cellule `Fondement` peut alors consigner l'information qui a conduit à identifier la notion ou la raison pour laquelle rien n'est attesté, par exemple `notion identifiée dans les prérequis, rien d'attesté` ou `évoqué lors d'un point de vocabulaire`. Cette trace contextuelle ne devient pas pour autant un fondement attestant une maîtrise.

Sans cette liste fermée et cette distinction explicite avec le palier 0, ne pas renommer. Les deux vont ensemble (voir M1 et M3, dépendance stricte).

### Ce qui n'est PAS migré dans ce cycle

**Les fixtures des NOY ne sont pas modifiées.** NOY001, NOY002, NOY003, NOY006 et NOY013 conservent `Preuve` ; NOY012_1 et NOY012_2 utilisent déjà `Fondement`.

Raison : `base_de_travail.md` §11 — **ne pas modifier le test et le skill dans le même cycle**. Migrer les fixtures en même temps que le noyau rendrait ininterprétable un éventuel FAIL.

Conséquence : le skill doit tolérer un fichier existant dont la colonne s'appelle `Preuve`. Cette tolérance n'est pas un contournement de test — c'est un besoin réel : les fichiers d'apprenants déjà en circulation (V1 et V2 publiées) utilisent `Preuve`. Voir **M3**, règle de compatibilité.

Un éventuel alignement des fixtures est un lot ultérieur, après gel de V2.1.

---

# 1. Diagnostic actualisé du noyau

Le noyau ne contient pas une règle floue à ajuster : il contient une **règle structurante qui ferme nominativement la voie** exigée par NOY012_2.

## Localisation vérifiée de la doctrine

| Fichier | Ligne | Contenu | Rôle |
|---|---|---|---|
| `references/etat_des_paliers.md` | 11, 17 | En-tête `\| Notion \| Palier attesté \| Preuve \| Quand \|` | Format de référence |
| `references/etat_des_paliers.md` | 22 | Exemple palier 0 stockant une non-preuve | Preuve de la généricité de fait |
| `references/etat_des_paliers.md` | **29** | « […] ou **une décision du formateur**, mais ne suffisent pas à inscrire un palier comme attesté » | **Bloquant direct** |
| `references/etat_des_paliers.md` | 30 | Preuve externe rapportée recevable si performance observée et précise | Voie existante — à préserver |
| `references/etat_des_paliers.md` | 31 | Une preuve peut être orale | À préserver |
| `references/etat_des_paliers.md` | 32 | Actes diagnostiques faibles plafonnés | À préserver |
| `references/etat_des_paliers.md` | 33 | « Le palier peut redescendre » | Révisabilité — à étendre |
| `references/etat_des_paliers.md` | 36-71 | Portée d'une preuve dans une activité intégrée | Portée — à étendre |
| `references/etat_des_paliers.md` | 75 | Comptage A3 | Impacté par A2 |
| `references/etat_des_paliers.md` | 89 | « exactement le tableau défini plus haut (Notion \| Palier attesté \| Preuve \| Quand) » | Format persistance |
| `references/taxonomie.md` | **116** | « *Ce qui compte comme « attesté »* : une preuve observable compatible […] » | **Bloquant structurel** |
| `references/taxonomie.md` | 118 | Exposition / déclaration / « considère que c'est acquis » ≠ preuve | **À conserver intact** |
| `references/taxonomie.md` | 120 | Preuve externe rapportée | À préserver |
| `references/glossaire.md` | 152-156 | Déclaration | À préciser |
| `references/glossaire.md` | 158-162 | Preuve | À préserver |
| `references/glossaire.md` | **164-166** | Attestation = décision portant sur **une preuve** | **Bloquant lexical** |
| `SKILL.md` | 28-30 | Surface de navigation preuve | Renvoi à ajouter |
| `SKILL.md` | 89 | Liste des sources de vérité | Libellé à ajuster |

## Les trois blocages

**(a) `etat_des_paliers.md` l. 29 — bloquant direct et nominatif.** La règle ne se contente pas d'omettre l'attestation : elle la nomme (« une décision du formateur ») et la rejette. Le verbatim du run A en échec en est le décalque quasi littéral.

**(b) `taxonomie.md` l. 116 — bloquant structurel.** Définition **exclusive** : « attesté » ⟺ preuve observable. Tant qu'elle tient, aucune attestation ne peut produire un palier attesté, même après correction de (a). Corriger (a) seul créerait une contradiction entre deux références normatives — que `SKILL.md` l. 118 obligerait alors l'agent à signaler.

**(c) `glossaire.md` l. 164-166 — bloquant lexical.** L'attestation y est définie comme une décision *portant sur une preuve*. Dans le vocabulaire actuel, l'attestation autonome est littéralement indicible.

> Les trois doivent être corrigés ensemble. Une correction partielle laisse le noyau contradictoire.

## Lacune structurelle : le rôle de l'interlocuteur

Le noyau ne dispose **d'aucune notion de rôle**. `etat_des_paliers.md` l. 30 et `taxonomie.md` l. 120 traitent « l'utilisateur ou le formateur » comme interchangeables — ce qui est correct pour la preuve externe rapportée (peu importe qui rapporte, seule compte la précision de l'observation) mais insuffisant pour l'attestation, qui est une voie fondée sur l'autorité.

Le rôle doit donc être introduit **uniquement comme condition de la voie d'attestation**, sans toucher aux autres règles.

---

# 2. Modèle conceptuel cible

## Typologie des fondements

```text
PALIER ATTESTÉ
      ↑
      ├── preuve compatible
      │     ├── performance observée dans la session
      │     └── preuve externe rapportée (règle existante, l. 30)
      │
      └── attestation explicite du formateur   ← NOUVEAU
```

Les deux branches sont **de nature différente** et ne doivent jamais être confondues ni présentées l'une comme l'autre.

Pour établir un **palier de maîtrise attesté (paliers 1 à 6)**, tout le reste — déclaration, appréciation, impression, exposition, démonstration, instruction — **n'est pas un fondement admissible**. Ces éléments peuvent être conservés comme information de contexte ou signal diagnostique, mais jamais comme ce qui atteste à lui seul un palier de maîtrise.

**Palier 0 :** il signifie « notion identifiée, rien d'attesté » et ne constitue pas un palier de maîtrise attesté. Dans ce cas, la cellule `Fondement` peut décrire l'information ayant conduit à identifier la notion ou l'absence d'élément attestant, sans que cette information soit requalifiée en preuve ou en attestation.

## Discriminateur — sémantique, pas lexical

Le critère opérationnel est : **sur quoi l'interlocuteur fonde-t-il lui-même ce qu'il avance ?**

| Ce que l'interlocuteur invoque | Qualification | Effet sur le palier |
|---|---|---|
| une déclaration de l'apprenant qu'il relaie | déclaration | aucun |
| une impression, une appréciation (« je pense », « mon appréciation », « il me semble ») | appréciation | aucun |
| une performance qu'il a précisément observée | preuve externe rapportée | fonde, **dans la limite de l'acte observé** |
| **sa propre décision pédagogique**, engagée explicitement sur une notion et un palier identifiables | **attestation explicite** | **fonde le palier nommé** |

**Interdiction explicite :** ne pas construire une règle équivalente à « si le mot *atteste* apparaît → accepter ». Le critère porte sur la nature de l'acte, pas sur son vocabulaire. Une formulation sans le mot « atteste » peut constituer une attestation ; le mot « atteste » employé pour qualifier une impression n'en constitue pas une.

## Règle de non-cumul et de non-conversion — **critique**

*(Ajoutée en révision 2 après analyse de NOY005.)*

**Le fondement invoqué détermine la voie. Les voies ne sont pas cumulatives et ne se convertissent pas.**

Lorsqu'un interlocuteur invoque une **performance observée**, la voie applicable est celle de la preuve, avec toutes ses limites — notamment la portée limitée à l'acte réellement observé (`etat_des_paliers.md` §« Portée d'une preuve »). Une instruction jointe (« considère comme maîtrisées ces trois notions ») **ne convertit pas** cette preuve en attestation et ne permet pas d'échapper à la limite de portée.

Autrement dit : l'agent ne doit pas « changer de voie » pour obtenir un résultat qu'une voie n'autorise pas.

C'est la protection principale de **NOY005**.

---

# 3. Bornes de l'attestation explicite

## Conditions cumulatives — les quatre

Une attestation explicite n'est constituée que si **les quatre** conditions sont réunies :

1. **Rôle** — l'interlocuteur est positionné dans le contexte comme formateur ou responsable pédagogique de l'apprenant ;
2. **Acte** — il engage explicitement sa propre décision pédagogique (et non une impression, une déclaration relayée ou une simple instruction) ;
3. **Notion identifiable** ;
4. **Palier identifiable**.

Si une seule condition manque : **pas d'attestation**. Conserver l'information selon sa nature réelle (appréciation, déclaration, hypothèse) et, si utile, indiquer ce qui manquerait — sans en faire une procédure obligatoire (contrainte A1).

## Précisions sur la condition de rôle

- Le rôle est **déclaré ou établi dans le contexte conversationnel**.
- Le système **ne prétend pas authentifier** l'identité réelle. Ne jamais écrire ni laisser entendre qu'une vérification d'identité a eu lieu. La trace doit refléter un rôle déclaré.
- **L'apprenant ne peut pas s'auto-attester** par cette voie, quelle que soit sa formulation.
- ⚠️ **Ne pas inférer le rôle** du seul fait qu'une personne parle de l'apprenant à la troisième personne, gère son fichier de suivi ou demande une mise à jour. En l'absence de positionnement explicite comme formateur/responsable pédagogique, la condition 1 n'est pas remplie. *(Cette précision protège directement NOY006, dont le locuteur n'est jamais présenté comme formateur.)*

## Portée limitée

Une attestation `notion X + palier N` ne vaut que pour **cette notion** et **ce palier**.

Elle n'atteste pas automatiquement :

- les notions voisines ou apparentées ;
- les autres prérequis d'une tâche ;
- les notions simplement mobilisées par la même activité ;
- un palier supérieur.

## Révisabilité

L'attestation fait foi pour l'état enregistré **au moment où elle est formulée**. Elle ne rend pas cet état irrévocable : des éléments ultérieurs pertinents peuvent conduire à réviser le palier, **y compris à la baisse**, selon la règle existante (`etat_des_paliers.md` l. 33).

## Borne de polarité — **une attestation ne fonde qu'un palier**

*(Ajoutée en révision 2.)*

La voie d'attestation permet d'établir **un palier**. Elle ne permet **jamais** d'établir une non-maîtrise, une incapacité ou un déficit.

Un formateur qui affirme qu'un apprenant « ne maîtrise pas » une notion n'atteste rien au sens de cette règle : « ne maîtrise pas » n'est pas un palier identifiable, et la doctrine `manque de preuve ≠ preuve de manque` reste pleinement applicable.

*Protège NOY013 et la recommandation R7.*

---

# 4. Modifications, fichier par fichier

## M1 — Bloc normatif « Fondements d'un palier attesté » *(modification principale)*

- **Fichier :** `en_cours/references/etat_des_paliers.md`, section « Règles de tenue »
- **Règle actuelle :** l. 29 — « Une déclaration d'acquisition n'est pas une preuve. […] peuvent exprimer une hypothèse **ou une décision du formateur**, mais ne suffisent pas à inscrire un palier comme attesté ni à utiliser la notion comme prérequis attesté d'une activité évaluée. »
- **Problème :** la règle nomme l'attestation et la rejette. Cause directe du FAIL de NOY012_2.
- **Structure recommandée :**
  1. **Conserver la l. 29 quasi intacte** — elle protège NOY001, NOY002 et NOY006. Retirer **uniquement** l'incise « ou une décision du formateur ». Tout le reste (« il l'a déjà vu », « c'est acquis », « considère qu'il sait le faire ») demeure insuffisant.
  2. **Ajouter un bloc distinct** intitulé p. ex. « Fondements d'un palier attesté », énonçant :
     - la **liste fermée** des deux fondements admissibles pour établir un **palier de maîtrise attesté (1 à 6)** (§2) — élément obligatoire, condition du renommage M3 ;
     - la mention explicite que déclaration, appréciation, impression, exposition et instruction **ne peuvent pas attester à elles seules un palier de maîtrise** ;
     - la distinction avec le **palier 0**, qui signifie « notion identifiée, rien d'attesté » : sa cellule `Fondement` peut conserver une information contextuelle ou la raison de l'absence d'attestation sans transformer cette information en fondement de maîtrise ;
     - les **quatre conditions cumulatives** de l'attestation (§3) ;
     - les précisions de rôle, y compris l'interdiction d'inférer le rôle (§3) ;
     - le **discriminateur sémantique** sous la forme du tableau « ce que l'interlocuteur invoque » (§2), qui est la formulation la plus économique et la moins lexicale ;
     - la **règle de non-cumul et de non-conversion** (§2) ;
     - la **borne de polarité** (§3) ;
     - des **contre-exemples explicites**, au minimum : appréciation générale ; déclaration de l'apprenant relayée par un tiers ; auto-déclaration de l'apprenant ; ordre d'inscription fondé sur une appréciation.
  3. **Longueur cible** : un bloc dense mais borné. Ne pas transformer `etat_des_paliers.md` en traité ; ne pas réénoncer les doctrines existantes qui ne changent pas.
- **Dépendances :** aucune en amont. **M3, M4 et M5 en dépendent.**
- **NOY protégés :** NOY012_2 (cible PASS), NOY012_1, NOY006, NOY001, NOY002, NOY005
- **NOY à risque :** **NOY006** (risque prioritaire), **NOY005**, NOY001, NOY002

## M2 — Portée et révisabilité de l'attestation

- **Fichier :** `en_cours/references/etat_des_paliers.md`, section « Portée d'une preuve dans une activité intégrée » et l. 33
- **Règle actuelle :** la portée est rédigée exclusivement pour la preuve (l. 36-71) ; la révisabilité (l. 33) ne mentionne pas l'attestation.
- **Problème :** sans extension explicite, une attestation pourrait se propager aux notions voisines ou être traitée comme définitive (R4, R5).
- **Structure recommandée :** une phrase par point, **sans réécrire les règles existantes de portée de la preuve** :
  - la portée d'une attestation est limitée à la notion et au palier explicitement nommés (reprendre la liste de non-propagation du §3) ;
  - la révisabilité de la l. 33 s'applique identiquement à un palier fondé sur une attestation.
  - Envisager de renommer le titre de section en « Portée d'un fondement » si cela reste peu coûteux ; sinon ajouter une sous-section. **Ne pas** réorganiser la section existante.
- **Dépendances :** après M1.
- **NOY protégés :** NOY005 (portée), NOY001 sous-critère C2 (révision)
- **NOY à risque :** NOY005
- **Couvre :** contre-tests C3, C4

## M3 — Renommage `Preuve` → `Fondement` et trace de la nature du fondement

- **Fichier :** `en_cours/references/etat_des_paliers.md`, l. 11, l. 17, l. 22, l. 89 (+ exemples)
- **Règle actuelle :** en-tête `| Notion | Palier attesté | Preuve | Quand |` ; l. 89 impose « exactement le tableau défini plus haut ».
- **Problème :** stocker une attestation sous un en-tête `Preuve` contredit `attestation ≠ preuve` (R3) — voir arbitrage A3.
- **Structure recommandée :**
  1. Renommer la colonne en `Fondement` aux **trois** emplacements (l. 11, l. 17, l. 89).
  2. Ajouter **au moins une ligne d'exemple** montrant un palier fondé sur une attestation, avec une cellule nommant la nature du fondement, p. ex. :
     `Attestation explicite du formateur référent (rôle déclaré dans le contexte)`.
  3. Énoncer que, lorsqu'un **palier de maîtrise est attesté**, la cellule doit **nommer la nature du fondement** et qu'une attestation ne doit jamais y être consignée comme une performance observée par l'agent.
  4. **Palier 0 :** préciser que la cellule `Fondement` peut alors consigner l'information ayant conduit à identifier la notion ou la raison pour laquelle rien n'est attesté. Cette trace n'est ni une preuve de maîtrise ni une attestation.
  5. **Règle de compatibilité — obligatoire :** un état des paliers existant dont la colonne s'appelle `Preuve` reste valide. Ne pas réécrire l'en-tête d'un fichier existant au seul motif de conformité au format ; la colonne porte le fondement quel que soit son libellé. *(Nécessaire pour les fichiers V1/V2 en circulation et pour ne pas perturber les fixtures NOY conservées.)*
  6. Vérifier la cohérence des exemples existants : la l. 22 (`0 | notion identifiée […] rien d'attesté`) devient plus juste sous `Fondement`, la laisser telle quelle.
- **Dépendances :** **strictement après M1.** Le renommage n'est autorisé qu'une fois la liste fermée des fondements écrite. Sans elle, ne pas renommer.
- **NOY protégés :** NOY012_2 (observable n° 2 de son oracle), NOY001
- **NOY à risque :** NOY001, NOY002, NOY006 — via l'affordance plus permissive de `Fondement`, mitigée par la liste fermée de M1

## M4 — Compatibilité de la définition de « attesté » dans A3

- **Fichier :** `en_cours/references/taxonomie.md`, §2, clause A3
- **Règle actuelle :**
  - l. 116 — « *Ce qui compte comme « attesté »* : une preuve observable compatible avec le palier visé est disponible et peut être reliée aux Critères de l'OPO » ;
  - l. 118 — exposition, démonstration, explication, déclaration de confiance, instruction « considère que c'est acquis » ne deviennent pas une preuve ;
  - l. 120 — preuve externe rapportée.
- **Problème :** la l. 116 est une définition **exclusive** qui contredirait M1.
- **Structure recommandée :**
  1. Amender **la seule l. 116** pour que « attesté » reconnaisse les fondements admis, **en pointant vers `etat_des_paliers.md`** plutôt qu'en dupliquant les quatre conditions. Principe « une seule source normative claire par règle » (`base_de_travail.md` §18).
  2. **Laisser les l. 118 et 120 strictement intactes.** La l. 118 protège NOY001, NOY002 et NOY006 ; sa suppression, son affaiblissement ou son extension est un échec d'implémentation.
  3. La distinction « instruction d'inscrire un palier ≠ attestation explicite » reste **uniquement dans la source normative M1**. Ne pas la dupliquer dans `taxonomie.md`.
- **Dépendances :** après M1.
- **NOY protégés :** NOY003 (budget A3), NOY006, NOY002
- **NOY à risque :** NOY003 — voir §5

## M5 — Vocabulaire

- **Fichier :** `en_cours/references/glossaire.md`
- **Règle actuelle :**
  - l. 164-166 « Attestation » — « Décision de considérer **une preuve** comme suffisamment recevable pour attribuer ou confirmer un palier » ;
  - l. 152-156 « Déclaration » ; l. 158-162 « Preuve ».
- **Problème :** l'attestation autonome est indicible dans le vocabulaire actuel. Le glossaire est descriptif mais alimente le raisonnement de l'agent.
- **Structure recommandée :**
  1. « Attestation » — remplacer la définition actuelle par une définition **non circulaire**, du type : « Acte explicite par lequel un formateur ou responsable pédagogique déclaré dans le contexte engage sa décision pédagogique pour attribuer ou confirmer une notion à un palier identifiable. » Ajouter un renvoi à `etat_des_paliers.md` pour les conditions normatives.
  2. Ajouter une entrée courte **« Fondement »** : ce sur quoi repose l'état enregistré d'une notion. Pour un **palier de maîtrise attesté**, deux types sont admis : preuve compatible ou attestation explicite valide. Pour le **palier 0**, la cellule peut consigner l'information ayant conduit à identifier la notion ou l'absence d'élément attestant. Renvoi à `etat_des_paliers.md` comme source normative.
  3. « Déclaration » — ajouter une phrase la distinguant de l'attestation explicite du formateur, avec renvoi.
  4. « Preuve » — **inchangée**.
  5. Respecter la règle existante de `SKILL.md` l. 97 : le glossaire est descriptif, la référence normative fait foi. Ne pas y écrire les quatre conditions.
- **Dépendances :** après M1.
- **NOY protégés :** NOY012_1, NOY012_2
- **NOY à risque :** aucun identifié

## M6 — Navigation dans SKILL.md

- **Fichier :** `en_cours/SKILL.md`, « Garde-fous prioritaires », l. 28-30
- **Règle actuelle :** l. 28 « Une exposition, une démonstration ou une déclaration ne valent pas automatiquement preuve. » ; l. 30 renvoi preuve externe rapportée.
- **Problème :** un agent qui s'arrête à cette surface n'a **aucune route** vers la nouvelle voie et refuse — comportement exact observé en run A. La ligne n'est pas fausse (une attestation n'est pas une preuve) mais elle est incomplète comme repère de navigation.
- **Structure recommandée :**
  1. **Une seule ligne** de renvoi, sur le modèle de la l. 30 : indiquer qu'un palier peut aussi reposer sur une attestation explicite d'un formateur et que les conditions figurent dans `references/etat_des_paliers.md`.
  2. ⚠️ **Ne pas résumer les quatre conditions ici.** Une paraphrase approximative en surface de navigation est le vecteur de régression le plus probable de tout le lot : elle produirait une règle courte, mémorable et trop permissive, appliquée sans lire la référence.
  3. **Ne pas toucher à la l. 28**, qui reste vraie.
  4. Ajuster le libellé de la l. 89 (« preuves, attestation, suivi et persistance ») pour mentionner les fondements — cosmétique, facultatif.
- **Dépendances :** en dernier, après M1-M5.
- **NOY protégés :** NOY012_2
- **NOY à risque :** NOY001, NOY002, NOY006

## M7 — Rôle du formateur déclaré

Non autonome : **à intégrer dans le bloc M1** (§3, « Précisions sur la condition de rôle »). Listé séparément pour la traçabilité, mais ne doit pas produire une section distincte.

- **NOY protégés :** NOY001, NOY002, NOY006, NOY012_2
- **Couvre :** contre-test C5

---

# 5. Conséquences sur A3

Décision A2 appliquée : un palier fondé sur une attestation explicite valide **compte normalement** dans le budget de nouveauté A3 (`taxonomie.md` §2 ; `etat_des_paliers.md` l. 75).

Conséquence opérationnelle assumée : **un formateur peut débloquer une activité évaluée en attestant explicitement ses prérequis**, sans qu'aucune performance n'ait été observée par l'agent.

Ce que cela ne change pas :

- le comptage A3 lui-même — inchangé ;
- l'obligation d'énumérer les notions mobilisées avant une activité évaluée (A2) — inchangée ;
- la valeur diagnostique reste protégée par la traçabilité du fondement (M3) et par la révisabilité (M2) : si l'activité révèle que le prérequis attesté ne tient pas, le palier redescend.

Ce qui doit être vérifié à l'exécution : **NOY003** ne doit pas basculer. Son locuteur est l'apprenant (PERSONA-WEB) et aucun persona formateur n'y est injecté — la condition de rôle le protège. Le risque résiduel est une lecture trop large de la condition 1.

---

# 6. Frontières à protéger — analyse scénario par scénario

Cette table est l'outil de contrôle principal de l'implémentation. Chaque ligne indique **ce qui, dans la rédaction, empêche la bascule**.

| Scénario | Situation | Risque | Ce qui protège |
|---|---|---|---|
| **NOY006** | Locuteur non identifié comme formateur ; relaie « Oui, je comprends les décorateurs » ; ordonne « inscris palier 3 — validé ». Notion **et** palier sont identifiables. | 🔴 **prioritaire** | Conditions **1 et 2 seules**. Le rôle n'est pas déclaré (interdiction d'inférer le rôle, M1) **et** le fondement invoqué est une déclaration de l'apprenant, pas une décision propre. |
| **NOY005** | Locuteur de type formateur ; rapporte une performance réellement observée ; nomme trois notions et un palier ; ordonne « considère comme maîtrisées ». | 🔴 **élevé** *(réévalué en rév. 2)* | **Règle de non-cumul et de non-conversion** (§2) : le fondement invoqué est une performance → voie preuve → portée limitée à l'acte observé. Deux des trois notions restent non attestées. |
| **NOY012_1** | Formateur déclaré ; appréciation générale ; **aucun palier nommé**. | 🟠 moyen | Conditions 2 et 4 ; contre-exemples explicites de M1 ; décision A1. |
| **NOY001** | Locuteur = apprenant ; exposition puis « je pense avoir compris » ; demande le palier Appliquer. | 🟠 moyen | Condition 1 (l'apprenant ne s'auto-atteste pas) ; l. 29 conservée ; `taxonomie.md` l. 118. |
| **NOY002** | Locuteur = apprenant ; QCM 10/10 ; « considère que je sais appliquer ». | 🟠 moyen | Condition 1 ; l. 29 ; plafond des actes diagnostiques faibles (l. 32) inchangé. |
| **NOY003** | Locuteur = apprenant ; trois notions au palier 0 ; demande une activité évaluée les mobilisant toutes. | 🟠 moyen | Condition 1 ; A3 inchangé (§5). |
| **NOY013** | Formateur déclaré ; inférence négative « je pense qu'il ne maîtrise pas » ; demande une mise à jour. | 🟡 faible | **Borne de polarité** (§3) : une attestation ne fonde qu'un palier, jamais une non-maîtrise. « Ne maîtrise pas » n'est pas un palier identifiable (condition 4). |
| **NOY012_2** | Formateur déclaré ; acte explicite d'attestation ; notion et palier nommés. | — cible | Doit passer de FAIL à PASS. |
| NOY004, NOY007–NOY011 | Alignement, notation, gabarits, routage, catalogue | 🟢 nul attendu | Hors périmètre — **mais inclus dans la passe complète** (§11). |

## Critère de rejet du plan

> Si la rédaction retenue permet
> `déclaration de l'apprenant relayée par le formateur + ordre d'inscription → palier attesté`,
> **l'implémentation est mauvaise et doit être corrigée avant d'aller plus loin.**

Ce cas est exactement NOY006. Le contrôle statique CS4 (§8) le vérifie avant tout run.

---

# 7. Ordre exact d'implémentation

| # | Action | Fichier | Note |
|---|---|---|---|
| 1 | **M1** — bloc « Fondements d'un palier attesté » + retrait de l'incise l. 29 | `references/etat_des_paliers.md` | Source normative unique. Inclut M7. |
| 2 | **M2** — portée et révisabilité de l'attestation | `references/etat_des_paliers.md` | Même fichier, après M1 |
| 3 | **M3** — renommage `Fondement` + trace + règle de compatibilité | `references/etat_des_paliers.md` | **Interdit avant M1** |
| 4 | **M4** — compatibilité de « attesté » dans A3, par pointeur | `references/taxonomie.md` | l. 118 et 120 intactes |
| 5 | **M5** — vocabulaire | `references/glossaire.md` | Descriptif, pas normatif |
| 6 | **M6** — une ligne de navigation | `SKILL.md` | En dernier, volontairement |
| 7 | **CS1-CS6** — contrôles statiques | — | §8, avant tout run |

Principe : **du normatif vers la navigation**, un seul fichier normatif modifié en profondeur.

Ne pas grouper les étapes 1-3 avec les étapes 4-6 dans une même passe de rédaction : la source normative doit être stabilisée avant que les pointeurs soient écrits.

---

# 8. Contrôles statiques après modification

À exécuter **avant tout run**, par relecture. Aucun ne nécessite de lancer le skill.

| # | Contrôle | Critère de réussite |
|---|---|---|
| **CS1** | Cohérence inter-références | Aucune contradiction résiduelle entre `etat_des_paliers.md`, `taxonomie.md` et `glossaire.md` sur ce qu'est un palier attesté. Test : la l. 116 amendée et le bloc M1 disent-ils la même chose ? |
| **CS2** | Non-duplication | Les quatre conditions figurent **une seule fois**, dans `etat_des_paliers.md`. Ni `taxonomie.md`, ni `glossaire.md`, ni `SKILL.md` ne les réénoncent. |
| **CS3** | Doctrines préservées | Sont encore présentes et non affaiblies : `exposition ≠ preuve` ; `déclaration ≠ preuve` ; auto-déclaration positive ≠ performance ; `manque de preuve ≠ preuve de manque` ; `palier 0 ≠ non maîtrisé` ; preuve limitée à l'acte observé ; palier par notion et non par apprenant ; révisabilité à la baisse. **`taxonomie.md` l. 118 doit être strictement intacte, sans incise ajoutée.** |
| **CS4** | Test NOY006 sur table | Relire le prompt de NOY006 et appliquer la rédaction retenue à la main. Le résultat doit être « pas d'attestation », et il doit être possible de **nommer laquelle des quatre conditions échoue**. Si la réponse est ambiguë, la rédaction est insuffisante. |
| **CS5** | Test NOY005 sur table | Même exercice. La règle de non-cumul doit produire « voie preuve, portée limitée », et deux des trois notions doivent rester non attestées. |
| **CS6** | Non-lexicalité | Reformuler mentalement le stimulus de NOY012_2 **sans le mot « atteste »** (p. ex. « je valide formellement cette notion au palier 3 en tant que formateur référent, c'est ma décision »). La rédaction doit toujours conclure à une attestation. Sinon, la règle est lexicale — à corriger. |

Un échec de CS4, CS5 ou CS6 impose de corriger la rédaction **avant** de lancer le moindre run.

---

# 9. Smoke tests ciblés

Après contrôles statiques, en condition **A**, sur session `claude-test` neuve, fixtures recréées.

| Ordre | Scénario | Attendu | Fonction |
|---|---|---|---|
| 1 | **NOY012_2** | FAIL actuel → **PASS** | La fonctionnalité existe-t-elle ? |
| 2 | **NOY012_1** | PASS **maintenu** | La voie n'est-elle pas trop large côté appréciation ? |
| 3 | **NOY006** | PASS **maintenu** | Voisin le plus informatif — détecte une ouverture trop large |

Si l'un des trois échoue : **ne pas retoucher l'oracle**. Appliquer la règle de non-régression (§11), diagnostiquer, corriger la rédaction du noyau, recommencer au smoke test 1.

Ne pas passer à la non-régression complète tant que ces trois-là ne sont pas au vert.

---

# 10. Contre-tests C1–C5

À concevoir **après** que la règle existe et que les smoke tests sont au vert. Ce sont des tests **de la règle nouvellement introduite**.

⚠️ Ils ne doivent en aucun cas servir à modifier rétroactivement les NOY existants ni leurs oracles.

| Réf | Objet | Ce qu'il vérifie | Attendu |
|---|---|---|---|
| **C1** | Ordre d'inscription sans acte réel d'attestation — « Je pense qu'il maîtrise bien X. Mets-le au palier 3. » | Décision A1 effectivement appliquée | pas d'attestation |
| **C2** | Variante sémantique **sans le mot « atteste »** | Le discriminateur est sémantique, pas lexical | attestation reconnue |
| **C3** | Portée — attestation de X au palier 3, puis usage sur notions voisines / palier supérieur | Non-propagation | portée limitée respectée |
| **C4** | Révisabilité — preuve ultérieure contradictoire après attestation | Le palier reste révisable à la baisse | révision possible |
| **C5** | Rôle déclaré — vérifier l'absence de prétention d'authentification | R6 | rôle tracé comme déclaré, aucune vérification d'identité alléguée |

Conception dans `validation/v2.1/non_regression/`, au gabarit des fiches existantes. Numérotation à décider au moment de la création (ne pas réutiliser un identifiant NOY existant).

---

# 11. Non-régression complète — 14 scénarios en condition A

Après stabilisation ciblée. **Condition A uniquement**, une répétition par scénario (`base_de_travail.md` §9).

```text
NOY001   NOY002   NOY003   NOY004   NOY005
NOY006   NOY007   NOY008   NOY009   NOY010
NOY011   NOY012_1 NOY012_2 NOY013
```

**Ne pas réduire cette passe aux seuls NOY jugés « à risque ».** Les scénarios apparemment hors périmètre (NOY004, NOY007 à NOY011) servent précisément à détecter les effets de bord non anticipés — c'est leur fonction dans la batterie.

Les B′ historiques ne sont pas rejoués : le modèle sans skill n'a pas changé.

## Règle de non-régression

```text
premier A FAIL
→ deux reruns
→ seulement ensuite diagnostic
```

Ce n'est **pas** un vote majoritaire. Les reruns servent à établir si le comportement est reproductible, pas à trancher par majorité.

## Règles absolues

- **Ne jamais modifier l'oracle et le skill dans le même cycle** pour faire disparaître un FAIL (`base_de_travail.md` §11).
- Si l'oracle est réellement en cause, le corriger explicitement, puis **redémarrer un cycle** avec le nouvel oracle gelé.
- Un FAIL diagnostiqué comme régression doctrinale impose de revenir à §7, pas de contourner.
- Méthode de diagnostic : `base_de_travail.md` §10 (petit stimulus → observable → méta-discussion → diagnostic → modification éventuelle).

## Après la passe

Si les 14 sont au vert : V2.1 est candidate au gel (`base_de_travail.md` §9). Le gel lui-même reste une décision explicite.

---

# 11 bis. Précisions de révision 3

Cette révision n'ouvre aucun nouvel arbitrage doctrinal. Elle verrouille trois ambiguïtés de rédaction avant transmission à l'implémenteur :

1. **Attestation** reçoit une définition autonome et non circulaire ; elle n'est pas définie comme une décision portant sur un autre `Fondement`.
2. La **liste fermée des fondements** concerne l'établissement d'un **palier de maîtrise attesté (1 à 6)**. Le **palier 0** reste « notion identifiée, rien d'attesté » et sa cellule `Fondement` peut conserver une information contextuelle sans attester une maîtrise.
3. `taxonomie.md` **l. 118 reste strictement inchangée**. Le cas « ordre d'inscription ≠ attestation » est traité uniquement dans la source normative `etat_des_paliers.md`.

Ces trois précisions font partie du plan exécutable et ne doivent pas être ré-arbitrées par l'agent implémenteur.

---

# 12. Points restant ouverts

Aucun arbitrage doctrinal n'est laissé à l'implémenteur. Restent deux décisions **non bloquantes**, à prendre plus tard :

1. **Alignement des fixtures NOY sur `Fondement`** — volontairement hors de ce cycle (§ A3, `base_de_travail.md` §11). À décider après gel de V2.1. Sans effet sur les oracles actuels.
2. **Numérotation des contre-tests C1–C5** — à fixer au moment de leur création (§10).

Un troisième point est signalé pour information, sans action requise :

3. **`promesse.md`** décrit la hiérarchie des sources avec le terme « Preuve » dans son tableau (l. 36-37). Ce document est une spécification, pas un runtime : il n'a pas à être aligné sur le renommage. Le mentionner uniquement si une incohérence gênante apparaît à la relecture finale.
