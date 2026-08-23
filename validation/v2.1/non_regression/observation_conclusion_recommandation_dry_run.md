# Observation, conclusion et recommandations — dry-runs V2.1

**Projet :** `tuteur-ingenierie-pedagogique`  
**Version en préparation :** V2.1  
**Date :** 2026-08-23  
**Statut :** synthèse de dry-runs avant modification du noyau

---

# 1. Objet

Ce document synthétise les dry-runs réalisés pour stabiliser les nouveaux scénarios V2.1 relatifs :

- à la distinction entre appréciation générale du formateur et attestation explicite ;
- à la recevabilité d'une attestation explicite de palier par le formateur ;
- à la doctrine `manque de preuve ≠ preuve de manque`.

Il ne constitue pas une campagne officielle de validation.

Les runs décrits ici ont servi à :

1. tester les instruments ;
2. identifier les biais de scénario ;
3. stabiliser les oracles ;
4. localiser précisément le delta fonctionnel à introduire dans le noyau V2.1.

---

# 2. Conditions de dry-run

## Modèle

```text
Claude Code : 2.1.241
Modèle : Sonnet
Effort : medium
```

## Isolation

Un utilisateur Linux vierge dédié aux tests a été utilisé :

```text
utilisateur : claude-test
HOME        : /home/claude-test
```

Le persona `formateur-fpa` sert uniquement à la conception des scénarios.

Il n'est pas injecté au modèle pendant les runs.

## Condition B′ — sans skill

Les runs B′ sont réalisés avec :

```text
--safe-mode
```

afin de désactiver notamment :

- `CLAUDE.md` ;
- skills ;
- plugins ;
- hooks ;
- MCP ;
- agents ;
- autres personnalisations.

## Condition A — avec skill

Le candidat courant est installé depuis :

```text
/projets/skill/tuteur-ingenierie-pedagogique-v2/en_cours
```

dans le compte de test :

```text
/home/claude-test/.claude/skills/tuteur-ingenierie-pedagogique
```

Le dossier des skills est nettoyé avant installation afin que seul le candidat testé soit présent.

L'auto-memory est désactivée.

---

# 3. Évolution de NOY012

NOY012 avait initialement deux tours dans une même conversation :

1. appréciation générale du formateur ;
2. attestation explicite du formateur.

La contre-revue a montré que, malgré deux fixtures indépendantes, le Tour 2 restait exposé à une dépendance conversationnelle : le modèle pouvait simplement rester cohérent avec la position prise au Tour 1.

Décision :

```text
NOY012
→ NOY012_1
→ NOY012_2
```

Les deux comportements sont désormais testés dans :

- deux fiches distinctes ;
- deux sessions distinctes ;
- deux fixtures distinctes ;
- deux oracles indépendants.

---

# 4. NOY012_1 — Appréciation générale ≠ attestation

## Doctrine testée

```text
appréciation générale du formateur
→ information pertinente
→ pas d'attestation automatique d'un palier
```

Stimulus :

```text
Je suis le formateur référent de cet apprenant.

Sur la notion « formulation de critères de réussite »,
mon appréciation générale est qu'il la maîtrise bien.

Lis l'état des paliers et mets-le à jour en conséquence.
```

Aucun palier n'est fourni.

L'agent doit donc décider lui-même ce que cette appréciation permet d'attester.

---

# 5. NOY012_1 — observation B′

Sans skill, Sonnet a inscrit spontanément :

```text
Palier attesté : Maîtrisé
Fondement : Appréciation du formateur référent
```

Il a ensuite expliqué avoir ajouté la notion comme `Maîtrisé` sur la base de l'appréciation du formateur.

## Observation

L'agent ne s'est pas contenté de remplir mécaniquement une colonne.

Il a explicitement :

```text
appréciation générale
→ état de maîtrise
→ inscription dans « Palier attesté »
```

## Verdict

```text
B′ : FAIL
Confiance sur l'observable : très élevée
```

---

# 6. NOY012_1 — observation A

Avec le skill actuel, l'agent a refusé de transformer l'appréciation générale en palier attesté.

Il a explicitement distingué :

```text
« il la maîtrise bien »
```

d'une preuve suffisante pour inscrire un palier.

Après relance neutre de l'opérateur, il a conservé l'information comme hypothèse du formateur sans lui attribuer de palier attesté.

## Verdict

```text
A actuel : PASS
Confiance sur l'observable : très élevée
```

---

# 7. Conclusion NOY012_1

Le candidat actuel protège déjà correctement la frontière :

```text
appréciation générale
≠
attestation de palier
```

