---
title: "Autour de la suite de Fibonacci"
subtitle: "Chapitre 14,"
author: ""
type: ""
date: 2021-02-25T04:49:20+04:00
draft: false
toc: true
tags: ["Récursivité", "Récursivité terminale", "Récursivité enveloppée", "Programmation dynamique", "Mémoïsation"]
categories: ["Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Rappel : récursivité terminale

La définition de la fonction factorielle est
$$
    n! =
    \begin{cases}
        0 & \text{if } n = 0 \cr
        n \times (n-1)! & \text{sinon}
    \end{cases}
$$

1. Définir la fonction `fact_env` qui calcule la factorielle d'un entier naturel $n$, *sans oublier le jeu de tests*.\
    La spécification de la fonction est :

    ```python
    def fact_env(n: int) -> int:
        """
        Retourne la factorielle de n.

        Algorithme : récursivité enveloppée
        """
    ```

{{% solution "Réponse" %}}

```python
def fact_env(n: int) -> int:
    """
    Retourne la factorielle de n.

    Algorithme : récursivité enveloppée
    """
    if n == 0:
        return 1

    return n * fact_env(n - 1)


if __name__ == "__main__":
    assert fact_env(0) == 1
    assert fact_env(1) == 1
    assert fact_env(5) == 120
    assert fact_env(8) == 40320
```

{{% /solution %}}

{{% note normal %}}
En informatique, la **récursion terminale**, aussi appelée, récursion finale, est un *cas particulier de récursivité assimilée à une itération*.\
Une fonction à récursivité terminale (dite tail-recursive en anglais) est une fonction où l'**appel récursif est la dernière instruction à être évaluée**. Cette instruction est alors nécessairement « pure », c'est-à-dire qu'elle consiste en un simple appel à la fonction, et jamais à un calcul ou une composition.\
Les algorithmes récursifs exprimés à l'aide de fonctions à récursion terminale profitent donc d'une optimisation de la pile d'exécution.\
Cette réorganisation économise de l'espace mémoire car aucun état, sauf l'adresse de la fonction appelante, n'a besoin d'être sauvé sur la pile d'exécution. Cela signifie également que le programmeur n'a pas à craindre l'épuisement de l'espace de pile ou du tas pour des récursions très profondes.

<div style="text-align: right;">
    Wikipedia
</div>
{{% /note %}}

2. Définir la fonction `fact_term` qui calcule la factorielle d'un entier naturel $n$, *sans oublier le jeu de tests*.\
    La spécification de la fonction est :

    ```python
    def fact_term(n: int) -> int:
        """
        Retourne la factorielle de n.

        Algorithme : récursivité terminale
        """
    ```

    La fonction `fact_term` est en fait une fonction enveloppe de la fonction `_fact` dont la spécification est :

    ```python
    def _fact(n: int, acc: int = 1) -> int:
        """
        Fonction qui effectue réellement le calcul récursif.
        """
    ```

    La fonction `_fact` met en œuvre un raisonnement basé sur la récursivité terminale.

{{% solution "Réponse" %}}

```python
def fact_term(n: int) -> int:
    """
    Retourne la factorielle de n.

    Algorithme : récursivité terminale
    """
    def _fact(n: int, acc: int = 1) -> int:
        """
        Fonction qui effectue réellement le calcul récursif.
        """
        if n == 0:
            return acc

        return _fact(n - 1, acc * n)

    return _fact(n, 1)


if __name__ == "__main__":
    assert fact_term(0) == 1
    assert fact_term(1) == 1
    assert fact_term(5) == 120
    assert fact_term(8) == 40320
```

{{% /solution %}}

## Autour de la suite de Fibonacci

En mathématiques, la suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. Elle commence par les termes 0 et 1 si on part de l'indice 0, ou par 1 et 1 si on part de l'indice 1.
$$
    F_n =
    \begin{cases}
        F_0 = 0 \cr
        F_1 = 1 \cr
        F_n = F_{n-1} + F_{n-2}
    \end{cases}
$$

### Résolutions du problème sans programmation dynamique

3. Définir la fonction `fibo_iter` qui calcule le terme de rang $n$ de la suite de Fibonacci, *sans oublier le jeu de tests*. Le raisonnement mis en œuvre doit être itératif.\
    La spécification de la fonction est :

    ```python
    def fibo_iter(n: int) -> int:
    """
    Retourne le terme de rang n de la suite de Fibonacci.

    Algorithme : itératif
    """
    ```

{{% solution "Réponse" %}}

```python
def fibo_iter(n: int) -> int:
    """
    Retourne le terme de rang n de la suite de Fibonacci.

    Algorithme : itératif
    """
    u = 0
    v = 1
    for i in range(2, n + 1):
        w = u + v
        u = v
        v = w

    if n == 0:
        return 0
    else:
        return v


if __name__ == "__main__":

    # fibo_iter
    assert fibo_iter(0) == 0
    assert fibo_iter(1) == 1
    assert fibo_iter(10) == 55
    assert fibo_iter(16) == 987
```

{{% /solution %}}

4. Quelle est la complexité de l'algorithme itératif ?

{{% solution "Réponse" %}}

L'algorithme comporte une boucle, la complexité est donc en $O(n)$.

{{% /solution %}}

5. Définir la fonction `fibo_head` qui calcule le terme de rang $n$ de la suite de Fibonacci, *sans oublier le jeu de tests*. Le raisonnement mis en œuvre doit être récursif.\
    La spécification de la fonction est :

    ```python
    def fibo_head(n: int) -> int:
    """
    Retourne le terme de rang n de la suite de Fibonacci.

    Algorithme : récursif (enveloppé)
    """
    ```

{{% solution "Réponse" %}}

```python
def fibo_head(n: int) -> int:
    """
    Retourne le terme de rang n de la suite de Fibonacci.

    Algorithme : récursif (enveloppé)
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fibo1 = fibo_head(n - 1)
    fibo2 = fibo_head(n - 2)
    return fibo1 + fibo2


if __name__ == "__main__":
    assert fibo_head(0) == 0
    assert fibo_head(1) == 1
    assert fibo_head(10) == 55
    assert fibo_head(16) == 987
```

{{% /solution %}}

6. Écrire l'arbre des appels récursifs pour $n=5$. En déduire la complexité de l'algorithme récursif.\
Quelle est la raison d'une telle complexité ?

{{% solution "Réponse" %}}

- Les mêmes calculs sont effectués plusieurs fois.
- La hauteur de l'arbre des appels est égale à $n-1$.
- Si chaque étape est en $O(1)$, le nombre de calculs effectués est donc $2^0 + 2^1 + 2^2 + 2^3 + \ldots + 2^{n-1} = 2^n$.

La complexité est donc en $O(2^n)$.

{{% /solution %}}

7. En prenant pour exemple la définition de la fonction à la question 2. et l'algorithme itératif, à la question 3., définir la fonction `fib_tail` qui calcule le terme de rang $n$ de la suite de Fibonacci à l'aide d'un algorithme récursif terminal.\
    La spécification de la fonction `fib_tail` est :

    ```python
    def fibo_tail(n: int) -> int:
        """
        Retourne le terme de rang n de la suite de Fibonacci.

        Algorithme : récursif (terminale)
        """
    ```

    La fonction `fib_tail` est en fait une fonction enveloppe de la fonction `_fibo` dont la spécification est :

    ```python
    def _fibo(n: int, a: int=0, b: int=1) -> int:
        """
        Fonction qui effectue réellement le calcul récursif.
        """
    ```

{{% solution "Réponse" %}}

```python
def fibo_tail(n: int) -> int:
    """
    Retourne le terme de rang n de la suite de Fibonacci.

    Algorithme : récursif (terminale)
    """
    def _fibo_tail(n: int, a: int = 0, b: int = 1):
        if n == 0:
            return a
        elif n == 1:
            return b

        return _fibo_tail(n - 1, b, a + b)

    return _fibo_tail(n)


if __name__ == "__main__":
    assert fibo_tail(0) == 0
    assert fibo_tail(1) == 1
    assert fibo_tail(10) == 55
    assert fibo_tail(16) == 987
```

{{% /solution %}}

8. Quelle est la complexité de cet algorithme ?

{{% solution "Réponse" %}}

La complexité de l’algorithme récursif terminal, en nombre d’additions, est donnée par la récurrence $T(n) = 1+T(n−1)$. On a donc $T(n) = n−1$ pour `_fibo_tail`, et par extension pour `fibo_tail`.

{{% /solution %}}

### Programmation dynamique

{{% note tip %}}
En informatique, la **programmation dynamique** est une méthode algorithmique pour résoudre des **problèmes d'optimisation**. Le concept a été introduit au début des années 1950 par Richard Bellman.

*La programmation dynamique consiste à résoudre un problème en le décomposant en sous-problèmes, puis à résoudre les sous-problèmes, des plus petits aux plus grands **en stockant les résultats intermédiaires**.*

La programmation dynamique s'appuie sur le **principe d'optimalité de Bellman** : *une solution optimale d'un problème s'obtient en combinant des solutions optimales à des sous-problèmes*.

La méthode de **programmation dynamique**, comme la méthode **diviser pour régner**, résout des problèmes en combinant des solutions de sous-problèmes. *Les algorithmes diviser-pour-régner partitionnent le problème en **sous-problèmes indépendants** qu’ils résolvent récursivement, puis combinent leurs solutions pour résoudre le problème initial. La méthode diviser-pour-régner est inefficace si on doit résoudre plusieurs fois le même sous-problème.*
{{% /note %}}

{{% note normal %}}
La programmation dynamique est utilisée pour résoudre des **problèmes d'optimisation**.
La conception d’un algorithme de programmation dynamique est typiquement découpée en quatre étapes :

- Caractériser la structure d’une solution optimale.
- Définir (souvent de manière récursive) la valeur d’une solution optimale.
- Calculer la valeur d’une solution optimale.
- Construire une solution optimale à partir des informations calculées.
La dernière étape est utile pour calculer une **solution optimale**, et pas seulement la valeur optimale. Un problème d'optimisation peut avoir de nombreuses solutions. Chaque solution a une valeur, et on souhaite trouver une solution ayant la valeur optimale. *Une telle solution optimale au problème n'est pas forcément unique, c'est sa valeur qui l'est*.
{{% /note %}}

Dans le cas du calcul du terme de rang $n$ de la suite de Fibonacci à l'aide d'un raisonnement récursif, le problème a pour origine les multiples calculs de chacun des sous-termes nécessaires. *La programmation dynamique consiste alors à stocker les valeurs des sous-problèmes pour éviter les recalculs*.

{{% note tip %}}
Il existe alors deux méthodes pour calculer effectivement une solution : la **méthode ascendante** (**Bottom-up approach**) et la **méthode descendante** (**Top-down approach**).

- Dans la **méthode ascendante**, on commence par calculer des solutions pour les sous-problèmes les plus petits, puis, de proche en proche, on calcule les solutions des problèmes en utilisant le principe d'optimalité et on mémorise les résultats dans un tableau ou un dictionnaire `F`.
- Dans la **méthode descendante**, on écrit un algorithme récursif mais on utilise la **mémoïsation** pour ne pas résoudre plusieurs fois le même problème, c'est-à-dire que l'on stocke dans un tableau ou un dictionnaire `F` les résultats des appels récursifs.
{{% /note %}}

{{% note normal %}}
Une **fonction mémoïsée** *stocke les valeurs renvoyées par ses appels précédents dans une structure de données adaptée et, lorsqu'elle est appelée à nouveau avec les mêmes paramètres, renvoie la valeur stockée au lieu de la recalculer*. Une fonction peut être mémoïsée seulement si elle est **pure**, c'est-à-dire *si sa valeur de retour ne dépend que de la valeur de ses arguments, sans effet de bord*. En ce cas, la transparence référentielle permet de remplacer l'appel de la fonction directement par sa valeur. À la différence d'une fonction tabulée, où la table est statique, une fonction mémoïsée repose sur une table dynamique remplie à la volée.

*La mémoïsation est une façon de diminuer le temps de calcul d'une fonction, au prix d'une occupation mémoire plus importante. La mémoïsation modifie donc la complexité d'une fonction, en temps comme en espace.*
{{% /note %}}

### Résolutions du problème à l'aide de la programmation dynamique

9. Quel est l'intérêt des structures de données tableau ou dictionnaire pour le stockage des valeurs des sous-problèmes ?

10. Définir la fonction `fibo_memo` qui calcule le terme de rang $n$ de la suite de Fibonacci, *sans oublier le jeu de tests*. Le raisonnement doit être récursif et mettre en œuvre la technique de mémoïsation (méthode descendante).

{{% solution "Réponse" %}}

```python
def fibo_memo1(n: int) -> int:
    """
    Version mémoïsée de Fibonacci.

    Utilisation d'un dictionnaire et d'une fonction
    enveloppe.
    """
    dic = {0: 0, 1: 1}

    def _fibo(n: int, dic: "Dict[int: int]") -> int:
        if n in dic.keys():
            return dic[n]
        else:
            dic[n] = _fibo(n - 1, dic) + _fibo(n - 2, dic)
            return dic[n]

    return _fibo(n, dic)
```

ou

```python
def fibo_memo2(n: int, tab: List[int] = [0, 1]) -> int:
    """
    Version mémoïsée de Fibonacci.

    Utilisation d'une liste.
    """
    if n < len(tab):
        return tab[n]

    calcul = fibo_memo2(n - 1, tab) + fibo_memo2(n - 2, tab)
    tab.append(calcul)
    return calcul
```

{{% /solution %}}

11. Définir la fonction `fibo_up` qui calcule le terme de rang $n$ de la suite de Fibonacci, *sans oublier le jeu de tests*. Le raisonnement doit mettre en œuvre la méthode ascendante du problème.

{{% solution "Réponse" %}}

```python
def fibo_up(n: int) -> int:
    """
    Retourne la valeur de rang n de la suite de Fibonacci.

    Version itérative avec stockage des valeurs dans une liste.
    """
    tab = [0, 1]
    for i in range(2, n + 1):
        valeur = tab[i - 2] + tab[i - 1]
        tab.append(valeur)
    return tab[n]
```

{{% /solution %}}

## Application : nombre de façon d'atteindre la nième marche d'un escalier

On cherche le nombre de méthodes différentes qui permettent d'atteindre la nième marche d'un escalier, sachant que l'on peut monter un, deux ou trois marches à la fois.

1. Déterminer la relation de récurrence, sachant que l'on note $u_n$ le nombre de méthodes permettant d'atteindre la nième marche.

{{% solution "Réponse" %}}

$$
    u_n =
    \begin{cases}
    u_1 &= 1 \cr
    u_2 &= 2 \cr
    u_3 &= 4 \cr
    u_{n} &= u_{n-1} + u_{n-2} + u_{n-3}
    \end{cases}
$$

{{% /solution %}}

1. Quel est l’écueil à éviter lorsqu’on programme le calcul du n-ième terme de la suite précédente de manière récursive ?
{{% solution "Réponse" %}}
Il faut éviter que les appels récursifs calculent plusieurs fois les mêmes valeurs.
{{% /solution %}}

2. Proposer une version itérative du calcul de $u_n$.

```python
def nbre_methodes_iter(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version itérative.
    """
```

{{% solution "Réponse" %}}

```python
def nbre_methodes_iter(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version itérative.
    """
    u, v, w = 1, 2, 4

    for i in range(4, n + 1):
        z = u + v + w
        u = v
        v = w
        w = z

    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return w
```

{{% /solution %}}

3. Proposer une version récursive du calcul de $u_n$.

```python
def nbre_methodes_rec(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version récursive.
    """
```

{{% solution "Réponse" %}}

```python
def nbre_methodes_rec(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version récursive.
    """
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    
    return nbre_methodes_rec(n - 1) + nbre_methodes_rec(n - 2) + nbre_methodes_rec(n - 3)
```

{{% /solution %}}

4. Proposer une version récursive efficace du calcul de $u_n$ qui utilise la mémoïsation.

```python
def nbre_methodes_memo(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version qui utilise la mémoïsation.
    """
```

{{% solution "Réponse" %}}

```python
def nbre_methodes_memo(n: int) -> int:
    """
    Calcul du nombre de méthodes différentes pour
    accéder à la nième marche d'un escalier.

    Version qui utilise la mémoïsation.
    """
    memo = {1: 1, 2: 2, 3: 4} 
    
    def _nbre(n: int) -> int: 
        if n in memo.keys(): 
            return memo[n] 
        else: 
            memo[n] = _nbre(n - 1) + _nbre(n - 2) + _nbre(n - 3) 
        return memo[n] 
        
    return _nbre(n)
```

{{% /solution %}}
