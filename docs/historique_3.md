# Historique — candidat V3

Journal court des étapes réalisées sur le candidat V3, toutes mineures confondues (3.1, 3.2, 3.3). Mis à jour avant chaque commit touchant à ce candidat. Ordre chronologique inverse (le plus récent en premier).

---

## 2026-09-03 — Ajout `V31-ACT02-4` : les métadonnées ne sont pas une table de décision mécanique

Question de l'utilisateur (« pas plus de sous ACT01 ou 02 pour confirmer l'exactitude de la promesse ? ») ayant fait relire ACT01/ACT02 intégralement contre les 6 fiches existantes. Un vrai trou trouvé, pas du remplissage : ACT02 promet explicitement que « les métadonnées constituent des indices de sélection, pas des conditions exclusives ni une table de décision mécanique » (`promesse.md` l. 103), mais aucune fiche ne le testait — toutes présentaient des métadonnées pointant proprement vers la bonne réponse. Second candidat plus faible identifié et écarté d'un commun accord : `granularité`/`étape pédagogique` citées comme critères de choix mais jamais testées comme facteur décisif — jugé moins urgent, pas traité.

- Nouveau `validation/v3.1/non_regression/V31-ACT02-4.md` : piège de mots-clés construit sur une distinction déjà établie dans `origine_des_formats.md` (`En un mot` = collecte individuelle verticale, `Rétrospective` = régulation collective horizontale). Stimulus au vocabulaire de surface évoquant `En un mot` (« feedback », « fin de journée ») mais décrivant explicitement la fonction de `Rétrospective` (négociation collective, décision partagée). Répétition requise (trois exécutions), même statut que les autres scénarios « charge de preuve ».
- `en_cours/promesse.md`, clause ACT02 sur les métadonnées : renvoi ajouté vers `V31-ACT02-4`.
- `README.md` et `CLAUDE.md` du dossier alignés : 7 scénarios au total, liste « charge de preuve » et exigence de répétition étendues.

---

## 2026-09-03 — Toujours 2 propriétés (ACT01, ACT02), mais placement corrigé du biais de familiarité

Question posée par l'utilisateur (« on a combien de ACT alors ») qui a fait remonter une incohérence plutôt qu'une réponse simple. Le paragraphe sur le biais de familiarité (qui a produit `V31-ACT01-3`) vivait sous **ACT02** dans `promesse.md`, alors que la fiche elle-même se déclare « validation comportementale de **ACT01** » et que son exemple (Planche météo) n'est pas un cas de repli sur le plus proche (territoire d'ACT02) mais une correspondance exacte risquant d'être ignorée par habitude (territoire d'ACT01, « mobiliser »).

- `en_cours/promesse.md` : paragraphe biais de familiarité déplacé sous ACT01, juste après la note SPEC sur le biais de nouveauté déjà présente — les deux risques symétriques cohabitent maintenant au même endroit. ACT02 conserve un renvoi court plutôt qu'une duplication de l'exemple.
- `validation/v3.1/non_regression/V31-ACT01-3.md` : renvoi corrigé de « `promesse.md` (ACT02) » vers « `promesse.md` (ACT01, "biais de familiarité") ».

Toujours 2 propriétés au total pour le Chantier 1 (ACT01, ACT02) — la question ne révélait pas un besoin d'ACT03, seulement un mauvais rangement à l'intérieur des deux existantes.

---

## 2026-09-03 — Écart pourquoi/comment comblé : exigence de répétition pour valider la fiabilité

Écart signalé par Claude puis confirmé par l'utilisateur : la promesse V3.1.0 engage explicitement la **fiabilité et la systématicité** d'ACT01/ACT02 comme critère de valeur (paragraphe ajouté plus tôt le même jour, suite au retour sur la boîte à outils éprouvée), mais les scénarios SPEC ne testaient qu'un run unique — une capacité, pas une fiabilité. L'utilisateur demande de combler l'écart en éditant d'abord la promesse, avant les scénarios.

