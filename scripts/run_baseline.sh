#!/usr/bin/env bash
# scripts/run_baseline.sh — exécute la baseline comportementale du lot 0.
#
# Joue les 14 scénarios NOY + C0 dans des sessions Claude Code fraîches et
# isolées, avec la recette figée de scripts/run_isole.sh.
#
#   ./scripts/run_baseline.sh                 # les 15 runs
#   ./scripts/run_baseline.sh NOY006 C0       # un sous-ensemble
#   BASELINE_ROOT=/chemin ./scripts/run_baseline.sh
#
# Ce script COLLECTE. Il ne score pas et ne connaît aucun oracle.
# NOY014_1 / NOY014_2 sont hors baseline (AMENDE_V2 §9) : ils ne sont pas joués.
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
KITS="${BASELINE_KITS:-$REPO/validation/v2.1/baseline/kits}"
PERSONAS="$REPO/validation/personas"
RACINE="${BASELINE_ROOT:-/projets/skill/tests/baseline_v2.1_$(date +%Y-%m-%d)}"

EN_ATTENTE=()
ORDRE=(C0 NOY001 NOY002 NOY003 NOY004 NOY005 NOY006 NOY007 NOY008 \
       NOY009 NOY010 NOY011 NOY012_1 NOY012_2 NOY013)
