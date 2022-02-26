---
title: "Exercices du chapitre"
subtitle: "Chapitre 2,5"
author: ""
type: ""
date: 2020-09-15T21:35:00+04:00
draft: false
toc: true
tags: ["Soluté", "Concentration molaire", "Concentration massique", "Beer Lambert", "Dilution", "Couleur", "Absorption"]
categories: ["Premières Spé PC", "Chimie"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Concentrations molaires et dilution

{{% note exercise %}}
#### Exercice 1 : Solution de réhydratation

On peut effectuer des injections de solution aqueuse de fructose, de
formule $\ce{C6H12O6}$, pour prévenir la déshydratation. De telles solutions sont
obtenues en dissolvant une masse $m = \pu{25,0 g}$ de fructose pour $\pu{500 mL}$ de solution finale.

1.  Déterminer la quantité de matière de fructose correspondant à la
    masse indiquée dans l'énoncé.

2.  En déduire la concentration molaire de ces solutions en fructose.
{{% /note %}}

{{% solution "Réponse" %}}
1.  $n(\ce{C6H12O6}) = \dfrac{m(\ce{C6H12O6})}{M(\ce{C6H12O6})}$

    **A.N.** $n(\ce{C6H12O6}) = 
        \dfrac{\pu{25,0 g}}{(\pu{6} \times \pu{12,0} + 12 \times \pu{1,0} + 6 \times \pu{16,0})\\, \pu{g.mol-1}} = \pu{1,39e-1 mol}$

2.  $C(\ce{C6H12O6}) = \dfrac{n(\ce{C6H12O6})}{V_{\text{solution}}}$   

    **A.N.** $C(\ce{C6H12O6}) = \dfrac{\pu{1,39e-1 mol}}{\pu{500e-3 L}} = \pu{2,78e-1 mol.L-1}$
{{% /solution %}}


{{% note exercise %}}
#### Exercice 2 : Vitamine C

La vitamine C, ou acide ascorbique $\ce{C6H8O6}$, est souvent prescrite en cas de
grippe ou de période de convalescence. Elle peut se présenter en sachets
contenant, entre autres, une masse $m_1 = \pu{1,0 g}$ de vitamine C
et $m_2 = \pu{6,05 g}$ de saccharose $\ce{C12H22O11}$.

Le contenu d'un sachet est dissous dans un demi-verre d'eau. En
considérant que le volume de la solution obtenue vaut
$V = \pu{125 mL}$, déterminer les concentrations molaires de
ces solutés dans la solution.
{{% /note %}}

{{% solution "Réponse" %}}
$C(\text{espèce}) = \dfrac{n(\text{espèce})}{V_{\text{solution}})}$ et $n(\text{espèce}) = \dfrac{m(\text{espèce})}{M(\text{espèce})}$, donc $$C(\text{espèce}) = \dfrac{m(\text{espèce})}{M(\text{espèce}) V_{\text{solution}}}$$

- Pour la vitamine C : 

$C(\ce{C6H8O6}) = \dfrac{ \pu{1,0 g} }{ \pu{ (6 \times \pu{12,0} + 8 \times \pu{1,0} + 6 \times \pu{16,0} ) \\, \pu{g.mol-1}} \times \pu{125e-3 L} } = \pu{4,5e-2 mol.L-1}$

- Pour le saccharose :

$C(\ce{C12H22O11}) = \dfrac{ \pu{6,05 g} }{ \pu{ (12 \times \pu{12,0} + 22 \times \pu{1,0} + 11 \times \pu{16,0} ) \\, \pu{g.mol-1}} \times \pu{125e-3 L} } = \pu{1,42e-1 mol.L-1}$

{{% /solution %}}

{{% note exercise %}}
#### Exercice 3 : Préparation d’une limonade

La limonade est une boisson contenant du dioxyde de carbone, du glucose,
du saccharose, de l'acide citrique et un arôme naturel de citron.

La concentration en glucose $\ce{C6H12O6}$ d'une limonade vaut $C_1
 = \pu{5,6e-2 mol.L-1}$. La concentration en saccharose $\ce{C12H22O11}$, dans
la même limonade, est égale à $C_2 = \pu{6,4e-2 mol.L-1}$.

Quelles sont les masses de glucose et de saccharose qu'un volume $V = \pu{1,5 L}$ de cette limonade contient ?
{{% /note %}}

