---
title: "Simulation d'un titrage conductimétrique"
subtitle: ""
author: ""
type: ""
date: 2020-10-11T20:53:53+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

```python
"""
Simulation du suivi conductimétrique pour le titrage
du sérum physiologique.
"""
import matplotlib.pyplot as plt
import csv
from scipy.stats import linregress


class Ion():
    """
    Définition d'un ion à prendre en compte dans le
    calcul de la conductivité d'une solution.
    """

    def __init__(self, nom, conduc=0, charge=0, n=0):
        self.nom = nom
        self.charge = charge        # Charge électrique (multiple de e)
        self.conductivite = conduc  # Conductivité molaire ionique
        self.quantite = n           # Quantité de matière (moles)

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, n):

        if n < 0:
            self._quantite = 0
        else:
            self._quantite = n

    def info(self):
        chaine = "Nom : {}\n".format(self.nom)
        chaine += "Charge électrique : {}e\n".format(self.charge)
        chaine += "Quantité de matière : {} mol\n".format(self.quantite)
        return chaine


class Solution():
    """
    Définition d'une solution ionique.
    """

    def __init__(self, liste_ions=[], volume=0):
        self.ions = liste_ions
        self.volume = volume

    def conductivite(self):

        conduc = 0
        for ion in self.ions:
            contrib = ion.conductivite * ion.quantite / self.volume
            conduc += contrib
        return conduc


def creation_fichier_resultat(nom_fichier, entete_x, entete_y,
                              list_x, list_y):

    with open(nom_fichier, 'w') as fichier:
        writer = csv.writer(fichier, dialect='excel')
        writer.writerow([entete_x, entete_y])

        for i in range(len(list_x)):
            writer.writerow((list_x[i], list_y[i]))


def affichage(list_v, list_conduc, list_regres):
    # Création d'une figure
    fig = plt.figure()
    # Création d'une sous-figure
    ax = fig.add_subplot(111)
    # Affichage des données
    ax.plot(list_v, list_conduc, 'ro')
    ax.plot(list_v, list_regres, 'b-')
    # Limites pour l'axe des abscisses
    ax.set_xlim(min(list_v) - 1E-3, max(list_v) + 1E-3)
    # Utilisation de l'écriture scientifique pour les valeurs
    ax.ticklabel_format(axis='both', style='sci', scilimits=(0, 0))
    # Label de l'axe des abscisses
    ax.set_xlabel(r'$V_2$ (L)')
    # Label de l'axe des ordonnées
    ax.set_ylabel(r'$\sigma$ ($\mathrm{S}\cdot\mathrm{m}^{-1}$)')
    # Affichage de la grille
    ax.grid()
    # Légende
    ax.set_title(r'Suivi conductimétrique sans effet de dilution')
    # Sauvegarde de la figure
    fig.savefig("conductimetrie_01.pdf")
    # Affichage de la figure
    plt.show()


def determination_intervalles(liste1, liste2):
    """
    Fonction qui, à partir de la liste liste1, possédant des valeurs
    décroissantes puis croissantes, retourne un tuple constitué de quatre
    listes ; la première ne contenant que les valeurs décroissantes, la
    deuxième les valeurs croissantes de la liste 1. Les deux autres listes
    correspondent aux parties correspondantes de la liste 2.
    """
    indice_du_min = liste1.index(min(liste1))
    liste1_1 = liste1[0:indice_du_min]
    liste1_2 = liste1[indice_du_min:]

    liste2_1 = liste2[0:indice_du_min]
    liste2_2 = liste2[indice_du_min:]
    return (liste2_1, liste1_1, liste2_2, liste1_2)


def regression_lineaire(vol_1, conduc_1, vol_2, conduc_2):
    lr1 = linregress(vol_1, conduc_1)
    lr2 = linregress(vol_2, conduc_2)

    drl = []
    for vol in vol_1:
        drl.append(lr1[0] * vol + lr1[1])
    for vol in vol_2:
        drl.append(lr2[0] * vol + lr2[1])

    return drl


def main():
    C = 3.2E-2   # Concentration des ions chlorure
    V = 10E-3    # Volume de sérum physiologique
    C2 = 2E-2    # Concentration des ions argent
    V2_max = 24  # Volume maximal de titrant versé (en mL)
    V_eau = 0.100   # Volume d'eau ajouté
    xE = C * V   # Avancement à l'équivalence

    ion_argent = Ion("ion argent", 6.2E-3, 1)
    ion_chlorure = Ion("ion chlorure", 7.6E-3, -1)
    ion_sodium = Ion("ion sodium", 5.0E-3, 1, C * V)
    ion_nitrate = Ion("ion nitrate", 7.1E-3, -1)

    sol = Solution([ion_argent, ion_chlorure, ion_sodium, ion_nitrate])

    # Volumes de titrant versés
    volumes = [i * 1E-3 for i in range(V2_max + 1)]
    conduc = []  # valeurs des conductivités dans la solution

    for V2 in volumes:
        n2 = C2 * V2
        ion_argent.quantite = n2 - xE
        ion_chlorure.quantite = C * V - n2
        ion_nitrate.quantite = n2
        # Partie à adapter si on veut montrer l'effet de la dilution
        sol.volume = V_eau + V + V2
        conduc.append(sol.conductivite())

    creation_fichier_resultat("valeurs.csv",
                              "Volumes (L)",
                              "Conductivité (S.m^-1)",
                              volumes,
                              conduc)

    vol_1, conduc_1, vol_2, conduc_2 = determination_intervalles(conduc,
                                                                 volumes)
    droites_regression = regression_lineaire(vol_1, conduc_1, vol_2,
                                             conduc_2)

    affichage(volumes, conduc, droites_regression)

    print(volumes)
    print(vol_1, vol_2)


main()
```