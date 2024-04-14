---
title: "Coloration d'un graphe"
subtitle: ""
author: ""
type: ""
date: 2024-04-14T18:42:53+04:00
draft: false
toc: true
tags: ["Graphe", "Structure de données"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de cette séance est de découvrir comment colorier chaque sommet
d'un graphe à l'aide d'un algorithme glouton.

{{% note normal %}}

Colorier un graphe signifie associer une couleur à chacun de ses sommets
de façon à ce que deux sommets liés par une arête n'aient pas la même couleur
(deux sommets non adjacents peuvent avoir la même couleur).

Colorier un graphe avec un **nombre minimal de couleurs** est un problème
difficile mais l'utilisation d'un algorithme glouton permet de résoudre
le problème, au prix d'un nombre de couleurs qui n'est pas toujours minimal.

{{% /note %}}

#### Remarques

- Les couleurs seront représentées par des nombres entiers
débutant à la valeur 0.
- La classe `Graphe` du document
[Représentation d'un graphe](2-representation-graphe-bis) sera utilisée.  
Son code est reproduit ci-dessous.
{{% solution "Code" %}}

```python
"""
Représentation d’un graphe à l'aide d'une liste d'adjacence.
"""
from __future__ import annotations


class Sommet:
    """
    Représentation d'un sommet.
    """

    def __init__(self: Sommet, val: str) -> None:
        """
        Initialisation du sommet.
        """
        self.val = val
        self.adj = []  # Sommets adjacents

    def liste_adjacents(self: Sommet) -> list[Sommet]:
        """
        Retourne la liste des sommets adjacents.
        """
        return self.adj

    def ajoute_adjacent(self: Sommet, som: Sommet) -> None:
        """ Ajoute un sommet adjacent """
        self.adj.append(som)

    def __repr__(self: Sommet) -> str:
        rep = str(self.val) + " : ["
        for i, sommet in enumerate(self.adj):
            rep += str(sommet.val)
            if i < len(self.adj) - 1:
                rep += ", "
        rep += "]"
        return rep


class Graphe:
    """
    Représentation du graphe.
    """

    def __init__(self: Graphe, valeurs: str = "") -> None:
        """
        La liste des sommets peut être passée dans une
        chaîne de caractères. Chaque sommet doit être
        séparé du précédent par une virgule.

        Hypothèse : chaque sommet n'est présent qu'une seule
        fois dans valeurs.
        """
        self.sommets = []  # liste des sommets

        if valeurs != "":
            for sommet in valeurs.split(","):
                self.sommets.append(Sommet(sommet))

    def liste_sommets(self: Graphe) -> list[Sommet]:
        """
        Retourne la liste des sommets du graphe.
        """
        return self.sommets

    def ajout_sommet(self: Graphe, val: str) -> None:
        """
        Ajout du sommet de valeur val.

        Si le sommet est déjà présent dans le graphe une exception
        est levée.
        """
        if self.existe_sommet(val):
            raise Exception("Sommet déjà présent dans le graphe !")

        self.sommets.append(Sommet(val))  # Ajout de l'objet de type Sommet

    def existe_sommet(self: Graphe, s: str) -> bool:
        """
        Vérifie que le sommet s existe bien dans le graphe.
        """
        sommet_present = False       # Sommet pas présent
        for sommet in self.sommets:  # sommet référence un objet
            if sommet.val == s:
                sommet_present = True
                break
        return sommet_present

    def recuperation_sommet(self: Graphe, s: str) -> Sommet:
        """
        Récupère le sommet de valeur s.
        Lève une exception si le sommet n'existe pas.
        """
        if not self.existe_sommet(s):
            raise Exception(f"Le sommet {s} n'existe pas.")

        for objet_sommet in self.sommets:
            if objet_sommet.val == s:
                return objet_sommet

    def ajout_arete(self: Graphe, s1: str, s2: str) -> None:
        """
        Ajoute l'arête (ou l'arc) {s1, s2} au graphe.

        Si les sommets n'existent pas, on lève une exception.
        Si l'arête existe déjà, on lève une exception.
        Ne crée pas l'arête {s2, s1}.
        """
        # L'arête existe-t-elle déjà ?
        if self.existe_arête(s1, s2):
            raise Exception("Arête existe déjà !")

        # Récupération des sommets
        sommet_depart = self.recuperation_sommet(s1)
        sommet_destination = self.recuperation_sommet(s2)

        # Ajout du sommet s2 à la liste des adjacents de s1
        sommet_depart.ajoute_adjacent(sommet_destination)

    def existe_arête(self, s1: str, s2: str) -> bool:
        """
        Détermine si l'arête {s1, s2} existe dans le graphe.

        Ne vérifie pas l'existence de l'arête {s2, s1}.
        Lève une exception si l'un des sommets n'existe pas.
        """
        objet_sommet_depart = self.recuperation_sommet(s1)
        objet_sommet_arrivee = self.recuperation_sommet(s2)

        return objet_sommet_arrivee in objet_sommet_depart.liste_adjacents()

    def est_non_oriente(self: Graphe) -> bool:
        """
        Détermine si le graphe est non orienté.
        """
        for sommet1 in self.sommets:
            for sommet2 in sommet1.liste_adjacents():
                if not self.existe_arête(sommet2.val, sommet1.val):
                    return False
        return True

    def construction_matrice(self: Graphe) -> list[list[int]]:
        """
        Construction de la matrice sommet - sommet du graphe.
        """
        val_sommets_ordonnees = sorted([sommet.val for sommet in self.sommets])

        matrice = []  # Initialisation de la matrice

        for nom_sommet in val_sommets_ordonnees:
            # Récupération de l'objet de type sommet associé au nom
            sommet = self.recuperation_sommet(nom_sommet)
            # Récupération des noms des sommets adjacents
            nom_sommets_adjacents = [
                sommet_adj.val for sommet_adj in sommet.adj]

            ligne_matrice = []       # Initialisation de la ligne de la matrice
            for i in range(len(val_sommets_ordonnees)):
                if val_sommets_ordonnees[i] in nom_sommets_adjacents:
                    ligne_matrice.append(1)
                else:
                    ligne_matrice.append(0)
            matrice.append(ligne_matrice)  # Ajout de la ligne à la matrice

        return matrice

    def representation_matrice(self: Graphe) -> str:
        """
        Retourne une chaîne de caractères qui permet un
        affichage classique de la matrice (lignes x colonnes).
        """
        matrice = self.construction_matrice()

        rep = ""
        nbre = len(matrice)  # nombre de lignes et de colonnes
        for i in range(nbre):
            for j in range(nbre):
                rep += str(matrice[i][j]) + '\t'
            rep += "\n"
        return rep

    def __repr__(self: Graphe) -> str:
        """
        Représentation du graphe sous forme d'une chaîne de caractères.
        """
        rep = "{"
        for i, sommet in enumerate(self.sommets):
            rep += repr(sommet)
            # Ajout de la virgule sauf dernier tour de boucle
            if i < len(self.sommets) - 1:
                rep += ', '
        rep += "}"
        return rep

    def suppression_arete(self: Graphe, s1: str, s2: str) -> None:
        """
        Supprime l'arête {s1, s2} si elle existe, lève une exception
        dans le cas contraire.
        """
        pass

    def suppression_sommet(self: Graphe, s: str) -> None:
        """
        Supprime le sommet s s'il existe, lève une exception dans
        le cas contraire.

        S'assure avant la suppression du sommet que toute arrête
        dans laquelle il intervient est supprimée.
        """
        pass

    def rend_non_oriente(self: Graphe) -> None:
        """
        Assure que pour toute arête {s1, s2} il existe une
        arête {s2, s1}. Si ce n'est pas le cas, cette arête
        est créée.
        """
        pass

    def taille(self: Graphe) -> int:
        """
        Retourne le nombre de sommets dans le graphe.
        """
        return len(self.sommets)


if __name__ == "__main__":
    s1 = Sommet("a")
    s2 = Sommet("b")
    s3 = Sommet("c")
    s1.adj.append(s2)
    s1.adj.append(s3)
    print(s1)
    print(s2)

    g1 = Graphe("a,b,c,d")
    print(g1)
    print(f"Sommet g présent dans le graphe : {g1.existe_sommet('g')}")
    print(f"Sommet a présent dans le graphe : {g1.existe_sommet('a')}")
    g1.ajout_sommet("e")
    print(g1)
    g1.ajout_arete("a", "b")
    g1.ajout_arete("b", "a")
    g1.ajout_arete("a", "e")
    # g1.ajout_arete("a", "b")
    g1.ajout_arete("c", "e")
    g1.ajout_arete("e", "c")
    print(g1)
    print(f"Le graphe est non orienté : {g1.est_non_oriente()}")
    g1.ajout_arete("e", "a")
    print(f"Le graphe est non orienté : {g1.est_non_oriente()}")
    print(f"Matrice : {g1.construction_matrice()}")
    print(g1.representation_matrice())
    print(f"Taille du graphe : {g1.taille()}")

    print("---------------------")
    g2 = Graphe("a,b,c,d,e,f,g")
    print(f"Taille du graphe : {g2.taille()}")
    g2.ajout_arete("a", "d")
    g2.ajout_arete("a", "b")
    g2.ajout_arete("a", "c")
    g2.ajout_arete("b", "a")
    g2.ajout_arete("b", "c")
    g2.ajout_arete("b", "d")
    g2.ajout_arete("b", "f")
    g2.ajout_arete("c", "a")
    g2.ajout_arete("c", "b")
    g2.ajout_arete("c", "e")
    g2.ajout_arete("d", "a")
    g2.ajout_arete("d", "b")
    g2.ajout_arete("d", "f")
    g2.ajout_arete("e", "c")
    g2.ajout_arete("f", "b")
    g2.ajout_arete("f", "d")
    g2.ajout_arete("f", "g")
    g2.ajout_arete("g", "f")
    print(f"Le graphe est non orienté : {g2.est_non_oriente()}")
    print(g2.representation_matrice())
    print(g2.liste_sommets())
```

{{% /solution %}}

Le code du fichier fourni comporte les instructions suivantes :

```python
g2 = Graphe("a,b,c,d,e,f,g")
    g2.ajout_arete("a", "d")
    g2.ajout_arete("a", "b")
    g2.ajout_arete("a", "c")
    g2.ajout_arete("b", "a")
    g2.ajout_arete("b", "c")
    g2.ajout_arete("b", "d")
    g2.ajout_arete("b", "f")
    g2.ajout_arete("c", "a")
    g2.ajout_arete("c", "b")
    g2.ajout_arete("c", "e")
    g2.ajout_arete("d", "a")
    g2.ajout_arete("d", "b")
    g2.ajout_arete("d", "f")
    g2.ajout_arete("e", "c")
    g2.ajout_arete("f", "b")
    g2.ajout_arete("f", "d")
    g2.ajout_arete("f", "g")
    g2.ajout_arete("g", "f")
```

1. Quelle est la taille de ce graphe ?

2. Représenter ce graphe.

3. Donner la matrice d'adjacence de ce graphe.

Lancer le programme et vérifier la validité des vos réponses.

{{% note normal %}}

#### Principe de l'algorithme

On parcourt tous les sommets du graphe dans un ordre arbitraire, et pour chaque
sommet, on lui attribue la première couleur qui n'est pas déjà attribuée
à ses sommets adjacents.

{{% /note %}}

4. Mettre en œuvre cet algorithme, à la main, sur le graphe proposé dans
le code fourni.

L'implémentation de l'algorithme en Python nécessite la définition de deux
fonctions : `coloriage` et `choix_couleur` dont les spécifications sont :

```python
def coloriage(g: Graphe) -> tuple[dict[str, int], int]:
    """
    Colorie le graphe g passé en argument.
    Retourne un tuple constitué du dictionnaire des couleurs pour chaque
    sommet et du nombre de couleurs utilisées.
    """
```

et

```python
def choix_couleur(sommet: Sommet, couleurs: dict[str, int]) -> int:
    """
    Choisi la première couleur disponible en fonction de celles
    déjà attribuées aux sommets adjacents.
    """
```

**Remarque :** la fonction `coloriage` appelle la fonction `choix_couleur`.

5. Écrire le code Python de ces deux fonctions.

{{% solution "Aide pour l'écriture de la fonction coloriage" %}}

La fonction doit :

- Initialiser à 0 la variable `nbre_couleurs`. Elle comptabilise le nombre
de couleurs différentes utilisées lors du coloriage du graphe.
- Initialiser au dictionnaire vide la variable `couleurs`. Ce dictionnaire a
pour clés les étiquettes des sommets visités et pour valeurs les couleurs
associées.
- Parcourir tous les sommets du graphe.
  - Pour chacun d'eux lui attribuer une couleur à l'aide de la fonction
    `choix_couleur`.
  - Incrémenter d'une unité le compteur de couleurs, **si cette couleur n'a
    pas déjà été utilisée**.
  - Mettre à jour le dictionnaire des couleurs.
- Retourner le tuple constitué du dictionnaire des couleurs et de la variable
qui comptabilise le nombre de couleurs utilisées.

{{% /solution %}}

{{% solution "Aide pour l'écriture de la fonction choix_couleur" %}}

La fonction doit :

- Déterminer le nombre de sommets adjacents au sommet passé en argument.
- Initialiser à `False` la liste de booléens `couleurs_attribuees`. Les indices
de cette liste sont les couleurs déjà attribuées aux sommets adjacents du sommet
étudié. La valeur `True` signifie que la couleur a été attribuée, `False` que
la couleur est libre.  
Dans le pire des cas, tous les sommets adjacents ont déjà une couleur attribuée ;
la première couleur attribuable sera donc l'indice $n$. C'est la raison pour
laquelle *la longueur de la liste doit être égale à $n+1$ si $n$ est le nombre
de sommets adjacents*.
- Doit rechercher les couleurs des sommets adjacents.
  - Pour chaque sommet adjacent, elle doit vérifier dans le dictionnaire
    `couleurs` si ce sommet a déjà été colorier.
  - Si c'est le cas et que cette couleur est inférieure à $n$, modifier
    à `True` la valeur de la liste `couleurs_attribuees` pour la couleur
    (indice) en question.
- Doit rechercher la première couleur (indice) libre dans la liste
`couleurs_attribuees` et la retourner.

{{% /solution %}}

{{% solution "Solution" %}}

```python
def coloriage(g: Graphe) -> tuple[dict[str, int], int]:
    """
    Colorie le graphe g passé en argument.
    Retourne un tuple constitué du dictionnaire des couleurs pour chaque
    sommet et du nombre de couleurs utilisées.
    """
    nbre_couleurs = 0  # Nombre de couleurs utilisées
    couleurs = {}      # Dictionnaire des sommets colorés

    for sommet in g.liste_sommets():
        # Choix d'une couleur pour le sommet
        couleur = choix_couleur(sommet, couleurs)
        # Incrémentation du compteur de couleurs si nouvelle couleur
        if couleur not in couleurs.values():
            nbre_couleurs += 1
        # Ajout de ce sommet au dictionnaire des couleurs
        couleurs[sommet.val] = couleur

    return couleurs, nbre_couleurs


def choix_couleur(sommet: Sommet, couleurs: dict[str, int]) -> int:
    """
    Choisi la première couleur disponible en fonction de celles
    déjà attribuées aux sommets adjacents.
    """
    # Nbre de sommets adjacents
    n_adj = len(sommet.liste_adjacents())

    # Initialisation des couleurs déjà attribuées (indices de la liste)
    # + 1 assure d'avoir un choix possible pour le sommet étudié.
    couleurs_attribuees = [False for i in range(n_adj + 1)]

    # recherche des couleurs déjà attribuées
    for adj in sommet.liste_adjacents():  # Sommet adjacent
        if adj.val in couleurs.keys():    # Sommet déjà colorié
            couleur_attribuee = couleurs[adj.val]  # avec une valeur <= n
            if couleur_attribuee <= n_adj:
                couleurs_attribuees[couleur_attribuee] = True

    # Détermination de la couleur
    for i in range(len(couleurs_attribuees)):
        if not couleurs_attribuees[i]:
            return i
```

{{% /solution %}}