{{% solution "Réponse" %}}
- $C = \dfrac{n(\text{soluté})}{V_{\text{solution}}}$ et $n(\text{soluté}) = \dfrac{m(\text{soluté})}{M(\text{soluté})}$ donc $C = \dfrac{m(\text{soluté})}{M(\text{soluté}) V_{\text{solution}}} \Leftrightarrow m(\text{soluté}) = C M(\text{soluté}) V_{\text{solution}}$.

- **A.N.** $m(\ce{C6H12O6}) = \pu{5,6e-2 mol.L-1} \times \pu{1,5 L} \pu{180 g.mol-1} = \pu{1,5e1 g}$.

- **A.N.** $m(\ce{C12H22O11}) = \pu{6,4e-2 mol.L-1} \times \pu{1,5 L} \pu{342 g.mol-1} = \pu{3,3e1 g}$.
{{% /solution %}}

{{% note exercise %}}
#### Exercice 4 : Un peu de sirop

Un sirop de menthe doit sa couleur à deux colorants : le *bleu patenté*
et la *tartrazine* (colorant jaune) respectivement repérés par les
sigles E131 et E102.

La concentration du E131 dans le sirop vaut
$C = \pu{7,7e-5 mol.L-1}$. À 40&nbsp;mL de ce sirop, dans un verre,
on ajoute de l'eau de telle sorte que le volume final de la solution,
après homogénéisation, est égal à $V' = \pu{250 mL}$.

Quelle est la concentration molaire du colorant dans cette solution ?
{{% /note %}}

{{% solution "Réponse" %}}
- Avant de pouvoir déterminer la concentration molaire du colorant dans la solution finale, il faut déterminer la quantité de matière prélevée lorsqu'on récupère un volume $V_1 = \pu{40 mL}$ : $n_1 = C_1 V_1$.
- La concentration finale est alors $C_2 = \dfrac{n_1}{V_2} = \dfrac{C_1 V_1}{V_2}$ où $V_2$ est le volume final de la solution.
- **A.N.** $C_2 = \dfrac{\pu{7,7e-5 mol.L-1} \pu{40 mL}}{\pu{250 mL}} = \pu{1,2e-5 mol.L-1}$.
{{% /solution %}}

{{% note exercise %}}
#### Exercice 5 : Dilution d’une solution

Un laboratoire dispose d'une solution de Lugol de concentration
$C_0 = \pu{4,10e-2 mol.L-1}$ en diiode $\ce{I_2}$. Un laborantin veut
préparer un volume $V_1 = \pu{100 mL}$ de « soluté de Tarnier »,
solution de diiode de concentration $C_1 = \pu{5,90e-3 mol.L-1}$.

Quel volume $V_p$ de solution de Lugol le laborantin doit-il prélever ?
{{% /note %}}

{{% solution "Réponse" %}}
- Si le laborantin prélève le volume $V_p$ de solution mère à la concentration $C_0$, il prélève la quantité de matière $n_p = C_0 V_p$.

- La quantité de matière en Lugol présente dans la solution fille à la concentration $C_1$ a pour origine la quantité de matière prélevée dans la solution mère, donc $n_1 = n_p$.

- Comme $n_1 = C_1 V_1$, $C_0 V_p = C_1 V_1 \Leftrightarrow V_p = \dfrac{C_1 V_1}{C_0} = V_1 \dfrac{C_1}{C_0}$.

- **A.N.** $V_p = \dfrac{\pu{5,90e-3 mol.L-1} }{\pu{4,10e-2 mol.L-1}} \times \pu{100 mL} = \pu{14,4 mL}$.
{{% /solution %}}

{{% note exercise %}}
#### Exercice 6 : Échelle de teintes

