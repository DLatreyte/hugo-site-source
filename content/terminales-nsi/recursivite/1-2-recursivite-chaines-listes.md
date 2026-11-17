---
title: "La récursivité appliquée aux chaînes de caractères et aux listes"
subtitle: ""
date: 2020-09-08T04:53:31+04:00
draft: false
toc: true
tags: ["Chaînes de caractères", "Listes", "Récursivité"]
categories: ["Informatique", "Terminales Spé NSI"]
solution_est_visible: true
auto_numbering: false
weight: 102
---

{{< note goal >}}
Appliquer la récursivité aux chaînes de caractères et aux listes, en s'appuyant sur leur définition récursive&nbsp;: un premier élément, suivi d'un reste qui est lui-même une chaîne (ou une liste).
{{< /note >}}

Avant de commencer, prévoir ce qu'affichent les instructions suivantes, puis vérifier dans la console.

```python
c = "radar"
print(c[0], c[1:], c[1:-1])
print("a"[1:] == "")
```

{{< solution "Réponse" >}}
La première ligne affiche `r adar ada`&nbsp;: `c[0]` est le premier caractère, `c[1:]` la chaîne privée de son premier caractère et `c[1:-1]` la chaîne privée de ses deux extrémités. La deuxième ligne affiche `True`&nbsp;: une chaîne d'un seul caractère, privée de ce caractère, devient la chaîne vide. Toutes les fonctions de ce document reposent sur ces découpages&nbsp;: chaque appel récursif travaille sur une chaîne plus courte, jusqu'à la chaîne vide.
{{< /solution >}}

## Introduction

Une chaîne de caractères est une **structure de données** qui permet de rassembler en un *unique objet* une **succession ordonnée** de caractères. Ainsi, une *définition récursive d'une chaîne de caractères* pourrait être :

{{< note tip >}}

#### Définition récursive d'une chaîne de caractères

Une chaîne de caractères est :

- soit la chaîne de caractères vide ;
- soit constituée de son premier caractère et du reste des caractères qui forment aussi une chaîne de caractères (éventuellement vide).

{{< /note >}}

Une liste est une **structure de données** qui permet de rassembler en un *unique objet* une **succession ordonnée** d'objets (ou de valeurs). Ainsi, une *définition récursive d'une liste* pourrait être :

{{< note tip >}}

#### Définition récursive d'une liste

Une liste est :

- soit la liste vide ;
- soit constituée de son premier élément et du reste des éléments qui forment aussi une liste (éventuellement vide).

{{< /note >}}

## Exercices

Penser à écrire, pour chacune des fonctions ci-dessous, sa spécification ainsi qu'un jeu de tests.

{{< note exercise >}}

#### Recherche dans une chaîne de caractères

Écrire une fonction récursive nommée `est_dans`, qui, à partir d'un caractère `e` et d'une chaîne de caractères `c`, détermine si ce caractère appartient à la chaîne.

Tester cette fonction.

**Remarque :** la fonction `est_dans` est un **prédicat**.
{{< /note >}}

{{< solution "Solution" >}}

```python
def est_dans(e: str, c: str) -> bool:
    """
    Détermine si le caractère e est dans la chaîne c.
    Version utilisant une sous-chaîne.
    Récursivité terminale.

    >>> est_dans("d", "radar")
    True
    >>> est_dans("z", "radar")
    False
    """
    if c == "":
        return False
    elif c[0] == e:
        return True
    else:
        return est_dans(e, c[1:])


def est_dans_02(e: str, c: str, i: int = 0) -> bool:
    """
    Détermine si le caractère e est dans la chaîne c.
    Version utilisant un indice et toujours la même chaîne.
    Il s'agit toujours d'une récursivité terminale.
    """
    if i == len(c):
        return False
    elif e == c[i]:
        return True
    else:
        return est_dans_02(e, c, i + 1)


def main() -> None:
    """Fonction principale."""
    chaine = input("Entrer la chaîne : ")
    car = input("Entrer le caractère à rechercher : ")

    print(f"{car} est-il dans {chaine} : {est_dans(car, chaine)}")
    print(f"{car} est-il dans {chaine} : {est_dans_02(car, chaine)}")


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Recherche de la position d'un caractère dans une chaîne de caractères

Écrire une fonction récursive nommée `rang`, qui, à partir d'un caractère `e` et d'une chaîne de caractères `c`, détermine la (première) position de ce caractère dans la chaîne. Si le caractère n'est pas présent, retourner un nombre négatif.

Tester cette fonction dans un programme.
{{< /note >}}

{{< solution "Solution" >}}

```python
def rang(e: str, c: str, i: int = 0) -> int:
    """
    Retourne l'indice de la première position du caractère e dans la
    chaîne c ou -1 si le caractère n'est pas présent dans la chaîne.

    Remarque : l'indice n'est pas réellement le rang. Faire débuter i
    à 0 pour obtenir l'indice, à 1 pour obtenir le rang.

    Remarque : récursivité terminale

    >>> rang("d", "radar")
    2
    >>> rang("z", "radar")
    -1
    """
    if c == "":
        return -1
    elif c[0] == e:
        return i
    else:
        return rang(e, c[1:], i + 1)


