---
title: "Réactions chimiques d’ordre 1"
subtitle: "Chapitre 7,5"
author: ""
type: ""
date: 2020-11-16T08:53:57+04:00
draft: false
toc: true
tags: ["Facteurs cinétiques", "Ordre de réaction", "Vitesse de réaction"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Vitesses de réactions et concentrations molaires

On observe **expérimentalement** qu'*en milieu homogène* les vitesses de réactions dépendent :
- d'une part des *concentrations molaires des constituants* ;
- d'autre part de la *température*.
*Ce sont les facteurs cinétiques.*

{{% note warning %}}
On exclut ici toute action **catalytique**.
{{% /note %}}

Si l'on considère, dans un premier temps, la *température constante et uniforme dans le réacteur, la vitesse ne dépend plus que des concentrations molaires*. Cette *dépendance* est a priori *quelconque*, plus ou moins complexe, et peut faire apparaître les concentrations tant des réactifs que des produits. Cependant, dans de nombreux cas la relation revêt une forme assez simple, du type : 

$$ v = k [A_1]^{\alpha_1}[A_2]^{\alpha_2}\ldots$$

*La vitesse est alors proportionnelle à un produit de concentrations molaires, le plus souvent de réactifs, élevée à certaines puissances*. Lorsqu'il en est ainsi, on dit que **la réaction a un ordre**.

{{% note normal %}}
Dans quelques cas particuliers, la concentration d'un produit peut apparaître dans l' expression de la vitesse $v$. La réaction est dite **autocatalytique**.
{{% /note %}}

On définit alors :
- La **constante de vitesse** $k$, coefficient de proportionnalité *strictement indépendant des concentrations des constituants*, mais qui *dépend très sensiblement de la température*. À température constante ce coefficient est donc constant.
- l'**ordre partiel** $\alpha_i$ **rapport au constituant** $A_i$, exposant de la concentration $[A_i]$. La somme des ordres partiels $\sum_i \alpha_i$, est l'**ordre global (ou ordre total) de la réaction**.      
Un ordre (partiel ou global) est dans le cas général un rationnel : il peut être nul, positif ou négatif, entier ou fractionnaire. La plupart du temps un ordre est entier ou demi-entier.

## Évolution de la réaction d'un réactif lors d'une réaction chimique d'ordre 1

{{% note normal %}}
De façon générale, les **réactions d'ordre 1** appartiennent aux *réactions de décomposition (d'un réactif chimique ou nucléaire), aux réactions entre un réactif et le solvant*, etc.
{{% /note %}}

### Schéma général 

{{% note warning %}}
**Cette partie n'est pas explicitement au programme !!!** Seule sa conclusion (l'allure de la courbe) l'est. Elle n'est présente dans ce cours qu'afin de vous aider à comprendre l'origine de ce comportement.
{{% /note %}}

Pour introduire l'évolution de la concentration d'un réactif lors d'une réaction d'ordre 1, on va considérer la décomposition d'une entité $A$ dans une solution homogène de volume $V$, selon l'équation :
$$ A \longrightarrow B + C $$

Le tableau d'avancement est alors :
<center>

| État | Avancement | $A$ | $B$ | $C$ |
| :---: | :---: | :---: | :---: | :---: |
| Initial $t=0$ | 0 | $n_0$ | 0 | 0 |
| Quelconque $t$ | $x(t)$ | $n_0 - x(t)$ | $x(t)$ | $x(t)$ |

</center>

{{% note tip %}}
La *vitesse volumique de disparition d'un réactif* $A$, pour une **réaction chimique d'ordre 1**, a pour expression 
$$ 
    v\_d = k [A] 
