---
title: "Récursivité sur les entiers"
subtitle: ""
date: 2020-09-05T18:34:00+04:00
draft: false
toc: true
tags: ["Programmation", "Récursivité", "Fonctions", "Algorithmique"]
categories: ["Informatique", "Terminales Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 101
---
[^1]: Ce n'est pas la seule définition possible et c'est loin d'être la plus efficace une fois implémentée.

<center>
<h3>To understand recursion, you must first understand recursion.</h3>
</center>

La **récurrence** est un *raisonnement mathématique* courant et parmi les plus puissants pour démontrer des théorèmes ou construire des objets. Par exemple, on l'utilise dans un cours de mathématique de lycée pour montrer que&nbsp;:

- Pour tout entier $n \geqslant 0$, on a&nbsp;: $1 + 2 + 3 + \ldots + n = \dfrac{n(n+1)}{2}$&nbsp;;
- Un entier naturel n'est autre que 0 ou le successeur d'un entier naturel (0 est 0, 1 est le successeur de 0, 2 est le successeur de 1, ...).

En programmation, on peut raisonner de façon identique, nous allons **construire des fonctions et des structures de données (listes chaînées, arbres, etc.) à l'aide d'une hypothèse de récurrence et d'un point de départ**. **Le déroulement de la récurrence sera quant à lui pris en charge par la machine**.

{{< note warning >}}
La récursion est une approche plus **descriptive** que **constructive**. *On «&nbsp;dit&nbsp;» quoi faire à l'ordinateur mais pas comment*.
{{< /note >}}

{{< note tip >}}
La **récursion** est un mécanisme puissant permettant d'exprimer la **répétition des opérations** dans un programme **sans utiliser de structure itérative** (boucles `while` ou `for`). C'est un mode de pensée qui permet de concevoir des fonctions ou des structures de données (listes chaînées, arbres, etc.) dont l'écriture condense en peu de lignes l'exécution de calculs éventuellement très longs.
{{< /note >}}

*Ce chapitre traite de la récursion sur les nombres entiers.*

{{< note goal >}}
Écrire la définition récursive d'une fonction sur les entiers (un cas de base et un appel récursif), la programmer en Python et suivre son exécution à l'aide de l'arbre des appels.
{{< /note >}}

Avant de commencer, une question à se poser sans calculatrice. On sait que $1 + 2 + \ldots + 99 = 4950$. Combien vaut $1 + 2 + \ldots + 99 + 100$&nbsp;? Faut-il refaire tout le calcul&nbsp;?

{{< solution "Réponse" >}}
Non&nbsp;: il suffit d'ajouter 100 au résultat connu, soit $4950 + 100 = 5050$. On a exprimé la somme jusqu'à 100 à l'aide de la somme jusqu'à 99. Toute la récursivité tient dans cette idée&nbsp;: résoudre un problème à l'aide de la solution du même problème, en plus petit.
{{< /solution >}}

## Rappels sur les fonctions

- {{< remote "Cours de 1ère NSI sur les fonctions" "/premieres-nsi/chap-2/2-1-types-fonctions/" >}}

## Définition récursive d'une fonction

### Factorielle d'un entier naturel

La fonction factorielle indique le **nombre de permutations** dans un ensemble comportant $n$ éléments.  Par exemple, il existe $3! =  6$ façons d'arranger les 3 caractères 'a', 'b', 'c'&nbsp;:
> 'abc', 'acb', 'bac', 'bca', 'cab' et 'cba'.

On peut exprimer de plusieurs façons la définition de cette fonction&nbsp;:

- Une définition **implicite**&nbsp;: $n! = 1 \times 2 \times 3 \times \ldots \times n$
- Une définition **explicite**&nbsp;:
$$
n! = \left\lbrace
        \begin{array}{ll}
            1                   & \text{ si } n = 0 \cr
            n\times (n-1)! & \text{ si } n \geq 1 \cr
        \end{array}
    \right.
$$

La première définition est *particulièrement ambigüe*&nbsp;:

- Que signifie l'ellipse ...&nbsp;?
- Est-il possible de calculer la factorielle d'un nombre inférieur à 3&nbsp;?
- La factorielle de 0 existe-t-elle&nbsp;?

Les réponses à toutes ces questions sont évidentes pour une personne ayant suivi un cours de mathématique mais inaccessibles à un ordinateur.

La  définition explicite, *qui se réfère à elle-même*, est dite **récursive**&nbsp;: *la valeur de la fonction en $n$ s'exprime au moyen de la valeur de la fonction en $n-1$*.

Une fonction définie de façon récursive est **calculable**.

### Élévation à la puissance

On peut exprimer de plusieurs façons la définition de cette fonction&nbsp;:

- Une définition **implicite**&nbsp;: $x^n = \overbrace{x \times x \times \ldots \times x}^{n \text{ fois}}$
- Une définition **explicite**[^1]&nbsp;:
$$
x^n = \left\lbrace
        \begin{array}{ll}
            1                   & \text{ si } n = 0 \cr
            x \times x^{ (n-1)} & \text{ si } n > 0 \cr
        \end{array}
    \right.
$$

La définition implicite présente les mêmes ambiguïtés que dans le cas du calcul de la factorielle d'un entier naturel, tandis que la définition explicite, *qui se réfère elle aussi à elle-même* et est donc **récursive**, permet de **calculer** la valeur de $x^n$.

### Mise en œuvre d'un raisonnement récursif&nbsp;: le jeu de Bowling

<img src="/terminales-nsi/chap-1/im-1-1.jpg" width="50%" alt="" />

La disposition des quilles de Bowling permet d'illustrer la mise en œuvre d'un *raisonnement récursif*&nbsp;:

- Combien de quilles composent l'arrangement présenté&nbsp;?

{{< solution "Réponse" >}}
10
{{< /solution >}}

- On veut ajouter une cinquième ligne à l'arrangement présenté. Combien de quilles supplémentaires devront être disposées si l'on souhaite respecter la logique présente&nbsp;?

{{< solution "Réponse" >}}
5
{{< /solution >}}

- De combien de quilles sera alors constitué l'arrangement&nbsp;?

{{< solution "Réponse" >}}
$10+5=15$
{{< /solution >}}

| Nombre de lignes | Nombre de quilles | Calcul du nombre de quilles |
|:---:|:---:|:---:|
| 1 | 1 | `arrangement(1)` |
| 2 | 3 | 2 + `arrangement(1)` |
| 3 | 6 | 3 + `arrangement(2)` |
| 4 | 10 | 4 + `arrangement(3)` |
| 5 | 15 | 5 + `arrangement(4)` |

> Nombre de quilles en fonction du nombre de lignes. La fonction **arrangement** reçoit en argument le nombre de lignes et retourne le nombre de quilles dans un arrangement de ce nombre de lignes.

Combien de quilles contient un arrangement de 11 lignes&nbsp;?
: On déduit rapidement du tableau ci-dessus que le nombre de quilles est égal à&nbsp;: 11 + `arrangement(10)`, c'est-à-dire à 11 plus le nombre de quilles présentes dans un arrangement à 10 lignes.

Obtient-on directement la réponse&nbsp;?
: Non, il faut tout d'abord calculer le nombre de quilles dans un arrangement à 10 lignes. Le calcul est facile, c'est&nbsp;: 10  + `arrangement(9)`, etc.

Quand faut-il s'arrêter&nbsp;?
: On sait que `arrangement(1)` = 1. On s'arrête donc lorsque l'on est parvenu à un arrangement à 1 ligne.

{{< note normal >}}
Le raisonnement précédent est **un raisonnement récursif**. On a découpé le problème en deux parties&nbsp;:

- Si l'arrangement comporte une seule ligne, la réponse est&nbsp;: `arrangement(1)` = 1.

- Si l'arrangement comporte $N$ lignes, la réponse est&nbsp;: N + `arrangement(N - 1)`.
{{< /note >}}

#### Calcul effectif du nombre de quilles dans un arrangement à 5 lignes

$$
\begin{aligned}
  \text{arrangement} (5) & = 5 + \text{arrangement} (4)  \cr
  & = 5 + (4 + \text{arrangement} (3))  \cr
  & = 5 + (4 + (3 + \text{arrangement} (2)))  \cr
  & = 5 + (4 + (3 + (2 + \text{arrangement} (1))))  \cr
  & = 5 + (4 + (3 + (2 + (1)))) \cr
  & = 5 + (4 + (3 + 3)) \cr
  & = 5 + (4 + 6)  \cr
  & = 5 + 10  \cr
  & = 15
\end{aligned}
$$

{{< note tip >}}

#### Algorithme récursif

Un algorithme est simplement **récursif** s'il s'appelle lui-même pour effectuer son traitement.

*Il est impératif de veiller à ce qu'un algorithme récursif se termine sous peine d'engendrer un processus infini*&nbsp;!
{{< /note >}}

#### Implémentation de l'algorithme en Python

```python
def arrangement(n: int) -> int:
    """
    Détermination du nombre de quilles dans un
    arrangement à n lignes.

    HYPOTHÈSE : n entier naturel non nul.
    """
    if n == 1:  # cas de base
        return 1
    else:
        return n + arrangement(n - 1)  # appel récursif


assert arrangement(5) == 15
```

- {{< remote "Code Python interactif" "https://pythontutor.com/visualize.html#code=def%20arrangement%28n%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20D%C3%A9termination%20du%20nombre%20de%20quilles%20dans%20un%20%0A%20%20%20%20arrangement%20%C3%A0%20n%20lignes.%0A%20%20%20%20%0A%20%20%20%20HYPOTH%C3%88SE%20%3A%20n%20entier%20naturel.%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20n%20%3D%3D%201%3A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20cas%20de%20base%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20n%20%2B%20arrangement%28n%20-%201%29%20%20%20%23%20appel%20r%C3%A9cursif%0A%20%20%20%20%20%20%20%20%0Aassert%20arrangement%285%29%20%3D%3D%2015&cumulative=false&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" >}}

### Retour sur le calcul de la factorielle d'un entier naturel

On reprend ici le calcul de la factorielle de l'entier naturel $n$. La *définition récursive* de la fonction factorielle est donc&nbsp;:

$$
n! = \left\lbrace
    \begin{array}{ll}
        1                   & \text{ si } n = 0\cr
        n\times (n-1)! & \text{ si } n \geq 1\cr
    \end{array}
    \right.
$$

#### Application&nbsp;: calcul de la factorielle de 5

- En prenant exemple sur le calcul effectif du nombre de quilles en fonction du nombre de ligne dans l'arrangement, calculer la valeur de $5!$ en détaillant toutes les étapes.
{{< solution "Réponse" >}}
$$
\begin{aligned}
  \text{factorielle} (5) & = 5 \times \text{factorielle} (4)\cr
  & = 5 \times (4 \times \text{factorielle} (3))\cr
  & = 5 \times (4 \times (3 \times \text{factorielle} (2)))\cr
  & = 5 \times (4 \times (3 \times (2 \times \text{factorielle} (1))))\cr
  & = 5 \times (4 \times (3 \times (2 \times (1 \times \text{factorielle} (0)))))\cr
  & = 5 \times (4 \times (3 \times (2 \times (1 \times 1))))\cr
  & = 5 \times (4 \times (3 \times (2 \times 1)))\cr
  & = 5 \times (4 \times (3 \times 2))\cr
  & = 5 \times (4 \times 6)\cr
  & = 5\times 24\cr
  & = 120
\end{aligned}
$$
{{< /solution >}}

#### Arbre des appels

**L'arbre des appels** est une représentation arborescente faisant apparaître les appels récursifs jusqu'au cas de base.

<img src="/terminales-nsi/chap-1/im-1-2.jpg" width="70%" alt="" />

#### Implémentation de l'algorithme récursif en Python

```python
def factorielle(n: int) -> int:
    """
    Définition récursive de la fonction factorielle.

    HYPOTHÈSE : n entier naturel.
    """
    if n == 0:  # cas de base
        return 1
    else:
        return n * factorielle(n - 1)  # appel récursif


assert factorielle(5) == 120
```

- {{< remote "Code Python interactif" "https://pythontutor.com/visualize.html#code=def%20factorielle%28n%3A%20int%29%20-%3E%20int%3A%0A%20%20%20%20%22%22%22%20%0A%20%20%20%20D%C3%A9finition%20r%C3%A9cursive%20de%20la%20fonction%20factorielle.%0A%20%20%20%20%0A%20%20%20%20HYPOTH%C3%88SE%20%3A%20n%20entier%20naturel.%0A%20%20%20%20%22%22%22%0A%20%20%20%20if%20n%20%3D%3D%200%3A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20cas%20de%20base%0A%20%20%20%20%20%20%20%20return%201%0A%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20return%20n%20*%20factorielle%28n%20-%201%29%20%20%20%23%20appel%20r%C3%A9cursif%0A%20%20%20%20%20%20%20%20%0Aassert%20factorielle%285%29%20%3D%3D%20120&cumulative=false&heapPrimitives=false&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false" >}}

## Structure d'une définition récursive

{{< note tip >}}
La **définition récursive** d'une fonction doit être formée&nbsp;:

- d'un ou plusieurs **cas de base**, qui ne *doivent contenir aucun appel récursif*&nbsp;;
- d'un ou plusieurs **appel(s) récursif(s)** au cours desquels *la fonction s'appelle elle-même*.
{{< /note >}}

#### Remarques

- Il est impératif que le cas de base soit réalisé à une étape du processus, sous peine d'obtenir une récursion infinie.
- Les appels récursifs n'apparaissent pas de façon évidente dans le cas de la *récursivité croisée* (cf. exercices).

{{< note info >}}

#### Ensembles bien fondés

La **récursion** sur les entiers naturels consiste à *transformer un problème sur un entier naturel $n$ en un ou plusieurs problèmes sur des nombres plus petits*. *Comme il n'existe pas de suite infinie strictement décroissante dans l'ensemble des entiers naturels*, la récursion finit par atteindre un *cas de base* comme 0 (ou 1, ou ...) *pour lequel une solution directe au problème est fournie*.

L'ensemble des entiers naturels est dit «&nbsp;bien fondé&nbsp;».
{{< /note >}}

## Récursivité vs itération

La récursivité et l'itération sont deux **paradigmes** différents ayant le même objectif&nbsp;: **faire effectuer des traitements répétitifs à un ordinateur**.

{{< note tip >}}

#### Récursivité, Itération

- Un **algorithme itératif décrit** *comment doivent être transformées les données* pour parvenir à résoudre le problème.  
À chaque «&nbsp;tour de boucle&nbsp;» des affectations sont réalisées.

- Un **algorithme récursif définit**, au sens mathématique du terme, le traitement à mettre en œuvre pour parvenir à résoudre le problème.  
Cet algorithme ne s'appuie généralement pas sur la notion d'affectation (nous reviendrons sur cette partie lorsque nous parlerons des différents paradigmes de programmation).

- *Tout problème dont la résolution s'appuie sur un algorithme récursif peut aussi être résolu à l'aide d'un algorithme itératif* (plus ou moins simplement).
  
- *Tout problème dont la résolution s'appuie sur un algorithme itératif peut aussi être résolu à l'aide d'un algorithme récursif*.

- Les algorithmes récursifs sont généralement plus simples à comprendre que les algorithmes itératifs correspondants.
{{< /note >}}

{{< note warning >}}
*La version récursive d'un algorithme ne dit pas comment atteindre l'état final d'un traitement, elle donne une définition de ce résultat*.
{{< /note >}}

#### Exemple

- L'algorithme récursif du calcul de la factorielle d'un nombre définit cette factorielle.
- L'algorithme itératif indique qu'il faut multiplier 1 par 2, stocker le résultat de ce calcul dans une variable, multiplier le contenu de cette variable par 3, ..., jusqu'à $n$.

{{< note normal >}}
Certains langages informatiques appelés **langages fonctionnels**, ne possèdent *ni instruction d'affectation ni structure itérative*&nbsp;!

Les langages qui privilégient les structures itératives (et l'affectation) sont dits **impératifs**.  
Python est un langage multi-paradigme&nbsp;: il permet de programmer de façon **impérative**, **objet** ou **fonctionnelle** (même si les appels récursifs, par exemple, ne sont pas aussi bien optimisés en Python que dans les langages fonctionnels).
{{< /note >}}

{{< note warning >}}

#### Pourquoi ne pas toujours utiliser la récursivité&nbsp;?

Un algorithme récursif est généralement plus facile à comprendre que l'équivalent itératif. On peut donc se demander pourquoi on ne privilégie pas toujours les traitements récursifs.

Généralement, les appels récursifs successifs *nécessitent plus d'espace mémoire et de traitements* que les processus itératifs (les *processeurs ont, eux, un fonctionnement fondamentalement itératif*). En Python, le nombre d'appels récursifs imbriqués est d'ailleurs limité à 1000 par défaut&nbsp;: au-delà, le programme s'arrête avec l'erreur `RecursionError`.  
Les **langages fonctionnels** modernes possèdent des compilateurs ou des interpréteurs suffisamment «&nbsp;intelligents&nbsp;» pour pallier ces inconvénients.
{{< /note >}}

## Si l'on devait résumer l'idée générale de la récursivité

{{< note tip >}}
Si un problème est facile à résoudre, le résoudre immédiatement.
: *C'est le cas de base*.

Si un problème n'est pas facile à résoudre, le découper en problèmes plus petits. Résoudre les plus petits problèmes.
: *Ce sont les appels récursifs*.
{{< /note >}}

## Exercices du chapitre

Penser à écrire, pour chacune des fonctions ci-dessous, sa spécification ainsi qu'un jeu de tests.

{{< note exercise >}}

#### Exercice 1&nbsp;: Factorielle

Écrire la définition itérative de la fonction factorielle.
{{< /note >}}

{{< solution "Solution" >}}

```python
def factorielle_iter(n: int) -> int:
    """
    Calcule la factorielle de n.
    Algorithme itératif.

    HYPOTHÈSE : n est un entier naturel
    """
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def factorielle_rec(n: int) -> int:
    """
    Calcule la factorielle de n.
    Algorithme récursif.

    HYPOTHÈSE : n est un entier naturel
    """
    if n == 0:
        return 1
    else:
        return n * factorielle_rec(n - 1)
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 2&nbsp;: Compte à rebours

- Écrire une fonction récursive qui, à partir d'un argument entier, affiche un compte à rebours.
- En modifiant seulement la position de la fonction `print`, faire en sorte que le comptage se fasse dans l'ordre croissant.
{{< /note >}}

{{< solution "Solution" >}}

```python
def compte_a_rebours(n: int) -> None:
    """
    Affiche un compte à rebours à l'écran.
    """
    if n == 0:
        print(n)
    else:
        print(n, end=" ")
        compte_a_rebours(n - 1)


def compte(n: int) -> None:
    """
    Affiche un comptage à l'écran.
    """
    if n == 0:
        print(n, end=" ")
    else:
        compte(n - 1)
        print(n, end=" ")
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 3&nbsp;: Somme des $N$ premiers entiers

Écrire les versions itérative et récursive d'une fonction qui calcule la somme des $N$ premiers entiers. La tester pour $N = 15$.
{{< /note >}}

{{< solution "Solution" >}}

```python
def somme_entiers_rec(n: int) -> int:
    """
    Calcule la somme des n premiers entiers.
    Algorithme récursif.

    HYPOTHÈSE : n entier naturel
    """
    if n == 0:
        return 0
    else:
        return n + somme_entiers_rec(n - 1)


def somme_entiers_iter(n: int) -> int:
    """
    Calcule la somme des n premiers entiers.
    Algorithme itératif.

    HYPOTHÈSE : n entier naturel
    """
    somme = 0
    for i in range(n + 1):
        somme += i
    return somme
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 4&nbsp;: Multiplication récursive

Écrire une fonction récursive qui calcule le produit de deux nombres entiers positifs en utilisant des additions.

Le principe est le suivant&nbsp;:
$$
a \times b = \left\lbrace
                \begin{array}{ll}
                    0                   & \text{ si } a = 0\cr
                    (a-1) \times b + b & \text{ si } a > 0\cr
                \end{array}
            \right.
$$

Exécuter la fonction pour $a = 4$ et $b = 5$ (pour cela, présenter les appels récursifs successifs sous forme d'un arbre), puis pour $a = 5$ et $b = 4$.  
Pour quel appel l'arbre est-il le plus grand&nbsp;?  
Noter sur quel argument porte la récursion.  
Que peut-on en conclure&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

```python
def multiplication(a: int, b: int) -> int:
    """
    Réalise la multiplication de deux entiers naturels a et b.
    """
    if a == 0:
        return 0
    else:
        return multiplication(a - 1, b) + b
```

`multiplication(4, 5)` provoque 5 appels (pour $a = 4, 3, 2, 1, 0$) et `multiplication(5, 4)` en provoque 6. La récursion porte sur $a$ seulement&nbsp;: le nombre d'appels vaut $a + 1$, quelle que soit la valeur de $b$. Il vaut donc mieux passer le plus petit des deux nombres en premier argument.

{{< /solution >}}

{{< note exercise >}}

#### Exercice 5&nbsp;: Calculs de puissances

- Écrire une fonction récursive qui calcule $x^n$ sachant que&nbsp;:
$$
    x^n = \left\lbrace
            \begin{array}{ll}
                1                   & \text{ si } n = 0 \cr
                x^{n-1} \times x     & \text{ si } n > 0 \cr
            \end{array}
        \right.
$$

- Écrire une fonction récursive qui calcule $x^n$ sachant que&nbsp;:
$$
    x^n = \left\lbrace
            \begin{array}{ll}
                1                   & \text{ si } n = 0\cr
                (x^{n/2})^2         & \text{ si } n > 0 \text{ pair}\cr
                (x^{(n-1)/2})^2  \times x       & \text{ si } n > 0 \text{ impair}\cr
            \end{array}
        \right.
$$

- Comparer les exécutions (avec arbre des appels) des deux fonctions ci-dessus pour $n = 11$ et $x = 2$. Quel est l'arbre le plus court&nbsp;? Que peut-on en conclure&nbsp;?
{{< /note >}}

{{< solution "Solutions" >}}

```python
def puissance_01(x: float, n: int) -> float:
    """
    Premier calcul de la puissance n du nombre x.

    HYPOTHÈSE : n entier naturel.
    """
    if n == 0:
        return 1
    else:
        return puissance_01(x, n - 1) * x


def puissance_02(x: float, n: int) -> float:
    """
    Second calcul de la puissance n du nombre x.

    HYPOTHÈSE : n entier naturel.
    """
    if n == 0:
        return 1
    elif n % 2 == 0:
        # mise en mémoire du résultat de l'appel récursif
        inter = puissance_02(x, n // 2)
        return inter * inter
    else:
        # mise en mémoire du résultat de l'appel récursif
        inter = puissance_02(x, (n - 1) // 2)
        return inter * inter * x
```

On utilise la division entière `//`&nbsp;: avec `/`, le deuxième argument deviendrait un flottant (`5.0` au lieu de `5`).

Pour $n = 11$, `puissance_01` provoque 12 appels ($n = 11, 10, \ldots, 0$), alors que `puissance_02` n'en provoque que 5 ($n = 11, 5, 2, 1, 0$). Comme $n$ est divisé par 2 à chaque appel, le nombre d'appels de la seconde fonction augmente très lentement avec $n$&nbsp;: pour $n = 1000$, il y en a 11 au lieu de 1001. C'est l'**exponentiation rapide**.

{{< /solution >}}

{{< note exercise >}}

#### Exercice 6&nbsp;: Suite de Fibonacci

- Écrire une fonction récursive qui calcule le $n^{\text{ième}}$ terme de la «&nbsp;suite de Fibonacci&nbsp;» définie par&nbsp;:
$$
\begin{aligned}
u_0 & = 0 \cr
u_1 & = 1 \cr
u_n & = u_{n - 1} + u_{n - 2} \hspace{0.5cm} \text{pour } n \geqslant 2
\end{aligned}
$$
Exécuter la fonction pour $n = 5$

- L'arbre des appels est représenté sur la figure ci-dessous. Expliquer pourquoi cette fonction est très peu efficace.

<img src="/terminales-nsi/chap-1/im-1-3.jpg" width="70%" alt="" />
{{< /note >}}

{{< solution "Solution" >}}

```python
def fibonacci(n: int) -> int:
    """
    Calcule le terme n de la suite de Fibonacci.

    HYPOTHÈSE : n entier naturel
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

`fibonacci(5)` retourne 5. L'arbre des appels montre que les mêmes calculs sont refaits plusieurs fois&nbsp;: `fibonacci(3)` est calculé 2 fois, `fibonacci(2)` 3 fois, et l'appel `fibonacci(5)` provoque 15 appels en tout. Ce nombre d'appels augmente aussi vite que la suite elle-même&nbsp;: `fibonacci(30)` en provoque plus de 2,6 millions.

{{< /solution >}}

{{< note exercise >}}

#### Exercice 7&nbsp;: Formule de Viète

On peut obtenir une valeur approchée du nombre $\pi$ grâce à la formule de Viète&nbsp;:
$$
    \pi \approx 2^k \sqrt{2 - \sqrt{2 + \sqrt{2 + \ldots \sqrt{ 2 + \sqrt 2 }  }  } }
$$
où $k$ est le nombre de racines carrées. Plus la valeur de $k$ est grande, meilleure est l'approximation.

On note $r_k$ le nombre formé de $k$ racines carrées imbriquées&nbsp;: $r_1 = \sqrt 2$, $r_2 = \sqrt{2 + \sqrt 2}$, $r_3 = \sqrt{2 + \sqrt{2 + \sqrt 2}}$, etc. On pose $r_0 = 0$. On constate que $r_k = \sqrt{2 + r_{k-1}}$&nbsp;: la définition de $r_k$ est récursive. La formule de Viète s'écrit alors $\pi \approx 2^k \sqrt{2 - r_{k-1}}$.

1. Écrire une fonction récursive nommée `calcul_inter`, qui, à partir d'un entier naturel $k$, calcule la valeur de $r_k$.
2. Écrire une fonction nommée `calcul_pi`, qui, à partir d'un entier $k \geqslant 1$, calcule la valeur approchée de $\pi$.

> Cette fonction doit appeler la fonction `calcul_inter`.

3. Depuis la fonction `main`, appeler la fonction `calcul_pi` avec plusieurs valeurs de $k$ (essayer 5, 10, 15). Comparer au résultat retourné par l'attribut `pi` du module `math`.
4. Essayer maintenant $k = 20$, $k = 25$ puis $k = 30$. Que constate-t-on&nbsp;? Proposer une explication.
{{< /note >}}

{{< note tip "Coup de pouce" >}}
Pour la question 4, calculer `calcul_inter(29)` et le comparer à 2. Combien de chiffres significatifs un flottant conserve-t-il&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

```python
from math import pi, sqrt


def calcul_inter(k: int) -> float:
    """
    Retourne r_k = sqrt(2 + sqrt(2 + ... + sqrt(2))), nombre formé
    de k racines carrées imbriquées (r_0 = 0).

    HYPOTHÈSE : k entier naturel.
    """
    if k == 0:
        return 0.0
    else:
        return sqrt(2 + calcul_inter(k - 1))


def calcul_pi(k: int) -> float:
    """
    Retourne la valeur approchée de pi donnée par la formule de Viète
    avec k racines carrées.

    HYPOTHÈSE : k entier, k >= 1.
    """
    return 2**k * sqrt(2 - calcul_inter(k - 1))


def main() -> None:
    """Compare les valeurs approchées de pi à math.pi."""
    for k in (5, 10, 15, 20, 25, 30):
        approximation = calcul_pi(k)
        print(f"k = {k} : {approximation} (écart : {abs(approximation - pi):.1e})")


if __name__ == "__main__":
    main()
```

| $k$ | 5 | 10 | 15 | 20 | 25 | 30 |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| écart avec $\pi$ | $\pu{1,3e-3}$ | $\pu{1,2e-6}$ | $\pu{8,3e-9}$ | $\pu{3,9e-6}$ | $\pu{2,1e-2}$ | $\pi$ |

L'approximation s'améliore jusqu'à $k = 15$, puis se dégrade&nbsp;: pour $k = 30$, `calcul_pi` retourne 0. Le nombre $r_{k-1}$ est très proche de 2, et un flottant ne conserve qu'environ 16 chiffres significatifs. La différence $2 - r_{k-1}$ perd presque tous ses chiffres exacts, et pour $k = 30$, $r_{29}$ est arrondi à 2 exactement. La formule est juste, mais le calcul en flottants ne l'est plus. Ce n'est pas une erreur de la récursivité.

{{< /solution >}}

{{< note exercise >}}

#### Exercice 8&nbsp;: Plus grand diviseur commun

Écrire une fonction récursive qui retourne le plus grand diviseur commun de deux entiers passés comme arguments. On se servira de l'algorithme d'Euclide&nbsp;:<span id="pgcd">  </span>
$$
\text{pgcd}(m,n) = \left\lbrace
        \begin{array}{ll}
            m                        & \text{ si } n = 0\cr
            \text{pgcd}(n,m)         & \text{ si } m < n \cr
            \text{pgcd}(n, m \, \text{mod}\, n)  & \text{ sinon }\cr
        \end{array}
    \right.
$$
{{< /note >}}

{{< solution "Solution" >}}

```python
def pgcd(m: int, n: int) -> int:
    """
    Calcule le pgcd de m et n. La récursivité est terminale.

    HYPOTHÈSE : n et m entiers naturels
    """
    if n == 0:
        return m
    elif m < n:
        return pgcd(n, m)
    else:
        return pgcd(n, m % n)
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 9&nbsp;: Ackermann-Péter

La fonction d'Ackermann-Péter est définie récursivement comme suit&nbsp;:
$$
A(m,n) = \left\lbrace
        \begin{array}{ll}
            n+1                        & \text{ si } m = 0\cr
            A(m-1,1)         & \text{ si } m > 0 \text{ et } n = 0 \cr
            A(m-1, A(m, n-1))  & \text{ si } m > 0 \text{ et } n > 0\cr
        \end{array}
    \right.
$$
Écrire une fonction qui, à partir de deux arguments $m$ et $n$, calcule $A(m,n)$. La tester avec les valeurs $m=3$, $n=4$ (le résultat doit être 125).

#### Remarques

- La fonction d'Ackermann croît extrêmement rapidement&nbsp;: $A(4,2)$ a déjà $\pu{19729}$ chiffres&nbsp;!
- La fonction d'Ackermann demandant beaucoup de calculs même pour de petites entrées, elle est parfois utilisée comme programme de test d'une implémentation d'un langage de programmation&nbsp;: en particulier, elle utilise de façon très exigeante la récursivité (cf. [Fonction d'Ackermann, Wikipédia](https://fr.wikipedia.org/wiki/Fonction_d'Ackermann)).
{{< /note >}}

{{< solution "Solution" >}}

```python
def ackermann(m: int, n: int) -> int:
    """
    Définition de la fonction d'Ackermann.

    HYPOTHÈSE : m, n entiers naturels
    """
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 10&nbsp;: Récursivité croisée

On considère deux suites $u(n)$ et $v(n)$ définies, pour $n \geq 0$ par&nbsp;:
$$
\begin{array}{rcl}
    u(0) & = & 1\cr
    v(0) & = & 2\cr
    u(n) & = & 3 u(n-1) + 2 v(n-1)\cr
    v(n) & = & 2 u(n-1) + 3 v(n-1)\cr
    \end{array}
$$
Ces deux suites ont pour particularité que&nbsp;: $v(n) - u(n) = 1$ pour tout $n$.

- Écrire un programme qui, à l'aide de fonctions récursives, donne les valeurs de ces deux suites pour un $n$ donné (tester avec $n=3$) et qui vérifie que la différence entre ces deux valeurs est égale à 1.

- Établir les *arbres des appels*.
{{< /note >}}

{{< solution "Solution" >}}

```python
def u(n: int) -> int:
    """
    Calcul de la valeur de u(n).
    """
    if n == 0:
        return 1
    else:
        return 3 * u(n - 1) + 2 * v(n - 1)


def v(n: int) -> int:
    """
    Calcul de la valeur de v(n)
    """
    if n == 0:
        return 2
    else:
        return 2 * u(n - 1) + 3 * v(n - 1)


def main() -> None:
    """Fonction principale."""
    n = int(input("Entrer la valeur de n : "))
    u_n = u(n)
    v_n = v(n)

    print(f"u({n}) = {u_n}")
    print(f"v({n}) = {v_n}")
    print(f"v({n}) - u({n}) = {v_n - u_n}")


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 11&nbsp;: Fonctions mutuellement récursives

Le but de cet exercice consiste à écrire les fonctions récursives `est_pair` et `est_impair` *sans utiliser le modulo*.  
La fonction `est_pair` (resp. `est_impair`) retourne `True` si son argument entier est pair (resp. impair).

- $n \in \mathbb{N}$ est impair si $n-1$ est pair.
- $n \in \mathbb{N}$ est pair si $n-1$ est impair.
- $0$ est pair.
- $0$ n'est pas impair.
{{< /note >}}

{{< solution "Solution" >}}

```python
def est_pair(nbre: int) -> bool:
    """
    Détermine si un nombre nbre est pair.

    HYPOTHÈSE : nbre entier naturel
    """
    if nbre == 0:
        return True
    else:
        return est_impair(nbre - 1)


def est_impair(nbre: int) -> bool:
    """
    Détermine si un nombre nbre est impair.

    HYPOTHÈSE : nbre entier naturel
    """
    if nbre == 0:
        return False
    else:
        return est_pair(nbre - 1)


def main() -> None:
    """Fonction principale."""
    n = int(input("Entrer le nombre à tester : "))
    print(f"Est-il pair ? {est_pair(n)}")


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice 12&nbsp;: Conjecture de Syracuse

On appelle **suite de Syracuse** une suite d'entiers naturels définie de la manière suivante&nbsp;: *On part d'un nombre entier plus grand que zéro. S'il est pair, on le divise par 2&nbsp;; s'il est impair, on le multiplie par 3 et on ajoute 1. En répétant l'opération, on obtient une suite d'entiers positifs dont chacun ne dépend que de son prédécesseur.*

Par exemple, à partir de 14, on construit la suite des nombres&nbsp;:
$$
    14,7,22,11,34,17,52,26,13,40,20,10,5,16,8,4,2,1,4,2,\ldots
$$
C'est ce qu'on appelle la suite de Syracuse du nombre 14. Une fois le nombre 1 atteint, la suite des valeurs $(1, 4, 2, 1, 4, 2, \ldots)$ se répète indéfiniment en un cycle de longueur 3 (appelé cycle trivial).

La **conjecture de Syracuse** (encore appelée conjecture de Collatz, ou conjecture d'Ulam) est l'hypothèse mathématique selon laquelle la suite de Syracuse de n'importe quel entier strictement positif atteint 1.

Écrire la fonction `syracuse` à un paramètre entier qui retourne le nombre de termes de la suite de Syracuse de cet entier, depuis l'entier de départ jusqu'au premier 1 inclus. Par exemple, `syracuse(14)` retourne 18.
{{< /note >}}

{{< solution "Solution" >}}

```python
def syracuse(n: int) -> int:
    """
    Retourne la longueur de la suite de Syracuse de n, c'est-à-dire
    le nombre de termes depuis n jusqu'au premier 1 inclus.
    Récursivité enveloppée.

    HYPOTHÈSE : n entier strictement positif.

    >>> syracuse(14)
    18
    >>> syracuse(1)
    1
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + syracuse(n // 2)
    else:
        return 1 + syracuse(n * 3 + 1)
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de ce chapitre, je sais…" >}}
- écrire la définition récursive d'une fonction sur les entiers, avec un ou plusieurs cas de base et un ou plusieurs appels récursifs ;
- vérifier que les appels récursifs finissent par atteindre un cas de base ;
- dérouler à la main l'exécution d'une fonction récursive et dessiner son arbre des appels ;
- programmer une fonction récursive en Python ;
- écrire la version itérative d'une fonction récursive, et inversement ;
- compter les appels provoqués par une fonction récursive, et expliquer pourquoi le calcul récursif naïf de la suite de Fibonacci est très lent ;
- écrire des fonctions mutuellement récursives.
{{< /note >}}

Le document suivant applique la récursivité aux chaînes de caractères et aux listes.
