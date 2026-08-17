# Bloc 1 — préparation et lancement du run

Ce bloc prépare le prompt, initialise la collecte et lance l’agent testé dans l’une des deux conditions expérimentales :

- **A — avec skill** : `/projets/skill/tests/tests_avec_skill_A`
- **B′ — sans skill** : `/projets/skill/tests/tests_sans_skill_B`

> Le suffixe `_B` du dossier est une convention de nommage. La condition expérimentale reste notée **B′**.

Les prompts utilisés sont stockés dans :

```text
/projets/skill/tests/prompts/
```

Les résultats collectés sont stockés dans :

```text
/projets/skill/tests/runs/
```

---

## Valeurs à adapter

Pour chaque run, remplacer :

- `RUN-ID` : identifiant unique du run ;
- `SCENARIO-ID` : identifiant du scénario testé ;
- `SKILL-NAME` : nom exact du skill testé ;
- `PROMPT EXACT` : prompt gelé du scénario.

Dans un test comparatif A/B′, le prompt doit rester **strictement identique dans les deux conditions**.

---

## A — Avec skill

```bash
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

mkdir -p /projets/skill/tests/prompts
mkdir -p /projets/skill/tests/runs

cat > /projets/skill/tests/prompts/RUN-ID.txt <<'EOF'
PROMPT EXACT
EOF

cd /projets/skill/tests/tests_avec_skill_A

python3 /projets/skill/tuteur-ingenierie-pedagogique/validation/collector-kit/collect_run.py start \
  --run-id RUN-ID \
  --scenario-id SCENARIO-ID \
  --condition skill \
  --skill-expected yes \
  --skill-name SKILL-NAME \
  --prompt-file /projets/skill/tests/prompts/RUN-ID.txt \
  --output-root /projets/skill/tests/runs

claude "$(cat /projets/skill/tests/prompts/RUN-ID.txt)"
```

---

## B′ — Sans skill

```bash
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=1

mkdir -p /projets/skill/tests/prompts
mkdir -p /projets/skill/tests/runs

cat > /projets/skill/tests/prompts/RUN-ID.txt <<'EOF'
PROMPT EXACT
EOF

cd /projets/skill/tests/tests_sans_skill_B

python3 /projets/skill/tuteur-ingenierie-pedagogique/validation/collector-kit/collect_run.py start \
  --run-id RUN-ID \
  --scenario-id SCENARIO-ID \
  --condition no-skill \
  --skill-expected n/a \
  --skill-name SKILL-NAME \
  --prompt-file /projets/skill/tests/prompts/RUN-ID.txt \
  --output-root /projets/skill/tests/runs

claude "$(cat /projets/skill/tests/prompts/RUN-ID.txt)"
```

---

## Pendant le run

Le prompt envoyé doit rester strictement identique au prompt gelé du scénario.

Ne pas ajouter spontanément d’informations absentes du scénario.

Si `AskUserQuestion` demande une information qui n’est pas fournie par le scénario :

> **faire `Esc` sans injecter d’information supplémentaire.**

Le comportement observé appartient à la trajectoire du run et ne doit pas être corrigé manuellement pendant l’expérience.

Lorsque le run est terminé, quitter Claude Code avec :

```text
exit
```

puis exécuter le Bloc 2.
