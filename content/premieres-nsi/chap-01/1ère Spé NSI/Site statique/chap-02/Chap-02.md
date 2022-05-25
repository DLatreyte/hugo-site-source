# Chap. 02 — Premiers pas en programmation... et en Python

[TOC]

---

On appelle **informatique** le *traitement automatisé des informations* par un ordinateur. Cette discipline s'appuie sur la **programmation**, activité qui consiste à apprendre à un ordinateur à effectuer des tâches qu'il n'est pas capable d'exécuter à sa conception. L'écriture d'un programme nécessite l'utilisation d'un **langage de programmation**. Dans ce cours nous utiliserons Python.


## À quoi a-t-on accès lorsqu'on utilise un langage de programmation ?

Un langage de programmation doit :

- *fournir des objets (ou types) primitifs* ;
- *posséder une bibliothèque de fonctions prédéfinies* ;
- *permettre la manipulation des objets primitifs et des fonctions
  prédéfinies* ;
- *établir des règles qui permettent de construire de nouveaux
  objets (ou types) ou de nouvelles fonctions par combinaison des types primitifs et des fonctions prédéfinies.*

Dans ce chapitre nous allons aborder chacun de ces points.

## Quelques objets primitifs en Python ##

Le langage Python possède un grand nombre d'objets primitifs. Parmi eux, on utilisera lors des premiers chapitres :

- Les **constantes entières** (« Integer », `int`)

```python
>>> type(3)
<type 'int'>
>>> type(-10)
<type 'int'>
```
- Les **constantes « flottantes »** (type `float`). Il s'agit d'une *approximations des nombres non entiers*.

```python
>>> type(0.1)
<type 'float'>
>>> type(-2.9)
<type 'float'>
>>> type(2e3)
<type 'float'>
```

- Les **valeurs booléennes** (type `bool`) `True` et `False`.

```python
>>> type(True)
<type 'bool'>
>>> type(False)
<type 'bool'>
```

- Les **chaînes de caractères** (« String », type `str`).

```python
>>> type("abcd")
<type 'str'>
>>> type('abcd')
<type 'str'>}
>>> type('a')
<type 'str'>
```


## Syntaxe et évaluation d'une expression en Python ##

> En mathématique et en informatique une **expression** est une *formule exprimant la façon de calculer une valeur*.


### Ambiguïté de l'écriture traditionnelle des expressions mathématiques ###

En mathématique on écrit $3 x^2 + 2 x + 4$ l'expression qui permet de calculer la valeur du polynôme du second degré, pour toute valeur de la variable $x$. En programmation, peut-on se contenter d'utiliser la syntaxe des mathématiques ? <br />
Si on se penche un peu plus attentivement sur l'écriture du polynôme, on remarque :

- qu'il faut savoir que $2 x$ signifie la multiplication du nombre 2 par $x$ ;
  
- que pour $3 x^2$ il faut d'abord élever à la puissance 2 $x$ avant de multiplier le résultat par 3 ;
  
- que $2 x + 4$ n'est pas 2 multiplié par le résultat du calcul de $x + 4$ ;
  