- `en_cours/promesse.md`, tête du Chantier 1 : paragraphe étendu — un run unique teste la capacité, pas la fiabilité ; la fiabilité suppose de rejouer le même stimulus plusieurs fois et de constater un résultat stable ; repère retenu, trois exécutions indépendantes, majorité stable. Distinction posée explicitement avec la règle de passe unique du gel de non-régression (§13.2) : celle-ci détecte une régression sur une propriété déjà établie, elle ne peut pas établir une propriété qui n'a jamais été montrée stable. Section « Statut de cette promesse » alignée (point 4 réécrit, mention de la passe de gel comme distincte de cette validation initiale).
- `en_cours/base_de_travail.md` §9 : règle de méthode générale ajoutée (pas propre à V3.1.0) — un run unique établit une capacité, pas une fiabilité ; répétition requise quand la promesse engage explicitement la fiabilité.
- `validation/v3.1/non_regression/V31-ACT01-2.md`, `V31-ACT01-3.md`, `V31-ACT02-3.md` : clause de répétition ajoutée (trois exécutions indépendantes, majorité stable) dans l'objectif du test et la validité technique de chacun — ce sont les trois scénarios qui portent la charge de preuve.
- `README.md` et `CLAUDE.md` du dossier alignés : liste des scénarios « charge de preuve » corrigée (ajout de `V31-ACT01-3`, omis par erreur depuis sa création), exigence de répétition documentée une fois pour les trois plutôt que dispersée sans référence croisée.

Non traité, laissé pour la construction de la campagne réelle : la paire contrastive `V31-ACT02-1`/`V31-ACT02-2` n'a pas reçu la même exigence de répétition — décision consciente de ne pas étendre le scope sans validation explicite de l'utilisateur, pas un oubli.

---

## 2026-09-03 — Contrôle rapide des 4 gabarits retravaillés (Atelier, Brique, Quiz, Recul)

Pas de nouvelle entrée de provenance nécessaire dans `origine_des_formats.md` (déjà couverts en §2/§4) : ce sont des retouches de métadonnées, pas de nouveaux formats. Juste une vérification de cohérence, à la demande de l'utilisateur (« on retouche vite fait »).

Aucune incohérence détectée, contrairement aux candidats neufs : `ritual.suitable: false` cohérent pour les quatre ; `taxonomy_levels.typical` vide pour Brique et Recul jugé logique (agnosticisme de niveau assumé, déjà documenté dans `origine_des_formats.md`), pas une erreur. Point neutre : `brique.md` mentionne littéralement « classe inversée » dans ses `typical_uses` — usage correct cette fois (travail préparatoire avant séance), à ne pas confondre avec l'écart corrigé sur Facettes le même jour.

---

## 2026-09-03 — Provenance des gabarits candidats V3.1.0, démarrée : Facettes

Ouverture d'un chantier documentaire distinct de la promesse : classer les 11 gabarits candidats de `plus_tard/nouvelles_activites_v3_metadonnees.zip` dans `dossier-pedagogique/origine_des_formats.md` (établi / observé / choisi), à raison d'un gabarit à la fois, en discussion directe. Objectif explicite : ne pas laisser la doc affirmer une équivalence à une méthode établie si ce n'en est pas une.

**Facettes** : premier passage classé « observé, parenté vague avec Jigsaw » jugé insuffisant par l'utilisateur (« pas vraiment un jigsaw, plus simple à mettre en place, vu surtout pour introduire un sujet, en classe inversée »). Vérifié par recoupement de deux sources indépendantes (Gemini, puis ChatGPT — signalé par l'utilisateur comme non neutre, déjà au courant du projet ; les citations elles-mêmes restent vérifiables indépendamment de ce biais, et ChatGPT a été le plus catégorique à *refuser* une équivalence facile, donc plutôt un signe rassurant qu'inquiétant ici).

Résultat convergent : filiation établie et citable (interdépendance positive — Deutsch 1949, Johnson & Johnson 1989 ; Group Investigation — Sharan & Sharan 1976/1990/1992 ; Co-op Co-op — Kagan 1985), explicitement pas un Jigsaw (Aronson 1978, confirmé par les deux sources), mais **aucune source ne nomme la variante allégée et pré-structurée utilisée ici, ni son usage en introduction/classe inversée**. `origine_des_formats.md` mis à jour en conséquence : filiation sourcée précisément, sans revendiquer d'équivalence.

Correction apportée après relecture par l'utilisateur : « classe inversée » n'était pas le terme juste — le point visé est que l'apprenant va chercher le savoir lui-même plutôt que de le recevoir, posture active déjà rattachée à Knowles ailleurs dans ce même document (§1, `andragogie.md`), pas une référence supplémentaire. Entrée corrigée en conséquence.

