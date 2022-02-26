---
title: "Parcours en profondeur : écriture du code en Python"
subtitle: "Chapitre 15,4"
author: ""
type: ""
date: 2021-05-06T06:46:05+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Écriture d'une classe `Graphe`

L'objectif de cette partie est l'écriture du code modélisant un graphe orienté. La représentation choisie est celle d'un dictionnaire de successeurs ([en cours]({{< ref "1-graphes-structure-de-donnees" >}}) et dans le [document 15,2]({{< ref "2-representation-graphe" >}}) on a étudié les représentations par des matrice et liste de successeurs).\
La représentation par un dictionnaire de successeurs présente de nombreux avantages. Par exemple,
- les sommets peuvent être des entiers ou des chaînes de caractères quelconques ;
- La complexité de la liste des successeurs est directement proportionnelle au nombre de successeurs pour un sommet donné. L'occupation mémoire est donc faible si les sommets possèdent peu de successeurs.\
**Remarque :** dans le cas d'une matrice d'adjacence, la taille est fixe et comporte $N^2$ éléments si le nombre de sommets est égal à $N$.

#### Remarque
Contrairement à ce qui a été fait dans le [document 15,2]({{< ref "2-representation-graphe" >}}), la classe qui va être implémentée ici permettra d'initialiser un graphe vide, puis de le constituer progressivement.

1. Initialiser la classe `Graphe`. La méthode `__init__` a pour seule fonction l'affectation d'un dictionnaire vide à l'attribut `succ`.
{{% solution "Solution" %}}
```python
from __future__ import annotations
from typing import List, Union

class Graphe:

    def __init__(self: Graphe) -> None:
        self.succ = {}
```
{{% /solution %}}

2. Créer la méthode `ajouter_sommet` dont la spécification est :
```python 
def ajouter_sommet(self: Graphe, s: Union[int, str]) -> None:
    """
    Ajoute le sommet s (entier ou chaîne de caractères) au graphe
    s'il n'est pas déjà présent.
    s est une clé du dictionnaire succ. Sa valeur associée par défaut 
    est une liste vide.
    """
```
{{% solution "Solution" %}}
```python
def ajouter_sommet(self: Graphe, s: Union[int, str]) -> None:
    """
    Ajoute le sommet s (entier ou chaîne de caractères) au graphe
    s'il n'est pas déjà présent.
    s est une clé du dictionnaire succ. Sa valeur associée par défaut 
    est une liste vide.
    """
    if s not in self.succ.keys():
        self.succ[s] = []
```
{{% /solution %}}

3. Créer la méthode `ajouter_arc` dont la spécification est :
```python
def ajouter_arc(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> None:
    """
    Ajoute s2 à la liste des successeurs de s1. Si s1 et s2 n'existent pas, ils sont
    créés en utilisant la méthode ajouter_sommet.
    """
```
{{% solution "Solution" %}}
```python
def ajouter_arc(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> None:
    """
    Ajoute s2 à la liste des successeurs de s1. Si s1 et s2 n'existent pas, ils sont
    créés en utilisant la méthode ajouter_sommet.
    """
    self.ajouter_sommet(self, s1)
    self.ajouter_sommet(self, s2)
    if s2 not in self.succ[s1]:
        self.succ[s1].append(s2)
```
{{% /solution %}}

4. Créer la méthode `existe_arc` dont la spécification est :
```python
def existe_arc(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> bool:
    """
    Retourne True si l'arc s1 -> s2 existe.
    """
``` 
{{% solution "Solution" %}}
```python
def existe_arc(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> bool:
    """
    Retourne True si l'arc s1 -> s2 existe.
    """
    return s2 in self.succ[s1]
``` 
{{% /solution %}}

5. Créer la méthode `liste_sommets` dont la spécification est :
```python
def liste_sommets(self: Graphe) -> List[Union[int, str]]:
    """
    Retourne la liste des sommets du graphe.
    """
``` 
{{% solution "Solution" %}}
```python
def liste_sommets(self: Graphe) -> List[Union[int, str]]:
    """
    Retourne la liste des sommets du graphe.
    """
    return list(self.succ.keys())
``` 
{{% /solution %}}

6. Créer la méthode `nbre_sommets` dont la spécification est :
```python
def nbre_sommets(self: Graphe) -> int:
    """
    Retourne le nombre de sommets du graphe.
    Utilise la méthode liste_sommets.
    """
```
{{% solution "Solution" %}}
```python
def nbre_sommets(self: Graphe) -> int:
    """
    Retourne le nombre de sommets du graphe.
    Utilise la méthode liste_sommets.
    """
    return len(self.liste_sommets())
```
{{% /solution %}}

