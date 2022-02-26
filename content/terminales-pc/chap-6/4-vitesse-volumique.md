---
title: "Suivi cinétique et vitesses volumiques de formation et de disparition"
subtitle: "Chapitre 7,4"
author: ""
type: ""
date: 2020-11-14T20:04:29+04:00
draft: false
toc: true
tags: ["Tableau d'avancement", "Vitesse volumique", "Suivi cinétique"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Comment suivre l’évolution au cours du temps d’un système formé d'ions iodure et péroxodisulfate&nbsp;:

{{% note normal %}}
#### Expérience

Dans un bécher on verse $\pu{50 mL}$ d’une solution incolore de péroxodisulfate de potassium $(\ce{2 K^+(aq) + S2O8^{2-}(aq)})$, à $\pu{0,10 mol.L-1}$, puis $\pu{50 mL}$ d’une solution incolore d’iodure de potassium, $(\ce{K^+(aq) + I^-(aq)})$, à $\pu{0,50 mol.L-1}$. On agite pour homogénéiser le mélange et on déclenche un chronomètre.

#### Observation

On note que la solution se colore progressivement en jaune, couleur caractéristique de la présence des molécules $\ce{I2(aq)}$.

#### Interprétation

Les ions peroxodisulfate réagissent lentement avec les ions iodure selon l’équation
$$
\ce{ 2 I^-(aq) + S2O8^{2-}(aq) -> I2(aq) + 2 SO4^{2-}(aq)  }
$$
{{% /note %}}

On utilise un colorimètre et la loi de Beer-Lambert pour déterminer l’évolution de la concentration du diiode formé au cours du temps.

<center>

| **t (min)** | 0 | 2 | 3,5 | 5 | 8 | 10 | 13 | 20 | 25 | 30 | 35 | 40 | 50 | 60 |  
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $[\ce{I2}]$ (mmol/L) | 0,0 | 8,0 | 12,0 | 16,5 | 23,2 | 27,2 | 31,2 | 38,6 | 41,6 | 44,1 | 45 | 46,7 | 48,6 | 49,1 | 

</center>

1. Établir, à l'aide du logiciel Graphical Analysis, le graphique $[\ce{I2}] = f(t)$.

{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-4-1.png" alt="" width="70%" />
{{% /solution %}}

2. Comment varie la vitesse de formation du diiode&nbsp;:

{{% solution "Réponse" %}}
Pour une durée $\Delta t$ donnée, on remarque que la concentration de diiode augmente de moins en moins vite lorsque le temps s'écoule. *La vitesse de formation du diiode est donc de moins en moins grande. Au bout d'une certaine durée elle s'annule même (l'état final de la transformation est atteint).*
{{% /solution %}}

3. Expliquer cette évolution en utilisant un des facteurs cinétiques introduits dans les documents précédents.

{{% solution "Réponse" %}}
La concentration des réactifs est un facteur cinétique. Lorsque le système avance, cette concentration diminue, il est donc normal, **sauf cas particulier**, que la vitesse de formation du diiode diminue progressivement.
{{% /solution %}}

4. Établir le tableau d'avancement de la transformation en fonction du temps.

{{% solution "Réponse" %}}
<center>

| **État** | **Av.** | $\ce{2 I^-(aq)}$ | $\ce{S2O8^{2-}(aq)}$ | $\ce{I2(aq)}$ | $\ce{2 SO4^{2-}(aq)}$ |
| :-:|:-:|:-:|:-:|:-:| :-:|
| Initial $t=0$| 0 | $n_0(\ce{I^-})$ | $n_0(\ce{S2O8^{2-}})$ | $0$ | $0$ |
| Quelconque $t$ | $x(t)$ | $n_0(\ce{I^-}) - 2x(t)$ | $n_0(\ce{S2O8^{2-}}) - x(t)$ | $x(t)$ | $2 x(t)$ |

</center>
{{% /solution %}}

5. La transformation étudiée est-elle totale&nbsp;? Justifier la réponse.

{{% solution "Réponse" %}}
- Si la transformation chimique est totale au moins un des réactifs est limitant et $x_f = x_{\text{max}}$.
- Détermination de l'avancement maximal&nbsp;:
    - $\ce{I^-}$ limitant&nbsp;:    
    $n_0(\ce{I^-}) - 2x_{\text{max}} = 0 \iff x_{\text{max}} = \dfrac{n_0(\ce{I^-})}{2}$.     
    <strong>A.N.</strong> $x_{\text{max}} = \dfrac{ \pu{50e-3 L} \times \pu{0,50 mol.L-1} }{2} = \pu{1,3e-2 mol}$.    
    - $\ce{S2O8^{2-}}$ limitant&nbsp;:    
    $n_0(\ce{S2O8^{2-}}) - x_{\text{max}} = 0 \iff x_{\text{max}} = n_0(\ce{S2O8^{2-}})$.    
    <strong>A.N.</strong> $x_{\text{max}} = \pu{50e-3 L} \times \pu{0,10 mol.L-1} = \pu{5,0e-3 mol}$.
    - Finalement, $x_{\text{max}} = \pu{5,0e-3 mol}$ et $\ce{S2O8^{2-}}$ est le réactif limitant.
- Sur le graphique, on constate que $[\ce{I2}]\_\infty = \pu{5,0e-2 mol.L-1}$. Or $[\ce{I2}]\_\infty = \dfrac{x_{\text{max}}}{V}$ avec $V$ le volume de la solution.    
<strong>A.N.</strong> $[\ce{I2(aq)}]\_\infty = \dfrac{\pu{5,0e-3 mol}}{\pu{50e-3 L} + \pu{50e-3 L}} = \pu{5,0e-2 mol.L-1}$. 

*La transformation chimique est bien totale.*
{{% /solution %}}

6. À partir du tableau d'avancement, écrire les expression des concentrations molaires de toutes les espèces chimiques en fonction de la concentration molaire en diiode.

{{% solution "Réponse" %}}
À chaque instant $t$, $x(t) = V \cdot [\ce{I2}] (t)$, donc&nbsp;:
- $[ \ce{S2O8^{2-}} ] (t) = [\ce{S2O8^{2-}}] _0 - \dfrac{x(t)}{V} = [\ce{S2O8^{2-}}] _0 - \dfrac{[\ce{I2}] \cdot V}{V} $
$$
\boxed{[\ce{S2O8^{2-}}] (t) = [\ce{S2O8^{2-}}] _0 - [\ce{I2}] (t) }
$$
- $[\ce{I^-}] (t) = [\ce{I^-}] _0 - \dfrac{2 x(t)}{V} =  [\ce{I^-}] _0 - \dfrac{2 [\ce{I2}] \cdot V}{V}$    
$$
\boxed{[\ce{I^-}] (t) = [\ce{I^-}] _0 - 2 [\ce{I2}] (t)}
$$ 
- $[\ce{SO4^{2-}}] (t) = \dfrac{2 x(t)}{V} = \dfrac{2 [\ce{I2}] \cdot V}{V}$    
$$
\boxed{[\ce{SO4^{2-}}] (t) = 2 [\ce{I2}] (t)}
$$
{{% /solution %}}

7. Ajouter les différentes fonctions sur le graphique de la question 1.

{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-4-2.png" alt="" width="100%" />
{{% /solution %}}

## Comment évaluer la durée nécessaire à l’achèvement de la transformation chimique étudiée&nbsp;:

### Temps de demi-réaction

{{% note tip %}}
Le **temps de demi-réaction**, noté $t\_{1/2}$, d’une réaction chimique est la *durée nécessaire pour que l’avancement de la réaction parvienne à la moitié de sa valeur finale*.

$$ 
    x (t_{1/2}) = \dfrac{x_f}{2} 
$$
{{% /note %}}

{{% note normal %}}

- Si la transformation chimique est **totale**, 
$$
    x (t_{1/2}) = \dfrac{x_{max}}{2} 
$$

- Si la transformation est **totale**, le temps de demi-réaction est aussi la *durée au bout de laquelle la moitié du réactif limitant a été consommée*.

- Le temps de demi-réaction est la durée au bout de laquelle la moitié de la quantité de matière finale de produit a été produite.

{{% /note %}}

### Le temps de demi-réaction est, en terminale, une valeur essentiellement expérimentale

En classe de terminale, il n'est pas question de résoudre les équations différentielles qui traduisent l'évolution au cours du temps des concentrations. *On détermine donc le temps de demi-réaction à partir de l'expérience*.

{{% note tip %}}
#### Détermination pratique du temps de demi-réaction

1. Tracer la courbe $x = f(t)$. 
2. Déterminer la valeur de l'avancement final.
2. Rechercher sur le graphique la date pour laquelle $x = \dfrac{x_f}{2}$&nbsp;; c'est $t_{1/2}$.
{{% /note %}}

8. Construire, à l'aide du logiciel Graphical Analysis, la courbe $x = f(t)$ et en déduire la valeur du demi-temps de réaction.

{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-4-3.png" alt="" width="100%" />
> $t_{1/2} = \pu{9 min}$
{{% /solution %}}

9. Démontrer que l'on peut, en fait, déterminer la valeur de $t_{1/2}$ à partir de la courbe $[\ce{I2}] = g(t)$ ou des courbes $[\ce{SO4^{2-}}] = h(t)$, $[\ce{I^-}] = m(t)$, etc.

{{% solution "Réponse" %}}
À partir du tableau d'avancement on a déterminé que&nbsp;:
- $[\ce{I2}] (t) = \dfrac{x(t)}{V}$, donc $[\ce{I2}]\_f = \dfrac{x_f}{V}$.     
On a donc $[\ce{I2}] (t_{1/2}) = \dfrac{x(t_{1/2})}{V} = \dfrac{x_f}{2V}$.      
Comme $x_f = V [\ce{I2}]\_f $, $[\ce{I2}] (t_{1/2}) = \dfrac{V [\ce{I2}] _f}{2V} = \dfrac{ [\ce{I2}] _f }{2}$.

$$ \boxed{[\ce{I2}] (t_{1/2}) = \dfrac{ [\ce{I2}] _f }{2} }$$

- $[\ce{SO4^{2-}}] (t) = \dfrac{2 x(t)}{V}$, donc $[\ce{SO4^{2-}}]\_f = \dfrac{2 x_f}{V}$.    
On a donc $[\ce{SO4^{2-}}] (t_{1/2}) = \dfrac{ 2 x(t_{1/2})}{V} = \dfrac{2 x_f}{2V} = \dfrac{x_f}{V}$.    
Comme $x_f = \dfrac{V [\ce{SO4^{2-}}]\_f}{2}$, $[\ce{SO4^{2-}}] (t_{1/2}) = \dfrac{V [\ce{SO4^{2-}}] _f}{2V} = \dfrac{ [\ce{SO4^{2-}}] _f }{2}$.

$$ \boxed{[\ce{SO4^{2-}}] (t_{1/2}) = \dfrac{ [\ce{SO4^{2-}}] _f }{2}} $$

- $[\ce{I^-}] (t) = [\ce{I^-}]\_0 - \dfrac{2 x(t)}{V}$, donc $[\ce{I^-}]\_f = [\ce{I^-}]\_0 - \dfrac{2 x_f}{V}$. On a donc $[\ce{I^-}] (t_{1/2}) = [\ce{I^-}]\_0 - \dfrac{ 2 x(t_{1/2})}{V} = [\ce{I^-}]\_0 - \dfrac{2 x_f}{2V} = [\ce{I^-}]\_0 - \dfrac{x_f}{V}$.    
Comme $x_f = \dfrac{V }{2}\\, ([\ce{I^-}]\_0 - V [\ce{I^-}]\_f) $, $ [\ce{I^-}] (t_{1/2}) =  [\ce{I^-}]\_0 - \dfrac{V }{2}\\, ([\ce{I^-}]\_0 - [\ce{I^-}]\_f) = \dfrac{1}{2}\\, ([\ce{I^-}]\_0 + [\ce{I^-}]\_f)$.

$$ \boxed{[\ce{I^-}] (t_{1/2}) = \dfrac{1}{2}\\, ([\ce{I^-}]\_0 + [\ce{I^-}]\_f) }$$

 - De même, 
 $$ \boxed{[\ce{S2O8^{2-}}] (t_{1/2}) = \dfrac{1}{2}\\, ([\ce{S2O8^{2-}}]\_0 + [\ce{S2O8^{2-}}]\_f) = \dfrac{[\ce{S2O8^{2-}}]\_0}{2} }$$
 puisqu'il s'agit du réactif limitant.

 <img src="/terminales-pc/chap-6/chap-6-4-4.png" alt="" width="100%" />
{{% /solution %}}

### Intérêt de $t_{1/2}$

{{% note tip %}}
Le **temps de demi-réaction** *fournit une échelle de temps caractéristique de la transformation étudiée*. L’expérience montre qu’un système cesse d’évoluer au bout d’une durée de l’ordre de quelques $t_{1/2}$.
{{% /note %}}


## Vitesses (volumiques) d'un formation d'un produit et de disparition d'un réactif

### Vitesse (volumique) de formation d'un produit

{{% note tip %}}
La vitesse (volumique) de formation $v\_f (t)$ d'un produit $X$ a pour expression&nbsp;:
$$ 
    v\_f (t) = \lim \limits_{\Delta t \to 0} \dfrac{\[ X \](t+\Delta t) - \[ X \] (t)}{\Delta t} = \left( \dfrac{\mathrm{d} \[ X \]}{\mathrm{dt}} \right)_t
$$
{{% /note %}}

### Vitesse volumique de disparition d'un réactif

{{% note tip %}}
La vitesse (volumique) de disparition $v\_d (t)$ d'un réactif $Y$ a pour expression&nbsp;:
$$ 
    v\_d (t) = - \left( \lim \limits_{\Delta t \to 0} \dfrac{\[ Y \](t+\Delta t) - \[ Y \] (t)}{\Delta t} \right) = - \left( \dfrac{\mathrm{d} \[ Y \]}{\mathrm{dt}} \right)_t
$$
{{% /note %}}

{{% note warning %}}

Le signe $-$ permet de définir *une vitesse de disparition positive* puisque la concentration du réactif $Y$ diminue au cours du temps.

{{% /note %}}

### Quelle est l’unité d'une vitesse volumique ?

10. À l'aide d'une analyse dimensionnelle, déterminer l'unité de la vitesse volumique.
{{% solution "Réponse" %}}
$[v] = \dfrac{1}{L^3} \times \dfrac{n}{T}$ où $n$ est une quantité de matière. Comme $\dfrac{n}{V} = [C]$ la vitesse volumique est donc une concentration sur un temps et s'exprime en *mole par mètre-cube par seconde*&nbsp;: $\pu{mol.m-3.s-1}$.    
En pratique, on utilise *mole par litre par seconde*&nbsp;: $\pu{mol.L-1.s-1}$.
{{% /solution %}}

### Comment déterminer expérimentalement la valeur de la vitesse de réaction&nbsp;:

{{% note tip %}}
Pour déterminer une vitesse volumique $v$ à une date $t_1$, à partir des valeurs de la concentration d'un produit (ou d'un réactif) $[X]$ (ou $[Y]$) obtenues lors d’une expérience&nbsp;:
- On modélise le «&nbsp;nuage de points&nbsp;»&nbsp;;
- On mesure la pente de la tangente à la courbe obtenue lors de l’étape précédente au point d’abscisse $t_1$.
{{% /note %}}

<!--
11. À l'aide du logiciel Graphical analysis déterminer la vitesse de réaction $v$ aux dates $\pu{5 min}$, $\pu{10 min}$ et $\pu{20 min}$.    
Commenter l'évolution de la vitesse volumique de réaction.
{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-4-5.png" alt="" width="100%" />

- $v (\pu{5 min}) = dfrac{\pu{2,4e-4 mol.min-1}}{\pu{100e-3 L}} = \pu{2,4e-3 mol.L-1.min-1}$&nbsp;;
- $v (\pu{10 min}) = \pu{1,5e-3 mol.L-1.min-1}$&nbsp;;
- $v (\pu{20 min}) = \pu{8,5e-4 mol.L-1.min-1}$&nbsp;;

Comme attendu, la vitesse volumique de réaction diminue au cours du temps.
{{% /solution %}}
-->

11. Écrire l'expression de la vitesse volumique de formation de $[\ce{I_2}]$ et et déterminer ses valeurs aux dates $\pu{5 min}$, $\pu{10 min}$ et $\pu{20 min}$.

{{% solution "Réponse" %}} 
$$ \boxed{v\_f (\ce{I_2})(t) = \dfrac{\mathrm{d} [\ce{I_2}]}{\mathrm{dt}}}$$

<img src="/terminales-pc/chap-6/chap-6-4-6.png" alt="" width="100%" />
{{% /solution %}}

12. Écrire l'expression de la vitesse volumique de disparition de $[\ce{I^-}]$ et déterminer ses valeurs aux dates $\pu{5 min}$, $\pu{10 min}$ et $\pu{20 min}$.

{{% solution "Réponse" %}}

$$
    v\_d (\ce{I^-})(t) = - \dfrac{1}{2} \dfrac{\mathrm{d} [\ce{I^-}]}{\mathrm{dt}}$$

<img src="/terminales-pc/chap-6/chap-6-4-7.png" alt="" width="100%" />

{{% /solution %}}

## Données expérimentales

{{< remote "Résultat du traitement à l'aide du logiciel Graphical Analysis" "/terminales-pc/chap-6/chap-6-4-8.ambl" >}}