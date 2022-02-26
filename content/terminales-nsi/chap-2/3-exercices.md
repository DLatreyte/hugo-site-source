---
title: "Exercices"
subtitle: "Chapitre 2,3"
author: ""
type: ""
date: 2020-09-20T05:12:32+04:00
draft: false
toc: true
tags: ["Modules", "Exceptions", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Enquêter sur une erreur dans un calcul de $\pi$

La somme des inverses des carrés des nombres entiers converge vers $\dfrac{\pi^2}{6}$.

$$\sum_{k=1}^{\infty} \dfrac{1}{k^2} = \dfrac{\pi^2}{6}$$

On utilise cette formule pour trouver une approximation de $\pi$.
{{< highlight py3 "linenos=table" >}}
import math


def terme(k: int) -> float:
    return 1 / (k**2)


def approxpi(n: int) -> float:
    s = 0
    # utilise les termes jusqu’à 1/n**2 inclus
    for k in range(n):
        s = s + terme(k)
    return math.sqrt(s * 6)
{{< /highlight >}}

1. Lors de l’exécution de `approxpi(1000)` une exception est levée à l’exécution de la ligne 5. Quel est le type d’exception ?   
    a. `ValueError`  
    b. `SyntaxError`  
    c. `TypeError`   
    d. `ZeroDivisionError`  
    e. `IndexError`    
    f. `NameError`

{{% solution "Réponse" %}}
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
{{% /solution %}}

2. Bien que l’exécution soit interrompue ligne 5, la source de l’erreur est ailleurs  
Expliquer d’où provient l’erreur et proposer un correctif.
{{% solution "Réponse" %}}
- $k$ ne doit jamais prendre la valeur 0, donc `range` doit commencer à 1. 
- Si on veut que la dernière valeur de la boucle soit $n$, comme l'indique le commentaire dans le code, la borne supérieure doit être égale à $n+1$.
```python
for k in range(1, n+1):
        s = s + terme(k)
```
ou 
```python
    for k in range(n):
        s = s + terme(k + 1)
```
{{% /solution %}}


## Enquêter sur une erreur de calcul de produit scalaire

Le produit scalaire de deux vecteurs $\vec{u}$ et $\vec{v}$ de l’espace, de coordonnées respectives $(u_1, u_2, u_3)$ et $(v_1, v_2, v_3)$, est le nombre réel $u_1 v_1 + u_2 v_2 + u_3 v_3$.  
Le code suivant permet de calculer des produits scalaires. Il est testé sur des vecteurs de l’espace choisis au hasard :

{{< highlight py3 "linenos=table" >}}
import random
from typing import Tuple

def scalaire(v1: Tuple[int], v2: Tuple[int]) -> float:  
    """
    Calcule le produit scalaire des deux vecteurs v1 et v2.
    """
    s = 0
    for k in range(len(v1)):
        s = s + v1[k] * v2[k]
    return s

def random_vect(n: int) -> tuple:
    """
    Génère un vecteur de taille n contenant des entiers non nuls 
    entre -10 et 10
    """
    v = []
    for i in range(n):
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)

def main():
    for i in range(20):
        print(scalaire(random_vect(3), random_vect(3)))
        
main()
{{< /highlight >}}

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
  File "scal.py", line 28, in <module> 
    main() 
  File "scal.py", line 26, in main 
    print(scalaire(random_vect(3), random_vect(3))) 
  File "scal.py", line 9, in scalaire 
    s = s + v1[k] * v2[k]
IndexError: tuple index out of range
```

1. En analysant le `traceback` donné plus haut, indiquer quel est le type d’exception qui a été levée, et sur quelle ligne de code.
{{% solution "Réponse" %}}
- L'exception est de type `IndexError`.
- Cette exception est levée à la ligne 9 du code.
{{% /solution %}}

2. Sur la ligne en question, qu’est-ce qui pourrait avoir provoqué l’erreur ?
{{% solution "Réponse" %}}
L’exception `IndexError` est levée si on essaie d’accéder à une valeur stockée dans une séquence en utilisant un indice invalide, par exemple si on essaie d’accéder à la quatrième valeur d’une liste, d’un tuple ou d’une chaîne de caractères qui n’en contient que 3. À la ligne 9, l’exception a donc été provoquée par l’accès à `v1[k]` ou par l’accès à `v2[k]`, car l’un des deux vecteurs (ou les deux) n’a pas de case pour la valeur de `k` à ce tour de boucle. Or `k` varie entre `0` et `len(v1)`. On en déduit que c’est le vecteur `v2` qui est trop court : soit `v1` a plus de 3 valeurs (et `v2` en a bien 3), soit `v1` a bien 3 valeurs et il en manque dans `v2`.
{{% /solution %}}

3. Proposer d’ajouter un affichage `print(...)` à un endroit du programme pour essayer de mettre en évidence la nature du problème, puis exécuter à nouveau le code.
{{% solution "Réponse" %}}
Il faut vérifier quelles valeur de `v1` et `v2`.
```python
def scalaire(v1: tuple, v2: tuple) -> float:  
    """
    Calcule le produit scalaire des deux vecteurs v1 et v2.
    """
    print("v1 : {} et v2 : {}".format(v1, v2))
    s = 0
    for k in range(len(v1)):
        s = s + v1[k] * v2[k]
    return s
