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
#
# État d'un répertoire de run — un répertoire existant n'est JAMAIS lu comme
# « déjà joué » : son état est déterminé par le marqueur qu'il porte.
#   COLLECTE_COMPLETE            scénario terminé, peut être ignoré à la relance
#   SCENARIO_SUSPENDU.md         incident technique (candidat ou opérateur),
#                                 non terminé, jamais ignoré silencieusement
#   DECISION_OPERATEUR_REQUISE.md  AMBIGU_OPERATEUR, arbitrage humain en attente
#   (aucun des trois)             anomalie : répertoire incomplet sans marqueur
#                                 reconnu (ex. script interrompu) — signalée,
#                                 jamais ignorée
set -u

REPO="$(cd "$(dirname "$0")/.." && pwd)"
KITS="${BASELINE_KITS:-$REPO/validation/v2.1/baseline/kits}"
PERSONAS="$REPO/validation/personas"
RACINE="${BASELINE_ROOT:-/projets/skill/tests/baseline_v2.1_$(date +%Y-%m-%d)}"

EN_ATTENTE=()
SUSPENDUS=()
ANOMALIES=()
ORDRE=(C0 NOY001 NOY002 NOY003 NOY004 NOY005 NOY006 NOY007 NOY008 \
       NOY009 NOY010 NOY011 NOY012_1 NOY012_2 NOY013)
