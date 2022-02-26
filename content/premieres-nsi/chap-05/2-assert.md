---
title: "Tester ses fonctions avec 'assert'"
subtitle: "Chapitre 5,1"
author: ""
type: ""
date: 2021-08-29T16:36:24+04:00
draft: false
toc: true
tags: ["Fonctions", "Python", "Jeux de tests", "assert"]
categories: ["Première Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: false
---


Dans le document 5,1, nous avons insisté sur l'importance de la spécification d'une fonction et sur celle d'un jeu de tests.\
Dans ce document, nous allons découvrir une nouvelle façon de tester ses fonctions.

## Le mot clé `assert`

{{% note tip %}}

Le mot clé `assert` est utilisé afin de s'assurer de la robustesse d'une fonction. *Il ne doit jamais être utilisé au sein d'un programme pour lever une exception* ; il ne faut donc pas le confondre avec le mot clé `raise`.\
Placé dans la zone de test du programme, 
```python
if __name__ == "__main__":
``` 
il permet 

1. de tester une expression booléenne&nbsp;; 
2. de lever une exception si la valeur de l'expression booléenne est `False` (**en clair le programme s'interrompt**)&nbsp;;
3. d'afficher éventuellement un message dans la **pile d'exécution** du programme, dans la console.

{{% /note %}}

## Syntaxe d'une assertion

{{% note normal %}}

La syntaxe d'utilisation du mot clé `assert` est la suivante&nbsp;:
```python
assert <expression booléenne>, <message si valeur Faux>
```

{{% /note %}}

{{% note normal %}}

`assert` est un mot-clé ! On n'utilise pas de parenthèses avec les mot-clés, seulement avec les fonctions.

{{% /note %}}

## Reprise de l'exemple du document précédent 

Écrire le code que doit contenir le fichier dans lequel on a défini la fonction dont la spécification est&nbsp;:

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

{{% solution "Réponse" %}}

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

if __name__ == "__main__":
    assert kelvin_vers_celsius(0) == -273.15, "Pb avec fonction kelvin_vers_celsius"
    assert kelvin_vers_celsius(273.15) == 0.0, "Pb avec fonction kelvin_vers_celsius"
```

{{% /solution %}}