**Devine-carte** : hypothèse *Time's Up!* confirmée directement par l'utilisateur (pas de vérification externe nécessaire, contrairement à Facettes — confirmation de première main plutôt qu'hypothèse à trancher). Contexte d'usage précisé : particulièrement adapté à un groupe ayant besoin de se détendre (fatigue, tension), avec une double fonction assumée détente + réactivation. Point pédagogique capturé dans la doc : les trois manches (explication libre, un mot, mime) ne testent pas le même niveau d'appropriation — le mime, sans recours verbal, est le plus exigeant des trois.

**Étude de cas** : établi sans discussion (méthode des cas, Harvard). Point ajouté par l'utilisateur, capturé dans la doc : ce gabarit se distingue des deux précédents par le niveau de taxonomie visé — `appliquer/analyser/évaluer` (et `créer` en option) contre `comprendre/appliquer` (Facettes) et `savoir/comprendre` (Devine-carte). Marque une bascule vers des gabarits de raisonnement complexe, pas de premier contact ou de réactivation.

**Simulation / mise en situation** : établi (apprentissage expérientiel, Kolb). Point important capturé : l'apprentissage produit est « discret mais réel », moins visible qu'une production écrite — rejoint directement le principe déjà central au skill sur la portée limitée d'une preuve (`activite_evaluee.md`). Question posée sur `properties.ludique: false` (semblait contredire « le jeu de rôle peut être très ludique ») — tranchée : la métadonnée est correcte, seul le jeu de rôle (registre théâtral) porte la dimension ludique, pas la simulation/mise en situation au sens de ce gabarit (confirmé par `V31-ACT02-2`, un entretien managérial sérieux). Point non traité, gardé pour plus tard : le nom du gabarit accole les deux notions ; une variante « jeu de rôle » plus légère et ludique n'est pas représentée séparément dans le catalogue candidat.

**Tabou conceptuel : écarté du catalogue V3.1.0.** À la différence de Facettes et Devine-carte, l'utilisateur n'a aucune validation de ce candidat (ni observé ni utilisé, ni formateur ni apprenant) — rompt le critère fondateur du chantier 1 (`promesse.md` : formats éprouvés, pas des inventions à valider a posteriori). Recommandation donnée et suivie : documenter le besoin réel qu'il vise (vérifier la compréhension au-delà du vocabulaire mémorisé — distinct de Devine-carte, qui teste la disponibilité en mémoire, pas la profondeur) séparément du véhicule hypothétique (adaptation du jeu Tabou), et ne pas l'intégrer tant qu'il n'est pas testé.

- `dossier-pedagogique/origine_des_formats.md` : nouvelle entrée « Tabou conceptuel — besoin identifié, véhicule non validé, hors catalogue V3.1.0 ».
- `validation/v3.1/non_regression/V31-ACT01-2.md` corrigé : `tabou_conceptuel` retiré de l'état de catalogue requis, du contraste visé, de la clause `FAIL` et de la validité technique — n'aurait plus dû être exigé comme distracteur d'un catalogue dont il est absent. `Devine carte` porte seul le contraste de nouveauté ludique face à `Quiz` dans ce scénario.

**Brainstorming** : établi (Osborn, 1953, *Applied Imagination*). Nuance pratique apportée par l'utilisateur, capturée dans la doc : le protocole ne s'anime pas tout seul, le formateur doit intervenir activement contre les longs silences — recoupe un risque documenté en créativité de groupe (*production blocking*, Diehl & Stroebe 1987). Combinaison observée avec les 5 Pourquoi (Toyota), technique distincte mobilisée en appui. Point non traité, pour l'implémentation future : cette exigence d'animation active et le recours aux 5 Why pourraient mériter une mention dans le contrat du gabarit lui-même (`typical_uses` ou section dédiée), pas seulement dans la doc de provenance.

**Planche météo** : établi comme genre (check-in d'état, répandu en facilitation/agile), pas comme forme unique (la métaphore météo est un choix parmi d'autres). Précision d'usage de l'utilisateur : à positionner comme rituel pour des formations un peu longues, répété au fil de la formation. **Incohérence de métadonnée détectée par cette précision, non corrigée dans le fichier candidat lui-même (encore dans `plus_tard/`)** : le front matter déclare `ritual.suitable: true` mais `typical_frequency: ponctuel`, ce qui contredit un usage rituel répété — à corriger au moment de l'intégration réelle du gabarit, pas dans ce document de provenance.

**Carte conceptuelle** : établi sans discussion (concept mapping, Novak, Cornell). Lien fait avec une source déjà citée ailleurs dans le même document (Ausubel, §1, apprentissage significatif) plutôt que traité isolément.

**En un mot** : établi comme genre (one word check-out, facilitation/agile), pas de source académique unique — même statut que Planche météo. Distinction faite avec Planche météo (que la ressemblance de surface aurait pu brouiller) : Planche météo regarde l'état de l'apprenant en ouverture, En un mot regarde les pratiques du formateur en clôture — confirmé par le formateur (fin de journée/séquence/séance, pour éclairer ses futures pratiques).

**Évaluation par les pairs** : établi sur deux plans (Topping 1998 en recherche pédagogique, module natif Moodle « Atelier »/Workshop). Point de vigilance apporté par l'utilisateur (niveau de taxonomie haut, critères à bien préciser) relié directement à la doctrine déjà centrale du skill (`activite_evaluee.md`, `opo.md`) plutôt qu'à une référence externe supplémentaire — sans critères explicites, cette activité redevient exactement le jugement arbitraire que le skill interdit ailleurs.

**Rétrospective** : établi (rétrospective Agile/Scrum ; Schwaber & Sutherland pour la cérémonie, Derby & Larsen 2006 pour la forme facilitée diffusée). Point distinctif apporté par l'utilisateur, capturé dans la doc avec un schéma comparatif : régulation **collective horizontale** (le groupe identifie et priorise ensemble) contre la collecte **individuelle verticale** de Planche météo et En un mot (chacun s'exprime séparément, le formateur synthétise). Empêche de traiter Rétrospective comme une simple variante longue d'En un mot.

