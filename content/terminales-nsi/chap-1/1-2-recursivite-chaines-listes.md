---
title: "La récursivité appliquée aux chaînes de caractères et aux listes"
subtitle: ""
author: ""
type: ""
date: 2020-09-08T04:53:31+04:00
draft: false
toc: true
tags: ["Chaînes de caractères", "Listes", "Récursivité"]
categories: ["Informatique", "Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: false
---

## Introduction

Une chaîne de caractère est une **structure de données** qui permet de rassembler en un *unique objet* une **succession ordonnée** de caractères. Ainsi, une *définition récursive d'une chaîne de caractères* pourrait être :

{{% note tip %}}

Une chaîne de caractères est :

- soit la chaîne de caractères vide ;
- soit constituée de son premier caractère et du reste des caractères qui forment aussi une chaîne de caractères (éventuellement vide).

{{% /note %}}

Une liste est une **structure de données** qui permet de rassembler en un *unique objet* une **succession ordonnée** d'objets (ou de valeurs). Ainsi, une *définition récursive d'une liste* pourrait être :

{{% note tip %}}

Une liste est :

- soit la liste vide ;
- soit constituée de son premier élément et du reste des éléments qui forment aussi une liste (éventuellement vide).

{{% /note %}}

## Exercices

Penser à écrire, pour chacune des fonctions ci-dessous, sa spécification ainsi qu'un jeu de tests.

{{% note exercise %}}

#### Recherche dans une chaîne de caractères

Écrire une fonction récursive nommée `est_dans`, qui, à partir d'un caractère `e` et d'une chaîne de caractères `c`, détermine si ce caractère appartient à la chaîne.

Tester cette fonction.

**Remarque :** la fonction `est_dans` est un **prédicat**.
{{% /note %}}

{{% solution "Solution" %}}

```python
def est_dans(e: str, c: str) -> bool:
    """
    Détermine si le caractère e est dans la chaîne c.
    Version utilisant une sous-chaîne.
    Récursivité terminale.
    """
    if c == "":
        return False
    elif c[0] == e:
        return True
    return est_dans(e, c[1:])


def est_dans_02(e: str, c: str, i: int) -> bool:
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


def main():
    """ Fonction principale. """
    chaine = input("Entrer la chaîne : ")
    car = input("Entrer le caractère à recherche : ")

    print("{} est-il dans {} : {}".format(car, chaine, est_dans(car, chaine)))
    print("{} est-il dans {} : {}".format(car, chaine, est_dans_02(car,
          chaine, 0)))

main()
```

{{% /solution %}}

{{% note exercise %}}

#### Recherche de la position d'un caractère dans une chaîne de caractères

Écrire une fonction récursive nommée `rang`, qui, à partir d'un caractère `e` et d'une chaîne de caractères `c`, détermine la (première) position de ce caractère dans la chaîne. Si le caractère n'est pas présent, retourner un nombre négatif.

Tester cette fonction dans un programme.
{{% /note %}}

{{% solution "Solution" %}}

```python
def rang(e: str, c: str, i: int) -> int:
    """
    Retourne l'indice de la première position du caractère e dans la
    chaîne c ou -1 si le caractère n'est pas présent dans la chaîne.

    Remarque : l'indice n'est pas réellement le rang. Faire débuter i
    à 0 pour obtenir l'indice, à 1 pour obtenir le rang.

    Remarque : récursivité terminale
    """
    if c == "":
        return -1
    elif c[0] == e:
        return i
    else:
        return rang(e, c[1:], i + 1)

def rang_2(c: str, e: str) -> int:
    """
    Retourne le rang de la première position du caractère e dans la
    chaîne c ou un nombre négatif si le caractère n'est pas présent
    dans la chaîne.

    Récursivité enveloppée.
    """
    if c == "":
        return -float('inf')
    elif c[0] == e:
        return 1
    else:
        return 1 + rang(c[1:], e)


def main():
    """ Fonction principale. """
    chaine = input("Chaîne ? ")
    car = input("Caractère ? ")

    indice = rang(car, chaine, 0)
    if indice >= 0:
        print("Position du carcatères :", indice)
    else:
        print("Caractère pas présent dans la chaîne.")

main()
```

{{% /solution %}}

{{% note exercise %}}

#### Copie d'une chaîne de caractères

Écrire une fonction récursive nommée `copie`, qui, à partir d'une chaîne de caractères `c`, retourne une nouvelle chaîne copie de `c`.

Tester cette fonction.

{{% /note %}}

{{% solution "Solution" %}}

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

    assert copie('abcd') == 'abcd'
    assert copie('a') == 'a'
    assert copie('') == ''
```

{{% /solution %}}

{{% note exercise %}}

#### Inversion d'une chaîne de caractères

Écrire une fonction récursive nommée `inversion`, qui, à partir d'une chaîne de caractères `c`, retourne la chaîne « mirroir », c'est à dire la chaîne égale à celle passée en argument quand on la lit de droite à gauche.

Tester cette fonction dans un programme.
{{% /note %}}

{{% solution "Solution" %}}

```python
def inversion(c: str) -> str:
    """
    Inverse une chaîne de caractères.
    Version avec sous-chaîne et récursivité enveloppée.
    """
    if c == "":
        return ''
    else:
        return inversion(c[1:]) + c[0]


def inversion_02(c: str, c_inv: str) -> str:
    """
    Inverse une chaîne de caractères.
    Version avec sous-chaîne et récursivité terminale.
    """
    if c == "":
        return c_inv
    else:
        return inversion_02(c[1:], c[0] + c_inv)


def inversion_03(c: str, i: int) -> str:
    """
    Inverse une chaîne de caractères.
    Version sans sous-chaîne et récursivité enveloppée.
    """
    if i == len(c):
        return ''
    else:
        return inversion_03(c, i + 1) + c[i]


def inversion_04(c: str, c_inv: str, i: int) -> str:
    """
    Inverse une chaîne de caractères.
    Version sans sous-chaîne et récursivité terminale.
    """
    if i == len(c):
        return c_inv
    else:
        return inversion_04(c, c[i] + c_inv, i + 1)


def main():
    """ Fonction principale. """
    chaine = input("Chaîne ? ")
    chaine_inversee_01 = inversion(chaine)
    print(chaine_inversee_01)
    chaine_inversee_02 = inversion_02(chaine, '')
    print(chaine_inversee_02)
    chaine_inversee_03 = inversion_03(chaine, 0)
    print(chaine_inversee_03)
    chaine_inversee_04 = inversion_04(chaine, '', 0)
    print(chaine_inversee_04)

main()
```

{{% /solution %}}

{{% note exercise %}}

#### Détecteur de palindrome

Un palindrome est un mot (ou une phrase) qui se lit aussi bien de la gauche vers la droite que de la droite vers la gauche : par exemple « radar », « kayak », ou bien la phrase « esope reste et se repose » (si l'on ne tient pas compte des espaces).

Écrire une fonction récursive nommée `est_palindrome` qui reçoit comme argument une chaîne de caractères contenant le mot (ou la phrase). Cette fonction doit tester si les deux caractères opposés sont identiques, puis appeler récursivement la fonction sur la partie de la chaîne qui ne contient pas ces deux caractères (les espaces sont ignorés).
{{% /note %}}

{{% solution "Solution" %}}

```python
def est_palindrome(c: str) -> bool:
    """
    Détecte si la chaîne de caractères est un palindrome.
    Utilisation d'une sous-chaïne. La récursivité est terminale.

    Hypothèse : la chaîne c n'est pas vide.
    """
    if c == "":
        return True
    elif c[0] != c[-1]:
        return False
    else:
        return est_palindrome(c[1: -1])


def est_palindrome_02(c: str, i: int, j: int) -> bool:
    """
    Détecte si la chaîne de caractères est un palindrome.
    i est le premier indice de la chaîne, j le dernier.
    Utilisation d'une sous-chaîne. La récursivité est terminale.

    Hypothèse : la chaîne c n'est pas vide.
    """
    if i == j:
        return True
    elif c[i] != c[j]:
        return False
    else:
        return est_palindrome_02(c, i+1, j-1)


def main():
    """ Fonction principale. """
    chaine = input("Chaîne à tester : ")
    print("Est un palindrome 01 ? {}".format(est_palindrome(chaine)))

    print("Est un palindrome 02 ?",
          est_palindrome_02(chaine, 0, len(chaine)-1))


main()
```

{{% /solution %}}

{{% note exercise %}}

#### Travail sur les listes

1. Écrire une fonction nommée `longueur_liste`, récursive, qui, à partir d'une liste passée en argument, détermine sa longueur.

2. Écrire une fonction nommée `produit_elements`, récursive, qui, à partir d'une liste d'entiers passée en argument, calcule le produit de tous les nombres.

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

6. Écrire une fonction nommée `duplique`, récursive, qui, à partir d'un élément `e` et d'un entier `n`, retourne une liste qui contient l'élément `e` un nombre de fois égal à `n`.

```python
assert duplique(5, 3) == [5, 5, 5]
```

7. Écrire une fonction nommée `extrait`, récursive, qui, à partir d'une liste `l` et d'un entier `n`, retourne une liste constituée par les `n` premiers éléments de `l`.

```python
assert extrait([5, 4, 3, 2, 1], 3) == [5, 4, 3]
```

8. Écrire une fonction nommée `renverse`, récursive, qui, à partir d'une liste, retourne une liste dans laquelle les éléments sont renversés (les derniers apparaissent en premier).

9. Écrire une fonction nommée `creation_liste_filtree`, qui, à partir de deux entiers `i` et `j` passés en argument retourne une liste d'entiers compris entre `i` et `j` multiples de 3 ou de 5.

```python
assert creation_liste_filtree(1, 10) == [3, 5, 6, 9, 10]
```

10. Modifier la fonction précédente afin que le filtre « entiers multiples de 3 ou de 5 » soit passé en argument.

{{% /note %}}

{{% solution "Solutions" %}}

```python
def plus_grand_element(liste: list) -> float:
    """
    Retourne le plus grand éléments de la liste.
    """
    if liste == []:
        raise Exception("La liste est vide.")
    elif len(liste) == 1:
        return liste[0]
    else:
        val_max = plus_grand_element(liste[1:])
        return (liste[0] if liste[0] > val_max else val_max)


def plus_petit_element(liste: list) -> float:
    """
    Retourne le plus petit élément de la liste.
    """
    if liste == []:
        raise Exception("La liste est vide")
    elif len(liste) == 1:
        return liste[0]
    else:
        val_min = plus_petit_element(liste[1:])
        return (liste[0] if liste[0] < val_min else val_min)


def longueur_liste(l: List) -> int:
    """
    Retourne le nombre d'éléments dans une liste.
    Récursivité enveloppée.
    """
    if l == []:
        return 0
    else:
        return 1 + longueur_liste(l[1:])


def longueur_liste_02(liste: list, l: int = 0) -> int:
    """
    Retourne le nombre d'éléments dans une liste.
    Récursivité terminale.
    """
    if liste == []:
        return l
    else:
        return longueur_liste_02(liste[1:], l + 1)


def somme_elements(l: List[float]) -> float:
    """
    Retourne la somme des éléments de la liste.
    Récursivité enveloppée.
    """
    if l == []:
        return 0
    else:
        return l[0] + somme_elements(l[1:])


def somme_elements_2(l: List[float], s: int = 0) -> float:
    """
    Retourne la somme des éléments de la liste.
    Récursivité terminale.
    """
    if l == []:
        return s
    else:
        return somme_elements_2(l[1:], s + l[0])


def somme_listes_imbriquees(liste: list, s: float = 0) -> float:
    """
    Retourne la somme des éléments de listes imbriquées.
    """
    if len(liste) == 0:
        return s
    else:
        if not isinstance(liste[0], list):
            return somme_listes_imbriquees(liste[1:], s + liste[0])
        else:
            somme_avec_sous_listes = somme_listes_imbriquees(liste[0], s)
            return somme_listes_imbriquees(liste[1:], somme_avec_sous_listes)


def somme_listes_imbriquees(l: List) -> float:
    """
    Retourne la somme de tous les éléments d'une liste,
    même si elle contient des sous-listes imbriquées.
    """
    if l == []:
        return 0
    elif isinstance(l[0], list):
        return somme_listes_imbriquees(l[0]) + somme_listes_imbriquees(l[1:])
    else:
        return l[0] + somme_listes_imbriquees(l[1:])


def produit_elements(l: List[float]) -> float:
    """
    Retourne le produit de tous les éléments de la liste.
    Récursivité enveloppée.
    """
    if l == []:
        raise Exception("La liste est vide.")
    elif len(l) == 1:
        return l[0]
    else:
        return l[0] * produit_elements(l[1:])


def produit_elements_2(l: List[float], p: float = 1) -> float:
    """
    Retourne le produit de tous les éléments de la liste.
    Récursivité terminale.
    """
    if l == []:
        raise Exception("La liste est vide.")
    elif len(l) == 1:
        return l[0] * p
    else:
        return produit_elements_2(l[1:], l[0] * p)


def recherche_element(liste: list, val_rech: int, i: int) -> int:
    """ Ne se contente pas de déterminer si la valeur cherchée est
    présente, retourne son indice (on ne cherche que la première
    valeur) si possible (sinon -1). """

    if i == len(liste):
        return -1
    elif liste[i] == val_rech:
        return i
    else:
        return recherche_element(liste, val_rech, i+1)


def main():
    l = [-128, -23, 123, 213, 9, 2891]
    nbre_max = plus_grand_element(l)
    nbre_min = plus_petit_element(l)
    longueur = longueur_liste(l)
    somme = somme_elements(l)
    produit = produit_elements(l)
    l2 = [[1, [1, [1, [1]], 1]], 1]
    somme2 = somme_listes_imbriquees(l2, 0)
    print("Recherche élément")
    print(recherche_element(l, 12, 0))
    print("Recherche nombre max")
    print(nbre_max)
    print(nbre_min)
    print(longueur)
    print(somme)
    print(produit)
    print(somme2)

main()
```

{{% /solution %}}
