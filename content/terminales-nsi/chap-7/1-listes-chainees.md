---
title: "Listes Chaînées"
subtitle: "Chapitre 7,1"
author: ""
type: ""
date: 2020-10-14T18:01:18+04:00
draft: false
toc: true
tags: ["Tableau", "Tableau dynamique", "Liste", "Liste chaînée", "Complexité"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---
{{% note normal %}}
- Un corrigé de la **section 1** se trouve {{< remote "ici" "https://repl.it/@dlatreyte/tableaux" >}}
- Un corrigé des **sections suivantes** se trouve {{< remote "ici" "https://repl.it/@dlatreyte/listeschainees" >}}
{{% /note %}}

## Tableaux

{{% note tip %}}
- Un **tableau** est une *structure de données* dans laquelle *les éléments, de même type, occupent des positions contiguës en mémoire*.   
- Le nombre d'éléments qu'un tableau peut contenir est déterminé à la création d'un tableau.
{{% /note %}}

|Type Python | Type abstrait | Opération | Exemple | Complexité |
| :----: | :----: | :----: | :----: | :----: |
| N'existe pas | Tableau | Accès à un élément | `tab[i]` | $O(1)$ |
|  |  | Modification d'un élément | `tab[i] = x` | $O(1)$ |
| |  | Effacement d'un élément | `retire(tab, i)` | $O(n)$ |
| |  | Insertion d'un élément | `insere(tab, x, i)` | $O(n)$ |
| |  | Recherche d'un élément | `est_dans(tab, x)` | $O(n)$ |

{{% note normal %}}
- La structure de données appelée « liste » dans le langage Python est en fait un **tableau dynamique**.
{{% /note %}}

**Remarque :** Dans la suite de ce document, on va considérer que la liste Python `tab`, créé par l'instruction `tab = [i for i in range(20)]` est de longueur fixe. Elle se comporte alors comme un tableau.

### Pourquoi la recherche d'un élément dans un tableau quelconque (non trié donc) est en $O(N)$ ?

1. Écrire le prédicat `est_dans` de spécification :
```python
def est_dans(tab: List[int], n: int) -> bool:
    """
    Recherche si la valeur n est présente au moins une fois
    dans le tableau tab.
    Algorithm itératif.
    """
```

2. Écrire un jeu de tests.

3. (Facultatif) Écrire le prédicat `est_dans_rec` de spécification :
```python
def est_dans_rec(tab: List[int], n: int, i: int = 0) -> bool:
    """
    Recherche si la valeur n est présente au moins une fois
    dans le tableau tab.
    Algorithme récursif, i est l'indice de recherche.
    """
```

4. Quelle est la complexité des algorithmes précédents en fonction de $N$, la taille du tableau ?
{{% solution "Réponse" %}}
- Dans l'algorithme itératif, dans le pire des cas (valeur absente du tableau) $N$ tours de boucle sont effectués.
- Dans l'algorithme récursif, $N$ appels récursifs sont effectués.

L'algorithme est donc en $O(N)$.
{{% /solution %}}

### Pourquoi l'insertion d'un élément dans un tableau est en $O(N)$ ?

Dans cette partie, on imagine que le tableau a cette allure :
<center>

| 1 | 1 | 2 | 3 | 4 | 5 | vide | vide | vide |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

</center>

Si on introduit, en position 1, la valeur 7. Le tableau est alors :
<center>

| 7 | 1 | 1 | 2 | 3 | 4 | 5 | vide | vide |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |

</center>

{{% note warning %}}
Cette opération n'est possible, sans crainte de perdre des données, que si toutes les cellules du tableau ne contiennent pas des données.
Toute fonction permettant l'insertion de valeurs doit donc avertir un utilisateur dans le cas contraire.
{{% /note %}}

**Remarque :** Dans le code ci-dessous, les cellules seront considérées vides si elles contiennent la valeur `None`.

5. Écrire la fonction `insere` dont la spécification est :
```python
def insere(tab: List[int], n: int, i: int) -> None:
    """
    Insère la valeur n à l'indice i du tableau tab.
    Algorithm itératif et en place.

    Lève une exception si le tableau est déjà plein.

    HYPOTHÈSE : la gestion des "trous" n'est pas assurée,
    l'algorithme se contente de décaler les valeurs vers 
    la droite.
    """
``` 

6. (Facultatif) Écrire la fonction `insere_rec` dont la spécification est :
```python
def insere_rec(tab: List[int], n: int, i: int, k: int) -> None:
    """
    Insère la valeur n à l'indice i du tableau tab.
    Algorithm récursif et en place. k est l'indice de recherche. Sa première valeur doit être len(tab) - 1.

    Lève une exception si le tableau est déjà plein.

    HYPOTHÈSE : la gestion des "trous" n'est pas assurée,
    l'algorithme se contente de décaler les valeurs vers 
    la droite.
    """
``` 

7. Quelle est la complexité des algorithmes précédents en fonction de $N$, la taille du tableau ?
{{% solution "Réponse" %}}
- Dans le pire des cas (insertion à la première place du tableau), on déplace $N-1$ valeurs.

L'algorithme est donc en $O(N)$.
{{% /solution %}}

## Structure de liste chaînée

{{% note tip %}}
Les **listes chaînées** constituent une structure de données :
- de *longueur modifiable* ;
- *plus efficace que les tableaux lorsqu'il s'agit d'ajouter ou de retirer un élément* (il n'est pas nécessaire de faire de la place en déplaçant les éléments) ;
- qui servira de brique à l'élaboration d'autres structures de données.
{{% /note %}}

