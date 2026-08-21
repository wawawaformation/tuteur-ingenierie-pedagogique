# Mesure de tokens — note d'interprétation

`TOKENS_V2_BASE40.tsv` contient les compteurs runtime observés pour les 40 runs de base.

La comparaison appariée A/B′ porte sur les 16 paires NOY001–NOY008 × R1/R2.

Le ratio brut de `total_tokens` mesure un **volume de tokens traité/comptabilisé par le runtime**. Il ne doit pas être assimilé directement à un ratio de prix : une grande partie de l'écart provient de `cache_read_input_tokens`, dont le poids économique dépend de la politique de facturation et du runtime.

L'observation opérateur sur le pourcentage de quota Claude est une information pratique séparée ; elle n'est ni une mesure de tokens, ni une mesure de prix, ni une mesure de temps de calcul.
