---
title: "Détermination expérimentale d'une énergie de combustion"
subtitle: "Chapitre 5,4"
author: ""
type: ""
date: 2022-02-22T05:15:58+04:00
draft: false
toc: true
tags: ["Énergie de combustion"]
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: false
auto_numbering: true
---

{{% note normal %}}

#### Échanges d'énergie

<div style="float: right; padding-left: 15px;">

| Combustible | Énergie de<br />combustion<br />(en kJ/mol) |
| :----: | :----: |
| Méthane | 800 |
| Méthanol | 636 |
| Éthane | 1438 |
| Éthanol | 1326 |
| Butane | 2691 |
| Butan-1-ol | 2447 |
| Octane | 5200 |
| Acide<br />stéarique | 10800 |

</div>

- L'**énergie de combustion** est l'*énergie libérée lors de la combustion d'une mole d'un combustible*. Ce transfert thermique s'effectue sous forme de **chaleur** (*transfert d'énergie thermique*) $Q$.

- Lorsqu'un corps incompressible (solide ou liquide) reçoit (algébriquement) la chaleur $Q$, sa température $T$ évolue de telle sorte que $$ Q = m\\; c\\; (T_f - T_i)$$
où $m$ est la masse du corps, $c$ sa capacité thermique (calorifique) massique, $T_f$ sa température finale et $T_i$ sa température initiale.    
La capacité thermique massique de l'eau vaut : $c_{\text{eau}} = \pu{4,18 J.g-1.°C-1}$.

- *L'énergie est une grandeur qui se conserve*&nbsp;: toute perte d'énergie par un système est transférée à son environnement.

{{% /note %}}

{{% note normal %}}

#### L'acide stéarique

L'acide stéarique (du grec ancien στέαρ, qui signifie suif) ou acide octadécanoïque (nom officiel) est un acide gras dont la chaîne principale comporte 18 atomes de carbone et aucune liaison covalente double&nbsp;: c'est un acide gras saturé. À température ambiante, il forme un solide blanc. Sa température de fusion est d'environ $\pu{70 °C}$. L'acide stéarique est abondant dans toutes les graisses animales (surtout chez les ruminants) sous la forme de l'ester tristéarate de glycérine (stéarine) ou végétales. Il est d'ailleurs le plus répandu des acides gras saturés après l'acide palmitique et avant l'acide myristique. Il a pour origine le suif. Il sert industriellement à faire des huiles, des **bougies** et des savons.

- Formule chimique semi-développée est&nbsp;: $\ce{CH3-(CH2)_{16}-COOH}$.
- Masse molaire : $M = \pu{284 g.mol-1}$.

{{% /note %}}

<center>
<iframe style="width: 600px; height: 200px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=5281&bg=white"></iframe>
</center>

> **Problématique**
>
> L'objectif de cette séance est de déterminer l'énergie de combustion de l'acide stéarique.

<!--
## Questions préliminaires

1. Comparer l’énergie de combustion des alcanes et des alcools. En déduire quels sont les meilleurs combustibles. Justifier.
{{% solution "Réponse" %}}

En comparant les énergies de combustion de molécules dont la chaîne carbonée est de même longueur (noms formés sur la même racine), on remarque que *l’énergie de combustion des alcanes est plus grande que celle des alcools*. *Les meilleurs combustibles sont donc les alcanes*.

{{% /solution %}}

2. Calculer l’énergie libérée $E_{lib}$ par la combustion de 10&nbsp;g de bougie.
{{% solution "Réponse" %}}



{{% /solution %}}

-->

## Protocole expérimental

> Proposer un protocole expérimental soigneusement détaillé pour répondre à la problématique.

{{% solution "Réponse" %}}

En utilisant le principe de conservation de l'énergie, et dans le cas idéal où il n'y aurait pas de perte thermique, on peut utiliser l'énergie de combustion de la bougie pour chauffer un volume d'eau. On mesure la masse de la bougie avant et après la combustion pour en déduire la quantité de matière d'acide stéarique brûlée. On mesure la différence de température de l'eau et par un calcul, on en déduit l'énergie qui s'est dégagée de la combustion. Le rapport des deux valeurs donne alors l'énergie de combustion en $\pu{J.mol-1}$.

- On mesure la masse initiale de la bougie : $m_{ini} = \pu{14,50 g}$.
- On mesure la température initiale de l’eau : $T_{ini} = \pu{23,0 °C}$.
- On chauffe $\pu{150,0 g}$ d’eau distillée dans une canette en aluminium à l’aide d’une bougie chauffe- plat.
- Le thermomètre est disposé dans l’eau mais pas au fond de la canette afin de ne pas fausser la mesure de la température.
- Après 15 minutes, on mesure la masse de la bougie $m_{finale} = \pu{13,60 g}$.
- On en déduit qu’une masse d’acide stéarique $m_{\text{stéarique}} = \pu{0,90 g}$ a été consommée au cours de la combustion.
- La température vaut alors $θ_{fin} = \pu{47,0 °C}$.
- On peut ainsi connaître la quantité de matière d'acide stéarique qui a été brûlé et grâce à l'élévation de température de l'eau, connaître l'énergie qui a été dégagée.

