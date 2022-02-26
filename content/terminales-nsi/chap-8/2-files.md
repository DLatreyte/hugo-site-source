---
title: "Les Files"
subtitle: "Chapitre 8,2"
author: ""
type: ""
date: 2020-10-31T22:50:06+04:00
draft: false
toc: true
tags: ["File", "Pile", "Liste chaînée", "Liste", "Tableau dynamique", "Complexité"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Rappel : Type de Données Abstrait (TDA)

Une structure de données ou type de données abstrait est un *moyen d'organiser et de manipuler les données en mémoire*. Un TDA est donc définit par :
- Son nom ;
- Sa spécification, c'est à dire la liste des manipulations/opérations que l'on peut ou pas effectuer.   
La spécification indique généralement la complexité de chacune des opérations prévues par le TDA.

{{% note warning %}}
Un type de données abstrait **ne dépend pas** de la manière dont la structure de données est implémentée dans le langage de programmation utilisé.  
Un TDA peut être implémenté de plusieurs façons différentes.
{{% /note %}}

## Qu'est-ce qu'une file ?

{{% note normal %}}
Une **file** est une structure de données abstraite dans laquelle *les données sont organisées comme le seraient des personnes dans une **file d'attente** (au guichet de la poste par exemple) :*
- à chaque fois qu'une personne arrive, elle se place à la fin de la file ;
- lorsqu'un guichet se libère, c'est la personne arrivée en premier parmi celles qui attendent qui est servie.
{{% /note %}}

{{% note tip %}}
#### Spécification d'une File de valeurs de type T
- **Créer** une file (type) : 
    - fonction : `creer_file()` $\longrightarrow$ retourne une file vide ;
    - complexité : $O(0)$ (pas tout à fait vrai mais suffisant pour comprendre la suite).
- **Enfiler** une valeur **à la fin** de la file :
    - fonction : `enfiler(f: File[T], valeur: T)` $\longrightarrow$ `None` ;
    - complexité : 1 opération élémentaire.
- **Accéder** à la valeur située au début de la file :
    - fonction : `lire(f: File[T])` $\longrightarrow$ retourne la première valeur de la file ;
    - Complexité : 1 opération élémentaire.
- **Retirer** la première valeur de la file :
    - fonction : `defiler(f : File[T])` $\longrightarrow$ `T` ;
    - complexité : 1 opération élémentaire.
- **Tester** si une file est vide :
    - fonction : `est_vide(f: File[T])` $\longrightarrow$ retourne un booléen ;
    - complexité : 1 opération élémentaire.
{{% /note %}}

{{% note warning %}}
La spécification d'une file montre qu'il n'existe aucune **opération élémentaire** pour&nbsp;:
- accéder à une donnée qui n'est pas la première de la file&nbsp;;
- déterminer combien de données contient la file.
- ...
{{% /note %}}

{{% note tip %}}
La valeur retirée de la file est toujours la première valeur à l'avoir intégrée&nbsp;: **First In, First Out (FIFO)**
{{% /note %}}

## Jeu de tests possibles

```python
if __name__ == "__main__":
	f = File()
	f.enfiler(1)
	f.enfiler(2)
	f.enfiler(3)
	f.enfiler(4)
	print(f.defiler())
	f.enfiler(5)
	print(f.defiler())
	print(f.defiler())
	print(f)
	print(f.defiler())
	print(f.defiler())
	print(f.defiler())
```

## Implémentation d'une structure de file à l'aide d'une liste Python

L'idée est de définir le type `File` à l'aide d'une classe ne possédant qu'un seul attribut nommé `contenu`, qui référence une liste, puis de créer les méthodes de la spécification.
On peut, par la suite, utiliser les méthodes des listes de Python.

1. Définir une classe nommée `File` et faire en sorte qu'à l'initialisation de tout objet de type `File`, l'attribut `contenu` référence une liste vide.

2. Écrire le code de la méthode `est_vide` de la spécification.

3. Écrire le code de la méthode `enfiler` de la spécification.

4. Écrire le code de la méthode `defiler` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de défiler une file vide.

5. Écrire le code de la méthode `lire` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de lire une file vide.

6. Tester le code.

7. La complexité de chacune des méthodes est égale à la complexité annoncée dans la spécification&nbsp;?

8. Comment pourrait-on améliorer la complexité de la méthode `defiler`&nbsp;?   
Modifier toutes les méthodes qui doivent l'être de façon à améliorer l'implémentation de la classe `File`.

{{% solution "Corrigé" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/fileliste" %}}
{{% /solution %}}

## Implémentation d'une structure de file à l'aide d'une liste chaînée

L'idée est de définir le type `File` à l'aide d'une classe ne possédant qu'un seul attribut nommé `contenu`, qui référence une liste chaînée, puis de créer les méthodes de la spécification.

1. Écrire le code de la classe `Cellule`, cellule d'une liste chaînée.

2. Définir une classe nommée `File` et faire en sorte qu'à l'initialisation de tout objet de type `File`, l'attribut `contenu` référence la liste vide.

3. Écrire le code de la méthode `est_vide` de la spécification.

4. Réfléchir au code de la méthode `enfiler` de la spécification et établir sa complexité. 

5. Afin de rendre le code performant, on utilise l'attribut `queue`. Cet attribut pointer toujours vers le dernier élément de la file.  
Ajouter l'attribut `queue` à la définition de la classe.

6. Écrire le code de la méthode `defiler` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de défiler une file vide.

7. Écrire le code de la méthode `lire` de la spécification.  
Cette méthode doit lever une exception de type `IndexError` lorsqu'on essaie de lire une file vide.

8. Tester le code.

{{% solution "Corrigé" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/filechaine" %}}
{{% /solution %}}


## Implémentation d'une structure de file à l'aide de deux piles

On considère dans cette partie le modèle d'un jeu de cartes où on disposerait d'une pioche, au sommet de laquelle on peut prendre des cartes (disposées face cachée), et d'une défausse au sommet de laquelle on peut reposer des cartes (disposées face apparente).  
Chacun de ces paquets est une pile. Ils forment la réserve de cartes.  
Les règles du jeu sont :
- toute carte prise dans la réserve est retirée dans l'une de ces piles (la pioche) ;
- toute carte remise dans la réserve est ajoutée à l'autre pile (la défausse).
On doit ajouter à ces règles une relation entre les deux paquets : une fois la pioche vide, on retourne la défausse pour en faire une nouvelle pioche, laissant à la place une défausse vide.

Cette gestion des cartes correspond à une structure de file : une fois la pioche initiale vidée, les cartes sont piochées précisément dans l'ordre dans lequel elles ont été défaussées. La première défaussée est la première piochée (FIFO).

1. Définir une classe nommée `File` et faire en sorte qu'à l'initialisation de tout objet de type `File`, les attributs `entree` et `sortie` soient créés en référencent deux piles vides.

2. Écrire le code de la méthode `est_vide` de la spécification.  
Une file est vide lorsque les deux piles sont vides.

3. Ajouter un nouvel élément à la file consiste à empiler cet élément sur la pile d'entrée.   
Écrire le code de la méthode `enfiler` de la spécification.

Pour retirer la première valeur de la pile deux cas sont à considérer :
- la pile de sortie n'est pas vide : la valeur est la dernière de cette pile. Il suffit donc de dépiler la pile de sortie.
- la pille de sortie est vide : il faut d'abord dépiler la pile d'entrée dans la pile de sortie puis dépiler cette pile de sortie.

4. Écrire le code de la méthode `defiler` de la spécification.

5. Écrire le code de la méthode `lire` de la spécification (le problème à considérer est très similaire à celui du retrait de la première valeur).

{{% solution "Corrigé" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/filepile" %}}
{{% /solution %}}

## À retenir

{{% note tip %}}
Une **file** est une structure de données de type **premier entré, premier sorti (FIFO)**. Elle peut être implémentée facilement à l'aide d'une liste chaînée, avec la structure de liste (tableau dynamique) de Python ou à l'aide de deux piles.
{{% /note %}}
