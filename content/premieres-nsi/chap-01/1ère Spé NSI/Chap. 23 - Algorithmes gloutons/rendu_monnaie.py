"""
Mise en œuvre de la stratégie gloutonne pour le
problème du rendu de monnaie.
Utilisation de l'opérateur modulo.
"""
from typing import List


def somme_a_rendre(prix: int, montant_client: int) -> int:
    """
    Détermine la somme à rendre à partir du prix et du montant donné par
    le client.
    """
    return montant_client - prix


def pieces_a_rendre(somme: int, pieces: List[int]) -> List[int]:
    """
    Détermine les pièces (et leur nombre) à choisir pour rendre la somme
    passée en argument.
    """
    a_rendre = []
    indice_piece = len(pieces) - 1
    while indice_piece >= 0:
        rendu = somme // pieces[indice_piece]
        encore_a_rendre = somme % pieces[indice_piece]
        a_rendre.insert(0, rendu)
        somme = encore_a_rendre
        indice_piece -= 1
    return a_rendre


def main():
    # valeurs des pièces
    pieces = [1, 2, 5, 10, 20, 50, 100]

    prix = int(input("Quel est le prix ? "))
    client = int(input("Combien le client donne-t-il ? "))

    a_rendre = somme_a_rendre(prix, client)
    comment = pieces_a_rendre(a_rendre, pieces)

    reponse = ["{} piece(s) de {}".format(comment[i], pieces[i]) for i in range(len(pieces))]
    print("Je dois rendre : {}".format(a_rendre))
    print("Je donne donc : {}".format(reponse))


main()