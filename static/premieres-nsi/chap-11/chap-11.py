"""
Chiffrement de César. L'algorithme utilisé permet d'envisager un
décalage positif de n'importe quelle valeur.
"""
import string


def chiffrement(chaine: str, decalage: int) -> str:
    """
    Fonction qui réalise le chiffrement de la chaîne passée en argument.
    """
    chaine_reference = string.ascii_lowercase
    liste_car_chiffres = []
    modulo = 26

    for car in chaine:  # pour chaque caractère de la chaîne non chiffrée
        indice_car = chaine_reference.index(car)  # On récupère l'indice du caractère
        nouvel_indice = indice_car + decalage     # On applique le décalage

        nouvel_indice = nouvel_indice % modulo    # On ramène la valeur dans le bon intervalle

        liste_car_chiffres.append(chaine_reference[nouvel_indice])

    chaine_chiffree = "".join(liste_car_chiffres)
    return chaine_chiffree


def dechiffrement(chaine: str, decalage: int) -> str:
    """
    Fonction qui réalise le déchiffrement de la chaîne passée en argument.
    """
    return chiffrement(chaine, -decalage)


def main():
    reponse_coherente = False

    while not reponse_coherente:
        action = input("Que voulez-vous faire, chiffrer (c) ou déchiffrer (d) ? : ")
        if action == 'c':
            chaine = input("Quelle chaîne voulez-vous chiffrer ? ")
            decalage = int(input("Quel décalage voulez-vous opérer ? "))
            chaine_chiffree = chiffrement(chaine, decalage)
            print("Chaîne de départ : {}, décalage : {}, chaîne chiffrée : {}".format(
                                                                                chaine,
                                                                                decalage,
                                                                                chaine_chiffree))
            reponse_coherente = True

        elif action == 'd':
            chaine_chiffree = input("Quelle chaîne voulez-vous déchiffrer ? ")
            decalage = int(input("Quel décalage a été appliqué lors du chiffrement ? "))
            chaine = dechiffrement(chaine_chiffree, decalage)
            print("Chaîne chiffrée : {}, décalage : {}, chaîne déchiffrée : {}".format(
                                                                                chaine_chiffree,
                                                                                decalage,
                                                                                chaine))
            reponse_coherente = True

        else:
            print("Demande incohérente...")


main()