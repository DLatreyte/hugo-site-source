---
title: "Structures de données fournies avec le langage Python"
subtitle: "Chapitre 6,1"
author: ""
type: ""
date: 2020-10-13T05:25:49+04:00
draft: false
toc: true
tags: ["Dictionnaire", "Liste", "Tableau dynamique", "Structures de données", "Ensemble", "Complexité", "Tableau associatif"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---
Python possède dans la bibliothèque standard un grand nombre de structures de données, programmées de manière efficace.

## Pourquoi différentes structures de données ?

Les **structures de données** *organisent différemment les données que le programme traite*. Le langage Python fournissant le type `list`, on pourrait se demander pourquoi ne pas *systématiquement* l'utiliser et pourquoi devoir apprendre de nouveaux types.   
En fait, *la spécialisation des structures de données rend la programmation plus simple (utilisation de l'**API**) et plus efficace (**complexité**).*

{{% note warning %}}

Nous verrons dans les prochains chapitres qu'*il faut distinguer l'objet que l'on manipule dans un programme de son implémentation* (comment il est programmé).

{{% /note %}}

{{% note tip %}}

Un même type peut être implémenté de différentes façons. *Dans tous les cas, il présente la même interface au programmeur* (API).

On parle donc de **type abstrait**.

{{% /note %}}

## Liste : `list`

Le type `list` de Python n'est pas implémeté à l'aide de **listes chaînées** (que nous étudierons au [chapitre 7](../../chap-7)), car *la suppression ou l’ajout ailleurs qu’en fin de liste nécessite de décaler les valeurs de fin de liste, et n’est donc pas réalisé en temps constant*. D’autre part, *l’accès à un élément quelconque est réalisé en temps constant*, ce qui n’est pas le cas avec une liste chaînée. 

Le type `list` de Python est implémenté à l'aide de *tableaux dynamiques*.

## Tableau associatif : `dict`

Le type `dict` de Python est une implémentation du type abstrait **tableau associatif**. L’implémentation correspond à une **table de hachage**, ce qui signifie que *la valeur est stockée dans un tableau et que la position dans ce tableau dépend du résultat d’une fonction de hachage appliquée à la clé*. En un temps indépendant du nombre de valeurs stockées dans le dictionnaire, Python peut retrouver la valeur associée à n’importe quelle clé : pour cela il calcule un indice à partir de la valeur de la clé (qui doit donc être hachable, c’est-à-dire récursivement non mutable) et récupère la valeur stockée à cet indice dans un tableau.

Une caractéristique essentielle des dictionnaires est que *la récupération d’une valeur associée à une clé se fait en un temps constant, indépendant de la taille du dictionnaire*. De même, *savoir si une clé fait partie du dictionnaire prend un temps constant* (alors que vérifier si un élément est dans une liste prend un temps proportionnel à la taille de la liste).

## Ensemble : `set` 

Un ensemble Python (`set`) est *équivalent à un dictionnaire ne contenant que des clés*. Par construction, *chaque élément est donc unique*. De plus, avec le type `set` on dispose déjà des opérations ensemblistes habituelles, implémentées de manière très efficace : **union**, **intersection**, **différence**, etc.

## Opérations usuelles et complexité en temps

### Opérations sur les listes

|Type Python | Type abstrait | Opération | Exemple | Complexité |
| :----: | :----: | :----: | :----: | :----: |
| `list` | Tableau dynamique | Ajout à la fin | `lst.append(x)` | $O(1)$ |
| `lst=[]` |  | Accès à un élément | `lst[i]` | $O(1)$ |
| `len(lst)` |  | Modification d'un élément | `lst[i] = x` | $O(1)$ |
| |  | Effacement d'un élément | `del lst[i]` | $O(n)$ |
| |  | Insertion d'un élément | `lst.insert(i, x)` | $O(n)$ |
| |  | Recherche d'un élément | `x in lst` | $O(n)$ |

### Opérations sur les dictionnaires

|Type Python | Type abstrait | Opération | Exemple | Complexité |
| :----: | :----: | :----: | :----: | :----: |
| `dict` | Tableau associatif | Ajout d'un élément | `d[key] = val` | $O(1)$ |
| `d={}` |  | Modification d'un élément | `d[key] = val` | $O(1)$ |
| `len(d)` |  | Effacement d'un élément | `del d[key]` | $O(1)$ |
| |  | Accès à un élément | `d[key]` | $O(1)$ |
| |  | Recherche d'une clé | `key in d` | $O(1)$ |
| |  | Recherche d'une valeur | `val in d.values()` | $O(n)$ |

### Opérations sur les ensembles

|Type Python | Type abstrait | Opération | Exemple | Complexité |
| :----: | :----: | :----: | :----: | :----: |
| `set` | Ensemble | Ajout d'un élément | `s.add(elt)` | $O(1)$ |
| `s = {}` |  | Retrait d'un élément | `s.remove(elt)` | $O(1)$ |
| `len(s)` |  | Test d'appartenance | `elt in s` | $O(1)$ |
| |  | Union | `s \| t` | $O(n + m)$ |
| |  | Intersection | `s & t` | $O(min(n, m))$ |
| |  | Différence | `s - t` | $O(n)$ |
| |  | Différence symétrique | `s ^ t` | $O(n)$ |