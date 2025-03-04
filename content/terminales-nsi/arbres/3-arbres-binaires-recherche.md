---
title: "Arbres Binaires Recherche"
subtitle: ""
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

- On peut ordonner des données dans un tableau mais l'algorithme de tri le plus rapide, pour un jeu de données aléatoires, est en $O(n \\; \log n)$ ;
- On peut accéder à une donnée en $O(1)$&nbsp;;
- On peut rechercher une valeur efficacement en utilisant la dichotomie (si le tableau est trié !) : $O(\log n)$&nbsp;;
- Supprimer ou insérer une valeur n'est pas très efficace : $O(n)$ (sauf à la fin du tableau).

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

1. Cet arbre binaire est-il un arbre binaire de recherche ?
{{% mermaid %}}
graph TD
    A(3) --- B(1)
    B --- C(None)
    B --- D(2)
    D --- E(None)
    D --- F(None)
    A --- G(4)
    G --- H(None)
    G --- I(None)
{{% /mermaid %}}
{{% solution "Réponse" %}}

oui

{{% /solution %}}

2. Cet arbre binaire est-il un arbre binaire de recherche ?
{{% mermaid %}}
graph TD
    A(3) --- B(2)
    B --- C(1)
    C --- D(None)
    C --- E(None)
    B --- F(None)
    A --- G(4)
    G --- H(None)
    G --- I(None)
{{% /mermaid %}}
{{% solution "Réponse" %}}

oui

{{% /solution %}}

3. Cet arbre binaire est-il un arbre binaire de recherche ?
{{% mermaid %}}
graph TD
   A(3) --- B(2)
    B --- C(None)
    B --- D(1)
    D --- E(None)
    D --- F(None)
    A --- G(4)
    G --- H(None)
    G --- I(None)
{{% /mermaid %}}

{{% solution "Réponse" %}}

Non ! La propriété est bien vérifiée pour la racine mais pas pour le sous-arbre gauche.  
La définition est récursive !

{{% /solution %}}

{{% note normal %}}
Les ABR servent à maintenir un ensemble de valeurs ordonnées, avec une meilleure complexité qu’une liste chaînée par exemple. On commence par la recherche d’un élément. La structure de l’ABR permet d’éviter de le parcourir en entier.
{{% /note %}}

## Un ABR est un arbre binaire

{{% note warning %}}

Le paradigme de programmation utilisé ci-dessous est le paradigme impératif : on crée dans un premier temps une structure élémentaire à l'aide d'une classe et on définit ensuite des fonctions qui manipulent cette structure.  
On ne crée pas de structure arbre binaire (accompagnée de méthodes).

{{% /note %}}

4. Pour représenter un ABR, on va à nouveau utiliser la classe `Noeud`. Écrire à nouveau le code de cette classe.  
**Les contraintes sur les valeurs des nœuds ne sont pas codées dans la classe**.

5. À quel arbre binaire de recherche ce code correspond-il ?  

```shell
# Création d'un arbre binaire de recherche
arbre = Noeud(10)
arbre.gauche = Noeud(5)
arbre.droit = Noeud(15)
arbre.gauche.gauche = Noeud(3)
arbre.gauche.droit = Noeud(8)
arbre.droit.gauche = Noeud(12)
arbre.droit.droit = Noeud(18)
```

{{% solution "Réponse" %}}
{{% mermaid %}}
graph TD
    A(10) --- B(5)
    A --- C(15)
    B --- D(3)
    B --- E(8)
    C --- F(12)
    C --- I(18)
{{% /mermaid %}}
{{% /solution %}}

5. Écrire à nouveau les spécifications des fonctions `taille`, `hauteur` et `parcours` (parcours infixe).

```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si le noeud passé en argument est vide ou pas.
    """
```

{{% solution "Réponse" %}}

```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si un arbre est vide.
    """
    return n == None
```

{{% /solution %}}

```python
def hauteur(a: Noeud) -> int:
    """
    Retourne la hauteur de l'arbre binaire de recherche a. 
    """
```

{{% solution "Réponse" %}}

```python
def hauteur(n: Noeud) -> int:
    """
    Retourne la profondeur de l'arbre. 
    """
    if est_vide(n):
        # Cas de base : si le nœud est vide, il n'est pas dans l'arbre.
        return -1
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        arbre_gauche = hauteur(n.gauche)
        arbre_droit = hauteur(n.droit)

        # Détermine la profondeur
        return 1 + max(arbre_gauche, arbre_droit)
```

{{% /solution %}}

```python
def taille(a: Noeud) -> int:
    """
    Retourne le nombre de noeuds dans l'arbre binaire de recherche.
    """
```

{{% solution "Réponse" %}}

```python
def taille(n: Noeud) -> int:
    """
    Retourne le nombre de noeud dans l'arbre.
    """
    if est_vide(n):
        # Cas de base : un arbre vide ne contient aucun noeud.
        return 0
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        taille_gauche = taille(n.gauche)
        taille_droit = taille(n.droit)

        # Calcul de la taille
        return 1 + taille_gauche + taille_droit
```

