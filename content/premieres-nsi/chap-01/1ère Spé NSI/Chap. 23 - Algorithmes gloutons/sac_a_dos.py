"""
Problème du sac à dos.
---------------------
Situation : on considère un sac à dos de capacité maximale 40 kg et on cherche 
à y ranger, parmi les objets proposés, ceux qui permettront de maximiser la valeur
transportée.

Objet   | A   | B   | C   | D   | E   | F   |
Masse   | 13  | 12  | 8   | 10  |14   | 18  |
Valeur  | 700 | 500 | 200 | 300 | 600 | 800 |
"""
from typing import List, Dict, Tuple


def tri_objets(objets: List[Dict]) -> List[Dict]:
    """
    Tri la liste de dictionnaires selon les rapports valeur/masse.
    """
    def recupere_rapports(objet):
        return objet['valeur'] / objet['masse']

    objets_tries = sorted(objets, key=recupere_rapports)

    return objets_tries


def constrution_sac_a_dos(objets_tries: List[Dict], masse_max: float) -> Tuple[List[str], int, int]:
    """
    Construction du sac à dos à partir d'une stratégie gloultonne.
    HYPOTHÈSE : la liste de dictionnaires est triée par ordre croissant des rapports
    valeurs/masses.

    Retourne un tuple constitué d'une liste contenant les noms des objets sélectionnés, 
    de la valeur du sac à dos et de la masse du sac à dos.
    """
    masse_sac = 0
    valeur = 0
    liste_objets = []

    i = len(objets_tries) - 1  # Compteur
    while i >= 0:
        objet = objets_tries[i]  # objet est un dictionnaire
        if (masse_sac + objet['masse']) <= masse_max:
            valeur += objet['valeur']
            masse_sac += objet['masse']
            liste_objets.append(objet['nom'])
    
        i -= 1  # Décrémentation du compteur

    return (liste_objets, valeur, masse_sac)


def combinaisons(objets: List[Dict]) -> List[List]:
    """
    Liste de toutes les combinaisons possibles d'objets sans prise en compte des
    contraintes.
    2^n combinaisons sont possibles où n est le nombre d'objets.
    """
    liste = [[] for i in range(2**len(objets))]
    print(len(liste))

    for i in range(len(objets)):               # Itération sur tous les objets
        for j in range(len(liste)):  # Itération sur toutes les listes
            for k in range(0, 2**i):
                liste[i].append(objets[i]['nom'])   
            for k in range(0, 2**i):
                continue

    return liste   


def main():
    # Définition des objets
    objets = [{'nom': 'A', 'masse': 13, 'valeur': 700},
              {'nom': 'B', 'masse': 12, 'valeur': 500},
              {'nom': 'C', 'masse': 8, 'valeur': 200},
              {'nom': 'D', 'masse': 10, 'valeur': 300},
              {'nom': 'E', 'masse': 14, 'valeur': 600},
              {'nom': 'F', 'masse': 18, 'valeur': 800}
              ]

    # Masse maximale transportable
    masse_max = 40

    # Tri de la liste des objets par ordre croissant des rapports valeurs/masses
    objets = tri_objets(objets)
    print("Objets utilisables : {}".format(objets), end='\n')

    # construction du sac à dos par stratégie gloutonne
    sac_a_dos, valeur, masse_sac = constrution_sac_a_dos(objets, masse_max)

    # Conclusion de la mise en œuvre de la stratégie gloutonne
    print("Stratégie gloutonne")
    print("-------------------")
    print("Constitution du sac à dos : {}".format(sac_a_dos))
    print("Masse du sac à dos : {}".format(masse_sac))
    print("Valeur du sac à dos : {}".format(valeur))
    print()

    # Exploration systématique (recherche par force brute)
    # Liste des combinaisons possibles sans contrainte
    liste_combinaisons = combinaisons(objets)
    print(liste_combinaisons)



main()
