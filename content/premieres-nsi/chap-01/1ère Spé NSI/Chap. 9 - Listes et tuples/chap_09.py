from typing import List, Tuple

def exo2(liste: List[float]) -> Tuple[float]:
    """
    Détermine l'élément le plus grand de la liste de floats passée
    en argument.
    """
    return max(liste), min(liste)

from typing import List, Tuple
import random

from typing import List
import random

def loto() -> List[int]:
    """
    Simule le tirage du Loto. retourne une liste de 6 entiers compris
    entre 1 et 49.
    """
    numeros = []
    nbre_valeurs = 6
    val_min = 1
    val_max = 49

    nbre_elements = 0
    while nbre_elements <= nbre_valeurs:
        numero = random.randint(val_min, val_max)
        if numero not in numeros:
            numeros.append(numero)
            nbre_elements += 1

    return numeros


from typing import List

def moyenne(liste_notes: List[float]) -> float:
    """
    Détermine la moyenne des notes reçues en argument dans la
    liste passée en argument.
    """
    return sum(liste_notes) / len(liste_notes)


def nombre_dans_intervalle(liste: List[float], valeur_min: float,
                           valeur_max: float) -> float:
    """
    Détermine le nombre de valeurs de liste comprises dans l'intervalle
    [val_min, val_max].
    """
    nbre = 0
    
    for valeur in liste:
        if valeur >= valeur_min and valeur <= valeur_max:
            nbre += 1
    
    return nbre


def statistiques(notes: List[float]) -> Tuple[float]:
    """
    Détermine les statistiques des notes reçues en argument : moyenne
    et notes comprises dans les intervalles [0, moy - 3], [moy - 3, moy + 3],
    [moy + 3, 20]
    """
    note_moyenne = moyenne(notes)
    intervalle_inf = nombre_dans_intervalle(notes, 0, note_moyenne - 3)
    intervalle_mid = nombre_dans_intervalle(notes, note_moyenne - 3, note_moyenne + 3)
    intervalle_sup = nombre_dans_intervalle(notes, note_moyenne + 3, 20)
    
    return (note_moyenne, intervalle_inf, intervalle_mid, intervalle_sup)


from typing import Tuple
import math as m


def distance(pt1: Tuple[float], pt2: Tuple[float]) -> float:
    """
    Détermine la distance entre les points pt1 et pt2.
    ERREUR si les dimensions des tuples ne correspondent pas.
    """
    if len(pt1) != len(pt2):
        raise Exception("Les dimensions des tuples ne correspondent pas.")
    
    distance_carre = 0
    for i in range(len(pt1)):
        distance_carre += (pt1[i] - pt2[i])**2
    
    return m.sqrt(distance_carre)
    