[ $# -gt 0 ] && ORDRE=("$@")

mkdir -p "$RACINE"
echo "racine de collecte : $RACINE"
echo "commit de en_cours  : $(git -C "$REPO" log --format=%H -1 -- en_cours/)"
git -C "$REPO" diff --quiet -- en_cours/ || { echo "ABANDON : en_cours/ n'est pas propre." >&2; exit 1; }

for SCEN in "${ORDRE[@]}"; do
  KIT="$KITS/$SCEN"
  [ -d "$KIT" ] || { echo "kit introuvable : $SCEN" >&2; exit 1; }
  # shellcheck disable=SC1090
  TOURS=$(sed -n 's/^tours=//p' "$KIT/meta.env")
  PERSONA_NOM=$(sed -n 's/^persona=//p' "$KIT/meta.env")

  RUN="$RACINE/$SCEN"
  if [ -d "$RUN" ]; then echo "== $SCEN : déjà joué, ignoré"; continue; fi

  echo "== $SCEN ($TOURS tour(s), persona=${PERSONA_NOM:-aucun})"
  "$REPO/scripts/run_isole.sh" preparer "$RUN" || exit 1

  # Fixtures : recréées depuis le kit, jamais reprises d'un workspace exécuté.
  [ -d "$KIT/fixtures" ] && cp -a "$KIT/fixtures/." "$RUN/workspace/"

  PERSONA_ARG=""
  if [ -n "$PERSONA_NOM" ]; then
    cp "$PERSONAS/$PERSONA_NOM" "$RUN/workspace/persona.md"
    PERSONA_ARG="$RUN/workspace/persona.md"
  fi

  SID=$(python3 -c "import uuid;print(uuid.uuid4())")
  echo "$SID" > "$RUN/session_id.txt"
  mkdir -p "$RUN/verbatim"

  for n in $(seq 1 "$TOURS"); do
    cp "$KIT/t$n.txt" "$RUN/verbatim/tour${n}_stimulus.txt"
    "$REPO/scripts/run_isole.sh" tour "$RUN" "$KIT/t$n.txt" "$SID" "$PERSONA_ARG" \
      > "$RUN/verbatim/tour${n}_reponse.txt" 2> "$RUN/verbatim/tour${n}_stderr.txt"
    RC=$?
    echo "$RC" > "$RUN/verbatim/tour${n}_rc.txt"
    if [ "$RC" -eq 65 ]; then echo "   INVALIDE : candidat modifié" >&2; break; fi
    echo "   tour $n : $(wc -c < "$RUN/verbatim/tour${n}_reponse.txt") octets"
  done

  DERNIER="$RUN/verbatim/tour${TOURS}_reponse.txt"

  # Relance conditionnelle : tranchée par la couche opérateur aveugle du
  # harnais, jamais par une heuristique. Une seule intervention d'opérateur par
  # scénario, conformément au "une seule fois, à l'identique" du plan §0.5.
  if [ -f "$KIT/relance.txt" ]; then
    "$REPO/scripts/operateur_sonnet.sh" "$RUN" "$KIT" > /dev/null 2>&1
    DEC=$(cat "$RUN/operateur/decision.txt" 2>/dev/null)
    case "$DEC" in
    AUCUNE)
      echo "   opérateur : AUCUNE — aucune relance"
      ;;
    REPONDRE_AVEC_CONTEXTE)
      if [ -s "$RUN/operateur/reponse.txt" ]; then
        echo "   opérateur : REPONDRE_AVEC_CONTEXTE"
        cp "$RUN/operateur/reponse.txt" "$RUN/verbatim/relance_stimulus.txt"
        "$REPO/scripts/run_isole.sh" tour "$RUN" "$RUN/operateur/reponse.txt" "$SID" "$PERSONA_ARG" \
          > "$RUN/verbatim/relance_reponse.txt" 2> "$RUN/verbatim/relance_stderr.txt"
        echo "$?" > "$RUN/verbatim/relance_rc.txt"
      else
        DEC=AMBIGU_OPERATEUR
        echo "REPONDRE_AVEC_CONTEXTE sans texte de réponse" > "$RUN/operateur/anomalie.txt"
      fi
      ;;
    RELANCE_NEUTRE)
      echo "   opérateur : RELANCE_NEUTRE"
      cp "$KIT/relance.txt" "$RUN/verbatim/relance_stimulus.txt"
      "$REPO/scripts/run_isole.sh" tour "$RUN" "$KIT/relance.txt" "$SID" "$PERSONA_ARG" \
        > "$RUN/verbatim/relance_reponse.txt" 2> "$RUN/verbatim/relance_stderr.txt"
      echo "$?" > "$RUN/verbatim/relance_rc.txt"
      ;;
    *)
      # AMBIGU_OPERATEUR, ou sortie d'opérateur non conforme au format.
      [ "$DEC" = AMBIGU_OPERATEUR ] || \
        echo "décision d'opérateur illisible : ${DEC:-<vide>}" > "$RUN/operateur/anomalie.txt"
      DEC=AMBIGU_OPERATEUR
      ;;
    esac

    printf 'decision=%s\nmotif=%s\n' "$DEC" "$(cat "$RUN/operateur/motif.txt" 2>/dev/null)" \
      > "$RUN/DECISION_OPERATEUR.txt"

    if [ "$DEC" = AMBIGU_OPERATEUR ]; then
      { echo "# Arbitrage humain requis — $SCEN"
        echo
        echo "L'opérateur du harnais n'a pas pu trancher sans supposer."
        echo
        echo "Motif : $(cat "$RUN/operateur/motif.txt" 2>/dev/null)"
        [ -f "$RUN/operateur/anomalie.txt" ] && echo "Anomalie : $(cat "$RUN/operateur/anomalie.txt")"
        echo
        echo "## Dernière réponse du candidat (tour $TOURS)"
        echo
        cat "$DERNIER"
        echo
        echo "## Règle exacte de la fiche"
        echo
        cat "$KIT/regle_relance.txt"
        echo
        echo "## Pour trancher"
        echo
        echo "  ./scripts/relance_operateur.sh $RACINE $SCEN --aucune \"motif\""
        echo "  ./scripts/relance_operateur.sh $RACINE $SCEN --envoyer"
        echo "  ./scripts/relance_operateur.sh $RACINE $SCEN --repondre \"texte\""
      } > "$RUN/DECISION_OPERATEUR_REQUISE.md"
      echo "   ⏸  AMBIGU_OPERATEUR — arbitrage humain requis"
      EN_ATTENTE+=("$SCEN")
    fi
  fi

  # Fichiers réellement lus : extraits de la trace, jamais demandés à l'agent
  # (le demander modifierait le stimulus exact).
  python3 "$REPO/scripts/extraire_fichiers_lus.py" "$RUN" > "$RUN/verbatim/fichiers_lus.txt" 2>/dev/null

  # Fixtures finales : observables de plein droit pour les scénarios qui en ont.
  [ -d "$KIT/fixtures" ] && { mkdir -p "$RUN/fixtures_finales"; \
    ( cd "$RUN/workspace" && find etat_des_paliers -type f 2>/dev/null | \
      while read -r f; do mkdir -p "$RUN/fixtures_finales/$(dirname "$f")"; \
        cp "$f" "$RUN/fixtures_finales/$f"; done ); }
done

echo
echo "collecte terminée : $RACINE"
echo "aucun scoring n'a été effectué."
if [ ${#EN_ATTENTE[@]} -gt 0 ]; then
  echo
  echo "SCÉNARIOS EN ATTENTE DE DÉCISION OPÉRATEUR (${#EN_ATTENTE[@]}) :"
  for s in "${EN_ATTENTE[@]}"; do echo "  - $s → $RACINE/$s/DECISION_OPERATEUR_REQUISE.md"; done
  echo
  echo "La baseline n'est pas close tant que chacun n'a pas été tranché."
fi
