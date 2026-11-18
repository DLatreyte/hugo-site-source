---
title: "Fourniture et utilisation d'une API"
subtitle: ""
date: 2020-09-22T05:15:58+04:00
draft: false
toc: true
tags: ["Modules", "API", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: false
auto_numbering: true
weight: 400
---

{{< note goal >}}
Écrire un module en respectant une API donnée, le faire évoluer sans casser les programmes qui l'utilisent, et utiliser des paramètres avec valeur par défaut.
{{< /note >}}

Avant de commencer&nbsp;: on utilise tous les jours la fonction `print` ou la fonction `len` sans connaître leur code. Que faut-il savoir d'une fonction pour pouvoir l'utiliser correctement&nbsp;?

{{< solution "Réponse" >}}
Il suffit de connaître son nom, ce qu'elle attend (le nombre et le type des arguments, et les conditions qu'ils doivent respecter) et ce qu'elle retourne. C'est exactement ce que décrit une API&nbsp;: le «&nbsp;mode d'emploi&nbsp;» d'un ensemble de fonctions, indépendamment de leur code.
{{< /solution >}}

## API

Une API (en anglais « Application programming interface ») est une interface de programmation d'application. Elle est destinée à être utilisée par des programmes. Le principe de ce type d'interface est le même que celui des UI (« User Interface ») ou des GUI (« Graphical User Interface ») destinées elles à un utilisateur humain.

Composée de *constantes*, de *fonctions*, de *classes*, elle sert de *lien entre un programme et les programmes qui vont l'utiliser*. Elle peut être proposée par un service web avec une documentation décrivant l'utilisation qui permettra la communication et l'échange des données. Il existe, par exemple, plusieurs API de géolocalisation qui peuvent être intégrées à des programmes. Une API est très souvent proposée par une bibliothèque logicielle composée de fonctions destinées à être utilisées dans divers programmes.

Le principe de base est que le *fonctionnement interne n'a pas besoin d'être connu du programme utilisateur.* Cela nécessite une *documentation fournie décrivant précisément son utilisation*. Ainsi, lors de l'élaboration d'un logiciel il est possible d'utiliser des parties d'autres logiciels, sans connaître leur fonctionnement interne, si l'on sait comment faire interagir ces différentes parties.  
Par exemple, pour utiliser une fonction il suffit de connaître sa **spécification**, c'est-à-dire son **nom**, les **types de ses paramètres et de la valeur qu'elle retourne** et sa **documentation**. Dans tous les cas, l'utilisateur, un programme ou un humain, se contente de fournir les données demandées et obtient le résultat du traitement.

## Travail à réaliser

1. Créer un module dont l'API est la suivante :

```python
>>> help(aires)
Help on module aires:

NAME
    aires

DESCRIPTION
    Fourniture de fonctions calculant les surfaces
    de diverses figures géométriques.

FUNCTIONS
    disque(rayon: float) -> float
        Renvoie l'aire du disque de rayon rayon.

    rectangle(largeur: float, longueur: float) -> float
        Renvoie l'aire d'un rectangle de côtés largeur
        et longueur.

    triangle(base: float, hauteur: float) -> float
        Renvoie l'aire d'un triangle de base base et de
        hauteur hauteur.

DATA
    pi = 3.14159

FILE
    /home/runner/aires/aires.py
```

2. Créer, de la façon qui semblera la plus pertinente, un jeu de tests des fonctions, dans ce module. Les tests ne doivent pas être exécutés lorsque le module est importé.

3. Écrire un programme principal qui utilise ce module.

4. Expliquer quelle est la différence entre les deux spécifications suivantes :

```python
def disque(rayon: float) -> float:
    """
    Renvoie l'aire du disque de rayon rayon.
    """
```

et

```python
def disque(rayon: float) -> float:
    """
    Renvoie l'aire du disque de rayon rayon.

    HYPOTHÈSE : rayon >= 0
    """
```

5. On souhaite prendre en charge les cas où l'utilisateur fournirait une dimension négative (erronée donc).  
Modifier le code des fonctions de telle sorte qu'une exception de type `ValueError` soit levée chaque fois qu'une valeur négative est passée en argument.

**Remarque :** on pourra se renseigner sur l'utilisation du mot-clé `raise`.

## Stabilité d'une API

Il est important, lorsqu'on souhaite faire évoluer une API, de faire en sorte que les utilisateurs qui l'utilisaient déjà, avant la modification, puissent toujours le faire sans avoir à modifier le programme ou voir celui-ci ne plus fonctionner.
*Sauf décision volontaire qu'**il faudra communiquer aux utilisateurs**, l'évolution d'une API doit apporter de nouvelles fonctionnalités sans en retirer.*

Par exemple, on pourrait vouloir proposer aux utilisateurs la possibilité d'arrondir le résultat du calcul d'une aire.

6. Modifier le code des différentes fonctions de façon à ce qu'il ressemble à celui de la fonction `disque` ci-dessous (la partie sur la levée de l'exception `ValueError` n'est pas insérée dans le code proposé).
Vérifier que le programme écrit à la question 3. fonctionne toujours sans aucune modification.

```python
def disque(rayon: float, decimales: int | None = None) -> float:
    """
    Renvoie l'aire du disque de rayon rayon, arrondie à decimales
    chiffres après la virgule si decimales est fourni.
    """
    aire = pi * rayon * rayon
    if decimales is not None:
        aire = round(aire, decimales)
    return aire
```