def rang_2(e: str, c: str) -> int:
    """
    Retourne le rang (à partir de 1) de la première position du
    caractère e dans la chaîne c, ou -1 si le caractère n'est pas
    présent dans la chaîne.

    Récursivité enveloppée.

    >>> rang_2("d", "radar")
    3
    >>> rang_2("z", "radar")
    -1
    """
    if c == "":
        return -1
    elif c[0] == e:
        return 1
    else:
        rang_reste = rang_2(e, c[1:])
        if rang_reste == -1:  # e n'est pas dans le reste de la chaîne
            return -1
        else:
            return 1 + rang_reste


def main() -> None:
    """Fonction principale."""
    chaine = input("Chaîne ? ")
    car = input("Caractère ? ")

    indice = rang(car, chaine)
    if indice >= 0:
        print("Position du caractère :", indice)
    else:
        print("Caractère pas présent dans la chaîne.")


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Copie d'une chaîne de caractères

Écrire une fonction récursive nommée `copie`, qui, à partir d'une chaîne de caractères `c`, retourne une nouvelle chaîne copie de `c`.

Tester cette fonction.

{{< /note >}}

{{< solution "Solution" >}}

```python
def copie(c: str) -> str:
    """
    Retourne une copie de la chaîne c.

    Algorithme récursif.
    """
    if c == "":
        return ""
    else:
        return c[0] + copie(c[1:])


assert copie("abcd") == "abcd"
assert copie("a") == "a"
assert copie("") == ""
```

{{< /solution >}}

{{< note exercise >}}

#### Inversion d'une chaîne de caractères

Écrire une fonction récursive nommée `inversion`, qui, à partir d'une chaîne de caractères `c`, retourne la chaîne « miroir », c'est-à-dire la chaîne égale à celle passée en argument quand on la lit de droite à gauche.

Tester cette fonction dans un programme.
{{< /note >}}

{{< solution "Solution" >}}

```python
def inversion(c: str) -> str:
    """
    Inverse une chaîne de caractères.
    Version avec sous-chaîne et récursivité enveloppée.
    """
    if c == "":
        return ""
    else:
        return inversion(c[1:]) + c[0]


def inversion_02(c: str, c_inv: str = "") -> str:
    """
    Inverse une chaîne de caractères.
    Version avec sous-chaîne et récursivité terminale.
    """
    if c == "":
        return c_inv
    else:
        return inversion_02(c[1:], c[0] + c_inv)


def inversion_03(c: str, i: int = 0) -> str:
    """
    Inverse une chaîne de caractères.
    Version sans sous-chaîne et récursivité enveloppée.
    """
    if i == len(c):
        return ""
    else:
        return inversion_03(c, i + 1) + c[i]


def inversion_04(c: str, c_inv: str = "", i: int = 0) -> str:
    """
    Inverse une chaîne de caractères.
    Version sans sous-chaîne et récursivité terminale.
    """
    if i == len(c):
        return c_inv
    else:
        return inversion_04(c, c[i] + c_inv, i + 1)


def main() -> None:
    """Fonction principale."""
    chaine = input("Chaîne ? ")
    print(inversion(chaine))
    print(inversion_02(chaine))
    print(inversion_03(chaine))
    print(inversion_04(chaine))


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Détecteur de palindrome

Un palindrome est un mot (ou une phrase) qui se lit aussi bien de la gauche vers la droite que de la droite vers la gauche : par exemple « radar », « kayak », ou bien la phrase « esope reste et se repose » (si l'on ne tient pas compte des espaces).

Écrire une fonction récursive nommée `est_palindrome` qui reçoit comme argument une chaîne de caractères contenant le mot (ou la phrase). Cette fonction doit tester si les deux caractères opposés sont identiques, puis appeler récursivement la fonction sur la partie de la chaîne qui ne contient pas ces deux caractères (les espaces sont ignorés).
{{< /note >}}

{{< note tip "Coup de pouce" >}}
Commencer par les chaînes sans espace. Quelles chaînes sont des palindromes sans qu'il soit besoin de rien comparer&nbsp;? Ce sont les cas de base. Pour ignorer les espaces, il suffit ensuite de traiter deux cas supplémentaires&nbsp;: le premier caractère est une espace, ou le dernier caractère est une espace. Sur quelle chaîne faut-il alors faire l'appel récursif&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

```python
def est_palindrome(c: str) -> bool:
    """
    Détecte si la chaîne de caractères est un palindrome, sans tenir
    compte des espaces.
    Utilisation d'une sous-chaîne. La récursivité est terminale.

    >>> est_palindrome("kayak")
    True
    >>> est_palindrome("esope reste et se repose")
    True
    >>> est_palindrome("radis")
    False
    """
    if len(c) <= 1:  # chaîne vide ou d'un seul caractère
        return True
    elif c[0] == " ":
        return est_palindrome(c[1:])
    elif c[-1] == " ":
        return est_palindrome(c[:-1])
    elif c[0] != c[-1]:
        return False
    else:
        return est_palindrome(c[1:-1])


