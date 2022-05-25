from typing import List

def table_multiplication(n: int) -> List[List[int]]:
    """
    Détermine la table de multiplication de tous les entiers compris entre
    1 et n.
    
    >>> table_multiplication(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
    table = []
    
    for i in range(1, n + 1):
        ligne = []
        for j in range(1, n + 1):
            ligne.append(i * j)
        table.append(ligne)
        
    return table

def longueur_liste(liste: List) -> int:
    """Détermine la longueur de la liste reçue en argument. """
    longueur = 0
    
    for element in liste:
        longueur += 1
    
    return longueur


if __name__ == "__main__":
    import doctest
    doctest.testmod()