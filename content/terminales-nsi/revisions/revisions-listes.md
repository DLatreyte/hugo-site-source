---
title: "Révisions sur la structure de liste en Python"
subtitle: ""
date: 2023-09-06T06:01:13+04:00
draft: false
toc: false
tags: []
categories: []
solution_est_visible: true
auto_numbering: false
weight: 9900
---

{{< note goal >}}
Revoir la structure de liste (parcours, construction, test d'appartenance) et la structure de tuple, qui permet de retourner plusieurs valeurs ou de représenter un point.
{{< /note >}}

Sans exécuter le programme suivant, prévoir ce qu'il affiche, puis vérifier.

```python
nombres = [4, 7, 1]
nombres.append(9)
print(len(nombres), nombres[1], nombres[-1])
```

{{< solution "Réponse" >}}

Le programme affiche `4 7 9`. Après `append`, la liste vaut `[4, 7, 1, 9]` et contient 4 éléments. Les indices commencent à 0 : `nombres[1]` est le **deuxième** élément, 7. L'indice $-1$ désigne le dernier élément, 9.

{{< /solution >}}

## Exercice 1

Écrire une fonction qui reçoit comme argument une liste de nombres à virgule et recherche lequel est le plus grand et lequel est le plus petit.

La spécification de la fonction est la suivante :

```python
def minmax(liste: list[float]) -> tuple[float, float]:
    """
    Retourne un tuple constitué des valeurs minimale
    et maximale de la liste
    """
```

{{< solution "Solution" >}}

```python
def minmax(liste: list[float]) -> tuple[float, float]:
    """
    Retourne un tuple constitué des valeurs minimale
    et maximale de la liste
    """
    val_min = liste[0]
    val_max = liste[0]
    for valeur in liste[1:]:
        if valeur > val_max:
            val_max = valeur
        if valeur < val_min:
            val_min = valeur
    return val_min, val_max
```

{{< /solution >}}

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

{{< solution "Solution" >}}

```python
def longueur(liste: list[float]) -> int:
    """
    Retourne le nombre d'éléments dans la
    liste
    """
    compteur = 0
    for _ in liste:
        compteur += 1
    return compteur
```

{{< /solution >}}

## Exercice 3

Écrire une fonction qui simule le tirage du Loto. Pour rappel, il s'agit de tirer aléatoirement 6 entiers compris entre 1 et 49.

**Remarque.** Un numéro ne peut apparaître qu'une seule fois. Il est donc nécessaire de stocker le résultat de chaque tirage dans une liste et de vérifier s'il est présent ou pas.

{{< note tip "Coup de pouce" >}}
On ne sait pas combien de tirages seront nécessaires, puisqu'un numéro déjà sorti est rejeté : la boucle est une boucle `while`. Elle s'arrête quand la liste contient 6 numéros. L'opérateur `in` teste si une valeur est déjà dans la liste.
{{< /note >}}

La spécification de la fonction est la suivante :

```python
def loto() -> list[int]:
    """
    Simule le tirage du Loto. Retourne une liste de 6 entiers différents
    compris entre 1 et 49.
    """
```

{{< solution "Solution" >}}

```python
from random import randint


def loto() -> list[int]:
    """
    Simule le tirage du Loto. Retourne une liste de 6 entiers différents
    compris entre 1 et 49.
    """
    tirages: list[int] = []
    nbre_valeurs = 6
    while len(tirages) < nbre_valeurs:
        tirage = randint(1, 49)
        if tirage not in tirages:
            tirages.append(tirage)
    return tirages
```

{{< /solution >}}

## Exercice 4

Écrire une fonction qui reçoit comme argument une liste non vide de notes comprises entre 0 et 20, et qui retourne la moyenne de ces notes ainsi que les pourcentages de notes comprises dans les intervalles $[0, moy - 3[$, $[moy - 3, moy + 3[$ et $[moy + 3, 20]$, où $moy$ est la valeur moyenne des notes.

La spécification de la fonction est :

```python
def statistiques(notes: list[float]) -> tuple[float, float, float, float]:
    """
    Retourne la moyenne des notes (liste non vide) et les pourcentages
    de notes comprises dans les intervalles [0, moy - 3[,
    [moy - 3, moy + 3[ et [moy + 3, 20].

    >>> statistiques([12, 15, 8, 14, 6, 17])
    (12.0, 33.33333333333333, 33.33333333333333, 33.33333333333333)
    """
```

Cette fonction doit utiliser les deux fonctions de signature :

```python
def moyenne(liste_notes: list[float]) -> float:
    """
    Détermine la moyenne des notes reçues en
    argument dans la liste passée en argument.
    """
```

et

```python
def nombre_dans_intervalle(
    liste: list[float], valeur_min: float, valeur_max: float
) -> int:
    """
    Détermine le nombre de valeurs de liste
    comprises dans l'intervalle [valeur_min, valeur_max[.
    """
```

{{< note tip "Coup de pouce" >}}
Les trois intervalles se suivent sans se chevaucher et couvrent toutes les notes. Pour les deux premiers, on utilise `nombre_dans_intervalle`. Pour le dernier, fermé à droite, il suffit de retirer du nombre total de notes celles déjà comptées. Un pourcentage s'obtient en divisant par le nombre total de notes, puis en multipliant par 100.
{{< /note >}}

{{< solution "Solution" >}}

```python
def moyenne(liste_notes: list[float]) -> float:
    """
    Détermine la moyenne des notes reçues en
    argument dans la liste passée en argument.
    """
    total = 0.0
    for note in liste_notes:
        total += note
    return total / len(liste_notes)


def nombre_dans_intervalle(
    liste: list[float], valeur_min: float, valeur_max: float
) -> int:
    """
    Détermine le nombre de valeurs de liste
    comprises dans l'intervalle [valeur_min, valeur_max[.
    """
    compteur = 0
    for valeur in liste:
        if valeur_min <= valeur < valeur_max:
            compteur += 1
    return compteur


def statistiques(notes: list[float]) -> tuple[float, float, float, float]:
    """
    Retourne la moyenne des notes (liste non vide) et les pourcentages
    de notes comprises dans les intervalles [0, moy - 3[,
    [moy - 3, moy + 3[ et [moy + 3, 20].

    >>> statistiques([12, 15, 8, 14, 6, 17])
    (12.0, 33.33333333333333, 33.33333333333333, 33.33333333333333)
    """
    moy = moyenne(notes)
    nbre_notes = len(notes)
    bas = nombre_dans_intervalle(notes, 0, moy - 3)
    milieu = nombre_dans_intervalle(notes, moy - 3, moy + 3)
    haut = nbre_notes - bas - milieu
    return (
        moy,
        bas / nbre_notes * 100,
        milieu / nbre_notes * 100,
        haut / nbre_notes * 100,
    )
```

Avec les notes de l'exemple, la moyenne vaut 12 : les intervalles sont $[0, 9[$, $[9, 15[$ et $[15, 20]$. On y trouve respectivement 8 et 6, puis 12 et 14, puis 15 et 17, soit deux notes sur six dans chacun.

{{< /solution >}}

## Exercice 5

Écrire une fonction qui, à partir de deux points de l'espace à trois dimensions, calcule la distance euclidienne entre ces deux points.
**Remarque.** Les coordonnées d'un point sont stockées dans un tuple.

La spécification de la fonction est :

```python
def distance(
    pt1: tuple[float, float, float], pt2: tuple[float, float, float]
) -> float:
    """
    Détermine la distance entre les points pt1 et pt2.

    >>> distance((0, 0, 0), (1, 2, 2))
    3.0
    """
```

{{< solution "Solution" >}}

```python
from math import sqrt


def distance(
    pt1: tuple[float, float, float], pt2: tuple[float, float, float]
) -> float:
    """
    Détermine la distance entre les points pt1 et pt2.

    >>> distance((0, 0, 0), (1, 2, 2))
    3.0
    """
    x1, y1, z1 = pt1
    x2, y2, z2 = pt2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
```

Le déballage `x1, y1, z1 = pt1` donne un nom à chaque coordonnée, ce qui rend la formule lisible.

{{< /solution >}}

## Exercice 6

Reprendre l'exercice précédent et considérer que les points appartiennent à un espace de dimension $N$ ($N$ étant potentiellement grand). Si les deux points n'ont pas le même nombre de coordonnées, la fonction lève une erreur avec l'instruction `raise ValueError("Les dimensions ne correspondent pas !")`.

La spécification de la fonction est :

```python
def distance_n(pt1: tuple[float, ...], pt2: tuple[float, ...]) -> float:
    """
    Détermine la distance entre les points pt1 et pt2.
    Lève une erreur ValueError si les dimensions des tuples
    ne correspondent pas.
    """
```

{{< solution "Solution" >}}

```python
from math import sqrt


def distance_n(pt1: tuple[float, ...], pt2: tuple[float, ...]) -> float:
    """
    Détermine la distance entre les points pt1 et pt2.
    Lève une erreur ValueError si les dimensions des tuples
    ne correspondent pas.
    """
    if len(pt1) != len(pt2):
        raise ValueError("Les dimensions ne correspondent pas !")

    carre_distance: float = 0
    for x1, x2 in zip(pt1, pt2):
        carre_distance += (x2 - x1) ** 2

    return sqrt(carre_distance)
```

{{< /solution >}}

## Exercice 7

Écrire une fonction qui retourne la table de multiplication de tous les nombres entiers compris entre 1 et n sous forme d'une liste de listes.

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

{{< solution "Solution" >}}

```python
def table_multiplication(n: int) -> list[list[int]]:
    """
    Détermine la table de multiplication de tous les
    entiers compris entre 1 et n.

    >>> table_multiplication(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
    table: list[list[int]] = []
    for i in range(1, n + 1):
        ligne: list[int] = []
        for j in range(1, n + 1):
            ligne.append(i * j)
        table.append(ligne)
    return table
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- lire un élément d'une liste à partir de son indice, y compris avec un indice négatif ;
- parcourir une liste par ses éléments ou par ses indices ;
- construire une liste avec `append`, et une liste de listes ;
- tester la présence d'une valeur dans une liste avec `in` ;
- retourner plusieurs valeurs grâce à un tuple, et déballer un tuple ;
- lever une erreur `ValueError` quand les arguments ne respectent pas la spécification.
{{< /note >}}
