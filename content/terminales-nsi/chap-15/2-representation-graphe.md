---
title: "Représentation d'un graphe en informatique"
subtitle: "Chapitre 15,2"
author: ""
type: ""
date: 2021-04-22T04:48:57+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

> Plusieurs modes de représentation peuvent être implémentés pour stocker des graphes : *matrices d’adjacence (ou sommet-sommet), listes des voisins, des successeurs ou des prédécesseurs*. Lors de cette séance nous allons écrire les classes réalisant ces implémentations.

## Matrice sommet-sommet

1. Écrire le code de la classe `GrapheM` qui implémente une matrice sommet-sommet.\
La spécification du constructeur de la classe est :
```python
def __init__(self: GrapheM, mat: List[List[int]]) -> None:
        """
        Constructeur de la classe.
        """
```

{{% solution "Solution" %}}
```python
class GrapheM:
    """
    Implémentation de la représentation
    matricielle d'un graphe.
    """
    def __init__(self: GrapheM, mat: List[List[int]]) -> None:
        """
        Constructeur de la classe.
        """
        self.mat = mat
```
{{% /solution %}}

2. Ajouter à la classe `GrapheM` une redéfinition de la méthode spéciale `__str__` de façon à ce qu'un appel à la fonction `print` avec comme argument un objet représentant un graphe donne un affichage qui rappelle celui d'une matrice (lignes et colonnes).

{{% solution "Solution" %}}
```python
def __str__(self: GrapheM) -> str:
    rep = ""
    for i in range(len(self.mat)):
        rep = rep + str(self.mat[i][0])  # Premier élement de la ligne
        for j in range(1, len(self.mat[0])):
            rep = rep + " " + str(self.mat[i][j])
        rep = rep + "\n"
    return rep
```
{{% /solution %}}

3. Écrire le code d'une fonction `main` qui permet de tester l'implémentation de la classe et la représentation du graphe à l'écran.\
Choisir comme matrices tests
$$
    M_1 = 
    \begin{pmatrix}
        1 & 1 & 0 \cr
        0 & 1 & 1 \cr
        0 & 0 & 1 \cr
    \end{pmatrix}
    \text{  et  }
    M_2 = 
    \begin{pmatrix}
        0 & 1 & 1 & 0 \cr
        1 & 0 & 1 & 1 \cr
        1 & 1 & 0 & 1 \cr
        0 & 1 & 1 & 0 \cr
    \end{pmatrix}
$$
Remarque
: Les sommets du graphe sont représentés par des entiers naturels.

{{% solution "Solution" %}}
```python
def main():
    """ Fonction principale """
    mat1 = [[1, 1, 0], [0, 1, 1], [0, 0, 1]]
    mat2 = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]

    graph11 = GrapheM(mat1)
    graph21 = GrapheM(mat2)

    print(graph11)
    print(graph21)

main()
```
{{% /solution %}}

4. Représenter les deux graphes sur une feuille.

5. Écrire le code de la méthode `nbre_sommets` qui détermine le nombre de sommets du graphe.\
Jeu de tests :
```python
assert graph11.nbre_sommets() == 3
assert graph21.nbre_sommets() == 4
``` 

{{% solution "Solution" %}}
Une matrice sommet-sommet est carrée ; le nombre de lignes est donc égal au nombre de colonnes.
```python
def nbre_sommets(self: GrapheM) -> int:
    """
    Retourne le nombre de sommets du graphe
    """
    return len(self.mat)
``` 
{{% /solution %}}

6. Écrire le code de la fonction `est_lie` dont la spécification est :
```python
def est_lie(self: GrapheM, i: int, j: int) -> bool:
    """
    Retourne True s'il existe une relation (arête ou arc) entre les sommets i et j, False sinon.
    """
```
Jeu de tests possible :
```python
assert graph11.est_lie(1, 1) == True
assert graph11.est_lie(0, 1) == True
assert graph11.est_lie(2, 0) == False
```

{{% solution "Solution" %}}
```python
def est_lie(self: GrapheM, i: int, j: int) -> bool:
    """
    Retourne True s'il existe une relation (arête ou arc) entre les sommets i et j, False sinon.
    """
    return self.mat[i][j] == 1
```
{{% /solution %}}

7. Quelle est la particularité de la matrice sommet-sommet d'un graphe non orienté ?

{{% solution "Solution" %}}
{{% /solution %}}

8. Écrire le code de la fonction `est_non_oriente` dont la spécification est 
```python
def est_non_oriente(self: GrapheM) -> bool:
    """
    Retourne True si le graphe est non orienté (si la matrice est symétrique) et False si le graphe est orienté.
    """
``` 
Jeu de tests :
```python
assert graph11.est_non_oriente() == False
assert graph21.est_non_oriente() == True
``` 

{{% solution "Solution" %}}
```python
def est_non_oriente(self: GrapheM) -> bool:
    """
    Retourne True si le graphe est non orienté (si la matrice est symétrique) et False si le graphe est orienté.
    """
    for i in range(len(self.mat)):
        for j in range(len(self.mat[i])):
            if self.mat[i][j] != self.mat[j][i]:
                return False
    return True
```
{{% /solution %}}

## Liste d'adjacence

Dans cette partie, on implémente la liste d'adjacence (liste des voisins) d'un graphe non orienté ou la liste des successeurs d'un graphe orienté.

9. Écrire le code de la classe `GrapheL` qui implémente une liste des voisins.\
La spécification du constructeur de la classe est :
```python
def __init__(self: GrapheM, lst: List[List[int]]) -> None:
        """
        Constructeur de la classe.
        """
```

