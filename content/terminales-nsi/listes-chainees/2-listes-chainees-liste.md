---
title: "Implémentation du type abstrait Liste Chaînée à l'aide de listes Python"
subtitle: ""
author: ""
type: ""
date: 2023-11-20T15:50:09+04:00
draft: false
toc: true
tags: ["Liste", "Liste chaînée"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

Reprendre toutes les fonctions des sections 2 et 3 du document 1 de ce chapitre, en implémentant cette fois le type abstrait « Liste chaînée » à l'aide de tuples (à la place de la classe).

{{% solution "Réponse" %}}

```python
def est_dans(tab: list[int], val: int) -> bool:
    """
    Recherche la présence de val dans tab.
    """
    trouve = False

    i = 0
    while i < len(tab) and not trouve:
        if val == tab[i]:
            trouve = True
        i += 1

    return trouve


def est_dans_rec(tab: list[int], n: int, i: int = 0) -> bool:
    """
    Recherche si la valeur n est présente au moins une fois
    dans le tableau tab.
    Algorithme récursif, i est l'indice de recherche.
    """
    if i == len(tab):
        return False
    elif tab[i] == n:
        return True
    else:
        return est_dans_rec(tab, n, i + 1)


def insere(tab: list[int], n: int, i: int) -> None:
    """
    Insère la valeur n à l'indice i du tableau tab.
    Algorithm itératif et en place.
    
    Lève une exception si le tableau est déjà plein.
    
    HYPOTHÈSE : la gestion des "trous" n'est pas assurée,
    l'algorithme se contente de décaler les valeurs vers 
    la droite.
    """
    dernier_indice = len(tab) - 1

    if tab[dernier_indice] != None:
        raise Exception("Tableau plein !")

    k = dernier_indice
    while k > i:
        tab[k] = tab[k - 1]
        k -= 1

    #for k in range(dernier_indice, i, -1):
    #    tab[k] = tab[k - 1]

    tab[i] = n


def insere_rec(tab: list[int], n: int, i: int, k: int) -> None:
    """
    Insère la valeur n à l'indice i du tableau tab.
    Algorithm récursif et en place. k est l'indice de
    recherche. 
    Sa première valeur doit être len(tab) - 1.
    
    Lève une exception si le tableau est déjà plein.
    
    HYPOTHÈSE : la gestion des "trous" n'est pas 
    assurée, l'algorithme se contente de décaler 
    les valeurs vers la droite.
    """
    dernier_indice = len(tab) - 1

    if tab[dernier_indice] != None and k == dernier_indice:
        raise Exception("Tableau plein !")
    elif k == i:
        tab[i] = n
        return None
    else:
        tab[k] = tab[k - 1]
        return insere_rec(tab, n, i, k - 1)


if __name__ == "__main__":
    tab = [i for i in range(20)]

    assert est_dans(tab, 12) == True
    assert est_dans(tab, 0) == True
    assert est_dans(tab, 20) == False

    assert est_dans_rec(tab, 12) == True
    assert est_dans_rec(tab, 0) == True
    assert est_dans_rec(tab, 20) == False

    print("Insertion itérative")
    tab = [1, 1, 2, 3, 4, 5, None, None, None]
    print(tab)
    insere(tab, 7, 0)
    print(tab)
    insere(tab, 7, 0)
    print(tab)
    insere(tab, 7, 0)
    print(tab)
    #insere(tab, 7, 0)
    #print(tab)
    print()
    print("Insertion récursive")
    tab = [1, 1, 2, 3, 4, 5, None, None, None]
    print(tab)
    insere_rec(tab, 7, 0, len(tab) - 1)
    print(tab)
    insere_rec(tab, 7, 0, len(tab) - 1)
    print(tab)
    insere_rec(tab, 7, 0, len(tab))
    print(tab)
```

{{% /solution %}}