L'annotation `int | None` signifie que `decimales` est soit un entier, soit la valeur spéciale `None`, qui indique ici qu'aucun arrondi n'est demandé.

7. En déduire comment se comportent, en Python, les paramètres d'une fonction auxquels on attribue des valeurs dans la signature.

8. Dans le programme principal modifier l'appel à la fonction `disque` de telle sorte que le résultat de son calcul soit arrondi à deux chiffres après la virgule.

9. Le code utilise la fonction intégrée au langage Python `round` pour arrondir un `float` à un certain nombre de chiffres après la virgule.  
Écrire sa propre fonction d'arrondi, nommée `arrondi` (pour ne pas masquer la fonction `round` de Python), en n'utilisant que les opérateurs `*`, `/`, `+`, `**` et la fonction `int`. On se limitera aux nombres positifs, ce qui suffit pour des aires.

{{< note tip "Coup de pouce" >}}
Pour la question 9 : `int` supprime la partie décimale d'un nombre positif. Pour arrondir 2,718 à deux décimales, on peut d'abord multiplier par $10^2$&nbsp;: comment obtenir alors 272 avec `int`, puis revenir à 2,72&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

1, 2, 5 et 6. Fichier `aires.py`&nbsp;:

```python
"""
Fourniture de fonctions calculant les surfaces
de diverses figures géométriques.
"""

pi = 3.14159


def disque(rayon: float, decimales: int | None = None) -> float:
    """
    Renvoie l'aire du disque de rayon rayon, arrondie à decimales
    chiffres après la virgule si decimales est fourni.
    """
    if rayon < 0:
        raise ValueError("Le rayon doit être positif.")
    aire = pi * rayon * rayon
    if decimales is not None:
        aire = round(aire, decimales)
    return aire


def rectangle(largeur: float, longueur: float, decimales: int | None = None) -> float:
    """
    Renvoie l'aire d'un rectangle de côtés largeur et longueur, arrondie
    à decimales chiffres après la virgule si decimales est fourni.
    """
    if largeur < 0 or longueur < 0:
        raise ValueError("Les côtés doivent être positifs.")
    aire = largeur * longueur
    if decimales is not None:
        aire = round(aire, decimales)
    return aire


def triangle(base: float, hauteur: float, decimales: int | None = None) -> float:
    """
    Renvoie l'aire d'un triangle de base base et de hauteur hauteur,
    arrondie à decimales chiffres après la virgule si decimales est fourni.
    """
    if base < 0 or hauteur < 0:
        raise ValueError("La base et la hauteur doivent être positives.")
    aire = base * hauteur / 2
    if decimales is not None:
        aire = round(aire, decimales)
    return aire


if __name__ == "__main__":
    assert disque(0) == 0
    assert disque(1) == pi
    assert rectangle(2, 3) == 6
    assert triangle(4, 3) == 6
    assert disque(2, 2) == 12.57
    try:
        disque(-1)
        assert False, "disque(-1) aurait dû lever ValueError"
    except ValueError:
        pass
```

Les tests sont placés dans le bloc `if __name__ == "__main__":`, exécuté seulement lorsque l'on lance `aires.py` directement.

3 et 8. Programme principal, enregistré dans le même dossier&nbsp;:

```python
import aires

print(aires.rectangle(2, 5))
print(aires.disque(2))  # 12.56636
print(aires.disque(2, 2))  # 12.57
```

4. La seconde spécification précise une **précondition**&nbsp;: la fonction n'est prévue que pour un rayon positif ou nul. La première ne dit rien du cas d'un rayon négatif&nbsp;: l'utilisateur ne sait pas s'il a le droit d'appeler `disque(-2)`, ni ce qu'il obtiendra.

7. Un paramètre auquel on attribue une valeur dans la signature est **facultatif**&nbsp;: si l'appel ne fournit pas d'argument pour ce paramètre, il prend sa valeur par défaut. Les anciens appels `disque(2)` restent donc valables, et l'API a évolué sans casser les programmes existants.

9. 

```python
def arrondi(x: float, decimales: int = 0) -> float:
    """
    Renvoie le nombre positif x arrondi à decimales chiffres après
    la virgule (arrondi au plus proche).
    """
    puissance = 10**decimales
    return int(x * puissance + 0.5) / puissance


assert arrondi(2.718, 2) == 2.72
assert arrondi(12.56636, 2) == 12.57
assert arrondi(2.5) == 3
```

Ajouter $0,5$ avant de supprimer la partie décimale avec `int` permet d'arrondir au plus proche plutôt que de tronquer. Remarque&nbsp;: `round(2.5)` vaut 2 en Python, car `round` arrondit les valeurs situées exactement au milieu vers le nombre pair le plus proche.

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- expliquer ce qu'est une API et pourquoi elle permet d'utiliser un code sans connaître son fonctionnement ;
- écrire un module qui respecte une API donnée, avec ses docstrings et ses tests ;
- préciser une précondition dans une spécification, et lever une exception `ValueError` quand elle n'est pas respectée ;
- ajouter un paramètre avec une valeur par défaut pour faire évoluer une API sans casser les programmes qui l'utilisent ;
- écrire une fonction d'arrondi à partir d'opérations élémentaires.
{{< /note >}}
