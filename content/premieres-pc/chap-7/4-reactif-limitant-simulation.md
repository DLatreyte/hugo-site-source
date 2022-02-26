---
title: "Recherche d'un réactif limitant à l'aide d'un programme écrit en Python"
subtitle: "Chapitre 6,4"
author: ""
type: ""
date: 2021-01-09T21:54:37+04:00
draft: false
toc: true
tags: ["Python", "Mélange initial stœchiométrique", "Tableau d'avancement", "Réactif limitant"]
categories: ["Premières Spé PC", "Chimie"]
image: ""
solution_est_visible: true
auto_numbering: true
---

On réalise l'oxydation des ions fer II $\ce{Fe^{2+} (aq)}$ par des ions permanganate $\ce{MnO4^- (aq)}$ en milieu acide.\
Les couples oxydant/réducteur mis en jeu sont : $\ce{Fe^{3+}/Fe^{2+}}$ et $\ce{MnO4^-/Mn^{2+}}$.

1. Montrer que l'équation de la réaction s'écrit :
$$
\ce{5 Fe^{2+} (aq) + MnO4^- (aq) + 8 H^+ --> 5 Fe^{3+} (aq) + Mn^{2+} (aq) + 4 H2O  }
$$

On met en présence $\pu{10 mL}$ d'une solution de permanganate de potassium à la concentration $\pu{0,03 mol.L-1}$ en ion permanganate et $\pu{10 mL}$ d'une solution de sulfate de fer II à la concentration $\pu{0,1 mol.L-1}$ en ion fer II. On acidifie cette solution en ajoutant de l'acide sulfurique. Le volume final de la solution est égal à $\pu{25 mL}$ et son pH vaut $\pu{1,0}$.

La transformation chimique associée à la réaction présentée est supposée totale.

Remarque
: Calcul de la concentration en ions $\ce{H+}$ à partir des données : $[\ce{H+}] = C^o \cdot 10^{-\mathrm{pH}}$ avec $C^o = \pu{1,00 mol.L-1}$.\
La notation $[\ce{H+}]$ sera explicitée dans un autre document.

{{% note exercise %}}

- Le programme Python à compléter se trouve à cette {{< remote "adresse" "https://repl.it/@dlatreyte/Simulation-Transformation-Chimique-Eleve-1ere" >}}

- Le corrigé se trouve à cette {{< remote "adresse" "https://repl.it/@dlatreyte/Simulation-transformation-chimique-1ere" >}}

{{% /note %}}

2. À partir des explications au début du fichier, compléter toutes les lignes (88 à 96) de la partie `# Variables du problème`.

3. Compléter l'instruction qui permet de calculer la concentration en ions oxonium dans le milieu à la ligne 99.

4. Compléter l'instruction à la ligne 30. Cette instruction calcule une quantité de matière à partir d'un volume et d'une concentration.

5. Compléter l'instruction à la ligne 50. Cette instruction permet de déterminer si le mélange initial est stœchiométrique.

6. Établir le tableau d'avancement de la transformation chimique.

7. À quoi sert la ligne 57 ?

8. Compléter l'instruction à la ligne 59. Cette instruction calcule la quantité de matière d'un réactif à partir de sa quantité de matière initiale et de la valeur de l'avancement de la réaction.\
On pourra s'aider du tableau d'avancement.

9. Lancer le programme.
    - Le mélange initial est-il stœchiométrique ?
    - Quel est le réactif limitant ?
    - Quelle est la valeur de l'avancement maximal ?

10. Confirmer ces résultats en faisant vous-même les calculs.