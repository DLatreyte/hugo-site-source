---
title: "Utilisation de numpy pour créer et gérer des vecteurs"
subtitle: ""
author: ""
type: ""
date: 2022-01-03T21:13:39+04:00
draft: false
toc: true
tags: ["Numpy"]
categories: ["Tutoriel"]
image: ""
solution_est_visible: true
auto_numbering: false
---

```python
import numpy as np
```

**Remarque :** Différence avec `R`, les indices commencent à 0.

## Création manuelle à partir d'un ensemble de valeurs

```python
tab = np.array([1, 2, 2.5, 3.2, 1.8])
``` 
### Type de la structure

```python
print(type(tab))
```
### Type des données

```python
print(tab.dtype)  # float64
```
### Nombre de dimensions

```python 
print(tab.ndim)  # 1 vecteur, 2 matrice
```

### Nombre de lignes et de colonnes

```python
print(tab.shape)
```

### Nombre total de valeurs

```python
print(tab.size)
```

## Type des données

```python
tab = np.array([1, 2, 4])
print(tab.dtype)  # int64

tab = np.array([1, 2, 4], dtype=float)
print(tab.dtype)  # float64

tab = np.array([False, True, False, False], dtype=bool)
print(tab.dtype)  # bool
```

**Remarque :** il est possible de créer des tableaux d'objets tels que les dictionnaires (`dtype=object`)

## Création d'une séquence de valeurs

### Suite arithmétique de raison 1

```python
tab = np.arange(start=0, stop=10)
print(tab)
```


### Suite arithmétique de raison step

```python
tab = np.arange(start=0, stop=10, step=2)
print(tab)
```

### Suite linéaire (nombre de valeurs fourni et point final est inclus)

```python
tab = np.linspace(start=0, stop=10, num=11)
print(tab)
```

### Vecteur de valeurs toutes égales à 1

```python
tab = np.ones(shape=5)
print(tab)
```

### Vecteur de valeurs toutes égales à 0

```python
tab = np.zeros(5)
print(tab)
```

### Vecteur de valeurs toutes égales à 3.2

```python
tab = np.full(shape=5, fill_value=3.2)
print(tab)
```


### Conversion d'une liste en vecteur

```python
lst = [4, 5, 6, 16, 18, 48, 64]
print(lst)
tab = np.asarray(lst, dtype=float)
print(tab)
```

## Nombres aléatoires

### Création d'un vecteur d'entiers aléatoires

{{% note tip %}}

Pour `size` on peut utiliser un nombre à la place du tuple.

{{% /note %}}

```python
tab = np.random.randint(1, high=100, size=(1000,))
print(tab)
```

### Création d'un vecteur de floats aléatoires compris entre 0 (inclus) et 1 (exclus)

```python
tab = np.random.rand(1000)
print(tab)
```

## Manipulation de fichiers

### Chargement à partir d'un fichier

**Remarque :** Pas d'entête.

```python
tab = np.loadtxt("vecteur.txt", dtype=float)
print(tab)
```


### Sauvegarde d'un vecteur dans un fichier texte

```python
lst = [np.random.randint(1, 10000) for i in range(1000)]
tab = np.asarray(lst, dtype=float)
np.savetxt("backup.txt", tab)
```

## Redimensionnements

### Ajout d'une valeur à la fin d'un tableau

```python
tab = np.array([1, 2, 3, 4])
tab = np.append(tab, 5)  # Ne modifie pas en place le tableau mais crée un nouveau tableau
print(tab)
```

### Suppression d'un élément

```python
tab = np.delete(tab, 2)  # Ne modifie pas en place le tableau mais crée un nouveau tableau
print(tab)
```

### Modification de la dimension (les nouvelles cases sont remplies par des 0)

```python
tab.resize((10,))
print(tab)
```

**Remarque :** Autre écriture possible si vecteur : 
```python
tab.resize(10)
```

### Concaténation de deux vecteurs

```python
tab1 = np.random.rand(20)
tab2 = np.random.rand(15)
tab = np.append(tab1, tab2)
print(tab)
```


## Filtrage - Extraction

### À l'aide d'un vecteur de booléens

```python
tab = np.array([1, 2, 3, 4])
cond = np.array([False, True, False, True])
print(tab[cond])
```

{{% note warning %}}

- Si la longueur de `cond` trop petite, les valeurs qui manquent sont égales à `False`.
- Si la longueur de `cond` trop grande, une exception est levée.

{{% /note %}}

### Une opération booléenne sur un vecteur retourne un vecteur de booléens

```python
cond = tab > 2
print(cond)
```


### Filtrage à l'aide d'une condition

```python
new_tab = tab[tab > 2]
print(new_tab)
```


## Fonctions accessibles

Si `tab` est défini par
```python
tab = np.random.rand(1000)
```


### Valeur maximale

```python
print(np.max(tab))
```

### Indice de la valeur maximale

```python
print(np.argmax(tab))
```

### Valeur minimale

```python
print(np.min(tab))
```

### Indice de la valeur minimale

```python
print(np.argmin(tab))
```

### Tri des valeurs

```python
print(np.sort(tab))
```

### Indices du vecteur trié

```python
print(np.argsort(tab))
```


# Vecteur constitué de valeurs toutes différentes

```python
print(np.unique(tab))
```

## Calculs sur les vecteurs

### Moyenne

```python
print(np.mean(tab))
```

### Médiane

```python
print(np.median(tab))
```


### Variance

```python
print(np.var(tab))
```


### Quantile

```python
print(np.percentile(tab, 50))
```


### Somme

```python
print(np.sum(tab))
```


### Somme cumulée

```python
print(np.cumsum(tab))
```

## Calculs entre vecteurs

{{% note warning %}}

**Principe :** les calculs se font éléménts par éléments entre les vecteurs

{{% /note %}}

```python
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 2, 3, 4, 6])
z = x * y
u = x + y
v = x / y
w = x - y
t = x < y
print(z, u, v, w, t)
```


## Fonctions matricielles

### Produit scalaire

```python
z = np.vdot(x, y)
print(z)
```


### Calcul de la norme

```python
n = np.linalg.norm(x)
print(n)

tab = np.array([2.1, 3.4, 6.7, 8.1, 3.5, 7.2])
tab = tab.reshape(2, 3)
print(tab.shape)
```
