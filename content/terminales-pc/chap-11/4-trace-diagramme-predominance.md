---
title: "Tracé d'un diagramme de distribution à l'aide du langage Python"
subtitle: "Chapitre 12,4"
author: ""
type: ""
date: 2021-01-30T21:28:32+04:00
draft: false
toc: true
tags: ["Constante d'équilibre", "pKa", "pH", "Domaine de prédominance"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de ce document est de tracer les diagrammes de prédominance de quelques couples acide/base.

## Cas d'un monoacide (ou d'une monobase)

Données
: - $\text{pK}\_a(\ce{NH4^+/NH3}) = \pu{9,24}$ ;
- $\text{pK}\_a(\ce{CH3CO2H/CH3CO2^-}) = \pu{4,70}$.

On introduit un acide faible à la concentration $C$ dans une solution dont on peut faire varier le pH.

1. Rappeler l'expression de la constante d'acidité $K\_a$ d'un couple $\ce{AH/A-}$.

2. À l'aide d'un tableau d'avancement, déterminer la relation qui existe, quel que soit l'avancement de la transformation, entre les grandeurs $C$, $[\ce{AH}]$ et $[\ce{A-}]$.

3. En déduire une expression de $[\ce{AH}]$ qui ne fait intervenir que les grandeurs $C$, $\text{pH}$ et $\text{pK}\_a$.

4. En déduire l'expression de \%(AH), pourcentage de l'espèce chimique AH dans la solution.

5. Reprendre les questions 3. et 4. pour l'entité $\ce{A-}$.

7. Compléter le code Python à cette {{< remote "adresse" "https://dlatreyte.github.io/jupyter-lite/lab?path=term-spe-pc%2FAcide-Base%2FDiagramme_predominance_eleves.ipynb" >}} de façon à ce que le diagramme de prédominance de l'acide éthanoïque soit tracé.\
Enregistrer l'image générée.

8. Tracer maintenant le diagramme de prédominance de l'ion ammonium.

9. Modifier le programme de façon à ce qu'il affiche à la fois le diagramme de prédominance de l'acide éthanoïque et celui de l'ion ammonium.

## Cas d'un diacide

Données
: - $\text{pK}\_a(\ce{H2CO3/HCO3^-}) = \pu{6,30}$ ;
- $\text{pK}\_a(\ce{HCO3^-/CO3^{2-}}) = \pu{10,33}$.

10. Reprendre l'étude précédente dans le cas de l'acide carbonique (dihydrogénocarbonate).


## Corrigé de la première partie

{{% solution "Corrigé" %}}

{{< remote "Programme" "https://dlatreyte.github.io/jupyter-lite/lab?path=term-spe-pc%2FAcide-Base%2FDiagramme_predominance.ipynb" >}} 

{{% /solution %}}