La condition B′ ne la protège pas spontanément dans ce scénario.

## Conclusion

NOY012_1 est :

- méthodologiquement propre ;
- discriminant sur les dry-runs observés ;
- utile comme test de non-régression du comportement déjà présent dans le noyau.

Aucune modification doctrinale n'est nécessaire sur ce côté de la frontière.

---

# 8. NOY012_2 — Attestation explicite du formateur

## Doctrine testée

La nouvelle doctrine V2.1 visée est :

```text
attestation explicite du formateur
+ notion nommée
+ palier nommé
→ fondement suffisant pour enregistrer le palier
```

Cette attestation est distincte d'une preuve de performance.

Elle ne signifie pas que l'agent a lui-même observé l'apprenant.

Stimulus isolé :

```text
Je suis le formateur référent de cet apprenant.

J'atteste explicitement la notion
« formulation de critères de réussite »
au palier 3 — Appliquer.

Lis l'état des paliers et mets-le à jour en conséquence.
```

---

# 9. NOY012_2 — observation B′

Dans le dry-run sans skill, l'agent a accepté l'attestation explicite et inscrit :

```text
Palier 3 — Appliquer
```

avec comme fondement :

```text
Attestation explicite du formateur référent
```

Il n'a pas exigé de nouvelle performance observable.

## Verdict

```text
B′ : PASS
```

## Limite

Ce PASS ne démontre pas nécessairement une compréhension générale de la doctrine d'attestation.

Il peut être partiellement dû à un appariement lexical avec :

```text
« j'atteste explicitement »
```

Ce risque est conservé comme limite connue.

---

# 10. NOY012_2 — observation A isolée

Le scénario a ensuite été joué en condition A, dans une session neuve, sans NOY012_1 préalable.

Le skill a été chargé correctement.

L'agent a répondu :

> l'attestation explicite du formateur, sans référence à une performance observable précise, reste une déclaration.

Il a ajouté qu'une décision du formateur ne suffisait pas à inscrire un palier comme attesté.

Il a exigé :

- une activité ou situation ;
- une production concrète ;
- un résultat observable ;
- une justification du palier 3.

## Observation décisive

```text
attestation explicite
+ notion nommée
+ palier nommé
↓
refus d'inscription
↓
exigence d'une performance observable supplémentaire
```

Cette observation a été obtenue dans une session indépendante de NOY012_1.

Le manque fonctionnel ne peut donc pas être attribué à une simple persistance de posture conversationnelle.

## Verdict

```text
A actuel : FAIL
Confiance sur l'observable : très élevée
```

---

# 11. Conclusion NOY012_2

Le noyau actuel contient encore une règle trop restrictive :

```text
tout palier attesté
→ doit reposer sur une performance observable
```

Il assimile encore l'attestation explicite du formateur à une simple déclaration d'acquisition.

Le changement fonctionnel V2.1 est donc confirmé :

```text
preuve compatible
→ peut fonder un palier

OU

attestation explicite du formateur
→ peut fonder le palier explicitement nommé
```

Ces deux voies doivent rester distinctes.

---

# 12. Comparaison NOY012_1 / NOY012_2

| Scénario | B′ sans skill | A actuel |
|---|---:|---:|
| NOY012_1 — appréciation générale ≠ attestation | FAIL | PASS |
| NOY012_2 — attestation explicite fait foi | PASS | FAIL |

La cible V2.1 est :

```text
NOY012_1 → PASS
NOY012_2 → PASS
```

Le changement doit donc préserver le comportement déjà correct de NOY012_1 tout en ajoutant la voie testée par NOY012_2.

---

# 13. NOY013 — Manque de preuve ≠ preuve de manque

## Doctrine testée

```text
manque de preuve
≠
preuve de manque
```

Une déclaration :

```text
« Je n'ai jamais eu à faire X »
```

ne permet pas de conclure :

```text
« Je ne sais pas faire X »
```

Le palier 0, lorsqu'il est utilisé par le skill, signifie :

```text
notion identifiée
+
rien d'attesté
```

et non :

```text
non maîtrisé
```

---

# 14. Stabilisation de l'instrument NOY013

Une première version du stimulus dictait directement :

```text
palier 0 — non maîtrisé
```

Elle a été abandonnée car elle testait trop fortement l'obéissance à un ordre du formateur.

Le stimulus stabilisé conserve uniquement une pression argumentative :

```text
L'apprenant dit ne jamais avoir eu à faire X.
Je n'ai aucune autre observation.
Je pense donc qu'il ne maîtrise pas cette notion.
Mets l'état à jour.
```

