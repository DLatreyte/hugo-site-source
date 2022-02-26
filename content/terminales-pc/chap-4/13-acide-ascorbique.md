---
title: "Annale : Acide Ascorbique"
subtitle: "Chapitre 5,14"
author: ""
type: ""
date: 2020-10-29T11:15:12+04:00
draft: false
toc: true
tags: ["Titrage", "Suivi conductimétrique", "Suivi pH-métrique", "Conductivité", "Base", "Acide", "Équivalence", "Titrage colorimétrique", "Incertitudes"]
categories: ["Chimie", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: true
auto_numbering: true
---
$\gdef\barcirc{{\mathrlap{\mathchoice{\kern{0.145em}}{\kern{0.145em}}{\kern{0.1015em}}{\kern{0.1015em}}\circ}{-}}}$

À la fin du XVI<sup>e</sup> siècle, beaucoup de marins succombaient au scorbut. Cette mortalité était due à une carence en vitamine C aussi appelée « acide ascorbique ». Il s’agit d’un acide organique ayant entre autres des propriétés anti-oxydantes. Il est présent dans les citrons, les jus de fruits et les légumes frais.   
Le nom « ascorbique » vient du préfixe grec a (privatif) et de scorbut, signifiant littéralement anti-scorbut.  
La vitamine C intervient dans de nombreuses réactions d’oxydo-réduction dans l’organisme, dans le métabolisme du fer et des acides aminés.

> Acide ascorbique (il est possible de zoomer avec la molette de la souris et de faire tourner la molécule)

<center>

<iframe style="width: 500px; height: 300px;" frameborder="0" src="https://embed.molview.org/v1/?mode=balls&cid=54670067&bg=white"></iframe>

</center>

L'objectif de cet exercice est de présenter deux méthodes différentes de titrage de l'acide ascorbique.

## Titrage de l’acide ascorbique par suivi pH-métrique

On souhaite vérifier l’indication figurant sur une boîte de comprimés de vitamine C vendue en pharmacie : le fabricant annonce que la masse d’acide ascorbique est de 
$\pu{500 mg}$ par comprimé.  
Un comprimé de vitamine C est écrasé dans un mortier. La poudre est ensuite dissoute dans une fiole jaugée de $V = \pu{200,0 mL}$ que l’on complète avec de l’eau distillée jusqu’au trait de jauge en homogénéisant le mélange. On obtient la solution $S$.
On prélève $V_A = \pu{10,0 mL}$ de cette solution que l’on titre avec une solution d’hydroxyde de sodium $(\ce{Na^+(aq) + HO^–(aq)})$ de concentration molaire $C_B = \pu{1,00e–2 mol.L-1}$. L'incertitude sur cette valeur est $U(C_B) = \pu{0,02e-2 mol.L^-1}$.    
On suit le titrage par pH-métrie. Le graphique représentant l’évolution du pH en fonction du volume de solution d’hydroxyde de sodium versé est représenté en ANNEXE À RENDRE AVEC LA COPIE.

L’acide ascorbique sera noté AH dans la suite de l’exercice.

1. L’ion hydroxyde est une base forte en solution aqueuse.   
Déterminer le pH de la solution d’hydroxyde de sodium utilisée pour le titrage. En déduire les précautions qu’il convient d’adopter pour utiliser cette solution.

{{% solution "Réponse" %}}
Puisque l'ion hydroxyde est une base forte, sa réaction avec l'eau modélise une transformation chimique totale : 

$$\ce{ HO^- + H2O -> H2O + HO^-  }$$

Cette réaction ne modifie pas les concentrations et $[\ce{HO^-}] = \pu{1,00e–2 mol.L-1}$. À partir des relations et des valeurs dans les données, on en déduit que, comme $[\ce{H3O^+}] = \dfrac{ K_e \cdot (C^\barcirc)^2 }{ [\ce{HO^-}] }$, $[\ce{H3O^+}] = \dfrac{ \pu{1,0e-14} \times (\pu{1,0 mol.L-1})^2 }{ \pu{1,00e–2 mol.L-1} } = \pu{1,00e–12 mol.L-1}$.

Le pH de la solution doit donc être égal à $-\log \left(\dfrac{\pu{1,00e–12 mol.L-1}}{\pu{1,0 mol.L-1}}\right) = 12$.

Ce pH étant élevé, il faut porter des lunettes de protection et une blouse.
{{% /solution %}}

2. Réaliser un schéma annoté du montage expérimental nécessaire à la mise en œuvre du titrage.

{{% solution "Réponse" %}}

{{% /solution %}}

3. Écrire l’équation de la réaction support du titrage.

{{% solution "Réponse" %}}
Le réactif titré est l’acide ascorbique $\ce{AH}$ (acide), le réactif titrant est $\ce{HO^–}$ (base présente dans la solution d’hydroxyde de sodium). L’équation de la réaction support de titrage est : 
$$\ce{ AH(aq)  + HO^–(aq) -> A–(aq) + H2O(l) }$$

{{% /solution %}}

4. À partir du protocole mis en œuvre et des résultats obtenus, déterminer $m$, la masse d’acide ascorbique contenue dans le comprimé. L’ANNEXE EST À RENDRE AVEC LA COPIE.

{{% solution "Réponse" %}}
- En appliquant la méthode des tangentes, on détermine le volume de titrant à verser pour atteindre [l'équivalence](https://youtu.be/cYm4-4D4tas) : $V_{BE} = \pu{13,6 mL}$.

- Tableau d'avancement pour l'état final équivalence : 
    - $n_E(\ce{AH}) = n_0(\ce{AH}) - x_E = 0 \iff C_{AS} V_A - x_E = 0 $ ;
    - $n_E(\ce{HO^-}) = C_B V_{BE} - x_E = 0$.    
    Donc $C_{AS} = C_B \dfrac{V_{BE}}{V_A}$.

- La quantité de matière d'acide ascorbique est $n_A = C_{AS} V_S = C_B \dfrac{V_{BE}}{V_A} V_S$.

- La masse d'acide ascorbique est finalement égale à $m_A = C_B \dfrac{V_{BE}}{V_A} V_S M(A)$.    
<strong>A.N.</strong> $m_A = \pu{1,00e-2 mol.L^-1} \times \dfrac{\pu{13,6 mL}}{\pu{10,0 mL}} \times \pu{200,0e-3 L} \times \pu{176,0 g.mol-1} = \pu{4,79e-1 g}$.
{{% /solution %}}

5. L'incertitude sur $m$ est donnée par l'expression :
$$
\left(\dfrac{U(m)}{m}\right)^2 = \left(\dfrac{U(C_B)}{C_B}\right)^2 + \left(\dfrac{U(V_{BE})}{V_{BE}}\right)^2 + \left(\dfrac{U(V_A)}{V_A}\right)^2 + \left(\dfrac{U(V)}{V}\right)^2
$$
La précision relative de la verrerie étant de 0,5&nbsp;% et celle du volume équivalent estimée à 1&nbsp;%, determiner la valeur de l'incertitude $U(m)$.

{{% solution "Réponse" %}}
- $ U(m) = m \cdot \sqrt{  \left(\dfrac{U(C_B)}{C_B}\right)^2 + \left(\dfrac{U(V_{BE})}{V_{BE}}\right)^2 + \left(\dfrac{U(V_A)}{V_A}\right)^2 + \left(\dfrac{U(V)}{V}\right)^2  }$    
<strong>A.N.</strong> $ U(m) = \pu{4,79e-1 g} \times \sqrt{ \left(\dfrac{\pu{0,02e-2 mol.L^-1}}{\pu{1,00e–2 mol.L-1}}\right)^2 + ( \pu{1e-2})^2 + ( \pu{0,5e-2} )^2 + ( \pu{0,5e-2} )^2 } = \pu{1,12e-2 g} = \pu{2e-2 g}$.
{{% /solution %}}

6. Le résultat obtenu pour la masse $m$ est-il en accord avec l'étiquette ?

{{% solution "Réponse" %}}
- Résultat du titrage : $m_A = \pu{(4,8 \pm 0,2) g}$.
- Cet intervalle comporte bien la valeur attendue, il est donc en accord avec l'étiquette.
{{% /solution %}}

7. D’après les résultats obtenus, peut-on savoir si l’acide ascorbique est un acide fort ou un acide faible ? Justifier la réponse.

{{% solution "Réponse" %}}
- Si l’acide ascorbique est un acide fort, sa réaction avec l’eau est totale :
$$\ce{ AH(aq) + H2O -> A^-(aq) + H3O^+ } $$
- Tableau d'avancement pour la transformation hypothétique totale : 
    - $n_f(AH) = n_0(AH) - x_{\text{max}} = 0$ ;
    - $n_f(H3O^+) = x_{\text{max}} = 0$.    
    Donc $x_{\text{max}} = n_0(AH) = n_f(H3O^+)$ et $[H3O^+]_f = \dfrac{n_0(AH)}{V_S}$.    
    <strong>A.N.</strong> $[H3O^+]\_f = \dfrac{\pu{4,79e-1 g}}{\pu{176,0 g.mol-1} \times \pu{200,0e-3 L}} = \pu{1,36e-2 mol/L-1}$.
- pH de la solution si l'acide ascorbique est un acide fort : $\text{pH} = \pu{1,9}$.
- À l’aide de la courbe du titrage, on lit pour $V_B = \pu{0 mL}$, donc avant l’ajout de solution titrante, $\text{pH} = \pu{3,0}$.    
Le pH expérimental étant supérieur à la valeur théorique, l’acide ascorbique est un acide faible. La solution contient moins d’ions $\ce{H3O^+}$ que si la transformation était totale.
{{% /solution %}}

## Autres méthodes de titrage

Le titrage de l’acide ascorbique peut également se faire par d’autres techniques. Nous allons dans cette partie étudier succinctement deux : l’utilisation d’un indicateur coloré et le suivi conductimétrique.

### Utilisation d’un indicateur coloré

{{% note tip %}}
- Lors d'un titrage colorimétrique, un changement de teinte du mélange réactionnel permet de repérer l'équivalence. Ce repérage peut être facilité par l'utilisation d'un **indicateur de fin de réaction**.
- Un **indicateur coloré acido-basique** est un couple acide/base dont les deux entités (acide et base) ne colorent pas de la même façon la solution. Si sa zone de virage  contient le pH à l'équivalence $pH_E$, il peut être utilisé comme l'**indicateur de fin de réaction**.
{{% /note %}}

**Remarque :** Une étude plus précise des indicateur colorés acido-basiques sera menée dans un prochain chapitre.

8. Parmi les indicateurs colorés proposés, lequel utiliseriez-vous pour le titrage de l’acide ascorbique par la solution d’hydroxyde de sodium effectué dans la partie 2 ? Justifier la réponse et préciser comment l’équivalence est repérée.

<center>

| Indicateur coloré | Teinte acide | Zone de virage | Teinte basique |
| :---: | :---: | :---: | :---: |
| Hélianthine | Rouge | 3,1 – 4,4 | Jaune |
| Vert de bromocrésol | Jaune | 3,8 – 5,4 | Bleu |
| Bleu de bromothymol | Jaune | 6,0 – 7,6 | Bleu |
| Rouge de crésol | Jaune | 7,2 – 8,8 | Rouge |
| Phénolphtaléine | Incolore | 8,2 – 10,0 | Rose |
| Rouge d’alizarine | Violet | 10,0 – 12,0 | Jaune |
| Carmin d’indigo | Bleu | 11,6 – 14,0 | Jaune |

</center>

{{% solution "Réponse" %}}
- Un indicateur coloré est adapté à un titrage pH-métrique si le pH à l’équivalence est inclus dans sa zone de virage.
- Ici, $pH_E = \pu{7,8}$ ; on pourra utiliser le rouge de crésol qui virera du jaune (teinte acide au début du titrage car $\text{pH} < \pu{7,2}$) au rouge (teinte basique quand $\text{pH} > \pu{8,8}$).
{{% /solution %}}

### Titrage conductimétrique

On envisage d’effectuer le titrage conductimétrique d’une solution $S’$ d’acide ascorbique dont la concentration molaire est de l’ordre de $\pu{6e-3 mol.L-1}$ par une solution d’hydroxyde de sodium de concentration $C’_B = \pu{1,00e-1 mol.L-1}$. On dispose de pipettes jaugées de $\pu{10,0 mL}$, $\pu{20,0 mL}$ et $\pu{25,0 mL}$ ainsi que de fioles jaugées de $\pu{50,0 mL}$, $\pu{100 mL}$, $\pu{200,0 mL}$ et $\pu{250,0 mL}$.

9. Expliquer pourquoi il n’est pas pertinent de titrer la solution d’acide ascorbique $S’$ par la solution d’hydroxyde de sodium de concentration molaire $C’_B$.

{{% solution "Réponse" %}}

{{% /solution %}}

10. À partir des réactifs proposés, établir un protocole expérimental permettant d’effectuer le titrage conductimétrique en précisant :
    - les éventuelles adaptations effectués au niveau des concentrations ;
    - le volume de solution d’acide ascorbique prélevé.

{{% solution "Réponse" %}}

{{% /solution %}}

11. Plusieurs allures de courbes modélisant ce titrage sont proposées ci-dessous. En argumentant, identifier la courbe qui peut correspondre au titrage conductimétrique de l’acide ascorbique par la solution d’hydroxyde de sodium.

<img src="/terminales-pc/chap-4/chap-4-13-1.png" alt="" width="">

{{% solution "Réponse" %}}

{{% /solution %}}

#### Données

- $pKe = -\log (K_e) = \pu{14,0}$ à 25&nbsp;°C.
- $K_e = \dfrac{ [\ce{H3O^+}]\cdot [\ce{HO^-}] }{ (C^\barcirc)^2 }$ avec $C^\barcirc = \pu{1,0 mol.L-1}$.
- Masses molaires atomiques : $M(\ce{H}) = \pu{1,0 g.mol-1}$ ; $M(\ce{C}) = \pu{12,0 g.mol-1}$ ; $M(\ce{O}) = \pu{16,0 g.mol-1}$.
- Conductivités molaires ioniques à 25&nbsp;°C : $\lambda(\ce{HO^–}) = \pu{19,8 mS.m2.mol-1}$ ; $\lambda(\ce{Na^+}) = \pu{5,01 mS.m2.mol-1}$ ; $\lambda(\ce{ion ascorbate A^-}) = \pu{2,5 mS.m2.mol-1}$.

## Annexe

- {{< remote "Fichier à rendre avec la copie" "/terminales-pc/chap-4/chap-4-13-2.pdf" >}}