{{% solution "Solution" %}}
```python
class GrapheL:
    """
    Implémentation de la liste des voisins d'un graphe non orienté.
    """
    def __init__(self, lst: List[List[int]]) -> None:
        self.lst = lst
```
{{% /solution %}}

10. Ajouter à la classe `GrapheL` une redéfinition de la méthode spéciale `__str__` de façon à ce qu'un appel à la fonction `print` avec comme argument un objet représentant un graphe donne un affichage qui rappelle celui d'une liste de listes.

{{% solution "Solution" %}}
```python
def __str__(self: GrapheLV) -> str:
    """
    Représentation sous forme d'une chaîne de caractères de l'objet.
    """
    rep = ""

    for i in range(len(self.lst)):
        rep += "{} :".format(i)
        for j in range(len(self.lst[i])):
            rep += " " + str((self.lst[i][j]))
        rep += "\n"

    return rep
```
{{% /solution %}}

11. Tester le code précédent à l'aide des listes des voisins/successeurs des graphes dont les matrices sommet-sommet sont données dans la première section.

{{% solution "Solution" %}}
```python
lst1 = [[0, 1], [1, 2], [2]]
lst2 = [[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]]

graph12 = GrapheL(lst1)
graph22 = GrapheL(lst2)

print(graph12)
print(graph22)
```
{{% /solution %}}

12. Écrire le code de la méthode `nbre_sommets` qui détermine le nombre de sommets du graphe.\
Jeu de tests :
```python
assert graph12.nbre_sommets() == 3
assert graph22.nbre_sommets() == 4
``` 

{{% solution "Solution" %}}
```python
def nbre_sommets(self: GrapheL) -> int:
    """
    Retourne le nombre de sommets du graphe.
    """
    return len(self.lst)
``` 
{{% /solution %}}

13. Écrire le code de la fonction `est_lie` dont la spécification est :
```python
def est_lie(self: GrapheL, i: int, j: int) -> bool:
    """
    Retourne True s'il existe une relation (arête ou arc) entre les sommets i et j, False sinon.
    """
```
Jeu de tests possible :
```python
assert graph12.est_lie(1, 1) == True
assert graph12.est_lie(0, 1) == True
assert graph12.est_lie(2, 0) == False
```

{{% solution "Solution" %}}
```python
def est_lie(self: GrapheL, i: int, j: int) -> bool:
    """
    Retourne True s'il existe une relation (arête ou arc) entre les sommets i et j, False sinon.
    """
    return j in self.lst[i]
```
{{% /solution %}}

14. Écrire le code de la fonction `est_non_oriente` dont la spécification est 
```python
def est_non_oriente(self: GrapheL) -> bool:
    """
    Retourne True si le graphe est non orienté, False sinon.
    """
``` 
Jeu de tests :
```python
assert graph12.est_non_oriente() == False
assert graph22.est_non_oriente() == True
``` 

{{% solution "Solution" %}}
```python
def est_non_oriente(self: GrapheL) -> bool:
    """
    Retourne True si le graphe est non orienté (si la matrice est symétrique) et False si le graphe est orienté.
    """
    for i in range(len(self.lst)):
        for j in range(len(self.lst[i])):
            s = self.lst[i][j]  # sommet
            if i not in self.lst[s]:
                return False
    return True
```
{{% /solution %}}

## Passage d'une représentation à l'autre

15. Ajouter à la classe `GrapheL` la méthode `lst_to_mat` dont la spécification est :
```python
def lst_to_mat(self: GrapheL) -> GrapheM:
    """
    Génère la matrice sommet-sommet à partir de la liste des voisins/successeurs.
    """
``` 

Tests :
```python
graph13 = graph12.lst_to_mat()
print(graph13)
graph23 = graph22.lst_to_mat()
print(graph23)
```

{{% solution "Solution" %}}
```python
def lst_to_mat(self: GrapheL) -> GrapheM:
    """
    Génère la matrice sommet-sommet à partir de la liste des voisins/successeurs.
    """
    liste = []  # liste des relations pour tous les sommets
    for i in range(len(self.lst)):
        rel = []  # relations pour un sommet donné
        for j in range(len(self.lst)):
            if j in self.lst[i]:
                rel.append(1)
            else:
                rel.append(0)
        liste.append(rel)
    return GrapheM(liste)
```
{{% /solution %}}

16. Ajouter à la classe `GrapheM` la méthode `mat_to_lst` dont la spécification est :
```python
def mat_to_lst(self) -> GrapheL:
    """
    Génère la liste des voisins/successeurs à partir de la matrice sommet-sommet.
    """
```

Tests :
```python
graph14 = graph11.mat_to_lst()
print(graph14)
graph24 = graph21.mat_to_lst()
print(graph24)
```

{{% solution "Solution" %}}
```python
def mat_to_lst(self) -> GrapheL:
    """
    Génère la liste des voisins/successeurs à partir de la matrice sommet-sommet.
    """
    liste = []  # liste des listes pour tous les sommets
    for i in range(len(self.mat)):
        rel = []  # relation pour le sommet i
        for j in range(len(self.mat)):
            if self.mat[i][j] != 0:
                rel.append(j)
        liste.append(rel) 
    return GrapheL(liste)
```
{{% /solution %}}


## Code complet

{{< remote "Code complet en ligne" "https://replit.com/join/yugulkal-dlatreyte" >}}
