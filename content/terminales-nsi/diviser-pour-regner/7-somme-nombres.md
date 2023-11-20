---
title: "Somme des $n$ nombres d'un tableau"
subtitle: ""
author: ""
type: ""
date: 2023-01-29T23:13:31+04:00
draft: false
toc: true
tags: ["Diviser pour régner", "Récursivité"]
categories: ["Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L’objectif de ce document est d’écrire et d’implémenter un algorithme s’appuyant sur le raisonnement « Diviser pour régner » qui permet de déterminer la somme des $n$ nombres (entiers) d'un tableau.

1. Écrire le code de fonction `somme1` dont la spécification est :

```python
def somme1(tab: List[float]) -> float:
    """
    Calcul de la somme des nombres éléments
    de tab.

    Algorithme : Récursivité enveloppée
    """
```

Penser à écrire un jeu de tests.
{{% solution "Réponse" %}}

```python
def somme1(tab: List[float]) -> float:
    """
    Calcul de la somme des nombres éléments
    de tab.

    Algorithme : Récursivité enveloppée
    """
    if len(tab) == 1:
        return tab[0]

    return tab[0] + somme1(tab[1:])

if __name__ == "__main__":
    tab = [1, 2, 3, 4, 5, 6, 7]
    n = tab[len(tab) - 1]
    assert somme1(tab) == n * (n + 1) // 2

    print("Done!")
```

{{% /solution %}}

2. Réfléchir à un algorithme utilisant le principe « Diviser pour régner » qui résoud le même problème.  
Écrire le code de la fonction `somme2` qui implémente cet algorithme.  
Tester cette fonction.

{{% solution "Réponse" %}}

```python
def somme2(tab: List[float]) -> float:
    """
    Calcul de la somme des nombres éléments
    de tab.

    Algorithme : Diviser pour Régner.
    """
    # Cas de base
    if len(tab) == 1:
        return tab[0]

    # Diviser
    m = len(tab) // 2

    somme_g = somme2(tab[:m])
    somme_d = somme2(tab[m:])

    # Régner
    total = somme_g + somme_d

    # Recombiner
    return total


if __name__ == "__main__":
    tab = [1, 2, 3, 4, 5, 6, 7]
    n = tab[len(tab) - 1]
    assert somme1(tab) == n * (n + 1) // 2
    assert somme2(tab) == n * (n + 1) // 2

    print("Done!")
```

{{% /solution %}}

3. Décrire le fonctionnement de l'algorithme pour la liste `[1, 2, 3, 4, 5, 6, 7]`.
{{% solution "Réponse" %}}

```bash
somme([1, 2, 3, 4, 5, 6, 7])
    somme_g = somme([1, 2, 3])
        somme_g = somme([1])
            retourne 1
        somme_d = somme([2, 3])
            somme_g = somme([2])
                retourne 2
            somme_d([3])
                retourne 3
            total = 5
            retourne 5
        total = 6
        retourne 6
    somme_d = somme([4, 5, 6, 7])
        somme_g = somme([4, 5])
            somme_g = somme([4])
                retourne 4
            somme_d = somme([5])
                retourne 5
            total = 9
            retourne 9
        somme_d = somme([6, 7])
            somme_g = somme([6])
                retourne 6
            somme_d = somme([7])
                retourne 7
            total = 13
            retourne 13
        total = 22
        retourne 22
    total = 28
    retourne 28
```

{{% /solution %}}