[ $# -gt 0 ] && ORDRE=("$@")

mkdir -p "$RACINE"
echo "racine de collecte : $RACINE"
echo "commit de en_cours  : $(git -C "$REPO" log --format=%H -1 -- en_cours/)"

# `git diff --quiet` seul est insuffisant : il ne compare le répertoire de
# travail qu'à l'INDEX, donc il ne voit ni une modification déjà stagée
# (index face à HEAD) ni un fichier non suivi. Les trois cas sont couverts en
# une passe par `git status --porcelain`, qui liste staged, unstaged et
# untracked pour le chemin donné ; une sortie vide garantit que le runtime
# copié depuis en_cours/ est exactement celui de HEAD, rien de plus, rien de
# moins.
ETAT_EN_COURS="$(git -C "$REPO" status --porcelain --untracked-files=all -- en_cours/)"
if [ -n "$ETAT_EN_COURS" ]; then
  echo "ABANDON : en_cours/ n'est pas dans l'état attendu du candidat (HEAD $(git -C "$REPO" rev-parse --short HEAD)) :" >&2
  echo "$ETAT_EN_COURS" >&2
  echo "Aucune collecte n'a été lancée." >&2
  exit 1
fi

for SCEN in "${ORDRE[@]}"; do
  KIT="$KITS/$SCEN"
  [ -d "$KIT" ] || { echo "kit introuvable : $SCEN" >&2; exit 1; }
  # shellcheck disable=SC1090
  TOURS=$(sed -n 's/^tours=//p' "$KIT/meta.env")
  PERSONA_NOM=$(sed -n 's/^persona=//p' "$KIT/meta.env")

  RUN="$RACINE/$SCEN"
  if [ -d "$RUN" ]; then
    if [ -f "$RUN/COLLECTE_COMPLETE" ]; then
      echo "== $SCEN : collecte déjà complète, ignoré"
    elif [ -f "$RUN/SCENARIO_SUSPENDU.md" ]; then
      echo "== $SCEN : SUSPENDU (incident technique antérieur, non rejoué) — voir $RUN/SCENARIO_SUSPENDU.md" >&2
      SUSPENDUS+=("$SCEN")
    elif [ -f "$RUN/DECISION_OPERATEUR_REQUISE.md" ]; then
      echo "== $SCEN : EN ATTENTE d'arbitrage humain (non rejoué) — voir $RUN/DECISION_OPERATEUR_REQUISE.md" >&2
      EN_ATTENTE+=("$SCEN")
    else
      echo "== $SCEN : ANOMALIE — répertoire existant sans marqueur d'état reconnu, non rejoué" >&2
      { echo "# Anomalie — $SCEN"
        echo
        echo "Répertoire de run présent sans COLLECTE_COMPLETE, SCENARIO_SUSPENDU.md ni"
        echo "DECISION_OPERATEUR_REQUISE.md : état non classé, probablement un run"
        echo "interrompu de façon anormale (script tué, machine éteinte...)."
        echo
        echo "Inspecter le contenu de verbatim/ avant de décider : reprendre ce run"
        echo "n'est pas sûr ; supprimer $RUN pour le rejouer proprement l'est."
      } > "$RUN/ANOMALIE_ETAT_INCONNU.md"
      ANOMALIES+=("$SCEN")
    fi
    continue
  fi

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

  # SUSPENDU porte le motif dès qu'un tour (initial, relance ou opérateur) ne
  # rend pas un succès technique franc. AMBIGU_EN_ATTENTE distingue une
  # ambiguïté de jugement réelle (état terminal légitime, pas un incident).
  # Les deux sont réinitialisés à chaque scénario : aucune valeur ne doit
  # survivre d'une itération à l'autre.
  SUSPENDU=""
  AMBIGU_EN_ATTENTE=""
  DEC=""
  for n in $(seq 1 "$TOURS"); do
    cp "$KIT/t$n.txt" "$RUN/verbatim/tour${n}_stimulus.txt"
    "$REPO/scripts/run_isole.sh" tour "$RUN" "$KIT/t$n.txt" "$SID" "$PERSONA_ARG" \
      > "$RUN/verbatim/tour${n}_reponse.txt" 2> "$RUN/verbatim/tour${n}_stderr.txt"
    RC=$?
    echo "$RC" > "$RUN/verbatim/tour${n}_rc.txt"
    if [ "$RC" -eq 65 ]; then
      echo "   INVALIDE : candidat modifié au tour $n" >&2
      SUSPENDU="candidat modifié au tour $n (code 65)"
      break
    elif [ "$RC" -ne 0 ]; then
      echo "   INCIDENT TECHNIQUE au tour $n (code $RC) — tour non collecté valablement" >&2
      SUSPENDU="incident technique au tour $n (code $RC)"
      break
    fi
    echo "   tour $n : $(wc -c < "$RUN/verbatim/tour${n}_reponse.txt") octets"
  done

  if [ -n "$SUSPENDU" ]; then
    { echo "# Scénario suspendu — $SCEN"
      echo
      echo "Motif : $SUSPENDU"
      echo
      echo "Aucun traitement ultérieur (opérateur, fichiers lus, fixtures finales)"
      echo "n'a été effectué sur ce scénario : le tour en échec n'a pas été traité"
      echo "comme une collecte réussie."
      echo
      echo "## stderr des tours de ce run"
      echo
      cat "$RUN"/verbatim/tour*_stderr.txt 2>/dev/null
    } > "$RUN/SCENARIO_SUSPENDU.md"
    echo "   ⏸  suspendu — voir $RUN/SCENARIO_SUSPENDU.md" >&2
    SUSPENDUS+=("$SCEN")
    continue
  fi

  DERNIER="$RUN/verbatim/tour${TOURS}_reponse.txt"

  # Relance conditionnelle : tranchée par la couche opérateur aveugle du
  # harnais, jamais par une heuristique. Une seule intervention d'opérateur par
  # scénario, conformément au "une seule fois, à l'identique" du plan §0.5.
  if [ -f "$KIT/relance.txt" ]; then
    "$REPO/scripts/operateur_sonnet.sh" "$RUN" "$KIT" > /dev/null 2> "$RUN/operateur_stderr.txt"
    RC_OPERATEUR=$?

    # Un incident technique de la couche opérateur (crash, erreur API, sortie
    # non exploitable au niveau processus) n'est PAS une ambiguïté de
    # jugement : l'opérateur n'a alors rendu aucune décision, il faut donc
    # suspendre le scénario plutôt que de retomber sur AMBIGU_OPERATEUR.
    if [ "$RC_OPERATEUR" -ne 0 ]; then
      { echo "# Scénario suspendu — $SCEN"
        echo
        echo "Motif : incident technique de la couche opérateur (code $RC_OPERATEUR)"
        echo
        echo "Ce n'est pas une ambiguïté de jugement (AMBIGU_OPERATEUR) : l'opérateur"
        echo "n'a rendu aucune décision. Diagnostic ci-dessous."
        echo
        echo "## stderr de l'appel opérateur"
        echo
        cat "$RUN/operateur_stderr.txt" 2>/dev/null
        echo
        echo "## sortie brute éventuelle de l'opérateur"
        echo
        cat "$RUN/operateur/verdict_brut.txt" 2>/dev/null
      } > "$RUN/SCENARIO_SUSPENDU.md"
      echo "   ⏸  INCIDENT_TECHNIQUE_OPERATEUR (code $RC_OPERATEUR) — suspendu" >&2
      SUSPENDUS+=("$SCEN")
      continue
    fi

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
        RC_RELANCE=$?
        echo "$RC_RELANCE" > "$RUN/verbatim/relance_rc.txt"
        if [ "$RC_RELANCE" -eq 65 ]; then
          SUSPENDU="candidat modifié pendant la relance (code 65)"
        elif [ "$RC_RELANCE" -ne 0 ]; then
          SUSPENDU="incident technique pendant la relance (code $RC_RELANCE)"
        fi
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
      RC_RELANCE=$?
      echo "$RC_RELANCE" > "$RUN/verbatim/relance_rc.txt"
      if [ "$RC_RELANCE" -eq 65 ]; then
        SUSPENDU="candidat modifié pendant la relance (code 65)"
      elif [ "$RC_RELANCE" -ne 0 ]; then
        SUSPENDU="incident technique pendant la relance (code $RC_RELANCE)"
      fi
      ;;
    *)
      # AMBIGU_OPERATEUR, ou sortie d'opérateur non conforme au format (RC=0
      # mais texte imparsable) : ce dernier cas reste routé vers l'arbitrage
      # humain, avec l'anomalie de format consignée pour ne rien masquer.
      [ "$DEC" = AMBIGU_OPERATEUR ] || \
        echo "décision d'opérateur illisible : ${DEC:-<vide>}" > "$RUN/operateur/anomalie.txt"
      DEC=AMBIGU_OPERATEUR
      ;;
    esac

    if [ -n "$SUSPENDU" ]; then
      { echo "# Scénario suspendu — $SCEN"
        echo
        echo "Motif : $SUSPENDU"
        echo
        echo "Survenu pendant la relance ($DEC). Aucune décision d'opérateur n'a été"
        echo "consignée : ce n'est pas un verdict, c'est un échec technique."
        echo
        echo "## stderr de la relance"
        echo
        cat "$RUN/verbatim/relance_stderr.txt" 2>/dev/null
      } > "$RUN/SCENARIO_SUSPENDU.md"
      echo "   ⏸  suspendu — voir $RUN/SCENARIO_SUSPENDU.md" >&2
      SUSPENDUS+=("$SCEN")
      continue
    fi

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
      AMBIGU_EN_ATTENTE=1
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

  # Terminal et complet uniquement si aucune ambiguïté n'attend d'arbitrage
  # (les cas SUSPENDU ont déjà quitté la boucle via `continue` plus haut).
  if [ -z "$AMBIGU_EN_ATTENTE" ]; then
    printf 'scenario=%s\ndecision=%s\n' "$SCEN" "${DEC:-N/A (aucune relance prévue)}" > "$RUN/COLLECTE_COMPLETE"
  fi
