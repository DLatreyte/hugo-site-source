---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2022-01-16T23:13:15+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Dans cet exercice, un arbre binaire de caractères est stocké sous la forme d’un dictionnaire où les clefs sont les caractères des nœuds de l’arbre et les valeurs, pour chaque clef, la liste des caractères des fils gauche et droit du nœud.

Par exemple, l’arbre

{{<mermaid>}}
graph TD
    F((F)) --> B((B))
    F((F)) --> G((G))
    B((B)) --> A((A))
    B((B)) --> D((D))
    G((G)) --> I((I))
    D((D)) --> C((C))
    D((D)) --> E((E)) 
    I((I)) --> H((H))
{{</mermaid>}}

est stocké dans
```python
a = {'F':['B','G'], 'B':['A','D'], 'A':['',''], 'D':['C','E'], \
     'C':['',''], 'E':['',''], 'G':['','I'], 'I':['','H'], \
     'H':['','']}
```

Écrire une fonction récursive `taille` prenant en paramètres un arbre binaire arbre sous la forme d’un dictionnaire et un caractère `lettre` qui est la valeur du sommet de l’arbre, et qui renvoie la taille de l’arbre à savoir le nombre total de nœud.      
On pourra distinguer les 4 cas où les deux « fils » du nœud sont `''`, le fils gauche seulement est `''`, le fils droit seulement est `''`, aucun des deux fils n’est `''`.

#### Test possible

```python
assert taille(a, 'F') == 9
```

{{% solution "Corrigé" %}}

```python
def taille(arbre,lettre):
    if arbre[lettre][0] != "" and arbre[lettre][1] != "":
        return 1 + taille(arbre, arbre[lettre][0]) + taille(arbre, arbre[lettre][1])
    elif arbre[lettre][0] == "" and arbre[lettre][1] != "":
        return 1 + taille(arbre, arbre[lettre][1])
    elif arbre[lettre][0] != "" and arbre[lettre][1] == "":
        return 1 + taille(arbre, arbre[lettre][0])
    else :
        return 1


a= {'F': ['B','G'], 'B': ['A','D'], 'A': ['',''], 'D': ['C','E'], 'C': ['',''], 'E': ['',''], 'G': ['','I'], 'I': ['','H'],'H': ['','']}
``` 

{{% /solution %}}

## Exercice 2 (50% des points)

On considère l'algorithme de tri de tableau suivant : « à chaque étape, on parcourt depuis le début du tableau tous les éléments non rangés et on place en dernière position le plus grand élément ».

Exemple avec le tableau :
```python
t = [41, 55, 21, 18, 12, 6, 25]
```

Étape 1 
: on parcourt tous les éléments du tableau, on permute le plus grand élément avec le dernier. Le tableau devient&nbsp;:
```python
t = [41, 25, 21, 18, 12, 6, 55]
```

Étape 2
: on parcourt tous les éléments **sauf le dernier**, on permute le plus grand élément
trouvé avec l'avant dernier. Le tableau devient&nbsp;:
```python
t = [6, 25, 21, 18, 12, 41, 55]
```
Et ainsi de suite.


Le code de la fonction `tri_iteratif` qui implémente cet algorithme est donné ci-dessous.
```python
def tri_iteratif(tab):
    for k in range( ... , 0, -1):
        imax = ...
        for i in range(0 , ... ):
            if tab[i] > ... :
                imax = i
        if tab[imax] > ... :
            ... , tab[imax] = tab[imax] , ...
    return tab
``` 

Compléter le code qui doit donner :
```python
assert tri_iteratif([41, 55, 21, 18, 12, 6, 25]) == [6, 12, 18, 21, 25, 41, 55]
```

{{% note normal %}}

On rappelle que l’instruction
```python
a, b = b, a
```
échange les contenus de `a` et de `b`.

{{% /note %}}


{{% solution "Corrigé" %}}

```python
def tri_iteratif(tab):
    for k in range( len(tab)-1 , 0, -1):
        imax = k
        for i in range(0 , k ):
            if tab[i] > tab[imax] :
                imax = i
        if tab[imax] > tab[k] :
            tab[k] , tab[imax] = tab[imax] , tab[k]
    return tab
```

{{% /solution %}}