---
title: "Problème du sac à dos"
subtitle: "Chapitre 9,5"
author: ""
type: ""
date: 2021-01-21T06:41:30+04:00
draft: false
toc: true
tags: ["Sac à dos", "Arbres", "Glouton"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note warning %}}
{{< remote "À lire absolument pour en découvrir plus !" "https://interstices.info/le-probleme-du-sac-a-dos/" >}}
{{% /note %}}

## Introduction

<img src="/terminales-nsi/chap-9/chap-9-5/chap-9-5-1.png" alt="" width="45%" style="float: right; padding-left: 10px;" />
Dans ce document, on s'intéresse à une classe de problèmes d'optimisation connus sous le nom général de « problème du sac à dos ». On peut définir ce problème de la manière suivante : *« durant un cambriolage un voleur possède un sac dont la capacité (en poids par exemple) est limitée. Il se trouve face à un ensemble d'objets qu'il veut dérober. Chacun de ces objets est caractérisé par sa valeur et son poids. Le voleur souhaite optimiser la valeur totale des objets qu'il dérobe tout en ne dépassant pas le poids maximal supporté par son sac ».*

Ce problème est une abstraction pour un grand nombre d'autres problèmes d'optimisation. Il a été utilisé en cryptographie comme base pour différents schémas de chiffrement1. Il faut cependant noter que la plupart de ces schémas de chiffrement ne sont plus actuellement considérés comme sûrs. ^1, il est utilisé lors du chargement des bateaux ou d'avions, lors de la découpe de matériaux (minimisation des coupes « chutes » lors de la découpe), etc.

## Problème étudié

On considère un sac à dos de masse maximale $m = \pu{40 kg}$ dans lequel on souhaite ranger les objets dont les caractéristiques sont données ci-dessous :

<center>

| Objet  | A   | B   | C   | D   | E   | F   |
| :----- | :-: | :-: | :-: | :-: | :-: | :-: |
| Masse  | 13  | 12  | 8   | 10  | 14  | 18  |
| Valeur | 700 | 500 | 200 | 300 | 600 | 800 |

</center>

Quels objets faut-il sélectionner de façon à ce que la valeur totale, dans le sac à dos, soit maximale ?

<!-- Première partie : stratégie gloutonne -->
## Méthode de résolution approchée : stratégie gloutonne

{{% note normal %}}
Une solution se trouve à cette adresse : {{< remote "https://repl.it/@dlatreyte/sacados" "https://repl.it/@dlatreyte/sacados" >}}
{{% /note %}}

1. Rappeler ce qu'est une stratégie gloutonne.
{{% solution "Réponse" %}}
{{% note tip %}}
Les algorithmes gloutons forment une catégorie d'algorithmes permettant de parvenir à une solution pour un **problème d'optimisation** qui vise à maximiser/minimiser une quantité (plus court chemin (GPS), plus petite durée d'exécution, meilleure organisation d'un emploi du temps, etc.)

Le principe d'un algorithme glouton est le suivant :

- Résoudre un problème étape par étape ;
- À chaque étape, faire le choix optimal de moindre coût (de meilleur gain).

Le choix effectué à chaque étape n'est jamais remis en cause, ce qui fait que cette stratégie permet d'aboutir rapidement à une solution au problème de départ. C'est en ce sens que l'adjectif greedy (glouton/avare) caractérise cet algorithme : il se termine rapidement (glouton) sans fournir beaucoup d'efforts (avare).
{{% /note %}}

{{% /solution %}}

2. Importer les types `List`, `Dict` et `Tuple` du module `typing`.

