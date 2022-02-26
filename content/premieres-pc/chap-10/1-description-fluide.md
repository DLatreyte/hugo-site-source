---
title: "Description d'un fluide au repos"
subtitle: "Chapitre 9,1"
author: ""
type: ""
date: 2021-02-24T05:06:35+04:00
draft: false
toc: true
tags: []
categories: ["Premières Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Modèle microscopique d'un gaz

### Compréhension du modèle

Visionner les deux vidéos suivantes en prenant des notes :

{{% youtube UDj7BXA1CHU %}} 

{{% youtube gPMVaAnij88 %}}

1. Rappeler quels sont les trois états physiques que l'eau peut prendre.
{{% solution "Réponse" %}}
On peut retrouver l'eau dans les états solide, liquide et gazeux.
{{% /solution %}}

2. Qu'est-ce qui caractérise un solide, **du point de vue macroscopique** ?
{{% solution "Réponse" %}}
Les solides possèdent une forme propre et ne sont pas compressibles.
{{% /solution %}}

3. Qu'est-ce qui caractérise un liquide, **du point de vue macroscopique** ?
{{% solution "Réponse" %}}
Les liquides s'écoulent et prennent la forme du récipient qui les contient. Ils ne sont pas très compressibles.
{{% /solution %}}

4. Qu'est-ce qui caractérise un gaz, **du point de vue macroscopique** ?
{{% solution "Réponse" %}}
Les gaz occupent tout l'espace disponible. Ils peuvent être compressé.
{{% /solution %}}

5. Qu'est-ce qui caractérise un solide, **du point de vue microscopique** ?
{{% solution "Réponse" %}}
Dans un solide, les entités microscopiques (atomes, molécules, etc.) vibrent autour d'une position moyenne fixe. Ces entités sont très proches les unes des autres.
{{% /solution %}}

6. Qu'est-ce qui caractérise un liquide, **du point de vue microscopique** ?
{{% solution "Réponse" %}}
Dans un liquide, les entités microscopiques (atomes, molécules, etc.) sont toujours très proches les unes des autres mais elles peuvent se déplacer.
{{% /solution %}}

7. Qu'est-ce qui caractérise un gaz, **du point de vue microscopique** ?
{{% solution "Réponse" %}}
Dans un gaz, les entités microscopiques (atomes, molécules) se déplacent librement. Elles sont donc beaucoup plus éloignées les unes des autres en moyenne. Le nombre de collisions reste très important.
{{% /solution %}}

8. Pourquoi peut-on regroupe les liquides et les gaz sous l'appellation « fluide » ?
{{% solution "Réponse" %}}
Dans les liquides et les gaz les entités peuvent se déplacer dans l'espace, contrairement à celles qui constituent solides.\
Ce point commun est suffisamment important pour que l'on puisse regrouper les états liquide et gazeux sous l'appellation état fluide.
{{% /solution %}}

9. Quel phénomène permet de valider le modèle microscopique d'un gaz ? Décrire ce phénomène (on pourra visionner la deuxième vidéo si la première n'est pas suffisamment claire).
{{% solution "Réponse" %}}
C'est le mouvement brownien.\
Brown, un botaniste, en 1827, alors qu'il étudiait des grains de pollen dans une goutte d'eau, au microscope, s'est rendu compte que ceux-ci n'était pas immobiles mais possédaient un mouvement erratique. L'explication théorique de ce phénomène a été donnée par Einstein en 1905, des molécules d'eau, invisibles au microscope, entrent à chaque instant en collision avec les grains de pollen. Ceux-ci sont donc projetés dans toutes les direction de façon complètement aléatoire. 
{{% /solution %}}

### Simulation d'une marche au hazard à deux dimensions

Le programme à {{< remote "cette adresse" "https://replit.com/@dlatreyte/Marche-au-hasard-a-deux-dimensions#main.py" >}} simule un déplacement, aléatoire, dans un plan, de trois tortues (commenter l'instruction `tortue1.hideturtle()` et dé-commenter l'instruction `tortue1.shape("turtle")` pour faire apparaître la tortue).

10. Lancer la simulation. Qu'est-ce qui provoque son arrêt ?
{{% solution "Réponse" %}}
La simulation s'arrête lorsqu'une tortue atteint le cadre qui délimite le plan.
{{% /solution %}}

11. Quelle est l'action des instructions comprises entre les lignes 45 et 52 ?
{{% solution "Réponse" %}}
Le bloc constitue une boucle `TantQue` qui se répète deux fois.\
Les instructions du bloc font :
- avancer la tortue de 400 pixels ;
- tourner à gauche de 90° la tortue ;
- avancer la tortue de 400 pixels ;
- tourner à gauche la tortue de 90°.
Le tout trace donc la limite du plan dans lequel les tortues peuvent se déplacer.
{{% /solution %}}

