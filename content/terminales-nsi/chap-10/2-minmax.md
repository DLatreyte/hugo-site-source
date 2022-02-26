---
title: "Recherche des plus grand et petit éléments dans un tableau"
subtitle: "Chapitre 13,2"
author: ""
type: ""
date: 2022-01-26T05:14:44+04:00
draft: false
toc: true
tags: ["Diviser pour régner", "Recherche"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de cette séance est d'écrire et d'implémenter un algorithme s'appuyant sur le paradigme «&nbsp;Diviser pour régner&nbsp;» qui permet de déterminer le maximum et le minimum des éléments dans un tableau.

1. Générer une liste contenant un million de termes choisis aléatoirement entre un et mille milliards.
{{% solution "Réponse" %}}

```python
from random import randint

if __name__ == "__main__":
    tab = [randint(1, int(1e12)) for i in range(int(1e6))]
```

{{% /solution %}}

2. Utiliser les fonctions `min` et `max` fournies par le langage Python afin d'afficher les maximum et minimum dans la liste.
{{% solution "Réponse" %}}

```python
    print("Fonctions Python")
    val_min, val_max = (min(tab), max(tab))

    print("min = {}, max = {}".format(val_min, val_max))
``` 

{{% /solution %}}

3. Écrire le code de la fonction `maxmin1` qui, à partir d'un algorithme de «&nbsp;brute force&nbsp;», détermine les maximum et minimum dans la liste passée en argument.    
La spécification de la fonction est&nbsp;:
```python
def maxmin1(tab: List[float]) -> Tuple[float, float]:
    """
    Recherche du minimum et du maximum dans le tableau tab.

    Paradigme « Brute force »
    """
```

{{% solution "Réponse" %}}

```python
def maxmin1(tab: List[float]) -> Tuple[float, float]:
    """
    Recherche du minimum et du maximum dans le tableau tab.

    Paradigme « Brute force »
    """
    val_max = tab[0]
    val_min = tab[0]

    for elt in tab:
        if elt > val_max:
            val_max = elt
        if elt < val_min:
            val_min = elt

    return (val_min, val_max)
```

{{% /solution %}}

4. Vérifier le bon fonctionnement de la fonction `maxmin1` en affichant les maximum et minimum dans la liste, à la suite de ceux déterminés à l'aide des fonctions fournies par Python.
{{% solution "Réponse" %}}

```python
    print("Recherche « Brute Force »")
    val_min, val_max = maxmin1(tab)
    print("min = {}, max = {}".format(val_min, val_max))
```

{{% /solution %}}

5. Quelle est la complexité de la fonction `maxmin1`&nbsp;?
{{% solution "Réponse" %}}

Il est nécessaire de parcourir tout le tableau, la complexité est donc en $O(N)$.

{{% /solution %}}

6. Comparer l'efficacité de la fonction `maxmin1` à celle des fonctions fournies par Python en mesurant les durées d'exécution à l'aide de la fonction `time` du module `time`.
{{% solution "Réponse" %}}

```python
import time

if __name__ == "__main__":
    tab = [randint(1, int(1e12)) for i in range(int(1e6))]

    print("Fonctions Python")
    t1 = time.time()
    val_min, val_max = (min(tab), max(tab))
    t2 = time.time()
    print("min = {}, max = {}".format(val_min, val_max))
    print("Durée de la recherche : {} s".format(t2 - t1))

    print("Recherche « Brute Force »")
    t1 = time.time()
    val_min, val_max = maxmin1(tab)
    t2 = time.time()
    print("min = {}, max = {}".format(val_min, val_max))
    print("Durée de la recherche : {} s".format(t2 - t1))
```

Il existe un rapport 2 entre les durées d'exécution des deux fonctions. Elles sont donc du même ordre de grandeur.

{{% /solution %}}

7. En faisant varier le nombre d'éléments dans le tableau, vérifier si les durées d'exécution de la fonction `maxmin1` correspond bien à la complexité établie à la question 5.    
La complexité des fonctions `max` et `min` fournies par Python vous semblent-elles être en $O(N)$&nbsp;?

8. À partir de l'algorithme du tri fusion, écrire et implémenter la fonction `maxmin2` qui, dans un premier temps, se contente de déterminer le maximum dans la liste passée en argument.    
La spécification de la fonction est&nbsp;:
```python
def maxmin2(tab: List[float]) -> float:
    """
    Recherche du maximum dans le tableau tab.
    
    Paradigme : Diviser pour règner
    """
```
{{% solution "Réponse" %}}

```python
def maxmin2(tab: List[float]) -> float:
    """
    Recherche du maximum dans le tableau tab.
    
    Paradigme : Diviser pour régner
    """
    if len(tab) == 1:
        return tab[0]

    milieu = len(tab) // 2
    max1 = maxmin2(tab[:milieu])
    max2 = maxmin2(tab[milieu:])

    return max(max1, max2)
```

{{% /solution %}}

9. Vérifier le bon fonctionnement de la fonction à la suite des précédentes vérifications.
{{% solution "Réponse" %}}

```python
    print("Diviser pour régner")
    val_max = maxmin2(tab)
    print("max = {}".format(val_max))
```

{{% /solution %}}

10. Modifier la fonction `maxmin2` afin qu'elle retourne les maximum et minimum dans la liste.    
La spécification de la fonction est&nbsp;:
```python
def maxmin2(tab: List[float]) -> Tuple[float, float]:
    """
    Recherche du minimum et du maximum dans le tableau tab.
    
    Paradigme : Diviser pour régner
    """
```

{{% solution "Réponse" %}}

```python
def maxmin2(tab: List[float]) -> Tuple[float, float]:
    """
    Recherche du minimum et du maximum dans le tableau tab.
    
    Paradigme : Diviser pour régner
    """
    if len(tab) == 1:
        return (tab[0], tab[0])

    milieu = len(tab) // 2
    max1, min1 = maxmin2(tab[:milieu])
    max2, min2 = maxmin2(tab[milieu:])

    return (min(min1, min2), max(max1, max2))
```

{{% /solution %}}

11. Quelle est la complexité de cette fonction&nbsp;?


12. Vérifier le bon fonctionnement de la fonction à la suite des précédentes vérifications.
{{% solution "Réponse" %}}

```python
print("Diviser pour régner")
    t1 = time.time()
    val_min, val_max = maxmin2(tab)
    t2 = time.time()
    print("min = {}, max = {}".format(val_min, val_max))
    print("Durée de la recherche : {} s".format(t2 - t1))
```

{{% /solution %}}

13. La fonction `maxmin2` est-elle, théoriquement, plus efficace que la fonction `maxmin1`&nbsp;? Dans la pratique&nbsp;? Comment expliquer ce comportement&nbsp;?