{{% note tip %}}
Une **liste chaînée** permet de représenter une liste ; *chaque élément de cette liste est une **cellule*** contenant :
- la **valeur** de l'élément à stocker ;
- l'**adresse mémoire de la cellule** représentant l'élément suivant.
{{% /note %}}

<img src="/terminales-nsi/chap-7/chap-7-1-1.png" alt="" width="60%" />

**Remarque :** le symbole $\perp$ marque la fin de la liste dans les schémas.

### Comment implémenter une cellule ?

En langage Python, on peut implémenter une cellule à l'aide d'une classe, de listes ou de tuples.

8. Définir la classe `Cellule` dont la spécification est :
```python
class Cellule():
    """
    Implémentation d'une cellule de liste chaînée
    de nombres entiers.

    Attributs
    ---------
    valeur : int
        Valeur à stocker dans la liste
    suivante : Cellule
        Addresse de la cellule suivante (chaînée)
    """
```

{{% note normal %}}
La *dernière cellule d'une liste chaînée devra pointer vers l'objet* `None` *qui représente donc une **cellule vide**.*
{{% /note %}}

9. Instancier 3 objets `c1`, `c2`, `c3`, de type `Cellule`, dont les valeurs sont 1, 2, 3.   
Tous ces objets sont pour l'instant isolés (ils ne pointent vers aucune autre cellule si ce n'est la cellule vide `None`).

10. Créer la liste `lst` à l'aide de ces trois objets.

11. Comment aurait-on pu créer la liste `lst` en une seule instruction ?   
<img src="/terminales-nsi/chap-7/chap-7-1-2.png" alt="" width="65%" />

### Les listes chaînées sont des structures fondamentalement récursives

{{% note tip %}}
Une liste chaînée est :
- *soit la liste vide* (objet `None`) ;
- *soit constituée de son premier élément* (objet de type `Cellule`) et *du reste des éléments qui forment aussi une liste*.    
Une liste chaînée est donc une **structure récursive**.
{{% /note %}}

### Une liste chaînée est-elle forcément homogène

Tout au long de ce document nous allons uniquement envisager des listes chaînées de nombres entiers. Rien n'impose, cependant, à l'attribut `valeur` de la classe `Cellule` d'être un entier. Chaque cellule peut même posséder des attributs `valeur` de type différent. *Les listes chaînées peuvent donc être hétérogènes.*

## Quelques opérations sur les listes chaînées

### Longueur d'une liste chaînée

12. Écrire la fonction `longueur` dont la spécification est :
```python
def longueur(lst: Cellule) -> int:
    """
    Détermine la longueur de la liste lst.

    Algorithm récursif.
    """
``` 

13. Écrire la fonction `longueur_iter` dont la spécification est :
```python
def longueur_iter(lst: Cellule) -> int:
    """
    Détermine la longueur de la liste lst.

    Algorithm itératif.
    """
``` 

