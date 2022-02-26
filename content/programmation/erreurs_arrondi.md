---
title: "Erreurs d'arrondi"
subtitle: "... dans le cas de la dérivation numérique"
author: ""
type: ""
date: 2020-08-25T17:14:39+04:00
draft: true
toc: true
tags: ["Analyse numérique", "Code"]
categories: ["Tutoriel"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{< highlight py3 >}}
# -*- coding: utf-8 -*-

"""
Mise en évidence de l'erreur d'arrondi lors de la dérivation
"""
import matplotlib.pyplot as plt
from typing import List

 
def df(f: "function", a: float, h: float) -> float:
    """
    Retourne le nombre dérivé de la fonction f à l'abscisse
    a en appliquant le schéma des différences finies à
    droite avec le pas h.
    """
    return ( f(a + h) - f(a) ) / h


def affichage(x: List[float], y: List[float], titre: str,
              x_label: str, y_label: str, save:bool=False) -> None:
    """
    Trace erreur = f(pas).
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titre)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    plt.grid()
    if (save):
        plt.savefig("Graphique-{}.png".format(compteur))
    plt.show()

def main():
    """
    Fonction principale
    """
    f = lambda x: x**2  # fonction à dériver
    a = 2               # nombre dérivé est calculé en x = 2
    f_prime = 4         # valeur théorique du nombre dérivé

    hs = [0.05 / 2**i for i in range(0, 45)]    # valeurs des pas h

    dfs = [df(f, a, h) for h in hs]             # valeurs des nombres dérivés
    erreurs = [abs(df - f_prime) / f_prime * 100 for df in dfs]    # évolution de l'erreur

    #affichage(dxs, df, "Valeur de la dérivée")
    affichage(hs, erreurs,
              "Évolution de l'erreur dans le calcul de la dérivéeen fonction du pas",
              "h", "erreur relative (%)", False)
    for i in range(len(hs)):
        print("Pas : {:.5e}, Nombre calculé : {:.9f}, erreur relative (%) : {:.9e}".format(hs[i],
                                                                              dfs[i],
                                                                              erreurs[i]))

main()
{{< /highlight >}}