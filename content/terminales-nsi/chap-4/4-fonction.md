---
title: "Résoudre un problème grâce aux paradigmes objet et fonctionnel"
subtitle: "Chapitre 4,4"
author: ""
type: ""
date: 2020-10-01T04:21:17+04:00
draft: false
toc: true
tags: ["Objet", "Classe", "Attribut", "Méthode", "Instance", "Encapsulation", "Fermeture", "Closure"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

L'objectif de ce document est d'illustrer une fois encore l'intérêt des différents paradigmes de programmation.

## Cas d'étude&nbsp;: fonction avec paramètres

On considère l'équation qui traduit le mouvement d'une balle lancée verticalement vers le haut avec une vitesse $\vec{v}_0$ depuis l'origine des altitudes telle que l'écrit un physicien&nbsp;: $$y(t) = -\dfrac{1}{2}g\\, t^2 + v_0\\, t$$
Ce physicien a donc tendance à considérer que $y$ est une fonction de la variable $t$ et que cette fonction dépend des paramètres $v_0$ et $g$. 

1. Comment définir cette fonction en informatique, sachant que $g$ est un paramètre fixe $g=\pu{9,81 m/s2}$ mais que $v_0$ est un paramètre qu'il peut être utile de faire varier&nbsp;?
{{% solution "Réponse" %}}
```python
def y(t: float, v0: float) -> float:
    """
    Calcule l'altitude d'une balle lancée vers le haut verticalement avec la vitesse v0 au cours du temps depuis l'origine des altitudes.

    REMARQUE : la fonction définit un paramètre constant g = 9.81
    """
    g = 9.81
    return -0.5 * g * t**2 + v0 *t
```
{{% /solution %}}

## Problème
Le physicien qui vient de définir la fonction de la question 1. peut vouloir utiliser les fonctions que certains modules, tels que les modules `math`, `numpy` ou `scipy`, proposent. Ces fonctions étant les plus générales possibles, elles implémentent le point de vue du physicien, $y$ est une fonction de $t$, plutôt que celui de l'informaticien, $y$ est une fonction de $t$ et de $v_0$.   
*Comment modifier la définition de la fonction `y` pour qu'elle puisse être utilisée avec n'importe quelle autre fonction&nbsp;?*

## Illustration du problème

On peut avoir envie de déterminer la vitesse $v_y(t)$ de la balle. La relation mathématique entre $v_y(t)$ et $y(t)$ est la suivante $$v_y(t) = \dfrac{\mathrm{d} y}{\mathrm{dt}} = y\rq (t)$$
$v_y(t)$ est la dérivée par rapport au temps de $y(t)$.

On peut montrer, en analyse numérique, que, en un point d'abscisse $x_0$ 
$$ f\rq (x_0) \approx \dfrac{f(x_0 + h) - f(x_0)}{h}$$

2. Définir la fonction `diff` dont la spécification est&nbsp;:
```python
def diff(f: Callable, x0: float, h: float=1E-7) -> float:
    """
    Calcule la dérivée de la fonction f au point d'abscisse x0.

    REMARQUE : le paramètre h est fixé à h = 1e-7 par défaut.
    """
``` 
{{% solution "Réponse" %}}
```python
def diff(f: Callable, x0: float, h: float = 1E-7) -> float:
    """
    Calcule la dérivée de la fonction f au point d'abscisse x0.

    REMARQUE : le paramètre h est fixé à h = 1e-5 par défaut.
    """
    return (f(x0 + h) - f(x0)) / h
```
{{% /solution %}}

3. Tester cette fonction en calculant la dérivée de $\cos(x)$ au point $x=0$.   
**Rappel :** $(\cos (0))\rq = -\sin(0) = 0$.
{{% solution "Réponse" %}}
```python
import math as m
print(diff(m.cos, 0))
```
{{% /solution %}}

4. La fonction `diff` peut-elle être utilisée pour déterminer la dérivée de la fonction `y`&nbsp;?
{{% solution "Réponse" %}}
Non, puisque `diff` ne prend que le nom de la fonction à dériver en argument et pas ses paramètres. `diff` suppose que la fonction `f` est une fonction à une seule variable.
{{% /solution %}}

## Première (très mauvaise !) solution&nbsp;: utilisation d'une variable globale

5. Écrire la fonction `y1` dont la spécification est 
```python
def y1(t: float) -> float:
    """
    Calcule l'altitude d'une balle lancée vers le haut verticalement avec la vitesse v0 au cours du temps depuis l'origine des altitudes.

    REMARQUE : la fonction définit un paramètre constant g = 9.81

    REMARQUE : la fonction utilise la variable globale v0.
    """
```

6. Déterminer la valeur de la vitesse de la balle à la date $t=\pu{0,1 s}$ en utilisant la fonction `y1`.   
**Remarque&nbsp;:** $v0 = \pu{3 m/s}$ et la réponse attendue est $v_y = \pu{2,02 m/s}$.
{{% solution "Réponse" %}}
```python
v0 = 3
t = 0.1
print(diff(y1, t))
```
{{% /solution %}}

7. Pourquoi est-ce une mauvaise idée que d'utiliser des variables globales&nbsp;?
{{% solution "Réponse" %}}
Une variable globale peut être utilisée et modifiée à plusieurs endroits d'un programme. Il n'est pas toujours facile, lors de l'appel d'une fonction utilisant une variable globale, de savoir exactement quelle est sa valeur.
{{% /solution %}}

## Deuxième méthode&nbsp;: représenter une fonction par une classe

### Sans utilisation des méthodes spéciales

{{% note tip %}}
Une **classe** définit un **nouveau type** et est constituée d'**attributs** (variables) et de **méthodes** (fonctions). *Les attributs sont accessibles en lecture et en modification par toutes les méthodes*&nbsp;; ce sont des **variables globale à la classe** !
{{% /note %}}

8. Définir la classe `Y1` dont la spécification est 
```python
class Y1():
    """
    Classe représentant la fonction mathématique y.
    
    Attributs
    ---------
    g : float
        Paramètre g dont la valeur est fixée à l'initialisation de l'objet.
    v0 : float
        Paramètre v0 dont la valeur est récupérée à l'initialisation de l'objet.
        
    Méthode
    -------
    valeur(self, t: float) -> float
        Retourne la valeur de y à la date t passée en argument.
    """
```
{{% solution "Réponse" %}}
```python
class Y1():
    """
    Classe représentant la fonction mathématique y.
    
    Attributs
    ---------
    g : float
        Paramètre g dont la valeur est fixée à l'initialisation de l'objet.
    v0 : float
        Paramètre v0 dont la valeur est récupérée à l'initialisation de l'objet.
        
    Méthode
    -------
    valeur(self, t: float) -> float
        Retourne la valeur de y à la date t passée en argument.
    """
    def __init__(self, v0: float, g: float = 9.81) -> None:
        self.v0 = v0
        self.g = g

    def valeur(self, t: float) -> float:
        """
        Retourne la valeur de y à la date t passée en argument.
        """
        return -0.5 * self.g * t**2 + self.v0 * t
```
{{% /solution %}}

9. Créer un objet de type `Y1` et vérifier que la valeur de la fonction $y$ à la date $t=\pu{0,1 s}$, lorsque $v_0=\pu{3 m/s}$ est $\pu{0,25 m}$.
{{% solution "Réponse" %}}
```python
yo = Y1(3)
print(yo.valeur(0.1))  # ou assert yo.valeur(0.1) == y(0.1, 3)
``` 
{{% /solution %}}

10. Déterminer la vitesse de la balle à cet instant.
{{% solution "Réponse" %}}
```python
yo = Y1(3)
print(diff(yo.valeur, 0.1))
``` 
{{% /solution %}}

### En utilisant une méthode spéciale

On peut penser que la définition de la classe `Y1` fait trop apparaître le concept d'objet au détriment de celui de fonction. En particulier, l'appel `yo.valeur(0.1)` n'est pas aussi clair que `yo(0.1)`.  
Les classes possèdent cependant, en Python, une méthode spéciale nommée `__call__` appelée automatiquement chaque fois que l'on *utilise un objet comme une fonction*.

11. Définir la classe `Y2` dont le code est proche de celui de `Y1` mais qui redéfinit la méthode `__call__` à la place de définir la méthode `valeur`.
{{% solution "Réponse" %}}
```python
class Y2():
    """
    Classe représentant la fonction mathématique y.
    
    Attributs
    ---------
    g : float
        Paramètre g dont la valeur est fixée à l'initialisation de l'objet.
    v0 : float
        Paramètre v0 dont la valeur est récupérée à l'initialisation de l'objet.
    """

    def __init__(self, v0: float, g: float = 9.81) -> None:
        self.v0 = v0
        self.g = g

    def __call__(self, t: float) -> float:
        """
        Retourne la valeur de y à la date t passée en argument.
        """
        return -0.5 * self.g * t**2 + self.v0 * t
```
{{% /solution %}}

12. Déterminer la vitesse de la balle à dans les mêmes conditions qu'à la question 10.
{{% solution "Réponse" %}}
```python
yo = Y2(3)
print( yo(0.1) )
``` 
{{% /solution %}}

## Troisième méthode&nbsp;: premiers pas dans le monde fonctionnel

{{% note tip %}}
En **programmation fonctionnelle**, *les fonctions sont des objets de première classe*&nbsp;: *une fonction peut être **passée comme argument** à une autre fonction*, *une fonction peut **retourner une fonction***.
{{% /note %}}

Étudier le code suivant 
```python
def fixe_param(v0: float) -> Callable:
    g = 9.81

    def calcule_y(t: float) -> float:
        return -0.5 * g * t**2 + v0 * t

    return calcule_y

y3 = fixe_param(3)
print( y3(0.1) )
``` 

13. Qu'attend comme argument la fonction `fixe_param`&nbsp;?
{{% solution "Réponse" %}}
`fixe_param` possède le paramètre `v0`.
{{% /solution %}}

14. Que sont les variables `v0` et `g` pour la fonction `calcule_y`&nbsp;?
{{% solution "Réponse" %}}
Ce sont des variables externes (non locales). En fait `calcule_y` les considère comme des variables globales (même si elles sont seulement locales à la fonction `fixe_param`). Le dernier point de ce document précise le vocabulaire.
{{% /solution %}}

15. Quel est le type de `y3`&nbsp;?
{{% solution "Réponse" %}}
`y3` référence une fonction.
{{% /solution %}}

16. Que signifie l'instruction `y3(0.1)`&nbsp;?
{{% solution "Réponse" %}}
`y3(0.1)` est un appel de fonction. On appelle la fonction référencée par la variable `y3` avec l'argument 0.1.
{{% /solution %}}

{{% note normal %}}
Utiliser le site [Pythontutor](http://pythontutor.com) pour bien comprendre l'effet de chacune des instructions.
{{% /note %}}

17. Quelles lignes de code faudrait-il modifier si maintenant la balle est lancée à la vitesse $v_0 = \pu{5 m/s}$ et que l'on cherche toujours sa position à la date $t = \pu{0,1 s}$&nbsp;?
{{% solution "Réponse" %}}
```python
y5 = fixe_param(5)
print( y5(0.1) )
```
{{% /solution %}}

18. Quel est le rôle de la fonction `fixe_param`&nbsp;?
{{% solution "Réponse" %}}
`fixe_param` enveloppe `calcule_y`, elle permet de réaliser une fermeture (closure).
{{% /solution %}}

{{% note tip %}}
Dans un langage de programmation, une **fermeture** (en anglais&nbsp;: *closure*) est une *fonction accompagnée de son environnement lexical*. L'**environnement lexical** d'une fonction est l'**ensemble des variables non locales qu'elle a capturé**, soit par valeur (c'est-à-dire par copie des valeurs des variables), soit par référence (c'est-à-dire par copie des adresses mémoires des variables). *Une fermeture est donc créée, entre autres, lorsqu'une fonction est définie dans le corps d'une autre fonction et utilise des paramètres ou des variables locales de cette dernière*.
<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Fermeture_(informatique)#Python">Wikipedia</a>
</div>
{{% /note %}}