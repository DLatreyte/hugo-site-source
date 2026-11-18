---
title: "Modules et exceptions"
subtitle: ""
date: 2020-09-15T05:06:32+04:00
draft: false
toc: true
tags: ["Modules", "Exceptions"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: true
auto_numbering: true
weight: 100
---
{{< note goal >}}
Organiser son code en modules, importer un module ou certains de ses objets en connaissant les conséquences sur les espaces de noms, et gérer les exceptions pour écrire des programmes robustes.
{{< /note >}}

Avant de commencer, prévoir ce qu'affiche ce programme, puis vérifier.

```python
x = 10


def f() -> None:
    x = 5
    print(x)


f()
print(x)
```

{{< solution "Réponse" >}}
Le programme affiche 5 puis 10. L'affectation `x = 5` dans la fonction crée une **variable locale** `x`, différente de la variable globale `x`. Quand la fonction se termine, sa variable locale disparaît, et `print(x)` affiche la variable globale, qui n'a pas changé. Ce document explique ces règles de portée, et ce qu'elles deviennent quand on importe des modules.
{{< /solution >}}

Ce chapitre se concentre sur les modules de Python et sur les modalités
d'importation des données des modules dans l'environnement de travail.

{{< note tip >}}
L'objectif de ce document est de souligner l'importance d'un **code modulaire**,
c'est-à-dire d'un code qui&nbsp;:

- puisse être *utilisé dans plusieurs programmes*&nbsp;;
- puisse être *documenté* précisément&nbsp;;
- soit suffisamment compact pour *être étudié avec soin* et en particulier *testé*.
{{< /note >}}

## Qu'est-ce qu'un module&nbsp;?

{{< note tip >}}
*Un module permet d'organiser logiquement le code Python*.
{{< /note >}}

- Quand la taille du code augmente, il peut être pratique de le diviser en entités organisées qui
peuvent continuer à interagir.
- Un module permet aussi de se créer une «&nbsp;boîte à outils&nbsp;» contenant des fonctions appelées depuis
plusieurs programmes.
- Finalement, *un module permet de bénéficier du travail déjà effectué, maximisant ainsi la réutilisabilité du code*.

## Modules et fichiers

{{< note tip >}}
Si les modules représentent un moyen d'organiser **logiquement** le code
Python, les fichiers permettent quant à eux d'organiser **physiquement** le
code.
{{< /note >}}

À cette fin, *chaque fichier est considéré comme un module individuel,
et réciproquement*. *Le nom de fichier d'un module est le nom du module
auquel on ajoute l'extension* `.py`.

Un module peut contenir tout objet Python: *variables*, *fonctions*,
*classes*, $\ldots$

## Chemin de recherche et recherche de fichiers

L'importation de modules s'appuie sur le *chemin de recherche*&nbsp;:
c'est une liste de *répertoires (dossiers) du système de fichiers* dans lesquels Python cherche
le fichier du module. Cette liste dépend de l'installation de Python et du système d'exploitation utilisé. Par exemple&nbsp;:

```python
>>> import sys
>>> print(sys.path)
['', '/usr/lib/python312.zip', '/usr/lib/python3.12',
'/usr/lib/python3.12/lib-dynload',
'/home/eleve/.local/lib/python3.12/site-packages',
'/usr/lib/python3/dist-packages']
```

La chaîne vide `''` désigne le répertoire courant.

Dans le cas où la recherche d'un module échoue, une exception est levée par
l'interpréteur&nbsp;:

```python
>>> import xxx
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'xxx'
```

Puisque le *chemin de recherche* consiste à construire une liste de
répertoires (dossiers), il est possible de la modifier. Ajouter un répertoire à cette liste avec la méthode `append`
permet d'importer un module situé dans un répertoire absent du chemin de
recherche&nbsp;:

```python
>>> sys.path.append('/home/utilisateur/dossier-modules')
```

{{< note warning >}}
Il n'est pas nécessaire de modifier le *chemin de recherche* si le **fichier
module** se trouve *dans le même répertoire* que le fichier source
contenant le code qui importe le module.
{{< /note >}}

## Portée des variables et espaces de noms

{{< note tip >}}
La *portée* d'un identificateur est la portion du programme à laquelle sa
déclaration s'applique. On emploie également le terme de *visibilité*.

*Les variables définies dans une fonction ont une **portée locale**, celles
définies au plus haut niveau d'un module ont une **portée globale***.
{{< /note >}}

{{< note tip >}}
Les **variables globales** présentent une caractéristique notable&nbsp;: *à moins
qu'elles n'aient été détruites, leur durée de vie est égale à celle du
script qui s'exécute*. En revanche, les **variables locales**, comme le **bloc de
pile** dans lequel elles résident, *sont temporaires et ne
«&nbsp;vivent&nbsp;» que le temps pendant lequel les fonctions dans
lesquelles elles sont définies sont actives*.
{{< /note >}}

```python
>>> chaine_globale = "Salut"
>>> def bonjour() -> None:
...     chaine_locale = " la planète"
...     print(chaine_globale + chaine_locale)
...
>>> bonjour()
Salut la planète
>>> print(chaine_locale)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'chaine_locale' is not defined
```

<img src="/terminales-nsi/chap-2/fig-2-1-1.jpg" alt="" width="80%" />
> Durée de vie des variables locales et globales.

{{< note warning >}}
Dans le cas où une variable locale porte le même nom qu'une variable
globale, c'est la variable locale qui est utilisée. *Python cherche d'abord
dans l'espace de noms local avant de chercher dans l'espace de noms global.*
{{< /note >}}

```python
>>> chaine = "Bonjour"
>>> def au_revoir() -> None:
...     chaine = "Au revoir"
...     print(chaine)
...
>>> au_revoir()
Au revoir
>>> print(chaine)
Bonjour
```

Il est donc possible de «&nbsp;masquer&nbsp;» une variable globale, en utilisant une
variable locale de même nom.

{{< note normal >}}
*Lorsque l'interpréteur Python importe un module, les règles de portée
s'appliquent&nbsp;: si l'import se situe au niveau du module, sa portée est globale,
s'il se situe dans une fonction, sa portée est locale*.
{{< /note >}}

## Import de modules

### L'instruction `import`

{{< note tip >}}
L'import d'un module nécessite l'emploi de l'instruction `import`. La syntaxe
est la suivante&nbsp;:

```python
import os
```

{{< /note >}}

Il est possible d'importer plusieurs modules&nbsp;:

```python
import os
import sys
```

Lorsque l'interpréteur rencontre un `import`, le chemin de recherche est
utilisé pour accéder au module. Si celui-ci est trouvé, il est importé. Comme annoncé ci-dessus, les
règles de portée s'appliquent&nbsp;: *si l'import se situe au niveau du module, sa
portée est **globale**, s'il se situe dans une fonction, sa portée est **locale**.*

{{< note warning >}}
L'instruction `import` amène le module dans l'espace de noms, pas les objets qu'il
contient. La notation `.` doit être utilisée afin d'utiliser ces objets.
{{< /note >}}

```python
>>> import os
>>> print(name)
Traceback (most recent call last):
NameError: name 'name' is not defined
>>> print(os.name)
posix
```

{{< note tip >}}

#### Comment accéder à la liste des objets contenus dans un module&nbsp;?

On peut utiliser la fonction `dir`&nbsp;:

```python
>>> import os
>>> dir(os)
```

{{< /note >}}

{{< note tip >}}

#### Comment obtenir l'aide d'un module&nbsp;?

On peut utiliser la fonction `help`&nbsp;:

```python
>>> import os
>>> help(os)
```

{{< /note >}}

<img src="/terminales-nsi/chap-2/fig-2-1-2.jpg" alt="" width="80%" />
> Résultat de l'importation du module `os`. Aucune référence à l'attribut `name` n'existe dans l'espace de noms global.

#### Comment obtenir la liste de tous les modules importés par un programme&nbsp;?

```python
>>> dir()
```

### L'expression from ... import

{{< note tip >}}
Il est possible d'importer des objets particuliers d'un module dans le
programme. **L'objet appartient alors réellement à l'espace de noms du
programme**.

```python
>>> from os import name
>>> print(name)
posix
```

{{< /note >}}

#### Remarque

Ce type d'import peut présenter de réels dangers dans un programme dont le nombre de lignes est important et dont le développement s'effectue sur une longue durée. *Que se passe-t-il si, dans le programme principal, un attribut ou
une fonction portent le même nom que l'élément importé&nbsp;?*

```python
>>> def sinc(x: int) -> str:
...     return "coucou" * x
...
>>> sinc(3)
'coucoucoucoucoucou'
>>> from numpy import sinc
>>> sinc(2)
np.float64(-3.8981718325193755e-17)
```

La fonction `sinc` du programme a été remplacée, sans aucun message, par la fonction `sinc` du module `numpy`.

#### Remarque

Il existe une façon encore plus dangereuse d'utiliser l'expression `from ... import ...`&nbsp;:

```python
>>> from os import *
```

*Tous les objets contenus dans le module sont alors ajoutés à l'espace de noms
global du programme.*

{{< note warning >}}
Éviter le plus possible la forme d'importation&nbsp;: `from nom_module import *`&nbsp;!
{{< /note >}}

### L'instruction import ... as

Il arrive que l'on souhaite importer un module ou un attribut de module
portant un nom déjà employé dans l'application, ou que ce nom ne convienne
pas parce qu'il est trop long. On peut changer le nom lié localement du module
et procéder ensuite comme avec le nom complet&nbsp;:

```python
>>> import matplotlib.pyplot as plt
>>> plt.plot(x,y)
```

### Import vs chargement

{{< note tip >}}
Un module n'est *chargé* (son code n'est exécuté) qu'une seule fois, quel que soit le nombre de fois
où il est *importé*. Les importations suivantes réutilisent le module déjà chargé.
{{< /note >}}

