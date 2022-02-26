---
title: "Détermination de la composition d'une solution colorée, loi de Beer-Lambert"
subtitle: "Chapitre 5,1"
author: ""
type: ""
date: 2020-10-05T09:38:31+04:00
draft: false
toc: true
tags: ["Soluté", "Concentration molaire", "Concentration massique", "Beer Lambert", "Dilution", "Couleur", "Absorption"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---
[^2]: On suppose que la dissolution s'effectue sans changement de volume.

Il est assez facile de calculer la concentration massique ou la concentration molaire lorsqu'on sait comment la solution a été préparée : il suffit de *diviser la masse (ou la quantité de matière) de soluté apporté par le volume du solvant*[^2].  
> Mais comment déterminer la concentration en soluté apporté d'une solution que l'on n'a pas préparé&nbsp;? Comment vérifier la valeur de la concentration en soluté apporté d'une solution&nbsp;?

> Ce chapitre introduit une méthode permettant de répondre à ces questions **à la condition que la solution soit colorée** !

## Pourquoi une solution est-elle colorée&nbsp;?

### Lumière blanche

{{% note tip %}}
- La **lumière blanche** contient toutes les radiations visibles par l'œil.
- Ces différentes radiations sont caractérisées par leur **longueur d'onde** $\lambda$ et *perçues comme des lumières de couleurs différentes*. *À chaque longueur d'onde correspond une couleur*.
{{% /note %}}

<img src="/premieres-pc/chap-2/chap-2-2-1.gif" alt="" width="85%" />
> Spectre de la lumière blanche

| Couleur | Violet | Bleu | Vert | Jaune | Orange | Rouge |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| $\lambda$ (m) | 400 -- 424 | 424 -- 491 | 491 -- 575 | 575 -- 585 | 585 -- 647 | 647 -- 750 |


### Lumière colorée

- Une lumière *ne comportant pas toutes les radiations du spectre visible* ou *des radiations en proportions très différentes* est colorée.
- Dans le cas où une couleur est absente, la couleur de la lumière est la **couleur complémentaire** de cette couleur.

<img src="/premieres-pc/chap-2/chap-2-2-2.jpg" alt="" width="60%" />
> L'analyse d'une lumière (ici plutôt rouge) permet de déterminer non seulement quelles radiations la composent mais aussi dans quelles proportions. Cette analyse est effectuée à l'aide d'un **spectrophotomètre**.

{{% note tip %}}
On appelle **couleurs complémentaires** deux couleurs dont la superposition donne une lumière blanche.
{{% /note %}}

<img src="/premieres-pc/chap-2/chap-2-2-3.png" alt="" width="40%" />

### Solution colorée

{{% note tip %}}
Une lumière, dite **incidente**, qui entre en contact avec une solution, peut être **diffusée** ou **absorbée**.
{{% /note %}}

<img src="/premieres-pc/chap-2/chap-2-2-4.png" alt="" width="60%" />


{{% note tip %}}
- Une solution est colorée si *elle absorbe une partie des radiations de la lumière incidente*.   
- *La solution soustrait à la lumière incidente les couleurs qu’elle absorbe.*
- La **couleur de la solution** est alors la *couleur complémentaire de la couleur absorbée*.
{{% /note %}}

## Loi de Beer-Lambert

### Absorbance d'une solution colorée

{{% note tip %}}
L'**absorbance** $A$ d'une solution colorée est *une grandeur **sans unité** qui caractérise l'aptitude des entités chimiques présentes dans la solution à absorber une radiation lumineuse de longueur d'onde $\lambda$ donnée*.
{{% /note %}}

<img src="/premieres-pc/chap-2/chap-2-2-5.png" alt="" width="60%" />

L'expression mathématique de l'absorbance $A$ (**qu'il ne faut pas apprendre&nbsp;!**) est 

$$A_{\lambda} = \log \left( \dfrac{I_0}{I_{\lambda_{\lambda} }}  \right)$$

Ce qu'il faut retenir, c'est que *l'absorbance fait intervenir une comparaison des intensités des lumières incidente et transmise*.

### Loi de Beer-Lambert

La **loi de Beer-Lambert**, découverte par Pierre Bouguer en 1729, est *une relation empirique reliant l'absorption de la lumière aux propriétés des milieux qu'elle traverse*.

{{% note tip %}}
La **loi de Beer-Lambert** établit une *proportionnalité entre la concentration molaire $C$ d'une entité chimique en solution, l'absorbance $A$ de celle-ci et la longueur $l$ du trajet parcouru par la lumière dans la solution*.
$$A_λ=ε_λ l C$$

En pratique, on utilise
$$A_λ=k C$$
Le coefficient de proportionnalité $k$ a pour unité $\pu{L/mol}$.
{{% /note %}}

{{% note warning %}}
La loi de Beer-Lambert n'est cependant valable que sous certaines conditions&nbsp;: 
- *la lumière doit être monochromatique*&nbsp;;
- *les solutions doivent être homogènes*&nbsp;;
- *la concentration de la solution en soluté doit être faible (inférieure à $\pu{1e-2 mol/L}$)*&nbsp;;
- *le soluté ne doit pas réagir sous l'action de la lumière incidente*.
{{% /note %}}

## Dosage spectrophotométrique (ou colorimétrique)

{{% note tip %}}
- **Doser une solution** consiste à *déterminer la concentration (molaire) d'une espèce chimique en solution*. 
- Un dosage colorimétrique est un type de dosage possible lorsque l'espèce chimique colore la solution et que la loi de Beer-Lambert peut être utilisée.
{{% /note %}}

{{% note normal %}}
- Il est nécessaire de réaliser, dans un premier temps, une **courbe d'étalonnage** à l'aide d'une **échelle de teinte** dont *les concentrations encadrent la concentration recherchée*.
- *La longueur d'onde du filtre choisi doit correspondre au rayonnement pour lequel l'absorbance de la solution est maximale*.
{{% /note %}}