14. Déterminer la complexité du calcul de la longueur d'une liste.
{{% solution "Réponse" %}}
On réalise autant d'appels récursifs (ou de tours de boucles qu'il y a d'éléments dans la liste).  
La complexité est donc en $O(N)$.
{{% /solution %}}

### Affichage de tous les éléments d'une liste

15. Écrire la fonction `affichage_elements_liste` dont la spécification est :
```python
def affichage_elements_liste(lst: Cellule) -> None:
    """
    Affiche tous les éléments de la liste lst.
    Chaque élément est séparé par une tabulation "\t"
    """
```

### Valeur du n-ième élément d'une liste

16. Écrire la fonction `n_ieme_element` dont la spécification est :
```python
def n_ieme_element(lst: Cellule, i: int) -> int:
    """
    Retourne le n-ième élément de la liste. La convention
    suivie est celle de Python, le premier élément ayant
    l'indice i = 0.

    Algorithme récursif.

    Lève une exception si l'indice de la liste est trop grand.
    """
``` 

17. Écrire la fonction `n_ieme_element_iter` dont la spécification est :
```python
def n_ieme_element_iter(lst: Cellule, i: int) -> int:
    """
    Retourne le n-ième élément de la liste. La convention
    suivie est celle de Python, le premier élément ayant
    l'indice i = 0.

    Algorithme itératif.

    Lève une exception si l'indice de la liste est trop grand.
    """
``` 

18. Déterminer la complexité de la recherche du n-ième élément d'une liste.
{{% solution "Réponse" %}}
- Si l'élément dont on cherche la valeur est le dernier de la liste il est nécessaire de faire $N$ appels récursifs (ou tours de boucles).
- Si l'indice est hors des limites, il est ici aussi nécessaire de parcourir toute la liste avant de s'en rendre compte.
L'algorithm est donc en $O(N)$.
{{% /solution %}}


### Modification de la valeur d'une cellule sans modifier la structure de la liste

19. Écrire la fonction `modifier_n_ieme_element` dont la spécification est : 
```python
def modifier_n_ieme_element(lst: Cellule, i: int, valeur: int) -> None:
    """
    Modifie le n-ième élément de la liste. La convention
    suivie est celle de Python, le premier élément ayant
    l'indice i = 0.

    Algorithme récursif.

    Lève une exception si l'indice de la liste est trop grand.
    """
```

### Ajout d'une valeur à la fin de la liste

20. Écrire la fonction `ajout_fin_liste` dont la spécification est :
```python
def ajout_fin_liste(lst: Cellule, valeur: Cellule) -> None:
    """
    Ajout de valeur à la fin de la liste.
    La liste lst est modifiée.

    Algorithme récursif.
    """
``` 

21. Quelle est la complexité de la fonction `ajout_fin_liste` ?
{{% solution "Réponse" %}}
On doit parcourir toute la liste pour ajouter un élément à la fin. La complexité est donc linéaire.
{{% /solution %}}

22. Écrire la fonction `ajout_debut_liste` dont la spécification est :
```python
def ajout_debut_liste(lst: Cellule, valeur: Cellule) -> Cellule:
    """
    Ajout de valeur au début de la liste.
    Création d'une nouvelle liste mais toute modification de la liste
    lst modifie cette nouvelle liste.
    """
````

23. Quelle est la complexité de cette fonction ?
{{% solution "Réponse" %}}
$O(1)$
{{% /solution %}}

### Retrait du dernier élément d'une liste

24. Écrire la fonction `retrait_dernier_element` dont la spécification est :
```python
def retrait_dernier_element(lst: Cellule) -> int:
    """
    Retire le dernier élément de la liste et le retourne.

    Algorithme récursif.
    """
```

### Concaténation de deux listes

{{% note tip %}}
On appelle **concaténation** de deux listes l'opération consistant à mettre bout à bout les deux listes.
{{% /note %}}

25. Écrire la fonction `concatener` dont la spécification est :
```python
def concatener(lst1: Cellule, lst2: Cellule) -> Cellule:
    """
    Concatène les listes lst1 et lst2. Une nouvelle liste est
    créée et retournée.
    Les éléments de la première liste sont copiés alors que ceux 
    de la deuxième sont insérés. lst1 et lst2 ne sont donc pas modifiées.

    ATTENTION : tout élément de lst partagé avec lst2 modifié l'est aussi 
    dans lst2.
    
    Algorithme récursif.
    """
