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
La définition est récurisve !

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

5. Écrire à nouveau les spécifications des fonctions `taille`, `hauteur` et `parcours` (parcours infixe).

```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si le noeud passé en argument est vide ou pas.
    """
```

```python
def hauteur(a: Noeud) -> int:
    """
    Retourne la hauteur de l'arbre binaire de recherche a. 
    """
```

```python
def taille(a: Noeud) -> int:
    """
    Retourne le nombre de noeuds dans l'arbre binaire de recherche.
    """
```

```python
def parcours(n: Noeud) -> None:
    """
    Parcours infixe de l'arbre
    """
```

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

8. Quelle est la complexité de cette recherche ?

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

{{< remote "Corrigé de l'activité" "https://repl.it/@dlatreyte/Arbre-binaire-de-recherche" >}}

## À retenir

{{% note tip %}}
Un **arbre binaire de recherche** est un arbre binaire contenant des **valeurs ordonnées**, tel que tout nœud contient une valeur plus grande (respectivement plus grande ou égale) que les valeurs de tous les nœuds situés dans son sous-arbre gauche. Cette organisation permet de procéder par **dichotomie**, en n'ayant à considérer qu'un seul sous-arbre pendant une opération.
Lorsqu'ils sont **équilibrés**, les arbres binaires de recherche constituent une méthode très efficace pour stocker et rechercher de l'information.
{{% /note %}}
