"""
Implémentation de quelques opérations utilisées en statistique.
"""
from typing import List
from random import randint


def tri_insertion(tab: List) -> List:
    """
    Tri par insertion. Cet algorithm fonctionne en place.
    Il n'est théoriquement pas nécessaire de retourner le
    tableau puisqu'il est modifié par la fonction mais on le
    fait pour des raisons de simplicité.
    """
    nb = len(tab)
    
    for i in range(1, nb):
        cle = tab[i]
        
        j = i - 1
        while j >= 0 and tab[j] > cle:
            tab[j + 1] = tab[j]
            j = j - 1
            
        tab[j + 1] = cle
    
    return tab


def etendue_sans_tri(serie: List) -> float:
    """
    Détermine l'étendue d'une série statistique pour une série non
    triée.
    """
    val_min = serie[0]
    val_max = serie[0]
    
    for i in range(1, len(serie)):
        if serie[i] < val_min:
            val_min = serie[i]
        elif serie[i] > val_max:
            val_max = serie[i]
            
    return val_max - val_min


def main():
#     serie = [0, 10, 6, 4, 4, 6, 4, 1]
    serie = [randint(0, 1000) for i in range(1000)]
    print("Série de travail : {}".format(serie))
    print("Étendue : {}".format(etendue_sans_tri(serie)))
    


main()