def est_palindrome_02(c: str, i: int, j: int) -> bool:
    """
    Détecte si la chaîne de caractères est un palindrome, sans tenir
    compte des espaces.
    i est le premier indice de la partie à tester, j le dernier.
    Utilisation des indices, sans sous-chaîne. La récursivité est terminale.

    >>> est_palindrome_02("abba", 0, 3)
    True
    >>> est_palindrome_02("esope reste et se repose", 0, 23)
    True
    """
    if i >= j:  # zéro ou un caractère restant
        return True
    elif c[i] == " ":
        return est_palindrome_02(c, i + 1, j)
    elif c[j] == " ":
        return est_palindrome_02(c, i, j - 1)
    elif c[i] != c[j]:
        return False
    else:
        return est_palindrome_02(c, i + 1, j - 1)


def main() -> None:
    """Fonction principale."""
    chaine = input("Chaîne à tester : ")
    print(f"Est un palindrome 01 ? {est_palindrome(chaine)}")
    print(f"Est un palindrome 02 ? {est_palindrome_02(chaine, 0, len(chaine) - 1)}")


if __name__ == "__main__":
    main()
```

{{< /solution >}}

{{< note exercise >}}

#### Travail sur les listes

1. Écrire une fonction nommée `longueur_liste`, récursive, qui, à partir d'une liste passée en argument, détermine sa longueur.

2. Écrire une fonction nommée `somme_elements`, récursive, qui, à partir d'une liste de nombres passée en argument, calcule la somme de tous les nombres. Écrire de même une fonction nommée `produit_elements`, récursive, qui, à partir d'une liste non vide de nombres passée en argument, calcule le produit de tous les nombres.

3. Écrire une fonction nommée `plus_grand_element`, récursive, qui, à partir d'une liste d'entiers passée en argument, détermine quel est l'entier le plus grand.

4. Écrire une fonction nommée `plus_petit_element`, récursive, qui, à partir d'une liste d'entiers passée en argument, détermine quel est l'entier le plus petit.

5. Écrire une fonction nommée `somme_listes_imbriquees`, récursive, qui additionne tous les entiers des listes.  
Exemple de listes imbriquées :

```python
l1 = [1, [2, [3, 4], 5], 6, [7, 8]]
l2 = [1, [2, [3, [4, [5]]]]]
```

Remarque.
: Cette question peut illustrer, par exemple, la recherche de l'occupation disque de tous les fichiers dans la structure arborescente d'un système de fichiers à partir d'un point de cette structure.

{{< note tip "Coup de pouce" >}}
Le premier élément d'une liste imbriquée est soit un entier, soit lui-même une liste. L'expression `isinstance(x, list)` vaut `True` si `x` est une liste. Dans le second cas, il faut deux appels récursifs&nbsp;: lesquels&nbsp;?
{{< /note >}}

6. Écrire une fonction nommée `duplique`, récursive, qui, à partir d'un élément `e` et d'un entier `n`, retourne une liste qui contient l'élément `e` un nombre de fois égal à `n`.

```python
assert duplique(5, 3) == [5, 5, 5]
```

7. Écrire une fonction nommée `extrait`, récursive, qui, à partir d'une liste `l` et d'un entier `n`, retourne une liste constituée par les `n` premiers éléments de `l`.

```python
assert extrait([5, 4, 3, 2, 1], 3) == [5, 4, 3]
```

8. Écrire une fonction nommée `renverse`, récursive, qui, à partir d'une liste, retourne une liste dans laquelle les éléments sont renversés (les derniers apparaissent en premier).

9. Écrire une fonction nommée `creation_liste_filtree`, récursive, qui, à partir de deux entiers `i` et `j` passés en argument, retourne la liste des entiers compris entre `i` et `j` (inclus) qui sont multiples de 3 ou de 5.

```python
assert creation_liste_filtree(1, 10) == [3, 5, 6, 9, 10]
```

10. Modifier la fonction précédente afin que le filtre « entiers multiples de 3 ou de 5 » soit passé en argument, sous la forme d'une fonction qui reçoit un entier et retourne un booléen (un prédicat).

{{< /note >}}

{{< solution "Solutions" >}}

```python
from collections.abc import Callable
from typing import TypeAlias

