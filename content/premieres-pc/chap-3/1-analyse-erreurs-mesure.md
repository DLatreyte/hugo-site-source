---
title: "Incertitudes et analyse des erreurs dans les mesures physiques"
subtitle: "Chapitre 3,1"
author: ""
type: ""
date: 2020-10-01T13:08:44+04:00
draft: false
toc: true
tags: ["Erreurs", "Incertitudes"]
categories: ["Premières Spé PC", "Physique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

La physique est une *science naturelle*. *Les lois qui décrivent et qui 
prédisent le comportement des objets doivent être validées par 
l'expérience* et donc par la publication de résultats de mesures (à partir 
desquelles on peut être amené à effectuer des calculs).

Dans ce document on va se poser les questions suivantes, sans répondre 
complètement à la seconde&nbsp;:
- *Quelle valeur a-t-on réellement mesuré&nbsp;?*
- *Quelle confiance peut-on accorder à cette mesure&nbsp;?*

## Erreur ou incertitude

L'erreur de mesure $E\_{R}$ d'une certaine grandeur est la différence entre 
la valeur mesurée $m$ et la «&nbsp;valeur vraie&nbsp;» $M$.

<figure style="text-align:center;">
<img src="/terminales-pc/chap-0/Chap-00-01-1.png" width="50%" />
</figure>

Si la mesure de la durée de roulement d'une balle sur un plan incliné donne 
$m = \pu{56 s}$ tandis que la durée réelle est $M = \pu{54 s}$, alors l'erreur est de 2&nbsp;s puisque $E\_{R} = | m - M |$. Les scientifiques aimeraient pouvoir déterminer l'erreur 
lors de chaque mesure mais c'est impossible en pratique puisque si on mesure la 
valeur d'une grandeur c'est parce qu'on ignore sa «&nbsp;valeur vraie&nbsp;».

{{% note tip %}}
La «&nbsp;valeur vraie&nbsp;» d'une mesure est une grandeur inaccessible, *l'erreur de 
mesure ne peut jamais être déterminée*. *L'incertitude d'une mesure traduit 
les tentatives scientifiques pour estimer l'importance de l'erreur commise.*
{{%  /note %}}

