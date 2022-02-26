---
title: "Électrocinétique"
subtitle: "Chapitre 6,1"
author: ""
type: ""
date: 2020-10-30T20:15:15+04:00
draft: false
toc: true
tags: ["Courant électrique", "Tension", "Potentiel électrique", "Générateur", "Dipôle", "Branche", "Maille", "Nœud", "Loi des nœuds", "Loi des mailles", "Loi d'Ohm", "Résistance"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

L'**électrocinétique** est l'*étude de la circulation des courants électriques dans des dispositifs reliés à une alimentation électrique*&nbsp;: l'étude de l'installation électrique d'une maison ou d'un appartement est typiquement un problème d'électrocinétique. Dans le domaine de l'électrocinétique, les circuits sont en général composés d'éléments simples&nbsp;: un gén*érateur, des *résistances*, des *inductances* et des *capacités*. On peut également y trouver des transformateurs et d'autres machines électriques. *L'essentiel consiste, finalement, à distribuer une certaine **puissance électrique venant de l'alimentation aux différents éléments du circuit**.*

> L'objectif de ce document est de rappeler les différentes notions de bases, vues dans les classes antérieures.

## Courant électrique

### Qu'est que le courant électrique&nbsp;?

1. Qu'appelle-t-on **courant électrique**&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Un courant électrique est un **mouvement d'ensemble** (ordonné) de *charges électriques*.
{{% /note %}}
{{% /solution %}}

2. Indiquer quelles sont les charges électriques qui se déplacent dans les différents milieux considérés&nbsp;:
    1. dans un conducteur solide&nbsp;;
    2. dans un isolant&nbsp;; 
    3. dans une solution électrolytique&nbsp;; 
    4. dans un plasma.
{{% solution "Réponse" %}}
{{% note tip %}}
1. Les seules charges libres de se déplacer dans les **solides conducteurs** sont les **électrons**.
2. *Aucune charge ne peut se déplacer dans un isolant*. Aucun courant électrique ne circule donc dans les isolants.
3. Les charges capables de se déplacer dans une **solution** électrolytique sont les **ions** (cations et anions). *Il n'existe pas d'électrons libres dans les solutions.*
4. Un plasma (étoile, lampes fluorescentes, etc.) sont des gaz dans lesquels on a séparé, à l'aide d'un champ électrique, les électrons des noyaux. Ces édifices, séparées, peuvent donc se déplacer (dans des sens opposés).
{{% /note %}}
{{% /solution %}}

3. Au déplacement de quel type de charges correspond le **sens conventionnel du courant électrique**&nbsp;?
{{% solution "Réponse" %}}
Le sens conventionnel du courant électrique a été choisi par Benjamin Franklin à une époque où la constitution de la matière n'était pas connue.
{{% note tip %}}
Le sens du déplacement du courant électrique est le sens de déplacement des charges positives.
{{% /note %}}
{{% /solution %}}

4. Quel est le **sens conventionnel** du courant électrique&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
*À l'extérieur du générateur, le courant électrique circule de la borne positive jusqu'à la borne négative de ce générateur.*
{{% /note %}}
{{% /solution %}}

### Qu'est-ce que l'intensité du courant électrique&nbsp;?

5. Qu'appelle-t-on **intensité du courant électrique**&nbsp;?
<img src="/terminales-pc/chap-5/chap-5-1-1.png" alt="" width="40%">
{{% solution "Réponse" %}}
{{% note tip %}}
- L'**intensité du courant électrique** est **la charge électrique qui traverse une section $S$ du circuit chaque seconde**.
- L'**intensité du courant électrique** est le **débit de charges électriques** à travers une section $S$ du circuit électrique.
{{% /note %}}
{{% /solution %}}

6. À partir de la définition de l'intensité du courant électrique établir l'expression de l'**intensité moyenne** $I_{\text{moy}}$ si une charge $\Delta q$ traverse une section $S$ du circuit pendant une durée $\Delta t$.
{{% solution "Réponse" %}}
- Pendant la durée $\Delta t$, située entre les dates $t$ et $t+\Delta t$, le nombre de charges électriques $q$ qui traversent la section $S$ du conducteur est égal à $\Delta n = n(t + \Delta t) - n(t)$. 
- La charge électrique qui traverse la section $S$ du conducteur est donc égale à $\Delta q = q\cdot \Delta n = q(t+\Delta t) - q(t)$.
{{% note tip %}}
$$ I_{\text{moy}} = \dfrac{q(t+\Delta t) - q(t)}{\Delta t}  = \dfrac{\Delta q}{\Delta t} $$
{{% /note %}}
{{% /solution %}}

Si le courant est indépendant du temps (**courant continu**), $I = I_{\text{moy}}$.

7. Quelle est l'unité de l'intensité du courant électrique&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
$I$ s'exprime en ampère. $$ \pu{1 A} = \pu{1 C.s-1} $$
{{% /note %}}
{{% /solution %}}

8. Comment et avec quel instrument mesure-t-on l'intensité du courant électrique&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
- Pour mesurer l'intensité du courant électrique on utilise un **ampèremètre**.
- L'appareil doit être traversé par le courant électrique pour pouvoir mesurer l'intensité du courant électrique.   
Il doit donc être **placé en série dans la branche** dans laquelle on souhaite mesurer l'intensité du courant électrique.
{{% /note %}}
{{% /solution %}}

> Quelques ordres de grandeurs

<center>

| Courant | Composants ou appareils |
| :---: | :---: |
| 10 mA | DEL commune | 
| 100 mA | Risque d’électrocution |
| 0.5 A | Ampoule à incandescence sous 230 V |
| 10 A | Four/Chauffage/Chauffe-eau sous 230 V |
| 100 A | Démarreur automobile |
| 10 kA–100 kA | Foudre |

</center>

9. *En général l'intensité du courant électrique varie avec le temps.* À partir de l'expression de l'intensité moyenne du courant électrique établir l'expression de l'**intensité instantanée** $i(t)$.
{{% solution "Réponse" %}}
{{% note tip %}}
**Idée&nbsp;:** En physique, lorsqu'on introduit une nouvelle grandeur, on réfléchit toujours à partir d'une variation moyenne, sur une durée finie $\Delta t$. Par la suite, lorsqu'on souhaite décrire des variations sur des intervalles de temps plus petits, on passe à la limite (c'est à dire que l'*on observe la variation de la grandeur sur un intervalle de temps infiniment petit mais non nul*).

$$ i(t) = \lim_{\Delta t \to 0} \left( \dfrac{q(t+\Delta t) - q(t)}{\Delta t}  \right) = \dfrac{\mathrm{d}q}{\mathrm{dt}} = q\rq(t)$$

L'intensité instantanée est la **dérivée par rapport au temps** de la fonction $t \longmapsto q(t)$.
{{% /note %}}
{{% /solution %}}

{{% note exercise %}}
#### Exercice 1

Un courant électrique continu d'intensité $I = \pu{0,50 A}$ circule dans un circuit électrique. 
1. Quelle charge électrique traverse une section $S$ quelconque du circuit en une minute&nbsp;?
2. Combien d'électrons traversent une section $S$ quelconque de ce circuit chaque minute&nbsp;?
{{% /note %}}
{{% solution "Réponses" %}}
1. $I = \dfrac{\Delta q}{\Delta t} \iff \boxed{ \Delta q = I \\, \Delta t }$.  
**A.N.** $\Delta q = \pu{0,50 A} \times \pu{60 s} = \pu{0,50 C.s-1} \times \pu{60 s} = \pu{30 C}$.

2. Chaque électron porte la charge électrique $e$ (en valeur absolue), donc $\Delta q = n\\, e$ où $n$ est le nombre d'électrons qui traversent la section $S$. Finalement $\boxed{ n =\dfrac{\Delta q}{e} }$.  
**A.N.** $n =\dfrac{\pu{30 C}}{\pu{1,6e-19 C}} = \pu{1,9e20}$.
{{% /solution %}}


## Qu'est-ce qui donne naissance à un courant électrique&nbsp;?

### Rôle d'un générateur, potentiel électrique

10. Quel est le rôle d'un générateur au sein d'un circuit électrique&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Un générateur (pile, alternateur, etc.) a pour rôle d'**entretenir une différence de potentiel électrique (exprimé en volt) entre ses bornes**.  
{{% /note %}} 
- La borne notée $\oplus$ est le point du circuit où le potentiel électrique est maximal.   
- La borne notée $\ominus$ est le point du circuit où le potentiel électrique est minimal.
{{% /solution %}}

**Remarque&nbsp;:** Nous étudierons en détail le fonctionnement des piles plus tard dans l'année.

11. Sachant qu'une *charge électrique* $q$ *située en un point où le potentiel électrique est* $V$ *possède l'énergie potentielle électrique* $E_{Pel} = qV$, décrire le rôle d'un générateur d'un point de vue énergétique.

{{% solution "Réponse" %}}
- L'énergie potentielle électrique des charges est plus grande au niveau de la borne $\oplus$ qu'au niveau de la borne $\ominus$.
- Nous verrons bientôt que l'*intensité du courant électrique (c'est à dire le débit des charges électriques) reste constante lorsque le courant circule dans le circuit*.

