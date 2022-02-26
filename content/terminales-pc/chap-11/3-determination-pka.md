---
title: "Détermination de la constante d'acidité du couple acide/base de l'acide méthanoïque"
subtitle: "Chapitre 12,3"
author: ""
type: ""
date: 2022-02-05T11:17:34+04:00
draft: false
toc: true
tags: ["Conductimétrie", "Constante d'équilibre", "Constante d'acidité"]
categories: ["Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif premier de cette séance est la détermination de la constante d'acidité du couple acide/base de l'acide méthanoïque.    
La méthode utilisée s'appuie sur une mesure de conductivité.


{{% note normal %}}

#### Acide méthanoïque

L'**acide méthanoïque** (appelé aussi **acide formique**) est le plus simple des acides carboxyliques. Sa formule chimique est $\ce{CH2O2}$ ou $\ce{HCOOH}$. Sa base conjuguée est l'**ion méthanoate** (**formiate**) de formule $\ce{HCOO-}$. Il s'agit d'un **acide faible** son $pK_a$ étant égal à 3,751 à $\pu{25 °C}$, qui se présente sous forme d'un liquide incolore à l'odeur pénétrante.

Dans la nature, on le trouve dans les glandes de plusieurs insectes de l'ordre des hyménoptères, comme les abeilles et les fourmis, mais aussi sur les poils qui composent les feuilles de certaines plantes de la famille des urticacées (orties). Son nom trivial formique vient du mot latin formica qui signifie fourmi, car il fut isolé pour la première fois par distillation de fourmis.

<div style="text-align: right;">
    <a href="https://fr.wikipedia.org/wiki/Acide_méthanoïque" target="_blank">Wikipedia</a>
</div>
{{% /note %}}


{{% note normal %}}

#### Constante d'équilibre, constante d'acidité d'un couple acide/base

Pour évaluer l'avancement d'une transformation dont la réaction chimique conduit à un état d'équilibre, on définit et utilise une grandeur **sans dimension** appelée **constante d'équilibre de la réaction** et notée $K$.    
*Pour une concentration apportée donnée, plus la valeur d'une constante d'équilibre est grande, plus l'état d'équilibre --- état final réel de la transformation --- se rapproche de l'état final hypothétique --- état d'avancement maximal dans lequel le réactif limitant a disparu.*

Dans le cas particulier de la réaction d'un acide faible avec l'eau 
$$ 
    \ce{AH + H_2O <=> A^- + H3O^+} 
$$
on appelle **constante d'acidité** $K_A$ la *constante d'équilibre* de cette réaction.   
Pour une concentration apportée donnée, plus la constante d'acidité $K_A$ est élevée, plus la dissociation de l'acide en solution est grande, et donc plus son comportement se rapproche de celui d'un acide fort.

Une constante d'acidité est **caractéristique** d'un couple acide/base $\ce{acide/base}$.       

Remarque 
: La constante d'équilibre d'une réaction (et donc la constante d'acidité d'un couple acide/base) est *une grandeur qui dépend de la température*. 

{{% /note %}}

## Protocole expérimental

- Étalonner le conductimètre.
- Mesurer la conductivité $\sigma_1$ d'une solution aqueuse $S_1$ d'acide méthanoïque de concentration molaire en soluté apporté $C_1 = \pu{5,0e-2 mol.L-1}$.
- Préparer une solution $S_2$ dont la concentration en acide méthanoïque est $C_2 = \pu{5,0e-3 mol.L-1}$.
- Mesurer la conductivité $\sigma_2$ de la solution aqueuse $S_2$.

{{% solution "Résultats expérimentaux" %}}

- $\sigma_1 = \pu{1,113e3 \mu S.cm-1}$
- $\sigma_2 = \pu{0,3206e3 \mu S.cm-1}$

{{% /solution %}}

## Exploitation


### Détermination de la concentration des ions dans la solution

{{% note normal %}}

#### Données

- $\lambda_{\ce{HCO2^-}} = \pu{5,46e-3 S.m2.mol-1} $
- $\lambda_{\ce{H3O^+}} = \pu{35,0e-3 S.m2.mol-1} $

{{% /note %}}

Dans un premier temps, on se concentre sur l'étude de la solution $S_1$.

1. Convertir la conductivité $\sigma_1$ en $\pu{S.m-1}$.
{{% solution "Réponse" %}}

- $\sigma_1 = \pu{1,113e-3 S.cm-1} = \pu{1,113e-1 S.m-1}$
- $\sigma_2 = \pu{0,321e-3 S.cm-1} = \pu{0,321e-1 S.m-1}$

{{% /solution %}}

2. Écrire l'équation de la réaction entre l'acide méthanoïque et l'eau.   
Cette réaction conduit quasiment instantanément le système à un état d'équilibre.

{{% solution "Réponse" %}}

$$
    \ce{HCO2H (aq) + H2O <=> HCO2^- (aq) + H3O^+} 
$$

{{% /solution %}}

3. Construire le tableau d'avancement de la transformation.

4. Quelle relation existe entre les grandeurs $n_{eq}(\ce{HCO2^-})$ et $n_{eq}(\ce{H3O^+})$&nbsp;?
{{% solution "Réponse" %}}

À l'équilibre, état final de la transformation, $n_{eq}(\ce{HCO2^-}) = x_f = x_{eq}$ et $n_{eq}(\ce{H3O^+}) = x_f = x_{eq}$. On a donc $n_{eq}(\ce{HCO2^-}) = n_{eq}(\ce{H3O^+})$.

{{% /solution %}}

5. En déduire la relation qui existe entre les grandeurs $[\ce{HCO2^-}]\{eq}$ et $[\ce{H3O^+}]\{eq}$.
{{% solution "Réponse" %}}

$\dfrac{n_{eq}(\ce{HCO2^-})}{V} = \dfrac{n_{eq}(\ce{H3O^+})}{V}$, donc $[\ce{HCO2^-}]\_{eq} = [\ce{H3O^+}]\_{eq}$.

{{% /solution %}}

6. Exprimer la conductivité $\sigma_1$ de la solution en fonction des entités présentes dans la solution à l'équilibre.
{{% solution "Réponse" %}}

$$
    \sigma_1 = \lambda_{\ce{HCO2^-}} [\ce{HCO2^-}]\_{eq} + \lambda_{\ce{H3O^+}} [\ce{H3O^+}]\_{eq}
$$

{{% /solution %}}

7. Déduire des questions précédentes l'expression de la concentration effective des ions oxonium dans la solution.
{{% solution "Réponse" %}}

Comme $[\ce{HCO2^-}]\_{eq} = [\ce{H3O^+}]\_{eq}$,
$$
    \sigma_1 = (\lambda_{\ce{HCO2^-}} + \lambda_{\ce{H3O^+}}) [\ce{H3O^+}]\_{eq}
    \iff
    [\ce{H3O^+}]\_{eq} = \dfrac{ \sigma_1 }{ \lambda_{\ce{HCO2^-}} + \lambda_{\ce{H3O^+}} }
$$

{{% /solution %}}

8. En déduire la valeur de la concentration effective des ions oxonium dans la solution en mole par litre.
{{% solution "Réponse" %}}
$
[\ce{H3O^+}]\_{eq} = \dfrac{ \pu{1,113e-1 S.m-1} }{ \pu{5,46e-3 S.m2.mol-1} + \pu{35,0e-3 S.m2.mol-1} } = \pu{2,75 mol.m-3} = \pu{2,75e-3 mol.L-1}
$
{{% /solution %}}

9. Quelle est la valeur de la concentration effective des ions méthanoate dans la solution&nbsp;?
{{% solution "Réponse" %}}

$[\ce{HCO2^-}]\_{eq} = [\ce{H3O^+}]\_{eq}$, donc $[\ce{HCO2^-}]\_{eq} = \pu{2,75e-3 mol.L-1}$.

{{% /solution %}}

### Constante d'acidité du couple de l'acide méthanoïque

10. Exprimer l'expression de la constante d'acidité du couple de l'acide méthanoïque.
{{% solution "Réponse" %}}

$$
K_A = \dfrac{[\ce{HCO2^-}]\_{eq} \cdot [\ce{H3O^+}]\_{eq}}{[\ce{HCO2H}]\_{eq} \cdot C^o}
$$

{{% /solution %}}

11. À partir du tableau d'avancement exprimer la quantité de matière d'acide méthanoïque dans l'état d'équilibre en fonction de la concentration apportée $C_1$, le volume $V$ de la solution et de la quantité de matière d'ions oxonium dans cet état.
{{% solution "Réponse" %}}

$ n_{eq}(\ce{HCO2H}) = n_{0}(\ce{HCO2H}) - x_{eq} $ donc $ n_{eq}(\ce{HCO2H}) = n_{0}(\ce{HCO2H}) -  n_{eq}(\ce{H3O^+})$. Comme $n_{0} = C_1 V$, $ n_{eq}(\ce{HCO2H}) = C_1 V -  n_{eq}(\ce{H3O^+})$.

{{% /solution %}}

12. En déduire la relation entre les concentrations, dans l'état d'équilibre, de l'acide méthanoïque et des ions oxonium.
{{% solution "Réponse" %}}

$ \dfrac{n_{eq}(\ce{HCO2H})}{V} = \dfrac{C_1 V}{V} -  \dfrac{n_{eq}(\ce{H3O^+})}{V}$, donc 
$ [\ce{HCO2H}]\_{eq} = C_1 - [\ce{H3O^+}]\_{eq} $

{{% /solution %}}

13. En déduire l'expression de la constante d'acidité du couple de l'acide méthanoïque en fonction de $C_1$ et $[\ce{H3O^+}]\_{eq}$.
{{% solution "Réponse" %}}

$$
K_A = \dfrac{[\ce{H3O^+}]\_{eq} \cdot [\ce{H3O^+}]\_{eq}}{(C_1 - [\ce{H3O^+}]\_{eq}) \cdot C^o} = \dfrac{[\ce{H3O^+}]\_{eq}^2 }{(C_1 - [\ce{H3O^+}]\_{eq}) \cdot C^o}
$$

{{% /solution %}}

14. Calculer la valeur de la constante d'acidité du couple de l'acide méthanoïque.
{{% solution "Réponse" %}}

$ K_A = \dfrac{(\pu{2,75e-3 mol.L-1})^2 }{(\pu{5,0e-2 mol.L-1} - \pu{2,75e-3 mol.L-1}) \cdot \pu{1,0 mol.L-1}} = \pu{1,51e-4} $

{{% /solution %}}


15. Mettre en commun l'ensemble des résultats obtenus par les $n$ groupes de la classe, calculer la valeur moyenne $K_{A_{moy}}$ (après avoir supprimé les résultats manifestement aberrants) puis l'incertitude de répétabilité $U(K_A)$.     
Exprimer finalement le résultat du mesurage sous la forme $K_{A_{moy}} \pm U(K_A)$.

Remarque
: Un fichier de travail se trouve à cette <a href="https://replit.com/@dlatreyte/Resultat-dun-mesurage-de-type-A#main.py" target="_blank">adresse</a>.

{{% solution "Réponse" %}}

- Valeurs obtenues par différents groupes : $\pu{1,55e-4}$, $\pu{1,57e-4}$, $\pu{1,51e-4}$, $\pu{1,56e-4}$, $\pu{1,60e-4}$, $\pu{1,56e-4}$, $\pu{1,53e-4}$.
- Si on choisit un taux de confiance de 95%, on obtient $K_A = \pu{(1,55 \pm 0,02)\cdot 10^{-4}}$.

{{% /solution %}}

16. Déterminer la valeur théorique de la constante d'acidité du couple de l'acide méthanoïque. La valeur déterminée lors de la manipulation est-elle en accord avec cette valeur&nbsp;?
{{% solution "Réponse" %}}

$K_{A_{theo}} = 10^{—\mathrm{pK}_A} = \pu{1,77e-4}$

L'intervalle trouvé expérimentalement est : $\pu{1,53e-4} \leq K_A \leq \pu{1,57e-4}$. Cet intervalle est trop petit pour contenir la valeur attendue.
{{% /solution %}}

17. Reprendre entièrement l'étude pour la solution $S_2$.     
**La valeur de la constante d'acidité dépend-elle de la concentration initiale en acide ?**
{{% solution "Réponse" %}}

- $
[\ce{H3O^+}]\_{eq} = \dfrac{ \pu{0,3206e-1 S.m-1} }{ \pu{5,46e-3 S.m2.mol-1} + \pu{35,0e-3 S.m2.mol-1} } = \pu{7,93e-1 mol.m-3} = \pu{7,93e-4 mol.L-1}
$

- $ 
K_A = \dfrac{(\pu{7,93e-4 mol.L-1})^2 }{(\pu{5,0e-3 mol.L-1} - \pu{7,93e-4 mol.L-1}) \cdot \pu{1,0 mol.L-1}} = \pu{1,49e-4} 
$


{{% note tip %}}


**La valeur de la constante d'acidité ne dépend pas de la concentration initiale en acide. Elle est spécifique à l'acide et ne dépend que de la température.**

{{% /note %}}

{{% /solution %}}