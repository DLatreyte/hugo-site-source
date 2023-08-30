---
title: "Héron d'Alexandrie"
subtitle: ""
author: ""
type: ""
date: 2021-09-05T04:24:09+04:00
draft: false
toc: true
tags: []
categories: ["Informatique", "Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: false
mathjax: true
---

Héron d'Alexandrie est un ingénieur, un mécanicien et un
mathématicien grec du premier siècle après J.-C.

On ne sait pas grand chose de la vie d'Héron, si ce n'est qu'il était
originaire d'Alexandrie ; les historiens se sont même longtemps
divisés sur l'époque où il a vécu. Leurs estimations allaient
du 1<sup>er</sup> siècle avant J.-C. au 3<sup>ème</sup> siècle de
notre ère. Aujourd'hui, la querelle est éteinte&nbsp;: il est clairement
établi que Héron est postérieur à Vitruve mort en $- 20$, et
contemporain de Pline l'Ancien (23 -- 79), en étant actif autour de l'an
62. Il a donc bien vécu au 1<sup>er</sup> siècle après J.-C. et sans
doute au début du 2<sup>ème</sup> siècle, donc sous l'Empire romain,
mais dans l'Alexandrie grecque.

On attribue à Héron d'Alexandrie plusieurs formules mathématiques
et une méthode efficace d'extraction de racine carrée,
c'est-à-dire de résolution de l'équation $x^2 = a$, avec $a$
positif&nbsp;:

{{% note normal %}}

1. Choisir une première valeur raisonnable que l'on note $G$.
2. Améliorer cette valeur en calculant la moyenne des valeurs $G$ et $x/G$.
3. Vérifier si cette nouvelle valeur convient.
4. Reprendre l'étape 2 tant que la valeur calculée n'est pas satisfaisante.

{{% /note %}}

> L'objectif de cette activité est de mettre en œuvre cette méthode en Python.

## Travail à réaliser

Le fichier réponse devra se terminer par les instructions&nbsp; afin de pouvoir y placer les jeux de tests pour les différentes fonctions (on découvrira la signification de cette instruction dans quelques jours).

```python
if __name__ == "__main__":
```

1. Qu'appelle-t-on la **documentation** d'une fonction ? La **spécification** d'une fonction ?

{{% note warning %}}

Toute fonction doit être accompagnée de sa spécification !

{{% /note %}}

2. Définir la fonction `moyenne` dont la spécification est

```python
def moyenne(a: float, b: float) -> float: 
    """ Calcule et retourne la moyenne des deux nombres a et b 
    passés en argument.
    """
```

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert moyenne(12, 16) == 14
assert moyenne(0, 8) == 4
```

{{% solution "Réponse" %}}

```python
def moyenne(a: float, b: float) -> float:
    """
    Calcule et retourne la moyenne des deux nombres a et b
    passés en argument.
    """
    return (a + b) / 2
```

{{% /solution %}}

3. Définir la fonction `valeur_absolue` dont la spécification est&nbsp;:

```python
def valeur_absolue(x: float) -> float: 
    """ 
    Calcule et retourne la valeur absolue du nombre x passé en argument.
    """
```

Remarque.
: Il est interdit d'utiliser la fonction `abs` intégrée à Python.

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert valeur_absolue(3) == 3
assert valeur_absolue(0) == 0
assert valeur_absolue(-3) == 3
```

{{% solution "Réponse" %}}

```python
def valeur_absolue(x: float) -> float:
    """
    Calcule et retourne la valeur absolue du nombre x positif
    passé en argument.
    """
    if x >= 0 :
        return x
    else:
        return -x
```

{{% /solution %}}

4. Définir la fonction `puissance` dont la spécification est&nbsp;:

```python
def puissance(x: float, n: int) -> float: 
    """ calcule et retourne le résultat de x à la puissance entière n :
    x^n = x . x . x . … . x (n fois)
    """
```

Remarque.
: Il est interdit d'utiliser l'opérateur `**` intégré à Python ou la fonction `pow` du module math.

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert puissance(2, 8) == 256
assert puissance(0, 2) == 0
assert puissance(3, 0) == 1
```

{{% solution "Réponse" %}}

```python
def puissance(x: float, n: int) -> float:
    """
    calcule et retourne le résultat de x à la puissance entière n :
    x^n = x . x . x . ... . x (n fois)
    """
    res = 1
    for i in range(1, n + 1):
        res *= x
    return res
```

{{% /solution %}}

5. Définir la fonction `amelioration_essai` dont la spécification est&nbsp;:

```python
def amelioration_essai(essai: float, x: float) -> float: 
    """ Calcule et retourne la moyenne des nombres essai (strictement positif) 
    et x/essai.
    """
```

Remarque.
: Cette fonction doit utiliser la fonction `moyenne` définie plus haut.

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert amelioration_essai(1, 2) == 1.5
assert amelioration_essai(2, 1) == 1.25
```

{{% solution "Réponse" %}}

```python
def amelioration_essai(essai: float, x: float) -> float:
    """
    Calcule et retourne la moyenne des nombres essai (strictement positif) et x/essai.
    """
    return moyenne(essai, x/essai)
```

{{% /solution %}}

6. Définir le prédicat `est_suffisamment_bon` dont la spécification est&nbsp;:

```python
def est_suffisamment_bon(essai: float, x: float) -> float: 
    """ 
    Retourne True si la valeur absolue de la différence du carré du nombre essai 
    et du nombre x est inférieure à une tolérance donnée (prendre 0.001).
    Retourne False sinon.
    """
```

Remarque.
: Cette fonction doit utiliser les fonctions `valeur_absolue` et `puissance` définies ci-dessus.

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert est_suffisamment_bon(1.9, 4) == False
assert est_suffisamment_bon(1.999, 4) == False
assert est_suffisamment_bon(1.9999, 4) == True
```

{{% solution "Réponse" %}}

```python
def est_suffisamment_bon(essai: float, x: float) -> float:
    """
    Retourne True si la valeur absolue de la différence du carré du nombre essai
    et du nombre x est inférieure à une tolérance donnée (prendre 0.001).
    Retourne False sinon.
    """
    tolerance = 0.001

    return valeur_absolue(puissance(essai, 2) - x) < tolerance
```

{{% /solution %}}

7. Définir la fonction `test` qui implémente l'algorithme de Héron d'Alexandrie. La spécification de la fonction est&nbsp;:

```python
def test(essai: float, x: float) -> float: 
    """ 
    Retourne la racine carrée du nombre x. Le calcul est effectué grâce à un
    raisonnement itératif depuis une première valeur strictement positive notée essai.
    """
```

Remarque.
: Cette fonction doit utiliser les fonctions `est_suffisamment_bon` et `amelioration_essai`.

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert test(2, 4) == 2
assert test(1, 4) == 2.0000000929222947
assert test(7, 4) == 2.0000000271231317
```

{{% solution "Réponse" %}}

```python
def test(essai: float, x: float) -> float:
    """
    Retourne la racine carrée du nombre x. Le calcul est effectué grâce à un
    raisonnement itératif depuis une première valeur strictement positive notée
    essai.
    """
    while not est_suffisamment_bon(essai, x):
        essai = amelioration_essai(essai, x)
    return essai
```

{{% /solution %}}

8. Définir la fonction `racine_carree` dont la spécification est&nbsp;:

```python
def racine_carree(x: float) -> float: 
    """ 
    Retourne le résultat de l'appel de la fonction test avec la valeur 1 
    pour l'argument essai.
    """
```

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert racine_carree(4) == 2.0000000929222947
assert racine_carree(9) == 3.00009155413138
assert racine_carree(16) == 4.000000636692939
```

{{% solution "Réponse" %}}

```python
def racine_carree(x: float) -> float:
    """
    Retourne le résultat de l'appel de la fonction test avec la valeur 1 pour l'argument essai.
    """

    return test(x, 1)
```

{{% /solution %}}

9. Définir la fonction `main` qui affiche à l'écran la liste des racines carrées de tous les nombres pairs compris dans l'intervalle $[1; 100]$.

Ajouter l'appel de la fonction `main` à la fin du fichier.

{{% solution "Réponse" %}}

```python
def main():
    return [racine_carree(i) for i in range(1, 100) if i % 2 == 0]
```

{{% /solution %}}
