---
title: "La récursivité appliquée aux chaînes de caractères et aux listes"
subtitle: "Chapitre 1,2"
author: ""
type: ""
date: 2020-09-08T04:53:31+04:00
draft: false
toc: true
tags: ["Chaînes de caractères", "Listes", "Récursivité"]
categories: ["Informatique", "Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

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
    if len(c) == 0:
        return False
    elif e == c[0]:
        return True
    else:
        return est_dans(e, c[1:])


def est_dans_02(e: str, c: str, i: int) -> bool:
    """
    Détermine si le caractère e est dans la chaîne c.
    Version utilisant un indice et toujours la même chaîne.
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

Écrire une fonction récursive nommée `rang`, qui, à partir d'un caractère `e` et d'une chaîne de caractères `c`, détermine la (première) position de ce caractère dans la chaîne. Si le caractère n'est pas présent, retourner un entier négatif.

Tester cette fonction dans un programme.
{{% /note %}}

{{% solution "Solution" %}}
```python
def rang(e: str, c: str, i: int) -> int:
    """
    Retourne l'indice de la première position du caractère e dans la
    chaîne c ou -1 si le caractère n'est pas présent dans la chaîne.
    """
    if i == len(c):
        return -1
    elif e == c[i]:
        return i
    else:
        return rang(e, c, i + 1)


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
    if len(c) == 0:
        return ''
    else:
        return inversion(c[1:]) + c[0]


def inversion_02(c: str, c_inv: str) -> str:
    """
    Inverse une chaîne de caractères.
    Version avec sous-chaîne et récursivité terminale.
    """
    if len(c) == 0:
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
    """
    if len(c) == 0:
        return True
    elif c[0] != c[-1]:
        return False
    else:
        return est_palindrome(c[1:-1])


def est_palindrome_02(c: str, i: int, j: int) -> bool:
    """
    Détecte si la chaîne de caractères est un palindrome.
    Utilisation d'une sous-chaïne. La récursivité est terminale.
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

    longueur = len(liste)

    if longueur == 0:
        raise IndexError("La liste est vide.")
    elif longueur == 1:
        return liste[0]
    else:
        val_max = plus_grand_element(liste[1:])
        return (liste[0] if liste[0] > val_max else val_max)


def plus_petit_element(liste: list) -> float:

    longueur = len(liste)

    if longueur == 0:
        raise IndexError("La liste est vide")
    elif longueur == 1:
        return liste[0]
    else:
        val_min = plus_petit_element(liste[1:])
        return (liste[0] if liste[0] < val_min else val_min)


def longueur_liste(liste: list) -> int:
    """ Récursivité enveloppée. """
    if len(liste) == 0:
        return 0
    else:
        return 1 + longueur_liste(liste[1:])


def longueur_liste_02(liste: list, l: int) -> int:
    """ Récursivité terminale. """
    if len(liste) == 0:
        return l
    else:
        return longueur_liste_02(liste[1:], l + 1)


def somme_elements(liste: list) -> float:
    """ Récursivité enveloppée. """
    if len(liste) == 0:
        return 0
    else:
        return liste[0] + somme_elements(liste[1:])


def somme_elements_02(liste: list, s: float) -> float:
    """ Récursivité terminale. """
    if len(liste) == 0:
        return s
    else:
        return somme_elements_02(liste[1:], s + liste[0])


def somme_listes_imbriquees(liste: list, s: float) -> float:

    if len(liste) == 0:
        return s
    else:
        if not isinstance(liste[0], list):
            return somme_listes_imbriquees(liste[1:], s + liste[0])
        else:
            somme_avec_sous_listes = somme_listes_imbriquees(liste[0], s)
            return somme_listes_imbriquees(liste[1:], somme_avec_sous_listes)


def produit_elements(liste: list) -> float:
    """ Récursivité enveloppée. """
    if len(liste) == 0:
        return 1
    else:
        return liste[0] * produit_elements(liste[1:])


def produit_elements_02(liste: list, m: float) -> float:
    """ Récursivité terminale. """
    if len(liste) == 0:
        return m
    else:
        return produit_elements_02(liste[1:], liste[0] * m)


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