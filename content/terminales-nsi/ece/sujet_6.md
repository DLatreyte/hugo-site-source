---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2021-10-27T17:34:19+04:00
draft: true
toc: true
tags: []
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% points)

On s’intéresse au problème du rendu de monnaie. On suppose qu’on dispose d’un nombre infini de billets de 5 euros, de pièces de 2 euros et de pièces de 1 euro.

Le but est d’écrire une fonction nommée `rendu` dont le paramètre est un entier positif non nul `somme_a_rendre` et qui retourne une liste de trois entiers `n1`, `n2` et `n3` qui correspondent aux nombres de billets de 5 euros (`n1`) de pièces de 2 euros (`n2`) et de pièces de 1 euro (`n3`) à rendre afin que le total rendu soit égal à `somme_a_rendre`.

On utilisera un algorithme glouton : on commencera par rendre le nombre maximal de billets de 5 euros, puis celui des pièces de 2 euros et enfin celui des pièces de 1 euros.

Exemples :
```python 
>>> rendu(13)
[2, 1, 1]
>>> rendu(64)
[12, 2, 0]
>>> rendu(89)
[17, 2, 0]
```

{{% solution "Corrigé" %}}



{{% /solution %}}

## Exercice 2 (50% points)

On veut écrire une classe pour gérer une file à l’aide d’une liste chaînée. On dispose d’une classe `Maillon` permettant la création d’un maillon de la chaîne, celui-ci étant constitué d’une valeur et d’une référence au maillon suivant de la chaîne :
```python
class Maillon :
    def __init__(self: Maillon, v: int) -> None:
        self.valeur = v
        self.suivant = None
```

Compléter la classe `File` suivante où l’attribut `dernier_file` contient le maillon correspondant à l’élément arrivé en dernier dans la file :
```python
class File :
    def __init__(self: Maillon) -> None:
        self.dernier_file = None

    def enfile(self: Maillon, element: int) -> None:
        nouveau_maillon = Maillon(... , self.dernier_file)
        self.dernier_file = ...

    def est_vide(self: Maillon) -> ... :
        return self.dernier_file == None

    def affiche(self: Maillon) -> None:
        maillon = self.dernier_file
        while maillon != ... :
            print(maillon.valeur)
            maillon = ...

    def defile(self: Maillon) -> int:
        if not self.est_vide() :
            if self.dernier_file.suivant == None :
                resultat = self.dernier_file.valeur
                self.dernier_file = None
                return resultat
            maillon = ...

            while maillon.suivant.suivant != None :
                maillon = maillon.suivant
            resultat = ...

            maillon.suivant = None
            return resultat

        return None
``` 

On pourra tester le fonctionnement de la classe en utilisant les commandes suivantes dans la console Python :

```python
>>> F = File()
>>> F.est_vide()
True
>>> F.enfile(2)
>>> F.affiche()
2
>>> F.est_vide()
False
>>> F.enfile(5)
>>> F.enfile(7)
>>> F.affiche()
7
5
2
>>> F.defile()
2
>>> F.defile()
5
>>> F.affiche()
7
```

{{% solution "Corrigé" %}}



{{% /solution %}}

