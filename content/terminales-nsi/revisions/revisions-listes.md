---
title: "Revisions sur la structure de liste en Python"
subtitle: ""
author: ""
type: ""
date: 2023-09-06T06:01:13+04:00
draft: false
toc: false
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: false
---


## Exercice 1

Écrire une fonction qui reçoit comme argument une liste de nombres à virgule et recherche lequel est le plus grand et lequel est le plus petit.

La spécification de la fonction est la suivante :

```python
def minmax(liste: list[float]) -> tuple[float]:
    """
    Retourne un tuple constitué des valeurs minimale
    et maximale de la liste
    """
```

{{% solution "Solution" %}}

```python
def minmax(liste: list[float]) -> tuple[float]:
    """
    Retourne un tuple constitué des valeurs minimale
    et maximale de la liste
    """
    val_min = liste[0]
    val_max = liste[0]
    for i in range(1, len(liste) - 1):
        if liste[i] > val_max:
            val_max = liste[i]
        if liste[i] < val_min:
            val_min = liste[i]
    return val_min, val_max
```

{{% /solution %}}

## Exercice 2

Écrire une fonction qui reçoit comme argument une liste et détermine le nombre d'éléments dans la liste.
Ne pas utiliser la fonction `len` du langage.

La spécification de la fonction est la suivante :

```python
def longueur(liste: list[float]) -> int:
    """
    Retourne le nombre d'éléments dans la
    liste
    """
```

{{% solution "Solution" %}}

```python
def longueur(liste: list[float]) -> int:
    """
    Retourne le nombre d'éléments dans la
    liste
    """
    longueur = 0
    for i in range(len(liste)):
        longueur += 1
    return longueur
```

{{% /solution %}}

## Exercice 3

Écrire une fonction qui simule le tirage du Loto. Pour rappel, il s'agit de tirer aléatoirement 6 entiers compris entre 1 et 49.

**Remarque.** Un numéro ne peut apparaître qu'une seule fois. Il est donc nécessaire de stocker le résultat de chaque tirage dans une liste et de vérifier s'il est présent ou pas.

La spécification de la fonction est la suivante :

```python
def loto() -> list[int]:
    """
    Simule le tirage du Loto. retourne une liste de 6 entiers compris
    entre 1 et 49.
    """
```

{{% solution "Solution" %}}

```python
def loto() -> list[int]:
    """
    Simule le tirage du Loto. retourne une liste de 6 entiers compris
    entre 1 et 49.
    """
    tirages = []
    nbre_valeurs = 6
    while len(tirages) <= nbre_valeurs:
        tirage = randint(1, 49)
        if tirage not in tirages:
            tirages.append(tirage)
    return tirages
```

{{% /solution %}}

## Exercice 4

Écrire une fonction qui reçoit une liste de notes comprises entre 0 et 20 comme argument et retourne la moyenne de ces notes et le pourcentage de ces notes comprises dans les intervalles : [0, moy - 3], [moy - 3, moy + 3] et [moy + 3, 20] où moy est la valeur moyenne des notes.

La signature de la fonction est :

```python
def statistiques(notes: List[float]) -> Tuple[float]:
    """
    Détermine les statistiques des notes reçues 
    en argument : moyenne et notes comprises dans
    les intervalles [0, moy - 3[, [moy - 3, moy + 3[, 
    [moy + 3, 20]
    """
```

Cette fonction doit utiliser les deux fonctions de signature :

```python
def moyenne(liste_notes: List[float]) -> float:
    """
    Détermine la moyenne des notes reçues en 
    argument dans la liste passée en argument.
    """
```

et

```python
def nombre_dans_intervalle(liste: List[float], valeur_min: float, valeur_max: float) -> float:
    """
    Détermine le nombre de valeurs de liste 
    comprises dans l'intervalle [val_min, val_max[.
    """
```

## Exercice 5

Écrire une fonction qui, partir de deux points de l'espace à trois dimensions, calcule la distance euclidienne entre ces deux points.
**Remarque.** Les coordonnées d'un point sont stockées dans un tuple.

La spécification de la fonction est :

```python
def distance(pt1: tuple[float], pt2: tuple[float]) -> float:
    """
    Détermine la distance entre les points pt1 et 
    pt2.
    ERREUR si les dimensions des tuples ne 
    correspondent pas.
    """
```

## Exercice 6

Reprendre l'exercice précédent et considérer que les points appartiennent à un espace de dimension N (N étant potentiellement grand).

La spécification de la fonction est :

```python
def distanceN(pt1: Tuple[float], pt2: Tuple[float]) -> float:
    """
    Détermine la distance entre les points pt1 et 
    pt2.
    ERREUR si les dimensions des tuples ne 
    correspondent pas.
    """
```

{{% solution "Solution" %}}

```python
from math import sqrt

def distanceN(pt1: tuple[float], pt2: tuple[float]) -> float:
    """
    Détermine la distance entre les points pt1 et
    pt2.

    ERREUR si les dimensions des tuples ne
    correspondent pas.
    """
    if len(pt1) != len(pt2):
        raise Exception("Les dimensions ne correspondent pas !")

    carre_distance: float = 0
    for i in range(len(pt1)):
        carre_distance += (pt2[i] - pt1[i])**2

    return sqrt(carre_distance)
```

{{% /solution %}}

## Exercice 7

Écrire une fonction qui retourne une la table de multiplication de tous les nombres entiers compris entre 0 et n sous forme d'une liste de listes.

La spécification de la fonction est :

```python
def table_multiplication(n: int) -> list[list[int]]:
    """
    Détermine la table de multiplication de tous les 
    entiers compris entre 1 et n.
    
    >>> table_multiplication(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
```

{{% solution "Solution" %}}

```python

def table_multiplication(n: int) -> list[list[int]]:
    """
    Détermine la table de multiplication de tous les 
    entiers compris entre 1 et n.

    >>> table_multiplication(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
    table = []
    for i in range(1, n + 1):
        ligne = []
        for j in range(1, n + 1):
            ligne.append(i * j)
        table.append(ligne)
    return table
```

{{% /solution %}}