$\implies$ La diminution (en valeur absolue) de l'énergie potentielle des charges électriques est transférée aux éléments du circuit électrique.
{{% note tip %}}
Un générateur fournit de l'énergie (d'origine chimique, mécanique, etc.) au circuit électrique auquel il est connecté.
{{% /note %}}
{{% /solution %}}

12. On utilise souvent une {{< remote "analogie hydroélectrique" "https://en.wikipedia.org/wiki/Hydraulic_analogy" >}} (en fait, il en existe plusieurs) pour expliquer aux élèves ce qu'est le potentiel électrique. La figure suivante illustre cette analogie. 
<img src="/terminales-pc/chap-5/chap-5-1-2.png" alt="" width="50%">
Indiquer quel est le rôle de la pompe et essayer de trouver la grandeur physique qui joue un rôle équivalent au potentiel électrique.
{{% solution "Réponse" %}}
- La pompe remonte l'eau au niveau d'altitude $h$. À cette altitude l'eau possède l'énergie potentielle de pesanteur $E_{PP} = mgh$.
- La grandeur physique analogue au potentiel électrostatique est donc l'altitude $h$ (en fait, c'est plutôt le produit $gh$)&nbsp;: *lorsque l'eau s'écoule, son énergie potentielle de pesanteur diminue, tout comme l'énergie potentielle électrique du courant diminue lorsqu'il circule*.
{{% /solution %}}


