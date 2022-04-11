---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2022-03-02T05:32:46+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Un professeur de NSI décide de gérer les résultats de sa classe sous la forme d’un dictionnaire&nbsp;:

- les clefs sont les noms des élèves ;
- les valeurs sont des dictionnaires dont les clefs sont les types d’épreuves et les valeurs sont les notes obtenues associées à leurs coefficients. Avec :

```python
resultats = {'Dupont':{'DS1' : [15.5, 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [13, 4],
                       'PROJET1' : [16, 3],
                       'DS3' : [14, 4]},
             'Durand':{'DS1' : [6 , 4],
                       'DM1' : [14.5, 1],
                       'DS2' : [8, 4],
                       'PROJET1' : [9, 3],
                       'IE1' : [7, 2],
                       'DS3' : [8, 4],
                       'DS4' :[15, 4]}}
```

L’élève dont le nom est Durand a ainsi obtenu au DS2 la note de 8 avec un coefficient 4. Le professeur crée une fonction `moyenne` qui prend en paramètre le nom d’un de ces élèves et lui renvoie sa moyenne arrondie au dixième.

Compléter le code du professeur ci-dessous :

```python
def moyenne(nom):
    if nom in ...:
        notes = ...
        total_points = ...
        total_coefficients = ...
        for ...  in ...:
            note , coefficient = ...
            total_points = ... + ... * ...
            total_coefficients = ... + ...
        return round( ... / total_coefficients , 1 )
    else:
        return -1
```

Remarque
: J'ai (DL) rendu cet exercice **un peu** plus difficile à résoudre que la version initiale proposée.

## Exercice 2 (50% des points)

Soit une image binaire représentée dans un tableau à 2 dimensions. Les éléments `M[i][j]`, appelés pixels, sont égaux soit à 0 soit à 1.

Une composante d’une image est un sous-ensemble de l’image constitué uniquement de 1 et de 0 qui sont côte à côte, soit horizontalement soit verticalement. Par exemple, les composantes de :
$$
M = \left( \begin{matrix}
   0 & 0 & 1 & 0 \cr
   0 & 1 & 0 & 1 \cr
   1 & 1 & 1 & 0 \cr
   0 & 1 & 1 & 0 \cr
\end{matrix}\right)
$$
sont
$$
M = \left( \begin{matrix}
   \color{blue}{0} & \color{blue}{0} & \color{hotpink}{1} & \color{orange}{0} \cr
   \color{blue}{0} & \color{orangered}{1} & \color{purple}{0} & \color{darkgray}{1} \cr
   \color{orangered}{1} & \color{orangered}{1} & \color{orangered}{1} & \color{green}{0} \cr
   \color{peru}{0} & \color{orangered}{1} & \color{orangered}{1} & \color{green}{0} \cr
\end{matrix}\right)
$$

On souhaite, à partir d’un pixel égal à 1 dans une image `M`, donner la valeur `val` à tous les pixels de la composante à laquelle appartient ce pixel.

La fonction `propager` prend pour paramètre une image `M`, deux entiers `i` et `j` et une valeur entière `val`. Elle met à la valeur `val` tous les pixels de la composante du pixel `M[i][j]` s’il vaut 1 et ne fait rien s’il vaut 0.
Par exemple, `propager(M,2,1,3)` donne :
$$
M = \left( \begin{matrix}
   \color{blue}{0} & \color{blue}{0} & \color{hotpink}{1} & \color{orange}{0} \cr
   \color{blue}{0} & \color{orangered}{3} & \color{purple}{0} & \color{darkgray}{1} \cr
   \color{orangered}{3} & \color{orangered}{3} & \color{orangered}{3} & \color{green}{0} \cr
   \color{peru}{0} & \color{orangered}{3} & \color{orangered}{3} & \color{green}{0} \cr
\end{matrix}\right)
$$

Compléter le code récursif de la fonction `propager` donné ci-dessous et écrire un programme qui teste cette fonction.

```python
def propager(M, i, j, val):
    if M[i][j]== ...:
        return None

    M[i][j] = val

    # l'élément en haut fait partie de la composante
    if ((i - 1) >= 0 and M[i - 1][j] == ...):
        propager(M, i - 1, j, val)

    # l'élément en bas fait partie de la composante
    if ((...) < len(M) and M[i + 1][j] == 1):
        ...(M, ..., j, val)

    # l'élément à gauche fait partie de la composante
    if ((...) >= 0 and M[i][j - 1] == 1):
        propager(M, i, ..., val)

    # l'élément à droite fait partie de la composante
    if ((...) < len(M) and M[i][j + 1] == 1):
        ...(M, i, ..., val)
```
