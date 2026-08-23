#!/usr/bin/env python3
"""Extrait, depuis la trace d'un run, les fichiers réellement ouverts et les
skills invoqués.

Cette information est exigée par la collecte (AMENDE_V2 §0.6). Elle est lue
dans la trace, jamais demandée à l'agent : l'ajouter au prompt modifierait le
stimulus exact de la fiche.

Usage : extraire_fichiers_lus.py <racine_run>
"""
import json, os, sys

racine = sys.argv[1]
work = os.path.join(racine, "workspace")
lus, skills, autres = [], [], []

for base, _, fichiers in os.walk(os.path.join(racine, "config", "projects")):
    for nom in sorted(f for f in fichiers if f.endswith(".jsonl")):
        for ligne in open(os.path.join(base, nom), encoding="utf-8"):
            try:
                bloc = json.loads(ligne)
            except ValueError:
                continue
            contenu = (bloc.get("message") or {}).get("content")
            if not isinstance(contenu, list):
                continue
            for b in contenu:
                if not (isinstance(b, dict) and b.get("type") == "tool_use"):
                    continue
                outil, entree = b.get("name"), b.get("input") or {}
                if outil == "Skill":
                    skills.append(entree.get("skill", "?"))
                elif outil in ("Read", "Glob", "Grep"):
                    chemin = entree.get("file_path") or entree.get("path") or ""
                    if chemin:
                        # Chemins relatifs au workspace : lisibles au scoring.
                        lus.append(os.path.relpath(chemin, work) if chemin.startswith(work) else chemin)
                else:
                    autres.append(outil)

def bloc(titre, valeurs):
    print("## %s" % titre)
    vus = []
    for v in valeurs:
        if v not in vus:
            vus.append(v)
    print("\n".join("- %s" % v for v in vus) if vus else "- (aucun)")
    print()

bloc("Skills invoqués", skills)
bloc("Fichiers ouverts", lus)
bloc("Autres outils utilisés", autres)
