def moyenne(a: float, b: float) -> float:
    """
    Calcule et retourne la moyenne des deux nombres a et b
    passés en argument.

    >>> moyenne(12, 16)
    14.0
    >>> moyenne(0, 8)
    4.0
    """
    return (a + b) / 2


def valeur_absolue(x: float) -> float:
    """
    Calcule et retourne la valeur absolue du nombre x positif
    passé en argument.

    >>> valeur_absolue(3)
    3
    >>> valeur_absolue(0)
    0
    >>> valeur_absolue(-3)
    3
    """
    if x >=0 :
        return x
    else:
        return -x


def puissance(x: float, n: int) -> float:
    """
    calcule et retourne le résultat de x à la puissance entière n :
    x^n = x . x . x . ... . x (n fois)

    >>> puissance(2, 8)
    256
    >>> puissance(0, 2)
    0
    >>> puissance(3, 0)
    1
    """
    res = 1
    for i in range(1, n + 1):
        res *= x
    return res


def amelioration_essai(essai: float, x: float) -> float:
    """
    Calcule et retourne la moyenne des nombres essai (strictement positif) et x/essai.

    >>> amelioration_essai(1, 2)
    1.5
    >>> amelioration_essai(2, 1)
    1.25
    """
    return moyenne(essai, x/essai)


def est_suffisamment_bon(essai: float, x: float) -> float:
    """
    Retourne True si la valeur absolue de la différence du carré du nombre essai
    et du nombre x est inférieure à une tolérance donnée (prendre 0.001).
    Retourne False sinon.

    >>> est_suffisamment_bon(1.9, 4)
    False
    >>> est_suffisamment_bon(1.999, 4)
    False
    >>> est_suffisamment_bon(1.9999, 4)
    True
    """
    tolerance = 0.001

    return valeur_absolue(puissance(essai, 2) - x) < tolerance


def test(essai: float, x: float) -> float:
    """
    Retourne la racine carrée du nombre x. Le calcul est effectué grâce à un
	raisonnement itératif depuis une première valeur strictement positive notée
	essai.

    >>> test(2, 4)
    2
    >>> test(1, 4)
    2.0000000929222947
    >>> test(7, 4)
    2.0000000271231317
    """
    while not est_suffisamment_bon(essai, x):
        essai = amelioration_essai(essai, x)
    return essai


def racine_carree(x: float) -> float:
    """
    Retourne le résultat de l'appel de la fonction test avec la valeur 1 pour l'argument essai.

    >>> racine_carree(4)
    2.0000000929222947
    >>> racine_carree(9)
    3.00009155413138
    >>> racine_carree(16)
    4.000000636692939
    """

    return test(1, x)


def main():
    return [racine_carree(i) for i in range(1, 100) if i % 2 == 0]


if __name__ == "__main__":
    import doctest
    doctest.testmod()