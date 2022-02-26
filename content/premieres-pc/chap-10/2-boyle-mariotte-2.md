---
title: "Vérification de la loi de Boyle-Mariotte"
subtitle: "Chapitre 9,2"
author: ""
type: ""
date: 2021-02-28T13:36:55+04:00
draft: false
toc: true
tags: []
categories: ["Premières Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objet de ce document est de vérifier la relation de Boyle-Mariotte pour un gaz décrit par le modèle du gaz parfait.

{{% note warning %}}
Aucune manipulation n'étant possible, on utilisera lors de cette séance, l'application accessible {{< remote "à cette adresse" "https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_en.html" >}}
{{% /note %}}

1. Faire afficher par l'application la longueur d'un côté de l'enceinte. Cette enceinte a la forme d'un cube.

2. Introduire 300 particules dans l'enceinte. Choisir de conserver constante la température.

3. Pour une température de $\pu{300 K}$, faire varier la longueur d'un côté de $\pu{7 nm}$ à $\pu{15 nm}$.\
Relever à chaque fois la valeur de la pression (en Pa).

4. Entrer toutes ces valeurs dans le logiciel Graphical Analysis.

5. Ajouter une colonne calculée. Le calcul à effectuer est celui du volume de l'enceinte.

6. Afficher la courbe $P = f(V)$. Existe-t-il une relation de proportionnalité entre $P$ et $V$ ?

7. Ajouter une colonne calculée. Le calcul à effectuer est celui de l'inverse du volume de l'enceinte.

8. Afficher la courbe $P = g(\dfrac{1}{V})$. Existe-t-il une relation de proportionnalité entre $P$ et $\dfrac{1}{V}$ sur tout l'intervalle des volumes possibles (ou des pressions) ?

9. Si on se limite aux faibles pressions, existe-t-il une relation de proportionnalité ?

10. Pourquoi la proportionnalité n'intervient-elle que pour les faibles pressions ?

{{% note tip %}}
#### Modèle du gaz parfait

Le modèle du gaz parfait est constitue une tentative de description du comportement d'un gaz réel. Lors de cette modèlisation :
- *on néglige la structure interne des entités qui constituent le gaz ; elles sont considérées comme étant de points matériels*.
- *on néglige les interactions qui existent entre les entités qui constituent le gaz*. Ces entités n'interagissent donc qu'avec les parois du récipient qui contient le gaz.

Quatre paramètres (non indépendant entre eux) permettent de décrire un gaz parfait en équilibre (mécanique et thermique) : $P$ la pression (en pascal), $T$ la température (en kelvin), $V$ le volume (en mètre-cube) et $n$ la quantité de matière (en mole).
{{% /note %}}

{{% note warning %}}
Le modèle du gaz parfait ne décrit fidèlement le comportement d'un gaz réel qu'à *basse pression*.\
On utilise cependant régulièrement ce modèle en chimie.
{{% /note %}}


{{% note tip %}}
La loi de Boyle-Mariotte relie la *pression* et le *volume* d'un **gaz parfait** *à température constante*. Son expression mathématique est :
$$
    P\\, V = \text{cste}
$$
En d'autres termes, *maintenir la température constante pendant une augmentation de pression d'un gaz exige une diminution de volume*. Inversement, *la réduction de la pression du gaz passe par une augmentation de volume*.\
La valeur exacte de la constante n'a pas besoin d'être connue pour appliquer la loi entre deux volumes de gaz sous des pressions différentes, à la même température :
$$
    P_1\\, V_1 = P_2\\, V_2 
$$
{{% /note %}}