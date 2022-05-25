"""
Implémentation du tri sélection.
"""

def tri_selection(tab):
    """
    Implémentation du tri par sélection.
    La tableau est trié en place. En théorie, il n'est pas nécessaire de retourner le
    tableau.
    """
    nb = len(tab) - 1  # dernier indice
    
    for i in range(0, nb):  # du premier à l'avant-dernier indice
        min = i
        for j in range(i + 1, nb+1):  # de l'indice i+1 au dernier indice
            if tab[j] < tab[min]:
                min = j
        # Permutation du contenu des variables
        k = tab[i]
        tab[i] = tab[min]
        tab[min] = k
    return tab


def main():
    tab = [5, 2, 4, 6, 1, 3]
    print(tab)
    tri_selection(tab)
    print(tab)
    
main()