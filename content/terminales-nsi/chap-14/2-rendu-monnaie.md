---
title: "Problème du rendu de monnaie"
subtitle: ""
author: ""
type: ""
date: 2021-02-28T05:28:54+04:00
draft: false
toc: true
tags: [ "Programmation dynamique"]
categories: ["Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Énoncé du problème

Un commerçant cherche à rendre la monnaie à ses clients **de façon optimale**, c'est-à-dire avec le **nombre minimal de pièces et de billets**.

Dans ce problème,

- On suppose que les clients ne donnent que des sommes entières en euros (pas de centimes pour simplifier) ;
- Les valeurs des pièces et billets à disposition sont : 1, 2, 5, 10, 20, 50, 100, 200 et 500. On suppose que l'on a autant d'exemplaires que nécessaire de chaque pièce et billet ;
- Dans la suite, afin de simplifier, on désigne par « pièces » à la fois les pièces et les billets.

## Algorithme glouton

Un client nous achète un objet qui coûte 53 euros. Il paye avec un billet de 200 euros. Il faut donc lui rendre 147 euros, par exemple un billet de 100, deux billets de 20, un billet de 5 et une pièce de 2.

Afin de **minimiser le nombre de pièces à rendre**, on peut suivre la stratégie suivante :

- On commence par rendre la pièce de plus grande valeur possible ;
- On déduit cette valeur de la somme (encore) à rendre ;
- On recommence, jusqu'à obtenir une somme nulle.

En procédant ainsi, **on résout le problème étape par étape** et **un choix optimal est effectué à chacune de ces étapes** (la pièce de plus grande valeur). *Cet algorithme fait parti de la catégorie des **algorithmes gloutons** : chercher la solution optimale à partir d'optima locaux.*

<!-- {{% note warning %}}
Le corrigé se trouve à cette adresse : {{< remote "https://repl.it/@dlatreyte/rendudemonnaie" "https://repl.it/@dlatreyte/rendudemonnaie" >}}
{{% /note %}} -->

1. Importer le module typing au début du fichier :

```python
from typing import List
```

2. Préparer le code suivant et étudier sa structure :

```python
if __name__ == "__main__":
    # valeurs des pièces
    pieces = [1, 2, 5, 10, 20, 50, 100]

    prix = int(input("Quel est le prix ? "))
    client = int(input("Combien le client donne-t-il ? "))

    a_rendre = somme_a_rendre(prix, client)
    comment = pieces_a_rendre(a_rendre, pieces)

    reponse = ["{} piece(s) de {}".format(comment[i], pieces[i]) for i in range(len(pieces))]
    print("Je dois rendre : {}".format(a_rendre))
    print("Je donne donc : {}".format(reponse))
```

3. Définir la fonction somme_a_rendre dont la spécification est :

```python
def somme_a_rendre(prix: int, montant_client: int) -> int:
    """
    Détermine la somme à rendre à partir du prix et du montant donné par
    le client.
    """
```

{{% solution "Réponse" %}}

```python
def somme_a_rendre(prix: int, montant_client: int) -> int:
    """
    Détermine la somme à rendre à partir du prix et
    du montant donné par le client.
    """
    return montant_client - prix
```

{{% /solution %}}

4. Définir la fonction pieces_a_rendre dont la spécification est :

```python
def pieces_a_rendre(somme: int, pieces: List[int]) -> List[int]:
    """
    Détermine les pièces (et leur nombre) à choisir pour rendre la somme
    passée en argument.
    Utilise la division euclidienne et le modulo de façon à pouvoir
    traiter tous les cas.
    """
```

{{% solution "Réponse" %}}

```python
def pieces_a_rendre(somme: int, pieces: List[int]) -> List[int]:
    """
    Détermine les pièces (et leur nombre) à choisir 
    pour rendre la somme passée en argument.
    
    Utilise la division euclidienne et le modulo de 
    façon à pouvoir traiter tous les cas.

    On reçoit : pieces = [1, 2, 5, 10, 20]
    On retourne : a_rendre = [x, z, y, a, b]
    """
    a_rendre = []

    for i in range(len(pieces) - 1, -1, -1):
        nbre = somme // pieces[i]
        somme = somme % pieces[i]
        a_rendre.append(nbre)

    return list(reversed(a_rendre))


def pieces_a_rendre_2(somme: int, pieces: List[int]):
    a_rendre = {}

    i = len(pieces) - 1
    while somme > 0:
        nbre = somme // pieces[i]
        somme = somme % pieces[i]
        a_rendre[pieces[i]] = nbre
        i = i - 1
    return a_rendre


def pieces_a_rendre_3(somme: int, pieces: List[int]) -> List[int]:
    a_rendre = [0] * len(pieces)

    i = len(pieces) - 1
    while somme > 0:
        nbre = somme // pieces[i]
        somme = somme % pieces[i]
        a_rendre[i] = nbre
        i = i - 1

    return list(reversed(a_rendre))
```

{{% /solution %}}

5. Appeler la fonction `main`.

{{% solution "Code complet" %}}

Le code se trouve à : {{< remote "cette adresse" "https://replit.com/@dlatreyte/Rendu-de-monnaie-Glouton#main.py" >}}

{{% /solution %}}

## Algorithme de force brute

1. On note $nb$ le nombre de pièces à rendre, prises dans la liste des pièces $p = [1, 2, 5, 10, 20, 50, 100, 200, 500]$, lorsque la somme à rendre est $x$.
Écrire la relation de récurrence que doit vérifier $nb$.
{{% solution "Réponse" %}}

$$
    nb(x) =
    \begin{cases}
    0 & \text{ si } x = 0\cr
    1 + nb(x - p[i]) & \text{ si } x - p[i] \geqslant 0  \cr
    \end{cases}
$$

{{% /solution %}}

2. En fait, on cherche le nombre minimal de pièces à rendre pour la somme $x$.
Adapter la relation de récurrence.
{{% solution "Réponse" %}}

$$
    nb(x) =
    \begin{cases}
    0 & \text{ si } x = 0\cr
    1 + \min{(nb(x - p[i]))} & \text{ si } x - p[i] \geqslant 0 \text{ et } i \in [0, \text{len}(p)[ \cr
    \end{cases}
$$

{{% /solution %}}

3. Écrire le schéma des appels récursifs pour $x=11$ et $p=[2,5,10]$.
{{% solution "Réponse" %}}

<img src="/terminales-nsi/chap-14/chap-14-2/chap-14-2-1.svg" alt="" width="100%" />

{{% /solution %}}

4. Indiquer l'avantage et l'inconvénient de l'algorithme par Brute Force.
{{% solution "Réponse" %}}

Cet algorithme retourne une solution optimale mais calcule plusieurs fois les mêmes valeurs. Il est donc inutilisable si la valeur à retourner est importante.

{{% /solution %}}

5. Réfléchir au code de la fonction dont la spécification est :

```python
def nb_rendre(a_rendre: int, pieces: List[int]) -> int:
    """
    Détermine le nombre minimal de pièces
    à rendre.

    Algorithme récursif.
    """
```

Écrire le code de cette fonction.
{{% solution "Réponse" %}}

```python
def nb_rendre(a_rendre: int, pieces: List[int]) -> int:
    """
    Détermine le nombre minimal de pièces
    à rendre.

    Algorithme récursif.
    """
    if a_rendre == 0:
        return 0

    nb_min = float('inf')

    for i in range(len(pieces)):
        if pieces[i] <= a_rendre:
            nb = 1 + nb_rendre(a_rendre - pieces[i], pieces)
            if nb <= nb_min:
                nb_min = nb

    return nb_min
```

{{% /solution %}}

6. Tester le code pour une somme à rendre de 13 puis de 130. Le résultat confirme-t-il la réponse à la question 4&nbsp;?

{{% solution "Code complet" %}}

Le code se trouve à : {{< remote "cette adresse" "https://replit.com/@dlatreyte/Rendu-de-monnaie-Brute-Force" >}}

{{% /solution %}}

## Programmation dynamique (mémoïsation)

1. 1. Rappeler quel est l'objectif de la programmation dynamique.
{{% solution "Réponse" %}}

{{% note tip %}}

La **programmation dynamique**, comme la méthode **diviser-pour-régner**, *résout des problèmes en combinant des solutions de sous-problèmes*.

- *Les algorithmes **diviser-pour-régner** partitionnent le problème en sous-problèmes indépendants qu’ils résolvent récursivement, puis combinent leurs solutions pour résoudre le problème initial*.
- *La **programmation dynamique**, quant à elle, peut s’appliquer même lorsque les sous-problèmes ne sont pas indépendants*, c’est-à-dire lorsque des sous-problèmes ont des sous-sous-problèmes communs.
Dans ce cas, un algorithme diviser-pour-régner fait plus de travail que nécessaire, en résolvant plusieurs fois le sous-sous-problème commun. Un algorithme de programmation dynamique **résout chaque sous-sous-problème une seule fois et mémorise sa réponse dans un tableau**, évitant ainsi le recalcul de la solution chaque fois que le sous-sous-problème est rencontré.

La programmation dynamique est, en général, appliquée aux **problèmes d’optimisation**. Dans ce type de problèmes, il peut y avoir de nombreuses solutions possibles. Chaque solution a une valeur, et on souhaite trouver une solution ayant la **valeur optimale** (**minimale** ou **maximale**). Une telle solution est une solution optimale au problème, et non pas la solution optimale, puisqu’il peut y avoir plusieurs solutions qui donnent la valeur optimale.

{{% /note %}}

{{% /solution %}}

2. Le manque d'efficacité de la méthode Brute-Force a pour origine les multiples redondants. Mettre en œuvre la méthode de mémoïsation afin d'améliorer l'efficacité du code de la fonction `nb_rendre`.

{{% solution "Code complet" %}}

Le code se trouve à : {{< remote "cette adresse" "https://replit.com/@dlatreyte/Rendu-de-monnaie-Programmation-dynamique-1" >}}

{{% /solution %}}

## Programmation dynamique (méthode tabulaire)

1. Rappeler quel est l'objectif de la programmation dynamique.
{{% solution "Réponse" %}}

{{% note tip %}}

La **programmation dynamique**, comme la méthode **diviser-pour-régner**, *résout des problèmes en combinant des solutions de sous-problèmes*.

- *Les algorithmes **diviser-pour-régner** partitionnent le problème en sous-problèmes indépendants qu’ils résolvent récursivement, puis combinent leurs solutions pour résoudre le problème initial*.
- *La **programmation dynamique**, quant à elle, peut s’appliquer même lorsque les sous-problèmes ne sont pas indépendants*, c’est-à-dire lorsque des sous-problèmes ont des sous-sous-problèmes communs.
Dans ce cas, un algorithme diviser-pour-régner fait plus de travail que nécessaire, en résolvant plusieurs fois le sous-sous-problème commun. Un algorithme de programmation dynamique **résout chaque sous-sous-problème une seule fois et mémorise sa réponse dans un tableau**, évitant ainsi le recalcul de la solution chaque fois que le sous-sous-problème est rencontré.

La programmation dynamique est, en général, appliquée aux **problèmes d’optimisation**. Dans ce type de problèmes, il peut y avoir de nombreuses solutions possibles. Chaque solution a une valeur, et on souhaite trouver une solution ayant la **valeur optimale** (**minimale** ou **maximale**). Une telle solution est une solution optimale au problème, et non pas la solution optimale, puisqu’il peut y avoir plusieurs solutions qui donnent la valeur optimale.

{{% /note %}}

{{% /solution %}}

2. On note $nb[i][j]$ le *nombre optimal de pièces à rendre pour une somme à rendre* $j$ et $i$ types de pièces.
Ce nombre est vérifie la relation de récurrence :
$$
    nb[i][j] =
    \begin{cases}
    0 & \text{ si } j = 0\cr
    0 & \text{ si } i = 0\cr
    min(nb[i-1][j] ; 1 + nb[i][j - \text{piece}[i]]) & \text{ si } j - \text{pieces}[i] \geqslant 0  \cr
    nb[i-1][j] & \text{ si } j - \text{pieces}[i] < 0 \cr
    \end{cases}
$$

    Justifier cette relation.

3. Représenter le tableau $nb$ pour une somme à rendre de 12 euros.

4. Quelle est le nombre de pièces optimal en utilisant la programmation dynamique ?

5. Écrire le code de la fonction `sol_dynamique` dont la spécification est :

```python
def construction_nb(somme: int, pieces: List[int]) -> List[List[int]]:
    """
    Construit le tableau dynamique nb définit par la relation de récurrence donnée.
    """
```

6. Quelle est la complexité de cet algorithme ?

<!--
7. À partir du tableau de la question 8, indiquer comment retrouver le découpage conduisant à la solution.
-->

7. Écrire la fonction `recherche_sol` dont la spécification est :

```python
def recherche_sol(somme: int, pieces: List[int], nb: List[List[int]]) -> Tuple[int, Dict[int: int]]:
    """
    Recherche la solution et toutes les pièces à rendre pour cette solution.
    La valeur retournée a pour forme (somme, {piece: nombre})
    """
```

{{% solution "Code complet" %}}

Le code se trouve à : {{< remote "cette adresse" "https://replit.com/@dlatreyte/Rendu-de-monnaie-dynamique-1" >}}

{{% /solution %}}