3. Dans la fonction `main`, définir la liste objets dont les membres sont des dictionnaires représentant les différents objets du problème.\
    Chacun de ces dictionnaires doit donc posséder les clés `nom`, `masse`, `valeur` associées aux valeurs.
{{% solution "Solution" %}}
```python
objets = [{'nom': 'A', 'masse': 13, 'valeur': 700},
              {'nom': 'B', 'masse': 12, 'valeur': 500},
              {'nom': 'C', 'masse': 8, 'valeur': 200},
              {'nom': 'D', 'masse': 10, 'valeur': 300},
              {'nom': 'E', 'masse': 14, 'valeur': 600},
              {'nom': 'F', 'masse': 18, 'valeur': 800}
              ]
```
{{% /solution %}}

4. Dans la fonction `main`, définir la variable `masse_max` et lui affecter la valeur 40.
{{% solution "Solution" %}}
```python
masse_max = 40
``` 
{{% /solution %}}

Le principe de la stratégie gloutonne consiste à ajouter en priorité les objets « les plus efficaces ». « Plus efficace » ne signifie pas « plus grande valeur » mais « plus grande valeur comparativement à la masse ».

Avant d'appliquer l'algorithme glouton, il est nécessaire de trier la liste objets. Définir la fonction suivante :
```python
def tri_objets(objets: List[Dict]) -> List[Dict]:
    """
    Tri la liste de dictionnaires selon les rapports valeur/masse.
    """
    def recupere_rapports(objet):
        return objet['valeur'] / objet['masse']

    objets_tries = sorted(objets, key=recupere_rapports)

    return objets_tries
```

5. Quel concept propre à la programmation fonctionnelle la fonction `sorted` met-elle en œuvre ?
{{% solution "Solution" %}}
Une fonction en Python peut être passée comme argument à une autre fonction.
{{% /solution %}}

6. Décrire précisément la structure et le comportement de la fonction `tri_objets`.

7. Affecter, dans la fonction `main`, le résultat de l'appel de la fonction `tri_objets` à la variable `objets`. \
    Afficher à l'écran la liste triée.
{{% solution "Solution" %}}
```python
objets = tri_objets(objets)
print("Objets utilisables : {}".format(objets), end='\n')
```
{{% /solution %}}

Remarque. 
: Ne pas oublier d'appeler la fonction main.

8. Définir la fonction `construction_sac_a_dos` dont la spécification est :
```python
def constrution_sac_a_dos(objets_tries: List[Dict], 
                          masse_max: float) -> Tuple[List[str], int, int]:
    """
    Construction du sac à dos à partir d'une stratégie gloutonne.
    HYPOTHÈSE : la liste de dictionnaires est triée par ordre croissant des rapports
    valeurs/masses.

    Retourne un tuple constitué d'une liste contenant les noms des objets sélectionnés, 
    de la valeur du sac à dos et de la masse du sac à dos.
    """
```
{{% solution "Solution" %}}
```python
def constrution_sac_a_dos(objets_tries: List[Dict], masse_max: float) -> Tuple[List[str], int, int]:
    """
    Construction du sac à dos à partir d'une stratégie gloultonne.
    HYPOTHÈSE : la liste de dictionnaires est triée par ordre croissant des rapports
    valeurs/masses.

    Retourne un tuple constitué d'une liste contenant les noms des objets sélectionnés, 
    de la valeur du sac à dos et de la masse du sac à dos.
    """
    masse_sac = 0
    valeur = 0
    liste_objets = []

    i = len(objets_tries) - 1  # Compteur
    while i >= 0:
        objet = objets_tries[i]  # objet est un dictionnaire
        if (masse_sac + objet['masse']) <= masse_max:
            valeur += objet['valeur']
            masse_sac += objet['masse']
            liste_objets.append(objet['nom'])
    
        i -= 1  # Décrémentation du compteur

    return (liste_objets, valeur, masse_sac)
```
{{% /solution %}}

9. Affecter, dans la fonction `main`, le tuple retourné par la fonction construction_sac_a_dos aux variables sac_a_dos, valeur et masse_sac.
{{% solution "Solution" %}}
```python
sac_a_dos, valeur, masse_sac = constrution_sac_a_dos(objets, masse_max)
```
{{% /solution %}}