# Une liste imbriquée contient des entiers et des listes imbriquées.
ListeImbriquee: TypeAlias = list["int | ListeImbriquee"]


def longueur_liste(liste: list) -> int:
    """
    Retourne le nombre d'éléments dans une liste.
    Récursivité enveloppée.
    """
    if liste == []:
        return 0
    else:
        return 1 + longueur_liste(liste[1:])


def longueur_liste_02(liste: list, acc: int = 0) -> int:
    """
    Retourne le nombre d'éléments dans une liste.
    Récursivité terminale : acc contient le nombre d'éléments déjà comptés.
    """
    if liste == []:
        return acc
    else:
        return longueur_liste_02(liste[1:], acc + 1)


def somme_elements(liste: list[float]) -> float:
    """
    Retourne la somme des éléments de la liste.
    Récursivité enveloppée.
    """
    if liste == []:
        return 0
    else:
        return liste[0] + somme_elements(liste[1:])


def somme_elements_02(liste: list[float], acc: float = 0) -> float:
    """
    Retourne la somme des éléments de la liste.
    Récursivité terminale.
    """
    if liste == []:
        return acc
    else:
        return somme_elements_02(liste[1:], acc + liste[0])


def produit_elements(liste: list[float]) -> float:
    """
    Retourne le produit de tous les éléments de la liste (non vide).
    Récursivité enveloppée.
    """
    if liste == []:
        raise ValueError("La liste est vide.")
    elif len(liste) == 1:
        return liste[0]
    else:
        return liste[0] * produit_elements(liste[1:])


def produit_elements_02(liste: list[float], acc: float = 1) -> float:
    """
    Retourne le produit de tous les éléments de la liste (non vide).
    Récursivité terminale.
    """
    if liste == []:
        raise ValueError("La liste est vide.")
    elif len(liste) == 1:
        return liste[0] * acc
    else:
        return produit_elements_02(liste[1:], liste[0] * acc)


def plus_grand_element(liste: list[float]) -> float:
    """
    Retourne le plus grand élément de la liste (non vide).
    """
    if liste == []:
        raise ValueError("La liste est vide.")
    elif len(liste) == 1:
        return liste[0]
    else:
        val_max = plus_grand_element(liste[1:])
        return liste[0] if liste[0] > val_max else val_max


def plus_petit_element(liste: list[float]) -> float:
    """
    Retourne le plus petit élément de la liste (non vide).
    """
    if liste == []:
        raise ValueError("La liste est vide.")
    elif len(liste) == 1:
        return liste[0]
    else:
        val_min = plus_petit_element(liste[1:])
        return liste[0] if liste[0] < val_min else val_min


def somme_listes_imbriquees(liste: ListeImbriquee) -> int:
    """
    Retourne la somme de tous les éléments d'une liste,
    même si elle contient des sous-listes imbriquées.

    >>> somme_listes_imbriquees([1, [2, [3, 4], 5], 6, [7, 8]])
    36
    >>> somme_listes_imbriquees([1, [2, [3, [4, [5]]]]])
    15
    """
    if liste == []:
        return 0
    elif isinstance(liste[0], list):
        return somme_listes_imbriquees(liste[0]) + somme_listes_imbriquees(liste[1:])
    else:
        return liste[0] + somme_listes_imbriquees(liste[1:])