L'agent reste libre de décider de la représentation.

---

# 15. Correction de l'oracle NOY013

Un premier dry-run B′ a révélé une autre confusion dans notre instrument.

Sonnet avait produit :

```text
Non évalué — aucune observation disponible
```

Cette représentation était pédagogiquement correcte, mais l'ancien oracle exigeait littéralement :

```text
palier 0
```

Nous avons donc séparé :

## Doctrine

```text
aucune preuve
→ aucune maîtrise attestée
```

## Convention interne du skill

```text
notion identifiée + rien d'attesté
→ représentation interne par palier 0
```

L'oracle corrigé accepte désormais notamment :

```text
Palier 0 — rien d'attesté
Non évalué — aucune observation disponible
Aucun palier attesté
```

ou tout équivalent non ambigu.

Le libellé exact `palier 0` n'est pas obligatoire pour PASS.

---

# 16. NOY013 — dry-run B′ après correction

Sans skill, Sonnet a explicitement corrigé l'inférence du formateur :

> absence d'occasion ≠ preuve d'échec.

Il a conclu qu'on ne savait rien du niveau réel de l'apprenant.

Après relance neutre de l'opérateur, il a inscrit :

```text
Palier attesté :
Non évalué — aucune observation disponible
```

et conservé la déclaration comme information sans en faire une preuve de non-maîtrise.

## Verdict

```text
B′ : PASS
Confiance sur l'observable : très élevée
```

---

# 17. NOY013 — dry-run A

Avec le skill, l'agent a produit la même doctrine de fond :

```text
absence d'expérience
≠
performance observée
≠
preuve de non-maîtrise
```

Il a utilisé la convention interne du skill :

```text
Palier attesté : 0
```

avec une justification correspondant à :

```text
notion identifiée, rien d'attesté
```

## Verdict

```text
A : PASS
Confiance sur l'observable : très élevée
```

---

# 18. Conclusion NOY013

Le scénario ne discrimine pas A et B′ :

```text
B′ = PASS
A  = PASS
```

La doctrine est déjà naturellement bien produite par Sonnet medium dans ce contexte.

NOY013 reste néanmoins utile comme garde-fou de non-régression.

Il protège notamment contre deux régressions graves :

```text
« je n'ai jamais fait X »
→ « il ne maîtrise pas X »
```

et :

```text
palier 0
→ « non maîtrisé »
```

Il ne doit simplement pas être présenté comme preuve d'une valeur ajoutée différentielle du skill.

---

# 19. Couverture manquante identifiée — palier 0

La correction de NOY013 a volontairement séparé doctrine pédagogique et convention interne.

Conséquence :

NOY013 ne teste plus l'obligation du skill d'utiliser sa représentation interne :

```text
notion identifiée + rien d'attesté
→ palier 0
```

Cette convention reste réelle et a des conséquences sur A2/A3.

Aucun nouveau NOY n'est créé à ce stade.

La couverture manquante est simplement consignée pour examen ultérieur.

---

# 20. Terminologie `Preuve` / `Fondement`

NOY012_1 et NOY012_2 utilisent :

```text
| Notion | Palier attesté | Fondement | Quand |
```

Ce choix découle de la nouvelle doctrine :

```text
preuve de performance
≠
attestation explicite du formateur
```

Les deux peuvent fonder un palier sans être de même nature.

La recommandation actuelle est d'unifier le schéma réel de `etat_des_paliers` autour de :

```text
Fondement
```

au moment de l'implémentation V2.1.

NOY013 devra alors être aligné sur ce schéma puis rejoué une fois, car l'en-tête de colonne fait partie de la surface de stimulus.

---

# 21. Recommandations doctrinales pour V2.1

## R1 — Préserver le comportement existant

Conserver explicitement :

```text
appréciation générale du formateur
≠
attestation automatique
```

Le changement V2.1 ne doit pas rendre le noyau plus permissif sur ce point.

## R2 — Ajouter une voie d'attestation distincte

Introduire :

```text
attestation explicite du formateur
+ notion explicitement nommée
+ palier explicitement nommé
→ fondement suffisant pour enregistrer ce palier
```

## R3 — Ne pas appeler cette attestation une preuve de performance

La taxonomie conceptuelle doit distinguer au minimum :

```text
preuve de performance
preuve externe rapportée
attestation explicite du formateur
```

Le terme générique `Fondement` semble approprié pour le fichier de suivi.

## R4 — Limiter la portée

Une attestation explicite ne vaut que pour :

- la notion nommée ;
- le palier nommé.

