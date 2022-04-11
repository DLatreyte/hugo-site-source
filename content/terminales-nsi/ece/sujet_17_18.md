---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2022-04-10T22:33:49+04:00
draft: true
toc: true
tags: []
categories: []
image: ""
solution_est_visible: false
auto_numbering: true
---

## Exercice 1 (1/3 des points)

Écrire une fonction `recherche` qui prend en paramètres un tableau `tab` de nombres entiers triés par ordre croissant et un nombre entier `n`, et qui effectue une recherche dichotomique du nombre entier `n` dans le tableau non vide `tab`.
Cette fonction doit renvoyer un indice correspondant au nombre cherché s’il est dans le tableau, -1 sinon.

## Exercice 2 (1/3 des points)

On considère la fonction `separe` ci-dessous qui prend en argument un tableau `tab` dont les éléments sont des 0 et des 1 et qui sépare les 0 des 1 en plaçant les 0 en début de tableau et les 1 à la suite.

```python
def separe(tab): 
    i = 0
    j = ...
    while i < j :
        if tab[i] == 0:
            i = ...
        else :
            tab[i], tab[j] = ...
            j = ...
return tab
```

Compléter la fonction `separe` ci-dessus.

#### Jeu de tests

```python
assert separe([1, 0, 1, 0, 1, 0, 1, 0]) == [0, 0, 0, 0, 1, 1, 1, 1]
assert separe([1, 0, 0, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0]) == [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
```

## Exercice 3 (1/3 des points)

On considère la fonction `insere` ci-dessous qui prend en argument un entier `a` et un tableau `tab` d'entiers triés par ordre croissant. Cette fonction insère la valeur `a` dans le tableau et renvoie le nouveau tableau. Les tableaux seront représentés sous la forme de listes python.

```python
def insere(a, tab):
    l = list(tab)  #l contient les mêmes éléments que tab
    l.append(a)
    i = ...
    while a < ... and ... >= ... :
      l[i + 1] = ...
      l[i] = a
      i = ...
return l
```

Compléter la fonction `insere` ci-dessus.

#### Jeu de tests

```python
assert insere(3,[1,2,4,5]) == [1, 2, 3, 4, 5]
assert insere(10,[1,2,7,12,14,25]) ==  [1, 2, 7, 10, 12, 14, 25]
assert insere(1,[2,3,4]) == [1, 2, 3, 4]
```