On cherche d'abord $Q$ gagnée par l'eau, et comme l’énergie reçue par l'eau est égale, aux pertes d'énergie près, à l'énergie de combustion de l’acide stéarique pour la masse de bougie brûlée, on trouve $E_{comb}$ l'énergie de combustion pour une certaine masse de bougie. Il suffit après de trouver l'énergie de combustion de l'acide stéarique $E_{comb,exp} (\text{acide stéarique})$ pour une mole de bougie.     


{{% /solution %}}

<!--
## Exercice : Comparaison de la combustion de 2 carburants (difficile)

{{% note exercise %}}

L’essence (modélisée par l’**octane** $\ce{C8H18}$) et l’**éthanol** ($\ce{C2H6O}$) sont des carburants utilisés dans les moteurs à explosion. Une voiture à essence consommant 6,0&nbsp;L au 100 (soit un volume $V = \pu{6,0 L}$ d’essence pour un parcours de 100&nbsp;km) et rejette une masse $m = \pu{130 g}$ de dioxyde de carbone par kilomètre.    
Vérifions s’il en est de même avec une voiture de motorisation équivalente fonctionnant à l’éthanol (ou bioéthanol).

1. Écrire les équations bilan traduisant la combustion complète de ces deux carburants.
2. Dans certains cas, pourquoi peut-il se former du monoxyde de carbone (gaz toxique) et des fumées noires de carbone&nbsp;? (Cours de 4ème)
3. Calculer la masse $m’$ de dioxyde de carbone produit par kilomètre par une voiture roulant au bioéthanol sachant qu’elle consomme 8,7&nbsp;L au 100. Conclure.

#### Données

- Masse volumique de l'éthanol : $\rho = \pu{0,79 kg.L-1}$.
- Masses molaires : $M(H) = \pu{1,0 g.mol-1}$, $M(C) = \pu{12,0 g.mol-1}$, $M(O) = \pu{16,0 g.mol-1}$.
{{% /note %}}

{{% solution "Réponses" %}}

1. $ \ce{2 C8H18 (g) + 25 O2 (g) -> 18 H2O (g) + 16 CO2 (g)} $     
$ \ce{C2H6O (g) + 3 O2 (g) → 3 H2O (g) + 2 CO2 (g)} $

2. Il peut se former du monoxyde de carbone (gaz toxique) et des fumées noires de carbone lorsque la **combustion est incomplète**, c'est à dire *quand le dioxygène n'est pas présent en quantité suffisante*.

3. Cette voiture consomme 8,7&nbsp;L pour 100&nbsp;km, soit $V = \pu{8,7e-2 L}$ pour 1&nbsp;km.     
Comme $$m(\text{éthanol}) = \rho(\text{éthanol})\\, V(\text{éthanol})$$ et $$m(\text{éthanol}) = n(\text{éthanol}) M(\text{éthanol})$$ alors $$ n(\text{éthanol}) M(\text{éthanol}) = \rho(\text{éthanol})\\, V(\text{éthanol})$$ ou $$n(\text{éthanol}) = \dfrac{\rho(\text{éthanol})\\, V(\text{éthanol})}{M(\text{éthanol})}$$

    **A.N.** $n(\text{éthanol}) = \dfrac{\pu{0,79e3 g.L-1} \times \pu{8,7e-2 L}}{\pu{46,0 g.mol-1}} = \pu{1,5 mol}$     
    La voiture consomme $\pu{1,5 mol}$ d'éthanol par kilomètre.

    L'équation de la réaction nous apprend que la combustion d'une mole d'éthanol conduit à la formation de deux moles de dioxyde de carbone. On a donc $$ n(\ce{CO2})\_{\text{produit}} = 2\\; n(\text{éthanol})\_{\text{consommé}}$$    
    
    **A.N.** $ n(\ce{CO2})\_{\text{produit}} = 2 \times \pu{1,5 mol} = \pu{3,0 mol}$       
    La voiture produit $\pu{3,0 mol}$ de dioxyde de carbone par kilomètre.

    $m(\ce{CO2})\_{\text{produit}} = n(\ce{CO2})\_{\text{produit}} M(\ce{CO2})$ donc $m(\ce{CO2})\_{\text{produit}} = \pu{3,0 mol} \times \pu{44,0 g.mol-1} = \pu{1,3e2 g}$     
    La voiture qui fonctionne à l'éthanol produit environ 130&nbsp;g de dioxyde de carbone par kilomètre, soit environ la même masse qu'une voiture qui utilise de l'essence.

{{% /solution %}}
-->
