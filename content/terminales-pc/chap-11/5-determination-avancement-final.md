---
title: "L'acide benzoïque, un conservateur alimentaire"
subtitle: "Chapitre 12,5"
author: ""
type: ""
date: 2021-01-30T21:29:18+04:00
draft: false
toc: true
tags: []
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de ce travail est la détermination de l'avancement final d'une transformation non totale à l'aide d'un langage de programmation.

## Documents

L'acide benzoïque, de formule chimique $\ce{C6H5COOH}$ est un acide carboxylique aromatique dérivé du benzène. Il est utilisé comme conservateur alimentaire et est naturellement présent dans certaines plantes. C'est par exemple l'un des principaux constituants de la gomme benjoin, utilisée dans des encens dans les églises de Russie et d'autres communautés orthodoxes. Bien qu'étant un acide faible, l'acide benzoïque n'est que peu soluble dans l'eau du fait de la présence du cycle benzénique apolaire.\
On trouve de l'acide benzoïque dans les plantes alimentaires :
- en quantité notable dans le canneberge d'Amérique11 (Vaccinium macrocarpon) : $\pu{48,10 mg/100 ml}$ ;
- dans une moindre mesure dans la poudre de cacao (Theobroma cacao) : $\pu{0,06 mg/100 ml}$.

Parmi les principaux composés qui dérivent de l'acide benzoïque, on peut citer l'acide salicylique et l'acide acétylsalicylique plus connu sous le nom d'aspirine.\
En tant qu'additif alimentaire, il est référencé en Europe sous le code E210.\
Au-dessus de 370&nbsp;°C, il se décompose en formant du benzène et du dioxyde de carbone.\
L'acide benzoïque a une odeur forte et est facilement inflammable.

Données
: - **Solubilité** dans l'eau à 20&nbsp;°C : $\pu{2,9 g.L-1}$, soluble dans le chloroforme, l'éthanol et l'acétone ;
- $\text{pK}\_A (\ce{C6H5CO2H/C6H5CO2^-}) = \pu{4,2}$ ;
- $M(\ce{C6H5CO2H}) = \pu{122,1 g.mol-1}$.

<div style="text-align: right;">
   <a href="https://fr.wikipedia.org/wiki/Acide_benzoïque" target="_blank">Page Wikipedia</a>
</div>

## Travail

1. Écrire l’équation de la réaction entre l’acide benzoïque et l’eau. 
{{% solution "Réponse" %}}
$\ce{C6H5CO2H (aq) + H2O <=> C6H5CO2^- (aq) + H3O+ }$
{{% /solution %}}

2. Déterminer la concentration molaire apporté $c\_A$ d'acide benzoïque dans une solution saturée en acide benzoïque.
{{% solution "Réponse" %}}
La solubilité $s$ est la masse maximale que l'on peut dissoudre dans un litre de solution. Si on essaie de dissoudre une masse plus grande, on obtient une solution saturée (la concentration massique n'augmente donc pas). La concentration molaire apportée d'acide dans la solution est donc $c\_A = \dfrac{s}{M}$ où $M$ est la masse molaire de l'acide benzoïque.

**A.N.** $c\_A = \dfrac{\pu{2,9 g.L-1}}{\pu{122,1 g.mol-1}} = \pu{2,4e-2 mol.L-1}$.
{{% /solution %}}

3. Déterminer l’avancement maximal $x\_{max}$ de la réaction de l’acide benzoïque avec l’eau dans un volume $V = \pu{40 mL}$ de solution saturée. 
{{% solution "Réponse" %}}
L'utilisation d'un tableau d'avancement permet de conclure que $n\_0(\ce{C6H5CO2H}) - x\_{max} = 0 \iff x\_{max} = n\_0(\ce{C6H5CO2H}) = c\_A \cdot V$.

**A.N.** $x\_{max} = \pu{2,4e-2 mol.L-1} \times \pu{40e-3 L} = \pu{9,5e-4 mol}$.
{{% /solution %}}

4. Cette solution a un pH de 2,9. Déterminer l’avancement final $x\_f$, puis le taux d’avancement final $\tau$ de la réaction.
{{% solution "Réponse" %}}
- L'utilisation d'un tableau d'avancement permet de conclure que $x\_f = n\_f(\ce{H3O+}) = C^o \cdot 10^{-\text{pH}} \cdot V$.

   **A.N.** $x\_f = \pu{1,0} \times 10^{-\pu{2,9}} \times \pu{40e-3 L} = \pu{5,0e-5 mol}$.

- $\tau = \dfrac{x\_f}{x\_{max}} = \dfrac{\pu{5,0e-5 mol}}{\pu{9,5e-4 mol}} = \pu{5,3e-2}$ L'avancement final ne représente que 5,3% de l'avancement maximal.
{{% /solution %}} 

5. Montrer qu'on peut exprimer la constante d'acidité $K\_A$ sous la forme 
$$
    K\_A = \dfrac{c\_A \cdot \tau^2}{C^o \\, (1 - \tau)}
$$


6. Calculer la valeur de $\tau$ et la comparer le résultat obtenu avec la valeur trouvée à la question 4.

7. Écrire un programme en Python qui calcule les racines d'un polynôme du second degré.\
Il doit, en particulier :
   - demander à l'utilisateur la valeur du $K\_A$ ;
   - demander à l'utilisateur la valeur de $c\_A$ ;
   - calculer le discriminant $\Delta$ ;
   - calculer, en fonction de la valeur du discriminant, la valeur des racines si elles existent.

{{% note normal %}}
- Affichage du contenu d'une variable à l'écran en Python
```python
print("Première racine : {}".format(variable))
```
- Demande d'une information à l'utilisateur en Python
```python
Ka = float(input("Entrer la valeur du Ka : "))
```

**Remarque :** La fonction `input` retourne toujours une chaîne de caractères. Lorsque l'information est un nombre, il faut transformer la chaîne de caractères. Ici, on utilise la fonction `float`.

- Structure conditionnelle en Python :
```python
if condition_1 :
    faire si condition_1 est vérifiée
elif condition_2:
    faire si condition_1 n est pas vérifiée et condition_2 est verifiée
else:
    faire si aucune condition n est vérifiée
```
{{% /note %}}