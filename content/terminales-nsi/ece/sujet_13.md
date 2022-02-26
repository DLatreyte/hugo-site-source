---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2022-01-12T07:34:41+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Écrire une fonction `tri_selection` qui prend en paramètre une liste `tab` de nombres entiers et qui renvoie le tableau trié par ordre croissant.

On utilisera l’algorithme suivant&nbsp;:

- on recherche le plus petit élément du tableau, et on l'échange avec l'élément d'indice 0&nbsp;;
- on recherche le second plus petit élément du tableau, et on l'échange avec l'élément d'indice 1&nbsp;;
- on continue de cette façon jusqu'à ce que le tableau soit entièrement trié.

#### Jeu de tests possible

```python
assert tri_selection([1, 52, 6, -9, 12]) == [-9, 1, 6, 12, 52]
```

{{% solution "Corrigé" %}}

```python
from typing import List


def tri_selection(tab: List[float]) -> List[float]:
    """
    Tri sélection avec l'algorithme imposé 
    par l'énoncé.
    """
    for i in range(0, len(tab) - 1):
        val_min = tab[i]
        for j in range(i + 1, len(tab)):
            if tab[j] < val_min:
                val_min = tab[j]  # valeur minimale
                i_min = j  # indice du minimum
        if val_min != tab[i]:
            tab[i_min] = tab[i]
            tab[i] = val_min

    return tab


def main():
    assert tri_selection([1, 52, 6, -9, 12]) == [-9, 1, 6, 12, 52]


main()
```

{{% /solution %}}

## Exercice 2 (50% des points)

Le jeu du «&nbsp;plus ou moins&nbsp;» consiste à deviner un nombre entier choisi entre 1 et 99. 

Un élève de NSI décide de le coder en langage Python de la manière suivante :

- le programme génère un nombre entier aléatoire compris entre 1 et 99&nbsp;;
- si la proposition de l’utilisateur est plus petite que le nombre cherché, l’utilisateur en est averti. Il peut alors en tester un autre&nbsp;;
- si la proposition de l’utilisateur est plus grande que le nombre cherché, l’utilisateur en est averti. Il peut alors en tester un autre&nbsp;;
- si l’utilisateur trouve le bon nombre en 10 essais ou moins, il gagne&nbsp;;
- si l’utilisateur a fait plus de 10 essais sans trouver le bon nombre, il perd.

**Remarque :** La fonction `randint` est utilisée. Si `a` et `b` sont des entiers, `randint(a,b)` renvoie un nombre entier compris entre `a` et `b` (inclus).

Compléter le code ci-dessous et le tester :
```python
from random import randint


def plus_ou_moins():
    nb_mystere = randint(1, ....)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = ....

    while nb_mystere != .... and compteur < ....:
        compteur = .... + ....
        if nb_mystere .... nb_test:
            nb_test = ....(input("Trop petit ! Testez encore : "))
        else:
            nb_test = ....(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", ....)
        print("Nombre d'essais: ", ....)
    else:
        print("Perdu ! Le nombre était ", ....)
``` 

{{% solution "Corrigé" %}}

```python
from random import randint


def plus_ou_moins():
    nb_mystere = randint(1, 99)
    nb_test = int(input("Proposez un nombre entre 1 et 99 : "))
    compteur = 1

    while nb_mystere != nb_test and compteur < 10:
        compteur = compteur + 1
        if nb_mystere > nb_test:
            nb_test = int(input("Trop petit ! Testez encore : "))
        else:
            nb_test = int(input("Trop grand ! Testez encore : "))

    if nb_mystere == nb_test:
        print("Bravo ! Le nombre était ", nb_mystere)
        print("Nombre d'essais: ", compteur)
    else:
        print("Perdu ! Le nombre était ", nb_mystere)
```

{{% /solution %}}
