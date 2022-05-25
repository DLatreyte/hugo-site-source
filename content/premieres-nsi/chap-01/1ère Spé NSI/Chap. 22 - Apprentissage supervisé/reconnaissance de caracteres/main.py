"""
Reconnaissance de caractères par la méthode des k plus proches voisins
"""

import numpy as np
import pandas as pd


def creation_echantillons(ensemble, ligne_debut, ligne_fin, nbre_col):
    """
    Création d'une liste d'échantillons. Chaque échantillon est un dictionnaire dont 
    certaines clés sont numériques (les numéros des pixels) avec pour valeur l'intensité
    lumineuse et une dernière clé est la chaîne de caractères 'chiffre'.

    Paramètres
    ----------
    ensemble : pandas data frame
        Ensemble des échantillons
    ligne_debut : int
        À partir de quelle ligne considère-t-on les échantillons.
    ligne_fin : int
        Dernière ligne que l'on prend en compte.
    nbre_col : int
        Nombre de colonnes à prendre en compte.int
    
    Retour
    ------
    echantillons : List[Dict]
        Liste des échantillons pris en compte.
        Chaque échantillon est un dictionnaire dont dont certaines clés sont numériques
        (les numéros des pixels) et une dernière est une chaîne de caractères 'chiffre'.
    """
    echantillons = []
    for i in range(ligne_debut, ligne_fin + 1):
        echantillon = {}
        for j in range(nbre_col):
            if j != nbre_col - 1:
                echantillon[j] = ensemble.iloc[i, j]
            else:
                echantillon['chiffre'] = str(ensemble.iloc[i, j])
        echantillons.append(echantillon)
    return echantillons


def calculs_distances(modeles, test):
    """
    Calcule les distances de chaque entrée du modèle à l'entrée test.
    
    Paramètres
    ----------
    modeles : List[Dict]
        Chaque dictionnaire représente un échantillon du modèle
        et possède les clés numériques 0, 1, ..., 64 et la clé classe.
    
    test : Dict
        Dictionnaire qui représente un échantillon. 
        Possède les clés numériques 0, 1, ..., 64, et la clé classe.

    Retour
    ------
    modeles : List[Dict]
        Chaque dictionnaire représente un échantillon du modèle
        et possède les clés numériques 0, 1, ..., 64 et les clés classe et distance.
    """
    for echantillon in modeles:  # echantillon est un dictionnaire
        carre_distance = 0
        for i in range(len(echantillon) - 2):
            carre_distance += (echantillon[i] - test[i])**2
        echantillon['distance'] = np.sqrt(carre_distance)
        
    return modeles


def k_plus_proches_voisins(modeles_avec_distances, k):
    """
    Construit la liste des k échantillons plus proches voisins.
    
    Paramètres
    ----------
    modeles_avec_distances : List[Dict]
        Chaque dictionnaire représente un échantillon du modèle
        et possède les clés numériques 0, 1, ..., 64 et les clés classe et distance.
    k : int
        Nombre de plus proches voisins à prendre en compte.
        
    Retour
    ------
    plus_proches_voisins : List[Dict]
        Liste de longueur k, composée des dictionnaires représentant les k
        échantillons les plus proches de l'échantillon testé.
    """
    # tri de la liste portant sur les premiers élements de chaque Tuple
    plus_proches_voisins = sorted(modeles_avec_distances,
                                  key=lambda x: x['distance'])  
    
    return plus_proches_voisins[ : k]


def determination_classe(voisins):
    """
    Détermine la classe probable de l'image de test. La classe de cette
    image est celle qui apparait le plus souvent dans la liste des plus 
    proches voisins.
    
    Paramètre
    ---------
    voisins : List[Dict]
        Liste des dictionnaires représentant les voisins les plus proches.
    
    Retour 
    ------
    classe : str
        Classe probable de l'échantillon testé.
    """
    classes = {}  # clés : classes, valeurs : nbre d'apparitions
    
    for echantillon in voisins:         # echantillon est un dictionnaire
        classe = echantillon['chiffre']  # on récupère la classe
        if classe not in classes:       # on incrémente sa valeur
            classes[classe] = 1
        else:
            classes[classe] += 1
    
    val_max = 0                        # initialisation du nombre d'apparitions
    nom_classe = None                  # initialisation du nom de la classe à conserver
    for classe in classes:
        if classes[classe] > val_max:
            val_max = classes[classe]
            nom_classe = classe

    return nom_classe


def main():
    # Ouverture du fichier contenant les données
    images = pd.read_csv("./digits.csv", sep=",", header=0)
    #print(images.tail())

    # Création des deux sous-ensembles : modeles et tests
    modeles = creation_echantillons(images, 0, 1780, 65)
    tests = creation_echantillons(images, 1781, 1796, 65)
    
    # Choix d'une image et calcul des distances
    image = tests[0]  # image est un dictionnaire
    modeles_avec_distances = calculs_distances(modeles, image)
    #print(modeles_avec_distances[0])
    
    # Détermination des k plus proches voisins
    k = 5
    voisins = k_plus_proches_voisins(modeles_avec_distances, k)
    #print(voisins)
    
    # détermination de la classe
    chiffre_devine = determination_classe(voisins)
    print("Chiffre deviné : {}".format(chiffre_devine))
    print("Chiffre réel : {}".format(image['chiffre']))


main()
