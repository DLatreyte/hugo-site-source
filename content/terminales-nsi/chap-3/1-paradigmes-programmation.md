---
title: "Paradigmes de programmation"
subtitle: "Chapitre 3"
author: ""
type: ""
date: 2020-09-21T20:58:45+04:00
draft: false
toc: true
tags: ["Fonctionnelle", "Impérative", "Objet"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Langages de programmation

{{% note tip %}}
Un *langage de programmation* a besoin&nbsp;: 
- des règles de **grammaire** qui définissent la **syntaxe** des expressions&nbsp;;
- d'une **sémantique** qui définit le sens des expressions.
{{% /note %}}

{{% note tip %}}
Un langage peut être&nbsp;:
- **interprété**&nbsp;: un interpréteur *lit et analyse le code **séquentiellement**,* *le traduit en langage machine* et *lance son exécution*.
- **compilé**&nbsp;: un compilateur *lit et analyse le code* puis *le traduit en langage machine*. Par la suite l'exécutable généré peut être lancé.

**Remarque&nbsp;:** Python un langage interprété mais le code n'est pas directement traduit dans le langage machine de l'ordinateur sur lequel le programme est lancé mais dans le langage machine d'une machine virtuelle (bytecode). Dans un second temps, ce langage machine est interprété par le logiciel.
{{% /note %}}

{{% note warning %}}
Un compilateur n'est *pas obligé d'effectuer une lecture séquentielle* du fichier contenant le code&nbsp;; il peut donc davantage l'**analyser** (recherche d'**erreurs de typage** par exemple) et **effectuer des optimisations**.
{{% /note %}}

## Paradigme de programmation

{{% note tip %}}
On appelle **paradigme de programmation** une *façon de se représenter un problème informatique et sa résolution*.

Le paradigme choisi a une très grande influence sur la manière de concevoir un programme, il constitue donc un des critères principaux pour le choix d’un langage.
{{% /note %}}

Il existe un grand nombre de paradigmes de programmation, le programme de la NSI se concentre sur la **programmation impérative**, la **programmation fonctionnelle** et la **programmation objet**.

