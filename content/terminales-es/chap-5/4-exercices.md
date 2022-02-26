---
title: "4 Exercices"
subtitle: "Chapitre 1,4"
author: ""
type: ""
date: 2021-01-07T07:46:48+04:00
draft: false
toc: true
tags: []
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---

## Barrage hydroélectrique

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/76227?docId=0bAKW-L7PPFtQMXJvarGh" >}}

{{% solution "Corrigé" %}}
1. Si on note $P\_f$ la puissance fournie par l’eau au barrage, on a :
$$
    r = \dfrac{P\_u}{P\_f}
$$
On peut donc en déduire que 
$$
    P\_f = \dfrac{P\_u}{r} = \dfrac{\pu{300 MW}}{\pu{0,82}} = \pu{366 MW}
$$
2. Si on note $r$ le rendement global, $r\_e$ le rendement de l'ensemble des autres éléments et $r\_{alt}$ le rendement de l'alternateur, l'énoncé nous dit que ces grandeurs sont reliées par la relation :
$$
    r = r\_e \cdot r\_{alt}
$$
On a donc aussi :
$$
    r\_{alt} = \dfrac{r}{r\_e} = \dfrac{\pu{0,82}}{\pu{0,85}} = \pu{0,96}
$$
Le rendement de l'alternateur vaut 96&nbsp;%.
3. Les pertes électriques proviennent des frottements de l’eau sur la conduite forcée et des frottements dans l’alternateur.
{{% /solution %}}

## Caractéristiques de cellules photovoltaïques

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/76227?docId=pv8ZBlcZGh89DgUIxnIPY" >}}

{{% solution "Corrigé" %}}
1. Pour le capteur 1, graphiquement : $U\_1 = \pu{4,0 V}$ et $I\_1 = \pu{1,3 A}$\
Pour le capteur 2, graphiquement : $U\_2 = \pu{3 V}$ et $I\_2 = \pu{1,7 A}$
2. La puissance délivrée par le capteur 1 est : $P\_1 = U\_1 \cdot I\_1 = \pu{4,0 V} \times \pu{1,3 A} = \pu{5,2 W}$.\
La puissance délivrée par le capteur 2 est : $P\_2 = U\_2 \cdot I\_2 = \pu{3,0 V} \times \pu{1,8 A} = \pu{5,1 W}$.\
On peut considérer que ces 2 capteurs délivrent la même puissance. 
3. Pour le capteur 1 : $I\_{CC1} = \pu{1,6 A}$ et $U\_{CO1} = \pu{4,8 V}$.\
Pour le capteur 2 : $I\_{CC2} = \pu{2,0 A}$ et $U\_{CO2} = \pu{3,4 V}$.
{{% /solution %}}

## Les pérovskites

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/3589526" >}}

{{% solution "Corrigé" %}}
1. Un semi-conducteur est un matériau qui a les caractéristiques électriques d'un isolant, mais pour lequel un apport d’énergie extérieur (photons) peut permettre à des électrons de contribuer au courant électrique, en franchissant le gap d’énergie du matériau. La conductivité électrique d'un semi-conducteur est donc intermédiaire entre celle des métaux et celle des isolants et elle augmente avec la température.
2. Les pérovskites ont un maximum d’absorbance dans la partie visible du spectre électromagnétique (400 nm à 800 nm).
3. L’utilisation commune des pérovskites et du silicium permet de couvrir une bande plus large du spectre électromagnétique (visible et proche IR) et donc d’augmenter le rendement du capteur photovoltaïque.
{{% /solution %}}

## Cellule photovoltaïque du futur

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/3589526" >}}

{{% solution "Corrigé" %}}

1. - UV : $\lambda < \pu{380 nm}$ (la limite inférieure n'apparaît pas clairement selon moi. En fait le domaine des UV s'étend jusqu'à une longueur d'onde de $\pu{10 nm}$).
    - IR : $\pu{25 \mu m} > \lambda > \pu{780 nm}$.

