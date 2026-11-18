---
title: "Exercices"
subtitle: ""
date: 2020-09-20T05:12:32+04:00
draft: false
toc: true
tags: ["Modules", "Exceptions", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: false
auto_numbering: true
weight: 300
---

{{< note goal >}}
Enquêter sur des erreurs à partir des messages de Python, choisir des tests qui révèlent qu'une fonction ne respecte pas sa spécification, puis écrire un module documenté et testé.
{{< /note >}}

Avant de commencer&nbsp;: une fonction passe les trois tests qu'on a écrits pour elle. Peut-on en conclure qu'elle est correcte&nbsp;?

{{< solution "Réponse" >}}
Non. Des tests réussis montrent seulement que la fonction donne le bon résultat **dans ces trois cas**. Un test qui échoue prouve qu'il y a une erreur&nbsp;; des tests qui réussissent ne prouvent pas qu'il n'y en a pas. Tout l'art consiste à choisir des tests qui ont une chance de révéler une erreur&nbsp;: cas limites (0, chaîne vide, dernière valeur d'un intervalle), majuscules et minuscules, etc.
{{< /solution >}}

## Enquêter sur une erreur dans un calcul de $\pi$

La somme des inverses des carrés des nombres entiers converge vers $\dfrac{\pi^2}{6}$.

$$\sum_{k=1}^{\infty} \dfrac{1}{k^2} = \dfrac{\pi^2}{6}$$

On utilise cette formule pour trouver une approximation de $\pi$.
```python {linenos=table}
import math


def terme(k: int) -> float:
    return 1 / (k**2)


def approxpi(n: int) -> float:
    s = 0.0
    # utilise les termes jusqu'à 1/n**2 inclus
    for k in range(n):
        s = s + terme(k)
    return math.sqrt(s * 6)
```

1. Lors de l’exécution de `approxpi(1000)` une exception est levée à l’exécution de la ligne 5. Quel est le type d’exception ?

    a. `ValueError`  
    b. `SyntaxError`  
    c. `TypeError`  
    d. `ZeroDivisionError`  
    e. `IndexError`  
    f. `NameError`

{{< solution "Réponse" >}}

```python
>>> approxpi(1000)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "main.py", line 12, in approxpi
    s = s + terme(k)
  File "main.py", line 5, in terme
    return 1 / (k**2)
ZeroDivisionError: division by zero
```

{{< /solution >}}

2. Bien que l’exécution soit interrompue ligne 5, la source de l’erreur est ailleurs.  
Expliquer d’où provient l’erreur et proposer un correctif.
{{< solution "Réponse" >}}

- Au premier tour de boucle, `k` vaut 0 et `terme(0)` calcule $1/0$. $k$ ne doit jamais prendre la valeur 0, donc `range` doit commencer à 1.
- Si on veut que la dernière valeur de la boucle soit $n$, comme l'indique le commentaire dans le code, la borne supérieure doit être égale à $n+1$.

```python
for k in range(1, n + 1):
    s = s + terme(k)
```

ou

```python
for k in range(n):
    s = s + terme(k + 1)
```

Avec ce correctif, `approxpi(1000)` retourne environ 3,1406&nbsp;: la série converge lentement.

{{< /solution >}}

## Enquêter sur une erreur de calcul de produit scalaire

Le produit scalaire de deux vecteurs $\vec{u}$ et $\vec{v}$ de l’espace, de coordonnées respectives $(u_1, u_2, u_3)$ et $(v_1, v_2, v_3)$, est le nombre réel $u_1 v_1 + u_2 v_2 + u_3 v_3$.  
Le code suivant permet de calculer des produits scalaires. Il est testé sur des vecteurs de l’espace choisis au hasard :

```python {linenos=table}
import random


def scalaire(v1: tuple[int, ...], v2: tuple[int, ...]) -> int:
    """
    Calcule le produit scalaire des deux vecteurs v1 et v2.
    """
    s = 0
    for k in range(len(v1)):
        s = s + v1[k] * v2[k]
    return s


def random_vect(n: int) -> tuple[int, ...]:
    """
    Génère un vecteur de taille n contenant des entiers non nuls
    entre -10 et 10
    """
    v: list[int] = []
    for _ in range(n):
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)


def main() -> None:
    for _ in range(20):
        print(scalaire(random_vect(3), random_vect(3)))


if __name__ == "__main__":
    main()
```

Prises séparément, les deux fonctions semblent opérationnelles :

```python
>>> scalaire((1, 2, 1), (-1, 3, -2))
3
>>> random_vect(3)
(-6, 2, 8)
```

Pourtant, lorsqu’on exécute la fonction `main()`, le programme n’affiche que quelques produits scalaires (ici 12, 118 et −104) puis lève une exception :

```python
>>> main()
12
118
-104
Traceback (most recent call last):
  File "scal.py", line 33, in <module>
    main()
  File "scal.py", line 29, in main
    print(scalaire(random_vect(3), random_vect(3)))
  File "scal.py", line 10, in scalaire
    s = s + v1[k] * v2[k]
IndexError: tuple index out of range
```

1. En analysant le `traceback` donné plus haut, indiquer quel est le type d’exception qui a été levée, et sur quelle ligne de code.
{{< solution "Réponse" >}}

- L'exception est de type `IndexError`.
- Cette exception est levée à la ligne 10 du code, dans la fonction `scalaire`. Les lignes précédentes du `traceback` indiquent le chemin suivi&nbsp;: l'instruction `main()` (ligne 33) a appelé `scalaire` (ligne 29).
{{< /solution >}}

2. Sur la ligne en question, qu’est-ce qui pourrait avoir provoqué l’erreur ?
{{< solution "Réponse" >}}
L’exception `IndexError` est levée si on essaie d’accéder à une valeur stockée dans une séquence en utilisant un indice invalide, par exemple si on essaie d’accéder à la quatrième valeur d’une liste, d’un tuple ou d’une chaîne de caractères qui n’en contient que 3. À la ligne 10, l’exception a donc été provoquée par l’accès à `v1[k]` ou par l’accès à `v2[k]`, car l’un des deux vecteurs n’a pas de case pour la valeur de `k` à ce tour de boucle. Or `k` varie entre `0` et `len(v1) - 1`&nbsp;: l'accès à `v1[k]` est toujours valide. On en déduit que c’est le vecteur `v2` qui est trop court&nbsp;: il contient moins de valeurs que `v1`. (Depuis Python 3.11, le message d'erreur souligne d'ailleurs `v2[k]` avec des `^`.)
{{< /solution >}}

3. Proposer d’ajouter un affichage `print(...)` à un endroit du programme pour essayer de mettre en évidence la nature du problème, puis exécuter à nouveau le code.
{{< solution "Réponse" >}}
Il faut afficher les valeurs de `v1` et `v2` reçues par `scalaire`.

```python
def scalaire(v1: tuple[int, ...], v2: tuple[int, ...]) -> int:
    """
    Calcule le produit scalaire des deux vecteurs v1 et v2.
    """
    print(f"v1 : {v1} et v2 : {v2}")
    s = 0
    for k in range(len(v1)):
        s = s + v1[k] * v2[k]
    return s
```

{{< /solution >}}

4. Expliquer l’erreur. Pourquoi ne se produit-elle pas toujours au même moment ?
{{< solution "Réponse" >}}

- **Exemple de résultat :**

```text
v1 : (6, 5, 7) et v2 : (8, -5, -1)
16
v1 : (-9, 1, -6) et v2 : (8, -5, 1)
-83
v1 : (-8, -6, -3) et v2 : (-1, 10)
Traceback (most recent call last):
  File "scal.py", line 34, in <module>
    main()
  File "scal.py", line 30, in main
    print(scalaire(random_vect(3), random_vect(3)))
  File "scal.py", line 11, in scalaire
    s = s + v1[k] * v2[k]
IndexError: tuple index out of range
```

- L'erreur a pour origine la façon dont `v1` et `v2` sont créés :

```python
def random_vect(n: int) -> tuple[int, ...]:
    """
    Génère un vecteur de taille n contenant des entiers non nuls
    entre -10 et 10
    """
    v: list[int] = []
    for _ in range(n):
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)
```

On constate que si `val` prend la valeur 0, rien n'est ajouté à la liste `v`. Le nombre de tours de boucle est fixé, mais pas la longueur de `v`&nbsp;: elle vaut 3 seulement si aucun des trois tirages n'a donné 0. Chaque tirage donne 0 avec une probabilité de 1 sur 21&nbsp;: l'erreur apparaît donc au hasard, plus ou moins tôt selon les tirages.
{{< /solution >}}

5. Proposer un correctif.
{{< solution "Réponse" >}}
La solution consiste à utiliser plutôt une boucle `while` avec un test sur la longueur de la liste générée.

```python
def random_vect(n: int) -> tuple[int, ...]:
    """
    Génère un vecteur de taille n contenant des entiers non nuls
    entre -10 et 10
    """
    v: list[int] = []
    while len(v) < n:
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)
```

Pour rendre `scalaire` plus robuste, on peut aussi y vérifier la précondition&nbsp;: `assert len(v1) == len(v2), "les vecteurs n'ont pas la même dimension"`. L'erreur serait alors signalée par un message clair, au lieu d'un `IndexError` qui n'apparaît que si `v2` est le plus court.

{{< /solution >}}

## Calculer la valeur d’un mot : arithmancie

On souhaite associer une valeur numérique à une chaîne de caractères. La valeur associée à la chaîne est la somme des valeurs associées à chacun des caractères qui la composent. Aux lettres non accentuées de A à Z, qu’elles soient en minuscules ou en majuscules, on associe leur numéro d’ordre dans l’alphabet, de 1 à 26. À tous les autres symboles (lettres accentuées, chiffres, espaces, ponctuations), on associe la valeur 0.  
On rappelle que `ord("a")` donne le code numérique associé à la lettre `"a"` passée en paramètre.
La chaîne `string.ascii_uppercase` est définie dans le module `string` et vaut `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`.

1. Pour chacune des propositions suivantes, proposer un test qui montre que la fonction ne répond pas au cahier des charges de l’énoncé.

**Proposition 1**

```python
def valeur1(chaine: str) -> int:
    s = 0
    for c in chaine:
        if c >= "A" and c <= "Z":
            s = s + ord(c) - ord("A") + 1
    return s
```

**Proposition 2**

```python
def valeur2(chaine: str) -> int:
    s = 0
    for c in chaine.upper():
        if c >= "A" and c < "Z":
            s = s + ord(c) - ord("A") + 1
    return s
```

**Proposition 3**

```python
import string


def valeur3(chaine: str) -> int:
    s = 0
    for c in chaine.upper():
        if c in string.ascii_uppercase:
            s = s + string.ascii_uppercase.index(c)
    return s
```

2. Proposer un ensemble complet de tests pour la fonction que l’on veut créer (on nomme cette fonction `valeur`).

3. Proposer le code de cette fonction (il est possible de s’inspirer d’une des versions vues à la question 1. en la corrigeant). Ne pas oublier de vérifier que la fonction écrite passe bien les tests de la question 2.

{{< note tip "Coup de pouce" >}}
Pour la question 1, regarder chaque proposition ligne par ligne en se demandant&nbsp;: que se passe-t-il pour une lettre minuscule&nbsp;? pour la lettre `"Z"`&nbsp;? pour la lettre `"A"`&nbsp;? Un bon test est un cas où l'on sait calculer à la main la valeur attendue.
{{< /note >}}

{{< solution "Réponses" >}}

1. 
    - `valeur1("a")` retourne 0 au lieu de 1&nbsp;: les minuscules sont ignorées.
    - `valeur2("Z")` retourne 0 au lieu de 26&nbsp;: la comparaison stricte `c < "Z"` exclut la lettre Z.
    - `valeur3("A")` retourne 0 au lieu de 1&nbsp;: `index` donne la position à partir de 0, il manque `+ 1`.

2. 

```python
assert valeur("") == 0
assert valeur("A") == 1
assert valeur("a") == 1
assert valeur("Z") == 26
assert valeur("z") == 26
assert valeur("abc") == 6
assert valeur("Bonjour !") == 95
assert valeur("é1 ,") == 0
```

3. 

```python
import string


def valeur(chaine: str) -> int:
    """
    Retourne la somme des numéros d'ordre dans l'alphabet des lettres
    non accentuées de chaine ; les autres caractères valent 0.
    """
    s = 0
    for c in chaine:
        if c in string.ascii_letters:
            s = s + string.ascii_uppercase.index(c.upper()) + 1
    return s
```

`string.ascii_letters` contient les 52 lettres non accentuées, minuscules et majuscules. On ne transforme en majuscule qu'une lettre déjà reconnue&nbsp;: ainsi, un caractère comme `"ß"`, dont la majuscule est `"SS"`, vaut bien 0.

{{< /solution >}}

## Module d’arithmétique

Créer un module contenu dans un fichier nommé `arithmetique.py`. Ce module contient des fonctions sur l’arithmétique des nombres entiers. En particulier :

- `expo` qui prend en paramètres les entiers $a$, $b$ et $n$ et calcule le reste de la division par $n$ de $a^b$&nbsp;;
- `pgcd` qui prend en paramètres les entiers $a$ et $b$ et renvoie le plus grand diviseur commun de $a$ et $b$ ([définition du pgcd]({{% ref "../recursivite/1-1-recursivite-sur-entiers.md#pgcd" %}}))&nbsp;;
- `decomposition` qui prend un entier $n \geqslant 2$ en paramètre et renvoie la liste de ses facteurs premiers ainsi que leur multiplicité, sous la forme d'une liste de tuples `(facteur, multiplicité)`.

1. Créer le module avec les trois fonctions proposées.
2. Proposer des *docstrings* pour le module et les trois fonctions décrites. Annoter les fonctions avec les *annotations de type*.
3. Ajouter quelques tests sous forme d'assertions.

#### Algorithme naïf pour la fonction `decomposition`

La première idée consiste à balayer la liste des nombres premiers en testant si le nombre premier $p$ divise $n$. Si oui, on recommence l'algorithme pour $n//p$, en ne testant que les diviseurs premiers encore envisageables. On s'arrête quand le nombre premier à tester devient supérieur à la racine carrée du nombre qu'il est censé diviser.  
Ainsi pour décomposer 2088 en produit de facteurs premiers

|  |  |  |  |
|:-:|:-:|:-:|-|
| 2088 | 2 |  | 2 divise 2088, le quotient est 1044 |
| 1044 | 2 |  | 2 divise 1044, le quotient est 522 |
| 522 | 2 |  | 2 divise 522, le quotient est 261 |
| 261 | 3 |  | 2 ne divise pas 261, mais 3 divise 261 et le quotient est 87 |
| 87 | 3 |  | 3 divise 87 et le quotient est 29 |
| 29 |  |  | ni 3, ni 5 ne divisent 29 et $7^2$ est plus grand que 29 (fin) |

On obtient la décomposition attendue : $2088=2^3 \times 3^2 \times 29$.
<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Décomposition_en_produit_de_facteurs_premiers" >Wikipedia</a>
</div>

{{< note tip "Coup de pouce" >}}
Pour `expo`, calculer $a^b$ puis le reste de la division par $n$ fonctionne, mais $a^b$ devient vite énorme. On peut prendre le reste à chaque multiplication&nbsp;: le reste de $x \times a$ ne dépend que du reste de $x$. Pour `decomposition`, il n'est pas nécessaire de connaître la liste des nombres premiers&nbsp;: si l'on teste les diviseurs dans l'ordre croissant en divisant $n$ autant de fois que possible, chaque diviseur trouvé est forcément premier.
{{< /note >}}

{{< solution "Solution" >}}

```python
"""
Module d'arithmétique des nombres entiers : exponentiation modulaire,
pgcd et décomposition en produit de facteurs premiers.
"""


def expo(a: int, b: int, n: int) -> int:
    """
    Retourne le reste de la division de a**b par n.
    Le reste est pris à chaque étape, pour que les nombres restent petits.

    HYPOTHÈSE : b entier naturel, n entier strictement positif.
    """
    resultat = 1 % n
    for _ in range(b):
        resultat = (resultat * a) % n
    return resultat


def pgcd(a: int, b: int) -> int:
    """
    Retourne le plus grand diviseur commun de a et b (algorithme d'Euclide).

    HYPOTHÈSE : a et b entiers naturels.
    """
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


def decomposition(n: int) -> list[tuple[int, int]]:
    """
    Retourne la décomposition de n en produit de facteurs premiers,
    sous la forme d'une liste de tuples (facteur, multiplicité).

    HYPOTHÈSE : n entier, n >= 2.
    """
    facteurs: list[tuple[int, int]] = []
    p = 2
    while p * p <= n:
        multiplicite = 0
        while n % p == 0:
            n //= p
            multiplicite += 1
        if multiplicite > 0:
            facteurs.append((p, multiplicite))
        p += 1
    if n > 1:  # ce qui reste est un nombre premier
        facteurs.append((n, 1))
    return facteurs


if __name__ == "__main__":
    assert expo(3, 4, 5) == 1  # 3**4 = 81 = 16 * 5 + 1
    assert expo(2, 10, 1000) == 24
    assert expo(7, 0, 5) == 1
    assert pgcd(12, 18) == 6
    assert pgcd(17, 5) == 1
    assert decomposition(2088) == [(2, 3), (3, 2), (29, 1)]
    assert decomposition(97) == [(97, 1)]
```

Dans `decomposition`, on teste tous les entiers $p$ à partir de 2, et pas seulement les nombres premiers&nbsp;: quand on arrive à un nombre composé comme 4, ses facteurs (ici 2) ont déjà été retirés de $n$, et il ne peut plus diviser $n$.

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- lire un `traceback` pour trouver le type d'une exception et la ligne où elle est levée ;
- remonter de la ligne où l'erreur se manifeste à sa véritable cause ;
- ajouter des affichages pour observer les valeurs des variables pendant l'exécution ;
- trouver un test qui montre qu'une fonction ne respecte pas sa spécification, et écrire un jeu de tests complet ;
- écrire un module documenté, annoté et testé.
{{< /note >}}