{{% note warning %}}
Fondamentalement, une analogie est possible si deux phénomènes *sont liés par des lois de conservations similaires*. Il faut cependant se méfier&nbsp;: une analogie peut être utiles pour expliquer/décrire certains phénomènes d'un domaine (ici ce que représente le potentiel électrique) mais cela ne signifie pas qu'elle décrit correctement tous les phénomènes de ce domaine.
{{% /note %}}

### Tension électrique

12. Qu'appelle-t-on **tension électrique** entre deux points $A$ et $B$ d'un circuit électrique&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
La tension électrique entre deux points A et B correspond à la différence de potentiel électrique entre ces points. On la note
$$U_{AB} = V_A - V_B$$
et elle s’exprime en Volts ($\pu{V}$).
{{% /note %}}
{{% /solution %}}

13. Comment et avec quel instrument mesure-t-on la tension électrique entre deux points d'un circuit&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
- Pour mesurer l'intensité la tension électrique entre deux points d'un circuit on utilise un **voltmètre**.
- L'appareil doit être **placé en dérivation**.
{{% /note %}}
{{% /solution %}}


> Quelques ordres de grandeurs

<center>

| Tension | Provenance | 
| :---: | :---: |
| 230 V | EDF (délivrée) |
| plusieurs kV | Industrielle |
| 225 kV à 400 kV | Lignes haute tension |
| quelques V | Piles |

</center>