**Les 11 candidats de `plus_tard/nouvelles_activites_v3_metadonnees.zip` sont maintenant tous classés dans `dossier-pedagogique/origine_des_formats.md`** : 10 intégrables au catalogue V3.1.0 (Facettes, Devine-carte, Étude de cas, Simulation/mise en situation, Brainstorming, Planche météo, Carte conceptuelle, En un mot, Évaluation par les pairs, Rétrospective), Tabou conceptuel étant le seul écarté pour absence de validation par l'utilisateur.

Récapitulatif des points non traités, à reprendre à l'implémentation réelle (pas dans ce document de provenance) :

- `en_cours/references/activite.md` doit référencer chaque nouveau gabarit (§5 de `base_de_travail.md`, prérequis déjà documenté dans `validation/v3.1/non_regression/README.md`) ;
- `SKILL.md` doit évoluer sur `typical_uses` → métadonnées de sélection plus riches (front matter des candidats), prérequis déjà documenté ;
- `planche_meteo.md` : `typical_frequency: ponctuel` incohérent avec l'usage rituel décrit, à corriger ;
- `brainstorming.md` : gagnerait une mention de l'animation active nécessaire et du recours possible aux 5 Why ;
- `activites_type_origine_retravaillees.zip` (les 4 gabarits actuels retravaillés) n'a pas encore été passé en revue de la même façon — reste à faire si on veut une couverture complète avant le gel de V3.1.0.

---

## 2026-09-03 — Ajout `V31-ACT01-3` : biais de familiarité (Planche météo)

L'utilisateur signale un risque distinct de ceux déjà couverts : pas seulement « manquer un gabarit absent » ou « le favoriser par nouveauté », mais **se rabattre sur un gabarit familier (`Atelier`, `Quiz`) par habitude alors qu'un gabarit récent y répond plus précisément**. Exemple donné : un besoin de connaître l'état du moment de chaque apprenant doit faire reconnaître `Planche météo` (`purpose` vérifié : « faire exprimer à l'apprenant son état du moment… disponibilité, énergie, ressenti »), pas un tour de table en `Atelier` ni un diagnostic en `Quiz`.

- `en_cours/promesse.md`, ACT02 : paragraphe ajouté précisant que « le plus proche » se détermine sur la finalité déclarée à travers tout le catalogue, pas par défaut vers un gabarit générique déjà connu — avec l'exemple météo.
- Nouveau `validation/v3.1/non_regression/V31-ACT01-3.md` : scénario symétrique de `V31-ACT01-2` (qui protège contre le biais de nouveauté) — celui-ci protège contre le biais de familiarité, sens opposé. `README.md` et `CLAUDE.md` du dossier mis à jour (6 scénarios, le dernier non encore joué).
- Non traité : ce scénario n'a pas encore été joué, même en exploratoire.

---

## 2026-09-03 — ACT02 : flux de décision explicité (Moodle comme ancrage), oracle V31-ACT02-3 élargi

