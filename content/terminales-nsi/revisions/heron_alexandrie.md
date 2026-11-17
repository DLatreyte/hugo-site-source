---
title: "Héron d'Alexandrie"
subtitle: ""
date: 2021-09-05T04:24:09+04:00
draft: false
toc: true
tags: []
categories: ["Informatique", "Terminales Spé NSI"]
solution_est_visible: true
auto_numbering: false
mathjax: true
weight: 9900
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

{{< note normal >}}

1. Choisir une première valeur raisonnable que l'on note $G$.
2. Améliorer cette valeur en calculant la moyenne des valeurs $G$ et $a/G$.
3. Vérifier si cette nouvelle valeur convient.
4. Reprendre l'étape 2 tant que la valeur calculée n'est pas satisfaisante.

{{< /note >}}

{{< note goal >}}
Programmer la méthode de Héron en la découpant en petites fonctions, chacune accompagnée de sa spécification et de ses tests.
{{< /note >}}

Avant de programmer, faisons tourner la méthode à la main, pour voir comment elle se comporte.

**Question.** On cherche la racine carrée de $a = 2$ en partant de $G = 1$. Effectuer deux fois l'étape 2 de la méthode, à la main. Comparer le résultat à la valeur $\sqrt{2} \approx \text{1,41421}$.

{{< solution "Réponse" >}}

- Première amélioration : la moyenne de $1$ et de $2/1 = 2$ vaut $\text{1,5}$.
- Deuxième amélioration : la moyenne de $\text{1,5}$ et de $2/\text{1,5} \approx \text{1,33333}$ vaut environ $\text{1,41667}$.

Après deux étapes seulement, le résultat est déjà correct à $\text{0,003}$ près. On comprend pourquoi la méthode marche : si $G$ est trop grand, $a/G$ est trop petit, et inversement. La moyenne des deux tombe entre les deux, plus près de la racine.

{{< /solution >}}

## Travail à réaliser

Le fichier réponse devra se terminer par l'instruction suivante (on découvrira sa signification dans quelques jours)&nbsp;:

```python
if __name__ == "__main__":
    ...
```

Les jeux de tests des questions suivantes sont à placer sous cette instruction, indentés, à la place des points de suspension.

1. Qu'appelle-t-on la **documentation** d'une fonction ? La **spécification** d'une fonction ?

{{< solution "Réponse" >}}

- La **documentation** d'une fonction est le texte placé entre triples guillemets juste sous sa première ligne. Elle explique ce que fait la fonction, ce qu'elle attend et ce qu'elle retourne. Python la conserve : `help(moyenne)` l'affiche dans la console.
- La **spécification** d'une fonction réunit sa signature (son nom, ses paramètres et leurs types, le type de la valeur retournée) et sa documentation. Elle dit *ce que fait* la fonction, sans dire *comment* elle le fait. Avec la spécification seule, on doit pouvoir utiliser la fonction sans lire son code.

{{< /solution >}}

{{< note warning >}}

Toute fonction doit être accompagnée de sa spécification !

{{< /note >}}

2. Définir la fonction `moyenne` dont la spécification est

```python
def moyenne(a: float, b: float) -> float:
    """Calcule et retourne la moyenne des deux nombres a et b
    passés en argument.
    """
```

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert moyenne(12, 16) == 14
assert moyenne(0, 8) == 4
```

{{< solution "Réponse" >}}

```python
def moyenne(a: float, b: float) -> float:
    """
    Calcule et retourne la moyenne des deux nombres a et b
    passés en argument.
    """
    return (a + b) / 2
```

{{< /solution >}}

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

{{< solution "Réponse" >}}

```python
def valeur_absolue(x: float) -> float:
    """
    Calcule et retourne la valeur absolue du nombre x passé en argument.
    """
    if x >= 0:
        return x
    else:
        return -x
```

{{< /solution >}}

4. Définir la fonction `puissance` dont la spécification est&nbsp;:

```python
def puissance(x: float, n: int) -> float:
    """calcule et retourne le résultat de x à la puissance entière n :
    x^n = x . x . x . … . x (n fois)
    """
