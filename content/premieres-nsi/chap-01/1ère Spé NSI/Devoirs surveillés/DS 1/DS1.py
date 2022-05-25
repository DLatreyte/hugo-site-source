import math as m


def aire_triangle(a: float, b: float, c: float) -> float:
    """
    Détermine l'aire du triangle par la méthode trouvée dans le vieux livre
    de mathématiques.
    
    >>> aire_triangle(2, 4, 4)
    3.872983346207417
    """
    s = (a + b + c) / 2
    return m.sqrt(s * (s - a) * (s - b) * (s - c))


def prix_timbre(masse: float, type: str) -> float:
    """
    Retourne le prix du timbre poste en fonction du type de la lettre et de sa
    masse.
    Retourne -1 si la masse est supérieure à 100 g.

    >>> prix_timbre(20, "Lettre prioritaire")
    0.6
    >>> prix_timbre(38, "Ecopli")
    0.78
    >>> prix_timbre(138, "Ecopli")
    -1
    >>> prix_timbre(95, "Lettre verte")
    1.4
    """
    if (masse <= 20) and (type == "Lettre verte"):
        prix = 0.57
    elif (masse <= 20) and (type == "Lettre prioritaire"):
        prix = 0.60
    elif (masse <= 20) and (type == "Ecopli"):
        prix = 0.55
    elif (masse <= 20) and (type == "Lettre verte"):
        prix = 0.95
    elif (masse <= 50) and (type == "Lettre prioritaire"):
        prix = 1.
    elif (masse <= 50) and (type == "Ecopli"):
        prix = 0.78
    elif (masse <= 100) and (type == "Lettre verte"):
        prix = 1.4
    elif (masse <= 100) and (type == "Lettre prioritaire"):
        prix = 1.45
    elif (masse <= 100) and (type == "Ecopli"):
        prix = 1.0
    else:
        prix = -1
    
    return prix



def factorielle(n: int) -> int:
    """
    Détermine la factorielle du nombre n.
    
    >>> factorielle(3)
    6
    >>> factorielle(10)
    3628800
    """
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


def sinus(x: float, N: int) -> float:
    """
    Détermine le développement en série de la fonction sinus en x.
    
    >>> sinus(3.1416/2, 10)
    0.9999999999932534
    >>> sinus(0, 10)
    0.0
    """
    sinus = 0
    n = 0
    
    while True:    
        sinus += (-1)**n * x**(2 * n + 1) / factorielle(2 * n + 1)
        
        if n == N:
            break
        else:
            n += 1
    
    return sinus
            


if __name__ == '__main__':
    import doctest
    doctest.testmod()