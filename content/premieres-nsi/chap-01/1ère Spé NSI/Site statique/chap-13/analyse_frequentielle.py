from typing import List, Dict, Sequence
import string


def affichage_dict(dic_car: Dict[str, float]) -> None:
    """
    Affichage du contenu d'un dictionnaire classé en fonction des valeurs,
    de la plus grande à la plus petite.
    """
    liste_couples = []
    for cle in dic_car.keys():
        liste_couples.append((cle, dic_car[cle]))
    for couple in sorted(liste_couples, key=lambda c: c[1], reverse=True):
        print("{} : {}".format(couple[0], couple[1]))


def creation_liste_cles_triees(dic_car: Dict[str, float]) -> List[str]:
    """
    Tri des clés de dic_car par ordre décrossant et créatio d'une liste contenant
    les clés.
    """
    liste_couples = []
    for cle in dic_car.keys():
        liste_couples.append((cle, dic_car[cle]))
    
    liste_cles_triees = []
    for couple in sorted(liste_couples, key=lambda c: c[1], reverse=True):
        liste_cles_triees.append(couple[0])
        
    return liste_cles_triees


def analyse_dict_car(dict_car: Dict[str, int]) -> Dict[str, float]:
    """
    Création d'un dictionnaire des caractères présents, comme clés, dans le
    dictionnaire dict_car et dont les valeurs représentent les fréquences
    d'apparition de ces caractères.
    """
    dict_frequences = {}

    nbre_car = 0
    for nbre in dict_car.values():
        nbre_car += nbre

    for cle in dict_car.keys():
        dict_frequences[cle] = dict_car[cle] / nbre_car * 100

    return dict_frequences


def creation_dict_car(liste_car: List[str]) -> Dict[str, str]:
    """
    Création d'un dictionnaire dont les clés sont les caratères présents dans
    la liste liste_car et dont les valeurs sont les nombres de fois que ces
    caractères sont présents.
    """
    dict_car = {}
    for car in liste_car:
        if car in dict_car.keys():
            dict_car[car] += 1
        else:
            dict_car[car] = 1
    return dict_car


def transformation_minuscules(liste_car: List[str]) -> List[str]:
    """
    Transforme toutes les minuscules de la liste liste_car en majuscules.
    """
    for i in range(len(liste_car)):
        if liste_car[i].islower():
            liste_car[i] = liste_car[i].upper()
    return liste_car


def trouve_indice(car: str, seq: Sequence) -> int:
    """
    Détermine le premier indice du caractère car dans liste.
    On suppose que car appartient à la liste.
    
    Ainsi trouve_indice('a', "jkhdsalkj") retourne 5.
    """
    indice = 0
    for elt in seq:
        if car == elt:
            return indice
        indice += 1


def transformation_accents(liste_car: List[str]) -> List[str]:
    """
    Transforme chaque caractère accentué en son équivalent sans accent.
    """
    accents = "âãàéèêëïîôôùüûÂÁÀÃÉÈËÊÎÏÔOÕõÙÜÛçÇÑñń"
    equivalents = "aaaeeeeiioouuuAAAAEEEEIIOOOOUUUcCNnn"

    for i in range(len(liste_car)):
        if liste_car[i] in accents:
            indice_car = trouve_indice(liste_car[i], accents)
            nouveau_car = equivalents[indice_car]
            liste_car[i] = nouveau_car
    return liste_car


def suppression_chiffres(liste_car: List[str]) -> List[str]:
    """
    Supprime tous les caractères invisibles dans la liste.
    """
    i = 0
    while i < len(liste_car):
        if liste_car[i] in string.digits:
            del liste_car[i]
            continue
        i += 1
    return liste_car


def suppression_blancs(liste_car: List[str]) -> List[str]:
    """
    Supprime tous les caractères invisibles dans la liste.
    """
    i = 0
    while i < len(liste_car):
        if liste_car[i] in string.whitespace:
            del liste_car[i]
            continue
        i += 1
    return liste_car


def suppression_ponctuation(liste_car: List[str]) -> List[str]:
    """
    Supprime tous les caractères de ponctuation dans la liste.
    """
    ponctuations = string.punctuation + "«»°"
    i = 0
    while i < len(liste_car):
        if liste_car[i] in ponctuations:
            del liste_car[i]
            continue
        i += 1
    return liste_car


def nettoyage(liste_car: List[str]) -> List[str]:
    """
    Supprime tous les caractères de ponctuation, les blancs et les chiffres
    dans la liste.
    """
    a_supprimer = string.punctuation + "«»°" + string.whitespace + string.digits
    i = 0
    while i < len(liste_car):
        if liste_car[i] in a_supprimer:
            del liste_car[i]
            continue
        i += 1
    return liste_car


def extraction_caracteres(nom_fichier: str) -> List[str]:
    """
    Ouvre le fichier nom_fichier, extrait l'ensemble des caractères
    sous forme d'une unique chaîne de caractères puis crée une liste 
    dont chaque élément est un caractère présent dans le texte initial.
    """
    with open(nom_fichier, 'r', encoding='utf-8-sig') as f:
        chaine_contenu = f.read()
    return list(chaine_contenu)


def main():
    """ Fonction principale qui appelle toutes les autres. """
    
    # Création du dictionnaire de référence
    roman = "la-jangada.txt"
    #     fichier_test = "texte-de-test.txt"
    liste_caracteres_ref = extraction_caracteres(roman)
    liste_caracteres_ref = nettoyage(liste_caracteres_ref)
    liste_caracteres_ref = transformation_accents(liste_caracteres_ref)
    liste_caracteres_ref = transformation_minuscules(liste_caracteres_ref)

    dict_car_ref = creation_dict_car(liste_caracteres_ref)
    dict_car_ref = analyse_dict_car(dict_car_ref)
#     print(dict_car_ref)
    
#     affichage_dict(dict_car_ref)
    liste_cles_ref = creation_liste_cles_triees(dict_car_ref)
    print("----------------------------------------")
    print(liste_cles_ref)

    # Analyse du texte chiffré
    texte = "texte-chiffre.txt"
    liste_caracteres_chif = extraction_caracteres(texte)
    liste_caracteres_chif = nettoyage(liste_caracteres_chif)
    
    dict_car_chif = creation_dict_car(liste_caracteres_chif)
    dict_car_chif = analyse_dict_car(dict_car_chif)
#     print(dict_car_chif)
    print("----------------------------------------")
#     affichage_dict(dict_car_chif)
    print("----------------------------------------")
    liste_cles_chif = creation_liste_cles_triees(dict_car_chif)
    print(liste_cles_chif)

main()

