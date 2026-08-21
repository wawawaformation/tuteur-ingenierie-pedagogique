# Plan de campagne — Validation V2 — 40 runs

> **Statut : PRÉ-GEL — AUCUN RUN OFFICIEL AUTORISÉ**
>
> Ce document remplace le plan antérieur à 38 runs fondé sur une séparation
> `NOY` / `DIFF`. La batterie V2 est désormais constituée d'un ensemble unique
> de douze scénarios `NOY001` à `NOY012`, soumis à deux régimes expérimentaux
> selon la nature du comportement testé.

## 1. Question générale

La campagne V2 doit établir trois choses distinctes :

1. le candidat V2 respecte-t-il les comportements pédagogiques protégés par
   `NOY001` à `NOY008` ?
2. pour ces comportements, la disponibilité du skill modifie-t-elle
   effectivement certaines décisions par rapport au même modèle sans skill ?
3. le candidat V2 respecte-t-il les contrats propres au produit et à son
   architecture d'activités/gabarits protégés par `NOY009` à `NOY012` ?
4. quel surcoût de consommation de tokens est associé à l'utilisation du skill,
   à comportement et stimulus comparables ?

Les résultats doivent être interprétés scénario par scénario avant toute
agrégation.

La consommation de tokens est une **mesure secondaire d'efficience**. Elle ne
participe jamais au verdict pédagogique `PASS` / `FAIL` / `INDÉTERMINÉ` et ne
peut pas être utilisée pour invalider rétrospectivement un résultat
comportemental.

Un résultat nul entre les conditions avec skill et sans skill est un résultat
expérimental recevable. La campagne ne doit jamais être modifiée dans le but
de fabriquer artificiellement un échec de la condition sans skill.

## 2. Batterie expérimentale

La batterie autoritative comprend douze scénarios :

| Scénario | Objet principal | Régime V2 |
|---|---|---|
| NOY001 | Élicitation du point de départ utile avant exposition substantielle | A/B′ |
| NOY002 | Exposition / auto-déclaration ≠ preuve attestée | A/B′ |
| NOY003 | Compatibilité entre preuve et palier attesté | A/B′ |
| NOY004 | Budget de nouveauté dans une activité évaluée | A/B′ |
| NOY005 | Alignement objectif / tâche / preuve / critère | A/B′ |
| NOY006 | Réussite intégrée et portée de la preuve | A/B′ |
| NOY007 | Auto-déclaration ≠ attestation d'un palier | A/B′ |
| NOY008 | Évaluer sans notation arbitraire | A/B′ |
| NOY009 | Héritage du socle Activité dans un gabarit Quiz | A uniquement |
| NOY010 | Routage d'un gabarit sans enfermement par modalité | A uniquement |
| NOY011 | Maîtrise de l'exposition dans une activité évaluée | A uniquement |
| NOY012 | Catalogue de gabarits et représentation correcte de l'architecture | A uniquement |

### 2.1 NOY001 à NOY008 — régime différentiel

Ces huit scénarios portent sur des comportements pédagogiques ou garde-fous
pour lesquels une comparaison au modèle sans skill est informative pendant la
validation de la V2.

Pour chacun :

```text
avec skill  × 2 répétitions indépendantes
sans skill  × 2 répétitions indépendantes
```

Soit :

```text
8 scénarios × 2 conditions × 2 répétitions = 32 runs
```

### 2.2 NOY009 à NOY012 — conformité propre au produit

Ces quatre scénarios portent sur des contrats d'architecture ou de
fonctionnement propres au skill : socle Activité, routage des gabarits,
maîtrise de l'exposition et représentation du catalogue.

La condition sans skill ne constitue pas un témoin pertinent pour un contrat
que le modèle nu n'est pas censé connaître.

Pour chacun :

```text
avec skill × 2 répétitions indépendantes
```

Soit :

```text
4 scénarios × 1 condition × 2 répétitions = 8 runs
```

### 2.3 Total planifié

```text
32 runs A/B′
+ 8 runs A uniquement
= 40 runs expérimentaux de base
```

Les reruns techniques et les éventuelles répétitions conditionnelles R3 ne
font pas partie de ces 40 runs de base.

### 2.4 Mesure secondaire — consommation de tokens

La campagne mesure également la consommation de tokens de chaque trajectoire.

La source autoritative est **l'usage déclaré par le runtime / fournisseur dans
la trace brute du run**. Les tokens ne doivent pas être reconstruits à partir
du texte avec un tokenizer approximatif lorsque les compteurs d'usage sont
disponibles.

Pour chaque run, collecter séparément, lorsqu'ils sont exposés par la trace :

```text
input_tokens
cache_creation_input_tokens
cache_read_input_tokens
output_tokens
```