**Remarque.** Une tension électrique n’est pas en soi {{< remote "dangereuse pour la santé" "https://youtu.be/Zi4kXgDBFhw" >}}, ce qui peut faire l’objet de {{< remote "spectacles impressionnants" "https://youtu.be/3FpjcOWwiI4" >}}. **Le fait d’être à un certain potentiel n’est donc pas forcément dangereux**. *Toutefois, une différence de potentiel induit un courant électrique, qui lui peut être dangereux*.

14. Quelle relation lie les tensions électriques $U_{AB}$ et $U_{BA}$&nbsp;? Quelle propriété importante peut-on en déduire&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
$$U_{AB} = V_A - V_B = -(V_B - V_A) = -U_{BA} $$

La tension électrique est une **grandeur algébrique**.
{{% /note %}}
{{% /solution %}}

15. Comment représente-t-on la tension $U_{AB}$ entre les points $A$ et $B$&nbsp;?
{{% solution "Réponse" %}}
On utilise une représentation vectorielle.
<img src="/terminales-pc/chap-5/chap-5-1-3.png" alt="" width="35%">
{{% /solution %}}



## Énergie et puissance

{{% note normal %}}
Un courant électrique transporte de l'énergie du générateur jusqu'aux différents composants du circuit.
{{% /note %}}

{{% note exercise %}}
#### Exercice 2
On suppose qu'une petite quantité de charge électrique $\Delta q$ traverse l'élément de circuit pendant $\Delta t$ secondes et subit une chute de potentiel.

1. Déterminer l'expression de la variation d'énergie potentielle de la quantité de charges $\Delta q$.
2. Cette énergie potentielle est cédée à l'élément de circuit. Donner l'expression $\Delta E$ de la variation d'énergie de l'élément de circuit lorsque la charge $\Delta q$ le traverse.
3. En déduire l'expression $P$ de la puissance électrique reçue par l'élément de circuit.
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-13.png" alt="" width="60%">
    

{{% solution "Réponse" %}}
1. $\Delta E_{Pel} = \Delta q\\, (V_B - V_A) = - \Delta q\\, U_{AB}$.
2. $\Delta E = -\Delta E_{Pel} = \Delta q\\, U_{AB}$.
3. $P = \dfrac{\Delta E}{\Delta t} = \dfrac{\Delta q\\, U_{AB}}{\Delta t} = \dfrac{\Delta q}{\Delta t}\\, U_{AB}$.   
Comme $\dfrac{\Delta q}{\Delta t} = I_{AB}$, $P = I_{AB}\\, U_{AB}$.
{{% /solution %}}

{{% note tip %}}
- La puissance électrique reçue par un élément de circuit a pour expression $$P = I_{AB}\\, U_{AB}$$
- On appelle **convention récepteur** la configuration où les *flèches courant et tension sont de sens opposés*.  
En convention récepteur, *si $P > 0$, l'énergie est effectivement reçue par l'élément de circuit*.
{{% /note %}}

## Éléments d'un circuit

### Vocabulaire

16. Qu'est-ce qu'un **dipôle électrique**&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Un dipôle électrique est un *composant électrique possédant deux bornes*.
{{% /note %}}
Les ampoules, les interrupteurs, les générateurs, les piles, les condensateurs, les inductances, les diodes, les DEL, les résistances et les moteurs sont des dipôles.
{{% /solution %}}

17. Qu'est-ce qu'un **nœud**&nbsp;? 
{{% solution "Réponse" %}}
{{% note tip %}}
Un **nœud** est un *point du circuit auquel sont connectés au moins trois fils*.
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-6.png" alt="" width="25%">
{{% /solution %}}

18. Qu'est-ce qu'une **branche**&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Une **branche** est une *portion de circuit située entre deux nœuds parcourue par le même courant électrique*.
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-5.png" alt="" width="50%">
{{% /solution %}}