{{% /solution %}}

```python
def parcours(n: Noeud) -> None:
    """
    Parcours infixe de l'arbre
    """
```

{{% solution "Réponse" %}}

```python
def parcours_inf(n: Noeud) -> str:
    """ Parcours en profondeur infixe d'un arbre binaire. """
    if est_vide(n):
        # Cas de base : On atteint un noeud vide
        return ""
    else:
        # Appel récursif à gauche, valeur du nœud, appel récursif à droite
        chaine = parcours_inf(n.gauche)
        chaine += str(n.valeur)
        chaine += parcours_inf(n.droit)
        return chaine
```

{{% /solution %}}

6. Vérifier que la fonction `parcours` affiche les valeurs dans l'ordre croissant.

{{% note warning %}}

Rappel
: *On peut voir le **parcours infixe** comme la **projection de l'arbre sur une droite**.*

{{% /note %}}

## Recherche dans un ABR

7. Écrire le code de la fonction `appartient` dont la spécification est

```python
def appartient(a: Noeud, x: int) -> bool:
    """
    Détermine si la valeur x apparaît dans l'arbre a.
    """
```

{{% solution "Réponse" %}}

```python
def appartient(a: Noeud, x: int) -> bool:
    """
    Détermine si la valeur x apparaît dans l'abr a.
    """
    if est_vide(a):
        # Cas de base : on parvient à un noeud vide,
        # la valeur n'est pas présente
        return False
    elif a.valeur == x:
        # Cas de base : on parvient au noeud recherché
        return True
    # Appels récursifs
    elif a.valeur > x:
        return appartient(a.gauche, x)
    else:
        return appartient(a.droit, x)
```

{{% /solution %}}

8. Quelle est la complexité de cette recherche ?

{{% solution "Réponse" %}}

La complexité du pire cas de la fonction `appartient` dépend de la hauteur de l'arbre binaire de recherche (ABR).

- Dans le pire des cas, l'arbre peut être déséquilibré au point de ressembler à une liste chaînée. Dans un tel scénario, la complexité de la recherche est **linéaire** par rapport au nombre total de nœuds dans l'arbre.  
Complexité : $O(n)$.
- Si on écarte ce cas extrême, l'arbre binaire de recherche (ABR) est plus ou moins équilibré et la hauteur est de l'ordre du logrithme du nombre de nœuds.  
Complexité : $O(\log n)$.

{{% /solution %}}

## Ajout d'une valeur dans un ABR

9. Envisager un ABR et, à la main, ajouter un élément.

10. Quel peut-être le code de la fonction `ajoute` dont la spécification est

```python
def ajoute(a: Noeud, x: int) -> None:
    """
    Ajoute x à l'arbre a (en place).

    HYPOTHÈSE : a n'est pas l'arbre vide.
    """
```

11. Quelle est la complexité de cette fonction ?

12. Pour résoudre le problème de l'ajout d'une valeur à un arbre initialement vide et/ou pour ne pas modifier un arbre déjà constitué, il est possible de programmer la fonction `ajoute_copie` dont la spécification est

```python
def ajoute_copie(n: Noeud, x: int) -> Noeud:
    """
    Ajoute la valeur x à l'ABR n. Un nouvel arbre est créé.
    """
```

Écrire le code de cette fonction.

## Utilisation d'un arbre binaire de recherche

13. Créer la fonction `plus_petit_element` dont la spécification est

```python
def plus_petit_element(a: Noeud) -> int:
    """
    Retourne le plus petit élément de l'arbre binaire de recherche a.

    Lève une exception si l'arbre est vide.
    """
```

14. Créer la fonction `plus_grand_element` dont la spécification est

```python
def plus_grand_element(a: Noeud) -> int:
    """
    Retourne le plus grand élément de l'arbre binaire de recherche a.

    Lève une exception si l'arbre est vide.
    """
```

15. Créer la fonction `est_abr` dont la spécification est

```python
def est_abr(a: Noeud) -> bool:
    """
    Détermine si l'arbre a est un arbre binaire de recherche.
    """
```

## Corrigé

{{< remote "Corrigé de l'activité" "<https://repl.it/@dlatreyte/Arbre-binaire-de-recherche>" >}}

## À retenir

{{% note tip %}}
Un **arbre binaire de recherche** est un arbre binaire contenant des **valeurs ordonnées**, tel que tout nœud contient une valeur plus grande (respectivement plus grande ou égale) que les valeurs de tous les nœuds situés dans son sous-arbre gauche. Cette organisation permet de procéder par **dichotomie**, en n'ayant à considérer qu'un seul sous-arbre pendant une opération.
Lorsqu'ils sont **équilibrés**, les arbres binaires de recherche constituent une méthode très efficace pour stocker et rechercher de l'information.
{{% /note %}}
