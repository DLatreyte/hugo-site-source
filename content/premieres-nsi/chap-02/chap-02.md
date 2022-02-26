---
title: "Langages et programmation"
subtitle: "Chapitre 2,1"
toc: true
date: 2019-09-14T21:37:45+04:00
draft: false
tags: ["Fonctions", "Typage", "Signature d'une fonction", "Spécification d'une fonction", "Python"]
categories: ["Première Spé NSI"]
solution_est_visible: true
auto_numbering: true

---
[^1]: Nous reviendrons sur ce point plus tard dans l'année.


## À quoi a-t-on accès lorsqu'on utilise un langage de programmation ?

{{% note tip %}}
Un langage de programmation doit :

- fournir des **objets (ou types) primitifs** ;
- posséder une bibliothèque de **fonctions prédéfinies** ;
- permettre la **manipulation des objets primitifs et des fonctions prédéfinies** ;
- établir des règles qui permettent de **construire de nouveaux objets (ou types)** ou de nouvelles fonctions par *combinaison des types primitifs et des fonctions prédéfinies*.
{{% /note %}}


Nous allons aborder chacun de ces points.

## Quelques objets primitifs en Python

Le langage Python possède un grand nombre d'*objets primitifs*. Parmi eux, on utilisera lors des premiers chapitres :

- Les **constantes entières** (« Integer », `int`)

```python3
>>> type(3)
<type 'int'>
>>> type(-10)
<type 'int'>
```

- Les **constantes « flottantes »** (type `float`). Il s'agit d'une *approximations des nombres non entiers*[^1].

```python3
>>> type(0.1)
<type 'float'>
>>> type(-2.9)
<type 'float'>
>>> type(2e3)
<type 'float'>
```

- Les **valeurs booléennes** (type `bool`) `True` et `False`.

```python3
>>> type(True)
<type 'bool'>
>>> type(False)
<type 'bool'>
```

- Les **chaînes de caractères** (« String », type `str`).

```python3
>>> type("abcd")
<type 'str'>
>>> type('abcd')
<type 'str'>
>>> type('a')
<type 'str'>
```

## Syntaxe et évaluation d'une expression en Python


{{% note tip %}}
En mathématique et en informatique une expression est une formule exprimant la façon de calculer une valeur.
{{% /note %}}


### Ambigüité de l'écriture traditionnelle des expressions

En mathématique on écrit l'expression qui permet de calculer la valeur du polynôme du second degrés, pour toute valeur de la variable $x$ : $3 x^2 + 2 x + 4$. En programmation, peut-on se contenter d'utiliser la syntaxe des mathématiques ?  
Si on se penche un peu plus attentivement sur l'écriture du polynôme, on remarque :

- qu'il faut savoir que $2 x$ signifie la multiplication du nombre 2 par $x$ ;
  
- que pour $3 x^2$ il faut d'abord élever $x$ à la puissance 2 avant de multiplier le résultat par 3 ;
  
- que $2 x + 4$ n'est pas 2 multiplié par le résultat du calcul de $x + 4$ ;
  