L'utilisateur précise le flux de décision d'ACT02, en s'appuyant sur Moodle comme exemple concret de LMS où ce type d'activités existe déjà : **situation + objectif → une activité du catalogue correspond-elle ? → sinon, dériver du gabarit existant le plus proche plutôt que reconstruire depuis zéro.** Ce flux correspond exactement à ce que les cinq runs exploratoires avaient déjà produit sans qu'on le leur demande explicitement (`Atelier` adapté deux fois, `Brique` adapté une fois).

- `en_cours/promesse.md`, ACT02 : diagramme du flux de décision ajouté en tête ; la clause de repli reformulée — « adapter le gabarit existant le plus proche » remplace « construire depuis le socle commun » comme premier réflexe attendu, la construction pure depuis le socle restant possible mais secondaire. Référence explicite aux runs exploratoires comme preuve que ce comportement existe déjà.
- `validation/v3.1/non_regression/V31-ACT02-3.md` : oracle élargi — la clause qui n'autorisait explicitement qu'`Atelier` comme repli générique couvre désormais aussi `Brique`, qui était le choix réellement observé dans le run et n'était pas nommé dans l'oracle initial. Corrige un écart entre l'oracle écrit et le principe qu'il est censé vérifier.

---

## 2026-09-03 — Réponse à la question de conception ouverte (finding des runs exploratoires)

L'utilisateur répond à la question laissée ouverte par les runs exploratoires : la valeur du chantier 1 ne tient pas à une capacité absente du socle, mais à la mise à disposition de formats **courants, déjà éprouvés par un formateur expérimenté**, pour que l'agent les mobilise plutôt que de reconstruire une structure équivalente par improvisation à chaque fois — la fiabilité et la systématicité du résultat priment sur la seule capacité brute. Point ajouté par l'utilisateur : la plupart de ces formats existent déjà sous des noms proches dans les LMS courants, ce qui en fait un vocabulaire partagé avec le terrain plutôt qu'un vocabulaire propre au skill.

Cette lecture change le statut du finding précédent sans l'invalider : que `Atelier` improvisé retombe près de la structure de `Facettes` n'est plus un signal défavorable à ACT01, c'est même attendu — la question que les scénarios doivent trancher n'est pas « le socle peut-il y arriver » mais « le gabarit y arrive-t-il de façon fiable, contrairement à une improvisation qui dépend de la capacité du modèle ce jour-là ».

- `en_cours/promesse.md`, tête du Chantier 1 : paragraphe ajouté portant cette double justification (formats éprouvés, vocabulaire LMS partagé) et reformulant ce que la phase SPEC doit viser (fiabilité plutôt que capacité brute).
- Implication non traitée à ce stade, à garder en tête pour la suite : si la fiabilité est le critère, les scénarios devraient à terme comparer plusieurs runs indépendants sur un même stimulus (répétition), pas un seul run par scénario — question à trancher au moment de construire la campagne réelle, pas dans ce paragraphe de promesse.

---

## 2026-09-03 — Premiers runs exploratoires des 5 scénarios V3.1.0 (aveugles, informels)

Runs joués via cinq sous-agents vierges (sans accès à cette conversation ni aux oracles), restreints par consigne à `en_cours/SKILL.md` et `en_cours/references/`, scorés a posteriori contre les oracles de `validation/v3.1/non_regression/`. **Exploratoire, pas une campagne officielle** : pas d'isolation par workspace dédié, pas de manifeste SHA-256, pas de couche opérateur séparée, verbatims non persistés sur disque (conservés dans la conversation Claude Code uniquement).

- **`V31-ACT01-2` : PASS.** `Quiz` retenu, en format oral individuel plutôt qu'écrit, avec justification explicite (`andragogie.md`). Diagnostic individuel correctement construit.
- **`V31-ACT02-3` : PASS.** `Brique` retenu pour la phase d'observation, l'agent signalant explicitement que l'exploitation relève d'une activité distincte à construire au retour (`Recul` pressenti) — décomposition en deux temps exactement conforme à l'oracle. Aucun force-fit : ni `Simulation` (rien n'est simulé), ni `Étude de cas` (aucun dossier inventé).
- **`V31-ACT01-1`, `V31-ACT02-1`, `V31-ACT02-2` : non évaluables contre l'oracle écrit** — les gabarits cibles (`Facettes`, `Étude de cas`, `Simulation / mise en situation`) sont absents du catalogue actuel (candidat limité à `atelier`, `brique`, `quiz`, `recul`), confirmant le prérequis bloquant déjà documenté.