- que cette écriture est une écriture à deux dimensions (élévation à la puissance 2 est indiquée en augmentant l'espace depuis la ligne de base).

De même, en mathématique, on peut écrire :

- $a + b$ : l'opérateur $+$ est entre les deux opérandes ;
- $\sin (x)$ : le nom de la fonction est placée avant son argument ;
- $f'$ pour indiquer la fonction dérivée de la fonction $f$ (le symbole de la dérivée est placé après le nom de la fonction).

En conclusion, l'écriture mathématique traditionnelle nous parait claire *car on l'utilise depuis les plus petites classes et parce qu'on a appris des règles telles que celles de la priorité des opérateurs*. *En informatique, la syntaxe doit être plus rigoureuse, moins ambiguë car la machine effectue une vérification pointilleuse de tout ce qui est écrit.*

L'écriture la plus rigoureuse du polynôme est : $\left( 3 \times \left( x \text{^}2 \right) \right) + ((2 \times x) + 4)$, heureusement le langage Python a intégré la règle de priorité des opérateurs et on peut écrire : $3 \times x \text{^} 2 + 2 \times x + 4$.


### Opérateurs arithmétiques en Python ###

> Les opérateurs en Python se répartissent en trois catégories :
>
> - les **opérateurs arithmétiques**, utilisés pour calculer des expressions ;
> - les **opérateurs de comparaison et les opérateurs logiques**, utilisés dans l'alternative ;
> - les **opérateurs d'affectation**, utilisés pour modifier la «  valeur » d'une variable.

Dans ce chapitre seuls les opérateurs arithmétiques seront utilisés.

| Opérateur |  Expression  | Description                                                  |
| :-------: | :----------: | :----------------------------------------------------------- |
|    `+`    | `op1 + op2`  | renvoie le résultat de l'addition de `op1` et `op2`          |
|    `-`    | `op1 - op2`  | renvoie le résultat de la soustraction de `op1` et `op2`     |
|    `-`    |    `-op`     | renvoie la valeur opposée de `op`                            |
|    `*`    | `op1 * op2`  | renvoie le résultat de la multiplication de `op1` et `op2`   |
|    `/`    | `op1 / op2`  | renvoie le résultat de la division de `op1` et `op2`         |
|   `//`    | `op1 // op2` | renvoie le **quotient de la division euclidienne** (le quotient donc) de `op1` et `op2` |
|    `%`    | `op1 % op2`  | renvoie le **reste de la division euclidienne** de `op1` et `op2` |
|   `**`    |  `op**exp`   | renvoie le résultat de `op` à la puissance `exp`             |

>  **Remarques.**
>
> - Le **résultat de la division de deux nombres est toujours un** `float`, **même s'il s'agit de la division de deux nombres entiers**.
> - Le résultat de la **division euclidienne** de deux nombres est un `float` si l'un des nombres est un `float`, un `int` si les deux nombres sont des entiers.


### Exercice. Utilisation de l'éditeur Thonny pour visualiser toutes les étapes de l'évaluation d'une expression ###

Utiliser l'éditeur de texte Thonny pour visualiser toutes les étapes de l'évaluation de l'expression $2 \times (3 + \text{4,3})^3 + 5 \times 6^2$.

---

<details>
    <summary><strong>Solution</strong></summary>
    <ul><li><span>Écrire dans la fenêtre principale : </span><code>2 * (3 + 4.3)**3 + 5 * 6**2</code><span>.</span></li><li><span>Lancer la commande : Run </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.323ex" height="1.645ex" style="vertical-align: -0.256ex;" viewBox="0 -597.7 1000 708.1" role="img" focusable="false"><defs><path stroke-width="0" id="E22-MJMAIN-2192" d="M56 237T56 250T70 270H835Q719 357 692 493Q692 494 692 496T691 499Q691 511 708 511H711Q720 511 723 510T729 506T732 497T735 481T743 456Q765 389 816 336T935 261Q944 258 944 250Q944 244 939 241T915 231T877 212Q836 186 806 152T761 85T740 35T732 4Q730 -6 727 -8T711 -11Q691 -11 691 0Q691 7 696 25Q728 151 835 230H70Q56 237 56 250Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E22-MJMAIN-2192" x="0" y="0"></use></g></svg></span><script type="math/tex">\rightarrow</script><span> Debug current script (touches </span><kbd><span>Ctrl + F5</span></kbd><span>). Un rectangle jaune doit apparaître à l'écran. Il indique la partie de l'expression que Python va évaluer au « pas » suivant.</span></li><li><span>Progresser pas à pas grâce à la commande Run </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.323ex" height="1.645ex" style="vertical-align: -0.256ex;" viewBox="0 -597.7 1000 708.1" role="img" focusable="false"><defs><path stroke-width="0" id="E22-MJMAIN-2192" d="M56 237T56 250T70 270H835Q719 357 692 493Q692 494 692 496T691 499Q691 511 708 511H711Q720 511 723 510T729 506T732 497T735 481T743 456Q765 389 816 336T935 261Q944 258 944 250Q944 244 939 241T915 231T877 212Q836 186 806 152T761 85T740 35T732 4Q730 -6 727 -8T711 -11Q691 -11 691 0Q691 7 696 25Q728 151 835 230H70Q56 237 56 250Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E22-MJMAIN-2192" x="0" y="0"></use></g></svg></span><script type="math/tex">\rightarrow</script><span> Step into  (touche </span><kbd><span>F7</span></kbd><span>) en notant à chaque fois ce qui est évalué et le résultat de l'évaluation.</span></li></ul>
</details>

---

## Application d'une fonction ##

### Schéma-bloc d'une fonction ###

>  On appelle **schéma-bloc** la modélisation du fonctionnement d'une fonction.  Cette modélisation est affichée sous forme graphique.


Par exemple, le schéma-bloc de la fonction « mise au carré » est le suivant :

<img src="./fonction.svg" width="80%" alt="Schéma bloc d'une fonction" style="zoom:60%;" />

Ce schéma montre que :

- La fonction a besoin de recevoir 1 argument pour effectuer son traitement ;
  
- La fonction effectue un traitement. **Ce traitement n'est pas indiqué dans le schéma-bloc car sa connaissance n'est pas nécessaire à un utilisateur de cette fonction**.
  
- La fonction retourne la valeur calculée.


### Fonctions intégrées du langage Python ###


Le langage Python possède de nombreuses fonctions prédéfinies. Les fonctions intégrées `dir` et `help` permettent de les découvrir.

```python
>>> dir()
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> dir('__builtins__')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> help(abs)
Help on built-in function abs in module builtins:

abs(x, /)
    Return the absolute value of the argument.
```

L'exemple ci-dessus pourrait laisser penser que le nombre de fonctions n'est pas très important. La plupart des fonctions sont en fait organisées au sein de modules : `math`, `random`, `time` qu'il faut importer.

```python
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

> **Remarque.** 
>
> Pour utiliser une fonction contenue dans le module `module`, on doit utiliser la syntaxe `module.nom_de_la_fonction`.


### Syntaxe de l'application d'une fonction ###

L'**appel** (ou l'**application**) d'une fonction obéit à une syntaxe bien particulière, *identique à celle utilisée en mathématique*. Par exemple, l'appel de la fonction `abs` avec l'argument `-3` s'écrit `abs(-3)`.

> Il ne faut donc pas confondre `f`, le **nom de la fonction**, avec `f(x)`, l'**appel** (ou **application**) de la fonction.


### Évaluation de l'argument d'une fonction ###


Il n'est pas nécessaire de fournir une constante comme argument à une fonction, on peut lui passser une expression. Par exemple l'appel suivant `abs(3 + 4 / 2 + 7 // 3)` est tout à fait valide. L'expression `3 + 4 / 2 + 7 // 3` est évaluée avant que la fonction ne commence son traitement.


## Définition d'une fonction ##


Malgré leur grand nombre, les fonctions prédéfinies du langage peuvent ne pas être suffisantes. Il faut alors définir soi-même une nouvelle fonction.

### Type et signature d'une fonction ###


En mathématique, on définie la fonction $f$ qui calcule le carré d'un nombre réel de la sorte :

$$
\begin{aligned}
f :\ & \mathbb{R} \longrightarrow \mathbb{R}\\
  & x \longmapsto x^2
\end{aligned}
$$

En informatique, on s'appuie sur cette écriture, en la précisant un peu : on dit que la fonction possède un **nom**, un **type** et finalement une **signature**.

<img src="signature_fonction.svg" alt="signature_fonction" style="zoom:8%;" />

> - Le **type** d'une fonction est constitué par les types de ses  paramètres et par le type de la valeur qu'elle retourne.
> - La **signature** d'une fonction est l'association du nom de cette fonction et de son type.

La connaissance de la signature d'une fonction est fondamentale, ce n'est pas parce qu'une fonction se nomme `sum` qu'elle est capable de faire la somme de deux nombres (cf. exercice 2) ! 

Le type de la fonction indique quels sont les types des arguments qu'elle accepte et quel est le type de la valeur qu'elle retourne. Il donne donc une première (mais insuffisante !) indication sur la façon d'utiliser la fonction.

**Remarque.**  En informatique, on a très souvent à utiliser des fonctions plus complexes que celle présentée ici, en particulier, des fonctions à plusieurs paramètres. Sans explication supplémentaire, il  faut admettre qu'une fonction nommée `surface` qui calcule la surface d'un rectangle de côtés $a$ et $b$ a pour définition :
$$
\begin{aligned}
\text{surface : }& \Bbb{R} \times \Bbb{R} \longrightarrow \Bbb{R}\\\\ & (a, b) \longmapsto a \times b
\end{aligned}
$$


###  Définition d'une fonction en Python ###


La syntaxe utilisée pour définir une fonction en Python est assez proche de celle des mathématiques :

```python
def f(x: float) -> float:
	return x**2
```

On reconnait tout de suite la signature de la fonction `def f(x: float) -> float` qui indique bien que la fonction possède un paramètre `x` de type `float` et retourne une valeur de type `float`. **Chaque paramètre doit donc être accompagné de son type !**

- Les deux points `:` à la fin de la ligne servent à indiquer que le *bloc d'instructions* qui suit la signature constitue *le corps de la fonction*, c'est à dire l'ensemble des étapes qui sont réalisées lorsqu'on appelle la fonction. **Un bloc d'instructions doit toujours être indenté par rapport à la marge !**

- L'instruction `return` *indique à la fonction de retourner la valeur qu'elle vient de calculer*.

La définition de la fonction `surface` définie plus haut est la suivante :

```python
def surface(a: float, b: float) -> float:
	return a * b
```

### Spécification d'une fonction ###

L'utilisation d'une fonction nécessite la description précise :

1. _des conditions dans lesquelles elle peut être utilisée : c'est le rôle de la **signature**._
  
2. *du traitement qu'elle effectue* : c'est le rôle de la **documentation**.

Il est donc indispensable d'établir *un contrat entre le concepteur de la fonction et son utilisateur*.

> On appelle spécification l'*association de la **signature** et de la **documentation** de la fonction* : 
>
> <center><strong>Spécification = Signature + Documentation</strong></center>

**Remarque.** *Une spécification ne s'intéresse pas au « comment »* ! <br /> L'utilisateur d'une fonction n'a pas besoin de connaître en détail toutes les étapes du traitement du problème par la fonction, il doit juste savoir *quelle valeur elle retourne et comment il faut l'utiliser*.

**Exemple.** Spécification d'une fonction qui élève au carré :

```python
def f(x: float) -> float:
	""" Retourne le carré du nombre x passé en argument. """
```

En fait, la spécification est la seule contrainte qu'est tenu de respecter le concepteur d'une fonction. Il faut donc être capable de faire la distinction entre toutes les spécifications suivantes :

- Le programmeur ne s'occupe pas vraiment des conditions d'utilisation de la fonction. Il présuppose que tous les utilisateurs penseront à vérifier que l'argument est bien positif lors de l'appel de la fonction. <br />Dans ce cas de figure,*Il incombe à l'utilisateur de bien utiliser la fonction.*
```python
def racine_carree(x: float) -> float:
	""" Retourne la racine carrée du nombre x. """
```

- Le programmeur avertit l'utilisateur qu'il existe une bonne utilisation de la fonction (l'argument doit être positif ou nul) mais n'empêche pas l'utilisateur d'appeler la fonction avec un mauvais argument.<br /> Ici aussi, il incombe à l'utilisateur de bien utiliser la fonction.

```python
  def racine_carree(x: float) -> float:
  	""" Retourne la racine carrée du nombre x positif ou nul. """
```

- Le programmeur prend en charge la bonne utilisation de la fonction.

```python
def racine_carree(x: float) -> float:
	"""
	Retourne la racine carrée du nombre x si positif ou nul.
	Retourne une erreur si x négatif.
	"""
```


## Exercices du chapitre ##

### Exercice. Découverte de fonctions ###

Les deux fonctions intégrées `dir` et `help` sont fondamentales. Les utiliser **dans la console** du logiciel Thonny afin de répondre aux questions ci-dessous.

1. La fonction `sum` intégrée au langage calcule-t-elle la somme de deux nombres ?
2. Que réalisent les fonctions intégrées `int`, `float`, `str`, `bool` ?
3. Quel traitement réalise la fonction `pow` du module `math` ? Quel opérateur étudié dans ce chapitre réalise la même opération ? Donner un exemple d'utilisation de la fonction `pow`.
4. Rechercher comment se nomme la fonction du module `math` qui calcule la racine carrée d'un nombre passé en argument.

---

<details>
    <summary><strong>Solution</strong></summary>
    <ul>
        <li><span>Pour afficher la spécification d'une fonction utiliser la fonction </span><code>help</code></li></ul>
        <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">help</span>(<span class="cm-builtin">sum</span>)</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">Help</span> <span class="cm-variable">on</span> <span class="cm-variable">built</span><span class="cm-operator">-</span><span class="cm-keyword">in</span> <span class="cm-variable">function</span> <span class="cm-builtin">sum</span> <span class="cm-keyword">in</span> <span class="cm-variable">module</span> <span class="cm-variable">builtins</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-builtin">sum</span>(<span class="cm-variable">iterable</span>, <span class="cm-variable">start</span>=<span class="cm-number">0</span>, <span class="cm-operator">/</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">Return</span> <span class="cm-variable">the</span> <span class="cm-builtin">sum</span> <span class="cm-variable">of</span> <span class="cm-variable">a</span> <span class="cm-string">'start'</span> <span class="cm-variable">value</span> (<span class="cm-variable">default</span>: <span class="cm-number">0</span>) <span class="cm-variable">plus</span> <span class="cm-variable">an</span> <span class="cm-variable">iterable</span> <span class="cm-variable">of</span> <span class="cm-variable">numbers</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">When</span> <span class="cm-variable">the</span> <span class="cm-variable">iterable</span> <span class="cm-keyword">is</span> <span class="cm-variable">empty</span>, <span class="cm-keyword">return</span> <span class="cm-variable">the</span> <span class="cm-variable">start</span> <span class="cm-variable">value</span>.</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-property">This</span> <span class="cm-variable">function</span> <span class="cm-keyword">is</span> <span class="cm-variable">intended</span> <span class="cm-variable">specifically</span> <span class="cm-keyword">for</span> <span class="cm-variable">use</span> <span class="cm-keyword">with</span> <span class="cm-variable">numeric</span> <span class="cm-variable">values</span> <span class="cm-keyword">and</span> <span class="cm-variable">may</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">reject</span> <span class="cm-variable">non</span><span class="cm-operator">-</span><span class="cm-variable">numeric</span> <span class="cm-variable">types</span>.</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 198px;"></div><div class="CodeMirror-gutters" style="display: none; height: 198px;"></div></div></div></pre>
        <p><span>D'après la documentation, la fonction </span><code>sum</code><span> attend une séquence de nombres et non pas deux nombres.</span></p>
    <ul><li><span>La fonction </span><code>int</code><span> convertit n'importe quel nombre ou une chaîne de caractères en nombre entier (si possible).</span></li></ul>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">help</span>(<span class="cm-builtin">int</span>)</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">Help</span> <span class="cm-variable">on</span> <span class="cm-keyword">class</span> <span class="cm-builtin">int</span> <span class="cm-keyword">in</span> <span class="cm-variable">module</span> <span class="cm-variable">builtins</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">class</span> <span class="cm-builtin">int</span>(<span class="cm-builtin">object</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator">|</span> &nbsp;<span class="cm-builtin">int</span>([<span class="cm-variable">x</span>]) <span class="cm-operator">-&gt;</span> <span class="cm-variable">integer</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator cm-error">|</span> &nbsp;<span class="cm-builtin">int</span>(<span class="cm-variable">x</span>, <span class="cm-variable">base</span>=<span class="cm-number">10</span>) <span class="cm-operator">-&gt;</span> <span class="cm-variable">integer</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator">|</span> &nbsp;</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator cm-error">|</span> &nbsp;<span class="cm-variable">Convert</span> <span class="cm-variable">a</span> <span class="cm-variable">number</span> <span class="cm-keyword">or</span> <span class="cm-variable">string</span> <span class="cm-variable">to</span> <span class="cm-variable">an</span> <span class="cm-variable">integer</span>, <span class="cm-keyword">or</span> <span class="cm-keyword">return</span> <span class="cm-number">0</span> <span class="cm-keyword">if</span> <span class="cm-variable">no</span> <span class="cm-variable">arguments</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator">|</span> &nbsp;<span class="cm-variable">are</span> <span class="cm-variable">given</span>. &nbsp;<span class="cm-property">If</span> <span class="cm-variable">x</span> <span class="cm-keyword">is</span> <span class="cm-variable">a</span> <span class="cm-variable">number</span>, <span class="cm-keyword">return</span> <span class="cm-variable">x</span>.<span class="cm-property">__int__</span>(). &nbsp;<span class="cm-property">For</span> <span class="cm-variable">floating</span> <span class="cm-variable">point</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> <span class="cm-operator">|</span> &nbsp;<span class="cm-variable">numbers</span>, <span class="cm-variable">this</span> <span class="cm-variable">truncates</span> <span class="cm-variable">towards</span> <span class="cm-variable">zero</span>.</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 220px;"></div><div class="CodeMirror-gutters" style="display: none; height: 220px;"></div></div></div></pre>
    <p><span>De même les fonctions </span><code>float</code><span>, </span><code>str</code><span> et </span><code>bool</code><span> convertissent, si possible, un nombre, une chaîne de caractères en approximation des nombres réels, chaîne de caractères, nombre booléen.</span></p>
    <ul><li><span>L'application de la fonction </span><code>pow</code><span> à deux nombres </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.329ex" height="1.519ex" style="vertical-align: -0.256ex;" viewBox="0 -543.6 572 653.9" role="img" focusable="false"><defs><path stroke-width="0" id="E30-MJMATHI-78" d="M52 289Q59 331 106 386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522 332 508 314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404 406 402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469 151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10 133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94 41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266 352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E30-MJMATHI-78" x="0" y="0"></use></g></svg></span><script type="math/tex">x</script><span> et </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="1.154ex" height="1.896ex" style="vertical-align: -0.634ex;" viewBox="0 -543.6 497 816.4" role="img" focusable="false"><defs><path stroke-width="0" id="E27-MJMATHI-79" d="M21 287Q21 301 36 335T84 406T158 442Q199 442 224 419T250 355Q248 336 247 334Q247 331 231 288T198 191T182 105Q182 62 196 45T238 27Q261 27 281 38T312 61T339 94Q339 95 344 114T358 173T377 247Q415 397 419 404Q432 431 462 431Q475 431 483 424T494 412T496 403Q496 390 447 193T391 -23Q363 -106 294 -155T156 -205Q111 -205 77 -183T43 -117Q43 -95 50 -80T69 -58T89 -48T106 -45Q150 -45 150 -87Q150 -107 138 -122T115 -142T102 -147L99 -148Q101 -153 118 -160T152 -167H160Q177 -167 186 -165Q219 -156 247 -127T290 -65T313 -9T321 21L315 17Q309 13 296 6T270 -6Q250 -11 231 -11Q185 -11 150 11T104 82Q103 89 103 113Q103 170 138 262T173 379Q173 380 173 381Q173 390 173 393T169 400T158 404H154Q131 404 112 385T82 344T65 302T57 280Q55 278 41 278H27Q21 284 21 287Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E27-MJMATHI-79" x="0" y="0"></use></g></svg></span><script type="math/tex">y</script><span> donne le nombre </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="2.377ex" height="2.022ex" style="vertical-align: -0.256ex;" viewBox="0 -760.2 1023.4 870.5" role="img" focusable="false"><defs><path stroke-width="0" id="E28-MJMATHI-78" d="M52 289Q59 331 106 386T222 442Q257 442 286 424T329 379Q371 442 430 442Q467 442 494 420T522 361Q522 332 508 314T481 292T458 288Q439 288 427 299T415 328Q415 374 465 391Q454 404 425 404Q412 404 406 402Q368 386 350 336Q290 115 290 78Q290 50 306 38T341 26Q378 26 414 59T463 140Q466 150 469 151T485 153H489Q504 153 504 145Q504 144 502 134Q486 77 440 33T333 -11Q263 -11 227 52Q186 -10 133 -10H127Q78 -10 57 16T35 71Q35 103 54 123T99 143Q142 143 142 101Q142 81 130 66T107 46T94 41L91 40Q91 39 97 36T113 29T132 26Q168 26 194 71Q203 87 217 139T245 247T261 313Q266 340 266 352Q266 380 251 392T217 404Q177 404 142 372T93 290Q91 281 88 280T72 278H58Q52 284 52 289Z"></path><path stroke-width="0" id="E28-MJMATHI-79" d="M21 287Q21 301 36 335T84 406T158 442Q199 442 224 419T250 355Q248 336 247 334Q247 331 231 288T198 191T182 105Q182 62 196 45T238 27Q261 27 281 38T312 61T339 94Q339 95 344 114T358 173T377 247Q415 397 419 404Q432 431 462 431Q475 431 483 424T494 412T496 403Q496 390 447 193T391 -23Q363 -106 294 -155T156 -205Q111 -205 77 -183T43 -117Q43 -95 50 -80T69 -58T89 -48T106 -45Q150 -45 150 -87Q150 -107 138 -122T115 -142T102 -147L99 -148Q101 -153 118 -160T152 -167H160Q177 -167 186 -165Q219 -156 247 -127T290 -65T313 -9T321 21L315 17Q309 13 296 6T270 -6Q250 -11 231 -11Q185 -11 150 11T104 82Q103 89 103 113Q103 170 138 262T173 379Q173 380 173 381Q173 390 173 393T169 400T158 404H154Q131 404 112 385T82 344T65 302T57 280Q55 278 41 278H27Q21 284 21 287Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E28-MJMATHI-78" x="0" y="0"></use><use transform="scale(0.707)" xlink:href="#E28-MJMATHI-79" x="808" y="513"></use></g></svg></span><script type="math/tex">x^y</script><span>.</span></li></ul>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-keyword">import</span> <span class="cm-variable">math</span> <span class="cm-keyword">as</span> <span class="cm-variable">m</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">help</span>(<span class="cm-variable">m</span>.<span class="cm-property">pow</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">Help</span> <span class="cm-variable">on</span> <span class="cm-variable">built</span><span class="cm-operator">-</span><span class="cm-keyword">in</span> <span class="cm-variable">function</span> <span class="cm-builtin">pow</span> <span class="cm-keyword">in</span> <span class="cm-variable">module</span> <span class="cm-variable">math</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-builtin">pow</span>(<span class="cm-variable">x</span>, <span class="cm-variable">y</span>, <span class="cm-operator">/</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">Return</span> <span class="cm-variable">x</span><span class="cm-operator">**</span><span class="cm-variable">y</span> (<span class="cm-variable">x</span> <span class="cm-variable">to</span> <span class="cm-variable">the</span> <span class="cm-variable">power</span> <span class="cm-variable">of</span> <span class="cm-variable">y</span>).</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 132px;"></div><div class="CodeMirror-gutters" style="display: none; height: 132px;"></div></div></div></pre>
    <ul><li><p><span>Pour rechercher une fonction appartenant au module </span><code>math</code><span> :</span></p><ul><li><span>Importer le module </span><code>math</code><span> ;</span></li><li><span>Lister, avec la fonction </span><code>dir</code><span>, toutes les fonctions de ce module et rechercher celle qui semble réaliser l'opération souhaitée ;</span></li><li><span>Utiliser la fonction </span><code>help</code><span> pour confirmer le choix.</span></li></ul></li></ul>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"><pre><span>xxxxxxxxxx</span></pre></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-keyword">import</span> <span class="cm-variable">math</span> <span class="cm-keyword">as</span> <span class="cm-variable">m</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">dir</span>(<span class="cm-variable">m</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation">[<span class="cm-string">'__doc__'</span>, <span class="cm-string">'__file__'</span>, <span class="cm-string">'__loader__'</span>, <span class="cm-string">'__name__'</span>, <span class="cm-string">'__package__'</span>, <span class="cm-string">'__spec__'</span>, <span class="cm-string">'acos'</span>, <span class="cm-string">'acosh'</span>, <span class="cm-string">'asin'</span>, <span class="cm-string">'asinh'</span>, <span class="cm-string">'atan'</span>, <span class="cm-string">'atan2'</span>, <span class="cm-string">'atanh'</span>, <span class="cm-string">'ceil'</span>, <span class="cm-string">'copysign'</span>, <span class="cm-string">'cos'</span>, <span class="cm-string">'cosh'</span>, <span class="cm-string">'degrees'</span>, <span class="cm-string">'e'</span>, <span class="cm-string">'erf'</span>, <span class="cm-string">'erfc'</span>, <span class="cm-string">'exp'</span>, <span class="cm-string">'expm1'</span>, <span class="cm-string">'fabs'</span>, <span class="cm-string">'factorial'</span>, <span class="cm-string">'floor'</span>, <span class="cm-string">'fmod'</span>, <span class="cm-string">'frexp'</span>, <span class="cm-string">'fsum'</span>, <span class="cm-string">'gamma'</span>, <span class="cm-string">'gcd'</span>, <span class="cm-string">'hypot'</span>, <span class="cm-string">'inf'</span>, <span class="cm-string">'isclose'</span>, <span class="cm-string">'isfinite'</span>, <span class="cm-string">'isinf'</span>, <span class="cm-string">'isnan'</span>, <span class="cm-string">'ldexp'</span>, <span class="cm-string">'lgamma'</span>, <span class="cm-string">'log'</span>, <span class="cm-string">'log10'</span>, <span class="cm-string">'log1p'</span>, <span class="cm-string">'log2'</span>, <span class="cm-string">'modf'</span>, <span class="cm-string">'nan'</span>, <span class="cm-string">'pi'</span>, <span class="cm-string">'pow'</span>, <span class="cm-string">'radians'</span>, <span class="cm-string">'remainder'</span>, <span class="cm-string">'sin'</span>, <span class="cm-string">'sinh'</span>, <span class="cm-string">'sqrt'</span>, <span class="cm-string">'tan'</span>, <span class="cm-string">'tanh'</span>, <span class="cm-string">'tau'</span>, <span class="cm-string">'trunc'</span>]</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">help</span>(<span class="cm-variable">m</span>.<span class="cm-property">sqrt</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">Help</span> <span class="cm-variable">on</span> <span class="cm-variable">built</span><span class="cm-operator">-</span><span class="cm-keyword">in</span> <span class="cm-variable">function</span> <span class="cm-variable">sqrt</span> <span class="cm-keyword">in</span> <span class="cm-variable">module</span> <span class="cm-variable">math</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">sqrt</span>(<span class="cm-variable">x</span>, <span class="cm-operator">/</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">Return</span> <span class="cm-variable">the</span> <span class="cm-variable">square</span> <span class="cm-variable">root</span> <span class="cm-variable">of</span> <span class="cm-variable">x</span>.</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 308px;"></div><div class="CodeMirror-gutters" style="display: none; height: 308px;"></div></div></div></pre>
</details>

---

##### Exercice 3. Utilisation d'une fonction #####

Utiliser **la console** du logiciel Thonny pour répondre aux questions suivantes : 

1. Peut-on appeler la fonction `randint` du module `random` sans argument ?<br />
    **Rappel :** La fonction intégrée `help` permet d'obtenir la documentation de n'importe quelle fonction.
2. Que retourne l'appel de la fonction `randint` du module `random` ?
3. Appeler cette fonction `randint` de façon à obtenir un nombre entier aléatoire compris entre 1 et 10.
4. Est-il possible que l'appel précédent retourne 1 ou 10 ?

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-keyword">import</span> <span class="cm-variable">random</span> <span class="cm-keyword">as</span> <span class="cm-variable">rd</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-operator">&gt;&gt;&gt;</span> <span class="cm-builtin">help</span>(<span class="cm-variable">rd</span>.<span class="cm-property">randint</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">Help</span> <span class="cm-variable">on</span> <span class="cm-variable">method</span> <span class="cm-variable">randint</span> <span class="cm-keyword">in</span> <span class="cm-variable">module</span> <span class="cm-variable">random</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-variable">randint</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>) <span class="cm-variable">method</span> <span class="cm-variable">of</span> <span class="cm-variable">random</span>.<span class="cm-property">Random</span> <span class="cm-variable">instance</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-variable">Return</span> <span class="cm-variable">random</span> <span class="cm-variable">integer</span> <span class="cm-keyword">in</span> <span class="cm-builtin">range</span> [<span class="cm-variable">a</span>, <span class="cm-variable">b</span>], <span class="cm-variable">including</span> <span class="cm-variable">both</span> <span class="cm-variable">end</span> <span class="cm-variable">points</span>.</span></pre><pre class=" CodeMirror-line " role="presentation" style="display: none;"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 132px;"></div><div class="CodeMirror-gutters" style="display: none; height: 132px;"></div></div></div></pre>
    <ul><li><span>La documentation nous apprend que la fonction attend deux arguments.</span></li><li><span>La fonction retourne un entier compris entre les deux bornes</span>
<span>passées en argument.</span></li><li><code>&gt;&gt;&gt; random.randint(1, 10)</code><span> permet d'obtenir un nombre entier aléatoire entre 1 et 10 inclus.</span></li><li><span>La fonction retourne un entier compris entre 1 et 10 inclus.</span></li></ul>
</details>

---


### Exercice. Définition d'une fonction ###

1. La fonction définie ci-dessous est-elle syntaxiquement correcte ?

```python
def retire_un(n):
	return 1 - n
```

2. La spécification est la suivante :

```python
def retire_un(n: float) -> float:
	""" Retourne la valeur de n - 1 """
```
La fonction telle qu'elle est définie à la question 1 correspond-elle à cette spécification ?

3. Corriger le corps de la fonction `retire_un` de façon à ce que le calcul effectué corresponde à ce qu'annonce la spécification.

---

<details>
    <summary><strong>Solution</strong></summary>
    <ul><li><span>Du point de vue syntaxique la fonction est correcte.</span></li><li><span>La fonction telle qu'elle est définie retourne la valeur de </span><span style="font-size: 100%; display: inline-block;" class="MathJax_SVG" tabindex="-1"><svg xmlns:xlink="http://www.w3.org/1999/xlink" width="5.394ex" height="2.148ex" style="vertical-align: -0.382ex;" viewBox="0 -760.2 2322.4 924.7" role="img" focusable="false"><defs><path stroke-width="0" id="E29-MJMAIN-31" d="M213 578L200 573Q186 568 160 563T102 556H83V602H102Q149 604 189 617T245 641T273 663Q275 666 285 666Q294 666 302 660V361L303 61Q310 54 315 52T339 48T401 46H427V0H416Q395 3 257 3Q121 3 100 0H88V46H114Q136 46 152 46T177 47T193 50T201 52T207 57T213 61V578Z"></path><path stroke-width="0" id="E29-MJMAIN-2212" d="M84 237T84 250T98 270H679Q694 262 694 250T679 230H98Q84 237 84 250Z"></path><path stroke-width="0" id="E29-MJMATHI-6E" d="M21 287Q22 293 24 303T36 341T56 388T89 425T135 442Q171 442 195 424T225 390T231 369Q231 367 232 367L243 378Q304 442 382 442Q436 442 469 415T503 336T465 179T427 52Q427 26 444 26Q450 26 453 27Q482 32 505 65T540 145Q542 153 560 153Q580 153 580 145Q580 144 576 130Q568 101 554 73T508 17T439 -10Q392 -10 371 17T350 73Q350 92 386 193T423 345Q423 404 379 404H374Q288 404 229 303L222 291L189 157Q156 26 151 16Q138 -11 108 -11Q95 -11 87 -5T76 7T74 17Q74 30 112 180T152 343Q153 348 153 366Q153 405 129 405Q91 405 66 305Q60 285 60 284Q58 278 41 278H27Q21 284 21 287Z"></path></defs><g stroke="currentColor" fill="currentColor" stroke-width="0" transform="matrix(1 0 0 -1 0 0)"><use xlink:href="#E29-MJMAIN-31" x="0" y="0"></use><use xlink:href="#E29-MJMAIN-2212" x="722" y="0"></use><use xlink:href="#E29-MJMATHI-6E" x="1722" y="0"></use></g></svg></span><script type="math/tex">1 - n</script><span> et ne correspond donc pas à la spécification.</span></li></ul>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation"><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">retire_un</span>(<span class="cm-variable">n</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-string">""" Retourne la valeur de n - 1 """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-tab" role="presentation" cm-text="	">    </span><span class="cm-keyword">return</span> <span class="cm-variable">n</span> <span class="cm-operator">-</span> <span class="cm-number">1</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 68px;"></div><div class="CodeMirror-gutters" style="display: none; height: 68px;"></div></div></div></pre>
</details>

---

### Exercice. Calcul de fonctions polynomiales ###

1.  Définir et tester une fonction écrite en Python, nommée `polynomiale`, telle que `polynomiale(a, b, c, d, x)` retourne la valeur de la fonction qui à $x$ associe $a x^3 + b x^2 + c x + d$. <br/>
    La documentation complète de cette fonction est la suivante :

```python
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
    La documentation complète de cette fonction est la suivante :

```python
from math import pow

def polynomiale_carre(a:int, b:int, c:int, x: float) -> float:
    """
    Retourne la valeur ax^4 + bx^2 + c
    
    >>> polynomiale(1, 1, 1, 1, 2)
    15.0
    
    >>> polynomiale(1, 1, 1, 1, 3)
    40.0
    """
    return a * pow(x, 4) + b * pow(x, 2) + c
```

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python" style="break-inside: unset;"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">polynomiale</span>(<span class="cm-variable">a</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">b</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">c</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">d</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">x</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la valeur ax^3 + bx^2 + cx + d</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; polynomiale(1, 1, 1, 1, 2)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  15.0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; polynomiale(1, 1, 1, 1, 3)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  40.0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">*</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">x</span>, <span class="cm-number">3</span>) <span class="cm-operator">+</span> <span class="cm-variable">b</span> <span class="cm-operator">*</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">x</span>, <span class="cm-number">2</span>) <span class="cm-operator">+</span> <span class="cm-variable">c</span> <span class="cm-operator">*</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-variable">d</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">polynomiale_carre</span>(<span class="cm-variable">a</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">b</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">c</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">x</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la valeur ax^4 + bx^2 + c</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; polynomiale(1, 1, 1, 1, 2)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  15.0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; polynomiale(1, 1, 1, 1, 3)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  40.0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">*</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">x</span>, <span class="cm-number">4</span>) <span class="cm-operator">+</span> <span class="cm-variable">b</span> <span class="cm-operator">*</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">x</span>, <span class="cm-number">2</span>) <span class="cm-operator">+</span> <span class="cm-variable">c</span></span></pre><pre class=" CodeMirror-line " role="presentation" style="display: none;"><span style="padding-right: 0.1px;" role="presentation"> &nbsp;  &gt;&gt;&gt; polynomiale(1, 1, 1, 1, 3)</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 528px;"></div><div class="CodeMirror-gutters" style="display: none; height: 528px;"></div></div></div></pre>
</details>

---

### Exercice. Calcul de la moyenne de trois nombres ###

1. Définir et tester la fonction nommée `somme`, écrite en Python, dont la spécification est :

```python
def somme(x:float, y: float, z: float) -> float:
    """
    Retourne la somme des trois nombres passés en argument.
    """
```

2. Définir et tester une fonction écrite en Python, nommée `moyenne`, qui détermine la moyenne arithmétique de trois nombres. <br /> **Remarque :** La fonction `moyenne` doit utiliser la fonction `somme` définie à la questions précédente pour effectuer son traitement.<br /> La spécification de la fonction est la suivante :

```python
def moyenne(a: float, b: float, c: float) -> float:
    """
    Retourne la moyenne des trois nombres passés comme arguments.
    """
```

3. Définir et tester une fonction écrite en Python, nommée `moyenne_ponderee`, qui détermine la moyenne pondérée de trois nombres avec des coefficients variables. Les paramètres devront être écrits dans l'ordre suivant : *d'abord les trois nombres,
    puis les trois coefficients*.<br /> **Remarque :** La fonction `moyenne_ponderee` doit effectuer deux appels à la fonction `somme` pour effectuer son traitement.<br /> La spécification de la fonction est la suivante :

```python
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

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python" style="break-inside: unset;"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">somme</span>(<span class="cm-variable">x</span>:<span class="cm-builtin">float</span>, <span class="cm-variable">y</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">z</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la somme des trois nombres passés en argument.</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">x</span> <span class="cm-operator">+</span> <span class="cm-variable">y</span> <span class="cm-operator">+</span> <span class="cm-variable">z</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">moyenne</span>(<span class="cm-variable">a</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">b</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">c</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la moyenne des trois nombres passés comme arguments.</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">somme</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>, <span class="cm-variable">c</span>) <span class="cm-operator">/</span> <span class="cm-number">3</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">moyenne_ponderee</span>(<span class="cm-variable">x</span>:<span class="cm-builtin">float</span>, <span class="cm-variable">y</span>:<span class="cm-builtin">float</span>, <span class="cm-variable">z</span>:<span class="cm-builtin">float</span>, <span class="cm-variable">a</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">b</span>:<span class="cm-builtin">int</span>, <span class="cm-variable">c</span>:<span class="cm-builtin">int</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la moyenne pondérée des nombres x, y et z par les coefficients</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  a, b et c.</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; moyenne_ponderee(5, 10, 15, 1, 1, 1)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  10.0</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; moyenne_ponderee(5, 10, 15, 1, 1, 0)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  7.5</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">somme</span>(<span class="cm-variable">a</span> <span class="cm-operator">*</span> <span class="cm-variable">x</span>, <span class="cm-variable">b</span> <span class="cm-operator">*</span> <span class="cm-variable">y</span>, <span class="cm-variable">c</span> <span class="cm-operator">*</span> <span class="cm-variable">z</span>) <span class="cm-operator">/</span> <span class="cm-variable">somme</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>, <span class="cm-variable">c</span>)</span></pre><div style="position: relative; display: none;" class=""><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp;  """</span></pre></div></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 572px;"></div><div class="CodeMirror-gutters" style="display: none; height: 572px;"></div></div></div></pre>
</details>

---


### Exercice. Calculs de surfaces et de volumes ###

1. Définir et tester une fonction écrite en Python, nommée `surface_rectangle`, qui détermine la surface d'un rectangle de longueur $a$ et de largeur $b$.<br />  **Préciser la spécification de la fonction.**
  
2. Définir et tester une fonction écrite en Python, nommée `volume_parallelepipede`, qui détermine le volume d'un parallélépipède rectangle de longueur $a$, de largeur $b$ et de hauteur $h$.<br />  **Préciser la spécification de la fonction.**
  
    *Cette fonction devra utiliser la fonction `surface_rectangle` pour effectuer son traitement son traitement.*
    
3. Définir et tester une fonction écrite en Python, nommée `surface_disque`, qui détermine la surface d'un disque de rayon $r$.<br />**Rappel :** Le module`math` possède une variable
      `pi`.<br />**Préciser la spécification de la fonction.**
    
4. Définir et tester une fonction écrite en Python, nommée `surface_couronne`, qui détermine la surface d'une couronne de rayon intérieur $r_1$ et de rayon extérieur $r_2$. **Préciser la spécification de la fonction.**
       Cette fonction devra utiliser la fonction `surface_disque` pour effectuer son traitement.*

      <img src="couronne.svg" alt="couronne" style="zoom:100%;" />

5. Définir et tester une fonction écrite en Python, nommée `volume_tube`, qui détermine le volume de la partie pleine d'un tube de longueur $l$, dont la section est une couronne de rayon intérieur $r\_1$ et de rayon extérieur $r\_2$.<br />  **Préciser la spécification de la fonction.**
  
    *Cette fonction devra utiliser la fonction `surface_couronne` pour effectuer son traitement.*

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python" style="break-inside: unset;"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">math</span> <span class="cm-keyword">import</span> <span class="cm-builtin">pow</span>, <span class="cm-variable">pi</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">surface_rectangle</span>(<span class="cm-variable">a</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">b</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">""" Détermine la surface du rectangle de côtés a et b. """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">a</span> <span class="cm-operator">*</span> <span class="cm-variable">b</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">volume_parallelepipede</span>(<span class="cm-variable">a</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">b</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">h</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">""" Retourne le volume du parallélépipède rectangle de côtés a, b et de</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  hauteur h. """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">surface_rectangle</span>(<span class="cm-variable">a</span>, <span class="cm-variable">b</span>) <span class="cm-operator">*</span> <span class="cm-variable">h</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">surface_disque</span>(<span class="cm-variable">r</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">""" Returne la surface du disque de rayon r. """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">pi</span> <span class="cm-operator">*</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">r</span>, <span class="cm-number">2</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">surface_couronne</span>(<span class="cm-variable">r1</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">r2</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la surface de la couronne comprise entre les rayons r1</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  et r2.</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">surface_disque</span>(<span class="cm-variable">r2</span>) <span class="cm-operator">-</span> <span class="cm-variable">surface_disque</span>(<span class="cm-variable">r1</span>)</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">volume_tube</span>(<span class="cm-variable">r1</span>, <span class="cm-variable">r2</span>, <span class="cm-variable">l</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">""" Retourne le volume de la partie pleine d'un tube de longueur l, dont</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  la section est une couronne de rayon intérieur r1 et de rayon extérieur</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  r2. """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">surface_couronne</span>(<span class="cm-variable">r1</span>, <span class="cm-variable">r2</span>) <span class="cm-operator">*</span> <span class="cm-variable">l</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 704px;"></div><div class="CodeMirror-gutters" style="display: none; height: 704px;"></div></div></div></pre>
</details>

---

### Exercice. Calcul d'une distance ###

Définir et tester une fonction écrite en Python, nommée `distance` qui détermine la distance séparant deux points de coordonnées $(x_1, y_1)$ et $(x_2, y_2)$ d'un plan.

La documentation complète de la fonction est la suivante :
```python
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """
    Retourne la distance dans le plan entre les deux points de coordonnées
    (x1, y1) et (x2, y2).
    
    >>> distance(0, 0, 1, 1)
    1.4142135623730951
    """
```

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">math</span> <span class="cm-keyword">import</span> <span class="cm-builtin">pow</span>, <span class="cm-variable">sqrt</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">distance</span>(<span class="cm-variable">x1</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">y1</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">x2</span>: <span class="cm-builtin">float</span>, <span class="cm-variable">y2</span>: <span class="cm-builtin">float</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">float</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne la distance dans le plan entre les deux points de </span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation" class="cm-tab-wrap-hack"><span class="cm-string"><span class="cm-tab" role="presentation" cm-text="	">    </span>coordonnées (x1, y1) et (x2, y2).</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp; &nbsp;</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  &gt;&gt;&gt; distance(0, 0, 1, 1)</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  1.4142135623730951</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-variable">sqrt</span>(<span class="cm-builtin">pow</span>(<span class="cm-variable">x2</span> <span class="cm-operator">-</span> <span class="cm-variable">x1</span>, <span class="cm-number">2</span>) <span class="cm-operator">+</span> <span class="cm-builtin">pow</span>(<span class="cm-variable">y2</span> <span class="cm-operator">-</span> <span class="cm-variable">y1</span>, <span class="cm-number">2</span>))</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 243px;"></div><div class="CodeMirror-gutters" style="display: none; height: 243px;"></div></div></div></pre>
</details>

---

### Exercice. Reprise de l'exercice 1 (difficile mais important ) ###

L'objectif de cet exercice est de retrouver une partie du comportement de la fonction `randint` du module `random` à partir de la fonction `random` de ce même module.

Définir et tester une fonction écrite en Python, nommée `tirage_entier`, telle que `tirage_entier(a)` retourne un nombre entier compris entre 1 et $a$ (inclus), au hasard. *La fonction `tirage_entier` doit utiliser la fonction `random` du module `random`.*

**Remarque :** Lire attentivement la documentation de la fonction `random` afin de comprendre ce qu'elle retourne.

**Rappel :** La fonction intégrée `int` permet de convertir n'importe quel nombre en nombre entier.

---

<details>
    <summary><strong>Solution</strong></summary>
    <pre spellcheck="false" class="md-fences md-end-block ty-contain-cm modeLoaded" lang="python"><div class="CodeMirror cm-s-inner CodeMirror-wrap" lang="python"><div style="overflow: hidden; position: relative; width: 3px; height: 0px; top: 0px; left: 12px;"><textarea style="position: absolute; bottom: -1em; padding: 0px; width: 1000px; height: 1em; outline: none;" autocorrect="off" autocapitalize="off" spellcheck="false" tabindex="0"></textarea></div><div class="CodeMirror-scrollbar-filler" cm-not-content="true"></div><div class="CodeMirror-gutter-filler" cm-not-content="true"></div><div class="CodeMirror-scroll" tabindex="-1"><div class="CodeMirror-sizer" style="margin-left: 0px; margin-bottom: 0px; border-right-width: 0px; padding-right: 0px; padding-bottom: 0px;"><div style="position: relative; top: 0px;"><div class="CodeMirror-lines" role="presentation"><div style="position: relative; outline: none;" role="presentation"><div class="CodeMirror-measure"></div><div class="CodeMirror-measure"></div><div style="position: relative; z-index: 1;"></div><div class="CodeMirror-code" role="presentation" style=""><div style="position: relative;" class="CodeMirror-activeline"><div class="CodeMirror-activeline-background CodeMirror-linebackground"></div><div class="CodeMirror-gutter-background CodeMirror-activeline-gutter" style="left: 0px; width: 0px;"></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">from</span> <span class="cm-variable">random</span> <span class="cm-keyword">import</span> <span class="cm-variable">random</span></span></pre></div><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span cm-text="">​</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-keyword">def</span> <span class="cm-def">tirage_entier</span>(<span class="cm-variable">a</span>: <span class="cm-builtin">int</span>) <span class="cm-operator">-&gt;</span> <span class="cm-builtin">int</span>:</span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-string">"""</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  Retourne un nombre entier aléatoire compris entre 1 et a (inclus).</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"><span class="cm-string"> &nbsp;  """</span></span></pre><pre class=" CodeMirror-line " role="presentation"><span style="padding-right: 0.1px;" role="presentation"> &nbsp; &nbsp;<span class="cm-keyword">return</span> <span class="cm-builtin">int</span>(<span class="cm-variable">random</span>() <span class="cm-operator">*</span> <span class="cm-variable">a</span> <span class="cm-operator">+</span> <span class="cm-number">1</span>)</span></pre></div></div></div></div></div><div style="position: absolute; height: 0px; width: 1px; border-bottom-width: 0px; border-bottom-style: solid; border-bottom-color: transparent; top: 154px;"></div><div class="CodeMirror-gutters" style="display: none; height: 154px;"></div></div></div></pre>
</details>

---

