---
title: "Quotient de réaction et constante d'équilibre"
subtitle: "Chapitre 10,4"
author: ""
type: ""
date: 2021-01-09T18:58:02+04:00
draft: false
toc: true
tags: ["Quotient de réaction", "Constante d'équilibre", "Taux d'avancement final"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Quotient de réaction

### Introduction

{{% note tip %}}

- Le **quotient de réaction** $Q\_r$ est une grandeur qui caractérise un système chimique dans **un état donné**.

- L’**évolution de sa valeur** au cours de la transformation renseigne sur l’évolution du système chimique étudié.
{{% /note %}}

{{% note normal %}}
Le quotient de réaction calculé dans **deux états différents** du système aura **deux valeurs différentes** *à moins que ces deux états ne soient des états d’équilibre*.
{{% /note %}}

### Expression de $Q\_r$ dans le cas de systèmes chimiques uniquement constitués d’espèces dissoutes 

{{% note tip %}}
Le **quotient de réaction** $Q\_r$ de la réaction d'équation chimique 
$$
    \ce{ \alpha{} A (aq) + \beta B (aq) <=> \gamma C (aq) + \delta D (aq)}
$$
a pour expression, lorsque toutes les espèces sont dissoutes dans la solution 
$$
    Q\_r = \dfrac{\left( \dfrac{[{C}]}{C^o} \right)^\gamma \cdot \left( \dfrac{[{D}]}{C^o} \right)^\delta}{\left( \dfrac{[{A}]}{C^o} \right)^\alpha \cdot \left( \dfrac{[{B}]}{C^o} \right)^\beta}
$$
avec $C^o = \pu{1,00 mol.L-1}$.
{{% /note %}}

{{% note warning %}}
$Q\_r$ est une grandeur sans dimension.
{{% /note %}}

<img src="/terminales-pc/chap-9/chap-9-4/chap-9-4-1.png" alt="" width="90%" />

{{% note exercise %}}
Soit l'équation de la réaction d'oxydation des ions thiosulfate $\ce{S2O3^{2-}}$ par le diiode $\ce{I2}$. Il se forme des ions tetrathionate  $\ce{S4O6^{2-}}$ et des ions iodure $\ce{I-}$.

1. Écrire l'équation de la réaction.

2. Donner l'expression du quotient de réaction pour un état quelconque d'une transformation modélisée par la réaction étudiée.
{{% /note %}}

{{% solution "Réponses" %}}
1. 
$$
    \ce{ I2 (aq) + 2 S2O3^{2-} (aq) <=> 2 I- (aq) +  S4O6^{2-} (aq)  }
$$

2. 
$$
    Q\_r = \dfrac{\left( \dfrac{[\ce{I-}]}{C^o} \right)^2 \cdot \left( \dfrac{[\ce{S4O6^{2-}}]}{C^o} \right)}{\left( \dfrac{[\ce{I2}]}{C^o} \right) \cdot \left( \dfrac{[\ce{S2O3^{2-}}]}{C^o} \right)^2}
$$
soit
$$
    Q\_r = \dfrac{[\ce{I-}]^2 \cdot [\ce{S4O6^{2-}}]}{[\ce{I2}] \cdot [\ce{S2O3^{2-}}]^2}
$$
{{% /solution %}}

{{% note exercise %}}
Soit la réaction acide-base entre l'acide éthanoïque et l'eau. 

1. Écrire l'équation de la réaction.

2. Donner l'expression du quotient de réaction pour un état quelconque d'une transformation modélisée par la réaction étudiée.
{{% /note %}}

{{% solution "Réponses" %}}
1. 
$$
    \ce{CH3CO2H (aq) + H2O <=> CH3CO2- (aq) + H3O+}
$$

2. 
$$
    Q\_r = \dfrac{\left( \dfrac{[\ce{CH3CO2-}]}{C^o} \right) \cdot \left( \dfrac{[\ce{H3O+}]}{C^o} \right)}{\left( \dfrac{[\ce{CH3CO2H}]}{C^o} \right)}
$$
soit
$$
    Q\_r = \dfrac{[\ce{CH3CO2-}] \cdot [\ce{H3O+}]}{[\ce{CH3CO2H}] \cdot C^o}
$$
{{% /solution %}}

{{% note warning %}}

- L’eau, **si c’est le solvant**, ne doit pas apparaître dans l’écriture du quotient de réaction.

- Dans le cas des réactions d'estérification l'eau est un produit de la réaction qui ne se fait pas en solution aqueuse. **L'eau doit alors intervenir dans le quotient de réaction**.
{{% /note %}}


### L’expression de $Q\_r$ dépend-elle du sens d’écriture de l’équation de la réaction ?

{{% note exercise %}}
On introduit dans un bécher de l’acide méthanoïque, des ions méthanoate, de l’acide éthanoïque et des ions éthanoate dilués. Le système ainsi formé est le siège d’une réaction chimique qui conduit à un état d’équilibre.

1. Écrire les deux équations chimiques symbolisant la réaction chimique.

2. Déterminer pour chacune de ces équations l’expression du quotient de réaction (les noter $Q\_{r,1}$ et $Q\_{r,2}$).

3. Quelle relation existe-t-il entre $Q\_{r,1}$ et $Q\_{r,2}$ ?
{{% /note %}}

### Expression de $Q\_r$ dans le cas de systèmes chimiques comportant des solides

{{% note tip %}}
L’expression du quotient de réaction d’une réaction faisant intervenir des solides et des espèces dissoutes ne doit faire apparaître que les concentrations molaires des espèces dissoutes.
{{% /note %}}

{{% note exercise %}}
Soit la réaction d'oxydoréduction du cuivre $\ce{Cu}$ avec les ions argent I $\ce{Ag+}$. Il se forme du cuivre II $\ce{Cu^{2+}}$ et de l'argent $\ce{Ag}$.

1. Écrire l'équation de la réaction chimique.

2. Donner l'expression du quotient de réaction pour un état quelconque d'une transformation chimique modélisée par cette réaction.
{{% /note %}}
{{% solution "Réponses" %}}

1. 
$$
    \ce{ Cu (s) + 2 Ag^+ (aq) <=> Cu^{2+} (aq) + 2 Ag (s)   }
$$

2. 
$$
    Q\_r = \dfrac{\left( \dfrac{[\ce{Cu^{2+}}]}{C^o} \right) }{\left( \dfrac{[\ce{Ag+}]}{C^o} \right)^2}
$$
soit
$$
    Q\_r = \dfrac{[\ce{Cu^{2+}}] \cdot C^o}{ [\ce{Ag+}]^2}
$$
{{% /solution %}}

{{% note exercise %}}
Soit la réaction de précipitation entre les ions fer III $\ce{Fe^{3+}}$ et les ions hydroxyde $\ce{OH^-}$ en solution aqueuse. Il se forme de l'hydroxyde de fer III.

1. Écrire l'équation de la réaction chimique.

2. Donner l'expression du quotient de réaction pour un état quelconque d'une transformation chimique modélisée par cette réaction.
{{% /note %}}
{{% solution "Réponses" %}}
1. 
$$
    \ce{ Fe^{3+} (aq) + 3 OH^- (aq) <=> Fe(OH)3 (s) }
$$

2. 
$$
    Q\_r = \dfrac{1}{\left( \dfrac{[\ce{OH^-}]}{C^o} \right)^3 \cdot \left( \dfrac{[\ce{Fe^{3+}}]}{C^o} \right)}
$$
soit 
$$
    Q\_r = \dfrac{C^{o4}}{[\ce{OH^-}]^3 \cdot [\ce{Fe^{3+}}]}
$$
{{% /solution %}}

{{% note exercise %}}
Soit la réaction de précipitation du phosphate de calcium $\ce{Ca3(PO4)2}$ en solution aqueuse à partir des ions calcium $\ce{Ca^{2+}}$ et phosphate $\ce{PO4^{3-}}$.

1. Écrire l'équation de la réaction chimique.

2. Donner l'expression du quotient de réaction pour un état quelconque d'une transformation chimique modélisée par cette réaction.
{{% /note %}}

{{% solution "Réponses" %}}
1. 
$$
    \ce{ 3 Ca^{2+} (aq) + 2 PO4^{3-} (aq) <=> Ca3(PO4)2 (s) }
$$

2. 
$$
    Q\_r = \dfrac{1}{\left( \dfrac{[\ce{Ca^{2+}}]}{C^o} \right)^3 \cdot \left( \dfrac{[\ce{PO4^{3-}}]}{C^o} \right)^2}
$$
soit
$$
    Q\_r = \dfrac{C^{o5}}{[\ce{Ca^{2+}}]^3 \cdot [\ce{PO4^{3-}}]^2}
$$
{{% /solution %}}




### Quotient de réaction et avancement de de la réaction

{{% note exercise %}}
On considère une transformation chimique modélisée par la réaction entre l’acide benzoïque et les ions éthanoate en solution aqueuse.\
On introduit $\pu{10,0 mmol}$ d’acide benzoïque et $\pu{20,0 mmol}$ d’ions éthanoate dans l’état initial.

1. Établir le tableau d’évolution de ce système.
2. Donner l’expression du quotient de réaction pour un état quelconque.
3. Exprimer ce quotient de réaction en fonction de $x$, avancement de la réaction.
4. Quelles sont les valeurs du quotient de réaction pour $\pu{x = 2,0 mmol}$ et $\pu{x = 4,0 mmol}$ ?

{{% /note %}}
{{% solution "Réponses" %}}

{{% /solution %}}


{{% note tip %}}
Le quotient de réaction dépend de l’avancement de la réaction.
{{% /note %}}


## Quotient de réaction dans l'état d'équilibre : constante d’équilibre

Que vaut le quotient de réaction lorsque l'état d'équilibre est atteint ?


### La valeur de $Q\_{r}$ à l'équilibre dépend-elle de l'état initial ?

{{% note exercise %}}
Soit la réaction entre l'acide éthanoïque et l'eau d'équation :
$$
\ce{CH3CO2H (aq) + H2O <=> CH3CO2^- (aq) + H3O+ (aq)}
$$
On mesure les conductivités de deux solutions d'acide éthanoïque :
<center>

|  | $C (\pu{mol.L-1})$ | $\sigma (\pu{mS.m-1})$|
| :----: | :----: | :----: |
| $S\_1$ | $\pu{5,0e-2}$ | 0,343 |
| $S\_2$ | $\pu{5,0e-3}$ | 0,107 |

</center>

Données
: $\lambda_{\ce{CH3CO2^-}} = \pu{4,09 mS.m2.mol-1}$, $\lambda_{\ce{H3O^+}} = \pu{35,0 mS.m2.mol-1}$

1. Pour la solution $S\_{1}$, dans l'état d'équilibre :

    1. Quelles sont les concentrations molaires de ces ions ?

    2. Quelle est la concentration molaire en acide éthanoïque ?

    3. Quelle est la valeur du quotient de réaction ?

2. Reprendre les mêmes questions pour la solution $S\_{2}$ et conclure.
{{% /note %}}
{{% solution "Réponse" %}}

{{% /solution %}}

### Constante d'équilibre

{{% note tip %}}

- Dans l'**état d'équilibre** d'un système, le quotient de réaction, $Q\_{r,eq}$, prend une *valeur indépendante de la composition initiale* du système.

- À chaque équation de réaction est associée une constante appelée **constante d'équilibre** et notée $K$ dont la *valeur ne dépend que de la température*.

- Dans l'état d'équilibre : $$ Q\_{r,eq} = K $$

- Pour une réaction en solution aqueuse d'équation,
$$
    \ce{ \alpha A (aq) + \beta B (aq) <=> \gamma C (aq) + \delta D (aq)  }
$$
la constante d'équilibre $K$ s'écrit :
$$
    K = \dfrac{\left( \dfrac{[{C}]}{C^o} \right)^\gamma \cdot \left( \dfrac{[{D}]}{C^o} \right)^\delta}{\left( \dfrac{[{A}]}{C^o} \right)^\alpha \cdot \left( \dfrac{[{B}]}{C^o} \right)^\beta}
$$
{{% /note %}}

{{% note warning %}}
$K$ est une grandeur sans dimension.
{{% /note %}}

### Le taux d'avancement final dépend-il de la valeur de la constante d'équilibre ?

{{% note exercise %}}
On mesure les conductivités $\sigma\_{1} = \pu{343 \mu S.cm-1}$ et $\sigma\_{2} = \pu{1129 \mu S.cm-1}$ de deux solutions $S\_{1}$ d'acide éthanoïque et $S\_{2}$ d'acide méthanoïque de même concentration apportée $C = \pu{5,0e-2 mol.L-1}$.

Données
: - Acide méthanoïque et eau : $K = \pu{1,6e-4}$ ;
- Acide éthanoïque et eau : $K = \pu{1,6e-5}$.

1. Quelles sont les concentrations des espèces ioniques dans ces deux solutions ?

2. Quelle est, dans chaque cas, la valeur du taux d'avancement final ? Conclure.
{{% /note %}}

{{% solution "Réponses" %}}

{{% /solution %}}

{{% note tip %}}
Le taux d'avancement final d'une réaction dépend de la valeur de sa constante d'équilibre.
{{% /note %}}

### Le taux d'avancement final dépend-il de la constitution de l'état initial ?

{{% note exercise %}}
On mesure les conductivités de diverses solutions d'acide éthanoïque de concentration apportée $C$ :

<center>

| $C (\pu{mol.L-1})$ |	$\sigma (\pu{mS.cm-1})$ |
| :----: |	:----: |
| $\pu{5,0e-2}$ | 0,343 |
| $\pu{1,0e-2}$ | 0,153 |
| $\pu{5,0e-3}$ | 0,107 |

</center>

Que vaut le taux d'avancement final de ces solutions ? Conclure.
{{% /note %}}

{{% solution "Réponses" %}}

{{% /solution %}}


{{% note tip %}}
Le taux d'avancement final d'une réaction dépend de l'état initial du système.
{{% /note %}}

## À retenir

{{% note tip %}}

- Dans l'état d'équilibre d'un système, le quotient de réaction, $Q\_{r,eq}$, prend une **valeur indépendante de la composition initiale**.

- À chaque équation de réaction est associée une constante, appelée **constante d'équilibre**, dont la **valeur ne dépend que de la température**.

- Dans l'état d'équilibre : $$Q\_{r,eq} = K$$

{{% /note %}}

> Pour deux transformations chimiques différentes mais modélisées par la même réaction chimique :
<img src="/terminales-pc/chap-9/chap-9-4/chap-9-4-2.png" alt="" width="100%" />

{{% note tip %}}
Le taux d'avancement final d'une réaction dépend de la **constante d'équilibre** de cette réaction et de l'**état initial du systèm**e.
{{% /note %}}