**Finding non anticipé** : sur ces trois runs, l'agent n'a pas simplement échoué faute d'outil — `Atelier` seul a produit des activités structurellement très proches des gabarits cibles. Sur la paire `V31-ACT02-1`/`-2`, le même label (`Atelier`) recouvre deux contenus réellement différenciés (analyse de dossier vs. jeu de rôle avec fiches confidentielles), montrant que le raisonnement pédagogique sous-jacent fonctionne déjà avec le seul socle. Confirme empiriquement la réserve déjà notée sur `V31-ACT01-1` (scénario le plus faible de la batterie).

**Question de conception ouverte, non tranchée** : la valeur ajoutée d'ACT01/ACT02 tient-elle à une capacité absente du socle générique, ou à autre chose (contrat imposé plus strict qu'`Atelier` ne l'impose — ex. interdiction explicite d'inventer un dossier —, vocabulaire partagé avec le formateur, fiabilité sur un modèle moins capable, rapidité d'invocation) ? Si c'est la seconde famille, l'observable des propriétés ACT01/ACT02 mériterait peut-être de porter sur autre chose que le nom du gabarit prononcé. Décision reportée à l'utilisateur.

Aucune modification de `promesse.md`, des oracles ou du scope du chantier 1 à ce stade.

---

## 2026-09-03 — Gel prématuré de la promesse V3.1.0, annulé

Malentendu sur une réponse de l'utilisateur à la question « on gèle maintenant ou on attend un tour de runs ? ». Lu comme un choix explicite de geler quand même (motif compris : le texte n'a pas changé depuis les revues, donc peu de risque). Statut « gelée » appliqué à `promesse.md`, `en_cours/CLAUDE.md`, `.claude/CLAUDE.md` et `validation/v3.1/non_regression/CLAUDE.md`.

**Correction** : l'utilisateur voulait dire l'inverse — que jouer les scénarios maintenant échouerait probablement faute d'avoir travaillé le runtime, pas qu'il fallait geler sans les jouer. Il voulait que les scénarios soient effectivement joués, pas sauter cette étape. Les quatre fichiers repassés à l'état « non gelée, prête pour SPEC » (texte identique à l'état d'avant le gel prématuré).

Aucun impact réel : rien n'était commité entre le gel et son annulation.

---

## 2026-09-03 — Scénarios candidats V3.1.0 : revue, correction et ajout

Cinq fiches créées dans `validation/v3.1/non_regression/` à partir d'une proposition externe, corrigée après vérification sur le matériau réel. **Aucun run joué.**