D'un point de vue scientifique, il aurait donc fallu indiquer que la mesure de 
la durée de roulement de la balle sur le plan incliné a donné (*c'est un exemple !*) $m = \pu{(56 \pm 3) s}$. Un lecteur en aurait donc conclu que 
l'incertitude[^2] vaut $U(m)  = \pu{3 s}$ et que la «&nbsp;valeur vraie&nbsp;» se trouve **probablement**  entre $\pu{53 s}$ et $\pu{59 s}$.

{{% note tip %}}
L'**incertitude** permet de définir un **intervalle** autour de la valeur mesurée. Il existe une certaine *probabilité pour que la «&nbsp;valeur vraie&nbsp;» se trouve dans cet intervalle* .
{{%  /note %}}

{{% note warning %}}
*Lorsqu'on effectue une mesure **on ne détermine pas une valeur mais un 
intervalle de valeurs** auquel on peut associer une certaine **confiance**.*
{{%  /note %}}

{{% note exercise %}}
**Écriture du résultat d'une mesure.**

Un menuisier réalise la mesure de l'encadrement d'une porte $L = \pu{210 cm}$, assurément comprise (selon lui) entre 205 et $\pu{215 cm}$.

1. À quoi est égale l'incertitude de cette mesure&nbsp;?
1. Réécrire le résultat de la mesure en faisant intervenir l'incertitude.
{{% /note %}}

{{% solution "Réponse" %}}
1. $U = | 215 - 210 |\\; \text{cm} = | 205 - 210 |\\; \text{cm} = \pu{5 cm}$.  
Autre calcul possible $U = \frac{| 215 - 205 |\\; \text{cm}}{2} = \pu{5 cm}$.
1. $L = \pu{(210 \pm 5) cm}$
{{% /solution %}}

{{% note exercise %}}
**Écriture du résultat d'une mesure.**

Un étudiant mesure la longueur d'une pendule simple. Il rapporte comme 
meilleure estimation $\pu{110 mm}$ avec un intervalle probable allant de 108 à $\pu{112 mm}$. 
Exprimer ce résultat en faisant intervenir l'incertitude.
{{% /note %}}

{{% solution "Réponse" %}}
$U = \frac{| 108 - 112 |  \text{mm}}{2} = \pu{2 mm}$. Donc le résultat de 
la mesure est $\pu{(110 \pm 2) mm}$.
{{% /solution %}}

{{% note exercise %}}
**Écriture du résultat d'une mesure.**

Une étudiante donne pour mesure d'un courant électrique $I = \pu{(3,05 \pm 0,03) A}$. 

Quel est l'intervalle dans lequel se trouve probablement $I$&nbsp;?
{{% /note %}}

{{% solution "Réponse" %}}
Intervalle&nbsp;: $\lbrack \pu{3,05} - \pu{0,03} = \pu{3,02}\\;&nbsp;; \pu{3,05} + \pu{0,03} = \pu{3,08} \rbrack  \text{A}$.
{{% /solution %}}

{{% note exercise %}}
**Écriture du résultat d'une mesure.**  

Un étudiant analysant le déplacement d'un mobile sur une table à coussin 
d'air, mesure à un instant donné sa position, sa vitesse et son 
accélération. Les résultats sont présentés dans le tableau suivant&nbsp;:

| Variable | Meilleure estimation | Intervalle probable |
|:-:|:-:|:-:|
| Position (cm)&nbsp;: $x$ | 53,3 | 53,1 et 53,5 |
| Vitesse (cm/s)&nbsp;: $v\_{x}$ | - 13,5 | -14,0 et -13,0 |
| Accélération ($\pu{cm/s2}$)&nbsp;: $a\_{x}$ | 93 | 90 et 96 |

Pour chaque variable indiquer l'incertitude de la mesure et réécrire le 
résultat en faisant apparaître cette incertitude.
{{% /note %}}

{{% solution "Réponse" %}}
1. $U(x) = \pu{0,2 cm}$&nbsp;; $U(v\_{x}) = \pu{0,5 cm/s}$&nbsp;; 
$U (a\_{x}) = \pu{3 cm/s2}$.

2. $x = \pu{(53,3 \pm 0,2) cm}$&nbsp;; $v\_{x} = \pu{(- 13,5 \pm 0,5) cm/s}$&nbsp;; $a\_{x} = \pu{(93 \pm 3) cm/s2}$.
{{% /solution %}}

{{% note exercise %}}
**De l'importance de connaître les incertitudes**

Confronté à un problème semblable à celui résolu par Archimède, on 
souhaite déterminer si une couronne est effectivement constituée d'or à 18 
carats ou simplement d'un alliage meilleur marché. Suivant Archimède, nous 
décidons d'en évaluer la densité $\rho$ sachant que celles de l'or à 18 
carats et de l'alliage suspecté sont&nbsp;: $\rho \_{\text{or}} = \pu{15,5 g/cm3}$ et $\rho \_{\text{alliage}} = \pu{13,8 g/cm3}$. La mesure de la densité de la couronne permettrait de décider 
si la couronne est réellement en or par comparaison de $\rho$ avec les 
densités $\rho \_{\text{or}}$ et $\rho \_{\text{alliage}}$. Deux experts de la 
mesure de densité sont appelés. Le premier, Georges, procédant à une rapide 
mesure de $\rho$, déclare que sa meilleure évaluation est $\pu{15 g/cm3}$ certainement située entre 13,5 et $\pu{16,5 g/cm3}$. Le deuxième, Martha, s'accorde plus de temps avant de déclarer que sa meilleure évaluation est $\pu{13,9 g/cm3}$ comprise dans un intervalle probable allant de 13,7 et $\pu{14,1 g/cm3}$.

1. Écrire les deux valeurs données par les experts en faisant intervenir 
   l'incertitude.
1. L'une des deux valeurs est-elle fausse selon vous&nbsp;?
1. L'une des deux valeurs est-elle plus précise que l'autre selon vous&nbsp;?
1. Les deux valeurs sont-elles utilisables&nbsp;?
1. La couronne est-elle en or&nbsp;?
{{% /note %}}

{{% solution "Réponse" %}}
1. Pour Georges, $\rho = \pu{(15,0 \pm 1,5)  g/cm3}$. 
   Pour Martha, $\rho = \pu{(13,9 \pm 0,2) g/cm3}$.
1. <figure>
   <img src="/terminales-pc/chap-0/Chap-00-01-2.png" width="50%" alt="solution" />
   </figure>
   Les deux mesures comprennent au moins une des valeurs attendues, on ne peut donc 
   pas dire qu'elles sont fausses.
1. La mesure de Martha présente une incertitude bien plus petite que celle de 
   Georges. Elle est donc plus précise.
1. La mesure de Georges n'est pas utilisable car elle contient les deux 
   valeurs $\rho \_{\text{or}}$ et $\rho \_{\text{alliage}}$. Il est donc 
   impossible de choisir entre les deux.
1. La couronne n'est manifestement pas en or.
{{% /solution %}}

{{% note tip %}}
On appelle **incertitude relative** le rapport de l'incertitude $U (m)$ sur la 
valeur mesurée $m$&nbsp;:

$$ \frac{U (m)}{m} $$

L'incertitude relative est donc l'incertitude de la mesure $U (m)$ *comparée* 
 à la valeur mesurée $m$.
 {{% /note %}}

{{% note exercise %}}
**Incertitude relative**  

* La largeur d'une feuille de papier peut être mesurée au demi-millimètre 
  près à l'aide d'une règle graduée&nbsp;: $L = \pu{(21,00 \pm 0,05) cm}$
* Le rayon équatorial de la planète Mars n'est connu qu'à cent mètres 
  près&nbsp;: $R = \pu{(3396,2 \pm 0,1) km}$.

Laquelle de ces deux mesures est la plus précise&nbsp;?
{{% /note %}}

{{% solution "Réponse" %}}
$\frac{U (L)}{L} = \frac{0 {,} 05}{21 {,} 00} = 2 \cdot 10^{- 3}$ et $\frac{U 
(R)}{R} = \frac{0 {,} 1}{3396 {,} 2} = 3 \cdot 10^{- 5}$. Plus l'incertitude 
relative est petite, plus précise est la mesure, donc le rayon équatorial de 
Mars est mesuré plus précisément que la largeur de la feuille de papier.
{{% /solution %}}

## La connaissance de l'incertitude permet d'écrire un résultat correctement

{{% note tip %}}
On convient généralement d'écrire l'incertitude $U (m)$ d'une mesure à 
l'aide d'un *seul chiffre significatif*  (*en arrondissant à la valeur 
supérieure* ).
{{% /note %}}

{{% note exercise %}}
1. Les deux résultats de mesure suivants sont-ils différents&nbsp;?
$$ m_{1} = \pu{(12,82 \pm 0,2) s} \text{ et } m_{2} = \pu{(12,8256 \pm 0,2) s} $$
1. Quelle serait l'écriture correcte de ces résultats&nbsp;?
{{% /note %}}

{{% solution "Réponse" %}}
1. L'incertitude de chacune des mesures est $U (m) = \pu{0,2 s}$. Cela 
signifie qu'il est probable que la «&nbsp;valeur vraie&nbsp;» soit comprise dans un 
intervalle de demi-largeur $\pu{0,2 s}$ autour de la valeur mesurée. La méthode 
utilisée pour déterminer l'incertitude n'a pas permis d'être plus précis 
(par exemple, $\pu{0,1 s}$ ou $\pu{0,02 s}$). *On ne peut pas accorder la moindre confiance à des chiffres indiquant les 1/100 de seconde, les 1/1000*. Les deux 
résultats sont donc identiques et *mal écrits* .

2. $m = \pu{(12,8 \pm 0,2) s}$.
{{% /solution %}}

{{% note warning %}}
Lorsqu'on écrit le résultat d'une mesure, les derniers chiffres 
significatifs utilisés sont ceux qui portent l'incertitude.
{{% /note %}}

**Exemple&nbsp;:** Si la mesure d'une résistance donne&nbsp;: $r = \pu{100,25 \Omega}$ et que le 
calcul de l'incertitude donne&nbsp;: $U (r) = \pu{0,812 \Omega}$, on écrit alors $r 
= \pu{(100,3 \pm 0,9) \Omega}$.

{{% note exercise %}}
 **Écriture d'un résultat**

Écrire les mesures suivantes sous une forme correcte avec le nombre 
convenable de chiffres significatifs&nbsp;:

1. $v = \pu{(8,123456 \pm 0,0312) m/s}$&nbsp;;
1. $x = \pu{(3,1234e4 \pm 2) m}$&nbsp;;
1. $m = \pu{(5,6789e-7 \pm 3e{-9}) kg}$.
{{% /note %}}

{{% solution "Réponse" %}}
$v = \pu{(8,12 \pm 0,04) m/s}$&nbsp;;
$x = \pu{(31234 \pm 2) m}$&nbsp;;
$m = \pu{(5,68 \pm 0,03)\cdot 10^{- 7} kg}$.
{{% /solution %}}

{{% note exercise %}}
**Écriture d'un résultat**  

Écrire les mesures suivantes sous une forme correcte avec le nombre 
convenable de chiffres significatifs&nbsp;:

1. Hauteur$= \pu{(5,03 \pm 0,04320) m}$.
1. Temps$= \pu{(1,5432 \pm 1) s}$.
1. Charge$= \pu{(-3,21e-19 \pm 2,67e-20) C}$.
1. Longueur d'onde$= \pu{(0,000000563 \pm 0,00000007) m}$.
{{% /note %}}

{{% solution "Réponse" %}}
1. $\text{Hauteur} = \pu{(5,03 \pm 0,05) m}$.
1. $\text{Temps} = \pu{(2 \pm 1) s}$.
1. $\text{Charge} = \pu{(-3,3 \pm 0,3) \cdot 10^{- 19} C}$.
1. $\text{Longueur d'onde} = \pu{(5,7 \pm 0,7) \cdot 10^{-7} m}$.
{{% /solution %}}

{{% note exercise %}}
**Justesse et fidélité d'un résultat**  

En TP évalué, trois candidats font la même détermination de la 
concentration molaire $c$ d'un acide. Ils proposent les valeurs suivantes&nbsp;:

- Linh $\pu{(24 \pm 3) mmol/L}$&nbsp;;

- Sarah $\pu{12 mmol/L}$&nbsp;;

- Romain $\pu{(19,935 \pm 4) mmol/L}$.

Le correcteur attend la valeur $c = \pu{(20 \pm 2) mmol/L}$. Critiquer le 
résultat de chacun des candidats.
{{% /note %}}

{{% solution "Réponse" %}}
**Linh&nbsp;:** Le résultat de la mesure est bien écrit et il semble fidèle puisque 
l'incertitude est assez petite (la plus petite des trois). Par contre, on ne 
peut pas vraiment considérer ce résultat juste car il ne contient pas la 
valeur attendue (*Rappel&nbsp;:* le résultat d'une mesure est un intervalle).

**Sarah&nbsp;:** La valeur n'est ni bien écrite ni juste car très éloignée de la 
valeur attendue. En fait, on ne peut pas dire grand chose tellement cette 
écriture est mauvaise.

**Romain&nbsp;:** La valeur est mal écrite, Romain aurait du écrire $\pu{(20 \pm 4) mmol/L}$. Par contre elle est juste puisqu'elle englobe la valeur attendue (l'intervalle attendu pour être plus précis). Pour finir, cette mesure n'est pas fidèle car l'incertitude est trop grande.
{{% /solution %}}

## En résumé

{{% note tip %}}
* *Le résultat d'une mesure n'est **pas une valeur mais un intervalle**  de 
  valeurs dans lequel on peut considérer, **avec une certaine confiance** , 
  que la «&nbsp;valeur vraie&nbsp;» se trouve* .
* *Un résultat de mesure est **juste**  si l'intervalle définit à l'aide de 
  la valeur mesurée et de l'incertitude contient la valeur attendue.*
* *Un résultat de mesure est **fidèle**  si l'incertitude n'est pas trop 
  grande*.
{{% /note %}}


[^1]: Le $\pm \pu{3 s}$ est juste un exemple.
[^2]: Notée $U$ pour «&nbsp;Uncertainty&nbsp;».