- que cette écriture est une écriture à deux dimensions (élévation à la puissance 2 est indiquée en augmentant l'espace depuis la ligne de base).

De même, en mathématique, on écrit :

- $a + b$ : l'opérateur $+$ est entre les deux opérandes ;
  
- $\sin (x)$ : la fonction est placée avant son argument ;
  
- $f'$ pour indiquer la fonction dérivée de la fonction $f$ (le symbole de la dérivée est placé après le nom de la fonction).

En conclusion, l'écriture mathématique traditionnelle nous parait claire *car on l'utilise depuis les plus petites classes et parce qu'on a appris des règles telles que celles de la priorité des opérateurs*. *En informatique, la syntaxe devra être plus rigoureuse, moins ambiguë car la machine effectuera une vérification pointilleuse de tout ce qui sera écrit.*

L'écriture la plus rigoureuse du polynôme est : $\left( \left( 3 \times \left( x^2 \right) \right) + \left( \left( 2 \times x \right) + 4 \right) \right)$, heureusement le langage Python a intégré la règle de priorité des opérateurs et on pourra écrire : `3 * x** 2 + 2 * x + 4`.


**Remarque :** Les expressions en informatique ne se limitent bien évidemment pas au domaine des mathématiques.


### Opérateurs arithmétiques en Python


Les opérateurs en Python se répartissent en trois catégories :

- les **opérateurs arithmétiques**, utilisés pour calculer des expressions ;

- les **opérateurs de comparaison et les opérateurs logiques**, utilisés dans l'*alternative* ;
  
- les **opérateurs d'affectation**, utilisés pour modifier la « valeur » d'une variable.

Dans ce chapitre nous allons nous contenter d'utiliser les opérateurs arithmétiques.

| Opérateur |  Expression  | Description                                                                         |
| :-------: | :----------: | :---------------------------------------------------------------------------------- |
|    `+`    | `op1 + op2`  | renvoie le résultat de l'addition de `op1` et `op2`                                 |
|    `-`    | `op1 - op2`  | renvoie le résultat de la soustraction de `op1` et `op2`                            |
|    `-`    |    `-op`     | renvoie la valeur opposée de `op`                                                   |
|    `*`    | `op1 * op2`  | renvoie le résultat de la multiplication de `op1` et `op2`                          |
|    `/`    | `op1 / op2`  | renvoie le résultat de la division de `op1` et `op2`                                |
|   `//`    | `op1 // op2` | renvoie le résultat de la division euclidienne (le quotient donc) de `op1` et `op2` |
|    `%`    | `op1 % op2`  | renvoie le reste de la division euclidienne de `op1` et `op2`                       |
|   `**`    |  `op**exp`   | renvoie le résultat de `op` à la puissance `exp`                                    |


{{% note warning %}}
- Le résultat de la **division de deux nombres** est toujours un `float`, *même s'il s'agit de la division de deux nombres entiers*.
  
- Le résultat de la **division euclidienne** de deux nombres est un `float` si l'un des nombres est un `float`, un `int` si les deux nombres sont des entiers.
{{% /note %}}


{{% note exercise %}}
#### Exercice 1.
 
Utiliser l'éditeur de texte Thonny pour visualiser toutes les étapes de l'évaluation de l'expression $2 \times (3 + 4, 3)^3 + 5 \times 6^2$.
{{% /note %}}

{{% solution "Solution 1" %}}

- Écrire dans la fenêtre principale : `2 * (3 + 4.3)**3 + 5 * 6**2`.

- Lancer la commande : Run $\rightarrow$ Debug current script (touches <kbd>Ctrl + F5</kbd>). Un rectangle jaune doit apparaître à l'écran. Il indique la partie de l'expression que Python va évaluer au « pas » suivant.

- Progresser pas à pas grâce à la commande Run $\rightarrow$ Step into  (touche <kbd>F7</kbd>) en notant à chaque fois ce qui est évalué et le résultat de l'évaluation.
{{% /solution %}}

## Application d'une fonction


### Schéma-bloc d'une fonction


{{% note tip %}}
On appelle schéma-bloc la modélisation du fonctionnement d'une fonction.  Cette modélisation est affichée sous forme graphique.
{{% /note %}}


Par exemple, le schéma-bloc de la fonction « mise au carré » est le suivant :

<img src="/premieres-nsi/chap-02/fonction.svg" width="80%" alt="Schéma bloc d'une fonction" />

Ce schéma indique que la fonction attend un argument (le nombre 2), effectue un traitement (élévation à la puissance 2) et retourne une valeur (le nombre 4).


### Fonctions intégrées du langage Python


Le langage Python possède de nombreuses fonctions prédéfinies. Les fonctions intégrées `dir` et `help` permettent de les découvrir.

```python3
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> dir('__builtins__')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
```

L'exemple ci-dessus pourrait laisser penser que le nombre de fonctions n'est pas aussi grand qu'annoncé. Elles sont en fait organisées au sein de modules : `math`, `random`, `time` qu'il faut importer au préalable pour pouvoir les utiliser.

```python3
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(math.tan)
Help on built-in function tan in module math:

tan(x, /)
    Return the tangent of x (measured in radians).
>>> import random
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_os', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> help(random.random)
Help on built-in function random:

random(...) method of random.Random instance
    random() -> x in the interval [0, 1).
```

**Remarque :** On constate que pour utiliser une fonction contenue dans le module de nom `module`, on doit utiliser la syntaxe `module.nom_de_la_fonction`.

{{% note warning %}}
Les fonctions intégrées `dir` et `help` sont très importantes. Il faut apprendre à les utiliser le plus rapidement possible.
{{% /note %}}


### Syntaxe de l'application d'une fonction

L'appel (ou l'application) d'une fonction obéit à une syntaxe bien particulière, semblable à celle utilisée en math. Par exemple, l'appel de la fonction `abs` avec l'argument `-3` s'écrit `abs(-3)`.


