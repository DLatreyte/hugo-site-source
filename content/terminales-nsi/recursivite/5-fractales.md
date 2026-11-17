---
title: "Dessin de figures fractales"
subtitle: ""
date: 2021-01-26T06:16:46+04:00
draft: false
toc: true
tags: ["Fractales", "Récursivité", "Turtle"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: true
auto_numbering: true
weight: 500
---

{{< note goal >}}
Dessiner des figures fractales avec le module `turtle`, en traduisant leur construction géométrique par une fonction récursive.
{{< /note >}}

{{< note tip >}}
Le mot fractale vient du latin fractus qui signifie brisé. En effet, une
figure fractale est un objet géométrique infiniment morcelé dont des détails
sont observables à une échelle arbitrairement choisie.

*En zoomant sur une partie de la figure, on peut retrouver toute la
figure*, on dit qu'elle est **autosimilaire**.

- {{< remote "Les fractales (maths-et-tiques)" "https://www.maths-et-tiques.fr/index.php/detentes/les-fractales" >}}
- {{< remote "Fractale (Wikipédia)" "https://fr.wikipedia.org/wiki/Fractale" >}}
{{< /note >}}

## Introduction

Dans le code suivant (qu'il faudra étudier et exécuter) :

1. Quel est le cas de base de l'algorithme récursif ?

2. Où s'effectue l'appel récursif ?

3. Pourquoi le cas de base est-il toujours réalisé ?

```python
import turtle
from math import cos, pi, sin


def dessine_etoile(t: turtle.Turtle, pt: tuple[float, float], longueur: float) -> None:
    """
    Dessine une étoile à six branches de centre pt, puis, à l'extrémité
    de chaque branche, une étoile trois fois plus petite, etc.
    """
    if longueur <= 2:
        return

    for i in range(6):
        x_ext = pt[0] + int(longueur * cos((2 * pi / 6) * i))
        y_ext = pt[1] + int(longueur * sin((2 * pi / 6) * i))

        pt_ext = (x_ext, y_ext)  # Extrémité du segment

        t.penup()
        t.setposition(pt)

        t.pendown()
        t.setposition(pt_ext)

        dessine_etoile(t, pt_ext, longueur / 3)


def main() -> None:
    """Fonction principale."""
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    segment = 300
    centre = (0, 0)
    dessine_etoile(t, centre, segment)
    turtle.mainloop()


if __name__ == "__main__":
    main()
```

{{< solution "Réponses" >}}
1. Le cas de base correspond à `longueur <= 2` : la fonction ne dessine rien et s'arrête (une branche de 2 pixels ne serait plus visible).
2. L'appel récursif `dessine_etoile(t, pt_ext, longueur / 3)` est placé dans la boucle : chaque étoile provoque six appels, un à l'extrémité de chacune de ses branches.
3. La longueur est divisée par 3 à chaque appel : $300$, $100$, $\text{33,3}$, $\text{11,1}$, $\text{3,7}$ puis $\text{1,2}$. Elle finit forcément par devenir inférieure ou égale à 2, ici au sixième niveau d'appels.
{{< /solution >}}

## Le flocon de von Koch

La première courbe à tracer a été imaginée par le mathématicien suédois
Niels Fabian Helge von Koch, afin de montrer que l'on pouvait tracer des
courbes continues en tout point, mais dérivables en aucun.

Le principe est le suivant : on divise un segment initial en trois morceaux,
et on construit un triangle équilatéral sans base au-dessus du morceau
central. On réitère le processus $n$ fois, $n$ étant appelé l'**ordre**.

{{< columns >}}
<img src="/terminales-nsi/chap-1/chap-1-5/koch_0.png" alt="" width="" />
{{< column >}}
<img src="/terminales-nsi/chap-1/chap-1-5/koch_1.png" alt="" width="" />
{{< endcolumns >}}
{{< columns >}}
<img src="/terminales-nsi/chap-1/chap-1-5/koch_2.png" alt="" width="" />
{{< column >}}
<img src="/terminales-nsi/chap-1/chap-1-5/koch_3.png" alt="" width="" />
{{< endcolumns >}}

> Ordres 0, 1, 2 et 3 de la fractale.

Si on trace trois fois cette figure, on obtient successivement un
triangle, une étoile, puis un flocon de plus en plus complexe.

{{< columns >}}
<img src="/terminales-nsi/chap-1/chap-1-5/flocon_0.png" alt="" width="60%" />
{{< column >}}
<img src="/terminales-nsi/chap-1/chap-1-5/flocon_1.png" alt="" width="60%" />
{{< endcolumns >}}
{{< columns >}}
<img src="/terminales-nsi/chap-1/chap-1-5/flocon_2.png" alt="" width="60%" />
{{< column >}}
<img src="/terminales-nsi/chap-1/chap-1-5/flocon_3.png" alt="" width="60%" />
{{< endcolumns >}}
> Figures successives (ordre 0, 1, 2 et 3).

### Principe de la construction

{{< note normal >}}
La méthode de construction utilise un algorithme récursif :

- À l'ordre 0, il suffit d'appeler une fois la méthode `forward` pour tracer un segment. *C'est le cas de base.*

- À l'ordre 1, il faut appeler la méthode `forward` (4 fois), les méthodes `left` et `right` pour découper le segment en 4 parties (de même longueur).

- À l'ordre $n \geq 1$, le code ressemble à celui de l'ordre 1, si ce
    n'est qu'on remplace l'appel de chacune des méthodes `forward` par le tracé de
    segments à l'ordre $n-1$. *C'est l'appel récursif, on découpe chaque
    partie de segment en sous-parties*.
{{< /note >}}

### Travail

1. Définir la fonction de signature

```python
def koch_1(t: turtle.Turtle, longueur: float) -> None: ...
```

qui dessine un segment de Koch à l'ordre 1, de longueur $l$, à l'aide de l'objet de type `Turtle` `t`. Les sous-segments de la figure sont de longueur $l/3$ et les angles
    sont de 60 ou 120 degrés.

2. Définir la fonction `main` permettant de tester la fonction `koch_1`.

Remarque.

:   Les futurs tracés vont nécessiter beaucoup de calculs et
    l'affichage de nombreux points à l'écran. De façon à améliorer la
    performance,

    - régler la vitesse de la tortue au maximum : `t.speed(0)` ;

    - cacher le symbole représentant la tortue à l'écran : `t.hideturtle()`.

3. Définir la fonction de signature

```python
def koch(t: turtle.Turtle, n: int, longueur: float) -> None: ...
```

qui dessine à l'écran un segment de
    Koch d'ordre 0 ou 1, de longueur $l$, à l'aide de l'objet de type
    Turtle `t`.\
    Le corps de la fonction doit uniquement gérer les deux cas : $n=0$
    et $n=1$ (le cas $n\geq 2$ sera traité dans l'une des prochaines
    questions).

4. Modifier la fonction `main` de façon à tester la fonction `koch`.

5. Cette partie généralise la fonction `koch` au cas $n \geq 2$. Il faut
    découper chaque segment de droite en sous-parties ; il faut donc
    remplacer chaque appel de la méthode `forward` dans `koch` par un appel de la
    fonction `koch` elle-même : `koch(t, n-1, ...)`.\
    Trouver par quoi remplacer les ... et modifier la fonction.

6. Tester la nouvelle fonction `koch` pour une longueur de 300 pixels et
    $n \in [0, 5]$ (au-delà de cette dernière valeur, on ne voit plus
    trop de différences).

7. Définir la fonction de signature

```python
def dessine_flocon(t: turtle.Turtle, n: int, longueur: float) -> None: ...
```

qui dessine à l'écran un flocon de von Koch, d'ordre $n$ et dont chaque segment a une
longueur $l$.

{{< note tip "Coup de pouce" >}}
Pour la question 5 : un segment d'ordre $n$ est formé de quatre segments d'ordre $n - 1$, trois fois plus courts. Pour la question 7 : le flocon est formé de trois segments de Koch disposés en triangle équilatéral. De quel angle faut-il tourner entre deux segments ?
{{< /note >}}

{{< solution "Solution" >}}

```python
"""
Tracé du flocon de von Koch.
"""

import turtle


def koch_0(t: turtle.Turtle, longueur: float) -> None:
    """
    Trace à l'écran un segment de longueur longueur (ordre 0).
    """
    t.forward(longueur)


def koch_1(t: turtle.Turtle, longueur: float) -> None:
    """
    Dessine une branche de longueur longueur du flocon de von Koch
    à l'ordre 1.
    """
    t.forward(longueur / 3)
    t.left(60)
    t.forward(longueur / 3)
    t.right(120)
    t.forward(longueur / 3)
    t.left(60)
    t.forward(longueur / 3)


def koch(t: turtle.Turtle, n: int, longueur: float) -> None:
    """
    Dessine une branche du flocon de von Koch à l'ordre n.

    HYPOTHÈSE : n entier naturel.
    """
    if n == 0:
        t.forward(longueur)
    else:
        koch(t, n - 1, longueur / 3)
        t.left(60)
        koch(t, n - 1, longueur / 3)
        t.right(120)
        koch(t, n - 1, longueur / 3)
        t.left(60)
        koch(t, n - 1, longueur / 3)


def dessine_flocon(t: turtle.Turtle, n: int, longueur: float) -> None:
    """
    Dessine un flocon de von Koch à l'ordre n.

    HYPOTHÈSE : n entier naturel.
    """
    if not t.isdown():
        t.pendown()

    for _ in range(3):
        koch(t, n, longueur)
        t.right(120)


def main() -> None:
    """Fonction principale."""
    fen = turtle.Screen()
    fen.bgcolor("black")

    t = turtle.Turtle()
    t.color("white")
    t.speed(0)
    t.hideturtle()
    t.penup()
    t.goto(-150, 150)
    t.pendown()

    dessine_flocon(t, 5, 400)
    # koch(t, 4, 300)
    # koch_1(t, 200)

    fen.exitonclick()


if __name__ == "__main__":
    main()
```

{{< /solution >}}

## Arbre fractal

On peut appliquer le même principe pour construire d'autres fractales
visuellement différentes, mais construites sur le même principe.

### Présentation

<img src="/terminales-nsi/chap-1/chap-1-5/arbre.png" alt="" width="50%" />
> Arbre fractal.

Par exemple, pour construire un arbre, on part d'un segment, et on
applique la transformation présentée ci-dessus à
chaque segment de la construction (on refait la transformation $n$ fois
pour obtenir un arbre d'ordre $n$) :

<img src="/terminales-nsi/chap-1/chap-1-5/arbre_1.png" alt="" width="50%" />
> Base de la construction d'un arbre.

Les portions dessinées en *pointillés sont celles sur lesquelles on
appliquera la transformation à l'ordre suivant* (on les appelle les
**segments non-terminaux**). Les portions dessinées en *trait plein sont
des segments qui ne seront pas transformés* (on les appellera les
**segments terminaux**).

Pour transformer un segment non-terminal de longueur $l$, on trace un
segment terminal de longueur $l/3$, puis deux segments non-terminaux de
longueur $2l/3$ à un angle $\theta$ du premier segment.

### Travail

Suivre la même démarche que pour le flocon de Koch pour écrire une
fonction de signature

```python
def arbre(t: turtle.Turtle, n: int, longueur: float, theta: float) -> None: ...
```

qui trace l'arbre, et *repositionne la tortue à son point de départ*.

- Dans un premier temps, gérer les ordres 0 et 1 (utiliser la méthode
    `forward` et aucun appel récursif), et tester la fonction. Vérifier en
    particulier que la tortue est bien revenue à son point de départ à
    la fin de l'exécution de la fonction dans les deux cas (n = 0 et n =
    1).

- Pour chaque tracé de segment non-terminal, remplacer l'appel à la
    méthode `forward` par un appel récursif à la fonction `arbre`, et vérifier le
    comportement de la fonction à différents ordres. Cette fois-ci, une
    profondeur 10 ou 11 donne un résultat assez joli.

{{< note tip "Coup de pouce" >}}
Pour que la tortue revienne à son point de départ, chaque déplacement doit être annulé dans l'ordre inverse : un `forward` par un `backward` de même longueur, un `left` par un `right` de même angle. Si chaque appel récursif ramène la tortue là où il l'a trouvée, il suffit de vérifier que la fonction annule ses propres déplacements.
{{< /note >}}

{{< solution "Solution" >}}

```python
"""
Programme qui dessine un arbre fractal.
"""

import turtle


def arbre(t: turtle.Turtle, n: int, longueur: float, theta: float) -> None:
    """
    Dessine un arbre fractal d'ordre n, de hauteur longueur, dont les
    branches forment un angle theta (en degrés), puis ramène la tortue
    à son point et à sa direction de départ.

    HYPOTHÈSE : n entier naturel.
    """
    if n == 0:
        t.color("red")
        t.forward(longueur)
        t.backward(longueur)
        t.color("black")

    else:
        t.width(n)
        t.forward(longueur / 3)
        t.left(theta)
        arbre(t, n - 1, longueur / 3 * 2, theta)
        t.right(2 * theta)
        arbre(t, n - 1, longueur / 3 * 2, theta)
        t.left(theta)
        t.backward(longueur / 3)


def main() -> None:
    """Fonction principale."""
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)
    t.setheading(90)

    longueur = 300
    theta = 35
    n = 11

    arbre(t, n, longueur, theta)
    # enregistrement de l'image (format PostScript)
    ts = turtle.getscreen()
    ts.getcanvas().postscript(file="arbre.eps")

    turtle.mainloop()


if __name__ == "__main__":
    main()
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- repérer le cas de base et les appels récursifs d'une fonction qui dessine une figure ;
- justifier qu'une fonction récursive se termine parce qu'un paramètre décroît jusqu'au cas de base ;
- traduire une construction géométrique répétée par une fonction récursive ;
- utiliser les méthodes `forward`, `backward`, `left` et `right` d'un objet `Turtle` ;
- écrire une fonction récursive qui ramène la tortue à son point de départ.
{{< /note >}}
