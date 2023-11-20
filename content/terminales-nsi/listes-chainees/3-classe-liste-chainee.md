---
title: "Réalisation d'une classe Liste Chainee"
subtitle: ""
author: ""
type: ""
date: 2023-11-20T15:50:34+04:00
draft: false
toc: true
tags: ["Liste", "Liste chaînée"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

Par transformation des fonctions du document 1 dans ce chapitre en méthodes, écrire le code de la classe `Liste` qui définit le type abstrait « Liste chaînée ».

{{% solution "Réponse" %}}

```python
from __future__ import annotations


class Maillon:
    """
    Un maillon de la liste.
    """

    def __init__(self: Maillon, valeur: int, suivant: Maillon = None) -> None:
        self.valeur = valeur
        self.suivant = suivant


class Liste:
    """
    Implémentation de la classe liste.
    """

    def __init__(self: Liste, valeur: int = None) -> None:
        """
        Initialisation de l'objet. Il est possible de créer une liste
        vide ou une liste contenant un élément.

        Il est possible de créer directemnt une liste contenant plusieurs
        éléments il faut utiliser une fonctionnalité de Python que vous
        ne connaissez pas forcément et qui n'est pas au programme.
        """
        if valeur is None:
            self.maillons = None
        else:
            self.maillons = Maillon(valeur)

    def est_vide(self: Liste) -> bool:
        """ Détermine si la liste est vide. """
        return self.maillons is None

    def __len__(self: Liste) -> int:
        """ Retourne le nombre d'éléments dans la liste. """
        if self.est_vide():
            return 0
        else:
            nbre = 0
            maillon = self.maillons
            while maillon is not None:
                nbre += 1
                maillon = maillon.suivant
            return nbre

    def append(self: Liste, valeur: int) -> None:
        """
        Ajoute valeur à la fin de la liste.
        """
        if self.est_vide():
            self.maillons = Maillon(valeur)
        else:
            maillon = self.maillons
            while maillon.suivant is not None:
                maillon = maillon.suivant

            maillon.suivant = Maillon(valeur)

    def append_first(self: Liste, valeur: int) -> None:
        """
        Ajoute valeur au début de la liste.
        """
        maillon = Maillon(valeur)
        maillon.suivant = self.maillons
        self.maillons = maillon

    def pop(self: Liste) -> int:
        """
        Retire le dernier élément de la liste et le retourne.

        Lève une erreur si la liste est vide.
        """
        if self.est_vide():  # Liste vide
            raise Exception("La liste est vide !")

        maillon = self.maillons
        if maillon.suivant is None:  # Cas d'une liste à un élément
            valeur = maillon.valeur
            self.maillons = None
            return valeur
        else:
            while maillon.suivant.suivant is not None:  # Cas général
                maillon = maillon.suivant
            valeur = maillon.suivant.valeur
            maillon.suivant = None
            return valeur

    def pop_first(self: Liste) -> int:
        """
        Retire le premier élément de la liste et le retourne.

        Lève une erreur si la liste est vide.
        """
        if self.est_vide():  # Liste vide
            raise Exception("La liste est vide !")

        valeur = self.maillons.valeur
        self.maillons = self.maillons.suivant
        return valeur

    def __getitem__(self: Liste, i: int) -> int:
        """
        Redéfinition de la fonction d'accès à l'élément d'indice i.
        """
        if self.est_vide():
            raise Exception("La liste est vide !")

        maillon = self.maillons
        j = 0
        while j < i:
            if maillon is None:
                raise IndexError("Indice hors des limites !")
            maillon = maillon.suivant
            j += 1
        return maillon.valeur

    def __str__(self: Liste) -> str:
        """
        Représentation de la liste sous-forme d'une chaîne de caractères.
        """
        rep = "["

        maillon = self.maillons
        while maillon is not None:
            rep += str(maillon.valeur)
            if maillon.suivant is not None:
                rep += ", "
            maillon = maillon.suivant

        rep += "]"
        return rep

```

{{% /solution %}}