{{% note warning %}}
Il ne faut donc pas confondre `f`, le nom de la fonction, avec `f(x)`, l'appel (ou application) de la fonction.
{{% /note %}}

### Évaluation de l'argument d'une fonction

Il n'est pas nécessaire de fournir une constante comme argument à une fonction, on peut lui fournir une expression comme argument. Par exemple l'appel suivant `abs(3 + 4 / 2 + 7 // 3)` est tout à fait valide.  
L'interpréteur Python procède ainsi :
1. Évaluation de l'expression `3 + 4 / 2 + 7 // 3`. Le résultat est le nombre 7.0 ;
2. Appel de la fonction `abs` avec comme argument le nombre 7.0.

## Définition d'une fonction

Malgré leur grand nombre, les fonctions prédéfinies du langage peuvent ne pas être suffisantes. Il faut alors définir soi-même une nouvelle fonction.

### Type et signature d'une fonction


En mathématique, on définie la fonction $f$ qui calcule le carré d'un nombre réel de la sorte :

$$
\begin{array}{l|rcl}
        f: & \mathbb{R} & \longrightarrow & \mathbb{R} \cr
           & x & \longmapsto & f(x) \cr
\end{array}
$$

   
En informatique, on s'appuie sur cette écriture, en la précisant un peu, on dit que la fonction possède un **nom**, un **type** et une **signature**.

<img src="/premieres-nsi/chap-02/signature_fonction.svg" width="22%" alt="Schéma bloc d'une fonction" />
  

{{% note tip %}}
- Le **type** d'une fonction est constitué par *les types de ses  paramètres et par le type de la valeur qu'elle retourne*.
- La **signature** d'une fonction est l'*association du nom de cette fonction et de son type*.
{{% /note %}}

La connaissance de la signature d'une fonction est fondamentale, ce n'est pas parce qu'une fonction se nomme `sum` qu'elle est capable de faire la somme de deux nombres (cf. exercice 2 plus bas) ! Le type de la fonction indique quels sont les types des arguments qu'elle accepte et donne une première (mais insuffisante !) indication sur la façon de l'utiliser.

**Remarque :**  En informatique, on aura très souvent à utiliser des fonctions plus complexes que celle présentée ici, en particulier, des fonctions à plusieurs paramètres. Sans explication supplémentaire, il vous faudra admettre qu'une fonction nommée `surface` qui calcule la surface d'un rectangle de côtés $a$ et $b$ a pour définition

$$
\begin{array}{l|rcl}
\text{surface} : & \Bbb{R} \times \Bbb{R} \longrightarrow \Bbb{R}\cr
                 & (a, b) \longmapsto a \times b
\end{array}
$$


### Définition d'une fonction en Python

La syntaxe utilisée pour définir une fonction en Python est assez proche de celle des mathématiques :

```python3
def f(x: float) -> float:
	return x**2
```

On reconnaît tout de suite la signature de la fonction `def f(x: float) -> float` qui indique bien que la fonction possède un paramètre `x` de type `float` et retourne une valeur de type `float`. **Chaque paramètre peut donc être accompagné de son type !**

- Les deux points `:` à la fin de la ligne servent à indiquer que le *bloc d'instructions* qui suit la signature constitue **le corps de la fonction**, c'est à dire l'ensemble des étapes qui sont réalisées lorsqu'on appelle la fonction. 

{{% note warning %}}
**Un bloc d'instructions doit toujours être indenté par rapport à la marge !**
{{% /note %}}

