---
title: "Lé Démineur"
subtitle: ""
author: ""
type: ""
date: 2022-02-28T06:33:38+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: false
auto_numbering: true
---

{{% note normal %}}
Le Démineur est un jeu vidéo de réflexion dont le but est de localiser des mines cachées dans une grille représentant un champ de mines virtuel, avec pour seule indication le nombre de mines dans les zones adjacentes.

<div style="text-align:right;">
<a href="https://fr.wikipedia.org/wiki/Démineur_(genre_de_jeu_vidéo)"> Wikipedia </a>
</div>
{{% /note %}}

> L'objectif de cette séance est la construction de la grille représentant le champ de mines.

1. Les fonctions développées ci-dessous devront appartenir à un module `demineur`.\
   Créer ce module.

Le plateau à deux dimensions (m lignes et n colonnes) du jeu sera défini à la question 3. par une liste de listes contenant des valeurs booléennes. La présence d'une bombe correspondra à la valeur `True` tandis que l'absence d'une bombe à la valeur `False`. Les bombes seront placées aléatoirement avec une probabilité de 1/p.

2. Dans le module `demineur`, définir la fonction `place_bombe` dont la spécification est :

```python
def contient_bombe(p: int) -> bool:
    """
    Fonction qui détermine si une case contient une bombe ou pas.
    Cette détermination est aléatoire, de probabilité 1/p.
    """
```

**Remarque.** Utiliser la fonction `randint` du module `random` pour effectuer le tirage aléatoire et décider que la présence d'une bombe correspond à la valeur 1 (c'est arbitraire).

3. Dans le module `demineur`, définir la fonction `initialisation_jeu` dont la spécification est :

```python
def initialisation_jeu(m: int, n: int, p: int) -> List[List[bool]]:
    """
    Initialise le Jeu en construisant un plateau de dimensions m x n cases, 
    contenant des bombes dont la probabilité d'apparition est de 1/p.

    La présence d'une bombe correspond à la valeur True, l'absence d'une
    bombe correspond à la valeur False.
    """
```

**Remarque.** En fait, il est plus pratique (la raison sera développée plus tard) de créer un plateau de m + 2 lignes et de n + 2 colonnes. Les première et dernière lignes, ainsi que les première et dernière colonnes ne devront contenir aucune bombe.

4. Dans le module `demineur`, définir la fonction `affichage` dont la spécification est :

```python
def affichage(p: List[List[bool]]) -> None:
    """
    Affiche le plateau du jeu dans la console.
    Une astérisque représente une bombe, un point représente une cellule
    « sure ».
    """
```

5. Dans le fichier principal, importer le module `demineur`,
   - définir les variables `M`, `N` et `p` en demandant à l'utilisateur leurs valeurs,
   - initialiser le jeu,
   - afficher le plateau.

7. Dans le module `demineur`, définir la fonction `nombre_bombes` dont la spécification est :

```python
def nombre_bombes(p: List[List[bool]], i: int, j: int) -> int:
    """
    Retourne le nombre de bombes au voisinage de la 
    cellule (i, j) du plateau p.
    """
```

**Remarque.** Le fait d'avoir choisi une liste de listes de dimensions (m + 2) x (n + 2) facilite l'écriture de cette fonction.

8. Dans le module `demineur`, définir la fonction dont la spécification est :

```python
def affichage_nbre_bombes(p: List[List[bool]]) -> None:
    """
    Affiche le plateau du jeu dans la console.
    Une astérisque représente une bombe, les cellules « sures » contiennent
    le nombre de bombes adjacentes.
    """
```

9. Appeler la fonction `affichage_nbre_bombes` depuis le fichier principal.

{{% solution "Corrigé" %}}
{{% remote "Un corrigé se trouve à cette adresse" "https://replit.com/@dlatreyte/Demineur" %}}
{{% /solution %}}
