#!/usr/bin/env bash
# scripts/relance_operateur.sh — arbitrage humain d'une relance conditionnelle.
#
# N'est utilisée que lorsque la couche opérateur du harnais a rendu
# AMBIGU_OPERATEUR : elle n'a alors pas pu trancher sans supposer.
#
#   relance_operateur.sh <racine> <scenario> --aucune "<motif>"
#       clôt le scénario sans relance, en consignant le motif.
#   relance_operateur.sh <racine> <scenario> --envoyer
#       envoie la relance neutre EXACTE de la fiche, une seule fois.
#   relance_operateur.sh <racine> <scenario> --repondre "<texte>"
#       envoie une réponse d'opérateur rédigée par l'humain qui arbitre.
set -u

RACINE="${1:?racine de collecte manquante}"
SCEN="${2:?scénario manquant}"
DECISION="${3:?décision manquante : --aucune, --envoyer ou --repondre}"
ARG="${4:-}"

REPO="$(cd "$(dirname "$0")/.." && pwd)"
KIT="${BASELINE_KITS:-$REPO/validation/v2.1/baseline/kits}/$SCEN"
RUN="$RACINE/$SCEN"

[ -d "$RUN" ] || { echo "run introuvable : $RUN" >&2; exit 1; }
[ -f "$RUN/DECISION_OPERATEUR_REQUISE.md" ] || { echo "aucun arbitrage en attente pour $SCEN" >&2; exit 1; }

SID=$(cat "$RUN/session_id.txt")
PERSONA=""
[ -f "$RUN/workspace/persona.md" ] && PERSONA="$RUN/workspace/persona.md"

# Retourne le code retour du tour. RC=0 : succès. RC=65 : intégrité du
# candidat violée. Tout autre code non nul : incident technique — dans les
# deux derniers cas, la décision d'arbitrage n'est PAS consignée comme
# tranchée : elle reste à refaire, le tour n'a jamais réellement eu lieu.
envoyer_tour() {
  "$REPO/scripts/run_isole.sh" tour "$RUN" "$1" "$SID" "$PERSONA" \
    > "$RUN/verbatim/relance_reponse.txt" 2> "$RUN/verbatim/relance_stderr.txt"
  local rc=$?
  echo "$rc" > "$RUN/verbatim/relance_rc.txt"
  # Les fixtures finales ont pu changer sous l'effet de ce tour.
  if [ -d "$RUN/fixtures_finales" ]; then
    ( cd "$RUN/workspace" && find etat_des_paliers -type f 2>/dev/null |
      while read -r f; do cp "$f" "$RUN/fixtures_finales/$f"; done )
  fi
  return $rc
}

case "$DECISION" in
--aucune)
  [ -n "$ARG" ] || { echo "--aucune exige un motif" >&2; exit 2; }
  printf 'decision=AUCUNE (arbitrage humain)\nmotif=%s\n' "$ARG" > "$RUN/DECISION_OPERATEUR.txt"
  echo "$SCEN clos sans relance"
  ;;
--envoyer)
  cp "$KIT/relance.txt" "$RUN/verbatim/relance_stimulus.txt"
  envoyer_tour "$KIT/relance.txt"; RC_RELANCE=$?
  if [ "$RC_RELANCE" -ne 0 ]; then
    echo "INCIDENT (code $RC_RELANCE) pendant l'envoi de la relance — décision NON consignée." >&2
    echo "Le scénario reste en attente ; relancer la commande une fois le problème diagnostiqué." >&2
    exit 3
  fi
  printf 'decision=RELANCE_NEUTRE (arbitrage humain)\n' > "$RUN/DECISION_OPERATEUR.txt"
  echo "relance neutre envoyée pour $SCEN"
  ;;
--repondre)
  [ -n "$ARG" ] || { echo "--repondre exige un texte" >&2; exit 2; }
  printf '%s\n' "$ARG" > "$RUN/verbatim/relance_stimulus.txt"
  envoyer_tour "$RUN/verbatim/relance_stimulus.txt"; RC_RELANCE=$?
  if [ "$RC_RELANCE" -ne 0 ]; then
    echo "INCIDENT (code $RC_RELANCE) pendant l'envoi de la réponse — décision NON consignée." >&2
    echo "Le scénario reste en attente ; relancer la commande une fois le problème diagnostiqué." >&2
    exit 3
  fi
  printf 'decision=REPONDRE_AVEC_CONTEXTE (arbitrage humain)\ntexte=%s\n' "$ARG" > "$RUN/DECISION_OPERATEUR.txt"
  echo "réponse d'opérateur envoyée pour $SCEN"
  ;;
*)
  echo "décision inconnue : $DECISION" >&2; exit 2
  ;;
esac

mv "$RUN/DECISION_OPERATEUR_REQUISE.md" "$RUN/DECISION_OPERATEUR_TRANCHEE.md"
python3 "$REPO/scripts/extraire_fichiers_lus.py" "$RUN" > "$RUN/verbatim/fichiers_lus.txt" 2>/dev/null

# Arbitrage effectivement tranché (aucun `exit` d'incident au-dessus n'a été
# atteint) : le scénario est désormais terminé, au même titre qu'une collecte
# résolue directement par run_baseline.sh. Réutilise le libellé déjà écrit
# dans DECISION_OPERATEUR.txt plutôt que le nom du flag CLI.
printf 'scenario=%s\n%s\n' "$SCEN" "$(head -1 "$RUN/DECISION_OPERATEUR.txt")" > "$RUN/COLLECTE_COMPLETE"
