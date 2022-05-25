def kelvin_vers_celsius(t: float) -> float:
    """
    Convertit la température donnée en kelvin en une température θ
    en degrés celsius. Relation : θ = t - 273.15.
    ERREUR si t est négative.
    
    >>> kelvin_vers_celsius(0)
    -273.15
    >>> kelvin_vers_celsius(273.15)
    0.0
    >>> kelvin_vers_celsius(-5)
    Traceback (most recent call last):
    ...
    ValueError: Température en kelvin doit être positive !
    """
    if t < 0:
        raise ValueError("Température en kelvin doit être positive !")
    
    offset = -273.15
    return t + offset


def est_egal(a: float, b: float) -> bool:
    """
    Teste l'égalité de 2 floats.
    epsilon = 1e-7
    
    >>> est_egal(0, 0.0)
    True
    >>> est_egal(1/49*49, 1)
    True
    """
    epsilon = 1e-7
    return abs(a - b) <= epsilon


def inverse(x: float) -> float:
    """
    Retourne l'inverse du nombre x.
    ERREUR si x est nul.
    
    >>> inverse(0)
    Traceback (most recent call last):
    ...
    ZeroDivisionError: Division par 0 !!!
    
    >>> inverse(5)
    0.2
    """
    if est_egal(x, 0):
        raise ZeroDivisionError("Division par 0 !!!")
    return 1 / x



if __name__ == "__main__":
    import doctest
    doctest.testmod()