---
title: "Illustration des différents schemas pour la dérivation numérique"
subtitle: ""
author: ""
type: ""
date: 2020-08-25T17:37:31+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---
Code le plus simple possible et donc pas modulable du tout
{{< highlight py3 >}}
"""
Différences finies centrées, ordre 02 en h.
Mise en évidence des erreurs de troncature et d'arrondis.
"""
from math import sin, cos

def df(x):
    return cos(x)


def err_centree(x, f, df, h):
    return abs(df(x) - (f(x + h / 2) - f(x - h / 2)) / h)


def err_progressive(x, f, df, h):
    return abs(df(x) - (f(x + h) - f(x)) / h)


def err_retrograde(x, f, df, h):
    return abs(df(x) - (f(x) - f(x - h)) / h)


def main():
    f = lambda x: sin(x)   # Fonction étudiée
    df = lambda x: cos(x)  # Fonction dérivée de la fonction étudiée
    x0 = 1                 # Point où le nombre dérivé est calculé
    hs = [1 / (10**i) for i in range(1, 15)]  # Liste des pas h

    print(
        "h \t\t Diff. finies Prog.   Diff. finies Retro.   Diff. finies centrées"
    )
    for h in hs:
        print("{:.1e} \t  {:.4e} \t  {:.4e} \t  {:.4e}".format(
            h, err_progressive(x0, f, df, h), err_retrograde(x0, f, df, h),
            err_centree(x0, f, df, h)))


main()
{{< /highlight >}}