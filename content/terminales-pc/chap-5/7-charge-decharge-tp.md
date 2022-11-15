---
title: "Étude expérimentale de la charge et de la décharge d'un dipôle $(R,C)$"
subtitle: ""
author: ""
type: ""
date: 2022-11-15T18:42:27+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de la séance est l'étude des différents paramètres qui influent sur le temps caractéristique du dipôle $(R,C)$ lors de la charge ou de la décharge d'un dipôle $(R,C)$.

## Documents

{{% note normal %}}

#### temps caractéristique

- Le **temps caractéristique** (ou **constante de temps**) d’un dipôle $(R,C)$ a pour expression $\tau = RC$.
- Le **temps caractéristique** peut se déterminer comme la *durée au bout de laquelle la tension aux bornes du condensateur est égale à 63 % de sa valeur finale (maximale) lors d'une **charge**,* ou comme la *durée au bout de laquelle la tension aux bornes du condensateur est égale à 37 % de sa valeur initiale lors d'une **décharge**.*
- Le **temps caractéristique** peut aussi se déterminer comme la *durée au bout de laquelle la tangente à l’origine à la courbe de charge (ou de décharge) croise son asymptote horizontale*.

Ces deux manières de déterminer le temps caractéristique sont liées à une **évolution exponentielle** ou de façon équivalente à un comportement défini par une **équation différentielle linéaire à coefficients constants du premier ordre**. Elles peuvent donc être utilisée indifféremment à partir de la courbe d'évolution de l’intensité du courant ou de celle de la tension aux bornes du condensateur.

{{% /note %}}

{{% note normal %}}

#### Tolérance

La valeur de la capacité d’un condensateur est accompagnée de la **tolérance**.  
Si un condensateur est étiqueté « $\pu{1 000 \mu F}$ ± 20% », alors sa capacité réelle est comprise entre $\pu{800 \mu F}$ et $\pu{1200 \mu F}$.

{{% /note %}}

{{% note normal %}}

<img src="/terminales-pc/chap-5/chap-5-7/montage.png" alt="" width="55%" style="float: right;" />

#### Montage expérimental

- Choisir la résistance de valeur $R=\pu{220 \Omega}$ et le condensateur de capacité $C=\pu{1 mF}$.
- Réaliser le montage schématisé ci-contre avec l’interrupteur en position 2.
- Ajouter dans le circuit un voltmètre mesurant $u_C$ et un ampèremètre mesurant $i$.

*Attention, dans le cas d’un condensateur chimique la polarité doit être respectée.*

#### Charge

- Basculer l’interrupteur en position 1 en déclenchant l'acquisition à l'aide du logiciel « Graphical Analysis ».

#### Décharge

- Une fois la charge réalisée, tout en continuant l'acquisition, basculer l’interrupteur en position 2.
{{% /note %}}

## Travail à réaliser

1. Décrire l'évolution de la tension $u_C$ aux bornes du condensateur et de l'intensité $i$ du courant électrique lors de la charge et la décharge du dipôle $(R,C)$.

2. Déterminer la valeur du temps caractéristique $\tau$ pour la charge et la décharge du dipôle $(R,C)$.

3. En déduire la valeur de la capacité $C$ du condensateur et la comparer à celle annoncée.

4. Choisir, parmi les résistances et les condensateurs fournis, la combinaison qui permettra d'obtenir la même évolution pour la tension $u_C$ aux bornes du condensateur et de l'intensité $i$ du courant électrique.  
Réaliser le montage et vérifier l'hypothèse.