Puis calculer :

```text
total_input_tokens =
    input_tokens
  + cache_creation_input_tokens
  + cache_read_input_tokens

total_tokens =
    total_input_tokens
  + output_tokens
```

Les quatre compteurs bruts doivent être conservés : un même nombre de tokens
n'a pas nécessairement le même coût selon qu'il s'agit d'entrée non cachée,
de création de cache, de lecture de cache ou de sortie.

Si l'un de ces compteurs n'est pas fourni par le runtime, il est marqué comme
indisponible ; il ne doit pas être estimé silencieusement.

#### Comparaison A/B′

Pour `NOY001` à `NOY008`, la comparaison de consommation est **appariée par
scénario et répétition** :

```text
NOYxxx / R1 : avec skill ↔ sans skill
NOYxxx / R2 : avec skill ↔ sans skill
```

Pour chaque paire calculer au minimum :

```text
delta_input_tokens  = total_input_tokens(A) - total_input_tokens(B′)
delta_output_tokens = output_tokens(A)      - output_tokens(B′)
delta_total_tokens  = total_tokens(A)       - total_tokens(B′)

surcout_total_pct =
    100 * delta_total_tokens / total_tokens(B′)
```

Un delta négatif est conservé tel quel : l'utilisation du skill peut, sur une
trajectoire donnée, réduire la consommation totale en raccourcissant ou en
structurant différemment la réponse.

L'analyse doit distinguer :

- le **surcoût d'entrée**, qui reflète notamment le contexte et les références
  chargés par le skill ;
- le **surcoût de sortie**, qui reflète aussi les différences de comportement
  et de longueur de réponse ;
- le **surcoût total observé**, qui combine les deux.

Les résultats agrégés sont descriptifs : somme, moyenne, médiane, minimum et
maximum des deltas, ainsi que le surcoût relatif. L'analyse par scénario reste
prioritaire.

Pour `NOY009` à `NOY012`, exécutés uniquement avec skill, la consommation
absolue est conservée et rapportée, mais **aucun “surcoût dû au skill” ne peut
être calculé**, faute de condition B′ comparable.

La mesure porte sur les tokens, pas sur un prix monétaire. Un coût financier
peut être calculé secondairement lors de l'analyse à partir des tarifs alors
applicables, sans modifier les données expérimentales gelées.

## 3. Conditions expérimentales

Deux conditions sont utilisées lorsque le scénario est en régime A/B′ :

- **A — avec skill** ;
- **B′ — sans skill**.

Pour une même cellule expérimentale, tout doit être identique sauf la
disponibilité du skill `tuteur-ingenierie-pedagogique`.

### 3.1 Avec skill

Le workspace neuf contient une copie byte-for-byte du candidat V2 gelé sous :

```text
<RUN_DIR>/.claude/skills/tuteur-ingenierie-pedagogique/
```

La copie doit être contrôlée contre le manifeste du candidat gelé avant le
lancement.

### 3.2 Sans skill

Le workspace neuf ne contient pas le skill candidat et aucun skill personnel,
synchronisé, de plugin ou d'entreprise portant le même nom ne doit être
disponible.

La condition sans skill n'est jamais utilisée pour `NOY009` à `NOY012`.

## 4. Modèle et paramètres d'exécution

Les paramètres sont identiques dans toutes les cellules :

```text
Claude Code : 2.1.232
modèle      : claude-sonnet-5
effort      : medium
permissions : default
```

Variables d'environnement :

```bash
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1
```

Chaque run utilise :

- une session Claude Code neuve ;
- un workspace neuf ;
- la persona prévue par la fiche ;
- le prompt exact de la fiche ;
- les fixtures exactes lorsqu'elles existent ;
- aucun état hérité d'un autre run.

## 5. Règle d'interaction opérateur

La fiche de scénario prime lorsqu'elle contient une consigne spécifique.

Règle générale :

> Lorsqu'une demande de précision intervient, l'opérateur répond de manière à
> permettre au scénario de se poursuivre et à rendre observable le
> comportement visé. Il utilise les informations prévues ou disponibles
> lorsqu'elles sont pertinentes, sans souffler artificiellement la réponse
> attendue ni introduire un élément qui modifierait ce que le test cherche à
> mesurer.

Lorsque aucune information pertinente supplémentaire n'est disponible,
l'opérateur peut répondre :

```text
Je n'ai pas d'information supplémentaire. Poursuis avec les éléments disponibles.
```

Une question de l'agent peut, lorsque la fiche le prévoit ou lorsque
l'observable est déjà suffisamment établi, suffire à terminer le run.

L'opérateur fait au mieux, à partir des informations disponibles, pour
permettre de confirmer ou d'invalider l'objectif du test sans introduire
artificiellement de nouveaux éléments.

