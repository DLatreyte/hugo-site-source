---
title: "Jeu de la vie"
subtitle: ""
author: ""
type: ""
date: 2020-10-04T04:35:40+04:00
draft: false
toc: true
tags: ["Objet", "Classe", "Attribut", "Méthode", "Instance", "Encapsulation"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> Le but de ce sujet est de réaliser en Python une implémentation du jeu de la vie en utilisant la programmation objet.

{{% note normal %}}

Un **automate cellulaire** consiste en une grille régulière de « cellules » contenant chacune un « état » choisi parmi un ensemble fini et qui peut évoluer au cours du temps. L'état d'une cellule au temps $t+1$ est fonction de l'état au temps $t$
 d'un nombre fini de cellules appelé son « voisinage ». À chaque nouvelle unité de temps, les mêmes règles sont appliquées simultanément à toutes les cellules de la grille, produisant une nouvelle « génération » de cellules dépendant entièrement de la génération précédente.

{{% /note %}}
Le **jeu de la vie** a été inventé par le mathématicien britannique John H. Conway (1937-2020). C’est un exemple de ce qu’on appelle un automate cellulaire bidimensionnel. Il se déroule sur un tableau rectangulaire $(L \times H)$ de cellules. Une cellule est représentée par ses coordonnées $x$ et $y$ qui vérifient $0 \leqslant x < L$ et $0 \leqslant y < H$.

Une cellule peut être dans deux états : **vivante** ou **morte**. La dynamique du jeu s’exprime par les règles de transition suivantes :

- *une cellule vivante reste vivante à la génération suivante si elle est entourée de 2 ou 3 voisines vivantes et meurt sinon* ;
- *une cellule morte devient vivante à la génération suivante si elle possède exactement 3 voisines vivantes*.

La notion de « voisinage » dans le jeu de la vie est celle des 8 cases qui peuvent entourer une case donnée (on parle de voisinage de Moore).

Pour implémenter la simulation, on va tout d’abord rechercher une modélisation objet du problème, puis procéder à son implémentation.

{{% note warning %}}
Chaque fonction/méthode devra posséder une spécification.
{{% /note %}}

## Modélisation objet

1. Quelles classes peut-on envisager au premier abord pour implémenter ce problème ?
{{% solution "Réponse" %}}
Les classes `Grille` et `Cellule` viennent facilement à l’esprit, on peut penser à une classe `Etat` représentant l’état d’une cellule si l’on veut pousser la modélisation un peu plus loin.
{{% /solution %}}

2. Quelles méthodes pourrait-on imaginer pour chaque classe ?
{{% solution "Réponse" %}}
Nous retrouverons ces méthodes dans l’implémentation, mais il faut au moins songer ici aux méthodes qui permettent de récupérer l’état interne des attributs et de les modifier. Il faut aussi penser à la représentation du voisinage d’une cellule et aux méthodes permettant de le modifier ou de le récupérer.
{{% /solution %}}

3. Dans quelle classe pouvons-nous représenter simplement la notion de voisinage d’une cellule ? Et le calculer ?
{{% solution "Réponse" %}}
Il peut être commode qu’une `Cellule` connaisse ses voisins, mais une `Grille` est plus à même de calculer les voisinages. On peut donc définir une méthode de calcul de voisinage dans la `Grille` et des méthodes pour affecter ou lire la liste des voisins dans la `Cellule`, ce qui lui permettra de calculer son état futur selon les règles du jeu de la vie.
{{% /solution %}}

4. Une cellule est au bord si $x=0$, $x=L-1$, $y=0$ ou $y=H-1$. Combien de voisins possède une cellule qui n’est pas au bord ?
Combien de voisins possède une cellule qui est au bord ?
{{% solution "Réponse" %}}
Une cellule qui n’est pas au bord possède 8 voisins. Une cellule qui est en bordure en possède 3 dans les angles ou 5 ailleurs sur les bords.
{{% /solution %}}

5. Que pourrions-nous aussi considérer comme voisin de droite de la case en haut et à droite de la grille ? Et comme voisin du haut ?
{{% solution "Réponse" %}}
Nous pourrions considérer que le voisin de la cellule en haut et à droite de la grille est la cellule en haut et à gauche. De même le voisin du haut de la case en haut à droite pourrait être la cellule en bas à droite de la grille (grille torique).
{{% /solution %}}

## Implémentation du jeu

{{% note warning %}}

Chaque classe sera définie dans un fichier différent.

{{% /note %}}

#### La classe `Cellule`

1. Implémenter tout d’abord une classe `Cellule` avec comme attributs :
    - un booléen `actuel` initialisé à `False` ;
    - un booléen `futur` initialisé à `False` ;
    - une liste `voisins` initialisée à `None`.

**Remarque.** La valeur `False` signifie que la cellule est morte et `True` qu’elle est vivante.

2. Ajouter les méthodes suivantes :
    - `est_vivant` qui renvoie l’état actuel (vrai ou faux) ;
    - `set_voisins` qui permet d’affecter comme voisins la liste passée en paramètre ;
    - `get_voisins` qui renvoie la liste des voisins de la cellule ;
    - `naitre` qui met l’état futur de la cellule à `True` ;
    - `mourir` qui permet l’opération inverse ;
    - `basculer` qui fait passer l’état futur de la cellule dans l’état actuel.

3. Ajouter à la classe Cellule une méthode `__str__` qui retourne le caractère `"X"` si la cellule est vivante et un tiret `"-"` sinon.  
Expliquer brièvement l’utilité d’une telle méthode `__str__` en Python.

4. Ajouter une méthode `calcule_etat_futur` dans la classe `Cellule` qui permet d’implémenter les règles d’évolution du jeu de la vie en préparant l’état futur à sa nouvelle valeur.

#### La classe `Grille`

5. Créer la classe `Grille` et y définir les attributs suivants :
    - `largeur` (passé en argument) ;
    - `hauteur` (passé en argument) ;
    - `matrix` : un tableau de cellules à 2 dimensions implémenté en Python par une liste de listes.

**Remarque :** Définir la méthode `set_matrix` pour construire le tableau.
**Remarque :** Une nouvelle Cellule sera créée par l’appel `Cellule()`.

6. Ajouter les méthodes :
    - `dans_grille` qui indique si un point de coordonnées $i$ et $j$ est bien dans la grille ;
    - `set_cell_xy` qui permet d’affecter une nouvelle cellule à la case $(i,j)$ de la grille, si $(i,j)$ est bien dans la grille ;
    - `get_cell_xy` qui permet de récupérer la cellule située dans la case $(i,j)$ de la grille, si $(i,j)$ est bien dans la grille ;
    - `get_largeur` qui permet de récupérer la largeur de la grille ;
    - `get_hauteur` qui permet de récupérer la hauteur de la grille ;
    - `est_voisin` une *méthode statique* qui vérifie si les cases $(i,j)$ et $(x,y)$ sont voisines dans la grille.

7. Ajouter une méthode `get_voisins` qui renvoie la liste des voisins d’une cellule.

8. Fournir une méthode `set_voisins` qui affecte à chaque cellule de la grille la liste de ses voisins.

9. Donner une méthode `__str__` qui permet d’afficher la grille sur un terminal.

10. On veut remplir aléatoirement la Grille avec un certain taux de Cellule vivantes. Définir une méthode `remplir_alea` avec le taux (en pourcentage) en argument.

#### Le jeu

11. Définir une méthode `jeu` permettant de passer en revue toutes les Cellules de la Grille, de calculer leur état futur, puis une méthode `actualise` qui bascule toutes les cellules de la Grille dans leur état futur.

12. Dans le fichier principal, entrer le code suivant afin de lancer le jeu :

```python
from grille import Grille
import time


def effacer_ecran():
    print("\u001B[H\u001B[J")


def main():
    plateau = Grille(20, 30)
    plateau.remplir_alea(55)
    plateau.set_voisins()
    while True:
        effacer_ecran()
        print(plateau)
        print("\n")
        time.sleep(0.5)
        plateau.jeu()
        plateau.actualise()


main()
```

## Spécifications

- Classe `Cellule`

```python
def __init__(self: Cellule) -> None:
    """
    Initialisation des attributs.
    """
```

```python
def est_vivant(self: Cellule) -> bool:
    """
    Retourne l'état actuel de la cellule.
    """
```

```python
def set_voisins(self: Cellule, voisins: List[Cellule]) -> None:
    """
    Affecte comme voisins la liste passée en paramètre.
    """
```

```python
def get_voisins(self: Cellule) -> List[Cellule]:
    """
    Renvoie la liste des voisins de la cellule
    """
```

```python
def naitre(self: Cellule) -> None:
    """
    Met l’état futur de la cellule à `True`
    """
```

```python
def mourir(self: Cellule) -> None:
    """
    Met l’état futur de la cellule à `False`
    """
```

```python
def basculer(self: Cellule) -> None:
    """
    Fait passer l’état futur de la cellule dans l’état actuel
    """
```

```python
def __str__(self: Cellule) -> str:
    """
    Représentation de l'objet sous forme d'une chaîne de caractères
    """
```

```python
def calcule_etat_futur(self: Cellule) -> None:
    """
    Implémente les règles d’évolution du jeu de la vie en préparant l’état futur à sa nouvelle valeur
    """
```

- Classe `Grille`

```python
def __init__(self: Grille, largeur: int, hauteur: int) -> None:
    """
    Initialisations des attributs
    """
```

```python
def set_matrix(self: Grille) -> List[List[Cellule]]:
    """
    Construction de la grille de cellules
    """
```

```python
def dans_grille(self: Grille, i: int, j: int) -> bool:
    """
    Vérifie que le point de coordonnées (i,j) est dans la grille
    """
```

```python
def set_cell_xy(self: Grille, i: int, j: int, cellule: Cellule) -> None:
    """
    Affecte une nouvelle cellule à la case (i,j) de la grille
    """
```

```python
def get_cell_xy(self: Grille, i: int, j: int) -> Cellule:
    """
    Récupère la cellule située dans la case (i,j) de la grille
    """
```

```python
def get_largeur(self: Grille) -> int:
    """
    Récupère la largeur de la grille
    """
```

```python
def get_hauteur(self: Grille) -> int:
    """
    Récupère la hauteur de la grille
    """
```

```python
@staticmethod
def est_voisin(i: int, j: int, x: int, y: int) -> bool:
    """
    Vérifie si les cases (i,j) et (x,y) sont voisines dans la grille
    """
```

```python
def get_voisins(self: Grille, x: int, y: int) -> List[Cellule]:
    """
    Renvoie la liste des voisins d’une cellule
    """
```

```python
def set_voisins(self: Grille):
    """
    Affecte à chaque cellule de la grille la liste de ses voisins
    """
```

```python
def __str__(self: Grille) -> str:
    """
    Représentation de l'objet
    """
```

```python
def remplir_alea(self, taux: int) -> None:
    """
    Remplir aléatoirement la Grille avec un certain taux de Cellules vivantes
    """
```

```python
def jeu(self: Grille) -> None:
    """
    Passe en revue toutes les Cellules de la Grille, calcule leur état futur
    """
```

```python
def actualise(self: Grille) -> None:
    """
    Bascule toutes les cellules de la Grille dans leur état futur
    """
```

## Corrigé

- {{< remote "Corrigé" "https://repl.it/@dlatreyte/jeudelavie" >}}