On prépare une [échelle de teintes](https://youtu.be/gApSW_bniIk) à partir d'une solution mère $S_0$ de permanganate de potassium de concentration
$C_0 = \pu{1,0e-2 mol.L-1}$. Pour cela, on introduit, dans des
tubes à essais identiques, un volume $V_{ip}$ de solution mère $S_0$ et on
complète à 10,0&nbsp;mL avec de l'eau distillée selon le tableau ci-dessous.

**Remarque :** $F_i$ est le facteur de dilution : $$F_i = \dfrac{C_0}{C_i} $$

Compléter le tableau ci-dessous.

<center>

| **Solution fille** | $S_1$ | $S_2$ | $S_3$ | $S_4$ | $S_5$ | $S_6$ |
| :-------: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: |
| $F_i$ | 5/4 | 5/3 | 5/2 | 5 | 10 | 20 |
| $V_{ip} (S_0)$ (mL) | | | | | | |                                              
| $V_i (\text{eau})$ (mL) |  |  |  |  |  |  |                                         
| $C_i$ (mol/L) |  |  |  |  |  |  | 

</center>
{{% /note %}}

{{% solution "Réponse" %}}
<center>

| **Solution fille** | $S_1$ | $S_2$ | $S_3$ | $S_4$ | $S_5$ | $S_6$ |
| :-------: | :-------: | :-------: | :-------: | :-------: | :-------: | :-------: |
| $F_i$ | 5/4 | 5/3 | 5/2 | 5 | 10 | 20 |
| $V_{ip} (S_0)$ (mL) | $\pu{8,0}$ | $\pu{6,0}$ | $\pu{4,0}$ | $\pu{2,0}$ | $\pu{1,0}$ | $\pu{0,5}$ |                                              
| $V_i (\text{eau})$ (mL) | $\pu{2,0}$ | $\pu{4,0}$ | $\pu{6,0L}$ | $\pu{8,0}$ | $\pu{9,0}$ | $\pu{9,5}$ |                                         
| $C_i$ (mol/L) | $\pu{8,0e-3}$ | $\pu{6,0e-3}$ | $\pu{4,0e-3}$ | $\pu{2,0e-3}$ | $\pu{1,0e-3}$ | $\pu{0,5e-3}$ | 

</center>

- Si on prélève le volume $V_{ip}$ de solution mère à la concentration $C_0$, on prélève la quantité de matière $n_{ip} = C_0 V_{ip}$.

- La quantité de matière en permanganate de potassium présente dans la solution fille $S_i$ à la concentration $C_i$ a pour origine la quantité de matière prélevée dans la solution mère, donc $n_i = n_{ip}$.

- Comme $n_i = n_{ip}$, $C_0 V_{ip} = C_i V_i \Leftrightarrow V_{ip} = \dfrac{C_i V_i}{C_0} = V_i \dfrac{C_i}{C_0}$.

Exemple de calcul : $V_{1p} = \pu{10 mL} \times \dfrac{\pu{8,0e-3}}{\pu{1,0e-2}} = \pu{8,0 mL}$.

- $V_i (\text{eau}) = V_i - V_{ip}$

Exemple de calcul : $V_1 (\text{eau}) = \pu{10 mL} - \pu{8,0 mL} = \pu{2,0 mL}$.
{{% /solution %}}

{{% note exercise %}}
#### Exercice 6 : Glycérotone

Le glycérotone est un médicament permettant de lutter contre les
tensions oculaires et intracrâniennes. C'est une solution aqueuse qui
contient du glycérol, de formule chimique $\ce{C3H8O3}$, à la concentration
$C = \pu{6,89 mol.L-1}$.

Le glycérol étant un liquide de masse volumique $\rho = \pu{1,26 g.mL-1}$, déterminer le volume de glycérol nécessaire à la préparation de $V = \pu{50,0 mL}$ de glycérotone.
{{% /note %}}

{{% solution "Réponse" %}}

- $C = \dfrac{n}{V_{\text{sol}}}$. Dans cette formule, nous connaissons la concentration et le volume de la solution, donc $n = C \cdot V_{\text{sol}}$ est la quantité de matière qu'il faut introduire pour préparer la solution attendue.
- $n = \dfrac{m}{M} \Leftrightarrow m = n \cdot M$. Introduire $n$ moles de glycérotone, revient à introduire une masse $m$ de cette espèce chimique.
- $m = \rho \cdot V_{\text{à prélever}} \Leftrightarrow V_{\text{à prélever}} = \dfrac{m}{\rho}$. Prélever une masse $m$ revient à prélever un volume $V_{\text{à prélever}}$.

Lorsqu'on remet tout en place, on obtient : $V_{\text{à prélever}} = \dfrac{n \cdot M}{\rho} = \dfrac{C \cdot V_{\text{sol}} \cdot M}{\rho} $.

**A.N.** $V_{\text{à prélever}} = \dfrac{\pu{6,89 mol.L-1} \times \pu{50,0e-3 L} \times (3 \times \pu{12,0} + 8 \times \pu{1,0} + 3 \times \pu{16,0})\pu{g.mol-1}}{\pu{1,26 g.mL-1}} = \pu{25,2 mL}$.

{{% /solution %}}


## Exercices sur le Livre Scolaire

- {{< remote "n° 9, 10, 11, 12, 13, 14" "https://www.lelivrescolaire.fr/page/6562927" >}}

- {{< remote "n° 26, 27, 28, 29" "https://www.lelivrescolaire.fr/page/6562971" >}}

{{% solution "Solutions" %}}
{{< remote "Corrigés" "/premieres-pc/chap-2/chap-2-5-1.pdf" >}}
{{% /solution %}}