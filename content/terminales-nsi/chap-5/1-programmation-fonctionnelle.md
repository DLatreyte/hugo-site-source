---
title: "Programmation Fonctionnelle"
subtitle: "Chapitre 5,1"
author: ""
type: ""
date: 2020-10-06T03:49:30+04:00
draft: false
toc: true
tags: ["Programmation fonctionnelle", "List Comprehension", "Récursivité"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Qu'est-ce que la programmation fonctionnelle&nbsp;?

S'il n'est pas facile de répondre précisément à cette question, on peut essayer de mettre en évidence les idées que le paradigme fonctionnel promeut&nbsp;:

- Les fonctions doivent être des **objets de première classe**, c'est à dire que *les fonctions doivent pouvoir être passées comme arguments à une fonction, les fonctions doivent aussi pouvoir être retournées par une fonction*.

- Les fonctions doivent (le plus possible) être **pures**, c'est à dire ne *générer aucun effet de bord*.

- La *manipulation de variable doit être la plus limitée possible*&nbsp;: il est *possible de s'en servir comme étiquettes* mais le contenu de ces variables doit être le moins modifié possible.

- Les fonctions doivent permettre la **composition**&nbsp;: *la valeur d'une fonction est passée comme argument à une fonction dont la valeur est passée comme argument à une autre fonction, ...*    
En fait, le programme lui-même est évalué et retourne une valeur.

- La **récursion** doit être utilisée à la place des boucles puisqu'il n'est pas question de modifier l'état d'un programme (donc la valeur d'un compteur de boucle, par exemple).

- Les *listes* (c'est même l'origine du langage Lisp) sont souvent la structure de données de base des programmes fonctionnels.   
Il n'est cependant pas question de modifier ces listes (méthode `append`).

## Découverte des quelques éléments de programmation fonctionnelle

{{% note normal %}}
#### Suite de Collatz

On peut générer la suite de Collatz, pour un entier $n$ donné, de la sorte&nbsp;:
- si $n$ est pair, on le divise par 2&nbsp;;
- sinon on le multiplie par 3 et on ajoute 1.
On stoppe le processus lorsque la valeur de $n$ est égale à 1.

La définition de la suite est donc&nbsp;:
$$ u_{n+1} = \begin{cases}
\dfrac{u_n}{2} &\text{si } u_n \text{ est pair} \cr
3 u_n + 1 &\text{sinon.}
\end{cases}
$$
{{% /note %}}

### Récursivité

1. Définir la fonction dont la spécification est&nbsp;:
```python
def collatz_iter(n: int) -> None:
    """
    Implémentation de l'algorithme itératif qui permet de déterminer la suite de Collatz".
    La fonction affiche les termes.
    """
``` 
{{% solution "Solution" %}}
```python
def collatz_iter(n: int) -> None:
    """
    Implémentation de l'algorithme itératif qui permet de construire la suite de Collatz".
    La fonction affiche les termes.
    """
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print(1)
``` 
{{% /solution %}}


2. Définir la fonction dont la spécification est&nbsp;:
```python
def collatz_recur(n: int) -> None:
    """
    Implémentation de l'algorithme récursif qui permet de construire la suite de Collatz.
    La fonction affiche les termes.
    """
``` 
{{% solution "Solution" %}}
```python
def collatz_recur(n: int) -> None:
    """
    Implémentation de l'algorithme récursif qui permet de construire la suite de Collatz.
    La fonction affiche les termes.
    """
    if n == 1:
        print(1)
    else:
        print(n, end=" ")
        if n % 2 == 0:
            return collatz_recur(n // 2)
        else:
            return collatz_recur(3 * n + 1)
``` 
{{% /solution %}}


### Génération de listes

3. Définir la fonction dont la spécification est&nbsp;:
```python
def collatz(n: int) -> List[int]:
    """
    Implémentation de l'algorithme récursif qui permet de construire la suite de Collatz.
    La suite est retournée sous forme d'une liste.
    """
``` 
{{% solution "Solution" %}}
```python
def collatz(n: int) -> List[int]:
    """
    Implémentation de l'algorithme récursif qui permet de construire la suite de Collatz.
    La suite est retournée sous forme d'une liste.
    """
    if n == 1:
        return [1]
    else:
        if n % 2 == 0:
            return [n] + collatz(n // 2)
        else:
            return [n] + collatz(3 * n + 1)
``` 
{{% /solution %}}


### Comment manipuler une liste sans réaliser la moindre boucle&nbsp;?

Après avoir construit la liste contenant la suite de Collatz débutant au nombre $n$, on peut vouloir en extraire, par exemple, tous les nombres pairs. 

4. À l'aide de la fonction `help` découvrir la spécification de la fonction `filter`. Écrire cette spécification en français.
{{% solution "Réponse" %}}
```python 
filter(function or None, iterable) --> filter object
    """
    Retourne un itérateur dont les valeurs sont celles pour 
    lesquelles l'application de la fonction function retourne
    True. 
    Si aucune fonction n'est fournie, retourne un itérateur dont
    les valeurs sont les valeurs True
```
{{% /solution %}}

5. Définir la fonction dont la spécification est la suivante&nbsp;:
```python 
def est_pair(n: int) -> bool:
    """
    Détermine si n est pair. 
    """
```
{{% solution "Solution" %}}
```python
def est_pair(n: int) -> bool:
    """
    Détermine si n est pair. 
    """
    return n % 2 == 0
``` 
{{% /solution %}}

6. Quelle instruction permet de générer une nouvelle liste ne contenant que les éléments pairs de la liste générée par l'application `collatz(7)`&nbsp;?

**Remarque&nbsp;:** `filter` réalise une évaluation paresseuse et ne retourne pas une liste mais un itérateur. Ce concept est fondamental en programmation fonctionnelle mais ne sera pas abordé dans ce document.  
Le résultat de l'application de `filter` doit donc être passé comme argument à la fonction `list`&nbsp;: `list(filter(..., ...))`.

{{% solution "Solution" %}}
```python
list(filter(est_pair, collatz(7)))
``` 
{{% /solution %}}

Programmer la fonction `est_pair` avec le mot-clé `def` nécessite d'entrer de nombreuses lignes de code pour, au final, ne nécessiter qu'une seule instruction&nbsp;: `n % 2 == 0`. Les langages fonctionnels permettent généralement de définir des **fonctions anonymes** (**lambda expressions**).  
En Python, l'expression 
```python
lambda x, y: x**y
```
est une fonction qui associe à $x$ et $y$ le nombre $x^y$. L'application suivante est donc possible 
```python
>>> (lambda x, y: x**y)(2,3)
8
``` 
Malheureusement, la fonction anonyme, une fois utilisée est «&nbsp;perdue&nbsp;»  puisqu'elle ne possède pas de nom&nbsp;!  Il est cependant possible de la référencer par une variable&nbsp;:
```python
>>> au_carre = lambda x: x**2
>>> au_carre(2)
4
```

{{% note warning %}}
Les fonctions anonymes sont limitées à une expression en Python.
{{% /note %}}

7. Reprendre l'instruction qui permet de générer une nouvelle liste ne contenant que les éléments pairs de la liste générée par l'application `collatz(7)`, *en remplaçant l'appel à la fonction `est_pair` par une fonction anonyme*.

{{% solution "Solution" %}}
```python
list(filter(lambda n: n % 2 == 0,\
                 collatz(7)))
``` 
{{% /solution %}}

8. À l'aide de la fonction `help` découvrir la spécification de la fonction `map`. Écrire cette spécification en français.
{{% solution "Réponse" %}}
```python 
map(func, *iterables) --> map object
    """
    Retourne un itérateur qui applique la fonction func
    à chaque valeur de l'itérateur *iterables passé en
    argument.
    Stoppe une fois que toutes les valeurs de *iterables
    ont été traitées.
    """
```
{{% /solution %}}

9. Quelle instruction permet de générer une nouvelle liste contenant chaque élément de la liste générée par l'application `collatz(7)` multiplié par 3&nbsp;?  
Utiliser une fonction anonyme.

**Remarque&nbsp;:** `map` réalise aussi une évaluation paresseuse et ne retourne pas une liste mais un itérateur. Le résultat de l'application de `map` doit donc être passé comme argument à la fonction `list`&nbsp;: `list(map(..., ...))`.

{{% solution "Solution" %}}
```python
list(map(lambda x: 3 * x,\
            collatz(7)))
``` 
{{% /solution %}}

10. Quelle instruction permet de générer une nouvelle liste contenant chaque élément pair de la liste générée par l'application `collatz(7)` multiplié par 3&nbsp;?  
Utiliser une fonction anonyme.
{{% solution "Solution" %}}
```python
list(map(lambda x: 3 * x,\
             filter(lambda n: n % 2 == 0,\
                     collatz(7))))
``` 
{{% /solution %}}

## List comprehension

Les **List Comprehensions**, introduites en classe de première, permettent d'écrire en Python des instructions réalisant les mêmes opérations que `filter` et `map` de façon très efficace et **lisible**.

11. Écrire l'instruction qui permet de générer une nouvelle liste ne contenant que les éléments pairs de la liste générée par l'application `collatz(7)`, à l'aide d'une List comprehension.
{{% solution "Solution" %}}
```python
[n for n in collatz(7) if n % 2 == 0]
``` 
{{% /solution %}}

12. Écrire l'instruction qui permet de générer une nouvelle liste dont les termes sont le triple de chaque terme de la liste générée par l'application `collatz(7)`, à l'aide d'une List comprehension.
{{% solution "Solution" %}}
```python
[3 * n for n in collatz(7)]
``` 
{{% /solution %}}

13. Écrire l'instruction qui permet de générer une nouvelle liste dont les termes sont le triple de chaque terme de la liste générée par l'application `collatz(7)` si ces termes sont pairs, à l'aide d'une List comprehension.
{{% solution "Solution" %}}
```python
[3 * n for n in collatz(7) if n % 2 == 0]
``` 
{{% /solution %}}

## Quelques mots sur l'évaluation paresseuse (laziness)

La fonction `collatz` génère une liste de nombre. Ce comportement est acceptable tant que le nombre d'éléments de la liste est limité mais *terriblement inefficace lorsque le nombre de termes devient très important puisque toute la structure doit être calculée et placée en mémoire avant toute autre opération*.

> On appelle **évaluation paresseuse** le mécanisme qui consiste à *ne pas construire toute la structure dans un premier temps et à ensuite agir sur cette structure* mais à *agir sur les éléments au fur et à mesure de leur création*.

L'iterateur le plus utilisé jusqu'à présent en cours est `range` :
```python
>>> range(10)
range(0, 10)
>>> list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # on oblige l'itérateur à fournir toutes les valeurs
``` 