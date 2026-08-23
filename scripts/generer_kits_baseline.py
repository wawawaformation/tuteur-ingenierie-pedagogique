#!/usr/bin/env python3
"""Génère les kits d'exécution de la baseline par extraction depuis les fiches NOY.

Les stimuli ne sont jamais recopiés à la main : ils sont extraits des blocs de
code des fiches autoritatives. Toute divergence typographique entre la fiche et
le stimulus envoyé est ainsi impossible.

Sortie : validation/v2.1/baseline/kits/<SCENARIO>/
"""
import io, os, re, shutil, sys

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NR = os.path.join(REPO, "validation", "v2.1", "non_regression")
KITS = os.path.join(REPO, "validation", "v2.1", "baseline", "kits")

# scenario -> (fiche, [titres de section des tours], persona, (titre fixture, chemin))
PLAN = {
  "NOY001":   ("NOY001.md", ["### Tour 1", "### Tour 2", "### Tour 3"], "apprenant.md",
               ("## Fixture", "etat_des_paliers/apprenant-noy001.md")),
  "NOY002":   ("NOY002.md", ["### Tour 1 — résultat obtenu par l'apprenant",
                             "### Tour 2 — demande d'attestation"], "apprenant.md",
               ("## Fixture technique", "etat_des_paliers/apprenant-noy002.md")),
  "NOY003":   ("NOY003.md", ["## Stimulus exact"], "apprenant.md",
               ("## Fixture", "etat_des_paliers/apprenant-noy003.md")),
  "NOY004":   ("NOY004.md", ["## Stimulus exact"], "formateur.md", None),
  "NOY005":   ("NOY005.md", ["## Prompt exact"], None, None),
  "NOY006":   ("NOY006.md", ["## Prompt exact"], None,
               ("## Fixture", "etat_des_paliers/apprenant-noy006.md")),
  "NOY007":   ("NOY007.md", ["## Prompt exact"], None, None),
  "NOY008":   ("NOY008.md", ["### Tour 1 — Prompt exact"], "formateur.md", None),
  "NOY009":   ("NOY009.md", ["### Tour 1 — Prompt exact"], "formateur.md", None),
  "NOY010":   ("NOY010.md", ["### Tour 1 — Prompt exact"], "formateur.md", None),
  "NOY011":   ("NOY011.md", ["### Tour 1 — Prompt exact"], "formateur.md", None),
  "NOY012_1": ("NOY012_1.md", ["### Tour unique — Appréciation générale"], None,
               ("### `etat_des_paliers/apprenant-noy012_1.md`", "etat_des_paliers/apprenant-noy012_1.md")),
  "NOY012_2": ("NOY012_2.md", ["### Tour unique — Attestation explicite"], None,
               ("### `etat_des_paliers/apprenant-noy012_2.md`", "etat_des_paliers/apprenant-noy012_2.md")),
  "NOY013":   ("NOY013.md", ["### Tour 1 — Déclaration négative rapportée"], None,
               ("### État initial", "etat_des_paliers/apprenant-noy013.md")),
  "C0":       ("CONTROLE_STABILISATION_NOY014.md", ["### Stimulus exact"], None, None),
}

def bloc_apres(lignes, titre, langue=None):
    """Retourne le contenu du premier bloc de code suivant `titre`."""
    try:
        i = next(k for k, l in enumerate(lignes) if l.rstrip() == titre)
    except StopIteration:
        sys.exit("titre introuvable : %r" % titre)
    # Une section peut contenir plusieurs blocs (p. ex. le chemin en ```text
    # puis le contenu en ```markdown) : on retient le premier de la langue voulue.
    fin = next((k for k in range(i + 1, len(lignes))
                if lignes[k].startswith("## ") or lignes[k].startswith("# ")), len(lignes))
    while i < fin and lignes[i].strip() != ("```" + langue if langue else "```"):
        i += 1
    if i >= fin:
        sys.exit("aucun bloc %s après %r" % (langue or "code", titre))
    j = i + 1
    while j < len(lignes) and not lignes[j].startswith("```"):
        j += 1
    return "\n".join(lignes[i + 1:j]).strip("\n") + "\n"

def section(lignes, titre):
    """Retourne le texte intégral d'une section, titre compris."""
    niveau = len(titre) - len(titre.lstrip("#"))
    try:
        i = next(k for k, l in enumerate(lignes) if l.rstrip() == titre)
    except StopIteration:
        return None
    # Arrêt au prochain titre de niveau INFÉRIEUR OU ÉGAL : sinon une section
    # `###` déborde sur les sections `##` suivantes.
    def est_borne(ligne):
        if not ligne.startswith("#"):
            return False
        n = len(ligne) - len(ligne.lstrip("#"))
        return n <= niveau and ligne[n:n + 1] == " "
    j = next((k for k in range(i + 1, len(lignes)) if est_borne(lignes[k])), len(lignes))
    return "\n".join(lignes[i:j]).rstrip() + "\n"