12. Résumer la condition d'arrêt de la boucle `TantQue` (`while`) qui débute à la ligne 64.
{{% solution "Réponse" %}}
La boucle se poursuit tant que les tortues restent dans le plan délimité par la frontière dessinée par les instructions comprises entre les lignes 45 et 52.\
Pour une tortue de coordonnées $(x,y)$, on doit donc avoir les relations, si $L$ est la largeur du plan et $H$ sa hauteur, $-L/2 \leqslant x \leqslant L/2$ et $$-H/2 \leqslant y \leqslant H/2$.
{{% /solution %}}

13. Que contient la variable `dx1` une fois l'instruction de la ligne 73 exécutée ? Se document sur la fonction `randint` du module `random` si nécessaire.
{{% solution "Réponse" %}}
La variable `dx1` contient un nombre entier compris entre -10 et 10 inclus, choisi aléatoirement.
{{% /solution %}}

14. À quoi servent les instructions des ligne 75 et 76 ?
{{% solution "Réponse" %}}
Les instructions calculent les nouvelles coordonnées de la tortue.
{{% /solution %}}

15. À quoi sert l'instruction de la ligne 77 ?
{{% solution "Réponse" %}}
L'instruction déplace la tortue jusqu'au nouveau point.
{{% /solution %}}

16. Ajouter une cinquième tortue à ce programme. Effectuer toutes les modifications nécessaires.

17. En quoi ce programme simule-t-il le mouvement brownien.
{{% solution "Réponse" %}}
À chaque tour de boucle la nouvelle position de la tortue est déterminée aléatoirement. C'est une situation comparable à celle d'une molécule percutée aléatoirement par d'autres molécules. 
{{% /solution %}}

### À retenir
- **Solides :** <img src="/premieres-pc/chap-10/chap-10-1/chap-10-1-1.png" alt="" width="20%" />
- **Liquides :** <img src="/premieres-pc/chap-10/chap-10-1/chap-10-1-2.png" alt="" width="20%" />
- **Gaz :** <img src="/premieres-pc/chap-10/chap-10-1/chap-10-1-3.png" alt="" width="20%" />

{{% note tip %}}
Un gaz est dans un état dispersé. Ses molécules sont en mouvement permanent et désordonné. Cet état dispersé permet aussi d'interpréter la compressibilité des gaz.
{{% /note %}}


## Quels sont les paramètres qui permettent de décrire le comportement d'un gaz

Utiliser la simulation {{< remote "à cette adresse" "https://phet.colorado.edu/sims/html/gas-properties/latest/gas-properties_en.html" >}}

18. Quels sont les paramètres que cette simulation permet de faire varier ?
{{% solution "Réponse" %}}
On peut faire varier le **volume** occupé par le gaz, la **température**, la **quantité de matière**.
{{% /solution %}}

19. Quel paramètre, non modifiable dans cette simulation, semble dépendre de la variation des paramètres modifiables ?
{{% solution "Réponse" %}}
La simulation ne permet pas de modifier directement la pression du gaz. Toute variation du volume, de la quantité de matière et de la température modifie la pression du gaz.
{{% /solution %}}

20. Afficher le nombre de collisions entre molécules. Augmenter la température du gaz.
    - Comment varie la pression ?
    - Comment varie le nombre de collisions ?
{{% solution "Réponse" %}}
La pression et le nombre de collisions augmentent lorsque la température augmente.
{{% /solution %}}

21. Augmenter la quantité de matière du gaz.
    - Comment varie la pression ?
    - Comment varie le nombre de collisions ?
{{% solution "Réponse" %}}
La pression et le nombre de collisions augmentent lorsque la quantité de matière du gaz augmente.
{{% /solution %}}

22. Diminuer le volume du gaz.
    - Comment varie la pression ?
    - Comment varie le nombre de collisions ?
{{% solution "Réponse" %}}
La pression et le nombre de collisions augmentent lorsque le volume du gaz diminue.
{{% /solution %}}

23. Existe-t-il une corrélation entre la valeur du paramètre pression et le nombre de collisions ?
{{% solution "Réponse" %}}
La pression et le nombre de collisions sont des grandeurs corrélées puisqu'elles varient de la même façon lors de chacune des expériences envisagées.
{{% /solution %}}

{{% note tip %}}
L'état d'un gaz peut être décrit par les paramètres **volume**, **pression**, **température** et **quantité de matière**.
{{% /note %}}