10. Afficher le résultat :
```python
print("Stratégie gloutonne")
print("-------------------")
print("Constitution du sac à dos : {}".format(sac_a_dos))
print("Masse du sac à dos : {}".format(masse_sac))
print("Valeur du sac à dos : {}".format(valeur))
print()
```


<!-- Deuxième partie : Arbre des possibilités -->
## Méthode de résolution exacte

Si on ne prend pas en compte, dans un premier temps, les contraintes, il est possible d'établir la liste des combinaisons possibles des objets à l'aide d'un **arbre d'exploration binaire**.

Par exemple, voici ce à quoi cet arbre ressemble lorsqu'on prend en compte les trois premiers objets :

{{< mermaid>}}
graph TD
V("" ) --> A
V --> V1(" ")
A --> C("A,B")
C --> D("A,B,C")
C --> E("A,B")
A --> F("A")
F --> G("A,C")
F --> H("A")
V1 --> I("B")
I --> J("B,C")
I --> K("B")
V1 --> V2(" ")
V2 --> L("C")
V2 --> M(" ")
{{< /mermaid >}}

Les combinaisons s'obtiennent en parcourant l'arbre du sommet jusqu'à chaque extrémité : on obtient alors un vecteur dont on peut calculer la poids et la valeur. Il suffit alors de retenir celui dont la masse est inférieure à la masse maximale et dont la valeur est alors maximale.

11. Au niveau de chaque nœud à quoi correspond le chemin « gauche » : objet retenu ou objet non retenu ?
{{% solution "Réponse" %}}
Objet retenu.
{{% /solution %}}

12. Compléter l'arbre avec l'objet D.

13. Si on implémente un algorithme mettant en œuvre la technique présentée ici, on trouve comme solution [A,C,F]. Vérifier que cette solution est meilleure que celle donnée par l'algorithme glouton.\
    Pourquoi cette méthode n'est cependant pas utilisable la plupart du temps ? Quel est le nombre de combinaisons possibles ?
{{% solution "Réponse" %}}
Le nombre de combinaisons est $2^n$ où $n$ est le nombre d'objets. Cette croissance exponentielle rend l'algorithme exact beaucoup trop lent.
{{% /solution %}}

14. Écrire le code de la fonction `masse_sac` dont la spécification est :
```python
def masse_sac(objets: List[Dict[str, str]], liste_obj: List[int]) -> int:
    """
    Calcule la masse du sac pour la liste d'objets retenus liste_obj.
    """
```

15. Écrire le code de la fonction `calcul_valeur_sac` dont la spécification est :
```python
def calcul_valeur_sac(objets: List[Dict[str, str]],
                      liste_obj: List[int]) -> int:
    """
    Calcule la masse du sac pour la liste d'objets retenus liste_obj.
    """
```

16. Écrire le code suivant :
```python
def recherche_recursive(objets: List[Dict[str, str]], masse_max: isinstance,
                        list_obj: List[int], i: int) -> List[int]:
    """
    Détermine le chemin de l'arbre de décision correspondant à la valeur optimale
    pour une masse du sac déterminée.
    """
    if i == len(objets):
        return list_obj[:]

    val1 = -1  # Initialisation à une valeur impossible du poids
    if objets[i]['masse'] <= masse_max - masse_sac(
            objets, list_obj):  # Ajoute objet si m_sac - m_inter > 0
        list_obj[i] = 1
        sol1 = recherche_recursive(objets, masse_max, list_obj, i + 1)
        val1 = calcul_valeur_sac(objets, sol1)

    list_obj[i] = 0  # On n'ajoute pas l'objet
    sol2 = recherche_recursive(objets, masse_max, list_obj, i + 1)
    val2 = calcul_valeur_sac(objets, sol2)

    if val1 > val2:
        return sol1[:]
    else:
        return sol2[:]
```
    Examiner cette fonction

