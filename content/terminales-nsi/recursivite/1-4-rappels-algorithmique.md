---
title: "Rappels d'algorithmique"
subtitle: ""
date: 2020-09-12T17:46:07+04:00
draft: false
toc: true
tags: ["Algorithmique", "Complexité", "Terminaison", "Invariant", "Variant", "Correction"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: true
auto_numbering: true
weight: 104
---

{{< note goal >}}
Revoir les outils qui permettent d'étudier un algorithme&nbsp;: sa complexité, la preuve de sa terminaison à l'aide d'un variant de boucle et la preuve de sa correction à l'aide d'un invariant de boucle.
{{< /note >}}

Avant de commencer&nbsp;: un programme parcourt une fois une liste de $N$ éléments et met 1 seconde pour $N = 10^6$. Combien de temps faut-il prévoir pour $N = 10^7$&nbsp;? Et pour un programme qui compare chaque élément à tous les autres, qui met lui aussi 1 seconde pour $N = 10^6$&nbsp;?

{{< solution "Réponse" >}}
Le premier programme effectue un nombre d'opérations proportionnel à $N$&nbsp;: si $N$ est multiplié par 10, la durée aussi, soit environ 10 secondes. Le second effectue environ $N^2$ comparaisons&nbsp;: si $N$ est multiplié par 10, la durée est multipliée par $10^2 = 100$, soit environ 100 secondes. Prévoir l'évolution de la durée quand la taille des données augmente, sans avoir à exécuter le programme, c'est exactement le rôle de la complexité.
{{< /solution >}}

## Algorithmique

<!--
### Introduction
-->

{{< note tip >}}
Un **algorithme** est une *suite finie et non ambiguë
d'opérations ou d'instructions* à réaliser afin de résoudre un problème.
{{< /note >}}

En informatique, pour qu'un algorithme puisse être implémenté, il est
nécessaire de s'assurer que la «&nbsp;suite finie et non ambiguë d'opérations ou
d'instructions à réaliser&nbsp;» s'effectue en une **durée finie**.

{{< note tip >}}
Lorsqu'on élabore ou étudie un algorithme, il est donc nécessaire de
vérifier&nbsp;:

- **Sa finitude&nbsp;:** Il doit se terminer en un temps fini.
- **Sa correction&nbsp;:** Il doit (généralement) donner le bon résultat.
- **Sa performance&nbsp;:** Plusieurs algorithmes peuvent permettre de résoudre une même
classe de problèmes. Ils ne nécessiteront cependant pas tous l'utilisation de
la même quantité de mémoire ou le même nombre d'étapes de calcul, donc la
même durée.
{{< /note >}}

#### Remarques

- Ce n'est pas toujours une mauvaise nouvelle si certains algorithmes ont besoin d'un «&nbsp;temps infini&nbsp;» pour résoudre un problème&nbsp;: certains choix en cryptographie reposent sur l'idée que «&nbsp;casser&nbsp;» la protection nécessite une durée de calcul trop grande, pour le matériel dont on dispose *aujourd'hui*.
- Pour certains problèmes on doit se contenter d'une *solution approchée* et pas d'une *solution exacte*.

{{< note tip >}}
La performance d'un algorithme porte sur deux aspects&nbsp;: la **durée du
calcul**  et la **quantité de mémoire**  nécessaires à la résolution du
problème. *Malheureusement ces deux points s'opposent*. Il est souvent
nécessaire d'occuper davantage de mémoire pour gagner en temps de calcul, ou
d'écrire plus d'instructions, et donc faire plus de calculs, pour aboutir à
une gestion de la mémoire optimale.
{{< /note >}}

Conformément au programme, on limite la *performance algorithmique*  à la **complexité algorithmique**.

## Notion de complexité algorithmique

### Introduction

{{< note tip >}}
La **complexité algorithmique** donne des informations
sur la **durée du calcul**  nécessaire à la résolution du problème. Plus
la complexité algorithmique est petite, moins de calculs sont effectués et
plus l'algorithme est performant (sous réserve que la gestion de l'espace
mémoire utilisé par l'implémentation de l'algorithme ne constitue pas un
problème).
{{< /note >}}

{{< note warning >}}
On exprime la complexité d'un algorithme en fonction de la **taille (nombre)
des données qu'il manipule**  en considérant que *chaque instruction
élémentaire s'effectue en temps constant*.
{{< /note >}}

Il existe plusieurs méthodes pour analyser la complexité d'un algorithme,
comme&nbsp;:

- **L'analyse moyenne&nbsp;:** Il s'agit d'*évaluer comment varie la **durée moyenne** des
calculs à effectuer en fonction du nombre de données manipulées*.

- **L'analyse optimiste&nbsp;:** Il s'agit d'*évaluer comment varie le nombre de calculs à
effectuer, dans le **scénario le plus favorable**, en fonction du nombre de
données manipulées*.  
Par exemple, on cherche une valeur dans une liste et c'est la première qui apparaît lors de cette recherche.

- **L'analyse pessimiste (ou du pire cas)&nbsp;:** Il s'agit d'*évaluer comment varie le
nombre de calculs à effectuer, dans le **scénario le moins favorable**, en
fonction du nombre de données manipulées*.
Par exemple, on cherche une valeur dans une liste alors qu'elle n'est pas présente dans la liste.

> *Lorsqu'on utilise le résultat de l'analyse du «&nbsp;pire cas&nbsp;», aucune
mauvaise surprise ne peut intervenir, le pire cas a été envisagé à
l'avance.*