- L'instruction `return` *indique à la fonction de retourner la valeur qu'elle vient de calculer*.

La définition de la fonction `surface` définie plus haut est la suivante :

```python3
def surface(a: float, b: float) -> float:
	return a * b
```

{{% note normal %}}
Les indications `: float`, qui sert à indiquer le **type** de l'argument attendu et `-> float`, qui permet d'indiquer le type de la valeur retournée par la fonction, sont des **annotations**.\
L'interpréteur Python ne les prend pas en compte, **leur présence est utile aux programmeurs et simplifie la lecture du code**.
{{% /note %}}

### Spécification d'une fonction

{{% note tip %}}
L'utilisation d'une fonction nécessite la description précise :

1. des conditions dans lesquelles elle peut être utilisée : c'est le rôle de la **signature**.
  
2. de la valeur qu'elle retourne : c'est le rôle de la **documentation**.
{{% /note %}}

Il est donc indispensable d'établir *un contrat entre le concepteur de la fonction et son utilisateur*.

{{% note tip %}}
On appelle spécification l'association de la **signature** et de la **documentation** de la fonction :
$$
    \text{\textbf{Spécification}} = \text{\textbf{Signature}} + \text{\textbf{Commentaires}}
$$
{{% /note %}}

**Remarque :** Une spécification ne s'intéresse pas au « comment » !  
L'utilisateur d'une fonction n'a pas besoin de connaître en détail toutes les étapes du traitement du problème par la fonction, il doit juste savoir *quelle valeur elle retourne et comment il faut l'utiliser*.

**Exemple :** Spécification d'une fonction qui élève au carré :

```python3
def f(x: float) -> float:
	""" Retourne le carré du nombre x passé en argument. """
```

En fait, la spécification est la seule contrainte qu'est tenu de respecter le concepteur d'une fonction. Il faut donc être capable de faire la distinction entre toutes les spécifications suivantes :

- Le programmeur ne s'occupe pas vraiment des conditions d'utilisation de la fonction. Il présuppose que tous les utilisateurs penseront à vérifier que l'argument est bien positif lors de l'appel de la fonction.  
Dans ce cas de figure, *l'utilisateur doit faire l'effort de bien comprendre le fonctionnement de la  fonction.*
  
```python3
def racine_carree(x: float) -> float:
	""" Retourne la racine carrée du nombre x. """
```

