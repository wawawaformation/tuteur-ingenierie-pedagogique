# CLAUDE.md — `validation/collector-kit/`

`collector-kit` est un outil **générique** de collecte et d'archivage de runs Claude Code.

> Le collector collecte. Il ne score pas.

## Périmètre

Ne pas introduire dans le collector :

- la logique d'un scénario particulier ;
- un verdict pédagogique ;
- une dépendance à une version particulière du skill ;
- une règle métier propre à `tuteur-ingenierie-pedagogique` si elle peut rester dans le protocole de campagne.

Le nom du skill doit rester paramétrable lorsque l'outil le prévoit.

## Conditions

La notation expérimentale est :

```text
A  = avec skill
B′ = sans skill
```

La CLI peut utiliser des valeurs techniques différentes (`skill`, `no-skill`). Ne pas confondre notation scientifique et noms physiques de dossiers/options.

## Isolation

- Désactiver la mémoire automatique lorsque le protocole le prévoit.
- Ne pas effectuer de recherche globale hors workspace pour « retrouver » une fixture ou un fichier de palier.
- Préserver l'isolation entre runs et conditions.
- Ne pas inventer une réponse à `AskUserQuestion` si le scénario ne la fournit pas.

## Tests du collector

Toute modification de code doit être suivie des tests pertinents dans `validation/collector-kit/tests/`.

Ne pas considérer une campagne comme invalide uniquement parce qu'une réponse est pédagogiquement faible : le contrôle technique et le scoring comportemental sont deux étapes distinctes.

## Tokens

Les compteurs de tokens sont des métriques d'efficience, pas des verdicts pédagogiques.

Distinguer notamment :

- input non caché ;
- cache creation ;
- cache read ;
- output ;
- total traité.

Ne pas assimiler automatiquement `total_tokens` à un coût financier : le cache et les politiques de facturation/quotas peuvent avoir des pondérations différentes.
