---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2021-11-21T05:54:29+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Écrire une fonction python appelée `nb_repetitions` qui prend en paramètres un élément `elt` et une liste `tab` et renvoie le nombre de fois où l’élément apparaît dans la liste.

#### Jeu de tests
```python
if __name__ == "__main__":
    assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
    assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
    assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0
```

{{% solution "Solution" %}}

```python
def nb_repetitions(elt: Union[int, float, str], tab: List) -> int:
    """
    Retourne le nombre de fois que elt apparaît dans tab.
    """
    nbre = 0
    for element in tab:
        if element == elt:
            nbre += 1
    return nbre

if __name__ == "__main__":
    assert nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]) == 3
    assert nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']) == 2
    assert nb_repetitions(12, [1, '! ', 7, 21, 36, 44]) == 0
```

{{% /solution %}}



## Exercice 2 (50% des points)

Pour rappel, la conversion d’un nombre entier positif en binaire peut s’effectuer à l’aide des divisions successives comme illustré ici&nbsp;:

<img src="/terminales-nsi/ece/sujet_21.png" alt="" width="45%" />

Voici une fonction python basée sur la méthode des divisions successives permettant de convertir un nombre entier positif en binaire&nbsp;:

```python
def binaire(a: int) -> str:
    bin_a = str(...)
    a = a ... 2
    while a ... :
        bin_a = ...(a ... 2) + ...
        a = ...
    return bin_a
```

#### Jeu de tests
```python
if __name__ == "__main__":
    assert binaire(0) == '0'
    assert binaire(1) == '1'
    assert binaire(2) == '10'
    assert binaire(4) == '100'
    assert binaire(77) == '1001101'
```

{{% solution "Solution" %}}

```python
def binaire(a: int) -> str:
    """
    Retourne la chaîne de caractères qui représente le codage de a en binaire.
    """
    bin_a = str(a % 2)
    a = a // 2
    while a >= 1:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a


if __name__ == "__main__":
    assert binaire(0) == '0'
    assert binaire(1) == '1'
    assert binaire(2) == '10'
    assert binaire(4) == '100'
    assert binaire(77) == '1001101'
``` 

{{% /solution %}}