```
{{% /solution %}}

4. Expliquer l’erreur. Pourquoi ne se produit-elle pas toujours au même moment ?
{{% solution "Réponse" %}}
- **Exemple de résultat :**
```python
v1 : (6, 5, 7) et v2 : (8, -5, -1)
16
v1 : (-9, 1, -6) et v2 : (8, -5, 1)
-83
v1 : (-8, -6, -3) et v2 : (-1, 10)
Traceback (most recent call last):
  File "main.py", line 52, in <module>
    main()
  File "main.py", line 50, in main
    print(scalaire(random_vect(3), random_vect(3)))
  File "main.py", line 33, in scalaire
    s = s + v1[k] * v2[k]
IndexError: tuple index out of range
```
- L'erreur a pour origine la façon dont `v1` et `v2` sont créés :
```python
def random_vect(n: int) -> tuple:
    """
    Génère un vecteur de taille n contenant des entiers non nuls 
    entre -10 et 10
    """
    v = []
    for i in range(n):
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)
```
On constate que si `val` prend la valeur 0 rien n'est ajouté à la liste `v`. On ne peut donc pas être certain de la longueur de `v` puisque le nombre de tour de boucle est lui fixé.
{{% /solution %}}

5. Proposer un correctif.
{{% solution "Réponse" %}}
La solution consiste à utiliser plutôt une boucle `TantQue` avec un test sur la longueur de la liste générée.
```python
def random_vect(n: int) -> tuple:
    """
    Génère un vecteur de taille n contenant des entiers non nuls 
    entre -10 et 10
    """
    v = []
    while len(v) < n:
        val = random.randint(-10, 10)
        if val != 0:
            v.append(val)
    return tuple(v)
```
{{% /solution %}}

## Calculer la valeur d’un mot : arithmancie

On souhaite associer une valeur numérique à une chaîne de caractères. La valeur associée à la chaîne est la somme des valeurs associées à chacun des caractères qui la composent. Aux lettres non accentuées de A à Z, qu’elles soient en minuscules ou en majuscules, on associe leur numéro d’ordre dans l’alphabet, de 1 à 26. À tous les autres symboles (lettres accentuées, chiffres, espaces, ponctuations), on associe la valeur 0.  
On rappelle que `ord("a")` donne le code numérique associé à la lettre `"a"` passée en paramètre.   
La chaîne `string.ascii_uppercase` est définie dans le module `string` et vaut `"ABCDEFGHIJKLMNOPQRSTUVWXYZ"`.

1. Pour chacune des propositions suivantes, proposer un test qui montre que la fonction ne répond pas au cahier des charges de l’énoncé.

**Proposition 1**
```python
def valeur1(chaine):
    s = 0 
    for c in chaine: 
        if c >= "A" and c <= "Z": 
            s = s + ord(c) - ord('A') + 1 
    return s
```

**Proposition 2**

```python
def valeur2(chaine) : 
    s = 0 
    for c in chaine.upper(): 
        if c >= "A" and c < "Z": 
            s = s + ord(c) - ord('A') + 1 
    return s
```

**Proposition 3**
```python
import string
def valeur3(chaine): 
    s = 0 
    for c in chaine.upper(): 
        if c in string.ascii_uppercase: 
            s = s + string.ascii_uppercase.index(c) 
    return s
```

2. Proposer un ensemble complet de tests pour la fonction que l’on veut créer (on nomme cette fonction `valeur`).

3. Proposer le code de cette fonction (il est possible de s’inspirer d’une des versions vues à la question 1. en la corrigeant). Ne pas oublier de vérifier que la fonction écrite passe bien les tests de la question 2.

## Module d’arithmétique

Créer un module contenu dans un fichier nommé `arithmetique.py`. Ce module contient des fonctions sur l’arithmétique des nombres entiers. En particulier :

– `expo` qui prend en paramètres les entiers $a$, $b$ et $n$ et calcule le reste de la division par $n$ de $a^b$ ;

– `pgcd` qui prend en paramètres les entiers $a$ et $b$ et renvoie le plus grand diviseur commun de $a$ et $b$ ([définition du pgcd]({{% ref "../chap-1/1-1-recursivite-sur-entiers.md#pgcd" %}})) ;

– `decomposition` qui prend un entier positif $n$ en paramètre et renvoie la liste de ses facteurs premiers ainsi que leur multiplicité.

1. Créer le module avec les trois fonctions proposées.
2. Proposer des *dosctrings* pour le module et les trois fonctions décrites. Annoter les fonctions avec les *annotations de type*.
3. Ajouter quelques tests sous forme d'assertions.

#### Algorithme naïf pour la fonction `decomposition` 
La première idée consiste à balayer la liste des nombres premiers en testant si le nombre premier $p$ divise $n$. Si oui, on recommence l'algorithme pour $n//p$, en ne testant que les diviseurs premiers encore envisageables. On s'arrête quand le nombre premier à tester devient supérieur à la racine carrée du nombre qu'il est censé diviser.  
Ainsi pour décomposer 2088 en produit de facteurs premiers

|  |  |  |  |
|:-:|:-:|:-:|-|
| 2088 | 2 |  | 2 divise 2088 le quotient est 1044 |
| 1044 | 2 |  | 2 divise 1044, le quotient est 522 |
| 522 | 2 |  | 2 divise 522, le quotient est 261 |
| 261 | 3 |  | 2 ne divise pas 261, mais 3 divise 261 et le quotient est 87 |
| 87 | 3 |  | 3 divise 87 et le quotient est 29 |
| 29 |  |  | ni 3, ni 5 ne divisent 29 et $7^2$ est plus grand que 29 (fin) |

On obtient la décomposition attendue : $2088=2^3 \times 3^2 \times 29$.
<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Décomposition_en_produit_de_facteurs_premiers" >Wikipedia</a>
</div>





