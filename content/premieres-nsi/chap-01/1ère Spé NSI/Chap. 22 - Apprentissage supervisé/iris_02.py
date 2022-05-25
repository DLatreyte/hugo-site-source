from mpl_toolkits.mplot3d import Axes3D

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def affichage(liste_echan, iris, titre, nom_fichier):
    """
    Construction des graphiques

    Paramètres
    ----------
    liste_echan : List[Dict]
        Liste de dictionnaires. Chaque dictionnaire représente un échantillon
        et possède les clés x, y, classe, indice.
    iris : Dict
        Dictionnaire qui représente un échantillon. Possède les clés x et y.
    titre : str
        Titre du graphique
    nom_fichier : str
        Nom du fichier image

    Retour
    ------
    None
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1, projection='3d')
    ax.set_title(titre)
    ax.set_xlabel("Longueur pétale (cm)")
    ax.set_ylabel("Largeur pétale (cm)")
    ax.set_zlabel("Longueur sépale (cm)")

    for echan in liste_echan:  # echan est un dictionnaire
        x = echan['x']
        y = echan['y']
        z = echan['z']
        
        if echan['classe'] == 'Iris-setosa':
            couleur = 'g'
        elif echan['classe'] == 'Iris-versicolor':
            couleur = 'r'
        else:
            couleur = 'b'
        ax.scatter(x, y, z, color=couleur)

    ax.scatter(iris['x'], iris['y'], iris['z'], color='black')

    ax.grid(True)
    plt.show()  # Sauf sur repl.it
    plt.savefig(nom_fichier)  # Sauvegarde


def calculs_distances(liste_echan, iris):
    """
    Calcule la distance entre chaque point de l'échantillon modèle et
    l'échantillon étudié. Ajoute cette distance à chaque dictionnaire de la
    liste echan_modeles.
    Retourne la liste echan_modeles.

    Paramètres
    ----------
    liste_echan : List[Dict]
        Liste de dictionnaires. Chaque dictionnaire représente un échantillon
        et possède les clés x, y, classe, indice.
    
    iris : Dict
        Dictionnaire qui représente un échantillon. Possède les clés x et y.

    Retour
    ------
    liste_echan : List[Dict]
        Liste de dictionnaires. Chaque dictionnaire représente un échantillon
        et possède les clés x, y, classe, indice, distance.
    """

    for echan in liste_echan:  # echan est un dictionnaire
        x1 = echan['x']
        y1 = echan['y']
        z1 = echan['z']
        x = iris['x']
        y = iris['y']
        z = iris['z']
        distance = np.sqrt( (x1 - x)**2 + (y1 - y)**2 + (z1 - z)**2 )
        echan['distance'] = distance
    
    return liste_echan


def k_plus_proches_voisins(echan_modeles_avec_distances, k):
    """
    Construit la liste des k échantillons plus proches voisins.
    
    Paramètres
    ----------
    echan_modeles_avec_distances : List[Dict]
        Liste de dictionnaires. Chaque dictionnaire représente un échantillon
        et possède les clés x, y, classe, indice, distance.
    k : int
        Nombre de plus proches voisins à prendre en compte.
        
    Retour
    ------
    plus_proches_voisins : List[Dict]
        Liste de longueur k, composée des dictionnaires représentant les k
        échantillons les plus proches de l'échantillon testé.
    """
    # tri de la liste portant sur les premiers élements de chaque Tuple
    plus_proches_voisins = sorted(echan_modeles_avec_distances,
                                  key=lambda x: x['distance'])  
    
    # on considère le cas où le nombre d'éléments de la liste est inférieur à k
    if k < len(plus_proches_voisins):
        return plus_proches_voisins[ : k]
    else:
        return plus_proches_voisins


def creation_echan(x, y, z, classe):
    """
    À partir des listes des coordonnées et des étiquettes des échantillons
    création d'une liste de dictionnaires d'échantillons.

    Paramètres
    ----------
    x : list[float]
        Liste des abscisses des points de l'échantillon de test.
    y : list[float]
        Liste des ordonnées des points de l'échantillon de test.
    z : list[float]
        Liste des altitudes des points de l'échantillon de test.
    classe : List[str]
        Liste des étiquettes de l'échantillon de test.

    Retour
    ------
    echantillons : List[Dict]
        Liste des dictionnaires représentant les échantillons.
        Chacun des échantillons est un dictionnaire possédant les clés
        x, y, indice, classe.
    """
    echantillons = []

    for i in range(len(x)):
        echan = {}
        echan['x'] = x[i]
        echan['y'] = y[i]
        echan['z'] = z[i]
        echan['classe'] = classe[i]
        echan['indice'] = i
        
        echantillons.append(echan)

    return echantillons


def determination_classe(liste_voisins_plus_proches):
    """
    Détermine la classe probable de l'échantillon testé. Cette classe est
    celle qui apparait le plus souvent dans la liste des plus proches
    voisins.
    
    Paramètre
    ---------
    liste_voisins_plus_proches : List[Dict]
        Liste des dictionnaires représentant les voisins les plus proches.
    
    Retour 
    ------
    classe_test : str
        Classe probable de l'échantillon testé.
    """
    frequences = {}  # nbre d'apparitions de chaque classe
    
    for echan in liste_voisins_plus_proches:
        classe = echan['classe']
        if classe not in frequences:
            frequences[classe] = 1
        else:
            frequences[classe] += 1
    
    freq = 0  # initialisation de la variable pour la boucle
    classe_test = None  # initialisation de la variable pour le nom
    for classe in frequences:
        if frequences[classe] > freq:
            classe_test = classe

    return classe_test



def main():
    iris = pd.read_csv("iris.csv", sep=";", header=0)
    print(iris.head())
    
    # Transformation des séries Pandas en listes
    x = iris.loc[:, 'Longueur pétale (cm)'].tolist()
    y = iris.loc[:, 'Largeur pétale (cm)'].tolist()
    z = iris.loc[:, 'Longueur sépale (cm)'].tolist()

    classe = iris.loc[:, 'Classe'].tolist()
    
    # Liste des échantillons
    echan_modeles = creation_echan(x, y, z, classe)
    #print(echan_modeles)

    # Échantillon
    iris = {'x' : 4.5, 'y' : 2, 'z' : 6}
    
    # Affichage des échantillons de test et de l'échantillon étudié
    affichage(echan_modeles, iris, "Représentation graphique des données",
             "Echantillons.svg")

    # Calcul des distances
    echan_modeles_avec_distances = calculs_distances(echan_modeles, iris)
    #print(echan_modeles_avec_distances)

    # Détermination des k plus proches voisins
    k = 10
    voisins = k_plus_proches_voisins(echan_modeles_avec_distances, k)

    affichage(voisins, iris, "{} plus proches voisins".format(k),
             "Voisins_proches.svg")

    classe_iris = determination_classe(voisins)
    print("Classe probable de l'échantillon testé : {}".format(classe_iris))

main() 
