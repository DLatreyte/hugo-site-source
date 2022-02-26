---
title: "Dosage par étalonnage d'un sérum physiologique"
subtitle: "Chapitre 5,4"
author: ""
type: ""
date: 2020-10-10T21:24:38+04:00
draft: false
toc: true
tags: ["Dosage", "Étalonnage", "Conductimétrie", "Kohlrausch"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Documents

### Solution physiologique

Une **solution physiologique** est un *liquide isotonique* au sang, c’est-à-dire exerçant la même pression osmotique sur les membranes cellulaires que les principaux fluides corporels, en particulier le sang humain. Une telle solution est également nommée liquide physiologique ou, improprement, sérum physiologique (en fait il ne s'agit pas d'un sérum car il ne provient pas directement du sang).

La solution est généralement composée d'eau distillée et de chlorure de sodium ($\ce{NaCl}$) dilué à 9 pour $1\\,000$ (c'est-à-dire une solution à 0,9&nbsp;% de masse/volume de $\ce{NaCl}$, soit $\pu{9 g.L-1}$).

Certaines solutions physiologiques d'usage commun sont commercialement disponibles à diverses concentrations à des fins différentes.
<div style="text-align: right;"> 
<a href="https://fr.wikipedia.org/wiki/Solution_physiologique">Wikipedia</a>
</div>

### Conductivité et concentration molaire

La conductivité $\sigma$ d’une solution ionique caractérise sa *capacité à conduire le courant électrique*. Elle s’exprime en Siemens par mètre ($\pu{S.m-1}$). *La conductivité d’une solution ionique dépend de la nature et de la concentration des ions présents* et de la température. 

**Remarque.** En pratique, on mesure souvent $\sigma$ en $\pu{mS.cm-1}$ : $\pu{1 mS.cm-1} = \pu{1e-1 S.m-1}$.

### Conductimètre

La cellule de mesure est constituée d’un corps en plastique et de 2 plaques de platine platiné parallèles (surface $S$ et distantes de $L$). Pour chaque cellule, la constante de cellule est définie par $K_{\text{cell}} = S / L$.

Le conductimètre est un ohmmètre alimenté en courant alternatif. On mesure la *conductance* $G$ définie comme l’inverse de la résistance $R$ : $G = 1 / R$. Elle représente l’*aptitude de la portion de solution comprise entre les plaques à conduire le courant électrique*.

La conductance $G$, en Siemens ($\pu{S}$), dépend de la *nature de la solution*, de la *constante de cellule* et de la température. Pour s’en affranchir, on utilise plutôt la conductivité $\sigma$ : $$\sigma = G/K_{\text{cell}}$$

### Dosage par étalonnage

Un dosage par étalonnage consiste à déterminer la concentration d’une espèce chimique en comparant une grandeur physique caractéristique de la solution, à la même grandeur physique mesurée pour des solutions étalon. La détermination de la concentration se fait alors par la lecture sur le graphe de la courbe d’étalonnage.

## Objectif

> L'objectif de cette séance est de vérifier que l'information sur la concentration massique en chlorure de sodium de sérum physologique annoncée sur Wikipedia est correcte.

## Matériel à disposition

- Solution de chlorure de sodium de concentration apportée    
$C_0 = \pu{1e-2 mol.L^-1}$ ;
- Conductimètre ;
- Fiole jaugée de $\pu{50 mL}$ ;
- Burette graduée ;
- Pipette jaugée ;
- Bécher ;
- Eau distillée ;
- Sérum physiologique dilué 20 fois.

## Travail à effectuer

### Résultats expérimentaux

- Conductivité d'une solution de sérum physiologique dilué 20 fois : $\sigma = \ldots$
{{% solution "Résultat expérimental" %}}

$\sigma = \pu{0,971 mS·cm-1}$

{{% /solution %}}


- Conductivités des solutions étalons

<center>

| Solution | $S_0$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
| :----: | :----: | :----: | :----: | :----: | :----: |
**Concentration**<br />($\pu{mol.L-1}$) | $\pu{1,0e-2}$ | $\pu{7,5e-3}$ | $\pu{5,0e-3}$ | $\pu{2,5e-3}$ | $\pu{1,0e-3}$ |
**Conductivité**<br />($\pu{mS.cm-1}$) |   |   |   |   |   |

</center>

{{% solution "Résultats expérimentaux" %}}

<center>

| Solution | $S_0$ | $S_1$ | $S_2$ | $S_3$ | $S_4$ |
| :----: | :----: | :----: | :----: | :----: | :----: |
**Concentration**<br />($\pu{mol.L-1}$) | $\pu{1,0e-2}$ | $\pu{7,5e-3}$ | $\pu{5,0e-3}$ | $\pu{2,5e-3}$ | $\pu{1,0e-3}$ |
**Conductivité**<br />($\pu{mS.cm-1}$) | $\pu{1,264}$ | $\pu{0,948}$ | $\pu{0,632}$ | $\pu{0,316}$ | $\pu{0,126}$ |

</center>

{{% /solution %}}

- L'exploitation des résultats expérimentaux nécessite le téléchargement du logiciel {{< remote "Graphical Analysis" "https://www.vernier.com/product/graphical-analysis-4/" >}}.

### Questions


1. Pourquoi a-t-on dilué la solution de sérum physiologique 20 fois ?
{{% solution "Solution" %}}
La proportionnalité entre la conductivité de la solution et la concentration en chlorure de sodium n'est valable que pour les solutions diluées. Grâce au document 1 on sait qu'il faut s'attendre à une concentration apportée en chlorure de sodium $\ce{NaCl}$ de l'ordre de $\pu{9 g.L-1}$, ce qui n'est pas suffisamment dilué.
{{% /solution %}}

2. Comment a-t-on choisi les valeurs des concentrations molaires des solutions étalons ?
{{% solution "Solution" %}}
**Les valeurs des concentrations des solutions étalons doivent encadrer la concentration recherchée lors du dosage.**   
Le document 1 nous apprend que la concentration en chlorure de sodium $\ce{NaCl}$ est $C_{\text{sérum}} \approx \pu{9 g.L-1} = \pu{1,5e-1 mol.L-1}$. Comme le sérum physiologique a été dilué 20 fois, $C_{\text{expé}} \approx \pu{7,7e-3 mol.L-1}$. Les valeurs choisies conviennent donc bien.
{{% /solution %}}

3. Donner le protocole expérimental permettant de fabriquer chacune des solutions étalons.
{{% solution "Solution" %}}

{{% /solution %}}

4. Mettre en œuvre un raisonnement permettant de vérifier que l'information sur la concentration massique en chlorure de sodium de sérum physiologique annoncée sur Wikipedia est correcte.
{{% solution "Solution" %}}

{{% /solution %}}

## Exploitation des données avec Python

{{% note normal %}}

- Un code Python incomplet se trouve à [cette adresse](https://replit.com/join/nmnrhpqzrn-dlatreyte).
- Un corrigé se trouve à [cette adresse](https://replit.com/join/rufhkoxaau-dlatreyte)

{{% /note %}}

Remplacer les .......... dans le code source de façon à déterminer la concentration en chlorure de sodium dans le sérum physiologique.