Les complexités des différents algorithmes varient beaucoup. On peut
néanmoins regrouper les algorithmes en quelques grandes familles&nbsp;:

- **Complexité constante&nbsp;:** Leur notation est de la forme $O(1)$. Ces algorithmes sont indépendants du nombre de données à traiter.
{{< note normal >}}
La **complexité constante** apparaît dans la *recherche par index dans un tableau*.  
*La complexité  constante est la plus «&nbsp;performante&nbsp;».*
{{< /note >}}

- **Les algorithmes logarithmiques&nbsp;:** Leur notation est de la forme $O(\log N)$. Ces
algorithmes sont très performants en temps de traitement. *Le nombre de calculs
dépend du logarithme du nombre de données à traiter*.  
Sur la Figure ci-dessous, on peut constater que, *plus le nombre de données $N$ à
traiter est important, moins le nombre de calculs à effectuer augmente
rapidement&nbsp;: la valeur de la dérivée est de moins en moins grande*.  
La fonction logarithme à utiliser dépend du problème étudié mais, comme
la complexité est définie à un facteur près, la base du logarithme n'a pas
d'importance.

{{< note normal >}}
La **complexité logarithmique** apparaît dans les problèmes dans lesquels
l'ensemble des données peut être décomposé en deux parties égales, qui
sont elles-mêmes décomposées en 2 (recherche par dichotomie, recherche dans un arbre binaire, etc.).  
*La **complexité logarithmique** est très «&nbsp;performante&nbsp;».*
{{< /note >}}

{{< note warning >}}
Le logarithme à utiliser est alors
la fonction réciproque de $f : x \longmapsto 2^x$, c'est-à-dire $\log_{2}$.  
On en retient une version entière, appelée <b>logarithme entier</b>&nbsp;: c'est le <b>nombre de fois qu'il faut diviser un nombre $x$ supérieur ou égal à 1 par deux pour obtenir un nombre inférieur ou égal à 1</b>. Par exemple, $8 \to 4 \to 2 \to 1$&nbsp;: le logarithme entier de 8 est 3, et $\log_2 8 = 3$.
{{< /note >}}

- **Les algorithmes linéaires&nbsp;:** Leur notation est de la forme $O(N)$. *Ces
algorithmes sont rapides. Le nombre de calculs dépend, de manière **linéaire**,
du nombre de données initiales à traiter*.

