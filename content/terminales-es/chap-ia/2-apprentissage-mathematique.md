---
title: "Exemples de méthodes d’apprentissage"
subtitle: ""
author: ""
type: ""
date: 2023-03-06T14:01:18+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

> Différentes méthodes sont ici présentées dans des contextes simples (nombre limité de données). L’objectif pédagogique est de faire comprendre les méthodes mathématiques utilisées dans un cadre beaucoup plus complexe (notamment quant au nombre de données utilisées) en intelligence artificielle.

## Les courbes d’ajustement

{{% note normal %}}

Cette méthode repose sur un **traitement statistique des données** :

- celles-ci, fournies lors de la phase d’apprentissage, *peuvent être représentées par un nuage de points*.
- Des méthodes statistiques permettent d’*ajuster ce nuage par une courbe* (droite, parabole, exponentielle).
- Les *paramètres de cette courbe sont déterminés à l’aide des données* : c’est la **phase d’entraînement**.
- La connaissance de cette courbe permet alors de prédire des valeurs pour des points de mesure absents : c’est la **phase d’inférence**.

{{% /note %}}

### Évolution du prix du mètre-carré dans le 6e arrondissement de Paris

| Année $x_i$ | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Prix $y_i$ | 4562 | 5270 | 5400 | 6020 | 6460 | 7360 | 8090 | 8840 | 9830 | 10100 | 9690 | 11870 | 12400 | 12250 | 11820 | 11280 | 12150 | 12320 | 12530 | 13880 |

> Évolution du prix du mètre carré dans le 6ème arrondissement de Paris (année 0 en 2000).

Les données antérieures à l’année 2020 constituent des données à partir desquelles on détermine l’équation d’une courbe approchant les données.

1. Tracer le nuage de points à l'aide d'un tableur.

2. Justifier qu'il peut être ajusté par une droite.

{{% note normal %}}

Lorsqu'un nuage de points peut être ajusté par une droite, on parle de régression linéaire.

{{% /note %}}

3. Établir les caractéristiques de la courbe de tendance (de la droite donc).

4. Estimer le prix du mètre carré dans le 6ème arrondissement en 2020.

5. De la même façon, estimer le prix du mètre carré dans le 6ème arrondissement en 1999.

{{% note normal %}}

#### Comment la droite d'ajustement est-elle déterminée ?

La droite d'ajustement est la droite qui passe par des valeurs aux points de mesures au plus près des vraies valeurs mesurées, dans un sens mathématique bien précis, celui des moindres carrés. Si on note $y=ax+b$ l'équation de la droite, on veut minimiser la somme des carrés des différences entres les vraies valeurs $y_i$ et leurs prédictions par la droite $a x_i + b$, soit trouver $a$ et $b$ qui minimisent $\sum_{i=1}^n (y_i - (ax_i+b))^2$.

Il convient de remarquer que la plupart des algorithmes d'apprentissage consistent à déterminer les valeurs des paramètres pour minimser l'erreur effectuée par la fonction de classification ou de régression qui est en train d'être apprise : on parle d'**optimisation**.

{{% /note %}}

## L'algorithme des plus proches voisins

### Modèle simplifié

On suppose que les données d’apprentissage sont classifiées en deux catégories ($M$ et $B$). On veut placer dans l’une ou l’autre de ces deux catégories une donnée nouvelle. Pour cela, on calcule sa distance à chacune des données déjà étiquetées et on lui attribue la catégorie de son plus proche voisin.

### Exemple d’utilisation dans le dépistage automatique d’une tumeur maligne

On se propose de répartir en deux catégories (Maligne, Bénigne) des tumeurs du
sein dont on connaît un certain nombre de caractéristiques. Dans la réalité, un tel diagnostic automatique est effectué à partir de données d’apprentissage portant sur une cinquantaine de caractéristiques mesurées sur un échantillon d’un millier de tumeurs déjà étiquetées « Maligne » ou « Bénigne ». Dans un souci de simplification, on se restreint ici
à 2 caractéristiques (diamètre et concavité) mesurées sur un panel de 10 patientes.

<center>

| Diamètre moyen (mm) | Concavité moyenne | Catégorie |
| :--: | :--: | :--: |
| 13,2 | 8,3 | Bénigne |
| 18,7 | 19,7 | Bénigne |
| 8,2 | 15,9 | Maligne |
| 13,2 | 9 | Bénigne |
| 13,5 | 4,8 | Maligne |
| 11,8 | 1,7 | Maligne |
| 13,6 | 1,9 | Maligne |
| 12 | 2 | Maligne |
| 18,2 | 17,7 | Bénigne |
| 12 | 6,6 | Maligne |

</center>

On considère une nouvelle tumeur de diamètre et de concavité connues et on cherche à savoir si elle est maligne ou bénigne.

### Méthode du plus proche voisin

On cherche parmi les données (triangles rouges pour les tumeurs malignes et losanges bleus pour les tumeurs bénignes) celle qui est la plus proche de la nouvelle donnée à catégoriser (point vert). On lui attribue la catégorie de son plus proche voisin.

<!--
<a href="https://www.geogebra.org/m/wwj9zm97" target="_blank">Accès à l'appliquette en ligne</a>
-->

<iframe scrolling="no" title="Copie de Illustration de la méthode du plus proche voisin" src="https://www.geogebra.org/material/iframe/id/vbmnddfv/width/1305/height/668/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="1305px" height="668px" style="border:0px;"> </iframe>

1. On considère une nouvelle tumeur ayant un diamètre de 10 mm et une concavité de 12. Comment l'algorithme la classe-t-elle ?
**Déplacer le point vert.**

2. Sélectionner « Coloriage » et « Frontière », puis déplacer le point vert.  
Peut-on mettre en évidence deux régions bien spécifiques de l'espace ?

### Méthode des 5 plus proches voisins

<iframe scrolling="no" title="Illustration de la méthode des 5 plus proches voisins" src="https://www.geogebra.org/material/iframe/id/yphmup2w/width/502/height/747/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="502px" height="747px" style="border:0px;"> </iframe>

La méthode peut être généralisée à $k$ plus proches voisins. Il suffit de considérer les $k$ voisins les plus proches, d’identifier la catégorie à laquelle appartient la majorité de ces voisins et d’affecter au nouveau point cette catégorie.

3. On considère une nouvelle tumeur ayant un diamètre de 10 mm et une concavité de 12. Comment l'algorithme la classe-t-elle ?
**Déplacer le point vert.**