- Vérification favorable : les finalités supposées par les oracles correspondent exactement aux `purpose` déclarés des brouillons de `plus_tard/` (Facettes = exploration répartie, Étude de cas = analyse contextualisée, Simulation = action en situation, Devine carte = récupération ludique/collective).
- **Trois prérequis bloquants documentés** (`README.md`) : (1) `references/activite.md` l. 21-24 énumère le catalogue et se déclare « premier niveau de sélection », donc tout gabarit joué doit y être référencé ; (2) `SKILL.md` l. 72 nomme `purpose` et `typical_uses`, or les gabarits de `plus_tard/` n'ont plus `typical_uses` (remplacé par `selection_keywords`, `participation`, `properties`, `taxonomy_levels`) — la micro-évolution du §5.3 devient un prérequis, pas une option ; (3) schéma de front matter mixte entre les 4 gabarits du candidat et les 15 de `plus_tard/`, rendant certains contrastes asymétriques.
- Deux voies d'exécution posées : injection de fixture dans la copie isolée avec recalcul du manifeste SHA-256 (précédent `NOY014`), recommandée pour respecter l'ordre du §15 ; ou implémentation préalable d'un sous-ensemble du catalogue.
- **Corrections appliquées** : stimulus de `V31-ACT01-2` délexicalisé — la formulation « je n'ai pas besoin d'une dimension ludique ni d'un travail collectif » niait littéralement deux champs de front matter et permettait de réussir par appariement de mots-clés, validant la table de décision mécanique que la promesse rejette ; retrait des phrases dictant la réponse dans la paire `V31-ACT02-1`/`-2` (« ils ne jouent pas la scène », « pas sur l'analyse préalable »), même défaut que celui corrigé sur `NOY013` en V2.1 ; clause de `FAIL` subjective de `V31-ACT01-2` (« sans justification permettant d'expliquer ») remplacée par un cas limite admissible à trois conditions cumulatives ; motif du choix sorti du verdict principal dans la paire ACT02 et borné aux motifs explicitement énoncés ; état de catalogue requis explicité par fiche avec avertissement de vacuité (précédent du `PASS` vacuous de `NOY014_2`) ; convention opérateur factorisée dans le `README.md` au lieu d'être répétée dans chaque fiche.
- **Ajout `V31-ACT02-3`** : besoin non couvert (observation en situation réelle non encadrée) → construire depuis le socle sans forcer un gabarit. Couvre ce que la promesse disclaime explicitement et qui n'était testé par aucune fiche, alors que le force-fit est le risque propre à l'enrichissement du catalogue. Oracle comportemental assumé, avec clause explicite rendant `Atelier` admissible pour éviter que le scoreur applique une règle plus stricte que l'oracle.
- Écart de convention consigné : identifiants `V31-<propriété>-<n>` plutôt que `NOY00x`, motivé par l'exigence du §9 (« directement relié à une propriété de promesse ») ; `validation/v3.1/non_regression/CLAUDE.md` corrigé, qui prescrivait encore la numérotation `NOY`.
- Réserve signalée : l'absence de comparaison A / B′ est défendable par la règle du projet sur les contrats propres au produit (`README.md` racine, qui cite nommément « la représentation du catalogue de gabarits »), mais elle retire un des deux appuis de la note SPEC d'ACT01 — la charge de preuve repose donc entièrement sur les scénarios négatifs et la paire contrastive.
- Encodage : la proposition reçue était de nouveau en mojibake, réécrite en UTF-8.

---

## 2026-09-03 — Décision : ne pas geler la promesse V3.1.0 maintenant

Proposition initiale de geler `promesse.md` immédiatement, avant tout scénario SPEC. Signalé comme contradictoire avec l'ordre du §15 corrigé le même jour (SPEC → A/B′ → ajuster → geler → implémenter), dont le but est justement de repérer une propriété peu discriminante avant de la figer. Question posée à l'utilisateur, tranchée pour respecter l'ordre du §15.

- `en_cours/promesse.md`, section « Statut de cette promesse » : reformulée en « candidate stabilisée pour V3.1.0, prête pour la phase SPEC — pas encore gelée » ; les points déjà couverts par les deux passes de revue (examen des propriétés, doublons) marqués faits ; le gel explicitement repoussé après scénarios, tests A/B′ et ajustement éventuel.
- Aucun autre fichier modifié. La création des scénarios SPEC reste à la main de l'utilisateur, pas engagée automatiquement.

---

## 2026-09-03 — Révision de la promesse V3.1.0 avant gel (retour de revue externe)

Retour de revue externe (ChatGPT) sur la promesse V3.1.0 fraîchement rédigée, vérifié point par point avant application (6 points retenus sur 7).

- `en_cours/promesse.md` : titre nettoyé d'une URL parasite collée accidentellement (corruption de copier-coller, sans lien avec le contenu) ; §0 « Socle hérité de la V2.1 » fortement allégé (pointeur + liste courte au lieu de la restitution intégrale de S01-S03 et des garanties, pour éviter une double source normative avec le runtime V2.1) ; ACT01 recentré sur la découvrabilité d'un gabarit nouvellement ajouté (distinct d'ACT02, le départage entre candidats plausibles) ; nouvelle sous-section « Invariant d'architecture » isolant la contrainte de conception (pas de nouvelle règle générale au noyau pour rendre un gabarit utilisable), non observable par un scénario, du comportement observable ; promesse centrale et intro débarrassées des tournures trop tutorat-centrées (« des acquis disponibles », « tuteur parfait », « accompagnement » dans le schéma), hors périmètre du chantier 1 seul.
- `en_cours/base_de_travail.md` §15 : correction d'une incohérence préexistante (déjà présente avant le séquencement en mineures) — le diagramme plaçait « geler la promesse » avant la création des SPEC et l'ajustement des propriétés, alors que `promesse.md` §Statut décrit correctement l'ordre inverse (« ajustée puis gelée »). Ordre corrigé dans les trois blocs (V3.1.0, V3.2.0, V3.3.0).
- **Suggestion écartée** : renommer `validation/v3.1/non_regression/` en `spec/` ou `validation_promesse/` au motif que des scénarios pré-gel ne sont pas encore de la non-régression. Rejetée : `validation/v2.1/non_regression/` a déjà hébergé des scénarios candidats non stabilisés (NOY012_1/2, NOY013) avant leur gel sous ce même nom — c'est la convention établie du dépôt, pas une imprécision de vocabulaire. Conserver le nom pour rester cohérent avec `v2.1/`.
- **Deuxième passe de revue, même jour** : l'invariant d'architecture est requalifié en invariant **hérité de la V2.1** à préserver, non en propriété nouvelle — vérifié sur le runtime (`SKILL.md` l. 72 décrit un départage générique par front matter, sans nommer de gabarit). Précision ajoutée à partir de cette vérification : la découvrabilité repose sur le catalogue énuméré de `references/activite.md` (l. 21-24, « premier niveau de sélection »), donc référencer un nouveau gabarit y reste nécessaire — question de conception ouverte pour la mineure, vu le passage envisagé de 4 à ~15 entrées. ACT01 recentré sur « mobiliser le catalogue enrichi » avec clause anti-biais de nouveauté et observable négatif ; observable d'ACT02 rendu scorable (choix justifiable) ; note SPEC ajoutée signalant que la moitié positive d'ACT01 est trivialement satisfiable et que le pouvoir discriminant tient à l'observable négatif et au contraste A / B′.
- Distinction de cycle de vie retenue sans changement de structure : les scénarios de `validation/v3.1/non_regression/` y vivent d'abord comme candidats de validation de la promesse et ne constituent une batterie de non-régression qu'après promotion — le qualificatif « candidat » du dossier porte déjà cette distinction, comme pour `v2.1/`.
- Incident sans lien avec le contenu : la version relue reçue de l'extérieur était en mojibake (UTF-8 lu en Latin-1) ; réécriture directe en UTF-8, aucun caractère abîmé conservé.
- Aucun scénario SPEC créé à ce stade ; la promesse V3.1.0 reste non gelée.

---

## 2026-09-03 — Démarrage de la mineure V3.1.0 (chantier 1 : catalogue d'activités)

Engagement de la première mineure de la trajectoire décrite par `en_cours/base_de_travail.md` §4.1 (V3.1.0 → V3.2.0 → V3.3.0), après le séquencement du plan de travail V3 en mineures indépendantes.

- `en_cours/VERSION` : `V3` → `V3.1`.
- `en_cours/promesse.md` réécrite en promesse candidate **V3.1.0** : conserve le socle hérité de la V2.1 (S01–S03, garanties) et le chantier 1 (ACT01, ACT02) à l'identique du contenu précédent ; retire les sections Chantier 2 (COG01–02) et Chantier 3 (TUT01–04), non engagées par cette mineure ; « Ce que la V3 ne promet pas » et le critère comportemental central recentrés sur le seul choix d'activité. Les chantiers 2 et 3 seront réintégrés au document lors des mineures V3.2.0 et V3.3.0 (promesse amendée en place, pas de fichier séparé par mineure).
- `en_cours/CLAUDE.md` : section « État actuel » alignée sur V3.1 et sur le périmètre réduit de la promesse.
- Création de `validation/v3.1/non_regression/` et de son `CLAUDE.md` (statut, numérotation à définir, non-régression cumulative en une seule passe, avant-gel, promotion) — dossier encore vide, aucun scénario créé à ce stade.
- `.claude/CLAUDE.md` : « État des versions », « Carte du dépôt » et « Sources de vérité » mis à jour pour refléter la mineure V3.1.0 et le nouveau dossier `validation/v3.1/non_regression/`.
- Création de ce journal (`docs/historique_3.md`), sur le modèle de `docs/historique_2.1.md`.
- Rappel pour mémoire : `plus_tard/activites_type_origine_retravaillees.zip` (gabarits existants retravaillés) et `plus_tard/nouvelles_activites_v3_metadonnees.zip` (onze gabarits candidats + métadonnées) sont le matériau brouillon disponible pour ce chantier (`base_de_travail.md` §5.5), pas encore trié ni intégré.
- Aucun fichier runtime (`SKILL.md`, `references/`) modifié à ce stade ; aucun scénario SPEC créé ; la promesse V3.1.0 n'est pas gelée.

---

## Comment utiliser ce fichier

Avant chaque commit touchant au candidat V3, ajouter une entrée courte : date, ce qui a changé, hash du commit une fois créé. Pas de détail d'implémentation ici — il vit dans les fichiers sources (`promesse.md`, `base_de_travail.md`, les fiches NOY, les `CLAUDE.md` de chaque dossier).
