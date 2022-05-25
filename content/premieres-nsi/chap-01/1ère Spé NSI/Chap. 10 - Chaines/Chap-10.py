def longueur(chaine: str) -> int:
    """
    Détermine la longueur de la chaine passée en argument.
    """
    long = 0
    for element in chaine:
        long += 1
    return long

def est_dans(chaine: str, caractere: str) -> bool:
    """
    Détermine si le caractère passé en argument appartient ou pas à
    la chaîne passée en argument.
    """
    for car in chaine:
        if car == caractere:
            return True
    return False