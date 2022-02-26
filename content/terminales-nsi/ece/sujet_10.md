---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2021-10-27T18:39:50+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Écrire une fonction `maxi` qui prend en paramètre une liste `tab` de nombres entiers et renvoie un couple donnant le plus grand élément de cette liste, ainsi que l’indice de la première apparition de ce maximum dans la liste.

Remarque
: L'utilisation de la fonction `max` fournie avec le langage Python n'est pas autorisée.

Exemple :
```python
if __name__ == "__main__":
    assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
```

{{% solution "Corrigé" %}}

```python
from typing import List, Tuple


def maxi(tab: List[int]) -> Tuple[int]:
    """
    Retourne le plus grand élément de cette liste, ainsi que l’indice de la première apparition de ce maximum dans la liste.
    """
    val_max = tab[0]
    indice = 0

    for i in range(1, len(tab)):
        if tab[i] > val_max:
            val_max = tab[i]
            indice = i
    return val_max, indice

if __name__ == "__main__":
    assert maxi([1, 5, 6, 9, 1, 2, 3, 7, 9, 8]) == (9, 3)
```

{{% /solution %}}

## Exercice 2 (50% des points)

Cet exercice utilise des piles qui seront représentées en Python par des listes (type `list`). On rappelle que l’expression `T1 = list(T)` fait une copie de `T` indépendante de `T`, que l’expression `x = T.pop()` enlève le sommet de la pile `T` et le place dans la variable `x` et, enfin, que l’expression `T.append(v)` place la valeur `v` au sommet de la pile `T`.

Compléter le code Python de la fonction `positif` ci-dessous qui prend une pile `T` de nombres entiers en paramètre et qui renvoie la pile des entiers positifs dans le même ordre, sans modifier la variable `T`.

```python
def positif(T):
    T2 = ...(T)
    T3 = ...
    while T2 != []:
        x = ...
        if ... >= 0:
            T3.append(...)
    T2 = []
    while T3 != ...:
        x = T3.pop()
        ...
    print('T = ',T)
return T2
```

Exemple : 
```python
if __name__ == "__main__":
    T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
    assert positif(T) == [0, 5, 4, 10, 9]
```

{{% solution "Corrigé" %}}

```python
from typing import List, Tuple


def positif(T: List[int]) -> List[int]:
    """
    Retourne la pile des entiers positifs dans le même ordre, sans modifier la pile T.
    """
    T2 = list(T)
    T3 = []
    while T2 != []:
        x = T2.pop()
        if x >= 0:
            T3.append(x)
    T2 = []
    while T3 != []:
        x = T3.pop()
        T2.append(x)
    return T2


if __name__ == "__main__":
    T = [-1, 0, 5, -3, 4, -6, 10, 9, -8]
    assert positif(T) == [0, 5, 4, 10, 9]
``` 

{{% /solution %}}