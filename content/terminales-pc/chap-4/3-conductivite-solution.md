---
title: "Conductimétrie"
subtitle: "Chapitre 5,3"
author: ""
type: ""
date: 2020-10-10T21:23:43+04:00
draft: false
toc: true
tags: ["Conductimétrie", "Kohlrausch", "Courant électrique", "Conductance", "Conductivité", "Conductivité molaire ionique"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---
[^1]: En chimie on préfère utiliser la conductance que la résistance.
[^2]: En réalité il faut faire bien plus d'expériences pour déterminer la dépendance exacte de la conductance envers les différentes grandeurs&nbsp;!


## Courant électrique

{{% note tip %}}
On appelle **courant électrique** le *déplacement d'ensemble de charges électriques*. 

- Dans les **solides**, les charges mobiles sont les *électrons*&nbsp;;
- Dans les **solutions ionique**, les charges mobiles sont les *ions*.   
{{% /note %}}

{{% note warning %}}
Les électrons ne peuvent pas se déplacer librement dans les solutions&nbsp;!
{{% /note %}}

{{% note tip %}}
- *À l'extérieur d'un générateur, le courant électrique circule du point de plus haut potentiel électrique (borne $+$ du générateur) vers le point de plus bas potentiel électrique (borne $-$ du générateur)*.
- Cette circulation correspond à la **circulation des charges positives**.
{{% /note %}}

- *Dans un circuit solide, aucune charge positive ne peut se déplacer*. Les **électrons** circulent donc dans le *sens opposé au sens de circulation du courant électrique*.
- *Toute solution ionique est électriquement neutre*&nbsp;: elle contient donc forcément des **cations** et des **anions**.   
Les *cations circulent dans le même sens que le courant électrique* alors que les *anions circulent dans le sens opposé au sens de circulation du courant électrique*.

## Conductance d'une solution ionique

### Résistance et conductance

#### Rappel
Lorsqu'on mesure la **tension électrique** $U$ aux bornes d'un *conducteur ohmique* et l'**intensité** $I$ du courant électrique le traversant, on constante que ces deux grandeurs sont proportionnelles&nbsp;: $U = R\cdot I$.    
$R$ le coefficient de proportionnalité est appelé la ***résistance** électrique* du conducteur ohmique.    
On peut aussi écrire cette relation sous la forme $I = G \cdot U$ où $G = 1/R$ est la **conductance** du conducteur ohmique (**unité :** $\pu{S}$, siemens).

#### En chimie
<img src="/terminales-pc/chap-4/chap-4-3-1.png" alt="" width="45%" />
Deux plaques conductrices reliées à un générateur basse fréquence (**courant alternatif**) et plongées dans une *solution aqueuse diluée* ont un comportement électrique que l'on peut **modéliser** comme étant celui d'un *conducteur ohmique*&nbsp;: *une solution ionique possède une résistance (ou une conductance)[^1].*

### Influence de différents paramètres expérimentaux sur la conductance d'une solution ionique

#### Résultats expérimentaux
- La conductance $G$ d'une portion de solution ionique, de section $S$ et de longueur $L$, diminue quand $S$ diminue ou quand $L$ augmente.
- La conductance d'une solution ionique augmente quand la concentration molaire en soluté chargé apporté croît.
- La conductance d'une solution ionique augmente quand la température croît.
- La conductance d'une solution ionique dépend de la nature des ions présents.

#### Bilan 
Les paramètres modifiés pour parvenir aux différents résultats[^2], dans la section précédente, peuvent être classés en deux catégories&nbsp;:
- ceux qui dépendent de la nature de la solution chimique&nbsp;;
- ceux qui ne dépendent que de la construction de la cellule.

{{% note tip %}}
La conductance $G$ d'une portion de **solution ionique**, de section $S$ et de longueur $L$, peut se mettre sous la forme&nbsp;: $$G = \sigma \cdot \dfrac{S}{L}$$

**Unités :** $G$ en siemens $\pu{S}$, $\sigma$ en siemens par mètre $\pu{S.m-1}$, $S$ en mètre carré $\pu{m2}$, $L$ en mètre $\pu{m}$.
{{% /note %}}

{{% note normal %}}
- Le quotient $\dfrac{S}{L}$ est une caractéristique de la cellule utilisée. Il est généralement déterminé à la construction de la cellule.
- La grandeur $\sigma$ est appelée **conductivité** de la solution, elle dépend *de la nature et de la concentration des ions* présents dans la solution et de la *température*.
{{% /note %}}

## Conductivité d'une solution ionique -- Loi de Kohlrausch

{{% note tip %}}
Dans une *solution ionique diluée*, la conductivité $\sigma$ de la solution est **proportionnelle à la concentration en soluté apporté** $C$.
$$\sigma = \Lambda \\, C$$
où $\Lambda$ est la **conductivité molaire** de la solution.  
**Unité :** $\pu{S.m2.mol-1}$.
{{% /note %}}

## Conductivité molaire ionique

{{% note tip %}}
Dans une *solution ionique diluée* contenant les ions $\ce{M^+}$ et $\ce{X^-}$, dont les concentrations effectives sont notées $[\ce{M^+}]$ et $[\ce{X^-}]$, la conductivité de la solution peut se mettre sous la forme&nbsp:
$$\sigma = \lambda _{M^+} \\, [\ce{M^+}] + \lambda _{X^-} \\, [\ce{X^-}]$$
Les quantités $\lambda _{\ce{M^+}}$ et $\lambda _{\ce{X^-}}$ sont appelées **conductivités molaires ioniques** des ions $\ce{M^+}$ et $\ce{X^-}$.   
**Unité :** $\pu{S.m2.mol-1}$.
{{% /note %}}

**Remarque :** La conductivité molaire ionique d'un ion ne dépend que de la **température** et de la **nature de l'ion**.