19. Qu'est-ce qu'une **maille**&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Une **maille** est une *portion fermée de circuit* (ensemble de branches qui partent et finissent au même nœud. 
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-4.png" alt="" width="50%">
**Remarque. ** Les circuits, hors circuits très simples, sont généralement constitués de plusieurs mailles.
{{% /solution %}}

{{% note exercise %}}
#### Exercice 3
Pour le circuit suivant&nbsp;:
<img src="/terminales-pc/chap-5/chap-5-1-7.png" alt="" width="50%">

1. Compter le nombre de dipôles.
2. Compter le nombre de nœuds.
3. Compter le nombre de branches.
4. Combien de mailles peut-on former&nbsp;?
{{% /note %}}

{{% solution "Réponses" %}}
1. 4 dipôles.
2. 2 nœuds.
3. 3 branches.
4. On peut former 3 mailles.
{{% /solution %}}

### Association d'éléments de circuits

20. Qu'appelle-t-on **association série** de deux dipôles&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
- Deux dipôles *sur une même branches* sont **en série**.
- *Ces deux dipôles sont parcourus par le même courant*.
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-8.png" alt="" width="50%">
{{% /solution %}}

21. Qu'appelle-t-on **association parallèle** (ou **en dérivation**) de deux dipôles&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
- Deux dipôles *reliés à deux mêmes nœuds* sont en **parallèle** (ou **en dérivation**).
- *Ces deux dipôles sont soumis à la même tension électrique*.
{{% /note %}}
<img src="/terminales-pc/chap-5/chap-5-1-9.png" alt="" width="50%">
{{% /solution %}}


## Loi d'Ohm, résistance

22. Rappeler ce qu'est la **caractéristique d'un dipôle** et préciser ce que l'on appelle **résistance électrique**.
{{% solution "Réponse" %}}
{{% note tip %}}
On appelle **caractéristique d'un dipôle** la relation $i = f(U)$ *entre l'intensité du courant électrique qui le traverse et la tension électrique à ses bornes*.  
{{% /note %}}

- La plupart du temps la caractéristique ne peut être donnée que sous la forme d'une courbe.
- La caractéristique d'une résistance est&nbsp;:
<img src="/terminales-pc/chap-5/chap-5-1-10.png" alt="" width="70%">
{{% /solution %}}


23. Déduire de la forme de la caractéristique d'une résistance la loi d'Ohm.
{{% solution "Réponse" %}}
{{% note tip %}}
On appelle **caractéristique d'un dipôle** la relation $i = f(U)$ *entre l'intensité du La loi d'Ohm est la traduction mathématique de la caractéristique d'une résistance électrique&nbsp;:
$$U_{AB} = R I_{AB} $$
La chute de potentiel aux bornes d'une résistance est proportionnelle à l'intensité du courant électrique qui la traverse.
{{% /note %}}
- Cette loi est empirique et n'est valable que pour des intensités électrique raisonnables.
- La loi d'Ohm reste valable lorsque le courant est variable dans le temps.
{{% /solution %}}

{{% note warning %}}
*Tous les composants électriques, notamment les câbles, présentent une certaine résistance à l'écoulement du courant électrique*. On réserve cependant le terme résistance à des composants spécifiques et **on considère que la résistance d'un câble est nulle**.
{{% /note %}}

24. Puisqu'on considère que la **résistance d'un câble électrique est nulle**, donner la valeur de la tension électrique entre deux points d'un même câble.
{{% solution "Réponse" %}}
Puisque $R = \pu{0 \Omega}$, $U = RI = 0$.
{{% note tip %}}
**Il n'existe aucune chute de potentiel électrique le long d'un fil électrique.**
{{% /note %}}
{{% /solution %}}

25. Donner l'expression de la puissance électrique qu'un courant électrique cède à une résistance $R$. Cet effet s'appelle l'**effet Joule**.
{{% solution "Réponse" %}}
$P=U_{AB}I_{AB}$ avec $U_{AB}=RI_{AB}$, donc $P=R I_{AB}^2 = \dfrac{U_{AB}^2}{R}$.
{{% note tip %}}
La puissance Joule cédée par un courant électrique à une résistance a pour expression 
$$P=R I_{AB}^2 = \dfrac{U_{AB}^2}{R}$$
{{% /note %}}
{{% /solution %}}

## Lois de Kirchhoff

En classe de terminale, les courants seront soit continus (constant dans le temps) soit lentement variables. Il ne sera donc pas nécessaire de prendre en compte les temps de propagations des ondes qui seront considérés nulls.

{{% note tip %}}
L'intensité du courant électrique est identique en tout point d'une même branche.
{{% /note %}}

### Loi des nœuds

26. La charge électrique est une grandeur qui se conserve. Il ne peut donc y avoir accumulation de charges au niveau d'un nœud. Donner la relation entre les différents courants pour le nœud considéré et en déduire la loi des nœuds.
<img src="/terminales-pc/chap-5/chap-5-1-11.png" alt="" width="35%">
{{% solution "Réponse" %}}
$I_1 + I_4 + I_6 = I_2 + I_3 + I_5$

{{% note tip %}}
La somme des intensités de tous les courants électriques qui arrivent à un nœud est égale à la somme des intensités de tous les courants qui le quittent.
{{% /note %}}
{{% /solution %}}

### Loi des mailles

27. Soit la maille ci-après. Calculer la sommes $U_{12} + U_{41} + U_{34} + U_{23} $ (les $V_i$ sont les potentiels électriques aux différents nœuds) et en déduire la loi des mailles.
<img src="/terminales-pc/chap-5/chap-5-1-12.png" alt="" width="45%">

{{% solution "Réponse" %}}
$U_{12} + U_{41} + U_{34} + U_{23} = V_1 - V_2 + V_4 - V_1 + V_3 - V_4 + V_2 - V_3 = 0$

{{% note tip %}}
- La somme algébrique des variations de potentiel électrique le long d'une maille est nulle.
- La somme algébrique des tensions électriques le long d'une maille est nulle.
{{% /note %}}
{{% /solution %}}

## Exercices

{{% note exercise %}}
#### Exercice 4
<img src="/terminales-pc/chap-5/chap-5-1-14.png" alt="" width="45%" style="float: right; margin-left: 10px;" />

1. Que vaut la tension $U_{AC}$&nbsp;?
2. Montrer que l'on peut remplacer les deux résistances $R_1$ et $R_2$ placées en série par une résistance unique de valeur $R_{eq} = R_1 + R_2$.
3. À partir de la réponse à la question précédente, calculer la valeur de l'intensité $I_{AC}$ du courant électrique qui circule dans la branche $AC$.
4. En déduire la valeur de la tension $U_{AB}$.
5. Même question pour la tension $U_{BC}$.
6. Calculer la puissance reçue par la résistance $R_1$.
7. Calculer la puissance reçue par le résistance $R_2$.
8. Vérifier que la somme des puissances reçues par $R_1$ et $R_2$ est égale à la puissance fournie par le générateur.
{{% /note %}}
{{% solution "Réponses" %}}
{{< remote "Fichier réponse au format pdf" "/terminales-pc/chap-5/chap-5-1-16.pdf" >}}
{{% /solution %}}

{{% note exercise %}}
#### Exercice 5
<img src="/terminales-pc/chap-5/chap-5-1-15.png" alt="" width="65%" style="float: right; margin-left: 10px;" />

1. Que vaut la tension $U_{AC}$&nbsp;?
2. Montrer que l'on peut remplacer les deux résistances $R_2$ et $R_3$ placées en parallèle par une résistance unique telle que $$\dfrac{1}{R_{eq}} = \dfrac{1}{R_2} + \dfrac{1}{R_3}$$   
Calculer la valeur de cette résistance équivalente.
3. À partir de la réponse à la question précédente, calculer la valeur de l'intensité $I_{AC}$ du courant électrique qui circule dans la branche $AC$.
4. En déduire la valeur de la tension $U_{AB}$.
5. Même question pour la tension $U_{BC}$.
{{% /note %}}

{{% solution "Réponses" %}}
{{< remote "Fichier réponse au format pdf" "/terminales-pc/chap-5/chap-5-1-17.pdf" >}}
{{% /solution %}}
