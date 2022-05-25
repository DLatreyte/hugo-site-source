def est_positif(x: float) -> bool:
    """ Retourne True si x est positif ou nul, False sinon. """
    return x >= 0


def est_egal(x: float, y: float) -> bool:
    """
    Retourne True si abs(x - y) < epsilon où epsilon = 1e-5.
    
    >>> est_egal(1 / 49 * 49, 1)
    True
    """
    epsilon = 1e-5
    return abs(x - y) < epsilon


def est_pair(n: int) -> bool:
    """ Retourne True si n est un nombre pair, False sinon. """
    return n % 2 == 0


def est_entier(n: int) -> bool:
    """ Détermine si n est un nombre entier. """
    return isinstance(n, int)


def est_naturel(n: int) -> bool:
    """
    Détermine si un nombre entier est un entier naturel.
    
    >>> est_naturel(5)
    True
    >>> est_naturel(-5)
    False
    """
    return est_entier(n) and est_positif(n)


def est_naturel_2(n: int) -> bool:
    """
    Détermine si un nombre entier est un entier naturel.
    ERREUR si n n'est pas un nombre.
    
    >>> est_naturel(5)
    True
    >>> est_naturel(-5)
    False
    >>> est_naturel_2("coucou")
    Traceback (most recent call last):
    ...
    TypeError: n n'est pas un nombre !!!
    """
    if not (isinstance(n, int) or isinstance(n, float)):
        raise TypeError("n n'est pas un nombre !!!")
    
    return est_naturel(n)


def est_plus_grand(x: float, y: float) -> bool:
    """ Retourne True si x > y, False sinon. """
    return x > y


def le_plus_grand(x: float, y: float) -> float:
    """ Retourne x si x > y, y sinon. """
    if est_plus_grand(x, y):
        return x
    else:
        return y


def valeur_absolue(x: float) -> float:
    """ Retourne la valeur absolue de x. """
    if est_positif(x):
        return x
    else:
        return -x


def est_bissextile(n: int) -> bool:
    """ Retourne True si l'année n est bissextile, False sinon. """
    pass


if __name__ == "__main__":
    import doctest
    doctest.testmod()