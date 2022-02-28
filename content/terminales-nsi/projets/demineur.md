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

1. Écrire une fonction qui demande à l’utilisateur trois nombres entiers $M$, $N$ et $p$. Cette fonction crée alors un tableau à deux dimensions $(M \times N )$ formé de booléens. Le nombre $p$ doit servir à établir la probabilité pour que la valeur du booléen stocké soit `True`.

Remarque
: Comment utiliser l’entier $p$&nbsp;?
Si $p=8$ (probabilité 1/8) effectuer un tirage au sort entre 1 et 8. La valeur 1 (*c’est arbitraire*) impose le booléen `True`, toute autre valeur, le booléen `False`.

2. Dans le jeu du Démineur, chaque cellule occupée (c.a.d dont la valeur vaut `True`) à représente une bombe.
Afficher dans la console le tableau en utilisant une astérisque pour représenter les bombes et un point pour représenter les
cellules «&nbsp;sures&nbsp;».

3. Effectuer un second affichage du tableau en remplaçant les points par des entiers indiquant le nombre de bombes dans le voisinage immédiat de la cellule.

{{% solution "Corrigé" %}}
{{% remote "Un corrigé se trouve à cette adresse" "https://replit.com/@dlatreyte/Demineur" %}}
{{% /solution %}}