## 6. Répétitions expérimentales

Chaque cellule planifiée comporte deux répétitions indépendantes :

```text
R1
R2
```

Elles sont définies avant l'exécution et ne dépendent pas du résultat de la
première répétition.

### 6.1 Répétition conditionnelle R3

Une troisième répétition ne doit jamais être systématique.

Elle peut être décidée uniquement lorsqu'une cellule présente une discordance
comportementale entre deux trajectoires techniquement valides, par exemple :

```text
R1 = PASS
R2 = FAIL
```

R3 sert alors à caractériser la stabilité du comportement, pas à effacer un
résultat défavorable.

La décision de lancer R3 doit être tracée et prise avant connaissance du
résultat de R3.

### 6.2 Rerun technique

Un rerun technique est distinct d'une répétition expérimentale.

Il n'est autorisé que lorsqu'un run est techniquement invalide. Le run initial
reste conservé dans l'archive d'audit et le rerun reprend exactement la même
cellule expérimentale.

Convention :

```text
RUN-012-R1
RUN-012-R2
```

Une réponse pédagogiquement mauvaise, inattendue, courte ou contraire à
l'effet espéré n'est jamais une invalidité technique.

## 7. Randomisation

L'ordre des 40 cellules doit être généré **une seule fois avant le premier run
officiel**, à partir d'une graine publique figée et d'une méthode
déterministe.

La randomisation ne doit dépendre d'aucun résultat de dry-run ou de campagne.

L'artefact autoritatif d'ordre sera :

```text
validation/v2/plan/RUNS.csv
```

Les `run_id` sont séquentiels et n'encodent ni le scénario, ni la condition,
ni la répétition.

La table de randomisation doit permettre de retrouver pour chaque run :

```text
run_id
scenario_id
condition
repetition
persona
prompt
```

La graine et la méthode de génération seront consignées dans :

```text
validation/v2/plan/RANDOMISATION.txt
```

## 8. Dry-runs et données confirmatoires

Les dry-runs réalisés pendant la conception des scénarios :

- servent uniquement à vérifier l'exécutabilité, l'oracle et la capacité
  éventuelle de discrimination ;
- ne font pas partie des données confirmatoires ;
- ne doivent pas être intégrés aux résultats de la campagne officielle ;
- ne doivent pas être utilisés par les scoreurs.

Les résultats historiques ou de dry-run ne préjugent jamais du verdict d'un
run officiel.

## 9. Validité technique

Un run est techniquement valide si tous les éléments applicables sont
conformes au plan gelé, notamment :

1. `run_id`, scénario, condition et répétition correspondent à `RUNS.csv` ;
2. le prompt est exact ;
3. la persona est exacte ;
4. le workspace est neuf ;
5. la session est neuve ;
6. la mémoire automatique est désactivée ;
7. la présence ou l'absence du skill correspond à la condition ;
8. le candidat présent en condition A correspond au candidat gelé ;
9. les fixtures prévues sont exactes et accessibles ;
10. modèle, version, effort et permissions sont conformes ;
11. la collecte est complète et exploitable ;
12. aucun incident d'environnement n'empêche l'interprétation de la
    trajectoire.

`INDÉTERMINÉ` est un verdict pédagogique possible ; ce n'est pas en soi une
invalidité technique.

## 10. Collecte et gel des données

Chaque run est collecté avec le `collector-kit` gelé.

Les collectes brutes ne sont jamais modifiées après acquisition.

Les artefacts de campagne doivent permettre de reconstruire au minimum :

```text
candidat exact
scénarios exacts
personas exactes
ordre des runs
condition de chaque run
répétition
prompt soumis
trajectoire brute
compteurs d'usage de tokens exposés par le runtime
contrôles techniques
incidents éventuels
```

Une archive globale accompagnée de son SHA-256 est créée après la collecte
des runs prévus et des éventuels reruns techniques.

## 11. Scoring aveugle

Le scoring est réalisé sur des trajectoires anonymisées.

Le scoreur ne voit pas :

- la condition expérimentale ;
- la répétition ;
- le `run_id` source ;
- les résultats des dry-runs ;
- les résultats historiques A/B′ ;
- le verdict d'un autre scoreur.

Verdicts autorisés :

```text
PASS
FAIL
INDÉTERMINÉ
```

Aucune note intermédiaire.

Les oracles sont issus des fiches `NOY001` à `NOY012`. Ils sont gelés avant le
premier run officiel.

Deux scoreurs indépendants peuvent être utilisés. Leurs verdicts sont gelés
avant comparaison et avant désaveuglement.

## 12. Analyse des résultats

### 12.1 NOY001 à NOY008