{{< note normal >}}
La **complexité linéaire** apparaît dans les problèmes dans lesquels *on
parcourt séquentiellement l'ensemble des données* pour réaliser une
opération (recherche d'une valeur, par exemple).  
*La complexité linéaire est considérée comme «&nbsp;efficace&nbsp;».*
{{< /note >}}

- **Les algorithmes linéaires et logarithmiques (quasi-linéaire)&nbsp;:** Leur notation est de la forme $O(N \log N)$.

{{< note normal >}}
La **complexité linéaire et logarithmique** apparaît dans des problèmes dans lesquels on *découpe répétitivement les données en deux parties, que l'on parcourt
séquentiellement* ensuite (tri Quicksort par exemple).  
*La complexité quasi-linéaire est considérée comme «&nbsp;assez efficace&nbsp;».*
{{< /note >}}

- **Les algorithmes de type polynomial&nbsp;:** Leur notation est de la forme $O(N^k)$ où
$k$ est la puissance.

{{< note normal >}}
Une complexité **quadratique** apparaît, par exemple, lorsqu'on parcourt un
*tableau à deux dimensions*, lorsqu'on effectue un tri par comparaison, etc.  
*La complexité polynomiale est considérée comme «&nbsp;moyennement efficace&nbsp;».*
{{< /note >}}

- **Les algorithmes exponentiels ou factoriels&nbsp;:** Leur notation est de la forme $O(e^N)$ ou $O(N!)$. Ce sont les algorithmes les plus complexes.  
Le nombre de calculs augmente de façon **exponentielle ou factorielle** en
fonction du nombre de données à traiter. Un algorithme de complexité
exponentielle traitera, dans le pire des cas, un ensemble de 10 données en
effectuant 22026 calculs&nbsp;; un ensemble de 100 données en effectuant $\pu{2,688e43}$ calculs&nbsp;!!!
On dit généralement que les problèmes qui ne sont résolus que par ce type d'algorithmes sont
«&nbsp;intraitables&nbsp;» en pratique&nbsp;: ils sont calculables, mais la durée du calcul devient vite inaccessible.

{{< note normal >}}
On rencontre les algorithmes de type **exponentiels ou factoriels** dans les problématiques liées à la
programmation de fonctions humaines comme la vision, la reconnaissance des
formes ou l'intelligence artificielle.
{{< /note >}}

<img src="/terminales-nsi/chap-1/fig-16-1.png" alt="" width="80%" />
<img src="/terminales-nsi/chap-1/fig-16-2.png" alt="" width="80%" />

<center>

| Complexité | Durée pour $N = 10^6$ |
|:-:|:-:|
| Logarithmique&nbsp;: $O(\log N)$ | 20 ns |
| Linéaire&nbsp;: $O(N)$ | 1 ms |
| Quadratique&nbsp;: $O(N^2)$ | 1/4 heure |
| Polynomiale&nbsp;: $O(N ^k)$ | 30 ans si $k=3$ |
| Exponentielle&nbsp;: $O(2^N)$  | plus de $10^{300000}$ milliards d'années |

</center>

> Ordres de grandeur des durées d'exécution d'un problème de taille $10^6$ sur un ordinateur à un milliard d'opérations par seconde («&nbsp;Informatique pour tous en CPGE&nbsp;», éditions Eyrolles).

### Quelques règles simples permettant de déterminer la complexité d'un algorithme

Nous allons introduire, dans cette partie, quelques règles simples qui permettent de se faire une idée de l'efficacité d'un algorithme&nbsp;:

- Une **affectation** ou l'**évaluation d'une expression** ont un temps d'exécution petit. *Cette durée constitue souvent l'unité de base dans laquelle on mesure le temps d'exécution d'un algorithme*.
- Le temps pris pour exécuter une séquence d'instructions `p q` est la *somme des temps pris pour exécuter les instructions `p` puis `q`.*
- Le temps pris pour exécuter un test `Si (b) Alors p Sinon q FinSi` est *inférieur ou égal au maximum des temps pris pour exécuter les instructions `p` et `q`, plus une unité qui correspond au temps d'évaluation de l'expression `b`.*
- Le temps pris pour exécuter une boucle `Pour i variant de 1 à m par pas de 1 Faire p FinPour` est *$m$ fois le temps pris pour exécuter l'instruction p si ce temps ne dépend pas de la valeur de i.*
En particulier, quand deux boucles sont imbriquées, le corps de la boucle interne est répété à cause de cette boucle, mais aussi parce qu'elle-même est répétée dans son intégralité. Ainsi, si les deux boucles sont répétées respectivement $m$ et $m\rq$ fois, alors le corps de la boucle interne est exécuté $m \times m\rq$ fois en tout.  
Quand le temps d'exécution du corps de la boucle dépend de la valeur de l'indice $i$, le temps total d'exécution de la boucle est la somme des temps d'exécution du corps de la boucle pour chaque valeur de $i$.
- Le cas des boucles `Tantque` est plus complexe puisque le nombre d'itérations n'est en général pas connu a priori. Il doit être évalué au cas par cas.

{{< note exercise >}}
Pour chacun des programmes suivants, dire en fonction de $n$ quel est le nombre d’opérations `op` que le programme effectue. Justifier votre résultat.

1.

```pseudo
Pour i de 1 à n Faire 
    op
```

2.

```pseudo
Pour i de 1 à n Faire 
    op; op
```

3.

```pseudo
Pour i de 1 à n Faire
    Pour j de 1 à n Faire 
        op
```

4.

```pseudo
Pour i de 1 à n Faire 
    Pour j de 1 à n Faire
        Pour k de 1 à n Faire
            op
```

5.

```pseudo
Pour i de 1 à n Faire
    op; op
    Pour j de 1 à n Faire
        op
        Pour k de 1 à n Faire
            op
```

6.

```pseudo
Pour i de 1 à n Faire
    Pour j de 1 à i Faire 
        op
```

7.

```pseudo
i ⟵ 1
j ⟵ 1
TantQue (i ≤ m) et (j ≤ n) Faire
    op
    i ⟵ i + 1 
    j ⟵ j + 1
```

8.

```pseudo
i ⟵ 1
j ⟵ 1
TantQue (i ≤ m) ou (j ≤ n) Faire
    op
    i ⟵ i + 1 
    j ⟵ j + 1
```

9.

```pseudo
Tant que n > 0 Faire 
    op
    n ⟵ n // 2
```

{{< /note >}}

{{< solution "Réponses" >}}

1. $n$ opérations.
2. $2n$ opérations.
3. La boucle intérieure effectue $n$ opérations, et elle est répétée $n$ fois&nbsp;: $n^2$ opérations.
4. $n^3$ opérations.
5. À chaque tour de la boucle sur $i$&nbsp;: 2 opérations, puis $n$ fois (1 opération et $n$ opérations), soit $2 + n(1 + n)$. Au total&nbsp;: $n(2 + n + n^2) = n^3 + n^2 + 2n$ opérations. Pour $n$ grand, c'est le terme $n^3$ qui l'emporte.
6. Pour $i$ donné, la boucle intérieure effectue $i$ opérations&nbsp;: $1 + 2 + \ldots + n = \dfrac{n(n+1)}{2}$ opérations, c'est-à-dire de l'ordre de $n^2$.
7. $i$ et $j$ augmentent ensemble&nbsp;; la boucle s'arrête dès que l'un des deux dépasse sa borne&nbsp;: $\min(m, n)$ opérations.
8. La boucle continue tant que l'un des deux ne dépasse pas sa borne&nbsp;: $\max(m, n)$ opérations.
9. $n$ est divisé par deux à chaque tour, jusqu'à atteindre 0&nbsp;: pour $n \geqslant 1$, il y a $\lfloor \log_2 n \rfloor + 1$ opérations (4 pour $n = 8$&nbsp;: $8, 4, 2, 1$), et aucune pour $n = 0$.

{{< /solution >}}

### Comment illustrer l'influence du nombre d'éléments passés en entrée

{{< note exercise >}}

#### Quelques complexités à tout de suite identifier

En utilisant la fonction `perf_counter` du module `time` (plus précise que la fonction `time`), écrire le code de fonctions qui :

1. montre que le temps d'accès à un élément d'une liste est en $O(1)$ ;
2. montre que la recherche linéaire dans une liste est en $O(N)$ ;
3. met en évidence la complexité de l'opérateur Python `in` ;
4. montre que la recherche linéaire dans une liste à deux dimensions est en $O(N^2)$ ;
5. montre que la recherche dichotomique dans une liste triée est en $O(\log(N))$.

{{< /note >}}

{{< note tip "Coup de pouce" >}}
`perf_counter()` retourne un instant, en secondes. On l'appelle juste avant et juste après le calcul&nbsp;: la différence est la durée du calcul. Pour une opération très rapide, on la répète un grand nombre de fois et on divise. On compare ensuite les durées obtenues pour des listes de $10^4$, $10^5$ et $10^6$ éléments&nbsp;: comment évolue la durée quand $N$ est multiplié par 10&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

```python
from collections.abc import Callable
from time import perf_counter


def duree(calcul: Callable[[], object], repetitions: int = 10) -> float:
    """Retourne la durée moyenne, en secondes, d'un appel à calcul."""
    debut = perf_counter()
    for _ in range(repetitions):
        calcul()
    return (perf_counter() - debut) / repetitions


def recherche_lineaire(liste: list[int], valeur: int) -> bool:
    """Recherche séquentielle de valeur dans liste."""
    for element in liste:
        if element == valeur:
            return True
    return False


def recherche_tableau(tableau: list[list[int]], valeur: int) -> bool:
    """Recherche séquentielle de valeur dans un tableau à deux dimensions."""
    for ligne in tableau:
        for element in ligne:
            if element == valeur:
                return True
    return False


def recherche_dichotomique(liste: list[int], valeur: int) -> bool:
    """Recherche dichotomique de valeur dans la liste triée liste."""
    gauche, droite = 0, len(liste) - 1
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        if liste[milieu] == valeur:
            return True
        elif liste[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return False


def main() -> None:
    """Affiche les durées mesurées pour des listes de tailles croissantes."""
    for n in (10_000, 100_000, 1_000_000):
        liste = list(range(n))  # liste triée ; -1 est absent : pire des cas
        print(f"N = {n}")
        print(f"  accès à un élément : {duree(lambda: liste[n // 2], 10_000):.1e} s")
        print(f"  recherche linéaire : {duree(lambda: recherche_lineaire(liste, -1)):.1e} s")
        print(f"  opérateur in       : {duree(lambda: -1 in liste):.1e} s")
        print(f"  dichotomie         : {duree(lambda: recherche_dichotomique(liste, -1), 10_000):.1e} s")
    for cote in (100, 300, 1000):
        tableau = [[0] * cote for _ in range(cote)]
        print(f"tableau {cote} x {cote} : {duree(lambda: recherche_tableau(tableau, -1)):.1e} s")


if __name__ == "__main__":
    main()
```

Quand $N$ est multiplié par 10, la durée d'accès à un élément ne change pas ($O(1)$), celle de la recherche linéaire et de l'opérateur `in` est multipliée par 10 environ ($O(N)$&nbsp;: `in` effectue lui aussi une recherche séquentielle, mais plus vite, car il est programmé en langage C), et celle de la dichotomie n'augmente presque pas ($O(\log N)$). Pour le tableau, quand le côté $N$ est multiplié par 3 puis par 10/3, la durée est multipliée par 9 environ, puis par 11&nbsp;: elle est proportionnelle à $N^2$, le nombre de cases.

{{< /solution >}}

## Terminaison d'un algorithme itératif&nbsp;: variant de boucle

La structure qui généralement doit retenir l'attention lors de l'analyse de
la terminaison d'un algorithme est la **structure de boucle**.

{{< note tip >}}
On appelle **variant** d'une boucle une *fonction qui a
pour variables les variables du problème, qui retourne une valeur entière positive et
qui décroît à chacune des itérations de la boucle, jusqu'à s'annuler ou
prendre une valeur constante négative qui dépend de la condition d'arrêt de
la boucle*.

**La découverte d'un variant de boucle permet de conclure que la boucle se
termine** puisqu'il n'existe aucune suite infinie strictement décroissante d'entiers naturels.
{{< /note >}}

### Exemple 1&nbsp;: Calcul de la plus petite puissance de deux supérieure ou égale à un entier $n$  

-----

##### Algorithme 1

**Fonction&nbsp;:** *plusPetitePuissance(n)*  
**Entrée&nbsp;:** *entier naturel n*  
**Sortie&nbsp;:** *entier naturel $p$ dont la valeur est égale à la plus petite
puissance de deux supérieure ou égale à $n$.*<br />
**Début**  
<span style="margin-left: 2em;">$p \longleftarrow 1$</span><br />
<span style="margin-left: 2em;">**TantQue**  $p < n$ **Faire**</span><br />
<span style="margin-left: 4em;">$p \longleftarrow 2 p$</span><br />
<span style="margin-left: 2em;">**FinTantQue**</span><br />
<span style="margin-left: 2em;">**Renvoyer**  $p$</span><br />
**Fin**

-----

 {{< note normal >}}
La fonction $f$ d'expression $f(p) = n - p$ est-elle un variant de boucle&nbsp;?

- $f(p)$ est un entier.
- Tant que $p < n$, $f(p) > 0$&nbsp;: tant que la boucle tourne, $f(p)$ est un entier naturel.
- $f$ décroît sur l'ensemble des valeurs de $p$ puisque $$f(p_{i+1}) - f(p) = n - p_{i+1} - n + p_{i} = p_{i} - p_{i+1} = p_{i} - 2p_{i} = - p_{i} <0$$
- *Condition d'arrêt&nbsp;:* $p_{max} \geqslant n$, donc $f (p_{max}) \leqslant 0$.

La fonction $f$ est un variant de boucle et la boucle se termine donc bien.
{{< /note >}}

### Exemple 2&nbsp;: Palindrome

-----

##### Algorithme 2

**Fonction&nbsp;:** *palindrome(m)*<br />
**Entrée&nbsp;:** *chaîne de caractères m*<br />
**Sortie&nbsp;:** *booléen Vrai si la chaîne de caractères m est un palindrome, Faux sinon* <br />
**Début**  
<span style="margin-left: 2em;">$i \longleftarrow 0$</span><br />
<span style="margin-left: 2em;">$j \longleftarrow \text{longueur} (m) - 1$</span><br />
<span style="margin-left: 2em;">**TantQue**  $i \leqslant j$ **Faire**</span><br />
<span style="margin-left: 4em;">**Si**  $m[i] = m[j]$ **Alors**</span><br />
<span style="margin-left: 6em;">$i \longleftarrow i + 1$</span><br />
<span style="margin-left: 6em;">$j \longleftarrow j - 1$</span><br />
<span style="margin-left: 4em;">**Sinon**</span><br />
<span style="margin-left: 6em;">**Renvoyer**  Faux</span><br />
<span style="margin-left: 4em;">**FinSi**</span><br />
<span style="margin-left: 2em;">**FinTantQue**</span><br />
<span style="margin-left: 2em;">**Renvoyer**  Vrai</span><br />
**Fin**

-----

1. Décrire au moyen d'un tableau indiquant l'évolution des valeurs des
   variables le fonctionnement de l'algorithme 2 pour la chaîne de caractères
   «&nbsp;sauras&nbsp;» puis pour la chaîne de caractères «&nbsp;radar&nbsp;».  
   **Remarque&nbsp;:** Le premier élément d'une chaîne a pour indice 0.
{{< solution "Réponse" >}}

- Pour l'entrée «&nbsp;sauras&nbsp;»&nbsp;:  
$i$&nbsp;: 0, 1, 2  
$j$&nbsp;: 5, 4, 3  
La fonction retourne `Faux`.

- Pour l'entrée «&nbsp;radar&nbsp;»&nbsp;:  
$i$&nbsp;: 0, 1, 2, 3  
$j$&nbsp;: 4, 3, 2, 1  
La fonction retourne `Vrai`.
{{< /solution >}}

2. Montrer que $f(i, j) = j - i$ est un variant de la boucle **TantQue**.
{{< solution "Réponse" >}}
$f(i, j) = j - i$ est-elle un variant de boucle&nbsp;?

- Tant que la boucle tourne, $i \leqslant j$, donc $f(i, j) = j - i$ est un entier naturel.
- $f (i+1, j-1) = j - 1 - (i + 1) = j - 1 - i - 1 = j - i - 2 = f(i, j) - 2 < f(i, j)$.  
La fonction est donc strictement décroissante au fil des tours de boucle.
- *Condition d'arrêt&nbsp;:* $i > j$, donc $f(i, j) = j - i < 0$
{{< /solution >}}

3. En déduire que la boucle **TantQue** se termine.
{{< solution "Réponse" >}}
La fonction $f$ est un variant de boucle. La boucle se termine donc bien.
{{< /solution >}}

## Correction d'un algorithme itératif&nbsp;: invariant de boucle

{{< note tip >}}
On appelle **invariant d'une boucle**  une *propriété qui,
si elle est vraie avant l'exécution d'une itération, le demeure après
l'exécution de l'itération*.
*Un invariant de boucle doit être vrai avant de commencer la boucle* et est
alors garanti de *rester correct après chaque itération* de la boucle. En
particulier, l'*invariant sera toujours vrai à la fin de la boucle*.
{{< /note >}}

Les boucles et la récursivité étant fondamentalement similaires, il y a peu de
différence entre démontrer un invariant de boucle et prouver qu'un programme
est correct en utilisant un raisonnement par récurrence.

### Exemple 3&nbsp;: Calcul de $2^n$

-----

##### Algorithme 3

**Fonction&nbsp;:** *calculPuissanceDeux(n)*  
**Entrée&nbsp;:** *entier naturel $n$*  
**Sortie&nbsp;:** *entier naturel $p$ dont la valeur est égale à $2^n$*  
**Début**  
<span style="margin-left: 2em;">$p \longleftarrow 1$</span><br />
<span style="margin-left: 2em;">**Pour**  $k$ **allant de**  1 à $n$ **faire**</span><br />
<span style="margin-left: 4em;">$p \longleftarrow 2 p$</span> <br />
<span style="margin-left: 2em;">**FinPour**</span>  <br />
<span style="margin-left: 2em;">**Renvoyer**  $p$</span><br />
**Fin**

-----

{{< note normal >}}
La propriété «&nbsp;Après le tour $k$ de la boucle, $p = 2^k$&nbsp;» est un invariant de
boucle. En effet&nbsp;:

- **Initialisation&nbsp;:** Avant d'entrer dans la boucle&nbsp;: $p = 1 = 2^0$.

- **Conservation&nbsp;:** On suppose l'invariant vérifié au tour $i$ de la boucle&nbsp;: $p =
2^i$. Au tour $i + 1$, $p_{i + 1} = p_{i} \times 2 = 2^i \times 2 = 2^{i + 1}$.

- **Terminaison&nbsp;:** La boucle réalise $n$ tours&nbsp;; au dernier tour $p = 2^{n - 1}
\times 2 = 2^n$

La proposition est donc bien un invariant de boucle et on peut conclure que l'algorithme est correct.
{{< /note >}}

### Exemple 4&nbsp;: Quotient et reste de la division euclidienne d'un entier positif par un entier strictement positif

-----

##### Algorithme 4

**Fonction&nbsp;:**  *division(a, b)*  
**Entrée&nbsp;:** *entier naturel $a$ et entier naturel non nul $b$*  
**Sortie&nbsp;:** *Quotient $q$ et reste $r$ de la division euclidienne
de l'entier naturel $a$ par l'entier naturel non nul $b$*  
**Début**  
<span style="margin-left: 2em;">$q \longleftarrow 0$</span><br />
<span style="margin-left: 2em;">$r \longleftarrow a$</span>  <br />
<span style="margin-left: 2em;">**TantQue**  $r \geqslant b$ **Faire**</span><br />
<span style="margin-left: 4em;">$q \longleftarrow q + 1$</span><br />
<span style="margin-left: 4em;">$r \longleftarrow r - b$</span><br />
<span style="margin-left: 2em;">**FinTantQue**</span><br />
<span style="margin-left: 2em;">**Renvoyer**  $q, r$</span><br />
**Fin**  

-----

1. Décrire le fonctionnement de l'algorithme pour l'entrée (`a = 17`, `b =
   5`) au moyen d'un tableau indiquant l'évolution des valeurs des variables
   au fil des itérations.
{{< solution "Réponse" >}}

$$
\begin{array}{c : c : c : c : c}
a & 17 & 17 & 17 & 17\cr \hdashline
b & 5 & 5 & 5 & 5 \cr \hdashline
q & 0 & 1 & 2 & 3 \cr \hdashline
r & 17 & 12 & 7 & 2 \cr
\end{array}
$$
{{< /solution >}}

2. Montrer que la boucle **TantQue**  se termine en utilisant un *variant de
   boucle*.
{{< solution "Réponse" >}}
La fonction $f(r) = r - b$ peut-elle être un variant de boucle&nbsp;?

- $f(r) = r -b$ est un entier.
- Pour n'importe quel tour de boucle $r \geqslant b$, donc $f(r) = r -b \geqslant 0$.
- Soit $r_2 = r_1 - b$.  
$f(r_2) = r_2 - b = r_1 - b - b = f(r_1) - b < f(r_1)$ car $b > 0$.  
La fonction $f$ est strictement décroissante. (Si $b$ valait 0, $r$ ne diminuerait jamais et la boucle ne s'arrêterait pas&nbsp;: d'où la condition $b \neq 0$.)
- *Condition d'arrêt&nbsp;:* $r < b$, donc $f(r) = r - b < 0$.

La fonction $f$ est bien un variant de boucle et cette boucle se termine.
{{< /solution >}}

3. Montrer que la propriété $a =bq+ r$ est un invariant de la
   boucle **TantQue**, en déduire que l'algorithme produit le résultat
   attendu.
{{< solution "Réponse" >}}
Si la propriété $a =b q+ r$ est un invariant de boucle, elle doit être vraie avant d'entrer dans la boucle, à chaque tour de boucle et une fois la boucle terminée.

- **Initialisation&nbsp;:** Avant d'entrer dans la boucle, $q=0$ et $r=a$. Donc on a bien $a = 0 \times b + a$.
- **Conservation&nbsp;:** On suppose la propriété vraie au rang $k$ quelconque de la boucle&nbsp;: $a = b q_k + r_k$.  
Au rang $k+1$, $q_{k+1} = q_{k} + 1$ et $r_{k+1} = r_k - b$. Donc $a = b q_{k+1} + r_{k+1} = b q_{k} + b + r_k - b = b q_k + r_k$.
- **Terminaison&nbsp;:** La boucle s'arrête lorsque $r < b$. À la sortie de la boucle on a donc bien $a=b q + r$.

La propriété $a =bq+ r$ est bien un invariant de boucle. À la sortie, on a de plus $r < b$ (condition d'arrêt) et $r \geqslant 0$ (on ne retire $b$ à $r$ que lorsque $r \geqslant b$). Les nombres $q$ et $r$ vérifient donc $a = bq + r$ et $0 \leqslant r < b$&nbsp;: ce sont bien le quotient et le reste de la division euclidienne. Le programme est correct.
{{< /solution >}}

<!--
4. Montrer que la propriété $0 \leqslant r < b$ est un invariant de boucle.
{{< solution "Réponse" >}}
Si la propriété $0 \leqslant r$ est un invariant de boucle, elle doit être vraie avant d'entrer dans la boucle, à chaque tour de boucle et une fois la boucle terminée.

- **Initialisation&nbsp;:** Avant d'entrer dans la boucle, $r=a > 0$.
- **Conservation&nbsp;:** On suppose la propriété vraie au rang $k$ quelconque de la boucle&nbsp;: $r_k \geqslant 0$.  
Au rang $k+1$, $r_{k+1} = r_k - b > 0$. On sait que $r_{k+1} > 0$ car on passe au rang $k+1$ uniquement si $r_k > b$.
- **Terminaison&nbsp;:** La boucle s'arrête dès que $r < b$. Donc au dernier tour (et à la sortie, donc) de la boucle on a donc bien encore $b > r \geqslant 0$.

La propriété $0 \leqslant r$ est bien un invariant de la boucle **TantQue** et en déduire que le programme est correct.
{{< /solution >}}

-->

4. Écrire le code Python implémentant l'algorithme 4. La spécification de la fonction est la suivante&nbsp;:

```python
def division_euclidienne(a: int, b: int) -> tuple[int, int]:
    """
    Calcule la division euclidienne de l'entier naturel a par l'entier naturel
    non nul b.
    Retourne les entiers naturels q et r, quotient et reste de cette division.
    """
```

{{< solution "Réponse" >}}

```python
def division_euclidienne(a: int, b: int) -> tuple[int, int]:
    """
    Calcule la division euclidienne de l'entier naturel a par l'entier naturel
    non nul b.
    Retourne les entiers naturels q et r, quotient et reste de cette division.
    """
    assert b > 0, "b doit être un entier naturel non nul"
    q = 0
    r = a
    while r >= b:
        q += 1
        r -= b
    return q, r
```

{{< /solution >}}

5. Écrire un jeu de tests pour la fonction `division_euclidienne`.
{{< solution "Réponse" >}}

```python
assert division_euclidienne(1, 2) == (0, 1)
assert division_euclidienne(2, 1) == (2, 0)
assert division_euclidienne(17, 5) == (3, 2)
```

{{< /solution >}}

## Exercices

{{< note exercise >}}

#### Exercice

On considère la fonction suivante :

```python
def power(n: int) -> int:
    p = 1
    i = 0
    while i < n:
        p = p * 2
        i = i + 1
    return p
```

1. Quel calcul ce code réalise-t-il ?

2. Écrire un jeu de test pour cette fonction.

3. Démontrer que l'algorithme se termine.

4. Démontrer que l'algorithme est correct.

5. Déterminer la complexité de cet algorithme.

{{< /note >}}

{{< solution "Réponses" >}}

1. `power` calcule $2^n$.

2.

```python
assert power(0) == 1
assert power(1) == 2
assert power(10) == 1024
```

3. $f(i) = n - i$ est-il un variant de boucle ?  
    - $f(0) = n$ est un entier naturel.
    - $f(i+1) - f(i) = n - i - 1 - n + i = -1$  
    La suite est strictement décroissante.
    - $i_{max} = n$ donc $f(i_{max}) = n - i_{max} = n - n = 0$.  
$f(i)$ est un variant de boucle, l'algorithme se termine.

4. Invariant de boucle : "À l'issue de chaque itération, $p=2^i$."  
    - **Initialisation :** À l'entrée de la boucle, $i=0$, $2^i = 2^0 = 1 = p$.
    - **Conservation :** On suppose qu'à l'issue du tour de boucle de compteur $k$, $p_k = 2^k$.  
    $p_{k+1} = p_k \times 2 = 2^k \times 2 = 2^{k+1}$.
    - **Terminaison :** Lors du dernier tour de boucle, $i = n - 1$, le calcul effectué est donc $p = 2^{n-1} \times 2= 2^n$.  
    L'algorithme est correct.

5. La boucle effectue $n$ tours, chacun avec un nombre constant d'opérations : la complexité est linéaire, en $O(n)$.

{{< /solution >}}

{{< note exercise >}}

#### Exercice

On considère la fonction suivante :

```python
def maxer(s: list[float]) -> float:
    while len(s) > 1:
        if s[0] > s[1]:
            s.pop(1)
        else:
            s.pop(0)
    return s.pop(0)
```

1. Quelle opération ce code réalise-t-il ?

2. Écrire un jeu de test pour cette fonction.

3. Démontrer que l'algorithme se termine.

4. Démontrer que l'algorithme est correct.

5. Déterminer la complexité de cet algorithme.

6. Existe-t-il un ou des algorithmes qui réalisent la même opération plus efficacement ?

{{< /note >}}

{{< solution "Réponses" >}}

1. La fonction retourne le plus grand élément de la liste (non vide) passée en argument. Attention : elle **vide** cette liste au passage, car `pop` modifie la liste reçue.

2.

```python
assert maxer([3, 8, 1, 5]) == 8
assert maxer([7]) == 7
assert maxer([2, 9, 9, 4]) == 9
assert maxer([-5, -2, -9]) == -2
```

3. Notons $\ell$ la longueur de `s`. $f(\ell) = \ell - 1$ est-il un variant de boucle ?  
    - Tant que la boucle tourne, $\ell > 1$, donc $f(\ell)$ est un entier naturel.
    - Chaque tour retire exactement un élément de `s` avec `pop` : $\ell$ diminue de 1, donc $f$ aussi. La fonction $f$ est strictement décroissante.  
    - La boucle s'arrête quand $\ell = 1$, c'est-à-dire quand $f(\ell) = 0$.  
    $f$ est un variant de boucle et la boucle se termine.

4. Invariant de boucle : « le plus grand élément de la liste initiale est présent dans `s` ».
    - **Initialisation :** avant la boucle, `s` est la liste initiale.
    - **Conservation :** à chaque tour, on retire celui des deux premiers éléments qui est le plus petit (ou l'un des deux s'ils sont égaux). L'élément retiré n'est jamais strictement plus grand que celui qui reste : le plus grand élément reste dans `s`.
    - **Conclusion :** à la sortie, `s` ne contient plus qu'un élément, et l'invariant dit qu'il s'agit du plus grand élément de la liste initiale. La fonction le retourne : elle est correcte.

5. La boucle effectue $n - 1$ tours pour une liste de $n$ éléments. Mais `pop(0)` et `pop(1)` ne sont pas des opérations élémentaires : pour retirer un élément au début d'une liste, Python décale tous les éléments suivants, ce qui coûte un temps proportionnel à la longueur de la liste. La complexité est donc en $O(n^2)$.

6. Oui : on parcourt une seule fois la liste en gardant en mémoire le plus grand élément rencontré. C'est un algorithme en $O(n)$, qui ne modifie pas la liste. La fonction `max` de Python fait de même.

```python
def maximum(s: list[float]) -> float:
    """Retourne le plus grand élément de la liste non vide s."""
    plus_grand = s[0]
    for element in s:
        if element > plus_grand:
            plus_grand = element
    return plus_grand
```

{{< /solution >}}

{{< note exercise >}}

#### Exercice

On considère la fonction `somme_premiers_entiers` qui implémente l'algorithme&nbsp;:

##### Algorithme 5

**Fonction&nbsp;:**  *somme_premiers_entiers(n)*  
**Entrée&nbsp;:** *entier naturel $n$*  
**Sortie&nbsp;:** *somme des entiers de 1 à $n$*  
**Début**  
<span style="margin-left: 2em;">$\text{somme} \longleftarrow 0$</span><br />
<span style="margin-left: 2em;">$i \longleftarrow 1$</span><br />
<span style="margin-left: 2em;">**TantQue**  $i \leqslant n$ **Faire**</span><br />
<span style="margin-left: 4em;">$\text{somme} \longleftarrow \text{somme} + i$</span><br />
<span style="margin-left: 4em;">$i \longleftarrow i + 1$</span><br />
<span style="margin-left: 2em;">**FinTantQue**</span><br />
<span style="margin-left: 2em;">**Renvoyer**  somme</span><br />
**Fin**  

1. Implémenter en Python l'algorithme proposé. Ne pas oublier la spécification de la fonction.

2. Écrire un jeu de test pour cette fonction.

3. Prouver que la boucle se termine à l'aide du variant de boucle $f(n, i) = n - i$ où $i$ est le compteur de la boucle.

4. Prouver que la proposition&nbsp;: «&nbsp;au début du $k$-ième tour de la boucle, la variable somme est égale à la somme des entiers de 1 à $k-1$&nbsp;» est un invariant de boucle.  En déduire que l'algorithme est correct.

5. Quelle est la complexité de cet algorithme&nbsp;?
{{< /note >}}

{{< solution "Réponses" >}}
1.

```python
def somme_premiers_entiers(n: int) -> int:
    """
    Calcule la somme des entiers de 1 à n.

    HYPOTHÈSE : n entier naturel
    """
    somme = 0
    i = 1
    while i <= n:
        somme += i
        i += 1
    return somme
```

2.

```python
assert somme_premiers_entiers(0) == 0
assert somme_premiers_entiers(1) == 1
assert somme_premiers_entiers(12) == 12 * (12 + 1) // 2
```

3.

- Pour n'importe quel tour de boucle, on a $i \leqslant n$. Donc $f(n, i) = n - i \geqslant 0$&nbsp;;
- Au rang $k+1$, $i_{k+1} = i_k + 1$ donc $f(n, i_{k+1}) = n - i_{k+1} = n - i_k - 1 = f(n, i_k) - 1 < f(n, i_k)$. La fonction $f$ décroît strictement lorsque la boucle progresse.
- *condition d'arrêt&nbsp;:* $i>n$, donc $f(n,i) = n - i < 0$.

La fonction $f$ est positive, décroissante lorsque la boucle «&nbsp;tourne&nbsp;» et finalement prend une valeur négative lorsque la boucle est terminée&nbsp;; c'est *un variant de boucle*.  
*La présence d'un variant de boucle nous assure que la boucle se termine*.

4.

- **Initialisation&nbsp;:** Avant d'entrer dans la boucle, $\text{somme} = 0$.
- **Conservation&nbsp;:** On suppose que $\text{somme} = 0 + 1 + \ldots + k -1$ au début de la kième boucle.
Pendant la kième boucle, on a $\text{somme} = \text{somme} + k = 0 + 1 + \ldots + k -1 + k$.  
Au début de la $k+1$ième boucle, on a donc bien $\text{somme} = 0 + 1 + \ldots + k$.
- **Terminaison&nbsp;:** La boucle s'arrête dès que $i > n$. Donc au début du $n+1$ième tour (tour de boucle qui n'aura jamais lieu), on a bien $\text{somme} = 0 + 1 + \ldots + n$.

La proposition est bien un invariant de boucle, *elle nous assure que le programme est correct*.

5. La boucle effectue $n$ tours, chacun avec un nombre constant d'opérations : la complexité est linéaire, en $O(n)$. On pourrait faire mieux, en $O(1)$, avec la formule $\dfrac{n(n+1)}{2}$.

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- citer les principales classes de complexité, de $O(1)$ à $O(2^N)$, et donner un exemple d'algorithme pour chacune ;
- compter le nombre d'opérations effectuées par des boucles, simples ou imbriquées ;
- mesurer la durée d'un calcul avec `perf_counter` et relier son évolution à la complexité ;
- prouver qu'une boucle se termine à l'aide d'un variant de boucle ;
- prouver qu'un algorithme est correct à l'aide d'un invariant de boucle ;
- écrire un jeu de tests pour une fonction.
{{< /note >}}
