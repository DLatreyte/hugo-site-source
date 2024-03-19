---
title: "Représentation d'un graphe en informatique"
subtitle: ""
author: ""
type: ""
date: 2024-03-19T19:48:53+04:00
draft: false
toc: false
tags: ["Graphe", "Structure de données"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> Plusieurs modes de représentation peuvent être implémentés pour stocker des graphes : *matrices d’adjacence (ou sommet-sommet), listes des voisins, des successeurs ou des prédécesseurs*. Lors de cette séance nous allons écrire les classes réalisant ces implémentations.

#### Structure de graphe basée sur une liste d'adjacence

1. Écrire le code de la méthode `__init__` de la classe `Sommet` dont la spécification est :

    ```python
    def __init__(self: Sommet, val: str) -> None:
        """
        Initialisation d'un sommet.
        """
    ```

    **Remarque** : La classe `Sommet` possède deux attributs :

    - `val` représente la valeur du sommet ou son étiquette. Cet attribut est de type chaîne de caractères (`str`) ;
    - `adj` représente la liste des sommets adjacents au sommet, instance de la classe. Cet attribut référence une liste de sommets ; lors de l'initialisation d'un sommet il doit référencer une liste vide.

{{% solution "Réponse" %}}

```python
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
```

{{% /solution %}}

2. Ajouter au code de la classe `Sommet` la re-définition de la méthode `__repr__` donnée ci-dessous :

    ```python
    def __repr__(self: Sommet) -> str:
        rep = str(self.val) + " : ["
        for i, sommet in enumerate(self.adj):
            rep += str(sommet.val)
            if i < len(self.adj) - 1:
                rep += ", "
        rep += "]"
        return rep
    ```

    Cette méthode permet de représenter un sommet sous la forme d'une chaîne de caractères.

3. Tester la définition de la classe `Sommet` en ajoutant les lignes de code suivantes au fichier :

    ```python
    if __name__ == "__main__":
        s1 = Sommet("a")
        s2 = Sommet("b")
        s3 = Sommet("c")
        s1.adj.append(s2)
        s1.adj.append(s3)
        print(s1)
        print(s2)
    ```

4. Écrire le code de la méthode `__init__` de la classe `Graphe` dont la spécification est :

    ```python
    def __init__(self: Graphe, valeurs: str = "") -> None:
        """
        La liste des sommets peut être passée dans une
        chaîne de caractères. Chaque sommet doit alors être
        séparé du précédent par une virgule.
    
        Hypothèse : chaque sommet n'est présent qu'une seule
        fois dans valeurs.
        """
    ```

    **Remarque :** La classe `Sommet` possède un seul attribut, `sommets`. Ce dernier référence une liste d'objets de type `Sommet`. Cette liste est initialement :

    - Soit vide,

    - Soit constituée des sommets passés en argument lors de l'initialisation d'un objet de type `Graphe`.

{{% solution "Réponse" %}}

```python
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
```

{{% /solution %}}

5. Ajouter au code de la classe `Graphe` la re-définition de la méthode `__repr__` donnée ci-dessous :

    ```python
    def __repr__(self: Graphe) -> str:
        """
        Représentation du graphe sous forme d'une chaîne de 
        caractères.
        """
        rep = "{"
        for i, sommet in enumerate(self.sommets):
            rep += repr(sommet)
            if i < len(self.sommets) - 1:  # Ajout de la virgule sauf dernier tour
                rep += ', '
        rep += "}"
        return rep
    ```

    Cette méthode permet de représenter un graphe sous la forme d'une chaîne de caractères.

6. Tester la définition de la classe `Graphe` à l'aide du code suivant, *sous les lignes de code de la question 3* :

    ```python
    g1 = Graphe("a,b,c,d")
    print(g1)
    ```

7. Écrire le code de la méthode `existe_sommet` dont la spécification est :

    ```python
    def existe_sommet(self: Graphe, s: str) -> bool:
        """
        Vérifie que le sommet s existe bien dans le graphe.
        """
    ```

{{% solution "Réponse" %}}

```python
def existe_sommet(self: Graphe, s: str) -> bool:
    """
    Vérifie que le sommet s existe bien dans le graphe.
    """
    sommet_present = False       # Sommet pas présent
    for sommet in self.sommets:  # sommet référence un objet
        if sommet.val == s:
            sommet_present = True
    return sommet_present
```

{{% /solution %}}

8. Tester le code précédent en ajoutant les instructions suivantes, *à la fin du fichier* :

    ```python
    print(f"Sommet g présent dans le graphe : {g1.existe_sommet('g')}")
    print(f"Sommet a présent dans le graphe : {g1.existe_sommet('a')}")
    ```

9. Écrire le code de la méthode `ajout_sommet` dont la spécification est :

    ```python
    def ajout_sommet(self: Graphe, val: str) -> None:
        """
        Ajout du sommet de valeur val au graphe.
    
        Si le sommet est déjà présent dans le graphe une exception
        est levée.
        """
    ```

{{% solution "Réponse" %}}

```python
def ajout_sommet(self: Graphe, val: str) -> None:
    """
    Ajout du sommet de valeur val.

    Si le sommet est déjà présent dans le graphe une exception
    est levée.
    """
    if self.existe_sommet(val):
        raise Exception("Sommet déjà présent dans le graphe !")

    self.sommets.append(Sommet(val))
```

{{% /solution %}}

10. Tester le code précédent en ajoutant les instructions suivantes, *à la fin du fichier* :

    ```python
    g1.ajout_sommet("e")
    print(g1)
    ```

11. Écrire le code de la méthode `recuperation_sommet` dont la spécification est :

    ```python
    def recuperation_sommet(self: Graphe, s: str) -> Sommet:
        """
        Récupère l'objet de type sommet, présent dans la liste
     sommets, dont la valeur/étiquette est s.
        Lève une exception si le sommet n'existe pas.
        """
    ```

​ **Remarque :** Cette méthode simplifie l'écriture des méthodes suivantes.

{{% solution "Réponse" %}}

```python
def recuperation_sommet(self: Graphe, s: str) -> Sommet:
    """
    Récupère le sommet de valeur s.
    Lève une exception si le sommet n'existe pas.
    """
    sommet_recherche = False
    for sommet in self.sommets:
        if sommet.val == s:
            sommet_recherche = sommet
            break
    return sommet_recherche
```

{{% /solution %}}

12. Écrire le code de la fonction `existe_arete` dont la spécification est :

    ```python
    def existe_arête(self, s1: str, s2: str) -> bool:
        """
        Détermine si l'arête {s1, s2} existe dans le graphe.
    
        Ne vérifie pas l'existence de l'arête {s2, s1}.
        Lève une exception si l'un des sommets n'existe pas.
        """
    ```

{{% solution "Réponse" %}}

```python
def existe_arête(self, s1: str, s2: str) -> bool:
    """
    Détermine si l'arête {s1, s2} existe dans le graphe.

    Ne vérifie pas l'existence de l'arête {s2, s1}.
    Lève une exception si l'un des sommets n'existe pas.
    """
    if not self.existe_sommet(s1):
        raise Exception(f"Sommet {s1} n'existe pas !")
    if not self.existe_sommet(s2):
        raise Exception(f"Sommet {s2} n'existe pas !")

    sommet_depart = self.recuperation_sommet(s1)
    sommet_destination = self.recuperation_sommet(s2)

    arete_existe = False
    if sommet_destination in sommet_depart.adj:
        arete_existe = True

    return arete_existe
```

{{% /solution %}}

13. Écrire le code de la fonction `ajout_arete` dont la spécification est :

    ```python
    def ajout_arete(self: Graphe, s1: str, s2: str) -> None:
        """
        Ajoute l'arête (ou l'arc) {s1, s2} au graphe.
    
        Si les sommets n'existent pas, on lève une exception.
        Si l'arête existe déjà, on lève une exception.
        Ne crée pas l'arête {s2, s1}.
        """
    ```

{{% solution "Réponse" %}}

```python
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
    sommet_depart.adj.append(sommet_destination)
```

{{% /solution %}}

14. Tester le code précédent en ajoutant les instructions suivantes, *à la fin du fichier* :

    ```python
    g1.ajout_arete("a", "b")
    g1.ajout_arete("b", "a")
    g1.ajout_arete("a", "e")
    # g1.ajout_arete("a", "b")
    g1.ajout_arete("c", "e")
    g1.ajout_arete("e", "c")
    print(g1)
    ```

15. Écrire le code de la fonction `est_non_oriente` dont la spécification est :

    ```python
    def est_non_oriente(self: Graphe) -> bool:
        """
        Détermine si le graphe est non orienté.
        """
    ```

{{% solution "Réponse" %}}

```python
def est_non_oriente(self: Graphe) -> bool:
    """
    Détermine si le graphe est non orienté.
    """
    for sommet1 in self.sommets:
        for sommet2 in sommet1.adj:
            if not (self.existe_arête(sommet1.val, sommet2.val)
                    and self.existe_arête(sommet2.val, sommet1.val)):
                return False
    return True
```

{{% /solution %}}

16. Tester le code précédent en ajoutant les instructions suivantes, *à la fin du fichier* :

    ```python
    print(f"Le graphe est non orienté : {g1.est_non_oriente()}")
    g1.ajout_arete("e", "a")
    print(f"Le graphe est non orienté : {g1.est_non_oriente()}")
    ```

17. On souhaite maintenant écrire le code de la fonction `construction_matrice` dont la spécification est :

    ```python
    def construction_matrice(self: Graphe) -> list[list[int]]:
        """
        Construction de la matrice sommet - sommet du graphe.
        """
    ```

    Compléter le code suivant :

    ```python
    def construction_matrice(self: Graphe) -> list[list[int]]:
        """
        Construction de la matrice sommet - sommet du graphe.
        """
        val_sommets_ordonnees = sorted([sommet.val for sommet in self.sommets])
    
        matrice = .....  # Initialisation de la matrice
        for nom_sommet in val_sommets_ordonnees:
            # Récupération de l'objet de type sommet associé au nom
            sommet = .....
            # Récupération des noms des sommets adjacents
            nom_sommets_adjacents = [
                sommet_adj.val for sommet_adj in sommet.adj]
            
            ligne_matrice = .....         # Initialisation de la ligne de la matrice
            for i in range(len(val_sommets_ordonnees)):
                if val_sommets_ordonnees[i] in nom_sommets_adjacents:
                    ......
                else:
                    ......
            .....  # Ajout de la ligne à la matrice
    
        return matrice
    ```

{{% solution "Réponse" %}}

```python
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

        ligne_matrice = []            # Initialisation de la ligne de la matrice
        for i in range(len(val_sommets_ordonnees)):
            if val_sommets_ordonnees[i] in nom_sommets_adjacents:
                ligne_matrice.append(1)
            else:
                ligne_matrice.append(0)
        matrice.append(ligne_matrice)  # Ajout de la ligne à la matrice

    return matrice
```

{{% /solution %}}

18. Tester le code précédent en ajoutant les instructions suivantes, *à la fin du fichier* :

    ```python
    print(f"Matrice : {g1.construction_matrice()}")
    ```

19. Écrire le code de la méthode `representation_matrice` dont la spécification est :

    ```python
    def representation_matrice(self: Graphe) -> str:
        """
        Retourne une chaîne de caractères qui permet un
        affichage classique de la matrice (lignes x colonnes).
        """
    ```

    Tester le code.

{{% solution "Réponse" %}}

```python
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
```

{{% /solution %}}

#### Extensions possibles

Il est possible de compléter la classe en définissant les méthodes suivantes :

- `taille`, de spécification :

    ```python
    def taille(self: Graphe) -> None:
        """
        Retourne le nombre de sommets dans le graphe.
        """
    ```

- `rend_non_oriente`, de spécification :

    ```python
    def rend_non_oriente(self: Graphe) -> None:
        """
        Assure que pour toute arête {s1, s2} il existe une 
        arête {s2, s1}. Si ce n'est pas le cas, cette arête
        est créée.
        """
    ```

- `suppression_arete`, de spécification :

    ```python
    def suppression_arete(self: Graphe, s1: str, s2: str) -> None:
        """
        Supprime l'arête {s1, s2} si elle existe, lève une exception
        dans le cas contraire.
        """
    ```

- `suppression_sommet`, de spécification :

    ```python
    def suppression_sommet(self: Graphe, s: str) -> None:
        """
        Supprime le sommet s s'il existe, lève une exception dans
        le cas contraire.
    
        S'assure avant la suppression du sommet que toute arrête
        dans laquelle il intervient est supprimée.
        """
    ```