### Exemple de création d'un module

1. Dans le fichier `demo.py`&nbsp;:

```python
"""
Un module de démonstration.
"""


# Fonctions du module
def b() -> str:
    """Retourne la chaîne "b"."""
    return "b"


def a() -> str:
    """Retourne la chaîne "a"."""
    return "a"


# Attributs (variables) du module
c = 2
d = 2

if __name__ == "__main__":  # test des fonctions du module
    assert b() == "b"  # place des assert
    assert a() == "a"
```

2. Dans l'interpréteur interactif, lancé depuis le dossier dans lequel on a enregistré le module `demo.py`&nbsp;:

```python
>>> import demo
>>> print(demo.b())
b
>>> demo.b()
'b'
>>> print(demo.c)
2
```

Quand on exécute `demo.py` directement, la variable `__name__` vaut `"__main__"` et les tests sont exécutés. Quand on importe le module, `__name__` vaut `"demo"`&nbsp;: les tests ne sont pas exécutés.

## Mécanisme de gestion des exceptions

Lorsqu'un problème intervient lors de l'exécution d'un programme (division
par zéro, tentative d'ouverture d'un fichier qui n'existe pas, erreur de
syntaxe, etc.), l'interpréteur passe dans un mode particulier dans lequel
il stoppe l'exécution du programme en cours et affiche une erreur&nbsp;:

