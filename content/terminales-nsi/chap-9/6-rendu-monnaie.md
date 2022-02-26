---
title: "Stratégie gloutonne : Le rendu de monnaie"
subtitle: "Chapitre 9,6"
author: ""
type: ""
date: 2021-01-24T01:51:49+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

Un client achète un objet qui coûte 53 euros. Il paye avec un billet de 200 euros. Il faut donc lui rendre 147 euros, par exemple un billet de 100, deux billets de 20, un billet de 5 et une pièce de 2.

Pour minimiser le nombre de pièces (on confond dans ce document les pièces et les billets) à rendre, on peut choisir la stratégie suivante :

- On commence par rendre la pièce de plus grande valeur possible ;
- On déduit cette valeur de la somme (encore) à rendre ;
- On recommence, jusqu’à obtenir une somme nulle.

En procédant ainsi, on se rend compte que l'**on résout le problème étape par étape et qu’un choix optimal est fait à chaque étape** (la pièce de plus grande valeur). Cette stratégie entre donc bien dans la catégorie des **algorithmes gloutons**.

1. Préparer la partie de code suivante : 
```python
def main():
    # valeurs des pièces
    pieces = [1, 2, 5, 10, 20, 50, 100]

    prix = int(input("Quel est le prix ? "))
    client = int(input("Combien le client donne-t-il ? "))

    a_rendre = somme_a_rendre(prix, client)
    comment = pieces_a_rendre(a_rendre, pieces)

    reponse = ["{} piece(s) de {}".format(comment[i], pieces[i]) for i in range(len(pieces))]
    print("Je dois rendre : {}".format(a_rendre))
    print("Je donne donc : {}".format(reponse))


main()
``` 

2. Définir la fonction `somme_a_rendre` dont la spécification est :
```python
def somme_a_rendre(prix: int, client: int) -> int:
    """
    Détermine la somme à rendre à partir du prix et du montant donné par
    le client.
    """
```

3. Définir la fonction `pieces_a_rendre` dont la spécification est :
```python
def pieces_a_rendre(somme: int, pieces: List[int]) -> List[int]:
    """
    Détermine les pièces (et leur nombre) à choisir pour rendre la somme
    passée en argument.
    Utilise la division euclidienne et le modulo de façon à pouvoir
    traiter tous les cas.
    """
```

4. Tester le programme.