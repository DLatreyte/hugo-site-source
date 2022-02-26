---
title: "Détermination de la masse du Soleil à l'aide de Python"
subtitle: "Chapitre 9,14"
author: ""
type: ""
date: 2022-01-11T10:47:21+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---

> L'objectif de ce document est de retrouver la masse du Soleil à l'aide des données des périodes et des demi-grands axes des planètes et de la troisième loi de Képler.

{{% note normal %}}

Un corrigé de cette activité se trouve à cette <a href="https://replit.com/@dlatreyte/Troisieme-loi-de-Kepler#main.py" target="_blank">adresse</a>. Ne pas le consulter avant d'avoir cherché les réponses aux questions.

{{% /note %}}

#### Données
<center>

| Planète | Période (ans) | Demi-grand axe ($\times \pu{10^{10} m}$) |
| :--: | :--: | :--: |
| Mercure | 0,24 | 5,79 |
| Vénus | 0,62 | 10,80 |
| Terre | 1,00 | 15,00 |
| Mars | 1,88 | 22,80 |
| Jupiter | 11,90 | 77,80 |
| Saturne | 29,50 | 143,00 |
| Uranus | 84,00 | 287,00 |
| Neptune | 165,00 | 450,00 |
| Pluton | 248,00 | 590,00 |

</center>

## Affichage du carré de la période en fonction du cube du demi-grand axe

1. Une version du fichier de travail se trouve à <a href="https://replit.com/@dlatreyte/Troisieme-loi-de-Kepler-Eleves#main.py" target="_blank">cette adresse</a>. L'intégrer à son profil personnel sur <a href="https://replit.com" target="_blank">Replit</a> (<kbd>Fork repl</kbd>).

2. Construire la liste `T`, à la ligne 47, avec les valeurs données dans le tableau ci-dessus.

3. Même question pour la liste `a`, à la ligne 49.

4. Les périodes sont données en années. L'objectif des instructions, lignes 56 et 57, est de toutes les transformer en secondes.   
Écrire les instructions nécessaires.

5. `T_carre` est un tableau de même longueur que la la liste `T` formé uniquement de 0. L'objectif des instructions, lignes 61 et 62, est de garnir le tableau `T_carre` des valeurs de la liste `T` au carré.   
Écrire les instructions nécessaires.

6. `a_cube` est un tableau de même longueur que la la liste `a` formé uniquement de 0. L'objectif des instructions, lignes 66 et 67, est de garnir le tableau `a_cube` des valeurs de la liste `a` au cube.   
Écrire les instructions nécessaires.

7. La fonction `affichage` permet une construction simple d'un graphique $y = f(x)$. Compléter l'instruction de la fonction `plot` qui permet cet affichage, ligne 14.

8. Compléter l'appel de la fonciton `affichage`, ligne 70, de façon à ce que le graphique construit soit $T^2 = f(a^3)$.     
Examiner le résultat.

## Modélisation

11. La fonction `f_modelisation`, dont la définition débute à la ligne 37, est la fonction mathématique qui traduit le mieux comportement du jeu de données.    
Remplacer `pass` par la bonne instruction :
    - `return a * x`
    - `return a * x + b`
    - `return a * x**2 + b * x + c`
    - `return a * sin(b * x)`
    - `return a * log(x)`


Ajouter, au bas du document, avec les lignes de code suivantes (faire un copier-coller) :
```python
# Modélisation
popt, pcov = curve_fit(f_modelisation, a_cube,
                       T_carre)  # Calcul modélisation

# Affichage modélisation
affichage_modelisation(a_cube, T_carre, f_modelisation(a_cube, *popt))

# Constante de Kepler
K = popt[0]
print("Modélisation : T^2 = {} a^3".format(popt[0]))
``` 

12. La modélisation est-elle satisfaisante ? Noter la valeur de la constante de Képler.

## Détermination de la masse du Soleil

13. Définir, au bas du document, la variable `G` et lui affecter la valeur de la constante universelle de gravitation.

14. Définir la variable `MS` et lui affecter le résultat du calcul de la masse du Soleil.     
Utiliser les variables `K`, `MS`, `np.pi`.

15. Afficher la masse du Soleil à l'écran.