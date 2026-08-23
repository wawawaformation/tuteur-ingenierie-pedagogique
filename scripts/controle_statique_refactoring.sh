#!/usr/bin/env bash
# scripts/controle_statique_refactoring.sh — contrôles statiques du refactoring noyau V2.1
cd "$(git rev-parse --show-toplevel)" || exit 1
R=en_cours
echo "== CS1 : aucune source normative dupliquée pour la preuve externe rapportée"
grep -rc "refactorings de ce type" $R/SKILL.md $R/references/ | grep -v ":0" || echo "  (0 occurrence)"
echo "== CS2 : chaîne d'alignement — une seule source portante"
grep -rn "→ critères" $R/SKILL.md $R/references/
echo "== CS3 : I25 — une seule source portante"
grep -rn "granularité la plus fine" $R/SKILL.md $R/references/
echo "== CS4 : I26 — une seule source portante"
grep -rn "conditions exclusives" $R/SKILL.md $R/references/
echo "== CS5 : le glossaire ne porte aucune règle comportementale"
grep -rn "doit \|ne doit pas \|jamais \|toujours " $R/references/glossaire.md | head
echo "== CS6 : aucun 'fait foi' sur l'axe de préséance"
grep -rn "fait foi" $R/SKILL.md
echo "== CS7 : ancrages 'taxonomie.md §2' encore valides"
grep -rc "taxonomie.md\` §2" $R/SKILL.md $R/references/ | grep -v ":0"
echo "== CS8 : invariants gelés toujours présents textuellement"
for m in "utiliser ≠ créer" "Budget de nouveauté" "palier 0" "auto-attester" "palier 2"; do
  printf "  %-28s %s occurrence(s)\n" "$m" "$(grep -rl "$m" $R --include=*.md | wc -l)"
done
echo "== CS9 : aucun gate de dérogation"
grep -rn "avant toute décision\|vérifier s'il existe\|rechercher systématiquement" $R/SKILL.md $R/references/ || echo "  OK"
