---
title: "Tri par sélection"
subtitle: ""
author: ""
type: ""
date: 2023-11-24T12:59:47+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

*La recherche d'un élément dans un tableau est beaucoup plus efficace si ce
tableau est ordonné*. À vrai dire, ce n'est pas en cours d'informatique que
vous avez découvert ceci : dans toutes les bibliothèques les livres sont
classés de façon à rendre leur recherche plus rapide !

{{% note normal %}}

Le tri des tableaux/listes permet de trouver rapidement les objets recherchés et facilite la recherche des valeurs extrêmes.

{{% /note %}}

La question que se propose d'aborder ce document est donc : « comment classer les éléments d'un tableau selon une relation d'ordre donnée ? ».

Cette question est suffisamment importante pour que de nombreux chercheurs se
soient penchés sur le problème et aient proposé plusieurs dizaines
d'algorithmes différents. Certains sont *spécifiques au données numériques*,
certains *copient les données dans une nouvelle structure ou une structure temporaire* (*ce qui réclame de l'espace en mémoire supplémentaire*), certains *effectuent un tri en place* (*c'est à dire dans le même espace mémoire*), certains sont *stables* (*ils préservent alors l'ordre initial des valeurs égales*), ...

Ce document aborde l'étude du tri par sélection.

## Du plus léger au plus lourd

Pour donner une idée de la difficulté du problème de tri, on peut utiliser le
petit jeu à [cette adresse](http://lwh.free.fr/pages/algo/tri/tri.htm).  
L'objectif est de trier quelques tonneaux (entre 3 et 10) par ordre de masse
croissante, la masse de chaque tonneau étant attribuée aléatoirement.  
On peut utiliser le « Glisser – Déposer » pour déplacer les tonneaux.

On dispose :

- d'une balance non étalonnée permettant de comparer les masses des tonneaux 2 à
2
- d'étagères pouvant servir de stockage intermédiaire.

{{% note normal %}}

Ce sont exactement les mêmes éléments que ceux dont dispose un ordinateur :
une **fonction de comparaison** et des **zones de stockage**.

{{% /note %}}

Le but ultime du jeu est évidemment de trier ces tonneaux en faisant le moins
de comparaisons et d'échanges possibles.

1. Limiter l'animation à trois tonneaux et trouver le tonneau le plus léger.
Décrire la méthode employée. Combien de comparaisons est-il nécessaire de
faire ?
{{% solution "Réponse" %}}

On compare les deux premiers tonneaux et on conserve le plus léger sur la
balance. On compare alors ce tonneau à celui qui reste dans la liste de
tonneaux. Deux comparaisons sont donc nécessaires.

{{% /solution %}}

2. Toujours à partir de trois tonneaux, les trier du plus léger au plus lourd.
Décrire la méthode employée (on peut schématiser toutes les étapes sur sa
feuille). Combien de comparaisons est-il nécessaire de faire ?
{{% solution "Réponse" %}}

Sans utilisation de la zone de stockage, il faut effectuer 3 comparaison. On peut se
contenter de deux comparaisons si on utilise la zone de stockage.

{{% /solution %}}

3. Choisir maintenant cinq tonneaux. Les trier du plus léger au plus lourd.
Décrire la méthode employée et indiquer combien de comparaisons ont été
effectuées.

4. (Facultatif) Toujours à partir de cinq tonneaux, essayer de trouver une autre
méthode permettant de les trier. La décrire.

## Algorithme de tri

{{% note tip %}}

Un **algorithme de tri** est, en informatique ou en mathématiques, un algorithme
qui permet d'organiser une collection d'objets selon un ordre déterminé.

Les objets à trier font donc partie d'un ensemble muni d'une relation d'ordre.
Les ordres les plus utilisés sont l'ordre numérique et l'ordre lexicographique
(dictionnaire).

{{% /note %}}

## Tri par sélection

### Introduction

La méthode du **tri par insertion** est expliquée à [cette adresse](https://youtu.be/AgFR0kO05RM), ou, de façon plus folklorique, à [cette adresse](https://youtu.be/0-W8OEwLebQ?si=k43jnksnMxiKil56).

**Remarque :** si la folie vous guette, évitez absolument [cette vidéo](https://youtu.be/92BfuxHn2XE?si=xPLRd7odBITzEPFl)... ou pas !

5. Visualiser la première vidéo (s'arrêter au bout de 4min40). Essayer de bien
comprendre la méthode.

6. Appliquer la méthode dans le jeu des tonneaux et trier cinq tonneaux du plus
léger au plus lourd. Cette méthode était-elle celle que vous aviez mise en
œuvre dans la section 1 ?

7. La méthode étant bien comprise, choisir sept cartes à jouer (avec les valeurs
numériques, pas des figures). Les placer en ligne au hasard sur une table et
les trier en appliquant le tri par sélection.  
**Se filmer pendant toute l'opération en commentant chacune des étapes !**

### Algorithme

{{% note normal %}}

À chaque étape du processus, le tableau est divisé en deux sous-tableaux : le
premier (indices plus petits que l'indice courant) est trié, le second
(indices plus grands que l'indice courant n'est pas encore trié). **On cherche,
à partir de la position courante, la plus petite valeur dans le sous-tableau
non trié (à droite) et une fois cette dernière trouvée, on permute (si
nécessaire) la valeur courante et la valeur la plus petite.**

{{% /note %}}

**Remarque :** La permutation des valeurs contenues dans deux variables est souvent employée en informatique, elle nécessite une troisième variable pour un stockage
temporaire.

{{% note tip %}}

Le **tri par sélection** est basé sur l'utilisation de deux boucles `Pour` imbriquées&nbsp;:

- La première boucle parcourt la liste des valeurs, de la première à l'avant dernière ;

- La seconde boucle recherche la plus petite valeur, de la position courante (compteur de la première boucle) à la fin du tableau, puis l'échange avec la position courante.

La partie gauche de la liste est donc triée au fur et à mesure de l'avancement
de la première boucle.

L'algorithme du tri par sélection est un algorithme de *tri en place* : la
réorganisation du tableau ne nécessite pas la création d'un nouveau tableau,
ce qui économise de la place en mémoire.

{{% /note %}}

8. À partir de toutes les informations précédentes, écrire l'algorithme du tri par sélection. Implémenter cet algorithme en Python.
{{% solution "Réponse" %}}

```python
from random import randint


def tri_selection(tab: list[int | float]) -> None:
    """
    Tri par sélection.
    """
    for i in range(len(tab) - 1):  # On s'arrête à l'avant-dernier élément
        val_min = tab[i]           # On sauvegarde la valeur courante
        for j in range(i + 1, len(tab)):  # On s'arrête au dernier élément
            if tab[j] < val_min:
                val_min = tab[j]   # On repère la valeur la plus petite
                j_min = j          # et son indice
        tab[j_min] = tab[i]
        tab[i] = val_min


if __name__ == "__main__":
    tab = [randint(1, 1000) for i in range(20)]
    print(tab)

    tri_selection(tab)
    print(tab)
```

{{% /solution %}}

9. Faire tourner « à la main » l'algorithme lorsque la fonction reçoit le tableau
`tab = [5,2,4,6,1,3]`.

10. Comment prouve-t-on, de façon générale, la terminaison d'un algorithme ?

11. Est-il nécessaire de prouver la terminaison de cet algorithme ?

12. Comment prouve-t-on, de façon générale, la correction d'un algorithme ?

13. Prouver que la proposition « Au début de chaque itération de la boucle `Pour` externe le tableau `tab[0, ..., i-1]` est un tableau trié constitué des `i` plus petits éléments du tableau `tab`, dans l'ordre croissant.» est un invariant de boucle.  
Prouver que l'algorithme est correct.

14. Déterminer la complexité de l'algorithme.

{{% note normal %}}

#### Dans quels cas le tri par sélection peut-il être pertinent ?

Le tri par sélection est globalement peu efficace. On peut tout de même lui attribuer quelques qualités :

- **Petites quantités de données :** Le tri par sélection peut être efficace pour trier de petites quantités de données. Sa complexité en temps est de l'ordre de $O(n^2)$, ce qui peut devenir inefficace pour des ensembles de données très importants. Pour des listes de taille modérée, le tri par sélection peut être simple à comprendre et à mettre en œuvre.

- **Complexité en espace :** Le tri par sélection n'a besoin que d'une quantité constante d'espace supplémentaire, ce qui signifie qu'il peut être plus efficace en termes de mémoire que d'autres algorithmes qui nécessitent une mémoire auxiliaire plus importante.

- **Stabilité :** Le tri par sélection est stable, ce qui signifie qu'il préserve l'ordre relatif des éléments égaux. Si la stabilité est une exigence, le tri par sélection peut être préférable dans certains cas.

- **Peu de mouvements d'éléments :** Bien que le tri par sélection effectue un nombre quadratique de comparaisons, le nombre de mouvements d'éléments est linéaire (*l'échange d'éléments n'a lieu qu'une seule fois à chaque itération*). Cela peut être avantageux dans des situations où le coût des comparaisons est faible par rapport au coût des déplacements d'éléments dans la mémoire.

{{% /note %}}