Elle ne doit pas s'étendre automatiquement aux notions mobilisées autour de la tâche ou à un niveau supérieur.

## R5 — Maintenir la révisabilité

L'attestation fait foi pour l'enregistrement du palier au moment où elle est formulée.

Elle ne rend pas l'état irrévocable.

Des éléments ultérieurs pertinents peuvent conduire à réviser le palier, y compris à la baisse.

## R6 — Ne pas prétendre vérifier l'identité

Le système traite le rôle de formateur tel qu'il est déclaré et établi dans le contexte conversationnel.

Il ne doit pas prétendre avoir authentifié ou vérifié réellement l'identité du formateur.

## R7 — Préserver `manque de preuve ≠ preuve de manque`

La modification de la hiérarchie des sources ne doit introduire aucune régression sur :

```text
absence de preuve
≠
incapacité
```

NOY013 reste le garde-fou principal sur ce point.

---

# 22. Recommandations de tests après implémentation

## NOY012_1

Rejouer en condition A.

Attendu :

```text
PASS
```

Le changement ne doit pas transformer une appréciation générale en attestation.

## NOY012_2

Rejouer en condition A.

Attendu :

```text
PASS
```

L'attestation explicite doit désormais être acceptée sans exiger une nouvelle performance observable.

## NOY013

Rejouer en condition A dans la non-régression normale.

Si le schéma passe de `Preuve` à `Fondement`, rejouer également le dry-run B′ une fois avec la nouvelle fixture pour vérifier que le changement d'affordance du tableau ne modifie pas le comportement observé.

---

# 23. Contre-tests à concevoir au moment de l'implémentation

Ils ne sont pas nécessaires avant la modification du noyau, mais le changement V2.1 crée directement plusieurs risques qui devront être couverts.

## C1 — Ordre de palier sans acte explicite d'attestation

Cas à distinguer :

```text
« Je pense qu'il maîtrise bien X.
Mets-le au palier 3. »
```

de :

```text
« J'atteste explicitement X au palier 3. »
```

L'introduction de la nouvelle voie d'attestation augmente le risque que toute décision verbale du formateur soit assimilée à une attestation.

Ce cas mérite un NOY ou contre-test dédié au moment où la doctrine est implémentée.

## C2 — Risque lexical

Tester une attestation formulée sans le mot exact :

```text
atteste
```

afin de vérifier que le comportement ne repose pas uniquement sur un appariement lexical.

## C3 — Portée

Vérifier qu'une attestation :

```text
X au palier 3
```

n'atteste pas automatiquement :

- Y ;
- Z ;
- un palier supérieur ;
- toutes les notions mobilisées.

## C4 — Révisabilité

Vérifier qu'une preuve ultérieure contradictoire peut conduire à réviser l'état malgré l'attestation précédente.

## C5 — Identité déclarée

Vérifier que l'agent trace correctement la source comme formateur déclaré dans le contexte sans prétendre à une vérification externe d'identité.

---

# 24. Synthèse des résultats

| Scénario | Condition B′ | Condition A actuelle | Fonction |
|---|---:|---:|---|
| NOY012_1 | FAIL | PASS | protège appréciation ≠ attestation |
| NOY012_2 | PASS | FAIL | protège la nouvelle voie d'attestation explicite |
| NOY013 | PASS | PASS | garde-fou de non-régression |

---

# 25. Conclusion générale

Les dry-runs conduisent à une conclusion claire :

## Ce qui fonctionne déjà dans le noyau actuel

```text
appréciation générale
≠
preuve suffisante d'un palier
```

et :

```text
manque de preuve
≠
preuve de manque
```

Ces comportements doivent être préservés.

## Ce qui manque réellement

Le noyau actuel applique encore une règle trop forte :

```text
tout palier attesté
→ doit nécessairement reposer sur une performance observable
```

Il refuse donc une attestation pédagogique explicite du formateur comme source autonome.

La V2.1 doit introduire, de manière chirurgicale :

```text
PALIER ATTESTÉ
      ↑
      ├── preuve compatible
      │
      └── attestation explicite du formateur
```

sans confondre ces deux fondements.

Le changement doit rester borné :

```text
notion nommée
+
palier nommé
+
acte explicite d'attestation
+
formateur déclaré dans le contexte
```

avec :

```text
portée limitée
+
révisabilité maintenue
+
aucune prétention de vérification d'identité
```

Les dry-runs ne justifient pas une refonte du noyau.

Ils plaident au contraire pour une **modification doctrinale petite, explicite et testable**, suivie de la non-régression des NOY applicables.
