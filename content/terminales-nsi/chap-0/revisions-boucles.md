---
title: "Revisions sur les strucures de boucle en Python"
subtitle: ""
author: ""
type: ""
date: 2023-09-06T05:51:48+04:00
draft: false
toc: false
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: false
mathjax: true
---

# Travail à effectuer  

## Exercice 1

Écrire et exécuter une fonction qui retourne une chaîne de caractères formée par une suite des 10 premiers termes de la table de multiplication d'un entier a passé en argument.
La spécification de la fonction est :

```python
def multiplication(a: int) -> str:
    """
    Retourne une chaîne de caractères formées des 10 premiers
    nombres de la table de multiplication de a.
    
    >>> multiplication(7)
    '7 14 21 28 35 42 49 56 63 70 '
    """
```

## Exercice 2

Écrire et exécuter une fonction qui retourne une chaîne de caractères formée par une suite des 10 premiers termes de la table de multiplication d'un entier a passé en argument en signalant au passage (à l'aide d'un astérisque) ceux qui sont des multiples de 3.
La spécification de la fonction est :

```python
def multiplication_multiple_trois(a: int) -> str:
    """
    Retourne une chaîne de caractères formées des 10 premiers
    nombres de la table de multiplication de a en signalant au
    passage ceux qui sont des multiples de 3.
    
    >>> multiplication_multiple_trois(2)
    '2 4 6* 8 10 12* 14 16 18* 20 '
    >>> multiplication_multiple_trois(7)
    '7 14 21* 28 35 42* 49 56 63* 70 '
    """
```

## Exercice 3

Écrire et exécuter une fonction qui calcule les 50 premiers termes de la table de multiplication d'un nombre a passé en argument mais qui retourne une chaîne de caractères formée seulement par ceux qui sont des multiples de 7.
La spécification de la fonction est :

```python
def multiplication_multiple_sept(a: int) -> str:
    """
    Calcule les 50 premiers termes de la table de a mais retourne
    une chaîne de caractères contenant uniquement les multiples de 7.
    
    >>> multiplication_multiple_sept(2)
    '14 28 42 56 70 84 98 '
    >>> multiplication_multiple_sept(9)
    '63 126 189 252 315 378 441 '
    """
```

## Exercice 3

Écrire et exécuter une fonction qui calcule et retourne une chaîne de caractères formée de la liste des diviseurs du nombre passé en argument.
La spécification de la fonction est :

```python
def diviseurs(a: int) -> str:
    """
    Retourne une chaîne de caractères formée de la liste des diviseurs
    de a.
    
    >>> diviseurs(18)
    '18 9 6 3 2 1 '
    """
```

## Exercice 4

Écrire une fonction qui retourne une chaîne de caractère formée des 10 premiers termes de la table de multiplication de 1 à 10. Le caractère de passage à la ligne `\n` doit être utilisé afin de séparer les différentes tables (de 2, de 3, etc.).

**Remarque :** Utiliser deux boucles imbriquées.

La spécification de la fonction est :

```python3
def table_multiplication() -> str:
    """
    Retourne la table de multiplication des nombres de 1 à 10.
    """
```

**Remarque :** Afin de visualiser le résultat sous forme d'un tableau, utiliser l'instruction suivante, **dans la console**, pour tester la fonction :

```python
>>> print(table_multiplication())
```

## Exercice5

Écrire et exécuter une fonction qui demande 10 nombres à l'utilisateur et qui détermine lequel est le plus grand et lequel est le plus petit. Les deux résultats sont retournés au sein d'une unique chaîne de caractères.

**Remarque :** la fonction qui permet de récupérer *du texte* entré au clavier est `input` :

```python
valeur = float(input("Entrez votre valeur : "))
```

La specification de la fonction est :

```python
def plus_grand_plus_petit() -> str:
    """
    Demande à l'utilisateur d'entrer 10 valeurs et retourne une
    chaîne de caractères formée des deux valeurs max et min.
    """
```

## Exercice 6

Reprendre l'exercice précédent mais en faisant en sorte que le nombre de valeurs demandées à l'utilisateur soit passé en argument à la fonction.

## Exercice 7

Écrire et exécuter une fonction qui demande à l'utilisateur d'entrer 10
  notes et qui retourne la moyenne de ces notes.
La spécification de la fonction est :

```python
def moyenne() -> float:
    """
    Demande 10 notes à l'utilisateur et retourne la moyenne.
    """
```

## Exercice 8

Modifier le programme précédent de façon à ce que le nombre de notes à prendre en compte soit passé en argument de la fonction.

## Exercice 9

Modifier le programme précédent de façon à ce que l'utilisateur n'ait pas à indiquer le nombre de notes qu'il souhaite saisir. Une note négative terminer la saisie.

 **Remarque :** la fonction doit afficher le nombre de notes saisies, elle retourne donc une chaîne de caractères.

## Exercice 10

Écrire et exécuter une fonction qui simule un tirage du Loto (s'aider de l'exercice 12 du chapitre 02).
La spécification de la fonction est

```python
def loto_naif() -> str:
    """
    Retourne 6 entiers sélectionnés aléatoirement dans l'intervalle
    [1, 49].
    """
```

**Remarque.** Normalement, lorsqu'un numéro est tiré, il ne peut pas apparaître à nouveau. On acceptera cependant qu'un même numéro puisse apparaitre plusieurs fois puisqu'on ne connaît pas encore de structure de contrôle qui permet de facilement « stocker » plusieurs valeurs.

## Exercice 11

Écrire et exécuter une fonction qui tire au hasard un nombre entier compris entre 1 et 50 et demande à l'utilisateur de le deviner.
  
Cette fonction doit indiquer à l'utilisateur si sa tentative est trop grande ou trop petite et quitter dès l'instant où il a deviné le nombre en indiquant le nombre de tentatives.

**Remarque.** La fonction ne doit rien retourner, elle doit utiliser la fonction `print` pour *afficher* à l'écran les informations. Sa spécification est

```python
def devine() -> None:
    """
    Déterminer aléatoirement un nombre compris en 1 et 49 et demande à l'utilisateur
    de le deviner.
    La fonction affiche des messages qui aident l'utilisateur dans recherche et quitte
    dès que cette dernière est fructueuse.
    """
```

## Exercice 12

Écrire et exécuter une fonction qui affiche l'alphabet à l'endroit si elle reçoit l'argument `"croissant"` ou à l'envers si elle reçoit l'argument `"decroissant"`.
  
**Remarque.** On peut obtenir le code décimal d'un caractère à l'aide de la fonction `ord`. À l'opposé, le caractère correspondant à un entier naturel dans la table ASCII est obtenu (si possible) à l'aide de la fonction `chr`.

La spécification de la fonction est

```python
def alphabet(sens: str) -> str:
    """
    Retourne les lettres de l'alphabet en fonction de la chaîne de caractères
    passée en argument.
    Les valeurs possibles pour cet argument sont 'croissant' ou 'decroissant'.
    """
```

## Exercice 13

Écrire et exécuter une fonction qui détermine les *n* premiers termes de la « suite de Fibonacci » définie par :

$$
\begin{align*}
u_1 &= 1 \\\\
u_2 &= 1  \\\\
u_n &= u_{(n-1)} + u_{(n-2)} \text{ pour } n > 2
\end{align*}
$$

Cette fonction doit recevoir en argument la valeur de $n$ et retourner la suite de nombres sous forme de chaîne de caractères. Spécification de la fonction :

```python
def fibo(n: int) -> str:
    """
    Retourne les n premiers termes de la suite de Fibonacci.
    """
```