```python
>>> 7 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero

>>> f = open("monfichier.txt", "r")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: 'monfichier.txt'

>>> 3 + message
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'message' is not defined

>>> while True print('Coucou !')
  File "<stdin>", line 1
    while True print('Coucou !')
               ^^^^^
SyntaxError: invalid syntax
```

{{< note tip >}}

#### Message d'erreur

Le message affiché contient le `traceback`, c'est-à-dire la pile d'appels&nbsp;: le chemin parcouru par l'interpréteur pour atteindre l'erreur (la liste des fonctions traversées pour atteindre l'erreur).  
Ce message comporte le **type d'exception** levée (`ZeroDivisionError`, `FileNotFoundError`, `NameError`, `SyntaxError`, etc.) et un **message** qui décrit le problème rencontré.
{{< /note >}}

#### Remarque

Dans le cas d'une erreur de syntaxe, *le message d'erreur indique même où est
détectée l'erreur à l'aide d'une flèche* (en fait, elle se trouve
généralement juste avant l'endroit pointé par la flèche).

{{< note tip >}}
Pour éviter que le programme ne se termine définitivement ou qu'il se
termine sans que la raison n'en soit explicite, il est conseillé de **gérer
les exceptions**.
{{< /note >}}

#### Exemple&nbsp;: Gestion des entrées du clavier

```python
while True:
    try:
        x = int(input("Entrer un nombre entier : "))
        break
    except ValueError:
        print("Oups ! Ce n'est pas un nombre entier. Nouvelle tentative.")
```

{{< note tip >}}
La gestion des exceptions repose sur quelques mots clés&nbsp;: `try`, `except`, `else`
et `finally` et sur une liste de types d'exceptions dont la liste peut être
consultée dans la [documentation en ligne de Python](https://docs.python.org/fr/3/library/exceptions.html)&nbsp;:

- `try`&nbsp;: le bloc de code qui suit ce mot clé est exécuté séquentiellement.
  En cas de problème, l'exécution est interrompue et l'interpréteur passe au
  bloc d'instructions suivant le mot clé except.
- `except NomErreur`&nbsp;: ce bloc d'instructions est exécuté si une erreur a
  été détectée dans le bloc try et si son type correspond à NomErreur.
Plusieurs clauses except peuvent être utilisées. Il n'est pas nécessaire
  d'indiquer le type de l'erreur (tous les types sont alors traités de façon
  identique).
- `else`&nbsp;: cette directive permet d'isoler dans la partie try la ou les
  instructions qui peuvent poser problème. Toutes les instructions suivantes
  (qui ne doivent donc être exécutées que si aucun problème n'intervient)
  peuvent être placées dans le bloc else.
- `finally`&nbsp;: le bloc qui suit est exécuté dans tous les cas de figure, qu'une
  exception ait été levée ou pas. C'est donc ici que l'on peut s'assurer
  qu'un fichier ouvert dans le bloc try est correctement fermé, quoi qu'il
  arrive.
{{< /note >}}

#### Exemple&nbsp;: Prise en compte de plusieurs erreurs

```python
try:
    f = open("fichier.txt", "r")
except OSError as err:
    print(f"Erreur d'entrée-sortie : {err}")
else:
    try:
        i = int(f.readline().strip())
    except ValueError:
        print("Je ne suis pas parvenu à convertir en entier la donnée.")
    finally:
        f.close()
```

Le fichier n'est fermé que s'il a pu être ouvert&nbsp;: si `open` échoue, la variable `f` n'existe pas, et `f.close()` provoquerait une nouvelle erreur. `OSError` regroupe les erreurs d'entrée-sortie, dont `FileNotFoundError`.

#### Utilisation de else

```python
try:
    f = open("fichier.txt", "r")
except OSError:
    print("Je ne parviens pas à lire le fichier.")
else:
    lignes = f.readlines()
    print(f"Le fichier comporte {len(lignes)} lignes.")
    f.close()
```

#### Les exceptions dans la définition d'une fonction

```python
def division(x: float, y: float) -> None:
    try:
        resultat = x / y
    except ZeroDivisionError:
        print("Division par zéro !")
    else:
        print(f"Le résultat est {resultat}")
    finally:
        print("Je suis toujours présent !")
```

```python
>>> division(2, 1)
Le résultat est 2.0
Je suis toujours présent !
>>> division(2, 0)
Division par zéro !
Je suis toujours présent !
```

Tout fichier manipulé doit être correctement fermé. Il n'est donc pas
envisageable d'utiliser la fonction `open` sans gérer les exceptions. Utiliser
les instructions `try`, `except` et `finally` peut cependant apparaître
contre-productif (cela fait beaucoup de code pour une action courante). `with`
permet de manipuler les fichiers en étant certain qu'ils seront fermés
correctement, *quoi qu'il arrive*.

```python
with open("fichier.txt", "r") as f:
    for ligne in f:
        print(ligne, end="")
```

Chaque ligne lue se termine déjà par un passage à la ligne&nbsp;: `end=""` évite que `print` en ajoute un second.

## Application

{{< note exercise >}}

1. Écrire un module nommé `convert_temp` contenant les fonctions réalisant les conversions entre des températures exprimées en degrés Celsius, degrés Fahrenheit et kelvins : `c_vers_f`, `f_vers_c`, `c_vers_k`, `k_vers_c`, `f_vers_k` et `k_vers_f`. On rappelle que $\theta_F = \dfrac{9}{5}\theta_C + 32$ et $T = \theta_C + \text{273,15}$.

2. Appeler ces fonctions depuis un autre programme.
{{< /note >}}

{{< note tip "Coup de pouce" >}}
Deux formules suffisent. Pour passer des degrés Fahrenheit aux kelvins, on peut passer par les degrés Celsius&nbsp;: `f_vers_k` peut appeler `f_vers_c` puis `c_vers_k`.
{{< /note >}}

{{< solution "Solution" >}}

Fichier `convert_temp.py`&nbsp;:

```python
"""
Conversions entre degrés Celsius, degrés Fahrenheit et kelvins.
"""


def c_vers_f(theta_c: float) -> float:
    """Convertit une température en degrés Celsius en degrés Fahrenheit."""
    return 9 / 5 * theta_c + 32


def f_vers_c(theta_f: float) -> float:
    """Convertit une température en degrés Fahrenheit en degrés Celsius."""
    return 5 / 9 * (theta_f - 32)


def c_vers_k(theta_c: float) -> float:
    """Convertit une température en degrés Celsius en kelvins."""
    return theta_c + 273.15


def k_vers_c(t: float) -> float:
    """Convertit une température en kelvins en degrés Celsius."""
    return t - 273.15


def f_vers_k(theta_f: float) -> float:
    """Convertit une température en degrés Fahrenheit en kelvins."""
    return c_vers_k(f_vers_c(theta_f))


def k_vers_f(t: float) -> float:
    """Convertit une température en kelvins en degrés Fahrenheit."""
    return c_vers_f(k_vers_c(t))


if __name__ == "__main__":
    assert c_vers_f(100) == 212
    assert f_vers_c(212) == 100
    assert abs(c_vers_k(25) - 298.15) < 1e-9
    assert abs(f_vers_k(32) - 273.15) < 1e-9
    assert abs(k_vers_f(273.15) - 32) < 1e-9
```

Programme qui utilise le module, enregistré dans le même dossier&nbsp;:

```python
import convert_temp

print(convert_temp.c_vers_f(37))  # environ 98.6
print(convert_temp.k_vers_c(0))  # -273.15
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- expliquer ce qu'est un module et pourquoi on découpe un programme en modules ;
- distinguer une variable locale d'une variable globale, et prévoir laquelle est utilisée ;
- importer un module avec `import`, `from … import` ou `import … as`, et expliquer les risques de `from module import *` ;
- écrire un module, avec des tests placés sous `if __name__ == "__main__":` ;
- lire un message d'erreur : type d'exception, message et pile d'appels ;
- gérer une exception avec `try`, `except`, `else` et `finally` ;
- ouvrir un fichier avec `with` pour être sûr qu'il sera fermé.
{{< /note >}}