2. - Courbe A : absorption dans l'UV et dans l'IR
    - Courbe B : absorption dans l'IR
    - Courbe C : absorption dans le visible
    
    Une cellule transparente absorbe dans l'UV et l'IR mais pas dans le visible. La courbe A correspond à une telle propriété.

3. a. Soit $P\_f$ la puissance fournie sous forme de rayonnement. Si on note $E$ la puissance surfacique que reçoit la cellule, $P\_f = E \cdot S$ où $S$ est la surface que la cellule présente au rayonnement. On a alors $P\_f = \pu{1000 W.m-2} \times \pu{0,012 m2} = \pu{1,2e1 W}$.

    b. $r = \dfrac{P\_u}{P\_f} = \dfrac{\pu{0,86 W}}{\pu{1,2e1 W}} = \pu{7,2e-2}$ Le rendement de la cellule vaut 7,2%

4. Le rendement d'une cellule conventionnelle est de l'ordre de 20%. Le rendement de cette cellule est donc (au moins) deux fois inférieur.

5. Cette faible valeur du rendement peut être compensée par le fait que ces cellules pourraient être installées sur toutes les surfaces vitrées, vues qu'elles sont transparentes.

{{% /solution %}}

## Caractéristique d’une cellule photovoltaïque

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/76946" >}}

{{% solution "Corrigé" %}}
1. D’après le graphique, $I\_{CC} = \pu{1,7 A}$ et $U\_{CO} = \pu{6,0 V}$.
2. La puissance maximale correspond au sommet de la courbe rose. En utilisant la courbe verte, on en déduit les valeurs maximales de la tension et de l’intensité : $I\_{max} = \pu{1,6 A}$ et $U\_{max} = \pu{5 V}$.
3. La puissance maximale de la cellule est : $P\_{max} = U\_{max} I\_{max}$.\
**A.N.** $P\_{max} = \pu{5 V} \times \pu{1,6 A} = \pu{8,0 W}$.\
C'est donc suffisant pour charger le smartphone qui nécessite $\pu{5 W}$.
4. La puissance absorbée par la cellule photovoltaïque est : $P\_{abs} = E \cdot S$\
**A.N.** $P\_{abs} = \pu{1000 W.m-2} \times \pu{15e-2 m} \times \pu{30e-2 m} = \pu{45 W}$.
5. Le rendement de la cellule est : 
$$
    r = \dfrac{P\_{max}}{P\_{abs}} = \dfrac{\pu{8,0 W}}{\pu{45 W}} = \pu{0,17}
$$
Le rendement vaut 17&nbsp;%.
{{% /solution %}}

<!--
## Pour ou contre le photovoltaïque (Travail audio à rendre)

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/76946" >}}
-->

## Comparaison

- {{< remote "Énoncé" "https://www.lelivrescolaire.fr/page/76775" >}}

{{% solution "Corrigé" %}}
1. $P\_{\text{cellule}} = U\_{max} \cdot I\_{max} = \pu{15,5 V} \times \pu{1,2 A} = \pu{18,6 W}$

2. Soit $N$ le nombre de cellules nécessaires pour que l'installation photovoltaïque soit équivalente à la centrale nucléaire, on a alors
$$
    N = \dfrac{P\_{\text{centrale}}}{P\_{\text{cellule}}} = \dfrac{\pu{900e6 W}}{\pu{18,6 W}} = \pu{48,4e6 cellules}
$$

3. Soit $S$ la surface de cellules nécessaires pour que l'installation photovoltaïque soit équivalente à la centrale nucléaire, on a alors
$$
    S = N \cdot S\_{\text{cellule}} = \pu{48,4e6 cellules} \times \pu{0,200 m2/cellule} = \pu{9,68e6 m2} = \pu{9,68 km2}
$$
{{% /solution %}}
