---
title: "Les Piles"
subtitle: "Chapitre 8,1"
author: ""
type: ""
date: 2020-10-27T03:40:03+04:00
draft: false
toc: true
tags: ["Pile", "Liste", "Liste chaînée", "Complexité", "Classe"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Rappel&nbsp;: Type de Données Abstrait (TDA)

Une structure de données ou type de données abstrait est un *moyen d'organiser et de manipuler les données en mémoire*. Un TDA est donc définit par&nbsp;:
- Son nom&nbsp;;
- Sa spécification, c'est à dire la liste des manipulations/opérations que l'on peut ou pas effectuer.   
La spécification indique généralement la complexité de chacune des opérations prévues par le TDA.

{{% note warning %}}
Un type de données abstrait **ne dépend pas** de la manière dont la structure de données est implémentée dans le langage de programmation utilisé.  
Un TDA peut être implémenté de plusieurs façons différentes.
{{% /note %}}

## Qu'est-ce qu'une pile ?

{{% note normal %}}
Une **pile** est une structure de données abstraite dans laquelle *les données sont organisées comme le seraient des assiettes dans une pile d'assiettes contenue dans une boite de profondeur quelconque mais étroite* (ce qui empêche de manipuler les assiettes par le côté).  
On peut donc seulement&nbsp;:
- Empiler une nouvelle assiette au-dessus des autres assiettes (ou d'aucune assiette si la pile est vide)&nbsp;;
- Retirer l'assiette située tout en haut de la pile&nbsp;;
- Regarder l'assiette située tout en haut de la pile&nbsp;;
- Regarder si la pile est vide.
{{% /note %}}


{{% note tip %}}
#### Spécification d'une Pile de valeurs de type T
- **Créer** une pile (type)&nbsp;: 
    - fonction&nbsp;: `creer_pile()` $\longrightarrow$ retourne une pile vide&nbsp;;
    - complexité&nbsp;: $O(0)$ (pas tout à fait vrai mais suffisant pour comprendre la suite).
- **Empiler** une valeur en **haut** de la pile&nbsp;:
    - fonction&nbsp;: `empiler(p: Pile[T], valeur: T)` $\longrightarrow$ `None`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Accéder** à la valeur située tout en haut de la pile&nbsp;:
    - fonction&nbsp;: `lire(p: Pile[T])` $\longrightarrow$ retourne la dernière valeur de la pile&nbsp;;
    - Complexité&nbsp;: 1 opération élémentaire.
- **Retirer** la dernière valeur de la pile&nbsp;:
    - fonction&nbsp;: `depiler(p: Pile[T])` $\longrightarrow$ `T`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Tester** si une pile est vide&nbsp;:
    - fonction&nbsp;: `est_vide(p: Pile[T])` $\longrightarrow$ retourne un booléen&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
{{% /note %}}

{{% note warning %}}
La spécification d'une pile montre qu'il n'existe aucune **opération élémentaire** pour&nbsp;:
- accéder à une donnée qui n'est pas sur le haut de la pile&nbsp;;
- déterminer combien de données contient la pile.
- ...
{{% /note %}}

{{% note tip %}}
La valeur dépilée est toujours la dernière valeur à avoir intégré la pile&nbsp;: **Last In, First Out (LIFO)**
{{% /note %}}


{{% note exercise %}}
#### Exemple d'utilisation d'une pile 
Tout navigateur possède un bouton permettant de retourner sur des pages que l'on a déjà consultées.  
Expliquer quelle structure de données permet de réaliser cette opération simplement et décrire les opérations en jeu.
{{% /note %}}


## Implémentation d'une structure de Pile à l'aide d'une liste Python

L'idée est de définir le type `Pile` à l'aide d'une classe ne possédant qu'un seul attribut nommé `contenu`, qui référence une liste, puis de créer les méthodes de la spécification.
On peut, par la suite, utiliser les méthodes des listes de Python.

1. Définir une classe nommée `Pile` et faire en sorte qu'à l'initialisation de tout objet de type `Pile`, l'attribut `contenu` référence une liste vide.

2. Écrire le code de la méthode `est_vide` de la spécification.

3. Écrire le code de la méthode `empiler` de la spécification.

4. Écrire le code de la méthode `depiler` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de dépiler une pile vide.

5. Écrire le code de la méthode `lire` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de lire une pile vide.

6. Tester le code.

7. Vérifier que la complexité de chacune des méthodes est égale à la complexité annoncée dans la spécification.

- {{< remote "Accès au corrigé" "https://repl.it/@dlatreyte/pileslistes" >}}

{{% note normal %}}
L'implémentation à l'aide des listes Python est efficace car, en moyenne, les méthodes `append` et `pop`, s'exécutent en temps constant. Tous les langages ne présentent cependant pas la structure de tableau dynamique et une autre implémentation doit alors être mise en œuvre.
{{% /note %}}

#### Jeu de tests possible
```python
if __name__ == "__main__":
    p = Pile()
    p.empiler(2)
    print(p.lire())
    p.empiler(42)
    p.empiler(89)
    p.empiler(23)
    print(p.lire())
    print(p.depiler())
    print(p.lire())
    print(p.depiler())
    print(p.lire())
    print(p.depiler())
    print(p.lire())
    print(p.depiler())
    print(p.depiler())
```

## Implémentation d'une structure de Pile à l'aide d'une liste chaînée

L'idée est de définir le type `Pile` à l'aide d'une classe ne possédant qu'un seul attribut nommé `contenu`, qui référence une liste chaînée, puis de créer les méthodes de la spécification.

1. Écrire le code de la classe `Cellule`, cellule d'une liste chaînée.

2. Définir une classe nommée `Pile` et faire en sorte qu'à l'initialisation de tout objet de type `Pile`, l'attribut `contenu` référence la liste vide.

3. Écrire le code de la méthode `est_vide` de la spécification.

4. Écrire le code de la méthode `empiler` de la spécification.  
**Attention à bien choisir la façon d'empiler la valeur. On peut passer d'une complexité en $O(1)$ à une complexité en $O(N)$&nbsp;!**

5. Écrire le code de la méthode `depiler` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de dépiler une pile vide.

6. Écrire le code de la méthode `lire` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de lire une pile vide.

7. Tester le code.

8. Vérifier que la complexité de chacune des méthodes est égale à la complexité annoncée dans la spécification.

- {{< remote "Accès au corrigé" "https://repl.it/@dlatreyte/pileschaines" >}}

#### Jeu de tests possible
```python
if __name__ == "__main__":
    p = Pile()
    p.empiler(2)
    print(p)
    p.empiler(42)
    p.empiler(89)
    p.empiler(23)
    print(p)
    print(p.depiler())
    print(p)
    print(p.depiler())
    print(p)
    print(p.depiler())
    print(p.depiler())
    print(p.depiler())
    print(p.depiler())
```

## À retenir

{{% note tip %}}
Une **pile** est une structure de données de type **dernier entré, premier sorti (LIFO)**. Elle peut être implémentée facilement à l'aide d'une liste chaînée ou avec la structure de liste (tableau dynamique) de Python.
{{% /note %}}


## Exercices

{{% note exercise %}}
#### Exercice 1
- Compléter le code de la classe `Pile` (version liste chaînée) en ajoutant les méthodes `vider` et `taille`.
- Évaluer approximativement le nombre d'opérations élémentaires de la structure `Pile` effectuées par la méthode `taille`.
{{% /note %}}

{{% note exercise %}}
#### Exercice 2
Pour améliorer la complexité de la méthode `taille` on ajoute l'attribut `taille` à la classe `Pile`.  
Reprendre le code de la classe `Pile` en modifiant toutes les méthodes qui doivent l'être.
{{% /note %}}

{{% solution "Solutions" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/stack" %}}
{{% /solution %}}

{{% note exercise %}}
#### Exercice 3
L'écriture **polonaise inverse** des expressions mathématiques place l'opérateur après ses opérandes. Cette notation ne nécessite ni l'utilisation des parenthèses ni la définition des règles de priorité des opérateurs.   
Ainsi l'expression l'expression $(1 + 2 \times 3) \times 4$ s'écrit $1\\ 2\\ 3\\ \times\\ +\\ 4\\ \times$.

La valeur d'une telle expression peut être calculée facilement en utilisant une pile pour stocker les résultats intermédiaires. Pour cela, on observer un à un les éléments de l'expression et on effectue les actions suivantes&nbsp;:
- si on voit un nombre, on le place sur la pile&nbsp;;
- si on voit un opérateur binaire, on récupère les deux nombres au sommet de la pile, on leur applique l'opérateur, et on replace le résultat au sommet de la pile.

Si l'expression est bien écrite, il doit toujours y avoir deux nombres sur la pile lorsqu'un opérateur apparaît et à la fin du processus il ne doit rester qu'un seul nombre sur la pile. Ce nombre est le résultat.  
L'opérateur unaire $-$ (l'opposé) devra être considéré comme un opérateur binaire dans cette implémentation&nbsp;: $-3$ sera donc écrit $0\\ 3\\ -$.

Écrire une fonction prenant en paramètre une chaîne de caractères représentant une expression en notation polonaise inverse composée d'additions et de multiplications de nombres entiers et renvoyant la valeur de cette expression. On supposera que les éléments de cette expression sont séparés par des espaces.   
Attention, cette fonction ne doit pas renvoyer de résultat si l'expression est mal écrite.
{{% /note %}}

{{% solution "Solution" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/polonaiseinverse" %}}
{{% /solution %}}