$$
où $A$ est le (ou l'un des) réactif(s) de la réaction.    
La vitesse volumique de disparition de ce réactif est donc *proportionnelle à la concentration molaire de l'entité* $A$.
{{% /note %}}


### Évolution de la concentration molaire d'un réactif

1. Écrire les expressions des concentrations molaire en $A$ dans la solution dans l'état initial et dans un état quelconque.
{{% solution "Réponse" %}}
- $[A]\_0 = \dfrac{n_0}{V}$ ;
- $[A] (t) = \dfrac{n_0 - x(t)}{V}$.
{{% /solution %}}

<!--
2. Donner l'expression de la vitesse volumique de réaction en fonction de l'avancement de la réaction.
{{% solution "Réponse" %}}
- $v = \dfrac{1}{V}\\, \dfrac{\mathrm{d} x}{\mathrm{dt}}$
{{% /solution %}}
-->

2. Rappeler la définition de la vitesse volumique de disparition du réactif $A$.
{{% solution "Réponse" %}}

$$
    v\_d (A)(t) = - \left( \dfrac{\mathrm{d}[\ce{A}]}{\mathrm{dt}} \right)\_t
$$

{{% /solution %}}

<!--
En déduire l'expression de la vitesse volumique de réaction en fonction de la concentration en réactif $A$.
{{% solution "Réponse" %}}
- Puisque le volume de la solution est constant, $v = \dfrac{\mathrm{d} (x/V)}{\mathrm{dt}}$ ;
- $[A] (t) = \dfrac{n_0 - x(t)}{V} \iff \dfrac{x(t)}{V} = \dfrac{n_0}{V} - [A] (t)$.

Finalement $v = \dfrac{\mathrm{d} (x/V)}{\mathrm{dt}} = \dfrac{\mathrm{d} }{\mathrm{dt}} \left( \dfrac{n_0}{V} - [A] (t)  \right) = - \dfrac{\mathrm{d} [A] }{\mathrm{dt}}$ puisque $\dfrac{n_0}{V}$ est une constante.
$$\boxed{v(t) = - \dfrac{\mathrm{d} [A] }{\mathrm{dt}}}$$
{{% /solution %}}
-->

3. Utiliser le fait que la réaction chimique est d'ordre 1 vis à vis de la concentration en $A$ pour écrire l'équation différentielle donnant l'évolution de la concentration molaire $[A]$ au cours du temps.
{{% solution "Réponse" %}}
- Définition de la vitesse volumique de disparition : $v\_d(t) = - \dfrac{\mathrm{d} [A] }{\mathrm{dt}}$
- Propriété des réactions chimiques d'ordre 1 : $v\_d(t) = k [A]$

Par identification, on peut donc écrire $- \dfrac{\mathrm{d} [A] }{\mathrm{dt}} = k [A]$ ou
$$ \boxed{\dfrac{\mathrm{d} [A] }{\mathrm{dt}} + k [A] = 0}$$
Il s'agit d'une équation différentielle linéaire du premier ordre à coefficients constants sans second membre.
{{% /solution %}}

La famille des solutions de l'équation différentielle est 
$$[A] (t) = D + E e^{(-t/F)}$$
avec $D$, $E$ et $F$ des constantes dont il faut déterminer l'expression.

4. Vérifier à quelle condition la famille de solutions proposée est satisfaisante.
{{% solution "Réponse" %}}
 - $\dfrac{\mathrm{d} [A] }{\mathrm{dt}} = \dfrac{\mathrm{d} }{\mathrm{dt}} \left( D + E e^{(-t/F)} \right) = -\dfrac{E}{F}\\, e^{(-t/F)}$ puisque $D$ est une constante.

 - Par substitution dans l'équation différentielle on obtient :      
 $-\dfrac{E}{F}\\, e^{(-t/F)} + k D + k E e^{(-t/F)} = 0 \iff \left( -\dfrac{1}{F} +  k \right) E e^{(-t/F)} = - kD$. 

 - La relation précédente doit être vraie quelle que soit la date $t$. Le terme à gauche de l'égalité ne peut donc pas dépendre du temps (puisque le terme de droit est constant). On doit avoir $-\dfrac{1}{F} +  k = 0$ ou $\boxed{F = \dfrac{1}{k}}$.

 - Puisque le terme de gauche de l'égalité est toujours nul, le terme de droite doit être nul. On a donc $kD = 0$ soit $\boxed{D = 0}$.

 Finalement, l'ensemble des solutions a pour expression 
 $$ \boxed{ [A] (t) = E e^{-kt}  }$$   
 Il s'agit d'une décroissance exponentielle.
{{% /solution %}}

5. En déduire la dimension du coefficient de proportionnalité $k$.
{{% solution "Réponse" %}}
L'argument de l'exponentielle doit être sans dimension, donc $kt$ est sans dimension. On peut en conclure que $k$ est l'inverse d'un temps.

#### Remarque.
On peut aussi analyser la dimension de $k$ à partir de l'équation différentielle : $\dfrac{\mathrm{d} [A] }{\mathrm{dt}}$ a la dimension d'une concentration sur un temps, $k [A]$ doit donc avoir la dimension d'une concentration sur un temps, ce qui implique que $k$ est l'inverse d'un temps.

#### Remarque.
On peut aussi analyser la dimension de $k$ à partir de la relation $v\_d = k [A]$ : $v\_d$ est une vitesse volumique, soit une concentration sur un temps, $k [A]$ doit donc avoir la dimension d'une concentration sur un temps, ce qui implique que $k$ est l'inverse d'un temps.
{{% /solution %}}

6. À la date $t=0$, la concentration molaire en l'entité $A$ étant égale à $[A]\_0$, donner l'expression de **la solution** pour l'évolution de la concentration molaire de l'entité $A$ au cours du temps.
{{% solution "Réponse" %}}
- À la date $t=0$, $[A] = [A]\_0 = E e^{k\times 0} = E$

Finalement $$ \boxed{ [A] (t) = [A]\_0 e^{-kt}  }$$
{{% /solution %}}

{{% note tip %}}
Pour une réaction chimique d'ordre 1, **la concentration molaire en réactif diminue de façon exponentielle**.
{{% /note %}}

### Temps de demi-réaction

7. Déterminer l'expression du temps de demi-réaction $t_{1/2}$ pour la réaction chimique d'ordre 1.
{{% solution "Réponse" %}}
À partir de la définition de $t_{1/2}$ on peut écrire que $[A] (t_{1/2}) = \dfrac{[A]\_0}{2}$, donc $[A]\_0 e^{-k t_{1/2}} = \dfrac{[A]\_0}{2}$ ou $e^{-k t_{1/2}} = \dfrac{1}{2}$. On en déduit que $-k t_{1/2} = - \ln(2)$ et 
$$\boxed {t_{1/2} = \dfrac{\ln 2}{k}} $$
{{% /solution %}}

{{% note tip %}}
Pour une réaction chimique d'ordre 1, **le temps de demi-réaction est indépendant de la concentration initiale**.
{{% /note %}}

## Application

Le sucre de consommation est principalement constitué de saccharose, une molécule susceptible de se décomposer et de former du glucose et du fructose en quantité équimolaire.

À $\pu{370 K}$, on enregistre la concentration en saccharose $\ce{C12H22O11}$ au cours du temps. Les résultats sont regroupés dans le {{< remote "fichier suivant pour Graphical Analysis" "/terminales-pc/chap-6/chap-6-5-1.ambl">}}

8. Montrer que l'allure de la courbe correspond bien à celle d'une réaction chimique d'ordre 1.

9. Déterminer le temps de demi-réaction. En déduire la valeur de la constante $k$.

<!--
10. À l'aide de l'outil tangente, vérifier que la vitesse volumique de disparition est bien proportionnelle à la concentration en saccharose et calculer à nouveau la valeur de la constante $k$.
-->

10. Tracer la la valeur de la vitesse volumique de disparition en fonction de la concentration en en saccharose. Retrouver que la réaction chimique est d'ordre 1 et calculer à nouveau la valeur de la constante $k$.