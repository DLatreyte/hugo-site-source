---
title: "Tri par insertion"
subtitle: ""
author: ""
type: ""
date: 2023-11-24T12:59:57+04:00
draft: false
toc: true
tags: ["Tri", "Invariant de boucle", "Variant de boucle", "Complexité"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Tri du joueur de cartes

<img src="/terminales-nsi/tris/insertion/cartes.png" alt="" width=40% style="float: right; padding-left: 6px;">

Le tri par insertion est un tri « naturel » souvent qualifié de « tri du
joueur de carte ».  
Comment un joueur de carte trie-t-il ses cartes ?

- Au début, la main gauche du joueur est vide et ses cartes sont posées sur la
table.
- Le joueur prend alors sur la table les cartes, une par une avec sa main
droite, pour les placer dans sa main gauche.
- Pour savoir où placer une carte dans son jeu, le joueur la compare avec
chacune des cartes déjà présentes dans sa main gauche, en examinant les cartes
de la droite vers la gauche.
- À tout moment, les cartes tenues par la main gauche sont triées ; ces cartes
étaient, à l'origine, les cartes situées au sommet de la pile sur la table.

1. Choisir sept cartes à jouer. Les placer en ligne au hasard sur une table et
mettre en œuvre la technique décrite ci-dessus.  
**Se filmer pendant toute l'opération en commentant chacune des étapes !**

## Tri par insertion

### Introduction

La méthode du tri par insertion est ilustré à [cette adresse](https://youtu.be/K4CuPzdiAIo), ou, de façon plus folklorique, à [cette adresse](https://youtu.be/ROalU379l3U).

**Remarque :** si la folie vous guette, évitez absolument [cette vidéo](https://youtu.be/8oJS1BMKE64?si=D9ws-_3cnR5qyJuL)... ou pas !

2. Visualiser la première vidéo (s'arrêter au bout de 4min40). Essayer de bien
comprendre la méthode.

3. La méthode étant bien comprise, choisir sept cartes à jouer (avec les valeurs
numériques, pas des figures). Les placer en ligne au hasard sur une table et
les trier en appliquant le tri par insertion.
**Se filmer pendant toute l'opération en commentant chacune des étapes !**

### Algorithme

{{% note normal %}}

À chaque étape du processus, le tableau est divisé en deux sous-tableaux : le
premier (indices plus petits que l'indice courant) est trié, le second
(indices plus grands que l'indice courant n'est pas encore trié). **On cherche
la place de l'élément courant (non encore trié) dans le tableau trié**.

{{% /note %}}

{{% note tip %}}

Le tri par insertion est basé sur l'utilisation de deux boucles imbriquées :

- La première boucle, une boucle `Pour`, parcourt la liste des valeurs, de la
deuxième à la dernière ;

- La seconde boucle, une boucle `TantQue`, cherche à placer l'élément courant
dans la première partie triée du tableau (indices inférieurs à l'indice
courant).

L'algorithme du *tri par insertion* est un algorithme de *tri en place*. La
réorganisation du tableau ne nécessite pas la création d'un nouveau tableau,
ce qui économise de la place en mémoire.
{{% /note %}}

4. À partir de toutes les informations précédentes, écrire l'algorithme du tri par insertion. Implémenter cet algorithme en Python.
{{% solution "Réponse" %}}

```python
def tri_insertion(tab: list[int | float | str]) -> None:
    """ Tri par insertion """
    for i in range(1, len(tab)):
        valeur = tab[i]   # Sauvegarde de la valeur en cours
    j = i - 1             # Indice de la boucle interne
        while tab[j] > valeur and j >= 0:
            tab[j + 1] = tab[j]  # On remonte la valeur plus grande
            j = j - 1
        tab[j + 1] = valeur      # On insère la valeur dans le tableau
```

{{% /solution %}}

5. Faire tourner « à la main » l'algorithme lorsque la fonction reçoit le tableau
`tab = [5,2,4,6,1,3]`.

6. Comment prouve-t-on, de façon générale, la terminaison d'un algorithme ?

7. Est-il nécessaire de prouver la terminaison de la boucle externe de cet
algorithme ? De la boucle interne ?

8. Démontrer la terminaison de cet algorithme.

9. Comment prouve-t-on, de façon générale, la correction d'un algorithme ?

10. Prouver que la proposition « Au début de chaque itération de la boucle `Pour` externe le tableau `tab[0, ..., i-1]` est un tableau trié dans l'ordre croissant.» est un invariant de boucle.  
Prouver que l'algorithme est correct.

11. Déterminer la complexité de l'algorithme.

{{% note normal %}}

Le tri par sélection est globalement peu efficace. On peut tout de même lui attribuer quelques qualités :

- **Pour de petites listes ou des données déjà partiellement triées :** Si vous avez une petite liste d'éléments à trier ou si votre liste est déjà partiellement triée, le tri par insertion peut être plus simple et rapide que d'autres méthodes.

- **Si vous voulez que l'ordre initial des éléments identiques soit préservé :** Le tri par insertion est une méthode « stable », ce qui signifie qu'il conserve l'ordre d'origine des éléments égaux. Cela peut être important dans certaines situations.

- **Lorsque vous ajoutez de nouveaux éléments à une liste déjà triée :** Le tri par insertion s'adapte bien lorsque vous ajoutez de nouveaux éléments à une liste déjà triée. En effet, la plupart des éléments sont déjà à leur place correcte ; le tri par insertion profite donc de cette caractéristique en minimisant le nombre d'opérations nécessaires pour insérer de nouveaux éléments car il peut sauter rapidement à travers la partie triée sans avoir à déplacer de nombreux éléments.

- **Si vous avez des contraintes de mémoire :** Le tri par insertion est un tri en place, il utilise une quantité constante de mémoire supplémentaire, ce qui peut être avantageux si vous avez des contraintes de mémoire.

{{% /note %}}
