---
title: "Diviser pour régner"
subtitle: ""
author: ""
type: ""
date: 2023-01-29T21:53:04+04:00
draft: false
toc: true
tags: ["Diviser pour régner"]
categories: ["Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Dans quel cas ?

- On parvient à découper un problème en **sous-problèmes indépendants les uns des autres**. On poursuit cette démarche jusqu'à aboutir à une situation simple : **cas de base**.
- La solution du **cas de base** est généralement simple à obtenir et permet la construction de la solution du problème.

#### Remarque

C'est l'indépendance des sous-problèmes qui permet la construction de la solution globale **directe** par recombinaison des solutions intermédiaires.

#### Exemples

- Exponentiation rapide
- Recherche dichotomique dans un tableau trié, dans une liste triée
- Tri rapide d'un tableau
- Tri fusion récursif d'un tableau
- etc.

## Schéma de résolution

{{% note tip %}}

Diviser
: On décompose le problème initial en un ou plusieurs sous-problèmes de plus petites tailles.

Régner
: Chaque sous-problème est résolu

Combiner
: Les solutions des sous-problèmes sont combinées pour construire la solution du problème initial.

{{% /note %}}

#### Remarques

- Cette procédure se prête naturellement à un **traitement récursif** des problèmes mais une **approche itérative** reste possible.
- Cette procédure assure que **l'algorithme est correct**. Il reste à valider sa **terminaison** (que  **le cas de base est toujours atteint** ).

## Exercice : exponentiation rapide

L'algorithme suivant permet de calculer $a^n$ :
$$
a^n = \begin{cases}
   1 &\text{if } n=0 \\\\
   a \times a^{n-1} &\text{if } n>0
\end{cases}
$$

1. Programmer la fonction `puissance1` dont la spécification est :

```python
def puissance1(a: int, n: int) -> int:
    """
    Calcul de a^n.
    """
```

Penser à écrire quelques tests.

{{% solution "Réponse" %}}

```python
def puissance1(a: int, n: int) -> int:
    """
    Calcul de a^n.
    Implémentation de l'algorithme 1.
    """
    if n == 0:
        return 1
    else:
        return a * puissance1(a, n - 1)


if __name__ == "__main__":
    assert puissance1(3, 2) == 9
    assert puissance1(5, 0) == 1
    assert puissance1(2, 8) == 256

    print("Done!")
```

{{% /solution %}}

2. Quelle est la complexité de cet algorithme ?

{{% solution "Réponse" %}}

Le calcul nécessite $n$ appels récursifs et $n+1$ multiplications. La complexité est donc en $O(n)$.

{{% /solution %}}

L'algorithme suivant permet aussi de calculer $a^n$ :
$$
a^n = \begin{cases}
   1 &\text{if } n=0 \\\\
    ( a^k )^2  &\text{if } n = 2k \text{ (n est pair)} \\\\
   a \times ( a^k )^2 &\text{if } n = 2k + 1 \text{ (n est impair)}
\end{cases}
$$

3. Programmer la fonction `puissance2` dont la spécification est :

```python
def puissance2(a: int, n: int) -> int:
    """
    Calcul de a^n.
    Implémentation de l'algorithme 2.
    """
```

Penser à écrire quelques tests.

{{% solution "Réponse" %}}

```python
def puissance2(a: int, n: int) -> int:
    """
    Calcul de a^n.
    """
    if n == 0:
        return 1

    calc = puissance2(a, n // 2)
    
    if n % 2 == 0:
        return calc**2
    else:
        return a * (calc)**2


if __name__ == "__main__":
    assert puissance2(3, 2) == 9
    assert puissance2(5, 0) == 1
    assert puissance2(2, 8) == 256

    print("Done!")
```

{{% /solution %}}

4. Justifier que le seconde algorithme met en œuvre le raisonnement « Diviser pour règner ».
{{% solution "Réponse" %}}

- La première ligne de l'algorithme correspond au cas de base pour lequel $n=0$ et $a^n=1$.
- Pour $n>0$, à partir de la valeur $n$, le calcul se poursuit avec la valeur $\left\lfloor \dfrac{n}{2} \right\rfloor$. On décompose le calcul de $a^n$ en celui de $a^{\left\lfloor \dfrac{n}{2} \right\rfloor}$, puis celui de $a^{\left\lfloor \dfrac{n}{2} \right\rfloor / 2}$, etc. jusqu'à atteindre le cas de base. Chaque calcul intermédiaire se fait sur une instance plus petite.
- Chaque calcul intermédiaire est aussi indépendant du calcul précédent.

#### Remarque

- $\left\lfloor \dfrac{n}{2} \right\rfloor$ est la notation mathématique pour l'opération en Python `n // 2`, c'est à dire *le plus grand entier inférieur au résultat de la division de* $n$ *par 2*.

- $\left\lceil \dfrac{n}{2} \right\rceil$ est la notation mathématique pour l'opération en Python `n // 2 + 1`, c'est à dire pour *le plus petit entier supérieur au résultat de la division de* $n$ *par 2*.

{{% /solution %}}

5. Pourquoi appelle-t-on l'algorithme 2, l'exponentiation rapide ?
{{% solution "Réponse" %}}

Soit $k$ le nombre de fois qu'il faut diviser (division euclidienne) $n$ par 2 pour parvenir à la valeur 1. $k$ est tel que
$$ 1 = \dfrac{n}{2^k} \iff 2^k = n \iff k = \log_2 n $$.  
Il reste un appel récursif supplémentaire à effectuer pour arriver au cas de base.  
La complexité de l'algorithme est donc en $O(\log_2 n)$ ; elle est bien meilleure que celle de l'algorithme 1.

{{% /solution %}}
