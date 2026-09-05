#!/usr/bin/env bash
# scripts/run_isole.sh — brique d'exécution isolée d'un run comportemental.
#
# Recette figée : la baseline (lot 0) et TOUS les contrôles post-refactoring
# doivent l'utiliser sans modification, sinon les verdicts ne sont pas
# comparables (AMENDE_V2 §8.2, §11.2, D6).
#
# Usage :
#   run_isole.sh preparer <racine_run>
#       construit l'environnement isolé et le workspace (idempotent).
#   run_isole.sh tour <racine_run> <fichier_stimulus> [session_id] [persona]
#       joue un tour et écrit la réponse verbatim sur stdout.
#
# Code de retour 65 : candidat modifié → RUN INVALIDE.
set -u

SOUS_CMD="${1:?sous-commande manquante : preparer|tour}"
RUN_ROOT="${2:?racine du run manquante}"

REPO="$(cd "$(dirname "$0")/.." && pwd)"
CANDIDAT="$REPO/en_cours"

# --- Paramètre de référence (validation/v2/operateur/ETAT_AUTORITATIF.md) ---
MODEL_ID=claude-sonnet-5
EFFORT=medium
# La campagne V2 tournait en `default` parce qu'elle était INTERACTIVE : un
# opérateur humain approuvait chaque écriture. En headless (`-p`), `default`
# refuse les écritures, ce qui viderait de leur observable les six scénarios
# exigeant une mise à jour de l'état des paliers (NOY001/002/006/012_1/012_2/013).
# `acceptEdits` joue le rôle de cet accord opérateur. L'invariance du candidat
# est garantie séparément, par chmod a-w + manifeste SHA-256.
PERMISSION_MODE=acceptEdits
# Binaire épinglé : le 2.1.232 de la campagne V2 n'est plus installé. La
# baseline étant un étalon interne au refactoring, seule compte la constance
# entre baseline et contrôles post-refactoring.
CLAUDE_BIN=/home/david/.local/share/claude/versions/2.1.241
export DISABLE_AUTOUPDATER=1
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

ISO="$RUN_ROOT/config"
WORK="$RUN_ROOT/workspace"
# Condition A, protocole V2 : le candidat vit DANS le workspace. Ses références
# sont donc sous le cwd et lisibles en permission mode `default`, sans
# dérogation ni --add-dir.
SKILL="$WORK/.claude/skills/tuteur-ingenierie-pedagogique"
MANIFESTE="$RUN_ROOT/skill_manifeste.sha256"

manifeste_candidat() {
  ( cd "$1" && find . -type f -print0 | sort -z | xargs -0 sha256sum )
}

verifier_integrite() {
  # Le contenu normatif testé doit rester invariant pendant tout le run.
  if ! manifeste_candidat "$SKILL" | diff -q - "$MANIFESTE" >/dev/null; then
    { echo "RUN INVALIDE — candidat modifié ($1) :"
      manifeste_candidat "$SKILL" | diff - "$MANIFESTE"; } >&2
    touch "$RUN_ROOT/INVALIDE"
    exit 65
  fi
}

case "$SOUS_CMD" in
preparer)
  [ -d "$ISO" ] && { echo "racine déjà préparée : $RUN_ROOT" >&2; exit 1; }
  mkdir -p "$ISO" "$SKILL"
  chmod 700 "$ISO"
  # Seules les credentials sont reprises du profil de développement : aucun
  # CLAUDE.md, skill, plugin, hook, agent, commande ou mémoire n'est hérité.
  cp /home/david/.claude/.credentials.json "$ISO/"
  chmod 600 "$ISO/.credentials.json"
  # Runtime seul. `en_cours/CLAUDE.md` est injecté en contexte système dès que
  # le skill est utilisé (prouvé par canari au préflight) et énumère les
  # invariants testés par NOY001-004/006/007 : le copier soufflerait l'oracle.
  # `promesse.md` et `base_de_travail.md` sont écartés pour la même raison.
  # Le runtime est défini par .claude/CLAUDE.md : SKILL.md + references/.
  cp -a "$CANDIDAT/SKILL.md" "$SKILL/"
  cp -a "$CANDIDAT/references" "$SKILL/"
  manifeste_candidat "$SKILL" > "$MANIFESTE"
  # Immuabilité physique : le workspace reste écrivable pour les fixtures que
  # certaines fiches exigent, mais pas le contenu normatif du candidat.
  chmod -R a-w "$SKILL"
  ;;
tour)
  STIMULUS="${3:?fichier de stimulus manquant}"
  SESSION_ID="${4:-}"
  PERSONA="${5:-}"
  verifier_integrite "AVANT le tour"

  ARGS=()
  if [ -n "$SESSION_ID" ] && [ -f "$RUN_ROOT/.session_ouverte" ]; then
    ARGS+=(--resume "$SESSION_ID")
  elif [ -n "$SESSION_ID" ]; then
    ARGS+=(--session-id "$SESSION_ID")
    touch "$RUN_ROOT/.session_ouverte"
  fi
  [ -n "$PERSONA" ] && ARGS+=(--append-system-prompt-file "$PERSONA")

  cd "$WORK" || exit 1
  # Les runs passent par l'API Anthropic directe (credentials.json) : annuler
  # les vars Azure Foundry héritées de la session parente si elle en a.
  CLAUDE_CODE_USE_FOUNDRY="" \
  ANTHROPIC_FOUNDRY_RESOURCE="" \
  ANTHROPIC_FOUNDRY_API_KEY="" \
  CLAUDE_CONFIG_DIR="$ISO" "$CLAUDE_BIN" -p \
    --model "$MODEL_ID" --effort "$EFFORT" --permission-mode "$PERMISSION_MODE" \
    "${ARGS[@]}" < "$STIMULUS"
  RC=$?
  verifier_integrite "PENDANT le tour"
  exit $RC
  ;;
*)
  echo "sous-commande inconnue : $SOUS_CMD (attendu preparer|tour)" >&2; exit 2 ;;
esac