def relance(lignes):
    """Extrait la relance neutre autorisée par la fiche, si elle en prévoit une."""
    texte = "\n".join(lignes)
    for m in re.finditer(r"```text\n(.*?)\n```", texte, re.S):
        c = m.group(1).strip()
        if "Poursuis avec les éléments disponibles" in c or "Mets le fichier à jour" in c:
            return c + "\n"
    return None

# Sections que l'opérateur du harnais a le droit de voir. Liste blanche
# stricte : tout titre absent d'ici est exclu du dossier opérateur.
#
# Exclus délibérément : Oracle*, Observables*, Invariant testé, Objectif du test,
# Périmètre de notation, Validité technique, Verdict*, Sous-critère*, INDÉTERMINÉ,
# « Ce qui n'est pas un FAIL », Contre-garde-fou*, Limites reconnues, dry-runs,
# Baseline*, Protocole*, Intention, Problème expérimental, Contexte de conception,
# et « Contrôle des interventions opérateur » — cette dernière énumère des
# éléments de l'oracle en exemples ("Ajoute un objectif", "Donne les critères
# de réussite"), sans rien apporter que la consigne opérateur ne dise déjà.
AUTORISEES = [
    "## Contexte persona",
    "## Contexte / Fixture",
    "## Notion testée",
    "## État initial des notions",
    "## Fixture",
    "## Fixture technique",
    "### Si l'agent demande des informations supplémentaires",
    "### Si l’agent demande des informations supplémentaires",
    "## Consigne opérateur",
]

if os.path.isdir(KITS):
    shutil.rmtree(KITS)

for scen, (fiche, titres, persona, fixture) in sorted(PLAN.items()):
    lignes = io.open(os.path.join(NR, fiche), encoding="utf-8").read().split("\n")
    d = os.path.join(KITS, scen)
    os.makedirs(d)
    for n, titre in enumerate(titres, 1):
        io.open(os.path.join(d, "t%d.txt" % n), "w", encoding="utf-8").write(
            bloc_apres(lignes, titre, "text"))
    if fixture:
        titre, chemin = fixture
        cible = os.path.join(d, "fixtures", chemin)
        os.makedirs(os.path.dirname(cible), exist_ok=True)
        io.open(cible, "w", encoding="utf-8").write(bloc_apres(lignes, titre, "markdown"))
    r = relance(lignes)
    if r:
        io.open(os.path.join(d, "relance.txt"), "w", encoding="utf-8").write(r)
        # Règle autoritative de la fiche, destinée à l'OPÉRATEUR HUMAIN qui
        # décidera d'envoyer ou non la relance. Ce fichier n'est jamais envoyé
        # à l'exécutant : il contient des éléments qui souffleraient le test.
        parties = [x for x in (section(lignes, "### Si l'agent demande des informations supplémentaires"),
                               section(lignes, "### Si l’agent demande des informations supplémentaires"),
                               section(lignes, "## Consigne opérateur")) if x]
        io.open(os.path.join(d, "regle_relance.txt"), "w", encoding="utf-8").write(
            "RÈGLE DE RELANCE — extraite de %s\nNE JAMAIS ENVOYER CE FICHIER À L'EXÉCUTANT.\n\n%s"
            % (fiche, "\n".join(parties)))

        # Dossier de l'opérateur du harnais : liste blanche de sections, dans
        # l'ordre du document. Ni oracle, ni invariant, ni observables, ni
        # verdict, ni résultat antérieur.
        dossier = [x for x in (section(lignes, t) for t in AUTORISEES) if x]
        vus, uniques = set(), []
        for bloc_txt in dossier:
            if bloc_txt not in vus:
                vus.add(bloc_txt); uniques.append(bloc_txt)
        io.open(os.path.join(d, "dossier_operateur.md"), "w", encoding="utf-8").write(
            "# Dossier opérateur — %s\n\nSections autorisées de %s, extraites par liste blanche.\n\n%s"
            % (scen, fiche, "\n".join(uniques)))
    meta = ["scenario=%s" % scen, "fiche=%s" % fiche, "tours=%d" % len(titres),
            "persona=%s" % (persona or ""), "fixture=%s" % (fixture[1] if fixture else "")]
    io.open(os.path.join(d, "meta.env"), "w", encoding="utf-8").write("\n".join(meta) + "\n")
    print("%-10s tours=%d persona=%-14s fixture=%-40s relance=%s" %
          (scen, len(titres), persona or "-", (fixture[1] if fixture else "-"), "oui" if r else "non"))
