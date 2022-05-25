"""
Carnet d'adresse.
"""
from typing import Dict, List, Tuple


def affichage(carnet: List[Dict]) -> None:
    """
    Affichage du contenu du carnet.
    """
    for membre in carnet:
        for cle in membre.keys():
            print("{} : {}".format(cle, membre[cle]), end="\t\t")
        print("\n")


def nouvelle_entree(carnet: List[Dict], cles: List[str]) -> List[Dict]:
    """
    Création d'une nouvelle entrée dans le carnet d'adresse. Chaque élément de la liste
    est un dictionnaire renfermant les informations du carnet.
    Les informations à stocker sont contenues dans la liste cles.
    """
    print("Création d'une entrée dans le carnet d'adresse.")
    
    infos = {}
    
    for cle in cles:
        info = input("{} : ".format(cle))
        infos[cle] = info
    
    carnet.append(infos)
    return carnet


def recherche(carnet: List[Dict]) -> None:
    """
    Recherche dans le carnet d'adresse.
    """
    nom = input("De qui cherchez-vous le téléphone ? ")
    trouve = False
    
    for i in range(len(carnet)):
        membre = carnet[i]
        if nom in membre.values():
            trouve = True
            for cle in membre.keys():
                print("{} : {}".format(cle, membre[cle]), end="\t")
    print("")
    if not trouve:
        print("{} non trouvée !".format(nom))


def destruction_entree(carnet: List[Dict], cles: List[str]) -> List[Dict] :
    """
    Suppression d'une entrée dans le carnet d'adresse.
    """
    nom = input("Quel nom faut-il supprimer ? ")
    trouve = False
    
    for i in range(len(carnet)):
        membre = carnet[i]  
        if nom in membre.values():  
            trouve = True
            del carnet[i]   
    
    if not trouve:
        print("Entrée non trouvée !")
        
    return carnet
    


def main():
    carnet = []  
    cles = ["Nom", "Prénom", "Téléphone"]  
    
    print("Application agenda téléphonique.")
    print("================================\n")
    
    poursuivre = True
    while poursuivre:
        print("1 : Affichage, 2 : Nouvelle entrée, 3 : Recherche d'un numéro, 4 : Suppression d'une entrée, q : Quitter \n") 
        choix = input("Choix : ")
        
        if choix == '1':
            print("------")
            affichage(carnet)
        elif choix == '2':
            print("------")
            carnet = nouvelle_entree(carnet, cles)
        elif choix == '3':
            print("------")
            recherche(carnet)
        elif choix == '4':
            print("------")
            carnet = destruction_entree(carnet, cles)

        else:
            poursuivre = False
        
        print("------")


main()