```

Remarque.
: Il est interdit d'utiliser l'opérateur `**` intégré à Python ou la fonction `pow` du module math.

{{< note tip "Coup de pouce" >}}
$x^n$ est le produit de $n$ facteurs égaux à $x$. On connaît à l'avance le nombre de multiplications à effectuer : quelle boucle faut-il utiliser ? Quelle valeur donner au résultat avant la première multiplication, pour que `puissance(3, 0)` retourne bien 1 ?
{{< /note >}}

Ajouter le jeu de test suivant à la fin du fichier :

```python
assert puissance(2, 8) == 256
assert puissance(0, 2) == 0
assert puissance(3, 0) == 1
```

{{< solution "Réponse" >}}

```python
def puissance(x: float, n: int) -> float:
    """
    calcule et retourne le résultat de x à la puissance entière n :
    x^n = x . x . x . ... . x (n fois)
    """
    resultat: float = 1
    for _ in range(n):
        resultat *= x
    return resultat
```

{{< /solution >}}

5. Définir la fonction `amelioration_essai` dont la spécification est&nbsp;:

```python
def amelioration_essai(essai: float, x: float) -> float:
    """Calcule et retourne la moyenne des nombres essai (strictement positif)
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

{{< solution "Réponse" >}}

```python
def amelioration_essai(essai: float, x: float) -> float:
    """
    Calcule et retourne la moyenne des nombres essai (strictement positif) et x/essai.
    """
    return moyenne(essai, x / essai)
```

{{< /solution >}}

6. Définir le prédicat `est_suffisamment_bon` dont la spécification est&nbsp;:

```python
def est_suffisamment_bon(essai: float, x: float) -> bool:
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
assert not est_suffisamment_bon(1.9, 4)
assert not est_suffisamment_bon(1.999, 4)
assert est_suffisamment_bon(1.9999, 4)
```

{{< solution "Réponse" >}}

```python
def est_suffisamment_bon(essai: float, x: float) -> bool:
    """
    Retourne True si la valeur absolue de la différence du carré du nombre essai
    et du nombre x est inférieure à une tolérance donnée (prendre 0.001).
    Retourne False sinon.
    """
    tolerance = 0.001

    return valeur_absolue(puissance(essai, 2) - x) < tolerance
```

{{< /solution >}}

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
assert abs(test(1, 4) - 2) < 0.001
assert abs(test(7, 4) - 2) < 0.001
```

{{< note warning >}}
La valeur retournée est approchée : `test(1, 4)` vaut `2.0000000929222947`, et non 2. On ne teste donc pas l'égalité de deux flottants avec `==`. On vérifie que leur écart est plus petit qu'une tolérance, ici 0,001. Le premier test peut utiliser `==`, car la valeur de départ 2 est déjà la racine exacte de 4 : la boucle ne s'exécute pas.
{{< /note >}}

{{< note tip "Coup de pouce" >}}
On ne sait pas à l'avance combien d'améliorations seront nécessaires : la boucle est une boucle `while`. Elle doit continuer *tant que* l'essai n'est pas suffisamment bon. Quel prédicat, déjà écrit, permet de l'exprimer ?
{{< /note >}}

{{< solution "Réponse" >}}

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

{{< /solution >}}

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
assert abs(racine_carree(4) - 2) < 0.001
assert abs(racine_carree(9) - 3) < 0.001
assert abs(racine_carree(16) - 4) < 0.001
```

{{< solution "Réponse" >}}

```python
def racine_carree(x: float) -> float:
    """
    Retourne le résultat de l'appel de la fonction test avec la valeur 1 pour l'argument essai.
    """

    return test(1, x)
```

{{< /solution >}}

9. Définir la fonction `main` qui affiche à l'écran la liste des racines carrées de tous les nombres pairs compris dans l'intervalle $[1; 100]$.

Ajouter l'appel de la fonction `main` à la fin du fichier.

{{< note tip "Coup de pouce" >}}
Le premier nombre pair de l'intervalle est 2 et le dernier est 100. Quels arguments donner à `range` pour obtenir directement ces nombres, de deux en deux ? Attention : la borne de fin de `range` est exclue.
{{< /note >}}

{{< solution "Réponse" >}}

```python
def main() -> None:
    """
    Affiche la liste des racines carrées des nombres pairs compris entre 1 et 100.
    """
    print([racine_carree(i) for i in range(2, 101, 2)])
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- expliquer la différence entre la documentation et la spécification d'une fonction ;
- écrire une fonction à partir de sa spécification ;
- écrire une fonction qui utilise des fonctions déjà écrites ;
- écrire une boucle bornée (`for`) quand le nombre de tours est connu, et une boucle non bornée (`while`) quand il ne l'est pas ;
- tester une fonction avec `assert` ;
- comparer deux flottants avec une tolérance plutôt qu'avec `==`.
{{< /note >}}