L'analyse porte d'abord sur chaque scénario et chaque condition :

```text
avec skill : R1 / R2 [/ R3]
sans skill : R1 / R2 [/ R3]
```

Le contraste A/B′ est décrit sans exiger qu'il soit systématiquement favorable
au skill.

Un scénario où les deux conditions réussissent est un résultat nul
informatif, pas un défaut du protocole.

### 12.2 NOY009 à NOY012

Ces scénarios sont interprétés comme des tests de conformité du candidat.

La question est uniquement de savoir si le comportement attendu est stable en
condition avec skill.

### 12.3 Analyse d'efficience — tokens

Pour `NOY001` à `NOY008`, produire un tableau apparié contenant au minimum :

```text
scenario_id
repetition
tokens_avec_skill
tokens_sans_skill
delta_tokens
delta_pct
```

Lorsque les compteurs détaillés sont disponibles, conserver également les
deltas d'entrée, de création/lecture de cache et de sortie.

Présenter ensuite :

- le delta par paire ;
- la moyenne et la médiane des deltas ;
- le total cumulé avec skill et sans skill ;
- le surcoût relatif global ;
- les scénarios contribuant le plus au surcoût.

Cette analyse reste descriptive et séparée de l'efficacité pédagogique. Un
skill peut être comportementalement meilleur tout en consommant davantage de
tokens ; inversement, une consommation moindre ne constitue pas une preuve de
meilleure qualité pédagogique.

### 12.4 Agrégation

Les taux globaux peuvent être fournis à titre descriptif, mais ils ne
remplacent pas l'analyse par scénario.

Un test statistique éventuel est secondaire compte tenu du faible nombre de
scénarios et de la dépendance conceptuelle entre certains d'entre eux.

## 13. Critères de décision V2

La campagne ne doit pas être réduite à un seuil numérique unique.

### Candidat stabilisable

Le candidat peut être considéré comme stabilisable si :

- les contrats `NOY009` à `NOY012` sont stables en PASS ;
- aucun défaut bloquant n'est établi sur `NOY001` à `NOY008` ;
- les éventuelles instabilités sont localisées et interprétables ;
- l'intégrité du candidat, des scénarios et du protocole est préservée.

La comparaison A/B′ sert à mesurer l'apport différentiel de la V2 ; elle ne
crée pas une obligation artificielle de faire échouer B′.

### Stop / révision

La campagne doit être arrêtée ou la promotion V2 différée si :

- un défaut bloquant du candidat est établi ;
- un contrat propriétaire `NOY009` à `NOY012` échoue de manière reproductible ;
- un oracle s'avère inapplicable ou ambigu en conditions réelles ;
- l'intégrité du candidat ou du protocole est compromise.

Toute correction du candidat ou d'un scénario après gel impose de documenter
la rupture de gel et de décider explicitement quelles données restent
exploitables.

## 14. Statut futur en V3

Une fois la V2 validée et promue, les douze scénarios `NOY001` à `NOY012`
changent de fonction méthodologique.

Pour une future V3, ils deviennent la batterie de non-régression héritée de la
V2 et sont exécutés **en condition avec skill uniquement**, sauf décision
expérimentale explicitement justifiée.

Les nouveaux comportements propres à la V3 peuvent, eux, faire l'objet de
comparaisons A/B′ pendant leur phase de validation.

Cette règle évite de redémontrer à chaque version l'effet différentiel de
comportements déjà validés, tout en conservant un filet de sécurité contre les
régressions.

## 15. Artefacts à produire avant gel

Avant le premier run officiel, `validation/v2/` doit au minimum contenir :

```text
validation/v2/
├── plan/
│   ├── PLAN_EXPERIMENTAL.md
│   ├── RUNS.csv
│   ├── RANDOMISATION.txt
│   ├── REGLE_REPETITIONS.md
│   └── PLAN_ANONYMISATION.md
├── manifest/
│   ├── CANDIDATE.sha256
│   ├── SCENARIOS.sha256
│   ├── PERSONAS.sha256
│   ├── RUNTIME_OPERATEUR.sha256
│   └── PLAN.sha256
└── operateur/
    ├── INSTRUCTIONS_AGENT_OPERATEUR.md
    └── PARAMETRES_EXECUTION.md
```

Le gel du candidat, des scénarios, des personas, du runtime opérateur et du
plan doit précéder toute exécution officielle.

---

## Décision de conception

Le plan V2 retient donc :

```text
NOY001–NOY008 : A/B′ × 2 = 32 runs
NOY009–NOY012 : A    × 2 =  8 runs
-------------------------------------
TOTAL                         40 runs
```

Aucun ancien scénario `DIFF-Pxx` ne subsiste dans le protocole.
