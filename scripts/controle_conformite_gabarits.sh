#!/usr/bin/env bash
# scripts/controle_conformite_gabarits.sh — conformité mécanique du catalogue d'activités V3.1.0
#
# Ne juge aucun comportement : vérifie que chaque gabarit de activites_type/
# porte le schéma attendu. C'est ce que la campagne V31-ACT02-3 du 2026-09-04
# a manqué — 3 gabarits sur 14 avaient perdu leur section discriminante sans
# qu'aucun scénario comportemental ne le détecte (voir
# docs/v3.1/RAPPORT_INSTABILITE_V31-ACT02-3_2026-09-03.md §9).
cd "$(git rev-parse --show-toplevel)" || exit 1
R=en_cours/references
D=$R/activites_type
CHAMPS="kind inherits purpose taxonomy_levels selection_keywords participation properties ritual typical_uses"

echo "== CG1 : chaque gabarit porte les 9 champs de front matter attendus"
fail=0
for f in "$D"/*.md; do
  fm=$(sed -n '2,/^---$/p' "$f")
  for champ in $CHAMPS; do
    echo "$fm" | grep -q "^${champ}:" || { echo "  MANQUANT : $champ dans $f" ; fail=1; }
  done
done
[ "$fail" -eq 0 ] && echo "  OK — $(ls "$D"/*.md | wc -l) gabarits, 9/9 champs chacun"

echo "== CG2 : chaque gabarit porte une section discriminante de sélection"
fail=0
for f in "$D"/*.md; do
  grep -qE '^## (Pourquoi choisir|Quand choisir)' "$f" || { echo "  MANQUANT : $f" ; fail=1; }
done
[ "$fail" -eq 0 ] && echo "  OK — $(ls "$D"/*.md | wc -l) gabarits"

echo "== CG3 : aucune référence obsolète vers taxonomie.md §2 dans le catalogue"
grep -rn 'taxonomie\.md`\? §2\|taxonomie\.md §2' "$D" "$R/activite.md" || echo "  OK — aucune"

echo "== CG4 : le catalogue énuméré de activite.md correspond exactement au dossier activites_type/"
enumeres=$(grep -oE '^- `[a-z_]+\.md`' "$R/activite.md" | grep -oE '[a-z_]+\.md' | sort)
presents=$(basename -a "$D"/*.md | sort)
diff <(echo "$enumeres") <(echo "$presents") > /tmp/cg4.diff
if [ -s /tmp/cg4.diff ]; then
  echo "  ÉCART :"; cat /tmp/cg4.diff
else
  echo "  OK — $(echo "$presents" | wc -l) gabarits, énumération et dossier alignés"
fi
rm -f /tmp/cg4.diff
