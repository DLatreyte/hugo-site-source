---
title: "Analyse des résultats du Loto"
subtitle: ""
author: ""
type: ""
date: 2021-01-28T04:03:54+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: false
---
[^2]: En réalité il existe deux fichiers car la formule du jeu a été modifiée en 2008. Nous ne traiterons que les résultats des tirages entre 1976 et 2008 !
[^1]: Vous pourrez en fournir d'autres qui vous paraitraient pertinentes.

Le LOTO de la Française des Jeux est un jeu de hasard et d'argent apparu en 1976 en France. Dans sa première version (jusqu'en 2008), les joueurs devaient choisir 6 numéros dans une grille contenant tous les nombres entiers de 1 à 49 (inclus).

Sur le site de la Française des Jeux {{<remote "https://www.fdj.fr/jeux/jeux-de-tirage/loto/statistiques" "https://www.fdj.fr/jeux/jeux-de-tirage/loto/statistiques" >}} il est possible de télécharger un fichier contenant les résultats de tous les tirages[^2], noyés parmi un grand nombre d'informations, depuis le tout début de ce jeu. La quantité d'informations contenues dans le fichier est tellement importante que l'utilisation d'un programme pour les analyser prend tout son sens.

> L'objectif du programme est, **au minimum**, de compter le nombre d'apparitions de chacun des numéros entre 1976 et 2008.\
Le résultat, dans la console, doit au minimum fournir les informations suivantes[^1] :

```bash
Lors des 4858 tirages : 
    le 1 est apparu 710 fois 
    le 2 est apparu 681 fois 
    le 3 est apparu 674 fois 
    le 4 est apparu 720 fois 
    le 5 est apparu 702 fois
    ...
```

Le programme devra être découpé en fonctions. **Chaque fonction devra être accompagnée de sa spécification**.

## Le site n'est pas accessible depuis les Émirats

- {{< remote "Accès au fichier" "/terminales-nsi/projets/analyse-loto/loto.csv" >}}
