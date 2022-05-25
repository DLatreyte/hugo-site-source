"""
Implémentation du tri par insertion.
"""

def tri_insertion(tab):
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

def main():
    tab = [5, 2, 4, 6, 1, 3]
    print(tab)
    tri_insertion(tab)
    print(tab)
    
main()