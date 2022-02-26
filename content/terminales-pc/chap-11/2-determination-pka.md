---
title: "Détermination du $pK_A$ du couple acide/base de l'acide acétique"
subtitle: "Chapitre 12,2"
author: ""
type: ""
date: 2022-02-02T04:20:24+04:00
draft: false
toc: true
tags: ["Constante d'équilibre", "Constante d'acidité"]
categories: ["Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---

> L'objectif premier de cette séance est la détermination de la constante d'acidité du couple acide/base de l'acide acétique (éthanoïque).   
La méthode utilisée s'appuie sur des mesures de pH.

{{% note normal %}}

#### Acide éthanoïque (ou acide acétique)

L'acide éthanoïque est naturellement présent dans le vinaigre. Il lui donne son goût acide et son odeur piquante. C'est un *antiseptique* et un *désinfectant*. L'acide acétique pur est un liquide très faiblement conducteur et incolore.    
Il doit être manipulé avec soin en suivant les consignes de sécurité.    
Son acidité est due à sa capacité à perdre le proton de son groupe carboxyle, le transformant ainsi en ion acétate $\ce{CH_3COO^-}$. C'est un **acide faible**, son $pK_a$ étant égal à 4,76 à $\pu{25 °C}$.

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

-  Préparer sept mélanges des solutions $A$ d’acide éthanoïque $\ce{CH3COOH (aq)}$, de concentration apportée $C_A = \pu{1,00e-2 mol·L-1}$, et des solutions $B$ d’éthanoate de sodium $\ce{(Na+ (aq) + CH3COO- (aq))}$, de concentration apportée $C_B = \pu{1,00e-2 mol·L-1}$, en prélevant les volumes $V_A$ et $V_B$ indiqués dans le tableau ci-dessous.

- Étalonner le pH-mètre.

- Après avoir homogénéisé ces mélanges, mesurer le pH de chacun d’eux et reporter les valeurs sur le tableau ci-dessous.

<center>

| Mélange | $M_1$ | $M_2$ | $M_3$ | $M_4$ | $M_5$ | $M_6$ | $M_7$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $V_A$ (mL) | 5,0 | 10,0 | 20,0 | 25,0 | 30,0 | 40,0 | 45,0 |
| $V_B$ (mL) | 45,0 | 40,0 | 30,0 | 25,0 | 20,0 | 10,0 | 5,0 |
| pH |      |      |      |      |      |      |      |

</center>

## Exploitation

### Analyse de la partie expérimentale

1. Compléter la partie «&nbsp;Variables du problème&nbsp;», dans le fichier accessible à <a href="https://dlatreyte.github.io/jupyter-lite/lab?path=term-spe-pc%2FAcide-Base%2FConstante-acidite-acide-ethanoique-eleves.ipynb" target="_blank">cette adresse</a>. 

2. Compléter la partie «&nbsp;Détermination des valeurs de la variable $x$&nbsp;».     
Pour chaque solution, 
$$
    x = \log\left( \dfrac{V_B}{V_A} \right)
$$

3. Tracer l'évolution du pH en fonction de la variable $x$.    

4. Quelle fonction modélise le mieux cette évolution ?

5. Partie «&nbsp;Modélisation de l'évolution du pH&nbsp;».
    - Écrire, à partir de la réponse à la question précédente, l'expression de la fonction qui modélisera le mieux les données.
    - Analyser le code.
    - Compléter les deux instructions de tracé.
    - Faire afficher et relever les valeurs des paramètres de la modélisation.

### Modèle théorique

On a déjà vu que l'acide acétique et l'ion acétate réagissent très peu avec l'eau. On considère donc, 
- que la concentration en acide acétique est $C_A$ dans la solution $A$&nbsp;;
- que la concentration en ion acétate est $C_B$ dans la solution $B$&nbsp;;
- qu'après le mélange des solutions $A$ et $B$, les quantités de matière $n_A$ et $n_B$ introduites restent constantes.

6. Exprimer, en fonction des grandeurs $C_A$, $C_B$, $V_A$, $V_B$, les concentrations de $[\ce{CH3CO2H}]\_{eq}$ et $[\ce{CH3CO2^-}]\_{eq}$.

7. En déduire que 
$$
\log \left( \dfrac{[\ce{CH3CO2^-}]\_{eq}}{[\ce{CH3CO2H}]\_{eq}} \right) = \log\left( \dfrac{V_B}{V_A} \right)
$$

8. Établir la relation qui existe entre le pH de la solution et le $pK_A$ du couple $\ce{CH3CO2H / CH3CO2^-}$.

9. Montrer que le graphe obtenu à la question 5. est compatible avec la relation de la question 8.

10. En déduire la valeur du $pK_A$ du couple $\ce{CH3CO2H / CH3CO2^-}$.

11. Tracer le diagramame de prédominance du couple $\ce{CH3CO2H / CH3CO2^-}$.

{{% solution "Corrigé" %}}

{{% remote "Corrigé" "https://dlatreyte.github.io/jupyter-lite/lab?path=term-spe-pc%2FAcide-Base%2FConstante-acidite-acide-ethanoique.ipynb" %}}

{{% /solution %}}