from math import pow, sqrt, pi


def retire_un(n: float) -> float:
    """ Retourne la valeur de n - 1 """
    return n - 1


def polynomiale(a:int, b:int, c:int, d:int, x: float) -> float:
    """
    Retourne la valeur ax^3 + bx^2 + cx + d
    
    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
    return a * pow(x, 3) + b * pow(x, 2) + c * x + d


def polynomiale_carre(a:int, b:int, c:int, x: float) -> float:
    """
    Retourne la valeur ax^4 + bx^2 + c
    
    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
    return a * pow(x, 4) + b * pow(x, 2) + c


def somme(x:float, y: float, z: float) -> float:
    """
    Retourne la somme des trois nombres passés en argument.
    """
    return x + y + z


def moyenne(a: float, b: float, c: float) -> float:
    """
    Retourne la moyenne des trois nombres passés comme arguments.
    """
    return somme(a, b, c) / 3


def moyenne_ponderee(x:float, y:float, z:float, a:int, b:int, c:int) -> float:
    """
    Retourne la moyenne pondérée des nombres x, y et z par les coefficients
    a, b et c.
    
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 1)
    10.0
    
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 0)
    7.5
    """
    return somme(a * x, b * y, c * z) / somme(a, b, c)


def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Retourne la distance dans le plan entre les deux points de coordonnées
    (x1, y1) et (x2, y2).
    
    >>> distance(0, 0, 1, 1)
    1.4142135623730951
    """
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))


def surface_rectangle(a: float, b: float) -> float:
    """ Détermine la surface du rectangle de côtés a et b. """
    return a * b


def volume_parallelepipede(a: float, b: float, h: float) -> float:
    """ Retourne le volume du parallélépipède rectangle de côtés a, b et de
    hauteur h. """
    return surface_rectangle(a, b) * h


def surface_disque(r: float) -> float:
    """ Returne la surface du disque de rayon r. """
    return pi * pow(r, 2)


def surface_couronne(r1: float, r2: float) -> float:
    """
    Retourne la surface de la couronne comprise entre les rayons r1
    et r2.
    """
    return surface_disque(r2) - surface_disque(r1)


def volume_tube(r1, r2, l) -> float:
    """ Retourne le volume de la partie pleine d'un tube de longueur l, dont
    la section est une couronne de rayon intérieur r1 et de rayon extérieur
    r2. """
    return surface_couronne(r1, r2) * l


from random import random

def tirage_entier(a: int) -> int:
    """
    Retourne un nombre entier aléatoire compris entre 1 et a (inclus).
    """
    return int(random() * a + 1)