``` 
<img src="/terminales-nsi/chap-7/chap-7-1-3.png" alt="" width="100%" />

26. Écrire la fonction `copie` dont la spécification est :
```python
def copie(lst: Cellule) -> Cellule:
    """
    Réalise une nouvelle copie de la liste lst.

    Algorithme récursif.
    """
``` 
<img src="/terminales-nsi/chap-7/chap-7-1-4.png" alt="" width="75%" />

27. Se servir de la fonction `copie` pour écrire la fonction `concatener_avec_copie_integrale` dont la spécification est : 
```python
def concatener_avec_copie_integrale(lst1: Cellule, lst2: Cellule) -> Cellule:
    """
    Concatène les listes lst1 et lst2. Les éléments des listes lst1 et lst2
    sont recopiés pour former une nouvelle liste.
    
    Algorithme récursif.
    """
```
<img src="/terminales-nsi/chap-7/chap-7-1-5.png" alt="" width="100%" />

28. Quelle est la complexité de la fonction `concatener` ? Même question pour la fonction `concatener_avec_copie_integrale`.
{{% solution "Réponse" %}}
- Dans le premier cas, il est nécessaire de recopier tous les éléments de `lst1`. La complexité est donc linéaire et dépend du nombre d'élements de `lst1`.
- Dans le second cas, on recopie tous les éléments de `lst1` et de `lst2`. La complexité est donc linéaire et est la somme du nombre d'éléments de `lst1` et de `lst2`.
{{% /solution %}}

### Renverser une liste

29. Écrire la fonction `renverser` dont la spécification est : 
```python
def renverser(lst: Cellule) -> Cellule:
    """
    Retourne une nouvelle liste formée des éléments de lst à l'envers. 
    Les éléments peuvent avoir été recopiés ou pas.

    Algorithme récursif.
    """
```
**Remarque.** Cette fonction doit s'appuyer sur les fonctions `concatener` ou `concatener_avec_copie_integrale`.

<img src="/terminales-nsi/chap-7/chap-7-1-6.png" alt="" width="85%" />

**Remarque.** Cet algorithme est particulièrement inefficace.


## Conclusion

{{% note tip %}}
- Une **liste chaînée** est une structure de données utile pour représenter une *séquence finie d'éléments*. 
- Chaque élément est contenu dans une **cellule**, qui fournit, en plus de la **valeur**, un moyen pour accéder à la **cellule suivante**. 
- Les opérations sur les listes chaînées se programment sous la forme de **parcours qui suivent ces liaisons**, en utilisant la récursivité ou des boucles.
{{% /note %}}


## Tests possibles

```python
if __name__ == "__main__":
    #c1 = Cellule(1, None)
    #c2 = Cellule(2, None)
    #c3 = Cellule(3, None)
    #lst = c1
    #lst.suivante = c2
    #c2.suivante = c3

    lst = Cellule(1, Cellule(2, Cellule(3, Cellule(4, None))))
    affichage_elements_liste(lst)

    assert longueur(lst) == 4
    assert longueur_iter(lst) == 4

    assert n_ieme_element(lst, 0) == 1
    assert n_ieme_element(lst, 3) == 4
    #print(n_ieme_element(lst, 4))

    assert n_ieme_element_iter(lst, 0) == 1
    assert n_ieme_element_iter(lst, 3) == 4
    #print(n_ieme_element_iter(lst, 4))

    lst1 = Cellule(1, Cellule(2, Cellule(3, Cellule(4, None))))
    lst2 = Cellule(5, Cellule(6, Cellule(7, None)))
    lst3 = concatener_avec_copie_integrale(lst1, lst2)
    print(lst3)

    # Modification de la liste
    modifier_n_ieme_element(lst, 0, 12)
    assert n_ieme_element_iter(lst, 0) == 12

    # Ajout en fin de liste
    ajout_fin_liste(lst, Cellule(25, None))
    affichage_elements_liste(lst)

    # Ajout en début de liste
    lst = ajout_debut_liste(lst, Cellule(34, None))
    affichage_elements_liste(lst)

    # Retrait dernier élément
    dernier = retrait_dernier_element(lst)
    print(dernier)
    affichage_elements_liste(lst)
    ```
