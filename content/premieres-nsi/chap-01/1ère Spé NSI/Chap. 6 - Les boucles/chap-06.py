def inconnue(a: int, b: int) -> int:
    """ Fonction dont il faut déterminer l'action. """
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b


def inconnue_deux(a: int) -> int:
    """ Fonction dont il faut déterminer l'action. """
    b = 1
    i = 2
    while i <= a:
        b *= i
        i += 1
    return b


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
    compteur = 1    # Initialisation du compteur
    val_max_compteur = 12   # Valeur maximale pour le compteur

    while compteur <= val_max_compteur:
        reponse += str(a) + " "  # reponse += "{} ".format(a)
        a *= 3
        compteur += 1
    return reponse


def multiplication(a: int) -> str:
    """
    Retourne une chaîne de caractères formées des 10 premiers
    nombres de la table de multiplication de a.
    
    >>> multiplication(7)
    '7 14 21 28 35 42 49 56 63 70 '
    """
    reponse = ""  # Initialisation de la chaîne à retourner
    compteur = 1
    val_max_compteur = 10
    
    while compteur <= val_max_compteur:
        reponse += str(a * compteur) + " "
        compteur += 1
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
    compteur = 1  # Initialisation du compteur
    val_max_compteur = 10  
    
    while compteur <= val_max_compteur:
        valeur = a * compteur
        reponse += str(valeur)
        if valeur % 3 == 0:  # si multiple de 3
            reponse += "*"   # ajouter astérisque
        reponse += " "  # pour séparer les valeurs
        compteur += 1
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
    compteur = 1  # Initialisation du compteur
    val_max_compteur = 50
    
    while compteur <= val_max_compteur:
        valeur = a * compteur
        if valeur % 7 == 0:  # si multiple de 3
            reponse += str(valeur) + " "   # ajouter valeur
        compteur += 1  # Incrémentation du compteur
    return reponse  


def diviseurs(a: int) -> str:
    """
    Retourne une chaîne de caractères formée de la liste des diviseurs
    de a.
    
    >>> diviseurs(18)
    '18 9 6 3 2 1 '
    """
    n = a  # Compteur
    reponse = ""
    while n > 0:
        if a % n == 0:
            reponse += str(n) + " "
        n -= 1  # Décrémentation du compteur
    return reponse


def table_multiplication() -> str:
    """
    Retourne la table de multiplication des nombres de 1 à 10.
    """
    i = 1  # Compteur 1
    j = 1  # Compteur 2
    reponse = ""
    val_max = 10
    while i <= val_max:
        while j <= val_max:
            reponse += "{} ".format(i * j)
            j += 1
        reponse += "\n"
        i += 1
        j = 1
    return reponse


def plus_grand_plus_petit(nbre_valeurs: int) -> str:
    """
    Demande à l'utilisateur d'entrer nbre_valeurs valeurs et retourne une
    chaîne de caractères formée des deux valeurs max et min.
    """
    valeur = float(input("Entrez la valeur 1 : "))
    valeur_plus_grande = valeur
    valeur_plus_petite = valeur
    i = 2  # Compteur
    while i <= nbre_valeurs:
        valeur = float(input("Entrez la valeur {} : ".format(i)))
        if valeur > valeur_plus_grande:
            valeur_plus_grande = valeur
        elif valeur < valeur_plus_petite:
            valeur_plus_petite = valeur
        i += 1
    reponse = "max : {}, min : {}".format(valeur_plus_grande,
                                          valeur_plus_petite)
    return reponse


def moyenne(nbre_notes: int) -> float:
    """
    Demande nbre_notes notes à l'utilisateur et retourne la moyenne.
    """
    somme = 0  # Initialisation de la somme
    i = 1  # Compteur
    while i <= nbre_notes:
        note = float(input("Entrez la note {} : ".format(i)))
        somme += note
        i += 1
    return somme / nbre_notes


def moyenne_ter() -> str:
    """
    Demande des notes à l'utilisateur et retourne la moyenne. La saisie
    cesse lorsque la note entrée est négative.
    """
    somme = 0  
    nbre_notes = 0
    
    while True:
        note = float(input("Entrez la note {} : ".format(nbre_notes + 1)))
        if note < 0:
            break
        somme += note
        nbre_notes += 1
        
    reponse = "Nbre de notes : {}, moyenne : {:.2f}".format(nbre_notes,
                                                        somme / nbre_notes)
    return reponse


def loto_naif() -> str:
    """
    Retourne 6 entiers sélectionnés aléatoirement dans l'intervalle
    [1, 49].
    """
    import random
    
    reponse = ""
    i = 1   # Compteur
    nbre_boules = 6  # Valeur max du compteur
    
    while i <= nbre_boules:
        boule = random.randint(1, 49)
        reponse += "{} ".format(boule)
        i += 1  # Incrémentation du compteur
        
    return reponse


def devine() -> None:
    """
    Déterminer aléatoirement un nombre compris en 1 et 49 et demande à l'utilisateur
    de le deviner.
    La fonction affiche des messages qui aident l'utilisateur dans recherche et quitte
    dès que cette dernière est fructueuse.
    """
    import random
    nbre_a_deviner = random.randint(1, 50)
    
    nbre_tentatives = 0
    
    while True:
        nbre = int(input("Proposition n° {} : ".format(nbre_tentatives + 1)))
        nbre_tentatives += 1
        
        if nbre == nbre_a_deviner:
            print("Bravo, le nombre a été deviné en {} tentatives.".format(nbre_tentatives))
            break
        elif nbre > nbre_a_deviner:
            print("Trop grand !")
        else:
            print("Trop petit ! ")


def alphabet(sens: str) -> str:
    """
    Retourne les lettres de l'alphabet en fonction de la chaîne de caractères
    passée en argument.
    Les valeurs possibles pour cet argument sont 'croissant' ou 'decroissant'.
    """
    nbre_lettres = 26
    i = 1   # Compteur
    reponse = ""
    
    if sens == "croissant":
        indice = 97
    elif sens == "decroissant":
        indice = 122
    else:
        raise Exception("Il faut choisir 'croissant' ou 'decroissant'.")
                        
    while i <= nbre_lettres:
        reponse += chr(indice)
        if sens == "croissant":
            indice += 1
        else:
            indice -= 1
        i += 1
        
    return reponse


def fibo(n: int) -> str:
    """

    """
    if n == 1:
        reponse = "1"
    elif n == 2:
        reponse = "1 1"
    else:
        u = 1  # u_{n-2}
        v = 1  # u_{n-1}
        reponse = "1 1 "
        rang = 3
        while rang <= n:
            w = u + v  # u_{n}
            u = v  # Mise à jour de u_{n-2}
            v = w  # Mise à jour de u_{n-1}
            reponse += str(w) + " "
            rang += 1
    return reponse


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
