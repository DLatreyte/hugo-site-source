def triple_du_precedent(a: int) -> str:
    """
    Retourne une chaîne de caractères formée par une suite de 12
    entiers dont chaque terme est égal au triple du précédent,
    à partir du premier entier a, positif,  passé en argument.
    
    >>> triple_du_precedent(1)
    '1 3 9 27 81 243 729 2187 6561 19683 59049 177147 '
    >>> triple_du_precedent(5)
    '5 15 45 135 405 1215 3645 10935 32805 98415 295245 885735 '
    """
    reponse = ""    # Initialisation de la chaîne à retourner
    val_max_compteur = 12   # Valeur maximale pour le compteur
    
    for i in range(1, val_max_compteur + 1):
        reponse += "{} ".format(a)
        a *= 3

    return reponse


def multiplication(a: int) -> str:
    """
    Retourne une chaîne de caractères formées des 10 premiers
    nombres de la table de multiplication de a.
    
    >>> multiplication(7)
    '7 14 21 28 35 42 49 56 63 70 '
    """
    reponse = ""  # Initialisation de la chaîne à retourner
    val_max_compteur = 10
    
    for i in range(1, val_max_compteur + 1):
        reponse += str(a * i) + " "

    return reponse


def multiplication_multiple_trois(a: int) -> str:
    """
    Retourne une chaîne de caractères formées des 10 premiers
    nombres de la table de multiplication de a en signalant au
    passage ceux qui sont des multiples de 3.
    
    >>> multiplication_multiple_trois(2)
    '2 4 6* 8 10 12* 14 16 18* 20 '
    >>> multiplication_multiple_trois(7)
    '7 14 21* 28 35 42* 49 56 63* 70 '
    """
    reponse = ""  # Initialisation de la chaîne à retourner
    val_max_compteur = 10  
    
    for i in range(1, val_max_compteur + 1):
        valeur = a * i
        reponse += str(valeur)
        if valeur % 3 == 0:  # si multiple de 3
            reponse += "*"   # ajouter astérisque
        reponse += " "  # pour séparer les valeurs

    return reponse


def multiplication_multiple_sept(a: int) -> str:
    """
    Calcule les 50 premiers termes de la table de a mais retourne
    une chaîne de caractères contenant uniquement les multiples de 7.
    
    >>> multiplication_multiple_sept(2)
    '14 28 42 56 70 84 98 '
    >>> multiplication_multiple_sept(9)
    '63 126 189 252 315 378 441 '
    """
    reponse = ""  # Initialisation de la chaîne à retourner
    val_max_compteur = 50
    
    for i in range(1, val_max_compteur + 1):
        valeur = a * i
        if valeur % 7 == 0:  # si multiple de 3
            reponse += str(valeur) + " "   # ajouter valeur

    return reponse


def diviseurs(a: int) -> str:
    """
    Retourne une chaîne de caractères formée de la liste des diviseurs
    de a.
    
    >>> diviseurs(18)
    '18 9 6 3 2 1 '
    """
    reponse = ""
    
    for n in range(a, 0, -1):
        if a % n == 0:
            reponse += str(n) + " "

    return reponse


def table_multiplication() -> str:
    """
    Retourne la table de multiplication des nombres de 1 à 10.
    """
    reponse = ""
    val_max = 10
    
    for i in range(1, val_max + 1):
        for j in range(1, val_max + 1):
            reponse += "{} ".format(i * j)
        reponse += "\n"

    return reponse


def plus_grand_plus_petit(nbre_valeurs: int) -> str:
    """
    Demande à l'utilisateur d'entrer nbre_valeurs valeurs et retourne une
    chaîne de caractères formée des deux valeurs max et min.
    """
    valeur = float(input("Entrez la valeur 1 : "))
    valeur_plus_grande = valeur
    valeur_plus_petite = valeur

    for i in range(2, nbre_valeurs + 1):
        valeur = float(input("Entrez la valeur {} : ".format(i)))
        if valeur > valeur_plus_grande:
            valeur_plus_grande = valeur
        elif valeur < valeur_plus_petite:
            valeur_plus_petite = valeur

    reponse = "max : {}, min : {}".format(valeur_plus_grande,
                                          valeur_plus_petite)
    return reponse


if __name__ == "__main__":
    import doctest
    doctest.testmod()