done

echo
echo "collecte terminée : $RACINE"
echo "aucun scoring n'a été effectué."

TOTAL=${#ORDRE[@]}
COMPLETS=0
for s in "${ORDRE[@]}"; do [ -f "$RACINE/$s/COLLECTE_COMPLETE" ] && COMPLETS=$((COMPLETS + 1)); done
echo
echo "état de la campagne : $COMPLETS/$TOTAL scénario(s) avec collecte complète."

if [ ${#EN_ATTENTE[@]} -gt 0 ]; then
  echo
  echo "SCÉNARIOS EN ATTENTE DE DÉCISION OPÉRATEUR (${#EN_ATTENTE[@]}) :"
  for s in "${EN_ATTENTE[@]}"; do echo "  - $s → $RACINE/$s/DECISION_OPERATEUR_REQUISE.md"; done
  echo
  echo "La baseline n'est pas close tant que chacun n'a pas été tranché."
fi
if [ ${#SUSPENDUS[@]} -gt 0 ]; then
  echo
  echo "SCÉNARIOS SUSPENDUS POUR INCIDENT TECHNIQUE (${#SUSPENDUS[@]}) :"
  for s in "${SUSPENDUS[@]}"; do echo "  - $s → $RACINE/$s/SCENARIO_SUSPENDU.md"; done
  echo
  echo "Aucun de ces scénarios n'a été collecté valablement. Diagnostiquer le"
  echo "motif technique (stderr consigné) avant de rejouer : supprimer"
  echo "\$RACINE/<SCENARIO> puis relancer — un répertoire SUSPENDU n'est jamais"
  echo "rejoué automatiquement."
fi
if [ ${#ANOMALIES[@]} -gt 0 ]; then
  echo
  echo "SCÉNARIOS EN ÉTAT ANORMAL, NON CLASSÉS (${#ANOMALIES[@]}) :"
  for s in "${ANOMALIES[@]}"; do echo "  - $s → $RACINE/$s/ANOMALIE_ETAT_INCONNU.md"; done
  echo
  echo "Inspecter chacun manuellement avant de poursuivre."
fi

if [ "$COMPLETS" -lt "$TOTAL" ]; then
  echo
  echo "LA CAMPAGNE N'EST PAS COMPLÈTE ($COMPLETS/$TOTAL)."
  exit 1
fi
