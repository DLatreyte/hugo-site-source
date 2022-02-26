---
title: "Fourniture et utilisation d'une API"
subtitle: "Chapitre 2,4"
author: ""
type: ""
date: 2020-09-22T05:15:58+04:00
draft: false
toc: true
tags: ["Modules", "API", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## API

Une API (en anglais « Application programming interface ») est une interface de programmation d'application. Elle est destinée à être utilisée par des programmes. Le principe de ce type d'interface est le même que celui des UI (« User Interface ») ou des GUI (« Graphical User Interface ») destinées elles à un utilisateur humain.

Composée de *constantes*, de *fonctions*, de *classes*, elle sert de *lien entre un programme et les programmes qui vont l'utiliser*. Elle peut être proposée par un service web avec une documentation décrivant l'utilisation qui permettra la communication et l'échange des données. Il existe, par exemple, plusieurs API de géolocalisation qui peuvent être intégrées à des programmes. Une API est très souvent proposée par une bibliothèque logicielle composée de fonctions destinées à être utilisées dans divers programmes.

Le principe de base est que le *fonctionnement interne n'a pas besoin d'être connu du programme utilisateur.* Cela nécessite une *documentation fournie décrivant précisément son l'utilisation*. Ainsi, lors de l'élaboration d'un logiciel il est possible d'utiliser des parties d'autres logiciels, sans connaître leur fonctionnement interne, si l'on sait comment faire interagir ces différentes parties.  
Par exemple, pour utiliser une fonction il suffit de connaître sa **spécification**, c'est à dire son **nom**, les **types de ses paramètres et de la valeur qu'elle retourne** et sa **documentation**. Dans tous les cas, l'utilisateur, un programme ou un humain, se contente de fournir les données demandées et obtient le résultat du traitement.

## Travail à réaliser

1. Créer un module dont l'API est la suivante :
```python
>>> help(aires)
Help on module aires:

NAME
    aires

DESCRIPTION
    Fourniture de fonctions calculant les surfaces
    de diverses figures géométriques.

FUNCTIONS
    disque(rayon: float) -> float
        Renvoie l'aire du disque de rayon r.
    
    rectangle(largeur: float, longueur: float) -> float
        Renvoie l'aire d'un rectangle de côtés largeur 
        et longueur.
    
    triangle(base: float, hauteur: float) -> float
        renvoie l'aire d'un triangle de base base et de 
        hauteur hauteur.

DATA
    pi = 3.14159

FILE
    /home/runner/aires/aires.py
```

2. Créer, de la façon qui semblera la plus pertinente, un jeu de tests des fonctions, dans ce module.

3. Écrire un programme principal qui utilise ce module.

4. Expliquer quelle est la différence entre les deux spécifications suivantes :
```python
def disque(rayon: float) -> float:
    """
    Renvoie l'aire du disque de rayon r.
    """
```
et 
```python
def disque(rayon: float) -> float:
    """
    Renvoie l'aire du disque de rayon r.

    HYPOTHÈSE: r > 0
    """
````
5. On souhaite prendre en charge les cas où l'utilisateur fournirait une dimension négative (erronée donc).  
Modifier le code des fonctions de telle sorte qu'une exception de type `ValueError` soit levée chaque fois qu'une valeur négative est passée en argument.

**Remarque :** on pourra se renseigner sur l'utilisation du mot-clé `raise`.

## Stabilité d'une API

Il est important, lorsqu'on souhaite faire évoluer une API, de faire en sorte que les utilisateurs qui l'utilisaient déjà, avant la modification, puisse toujours le faire sans avoir à modifier le programme ou voir celui-ci ne plus fonctionner.   
*Sauf décision volontaire qu'**il faudra communiquer aux utilisateurs**, l'évolution d'une API doit apporter de nouvelles fonctionnalités sans en retirer.*

Par exemple, on pourrait vouloir proposer aux utilisateurs la possibilité d'arrondir le résultat du calcul d'une aire. 

6. Modifier le code des différentes fonctions de façon à ce qu'il ressemble à celui de la fonction `disque` ci-dessous (la partie sur la levée de l'exception `ValueError` n'est pas insérée dans le code proposé).   
Vérifier que le programme écrit à la question 3. fonctionne toujours sans aucune modification. 
```python
def disque(rayon: float, dec: int = -1) -> float:
    """
    Renvoie l'aire du disque de rayon r.
    """
    aire = pi * rayon * rayon
    if dec >= 0:
        aire = round(aire, dec)
    return aire
```

7. En déduire comment se comportent, en Python, les paramètres d'une fonction auxquels on attribue des valeurs dans la signature.

8. Dans le programme principal modifier l'appel à la fonction `disque` de telle sorte que le résultat de son calcul soit arrondi à deux chiffres après la virgule.

9. Le code utilise la fonction intégrée au langage Python `round` pour arrondir un `float` à un certain nombre de chiffres après la virgule.  
Écrire sa propre fonction `round` en n'utilisant que les opérateurs `*`, `/`, `+`, `**` et la fonction `int`.

