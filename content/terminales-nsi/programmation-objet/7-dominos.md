---
title: "Jeu de dominos"
subtitle: ""
author: ""
type: ""
date: 2023-02-28T13:02:19+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Les dominos

[Qu'est-ce que le jeu de dominos ?](https://www.agoralude.com/blog/la-regle-du-jeu-de-dominos-n33)

## Programmation

1. Écrire le code de la classe `Domino` telle que le constructeur initialise les variables `gauche` et `droite`.

Penser à définir et utiliser une fonction `verifie_valeur` dont la spécification est

```python
def verifie_valeur(self, val: int, cote: str) -> int:
    """
    Vérifie que la valeur attribuée au Domino est correcte.
    Dans le cas contraire, lève une exception.
    """
```

2. Écrire le code de la fonction `est_double` dont la spécification est

```python
def est_double(self: Domino) -> bool:
    """
    Teste si le domino est double.
    """
```

3. Écrire le code de la fonction `est_blanc` dont la spécification est

```python
def est_blanc(self: Domino) -> bool:
    """
    Teste si le domino est blanc, c'est à dire si ces valeurs gauche et
    droite sont nulles.
    """
```

4. Écrire le code de la fonction `nbre_points` dont la spécification est

```python
def nbre_points(self: Domino) -> int:
    """
    Compte le nombre de points.
    """
```

5. Écrire le code de la fonction `__str__` suivant

```python
def __str__(self: Domino) -> str:
    """
    Affichage du domino.
    """
    if not self.est_double():
        return """
        ⎡⎺⎺⎺⎺⎺ ⎺⎺⎺⎺⎺⎤
        ⎢  {}  ⎢  {}  ⎥ 
        ⎣⎽⎽⎽⎽⎽ ⎽⎽⎽⎽⎽⎦
        """.format(self.gauche, self.droite)
    else:
        return """
        ⎡⎺⎺⎺⎺⎺⎤
        ⎢  {}  ⎢
        ⎢⎻⎻⎻⎻⎻⎢
        ⎢  {}  ⎢
        ⎣⎽⎽⎽⎽⎽⎦
        """.format(self.gauche, self.droite)
```

6. Écrire le code de la classe `JeuDominos` dont le constructeur initialise la variable `nbre_pieces` à 28 et crée la variable `jeu` de type liste de dominos.  
Définir la fonction `creation_jeu` dont l'objet est la création du jeu.

7. Écrire le code de la fonction `melanger` dont la spécification est

```python
def melanger(self: JeuDominos) -> None:
    """
    Mélange aléatoirement le jeu de dominos.
    """
```

8. Écrire le code de la fonction `distribuer` dont la spécification est

```python
def distribuer(self: JeuDominos, nbre_joueurs: int) -> List[Domino]:
    """
    Extractions des dominos attribués à un joueur de la liste des dominos et retour des dominos attribués à ce joueur.
    """
```

9. Écrire le code de la fonction `affiche_jeu` dont la spécification est

```python
def affiche_jeu(self: JeuDominos) -> None:
    """
    Affiche le jeu ou la pioche en fonction de l'avancée du jeu.
    """
```

10. Initialiser le jeu, et le mélanger.

11. Pour le joueur 1, utiliser le code suivant

```python
print("Joueur 1")
print("========")
jeu_j1 = jeu.distribuer(2)
points_joueur_1 = 0
nbre_dominos_blancs_j1 = 0
nbre_dominos_doubles_j1 = 0
for domino in jeu_j1:
    print(domino)
    points_joueur_1 += domino.nbre_points()
    if domino.est_blanc():
        nbre_dominos_blancs_j1 += 1
    if domino.est_double():
        nbre_dominos_doubles_j1 += 1

print(
    f"{points_joueur_1} points possibles, dont {nbre_dominos_blancs_j1} dominos blancs et {nbre_dominos_doubles_j1} dominos doubles."
)
```

12. Adapter le code précédent pour le joueur 2.

13. Afficher la pioche.