def somme_listes_imbriquees_02(liste: ListeImbriquee, acc: int = 0) -> int:
    """
    Retourne la somme des éléments de listes imbriquées.
    Version avec accumulateur.
    """
    if liste == []:
        return acc
    elif isinstance(liste[0], list):
        somme_avec_sous_liste = somme_listes_imbriquees_02(liste[0], acc)
        return somme_listes_imbriquees_02(liste[1:], somme_avec_sous_liste)
    else:
        return somme_listes_imbriquees_02(liste[1:], acc + liste[0])


def duplique(e: object, n: int) -> list:
    """
    Retourne une liste qui contient n fois l'élément e.

    >>> duplique(5, 3)
    [5, 5, 5]
    """
    if n == 0:
        return []
    else:
        return [e] + duplique(e, n - 1)


def extrait(liste: list, n: int) -> list:
    """
    Retourne la liste des n premiers éléments de liste
    (toute la liste si elle contient moins de n éléments).

    >>> extrait([5, 4, 3, 2, 1], 3)
    [5, 4, 3]
    """
    if n == 0 or liste == []:
        return []
    else:
        return [liste[0]] + extrait(liste[1:], n - 1)


def renverse(liste: list) -> list:
    """
    Retourne une nouvelle liste contenant les éléments de liste
    dans l'ordre inverse.

    >>> renverse([1, 2, 3])
    [3, 2, 1]
    """
    if liste == []:
        return []
    else:
        return renverse(liste[1:]) + [liste[0]]


def creation_liste_filtree(i: int, j: int) -> list[int]:
    """
    Retourne la liste des entiers compris entre i et j (inclus)
    qui sont multiples de 3 ou de 5.

    >>> creation_liste_filtree(1, 10)
    [3, 5, 6, 9, 10]
    """
    if i > j:
        return []
    elif i % 3 == 0 or i % 5 == 0:
        return [i] + creation_liste_filtree(i + 1, j)
    else:
        return creation_liste_filtree(i + 1, j)


def creation_liste_filtree_02(i: int, j: int, filtre: Callable[[int], bool]) -> list[int]:
    """
    Retourne la liste des entiers compris entre i et j (inclus)
    pour lesquels le prédicat filtre retourne True.

    >>> creation_liste_filtree_02(1, 10, lambda k: k % 3 == 0 or k % 5 == 0)
    [3, 5, 6, 9, 10]
    """
    if i > j:
        return []
    elif filtre(i):
        return [i] + creation_liste_filtree_02(i + 1, j, filtre)
    else:
        return creation_liste_filtree_02(i + 1, j, filtre)


def recherche_element(liste: list[int], val_rech: int, i: int = 0) -> int:
    """
    Ne se contente pas de déterminer si la valeur cherchée est
    présente, retourne son indice (on ne cherche que la première
    valeur) si possible (sinon -1).
    """
    if i == len(liste):
        return -1
    elif liste[i] == val_rech:
        return i
    else:
        return recherche_element(liste, val_rech, i + 1)


def main() -> None:
    """Fonction principale."""
    nombres: list[float] = [-128, -23, 123, 213, 9, 2891]
    print("Plus grand élément :", plus_grand_element(nombres))
    print("Plus petit élément :", plus_petit_element(nombres))
    print("Longueur :", longueur_liste(nombres))
    print("Somme :", somme_elements(nombres))
    print("Produit :", produit_elements(nombres))
    print("Indice de 12 :", recherche_element([3, 12, 5], 12))
    imbriquee: ListeImbriquee = [[1, [1, [1, [1]], 1]], 1]
    print("Somme de la liste imbriquée :", somme_listes_imbriquees(imbriquee))


if __name__ == "__main__":
    main()
```

La fonction `creation_liste_filtree_02` reçoit une fonction en argument. Pour lui transmettre le filtre, on peut définir une fonction avec `def`, ou écrire une fonction anonyme avec `lambda`, comme dans l'exemple de la documentation. Le type d'un tel argument s'écrit `Callable[[int], bool]`&nbsp;: une fonction qui reçoit un entier et retourne un booléen.

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- donner la définition récursive d'une chaîne de caractères et d'une liste ;
- découper une chaîne ou une liste en son premier élément et son reste (`c[0]`, `c[1:]`) ;
- écrire une fonction récursive sur une chaîne ou une liste, avec la chaîne vide ou la liste vide comme cas de base ;
- écrire deux versions d'une même fonction, l'une avec sous-chaînes, l'autre avec un indice passé en paramètre ;
- distinguer une récursivité enveloppée d'une récursivité terminale, qui utilise un accumulateur ;
- parcourir une liste imbriquée par une double récursion ;
- passer une fonction en argument d'une autre fonction.
{{< /note >}}