Certains langages sont très liés à certains paradigmes mais la plupart permettent de mettre en œuvre plusieurs paradigmes&nbsp;; c'est le cas de Python&nbsp;:
- **Impératif&nbsp;:** [Simple statements](https://docs.python.org/3/reference/simple_stmts.html) et [Compound statements](https://docs.python.org/3/reference/compound_stmts.html)&nbsp;;
- **Fonctionnel&nbsp;:** [Functional Programming HOWTO](https://docs.python.org/3/howto/functional.html)&nbsp;;
- **Objet&nbsp;:** [Classes](https://docs.python.org/3/tutorial/classes.html).


## Programmation impérative 
{{< remote "Wikipedia" "https://fr.wikipedia.org/wiki/Programmation_impérative" >}}

{{% note tip %}}
En *programmation impérative* les opérations sont décrites en **séquences d'instructions**, dont **l'ordre est déterminé par le programmeur**, et donc l'objectif est la **modification de l'état de la mémoire** (**variables**).
{{% /note %}}

Les «&nbsp;langages impératifs&nbsp;» sont les plus répandus parmi l'ensemble des langages de programmation et sont ceux qui sont les plus proches du fonctionnement des processeurs&nbsp;: *exécuter une suite d'instructions élémentaires*.

{{% note normal %}}
Les instructions de base de ce paradigme sont&nbsp;:
- la **séquence d'instructions**&nbsp;: les instructions sont exécutées les unes après les autres&nbsp;;
- l'**assignation** ou **affectation**&nbsp;: on stocke ou on modifie une information en mémoire (dans une variable)&nbsp;;
- l'**instruction conditionnelle**&nbsp;: un bloc d'instruction n'est effectué que si une certaine condition est réalisée&nbsp;;
- la **boucle**&nbsp;: une séquence d'instructions est répétée un certain nombre de fois (boucle `Pour`) ou jusqu'à ce qu'une condition soit réalisée.
- les **branchements**&nbsp;: la séquence d'instruction est transférée à un autre endroit dans le code.   
De nombreux langages incluent un `goto` permettant de réaliser un branchement ou la possibilité d'écrire des **fonctions** — qui ne sont dans ce cas qu'une suite d'instructions (et donc n'ont aucun sens mathématique).
{{% /note %}}

{{% note normal %}}
La programmation impérative s'appuie sur le modèle des machines à états, avec une **mémoire centrale** et des **instructions qui modifient son état** grâce à des **affectations** successives. Cela nécessite pour le programmeur d'avoir à tout instant un modèle exact de l'état de la mémoire que le programme modifie.
{{% /note %}}

#### Mots clés pour repérer un langage impératif
- affectation, mémoire, instruction, boucle, mutabilité, effets de bord, ...

#### Exemples de langages impératifs
- Langage machine, C, Bash, Perl, Tcl, Python, PHP, Java, JavaScript, ...

#### Usage typique
- Lorsque le programme à réaliser s’exprime sous forme d’actions à réaliser. Les actions reflètent les changements dans l’environnement (mémoire) du programme.
- Dans le cadre de la programmation système, pour une gestion manuelle, potentiellement fine, de l’allocation mémoire.

## Programmation fonctionnelle 
{{< remote "Wikipedia" "https://fr.wikipedia.org/wiki/Programmation_fonctionnelle" >}}

{{% note tip %}}
En *programmation fonctionnelle* un programme est considéré comme l'**application** (au sens mathématique du terme) d'une **fonction** à l'ensemble des données que le programme doit manipuler. Ce programme donne donc **toujours le même résultat pour les mêmes données** (pas d'effet de bord).
{{% /note %}}

{{% note normal %}}
- La programmation fonctionnelle s'affranchit de façon radicale des effets de bord en **interdisant toute opération d'affectation**. 
- La manipulation de variables est remplacée par la **composition de fonctions** (boîtes noires imbriquées les unes dans les autres).
- Les langages purement fonctionnels remplacent les boucles par la **récursivité**.
- Les langages fonctionnels mettent tous en œuvre une *gestion automatique de l'allocation mémoire*.
- Dans les langages fonctionnels les fonctions sont des **citoyennes de première classe**&nbsp;: *une fonction peut recevoir une fonction comme argument*, *une fonction peut retourner une fonction*.
{{% /note %}}

#### Remarque
- La mise en œuvre des langages fonctionnels fait un usage sophistiqué de la **pile** (cf. chapitre 1 sur la [récursivité]({{% ref "../chap-1/1-1-recursivite-sur-entiers.md" %}}) et chapitre 8 sur la [structure de pile]({{% relref "../chap-8/_index.md" %}})) car, *afin de s'affranchir de la nécessité de stocker des données temporaires dans des tableaux*, ils font largement appel à la **récursivité**. L'une des multiples techniques pour rendre la compilation de la récursivité plus efficace est une technique dénommée **récursion terminale** (en anglais&nbsp;: **tail-recursion**), qui consiste à *accumuler les résultats intermédiaires dans une case mémoire de la pile et à la passer en paramètre dans l'appel récursif*. Ceci permet d'*éviter d'empiler les appels récursifs dans la pile en les remplaçant par une simple succession de sauts*. Le code généré par le compilateur est alors similaire à celui généré par une boucle en impératif.

- La programmation fonctionnelle éliminant les effets de bord (*fonctions pures*), il est plus facile de faire effectuer des calculs en parallèle aux programmes développés dans un style fonctionnel pur.

#### Mots clés pour repérer un langage impératif
- déclaratif, expressions, immutabilité, ordre supérieur, $\lambda$-calcul, fonction pure, ...

#### Exemples de langages fonctionnels
- Haskell, Lisp, Scheme, OCaml, ...

#### Usage typique
- Manipulations de haut niveau&nbsp;;
- Calculs algébriques, abstraits&nbsp;; 
- Écriture de compilateurs.

## Comparaison des deux styles de programmation

{{% note exercise %}}
#### Exercice 1&nbsp;: illustration des différences entre les style impératif et fonctionnel

Définir une fonction qui réalise la somme des nombres d'une liste passée en argument,
1. En style impératif.
2. En style fonctionnel.
{{% /note %}}

1. **Style impératif**
{{< highlight py3 "linenos=table" >}}
from typing import List

def somme(liste: List[float]) -> float:
    """
    Calcule la somme des éléments de la liste liste.
    """
    somme = 0
    for nbre in liste:
        somme = somme + nbre
    return somme
{{< /highlight >}}
Cette fonction manipule la variable locale `somme` et utilise une boucle `for`. *Le paradigme utilisé est bien impératif.*

2. **Style fonctionnel**
{{< highlight py3 "linenos=table" >}}
from typing import List

def somme(liste: List[float]) -> float:
    """
    Calcule la somme des éléments de la liste liste.
    """
    if len(liste) == 0:
        return 0
    else:
        return liste[0] + somme(liste[1:])
{{< /highlight >}}
Cette fonction ne manipule aucune variable et n'utilise pas de boucle mais la récursivité. *Le paradigme employé est bien fonctionnel.*   

**Remarque :** `liste[1:]` est une sous-liste de `liste` dans laquelle le premier élément de `liste` n'est pas présent.

2. **Style fonctionnel avec récursion terminale**
{{< highlight py3 "linenos=table" >}}
from typing import List

def somme(liste: List[float], total: float = 0) -> float:
    """
    Calcule la somme des éléments de la liste liste.
    """
    if len(liste) == 0:
        return total
    else:
        return somme(liste[1:], liste[0] + total)
{{< /highlight >}}

{{% note warning %}}
*L'utilisation de la récursivité, seule, n'implique pas forcément que le paradigme de programmation utilisé est fonctionnel*. Il faut regarder l'ensemble du programme.
{{% /note %}}

{{% note exercise %}}
#### Exercice 2&nbsp;: un exemple de fonction non pure

Écrire une fonction (sans grand intérêt !!!) dont la spécification est la suivante :
```python
def elevation_puissance(n: int) -> float:
    """
    Retourne le nombre demandé à l'utilisateur à la puissance n.
    """
```
{{% /note %}}

{{< highlight py3 "linenos=table" >}}
def elevation_puissance(n: int) -> float:
    """
    Retourne le nombre demandé à l'utilisateur à la puissance n.
    """
    x = float(input("Veuillez entrer le nombre à élever à la puissance n : "))

    return x**n
{{< /highlight >}}

Il est évident que deux appels successifs à la fonction `elevation_puissance` avec le même argument (2 par exemple) pourront renvoyer des valeurs différentes puisque celles-ci dépendent de la valeur entrée par l'utilisateur. *Cette fonction n'est pas une fonction pure ; sa définition n'est pas acceptable du point de vue de la programmation fonctionnelle*.


{{% note exercise %}}
#### Exercice 3&nbsp;: illustration d'un effet de bord

Définir une fonction qui élève au carré chaque élément d'une liste.
1. En style impératif (avec effet de bord possible).
2. En style fonctionnel (sans effet de bord).
{{% /note %}}

1. Style impératif avec effet de bord.
{{< highlight py3 "linenos=table" >}}
from typing import List

def liste_carre(liste: List[float]) -> None:
    """
    Élève au carré chaque élément de la liste liste.
    """
    for i in range(len(liste)):
        liste[i] = liste[i]**2

l = [1, 2, 3, 4]
liste_carre(l)
{{< /highlight >}}
La fonction modifie la liste globale `liste`&nbsp;! Le problème a pour origine la mutabilité de la structure de données «&nbsp;liste&nbsp;» et le passage d'une *référence* à la fonction, et non pas une *copie de cette liste*.

{{< highlight py3 "linenos=table" >}}
from typing import List

def liste_carre(liste: List[float]) -> List[float]:
    """
    Élève au carré chaque élément de la liste liste.
    """
    newList = liste[:]
    
    def eleve_carre(liste: List[float]) -> List[float]:
        if len(liste) == 0:
            return liste
        else:
            return [liste[0]**2] + eleve_carre(liste[1:])
    
    return eleve_carre(newList)
{{< /highlight >}}
On copie dans un premier temps la liste et on agit sur cette nouvelle liste.   
À noter que cette copie n'était dans l'absolu pas nécessaire car l'opérateur `+` appliqué à des opérandes du type «&nbsp;séquence&nbsp;» génère une nouvelle liste en Python.


## Programmation objet

{{% note tip %}}
La **programmation objet** s'inspire du monde réel dans lequel des *objets créés à partir de patrons (ou moules) interagissent les uns avec les autres*.  
Mettre en œuvre ce paradigme nécessite donc de **modéliser le problème** *par une interaction d'objets dont on définit les caractéristiques*.
{{% /note %}}

{{% note tip %}}
- Un **objet** possède un **état** (des **champs** ou **attributs**) et un **comportement** (des **méthodes**).
- Une **classe** est un **patron** permettant de fabriquer des objets.   
    Une **classe** est aussi la définition d'un **nouveau type** de données.
{{% /note %}}

#### Mots clés pour repérer un langage objet
- classes ou prototype, objet, méthode, attribut, champ, statique, encapsulation, héritage, polymorphisme, ...

#### Exemples de langage orientés objets
- C++, Java, Python, OCaml, ...

#### Usage typique
- Développement en équipe de logiciels comportant un très grand nombre de lignes de code.