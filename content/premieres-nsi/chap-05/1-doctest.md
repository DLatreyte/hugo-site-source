---
title: "Tester ses fonctions avec doctest"
subtitle: "Chapitre 5,1"
author: ""
type: ""
date: 2021-08-29T16:36:33+04:00
draft: true
toc: true
tags: ["Fonctions", "Python", "Jeux de tests", "doctest"]
categories: ["Première Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}

Le travail qui suit s'appuie sur la définition de la fonction `kelvin_vers_celsius` suivante :

```python
def kelvin_vers_celsius(t: float) -> float:
    """ 
    Convertit la température donnée en kelvin en une température θ en degrés celsius.
    Relation : θ = t - 273.15.
    
    >>> kelvin_vers_celsius(0) -273.15
    >>> kelvin_vers_celsius(273.15) 0.0
    """
    offset = -273.15
    return t + offset
```

{{% /note %}}

## Première utilisation du module `doctest`

### À quoi sert le module `doctest` ?

#### À faire ####

1. Taper le code complet de la définition de la fonction `kelvin_vers_celsius` dans un fichier.

2. Écrire, sur la première ligne du fichier, l'instruction :
```python
import doctest
```
Enregistrer le fichier contenant le code précédent.

3. Charger le fichier dans l'interpréteur. La fonction peut être appelée, rien de particulier n'apparaît pour l'instant.
```python
>>> kelvin_vers_celsius(373.15)
100.0
```

4. Entrer et exécuter l'instruction suivante :
```python
>>> doctest.testmod()
TestResults(failed=0, attempted=2)
```
La fonction `testmod` du module `doctest` semble avoir effectué deux tests (`attempted=2`) sans avoir rencontré le moindre problème (`failed=0)`.\
Mais quels tests a-t-elle effectué ?

5. Entrer et exécuter l'instruction suivante :
```python
>>> doctest.testmod(verbose = True)
   Trying: 
     kelvin_vers_celsius(0) 
   Expecting: 
      -273.15 
   ok 
   Trying: 
      kelvin_vers_celsius(273.15) 
   Expecting: 
      0.0 
   ok 
```

{{% note normal %}}

La fonction `testmod` du module doctest a :

- lu la documentation de la fonction `kelvin_vers_celsius` à la recherche de lignes débutant par `>>>` ;
- exécuté les instructions de ces lignes ;
- vérifié que le résultat retourné correspond bien à ce qui est écrit dans cette documentation.

{{% /note %}}

6. Modifier maintenant, dans la définition de la fonction `kelvin_vers_celsius`, la valeur 0.0 par 1.0. Charger à nouveau le fichier dans l'interpréteur et relancer la commande du point 5. ci-dessus.\
Que retourne la fonction `testmod` maintenant ? Ce message décrit-il précisément le problème ?

{{% note tip %}}
La fonction testmod du module doctest analyse la valeur retournée par une fonction à partir d'exemples données dans sa **documentation**.
{{% /note %}}


### Comment rendre l'analyse de la valeur retournée par une fonction automatique ?


1. Effacer l'instruction `import doctest` de la ligne 1 du code.

2. Inclure, à la fin du fichier (**après la définition de toutes les fonctions**), le bloc d'instructions suivant :

```python
if __name__ == "__main__":

    import doctest 
    doctest.testmod()
```

3. Lancer à nouveau le programme.   
La fonction `testmod` est lancée automatiquement et retourne la même erreur qu'au point 6 de la section 2.1 ci-dessus.

4. Modifier maintenant, dans la documentation de la fonction `kelvin_vers_celsius`, la valeur 1.0 par 0.0.   
A-t-on la moindre indication que la fonction `testmod` a été lancée ?

### Que faire lorsqu'on souhaite prendre en compte la mauvaise utilisation d'une fonction ? 


1. Remplacer la définition de la fonction `kelvin_vers_celsius` par celle-ci :
```python
def kelvin_vers_celsius(t: float) -> float:

    """ Convertit la température donnée en kelvin en une
    température θ en degrés celsius. 
    Relation : θ = t - 273.15. 
    
    ERREUR si t est négative.
    
    >>> kelvin_vers_celsius(0) 
    -273.15
    >>> kelvin_vers_celsius(273.15) 
    0.0 
    """ 
    if t < 0: 
        raise ValueError("Température en kelvin doit être positive !")

    offset = -273.15 
    return t + offset
```
Quelle est la différence dans le comportement de la fonction ce code introduit-il ?

2. Pour l'instant la documentation de la fonction ne comporte aucun exemple illustrant ce à quoi il faut s'attendre si on appelle la fonction avec un nombre négatif.

    1. Charger le fichier dans l'interpréteur.

    2. Écrire et exécuter l'instruction
    ```python
    >>> kelvin_vers_celsius(-5)
    ```
    On obtient
    ```python
    Traceback (most recent call last):
    ...
    ValueError: Température en kelvin doit être positive !
    ``` 

    3. Ce sont ces lignes qu'il faut ajouter à la documentation de la fonction
    ```python
    >>> kelvin_vers_celsius(-5)

    Traceback (most recent call last): 
    ...
    ValueError: Température en kelvin doit être positive !
    ```
    Compléter la documentation de la fonction et la tester.


## À retenir

{{% note tip %}}

Pour chacune des fonctions, il faut
1. Incorporer à sa documentation des exemples pertinents d'utilisation de ces fonctions ;

2. Ajouter le bloc d'instruction suivant à la fin du fichier
```python
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

{{% /note %}}


## Exercices

{{% note exercise %}}
#### Exercice 1

Définir le prédicat `est_egal` dont une partie de la spécification est :
```python
def est_egal(a: float, b: float) -> bool:
    """
    Teste l'égalité de 2 floats a et b : abs(a - b) <= epsilon avec
    epsilon = 1e-7
    
    >>> est_egal(0, 0.0) 
    xxx 
    >>> est_egal(1/49*49, 1) 
    xxx 
    """
```
Remplacer les `xxx` de façon à ce que la fonction testmod accepte votre définition.
{{% /note %}}

{{% note exercise %}}

#### Exercice 2

Définir la fonction `inverse` dont une partie de la spécification est :
```python
def inverse(x: float) -> float:
    """ Retourne l'inverse du nombre x.
    ERREUR si x est nul.

    >>> inverse(0) 
    Traceback (most recent call last):
    …
    ZeroDivisionError: Division par 0 !!!
    >>> inverse(5) 
    xxx
    """
```
Remplacer les *xxx* de façon à ce que la fonction testmod accepte votre définition.
{{% /note %}}