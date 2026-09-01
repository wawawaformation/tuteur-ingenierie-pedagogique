# Tuteur & ingénierie pédagogique — candidat V3

Ce dossier contient le **candidat V3** du skill `tuteur-ingenierie-pedagogique`.

Il est destiné au tutorat d’adultes et à l’assistance à l’ingénierie pédagogique. Son rôle n’est pas de remplacer le jugement du formateur, mais de fournir à l’agent des garde-fous et des ressources lui permettant de raisonner de façon plus cohérente sur la progression, l’évaluation et la conception des activités.

> **Ce candidat n’est pas encore la version publique recommandée.**
>
> La version publique reste celle distribuée dans `../dist/stable/` tant que la promotion V3 n’a pas été explicitement réalisée.

---

## Les trois fonctions principales

### 1. Progression par notions, paliers et preuves

Le skill suit l’état d’apprentissage **notion par notion**.

```text
notion
→ palier
→ preuve
→ décision
```

Il distingue notamment exposition, déclaration et preuve observable.

Une capacité n’est attestée qu’à hauteur de ce que la preuve permet réellement de conclure.

---

### 2. Activités évaluées interprétables

Lorsqu’une activité est évaluée, le skill cherche à préserver l’interprétabilité de son résultat.

```text
objectif
→ tâche
→ production / performance
→ critères
→ preuve
→ conclusion
```

Il protège notamment le budget de nouveauté : une activité évaluée ne doit pas introduire silencieusement plusieurs notions non attestées dont l’échec deviendrait impossible à diagnostiquer.

Les critères restent visibles pour l’apprenant, tandis que les éléments de correction ou une production de référence donnant la solution sont protégés jusqu’à sa propre production.

---

### 3. Bibliothèque de gabarits pédagogiques auto-descriptifs

Toute Activité repose sur un socle commun défini dans :

```text
references/activite.md
```

Les spécialisations disponibles sont :

```text
references/activites_type/
├── brique.md
├── atelier.md
├── quiz.md
└── recul.md
```

Le catalogue du socle aide l’agent à effectuer une première sélection. Les métadonnées `purpose` et `typical_uses` peuvent départager plusieurs gabarits plausibles avant de charger le contrat détaillé du gabarit retenu.

L’analogie agentique est la suivante :

```text
métadonnées
→ description d’un outil possible

contenu du gabarit
→ contrat d’utilisation

SKILL.md
→ orchestration
```

Les gabarits jouent donc un rôle proche de **tools disponibles pour l’agent**, mais ce ne sont pas techniquement des tool calls.

---

## Deux modes d’usage

### Tutorat direct

L’agent accompagne un apprenant :

- comprend la demande ou le blocage ;
- établit le point de départ lorsque cela change la décision ;
- raisonne sur les notions et preuves disponibles ;
- explique ou fait pratiquer ;
- propose une activité compatible avec l’état connu ;
- ajuste la suite à partir des résultats observés.

### Ingénierie pédagogique

L’agent assiste un formateur ou concepteur :

- identifie le bon niveau de granularité ;
- structure Module, Séquence, Séance et Activité ;
- formule les objectifs pédagogiques ;
- choisit un gabarit d’Activité lorsque pertinent ;
- produit brief, tâche, production attendue et critères ;
- vérifie l’alignement avant livraison.

---

## Granularité, modalité et gabarit sont indépendants

Le découpage interne de référence est :

```text
Module
└── Séquence
    ├── Séance
    │   └── Activité
    └── Activité directement rattachée si pertinent
```

`Activité` est le niveau de granularité le plus fin.

La modalité ne choisit pas automatiquement la structure ou le gabarit.

```text
synchrone / asynchrone
≠
présentiel / distanciel
```

De même :

```text
court ≠ automatiquement Brique
difficile ≠ automatiquement Atelier
asynchrone ≠ automatiquement Atelier
présentiel ≠ automatiquement Séance
```

La décision dépend du besoin pédagogique et du contexte.

---

## Gabarits disponibles

### Brique

Activité élémentaire au sens de la structure pédagogique : une tâche ciblée, suffisamment autonome pour être utilisée seule ou composée avec d’autres.

« Élémentaire » ne signifie pas « facile ».

### Atelier

Activité structurée autour d’une production évaluée nécessitant une démarche organisée en plusieurs étapes.

Sa caractéristique n’est ni sa durée ni sa modalité.

### Quiz

Activité principalement destinée au diagnostic ou à l’auto-positionnement.

Le format exact dépend du besoin ; ses règles détaillées sont définies dans son propre contrat.

### Recul

Activité de réflexivité permettant d’expliciter, analyser et mettre en perspective une expérience, une production, une démarche ou des choix.

Il n’a pas de palier propre : la valeur de preuve dépend de la performance réellement observable.

---

## Garde-fous du noyau

Les conditions exactes sont définies dans `references/activite_evaluee.md`.

Le noyau utilise notamment quatre repères :

```text
A1 — Exposition libre
A2 — Palier attaché à une notion
A3 — Budget de nouveauté = 1
A4 — Pas de notation arbitraire
```

Ces intitulés sont des repères de navigation. La formulation normative complète reste celle de `references/activite_evaluee.md`.

Autres principes importants :

- une déclaration n’est pas une preuve attestée ;
- une preuve externe rapportée peut être recevable si la tâche, les conditions et le résultat observé sont suffisamment précis ;
- le canal oral n’impose pas un palier : c’est l’acte observable qui compte ;
- la portée d’une preuve est limitée à ce qui a réellement été produit ou démontré ;
- `utiliser ≠ créer`, `exécuter ≠ écrire`, `lire ≠ produire`.

---

## Références runtime

```text
SKILL.md
references/
├── activite.md
├── activite_evaluee.md
├── activites_type/
│   ├── atelier.md
│   ├── brique.md
│   ├── quiz.md
│   └── recul.md
├── andragogie.md
├── decoupage_pedagogique.md
├── etat_des_paliers.md
├── glossaire.md
├── opo.md
├── production_documentaire.md
├── seance.md
├── sequence.md
├── syllabus.md
└── taxonomie.md
```

Rôles principaux :

- `SKILL.md` : orchestration et garde-fous prioritaires ;
- `taxonomie.md` : échelle des paliers cognitifs ;
- `activite_evaluee.md` : règles normatives A1 à A4 ;
- `etat_des_paliers.md` : suivi notion / palier / preuve ;
- `opo.md` : objectifs pédagogiques opérationnels ;
- `decoupage_pedagogique.md` : granularité et articulation des niveaux ;
- `activite.md` : socle commun et catalogue des gabarits ;
- `activites_type/` : contrats spécialisés ;
- `glossaire.md` : clarification descriptive du vocabulaire.

Le glossaire n’est pas une seconde source normative.

---

## Statut de validation

Le runtime V3 a été restructuré et soumis à des revues statiques de cohérence.

La validation comportementale reste nécessaire avant promotion publique.

Les tests de non-régression du projet sont conservés hors du runtime, dans `../validation/`.

La promotion suit le flux :

```text
en_cours/
→ validation
→ stable/
→ dist/stable/
```

Aucune version située dans `en_cours/` ne doit être considérée comme publique avant cette promotion explicite.
