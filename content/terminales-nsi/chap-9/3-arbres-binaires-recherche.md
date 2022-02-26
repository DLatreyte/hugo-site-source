---
title: "Arbres Binaires Recherche"
subtitle: "Chapitre 9,3"
author: ""
type: ""
date: 2020-11-10T05:04:12+04:00
draft: false
toc: true
tags: ["Arbres", "Arbres binaires", "Arbres binaires de recherche"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---


## Introduction

{{% note normal %}}

Quelle structure de données permet :
- d'organiser les données selon un ordre donné (numérique, lexicographique, etc.)&nbsp;;
- d'effectuer des recherches le plus efficacement possible&nbsp;;
- d'accéder à, d'insérer ou de supprimer les données le plus efficacement possible.

{{% /note %}}

#### Tableaux 

{{% solution "Propriétés" %}}

- On peut ordonner des données dans un tableau mais l'algorithme de tri le plus rapide est en $O(n \\; \log n)$&nbsp;;
- On peut accéder à une donnée en $O(1)$&nbsp;;
- On peut rechercher une valeur efficacement en utilisant la dichotomie : $O(\log n)$&nbsp;;
- Supprimer ou insérer une valeur n'est pas très efficace : $O(n)$.

{{% /solution %}}

#### Dictionnaires

{{% solution "Propriétés" %}}

- Accéder à, supprimer et insérer une valeur se fait très efficacement : $O(1)$&nbsp;;
- *Les données ne sont pas ordonnées*.

{{% /solution %}}


Remarque
: Dans la suite de ce document, on considérera que les valeurs des nœuds sont des entiers.


{{% note tip %}}
Un **arbre binaire de recherche**, ou **ABR**, est un arbre binaire avec la propriété suivante : quel que soit le nœud $x$, **tous les nœuds situés dans le sous-arbre gauche** de $x$ ont une **valeur inférieure à la valeur** du nœud $x$, et **tous ceux situés dans son sous-arbre droit** ont une **valeur supérieure à la valeur** du nœud $x$.

Remarque
: La définition précédente est **récursive**.
{{% /note %}}

{{% note normal %}}
Les ABR servent à maintenir un ensemble de valeurs ordonnées, avec une meilleure complexité qu’une liste chaînée par exemple. On commence par la recherche d’un élément. La structure de l’ABR permet d’éviter de le parcourir en entier.
{{% /note %}}

## Un ABR est un arbre

1. Pour représenter un ABR, on va à nouveau utiliser la classe `Noeud`. Écrire à nouveau le code de cette classe.  
**Les contraintes sur les valeurs des nœuds ne sont pas codées dans la classe**.

2. Écrire à nouveau les spécifications des fonctions `taille`, `hauteur` et `parcours_infixe`.

3. Vérifier que la fonction `parcours_infixe` affiche les valeurs dans l'ordre croissant.

{{% note warning %}}

Rappel
: *On peut voir le **parcours infixe** comme la *projection de l'arbre sur une droite*.*

{{% /note %}}

## Recherche dans un ABR

4. Écrire le code de la fonction `appartient` dont la spécification est 
```python
def appartient(a: Noeud, x: int) -> bool:
    """
    Détermine si la valeur x apparaît dans l'arbre a.
    """
```

5. Quelle est la complexité de cette recherche ?

## Ajout d'une valeur dans un ABR

6. Envisager un ABR et, à la main, ajouter un élément.

7. Quel peut-être le code de la fonction `ajoute` dont la spécification est 
```python
def ajoute(a: Noeud, x: int) -> None:
    """
    Ajoute x à l'arbre a (en place).

    HYPOTHÈSE : a n'est pas l'arbre vide.
    """
``` 

8. Quelle est la complexité de cette fonction ?

9. Pour résoudre le problème de l'ajout d'une valeur à un arbre initialement vide et/ou pour ne pas modifier un arbre déjà constitué, il est possible de programmer la fonction `ajoute_copie` dont la spécification est 
```python
def ajoute_copie(n: Noeud, x: int) -> Noeud:
    """
    Ajoute la valeur x à l'ABR n. Un nouvel arbre est créé.
    """
```
Écrire le code de cette fonction.

## Utiliser un arbre binaire de recherche

10. Créer la fonction `plus_petit_element` dont la spécification est 
```python
def plus_petit_element(a: Noeud) -> int:
    """
    Retourne le plus petit élément de l'arbre binaire de recherche a.

    Lève une exception si l'arbre est vide.
    """
```

11. Créer la fonction `plus_grand_element` dont la spécification est 
```python
def plus_grand_element(a: Noeud) -> int:
    """
    Retourne le plus grand élément de l'arbre binaire de recherche a.

    Lève une exception si l'arbre est vide.
    """
```

12. Créer la fonction `est_abr` dont la spécification est 
```python
def est_abr(a: Noeud) -> bool:
    """
    Détermine si l'arbre a est un arbre binaire de recherche.
    """
```


### Corrigé

{{< remote "Corrigé de l'activité" "https://repl.it/@dlatreyte/Arbre-binaire-de-recherche" >}}


## À retenir

{{% note tip %}}
Un **arbre binaire de recherche** est un arbre binaire contenant des **valeurs ordonnées**, tel que tout nœud contient une valeur plus grande (respectivement plus grande ou égale) que les valeurs de tous les nœuds situés dans son sous-arbre gauche. Cette organisation permet de procéder par **dichotomie**, en n'ayant à considérer qu'un seul sous-arbre pendant une opération.   
Lorsqu'ils sont **équilibrés**, les arbres binaires de recherche constituent une méthode très efficace pour stocker et rechercher de l'information.
{{% /note %}}