7. Créer la méthode `liste_successeurs` dont la spécification est :
```python
def liste_successeurs(self: Graphe, s: Union[int, str]) -> List[Union[int, str]]:
    """
    Retourne la liste des successeurs du sommet s1.
    """
``` 
{{% solution "Solution" %}}
```python
def liste_successeurs(self: Graphe, s: Union[int, str]) -> List[Union[int, str]]:
    """
    Retourne la liste des successeurs du sommet s1.
    """
    return self.succ[s1]
``` 
{{% /solution %}}

8. Dans la partie principale du programme, entrer les instructions qui permettent de coder le graphe suivant :
{{< mermaid >}}
graph TD
    A(0) --> B(1)
    B --> C(2)
    A --> D(3)
    D --> B
{{< /mermaid >}}

{{% solution "Solution" %}}
```python
g = Graphe()
g.ajouter_arc(0,1)
g.ajouter_arc(0,3)
g.ajouter_arc(1,2)
g.ajouter_arc(3,1)
``` 
{{% /solution %}}

## Parcours en profondeur basé sur la récursivité

9. Reprendre la fonction `parcours_profondeur` proposée dans le [document 15,3]({{< ref "3-parcours-graphes" >}}) et la transformer en méthode de la classe `Graphe`. Sa nouvelle spécification est alors :
```python
def parcours_profondeur(self: Graphe, vus: List[Union[int, str]], s: Union[int, str]) -> None:
    """
    Parcours en profondeur depuis le sommet s.
    Cette méthode prend en argument la liste des sommets déjà visités. Lors du premier appel
    cette liste doit être vide.
    Le parcours est accessible par lecture de la liste vus.
    """
```

Remarque.
: Attention, j'ai modifié le nom d'une méthode : `voisins` s'appelle désormais `liste_successeurs`.

{{% solution "Solution" %}}
```python
def parcours_profondeur(self: Graphe, vus: List[Union[int, str]], s: Union[int, str]) -> None:
    """
    Parcours en profondeur depuis le sommet s.
    Cette méthode prend en argument la liste des sommets déjà visités. Lors du premier appel
    cette liste doit être vide.
    Le parcours est accessible par lecture de la liste vus.
    """
    if s not in vus:
        vus.append(s)
        for v in self.liste_successeurs(s):
            parcours_profondeur(self, vus, v)
```
{{% /solution %}}

10. Créer la méthode `existe_chemin` dont la spécification est :
```python
def existe_chemin(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> bool:
    """
    Retourne True s'il existe un chemin depuis s1 jusqu'à s2.
    """
``` 
{{% solution "Solution" %}}
```python
def existe_chemin(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> bool:
    """
    Retourne True s'il existe un chemin depuis s1 jusqu'à s2.
    """
    vus = []
    self.parcours_profondeur(self, vus, s1)
    return s2 in vus
``` 
{{% /solution %}}

11. Vérifier le code précédent en utilisant le graphe proposé à la question 8.

Comment construire le chemin entre `s1` et `s2` ?\
- Remplacer, dans la méthode `parcours_profondeur` la liste `vus` par un dictionnaire dont les clés sont les sommets visités et les valeurs associées sont les sommets prédécesseurs.
Attribuer la valeur `None` au sommet de départ.
- Une fois le parcours en profondeur achevé, on peut vérifier qu'il existe un chemin en vérifiant si les deux sommets sont dans la liste des valeurs du dictionnaire.
- Une fois le parcours en profondeur achevé, on peut donner le parcours en remontant le dictionnaire depuis le sommet d'arrivée.

12. Modifier le code des méthodes `parcours_profondeur` et `existe_chemin` à partir des consignes ci-dessus.

13. Créer la méthode `chemin_entre` dont la spécification est :
```python
def chemin_entre(self: Graphe, s1: Union[int, str], s2: Union[int, str]) -> List[Union[int, str]]:
    """
    Vérifie que le chemin entre s1 et s2 existe puis le retourne sous la forme d'une liste.
    """
```

## Parcours en profondeur basé sur la structure pile

13. Écrire le code de la classe `Pile`. En plus de la méthode `__init__` cette classe doit posséder les méthodes `est_vide`, `empiler` et `depiler`.

14. Adapter le code de la fonction proposée dans le document [document 15,3]({{< ref "3-parcours-graphes" >}}) afin de la transformer en méthode de la classe `Graphe`.