- Le programmeur avertit l'utilisateur qu'il existe une bonne utilisation de la fonction (l'argument doit être positif ou nul) mais n'empêche pas l'utilisateur d'appeler la fonction avec un mauvais argument.  
Ici aussi, il incombe à l'utilisateur de bien utiliser la fonction.

```python3
  def racine_carree(x: float) -> float:
  	""" 
    Retourne la racine carrée du nombre x.
    HYPOTHÈSE : x positif ou nul. """
```

- Le programmeur prend en charge la bonne utilisation de la fonction.

```python3
def racine_carree(x: float) -> float:
	"""
	Retourne la racine carrée du nombre x si positif ou nul.
	ERREUR : x négatif.
	"""
```
 

## Exercices du chapitre

{{% note exercise %}}
#### Exercice 2. Découverte de fonctions
 
Les deux fonctions intégrées `dir` et `help` sont fondamentales. Les utiliser **dans la console** du logiciel Thonny afin de répondre aux questions ci-dessous.

1. La fonction `sum` intégrée au langage calcule-t-elle la somme de deux nombres ?
2. Que réalisent les fonctions intégrées `int`, `float`, `str`, `bool` ?
3. Quel traitement réalise la fonction `pow` du module `math` ? Quel opérateur étudié dans ce chapitre réalise la même opération ? Donner un exemple d'utilisation de la fonction `pow`.
4. Rechercher comment se nomme la fonction du module `math` qui calcule la racine carrée d'un nombre passé en argument.
{{% / note %}}

{{% solution "Solution 2." %}}

- Pour afficher la spécification d'une fonction utiliser la fonction `help`

```python3
>>> help(sum)
Help on built-in function sum in module builtins:

sum(iterable, /, start=0)
    Return the sum of a 'start' value (default: 0) plus an iterable of numbers
    When the iterable is empty, return the start value.
    This function is intended specifically for use with numeric values and may
    reject non-numeric types.
```

D'après la documentation, la fonction `sum` attend une séquence de nombres et non pas deux nombres.

- La fonction `int` convertit n'importe quel nombre ou une chaîne de caractères en nombre entier (si possible).

```python3
>>> help(int)
Help on class int in module builtins:

class int(object)
 | int([x]) -> integer                                                   |
 | i-------------------------------------------------------------------r |
 |                                                                       |
 | Convert a number or string to an integer, or return 0 if no arguments |
 | are given.  If x is a number, return x.__int__().  For floating point |
 | numbers, this truncates towards zero.                                 |
```

De même les fonctions `float`, `str` et `bool` convertissent, si possible, un nombre, une chaîne de caractères en approximation des nombres réels, chaîne de caractères, nombre booléen.

- L'application de la fonction `pow` à deux nombres $x$ et $y$ donne le nombre $x^y$.

```python3
>>> import math as m
>>> help(m.pow)
Help on built-in function pow in module math:

pow(x, y, /)
    Return x**y (x to the power of y).
```

- Pour rechercher une fonction appartenant au module `math` :
	- Importer le module `math` ;
	- Lister, avec la fonction `dir`, toutes les fonctions de ce module et rechercher celle qui semble réaliser l'opération souhaitée ;
	- Utiliser la fonction `help` pour confirmer le choix.

```python3
>>> import math as m
>>> dir(m)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>> help(m.sqrt)
Help on built-in function sqrt in module math:

sqrt(x, /)
    Return the square root of x.
```

{{% /solution %}}

{{% note exercise %}}
#### Exercice 3. Utilisation d'une fonction

Utiliser **la console** du logiciel Thonny pour répondre aux questions suivantes&nbsp;: 

1. Peut-on appeler la fonction `randint` du module `random` sans argument ?  
    **Rappel :** La fonction intégrée `help` permet d'obtenir la documentation de n'importe quelle fonction.

2. Que retourne l'appel de la fonction `randint` du module `random` ?
    
3. Appeler cette fonction `randint` de façon à obtenir un nombre entier aléatoire compris entre 1 et 10.
    
4. Est-il possible que l'appel précédent retourne 1 ou 10 ?
{{% /note %}}

{{% solution "Solution 3." %}}

```python3
>>> import random as rd
>>> help(rd.randint)
Help on method randint in module random:

randint(a, b) method of random.Random instance
    Return random integer in range [a, b], including both end points.
```

- La documentation nous apprend que la fonction attend deux arguments.
    
- La fonction retourne un entier compris entre les deux bornes
    passées en argument.
    
- `>>> random.randint(1, 10)` permet d'obtenir un nombre entier aléatoire entre 1 et 10 inclus.
    
- La fonction retourne un entier compris entre 1 et 10 inclus.
{{% /solution %}}
 

{{% note exercise %}}
#### Exercice 4. Définition d'une fonction

1. La fonction définie ci-dessous est-elle syntaxiquement correcte ?
    
```python3
def retire_un(n):
	return 1 - n
```

2. La spécification est la suivante&nbsp;:

```python3
def retire_un(n: float) -> float:
	""" Retourne la valeur de n - 1 """
```
	La fonction telle qu'elle est définie à la question 1 correspond-elle à cette spécification ?

3. Corriger le corps de la fonction `retire_un` de façon à ce que le calcul effectué corresponde à ce qu'annonce la spécification.
{{% /note %}} 

{{% solution "Solution 4." %}}
- Du point de vue syntaxique la fonction est correcte.
    
- La fonction telle qu'elle est définie retourne la valeur de $1 - n$ et ne correspond donc pas à la spécification.
    
```python3
def retire_un(n: float) -> float:
	""" Retourne la valeur de n - 1 """
	return n - 1
```
{{% /solution %}}

{{% note exercise %}}
#### Exercice 5. Calcul de fonctions polynomiales

1.  Définir et tester une fonction écrite en Python, nommée `polynomiale`, telle que `polynomiale(a, b, c, d, x)` retourne la valeur de la fonction qui à $x$ associe $a x^3 + b x^2 + c x + d$.  
    La documentation complète de cette fonction est la suivante&nbsp;:

```python3
def polynomiale(a:int, b:int, c:int, d:int, x: float) -> float:
    """
    Retourne la valeur ax^3 + bx^2 + cx + d
    
    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
```

2. Définir et tester une fonction écrite en Python, nommée `polynomiale_carre` qui retourne la valeur de la fonction $a x^4 + b x^2 + c$.<br/>
    La documentation complète de cette fonction est la suivante&nbsp;:

```python3
def polynomiale_carre(a:int, b:int, c:int, x: float) -> float:
    """
    Retourne la valeur ax^4 + bx^2 + c
    
    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
```
{{% /note %}}

{{% solution "Solution 5." %}}

```python
def polynomiale(a: int, b: int, c: int, d: int, x: float) -> float:
    """
    Retourne la valeur ax^3 + bx^2 + cx + d

    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
    return a * x**3 + b * x**2 + c * x + d


def polynomiale_carre(a:int, b:int, c:int, x: float) -> float:
    """
    Retourne la valeur ax^4 + bx^2 + c

    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
    return a * x**4 + b * x**2 + c
```
{{% /solution %}}

{{% note exercise %}}
#### Exercice 6. Calcul de la moyenne de trois nombres

1. Définir et tester la fonction nommée `somme`, écrite en Python, dont la spécification est&nbsp;:

```python
def somme(x:float, y: float, z: float) -> float:
    """
    Retourne la somme des trois nombres passés en argument.
    """
```

2. Définir et tester une fonction écrite en Python, nommée `moyenne`, qui détermine la moyenne arithmétique de trois nombres.  
**Remarque :** La fonction `moyenne` doit utiliser la fonction `somme` définie à la questions précédente pour effectuer son traitement.  
La spécification de la fonction est la suivante&nbsp;:

```python
def moyenne(a: float, b: float, c: float) -> float:
    """
    Retourne la moyenne des trois nombres passés comme arguments.
    """
```
    
3. Définir et tester une fonction écrite en Python, nommée `moyenne_ponderee`, qui détermine la moyenne pondérée de trois nombres avec des coefficients variables. Les paramètres devront être écrits dans l'ordre suivant&nbsp;: *d'abord les trois nombres, puis les trois coefficients*.  
**Remarque :** La fonction `moyenne_ponderee` doit effectuer deux appels à la fonction `somme` pour effectuer son traitement.  
La spécification de la fonction est la suivante&nbsp;:

```python3
def moyenne_ponderee(x:float, y:float, z:float, a:int, b:int, c:int) -> float:
    """
    Retourne la moyenne pondérée des nombres x, y et z par les coefficients
    a, b et c.
    
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 1)
    10.0
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 0)
    7.5
    """
```
{{% /note %}}

{{% solution "Solution 6." %}}
```python
def somme(x:float, y: float, z: float) -> float:
    """
    Retourne la somme des trois nombres passés en argument.
    """
    return x + y + z


def moyenne(a: float, b: float, c: float) -> float:
    """
    Retourne la moyenne des trois nombres passés comme arguments.
    """
    return somme(a, b, c) / 3


def moyenne_ponderee(x:float, y:float, z:float, a:int, b:int, c:int) -> float:
    """
    Retourne la moyenne pondérée des nombres x, y et z par les coefficients
    a, b et c.
    
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 1)
    10.0
    
    >>> moyenne_ponderee(5, 10, 15, 1, 1, 0)
    7.5
    """
    return somme(a * x, b * y, c * z) / somme(a, b, c)
```
{{% /solution %}}

{{% note exercise %}}
#### Exercice 7. Calculs de surfaces et de volumes

1. Définir et tester une fonction écrite en Python, nommée `surface_rectangle`, qui détermine la surface d'un rectangle de longueur $a$ et de largeur $b$.  
**Préciser la spécification de la fonction.**
    
2. Définir et tester une fonction écrite en Python, nommée `volume_parallelepipede`, qui détermine le volume d'un parallélépipède rectangle de longueur $a$, de largeur $b$ et de hauteur $h$.  
**Préciser la spécification de la fonction.**  
*Cette fonction devra utiliser la fonction `surface_rectangle` pour effectuer son traitement son traitement.*
    
3. Définir et tester une fonction écrite en Python, nommée `surface_disque`, qui détermine la surface d'un disque de rayon $r$.  
**Rappel :** Le module`math` possède une variable `pi`.   
**Préciser la spécification de la fonction.**
    
4. Définir et tester une fonction écrite en Python, nommée `surface_couronne`, qui détermine la surface d'une couronne de rayon intérieur $r_1$ et de rayon extérieur $r_2$.  
<img src="/premieres-nsi/chap-02/couronne.svg" width="30%" />  
 **Préciser la spécification de la fonction.**  
 *Cette fonction devra utiliser la fonction `surface_disque` pour effectuer son traitement.*
    
5. Définir et tester une fonction écrite en Python, nommée `volume_tube`, qui détermine le volume de la partie pleine d'un tube de longueur $l$, dont la section est une couronne de rayon intérieur $r\_1$ et de rayon extérieur $r\_2$.  
**Préciser la spécification de la fonction.**  
*Cette fonction devra utiliser la fonction `surface_couronne` pour effectuer son traitement.*
{{% /note %}}

{{% solution "Solution 7." %}}

```python
from math import pow, pi

def surface_rectangle(a: float, b: float) -> float:
    """ Détermine la surface du rectangle de côtés a et b. """
    return a * b


def volume_parallelepipede(a: float, b: float, h: float) -> float:
    """ Retourne le volume du parallélépipède rectangle de côtés a, b et de
    hauteur h. """
    return surface_rectangle(a, b) * h


def surface_disque(r: float) -> float:
    """ Returne la surface du disque de rayon r. """
    return pi * pow(r, 2)


def surface_couronne(r1: float, r2: float) -> float:
    """
    Retourne la surface de la couronne comprise entre les rayons r1
    et r2.
    """
    return surface_disque(r2) - surface_disque(r1)


def volume_tube(r1, r2, l) -> float:
    """ Retourne le volume de la partie pleine d'un tube de longueur l, dont
    la section est une couronne de rayon intérieur r1 et de rayon extérieur
    r2. """
    return surface_couronne(r1, r2) * l

```
{{% /solution %}}

{{% note exercise %}}
#### Exercice 8. Calcul d'une distance 
  
Définir et tester une fonction écrite en Python, nommée `distance` qui détermine la distance séparant deux points de coordonnées $(x_1, y_1)$ et $(x_2, y_2)$ d'un plan.
  
La documentation complète de la fonction est la suivante&nbsp;:
```python
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Retourne la distance dans le plan entre les deux points de coordonnées
    (x1, y1) et (x2, y2).
    
    >>> distance(0, 0, 1, 1)
    1.4142135623730951
    """
```
{{% /note %}}
{{% solution "Solution 8." %}}
```python
from math import pow, sqrt

def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Retourne la distance dans le plan entre les deux points de 
	coordonnées (x1, y1) et (x2, y2).
    
    >>> distance(0, 0, 1, 1)
    1.4142135623730951
    """
    return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
```
{{% /solution %}}

{{% note exercise %}}
#### Exercice 9. Reprise de l'exercice 1 (difficile ) 

L'objectif de cet exercice est de retrouver une partie du comportement de la fonction `randint` du module `random` à partir de la fonction `random` de ce même module.
  
Définir et tester une fonction écrite en Python, nommée `tirage_entier`, telle que `tirage_entier(a)` retourne un nombre entier compris entre 1 et $a$ (inclus), au hasard. *La fonction `tirage_entier` doit utiliser la fonction `random` du module `random`.*
  
**Remarque :** Lire attentivement la documentation de la fonction `random` afin de comprendre ce qu'elle retourne.

**Rappel :** La fonction intégrée `int` permet de convertir n'importe quel nombre en nombre entier.
{{% /note %}}

{{% solution "Solution 9." %}}
```python
from random import random  
    
def tirage_entier(a: int) -> int:
    """
    Retourne un nombre entier aléatoire compris entre 1 et a (inclus).
    """
    return int(random() * a + 1)
```
{{% /solution %}}