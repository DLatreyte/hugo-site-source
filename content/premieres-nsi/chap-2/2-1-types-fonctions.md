---
title: "Notions de type et de fonction"
subtitle: "Doc. 2,1"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["type", "expression", "évaluation", "opérateur", "fonction", "argument", "paramètre", "valeur de retour", "signature", "spécification", "module"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 10
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-2/2-1/2-1-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/premieres-nsi/chap-2/2-1/2-1-corrige.pdf" >}}

{{< note goal >}}
En manipulant Python dans la console et dans Thonny, vous allez chercher à répondre aux questions suivantes :

- Comment un programme **représente-t-il** une information (un âge, un nom, une réponse par oui ou non) ?
- Comment Python **calcule-t-il** le résultat d'une expression, et dans quel ordre ?
- Que se passe-t-il quand on **appelle** une fonction, et comment savoir s'en servir ?
- Comment **fabriquer** sa propre fonction et vérifier qu'elle fait ce qu'on attend d'elle ?
{{< /note >}}

## Comment représenter une information dans un programme ?

L'informatique consiste à automatiser le traitement d'informations. Pour effectuer ces traitements, un programme doit d'abord être capable de **représenter** les informations issues du monde réel.

Un âge, une température, un nom, une réponse à une question ou une distance ne sont pas des informations de même nature. Un langage de programmation utilise donc différents **types** pour **modéliser** ces différentes informations.

{{< question >}}
Pour chacune des informations suivantes, proposer une manière simple de la représenter à l'aide de Python :

- le nombre d'élèves d'une classe ;
- une température de 18,5 °C ;
- le nom d'un élève ;
- la réponse à la question « l'élève est-il majeur ? ».

Tester ensuite dans la console :

```python
>>> type(32)
>>> type(18.5)
>>> type("Alice")
>>> type(False)
```

Quels sont les quatre réponses obtenus ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient :

```python
>>> type(32)
<class 'int'>
>>> type(18.5)
<class 'float'>
>>> type("Alice")
<class 'str'>
>>> type(False)
<class 'bool'>
```

On utilise `int` pour représenter un entier relatif, `float` pour un nombre flottant, `str` pour du texte et `bool` pour une information logique.

Le choix d'un type constitue donc une première étape de **modélisation d'une information réelle**.
{{< /solution >}}

{{< note success "À retenir" >}}
Un programme manipule des représentations d'informations. Le **type** précise la nature des valeurs manipulées et détermine les opérations que Python pourra leur appliquer.

| **Type** | **Information représentée** | **Exemple** |
|:---|:---|:---|
| `int` | nombre entier relatif | `12` |
| `float` | nombre décimal approché | `18.5` |
| `str` | texte | `"Alice"` |
| `bool` | vrai ou faux | `True` |
{{< /note >}}

{{< qcm >}}
- question: 'Quel type Python convient pour représenter la réponse à la question « l''élève est-il majeur ? » ?'
  reponses:
    - '`str` (on écrit `"oui"` ou `"non"`)'
    - '`bool`'
    - '`int` (on écrit `1` ou `0`)'
    - '`float`'
  bonne: 2
  explication: 'Une information qui ne peut être que vraie ou fausse se représente par un booléen : `True` ou `False`. Une chaîne `"oui"` fonctionnerait, mais Python ne pourrait pas l''utiliser directement comme une condition.'
- question: 'Que retourne l''évaluation de `type("32")` ?'
  reponses:
    - "`<class 'int'>`"
    - "`<class 'float'>`"
    - "`<class 'str'>`"
    - "`<class 'bool'>`"
  bonne: 3
  explication: 'Les guillemets indiquent une chaîne de caractères, même si son contenu ressemble à un nombre : `"32"` est un `str`, `32` est un `int`.'
- question: 'Une température de 18,5 °C s''écrit en Python :'
  reponses:
    - '`18,5`'
    - '`18.5`'
    - '`"18.5"`'
  bonne: 2
  explication: 'Python utilise le point comme séparateur décimal : `18.5` est un `float`. Avec une virgule, `18,5` est interprété comme deux valeurs séparées (un tuple). Avec des guillemets, on obtient un texte, pas un nombre.'
{{< /qcm >}}

## Écrire des expressions et comprendre leur évaluation

{{< question >}}
Prévoir la valeur de chacune des expressions suivantes :

```python
>>> 3 + 4
>>> 2 * 5 + 1
>>> "NS" + "I"
>>> -7 / 0
```

Vérifier ensuite vos réponses dans la console. Quel point commun possèdent ces quatre écritures ?
{{< /question >}}

{{< solution "Réponse" >}}
Elles produisent respectivement `7`, `11`, `'NSI'` et `ZeroDivisionError`.

Ces quatre écritures sont des **expressions** : Python les évalue pour obtenir une valeur.
{{< /solution >}}

{{< note success "À retenir" >}}
Une **expression** décrit un calcul permettant d'obtenir une valeur. L'action de déterminer cette valeur est appelée **évaluation de l'expression**.
{{< /note >}}

{{< question >}}
On souhaite calculer $3 x^2 + 2 x + 4$ pour $x = 5$.
Tester les expressions suivantes dans la console :

```python
>>> 3x^2 + 2x + 4
>>> 3 * 5^2 + 2 * 5 + 4
>>> 3 * 5**2 + 2 * 5 + 4
```

Laquelle de ces expressions permet d'obtenir le résultat attendu ? Quelles différences importantes existe-t-il entre l'écriture mathématique et l'écriture Python ?
{{< /question >}}

{{< solution "Réponse" >}}
L'expression correcte est :

```python
>>> 3 * 5**2 + 2 * 5 + 4
89
```

Python exige d'écrire explicitement les multiplications avec `*`. La puissance s'écrit `**` et non `^`.
{{< /solution >}}

{{< question >}}
Prévoir les valeurs des expressions suivantes puis vérifier le résultat de l'évaluation par Python :

```python
>>> 7 + 3
>>> 7 - 3
>>> 7 * 3
>>> 7 / 3
>>> 7 // 3
>>> 7 % 3
>>> 7 ** 3
```
Associer ensuite à chaque opérateur son rôle.
{{< /question >}}

{{< solution "Réponse" >}}
| `+` | addition |
|:---|:---|
| `-` | soustraction |
| `*` | multiplication |
| `/` | division |
| `//` | quotient de la division euclidienne |
| `%` | reste de la division euclidienne |
| `**` | puissance |
{{< /solution >}}

{{< question >}}
Déterminer les valeurs des deux expressions suivantes :

```python
>>> 17 // 5
>>> 17 % 5
```

Utiliser les résultats obtenus pour compléter l'expression mathématique : $17 = \dots \times 5 + \dots$.  
Recommencer avec les valeurs 38 et 7. À quoi servent les opérateurs `//` et `%` ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient $17 = 3 \times 5 + 2$ et $38 = 5 \times 7 + 3$.

`//` retourne le quotient de la division euclidienne et `%` son reste.
{{< /solution >}}

{{< question >}}
Évaluer les expressions suivantes :

```python
>>> 8 / 2
>>> 8 // 2
>>> type(8 / 2)
>>> type(8 // 2)
>>> type(8.0 // 2)
```

Que remarquez-vous ?
{{< /question >}}

{{< solution "Réponse" >}}
`/` retourne ici `4.0`, de type `float`, tandis que `8 // 2` retourne `4`, de type `int`. Avec `8.0 // 2`, le résultat est un `float`.
{{< /solution >}}

### Dans quel ordre Python effectue-t-il les opérations ?

{{< question >}}
Sans utiliser Python, prévoir la valeur des expressions suivantes :

```python
>>> 2 + 3 * 4
>>> (2 + 3) * 4
>>> 2 * 3**2
>>> (2 * 3)**2
```

Vérifier ensuite dans la console. Python effectue-t-il simplement les opérations de gauche à droite ?
{{< /question >}}

{{< solution "Réponse" >}}
Les résultats sont respectivement `14`, `20`, `18` et `36`. Python applique des règles de priorité ; les parenthèses permettent de modifier l'ordre d'évaluation.
{{< /solution >}}

### Observer pas à pas une évaluation avec Thonny

Dans la partie centrale de l'éditeur Thonny, écrire :

```python
2 * (3 + 4)**2 + 5 * 6 // 2
```

Lancer le programme en mode **débogage** puis utiliser la touche <kbd>F7</kbd>.

{{< question >}}
À l'aide de Thonny, relever l'ordre dans lequel les sous-expressions sont évaluées. Comparer cet ordre avec celui utilisé pour effectuer le calcul à la main.
{{< /question >}}

{{< solution "Réponse" >}}
On observe notamment : `3 + 4`, l'élévation au carré, la multiplication par 2, `5 * 6`, la division entière par 2, puis l'addition des deux résultats.

Une expression complexe est évaluée par réduction progressive de sous-expressions plus simples.
{{< /solution >}}

{{< qcm >}}
- question: 'Quelle expression Python calcule $3 x^2 + 2 x + 4$ pour $x = 5$ ?'
  reponses:
    - '`3x^2 + 2x + 4`'
    - '`3 * 5^2 + 2 * 5 + 4`'
    - '`3 * 5**2 + 2 * 5 + 4`'
    - '`3 * 5 ** 2 + 2 5 + 4`'
  bonne: 3
  explication: 'En Python, la multiplication s''écrit toujours avec `*` et la puissance avec `**`. Le symbole `^` existe, mais il désigne une tout autre opération.'
- question: 'Que valent `17 // 5` et `17 % 5` ?'
  reponses:
    - '`3` et `2`'
    - '`3.4` et `2`'
    - '`2` et `3`'
    - '`3.4` et `0.4`'
  bonne: 1
  explication: '$17 = 3 \times 5 + 2$ : `//` donne le quotient de la division euclidienne (3) et `%` son reste (2).'
- question: 'Quel est le type de la valeur de `8 / 2` ?'
  reponses:
    - '`int`, car 8 est divisible par 2'
    - '`float`'
    - '`str`'
  bonne: 2
  explication: 'L''opérateur `/` retourne toujours un flottant : `8 / 2` vaut `4.0`. Pour obtenir l''entier `4`, on utilise la division entière `8 // 2`.'
- question: 'Que vaut `2 * 3**2` ?'
  reponses:
    - '`36`'
    - '`18`'
    - '`12`'
  bonne: 2
  explication: 'La puissance est prioritaire sur la multiplication : Python calcule d''abord `3**2 = 9`, puis `2 * 9 = 18`. Pour obtenir 36, il faut écrire `(2 * 3)**2`.'
{{< /qcm >}}

## Comment utiliser une fonction déjà écrite ?

En mathématiques, une fonction associe à une valeur d'entrée (**l'antécédent**) une valeur de sortie (**l'image**) : pour $f(x) = x^2$, l'entrée $3$ donne la sortie $9$.

{{< note success "À retenir" >}}
En programmation, une **fonction** est un outil qui porte un **nom**, reçoit des données appelées **arguments** et **retourne** un résultat après avoir effectué un traitement. Utiliser une fonction, c'est l'**appeler** en écrivant son nom suivi de parenthèses.
{{< /note >}}

Python fournit déjà de nombreuses fonctions prêtes à l'emploi : on apprend d'abord à s'en servir, avant d'apprendre à en écrire soi-même.

### De quoi se compose l'appel d'une fonction ?

{{< question >}}
Tester les appels de fonctions suivants :

```python
>>> abs(-5)
>>> round(3.14159, 2)
>>> max(4, 9)
```

Pour chaque appel, identifier le nom de la fonction, le ou les arguments et la valeur retournée.
{{< /question >}}

{{< solution "Réponse" >}}
Dans `abs(-5)`, `abs` est le nom de la fonction, `-5` l'argument et `5` la valeur retournée. Dans `round(3.14159, 2)`, la fonction `round` reçoit deux arguments et retourne `3.14`.
{{< /solution >}}

### Comment savoir ce que fait une fonction ?

{{< question >}}
Évaluer les expressions suivantes :

```python
>>> help(abs)
>>> help(round)
```

Quelles opérations réalisent ces fonctions ? Combien d'arguments peut-on leur fournir ? Pourquoi la fonction `help` est-elle importante pour un programmeur ?
{{< /question >}}

{{< solution "Réponse" >}}
`help` permet de consulter la documentation d'une fonction. Un programmeur n'a pas à mémoriser toutes les fonctions : il doit savoir consulter leur documentation et comprendre comment les utiliser.
{{< /solution >}}

{{< question >}}
Évaluer les expressions suivantes :

```python
>>> sum(4, 7)
>>> help(sum)
```

Pourquoi le nom d'une fonction ne suffit-il pas pour savoir comment l'utiliser ?
{{< /question >}}

{{< solution "Réponse" >}}
L'appel proposé ne correspond pas à l'utilisation attendue de `sum`. La documentation indique notamment que son premier argument doit être un objet itérable, notion qui sera étudiée ultérieurement.
{{< /solution >}}

### À quoi servent les modules ?

De nombreuses fonctions fournies avec le langage Python sont regroupées dans des **modules**.

{{< question >}}
Tester le code suivant dans la console :

```python
>>> import math
>>> dir(math)
```

Repérer les noms des fonctions qui permettent de calculer : une racine carrée, un sinus, un cosinus et le nom de la variable qui référence la constante $\pi$. 
Exécuter ensuite `help(math.sqrt)` et calculer la racine carrée de 81.
{{< /question >}}

{{< solution "Réponse" >}}
On trouve notamment `math.sqrt`, `math.sin`, `math.cos` et `math.pi`.

```python
>>> math.sqrt(81)
9.0
```
{{< /solution >}}

{{< note idea "Module" >}}
Un **module** regroupe des fonctions (et parfois des variables) consacrées à un même domaine : calculs mathématiques, tirages aléatoires, interfaces graphiques, etc. Après :
```python
import math
```
un élément (une fonction par exemple) du module `math` est accessible avec la syntaxe `math.nom`.
{{< /note >}}

{{< question >}}
À l'aide de la fonction `help`, découvrir comment et pourquoi utiliser la fonction `random.randint`, puis écrire un appel retournant un entier aléatoire compris entre 1 et 10. Les deux bornes peuvent-elles être obtenues ?\
Travailler dans la console.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> import random
>>> help(random.randint)
>>> random.randint(1, 10)
```

Les deux bornes sont incluses.
{{< /solution >}}

### Que peut-on écrire comme argument d'une fonction ?

{{< question >}}
Sans utiliser Python, prévoir ce que retournent ces appels de fonctions, puis les tester dans la console :

```python
>>> abs(3 - 8)
>>> math.sqrt(4 + 5)
>>> abs(3 + 4 / 2 + 7 // 3)
```

Que devient une expression utilisée comme argument d'une fonction ?
{{< /question >}}

{{< solution "Réponse" >}}
Python commence par évaluer l'expression utilisée comme argument. Ainsi `abs(3 - 8)` devient d'abord `abs(-5)`, puis produit `5`.
{{< /solution >}}

{{< question >}}
Dans la partie principale de l'éditeur Thonny, écrire :

```python
import math

math.sqrt(abs(3 - 12))
```

Lancer le programme en mode **débogage** puis utiliser la touche <kbd>F7</kbd>. Décrire l'ordre des calculs.
{{< /question >}}

{{< solution "Réponse" >}}
Python évalue d'abord $3 - 12 = -9$, puis `abs(-9)` qui vaut 9, puis `math.sqrt(9)` qui vaut 3.

La valeur retournée par une fonction peut donc être utilisée comme argument d'une autre fonction.
{{< /solution >}}

{{< question >}}
Dans la partie principale de l'éditeur Thonny, écrire :

```python
max(2 + 3, 4 * 2)
```

Lancer le programme en mode **débogage** puis utiliser la touche <kbd>F7</kbd>. Relever les valeurs successives prises par chacun des deux arguments avant que la fonction `max` ne soit appliquée. Que peut-on en conclure sur la nature d'un argument ?
{{< /question >}}

{{< solution "Réponse" >}}
Thonny évalue d'abord séparément chaque argument : `2 + 3` devient `5` et `4 * 2` devient `8`. L'appel se ramène alors à `max(5, 8)`, qui retourne `8`.

**Un argument est une expression** : Python la réduit à une valeur avant d'effectuer l'appel de la fonction.
{{< /solution >}}

{{< question >}}
Prévoir la valeur de chacune des expressions suivantes, puis les écrire dans la partie principale de l'éditeur Thonny :

```python
round(math.sqrt(50), 1)
max(abs(-10), round(7.4))
```

Il sera peut être nécessaire de rechercher à l'aide de la fonction `help` l'action de chacune des fonctions qui doivent être utilisées.

Lancer le programme en mode **débogage** puis utiliser la touche <kbd>F7</kbd>. Pour chaque expression, indiquer quelle fonction est appelée en premier, quelle valeur elle retourne, et comment cette valeur est ensuite utilisée.
{{< /question >}}

{{< solution "Réponse" >}}
Dans `round(math.sqrt(50), 1)`, Python évalue d'abord `math.sqrt(50)`, qui retourne environ `7.071`. Cette valeur devient le premier argument de `round` : l'appel se ramène à `round(7.071, 1)`, qui retourne `7.1`.

Dans `max(abs(-10), round(7.4))`, les deux arguments sont d'abord évalués : `abs(-10)` retourne `10` et `round(7.4)` retourne `7`. L'appel devient `max(10, 7)`, qui retourne `10`.

La valeur retournée par une fonction peut donc servir d'argument à une autre fonction : c'est la **composition de fonctions**.
{{< /solution >}}

{{< note success "À retenir" >}}
**Appeler (ou utiliser) une fonction**, c'est écrire son **nom** suivi de parenthèses contenant ses **arguments**, séparés par des virgules : `round(3.14159, 2)`.

- Une fonction reçoit zéro, un ou plusieurs arguments et **retourne** une valeur après avoir effectué un traitement.
- Chaque argument est une **expression** : Python l'évalue d'abord, puis effectue l'appel.
- La valeur retournée peut être réutilisée, en particulier comme argument d'une autre fonction : `math.sqrt(abs(3 - 12))`.
- Le nom d'une fonction ne suffit pas pour savoir l'utiliser : on consulte sa **documentation** avec `help`.
- Des fonctions supplémentaires sont regroupées dans des **modules**, chargés avec `import` puis utilisés avec la syntaxe `module.nom`.
{{< /note >}}

{{< qcm >}}
- question: 'Dans l''appel `round(3.14159, 2)`, quels sont les arguments ?'
  reponses:
    - '`round`'
    - '`3.14159` et `2`'
    - '`3.14`'
    - '`round`, `3.14159` et `2`'
  bonne: 2
  explication: '`round` est le nom de la fonction ; les arguments sont les valeurs placées entre les parenthèses ; `3.14` est la valeur retournée.'
- question: 'Lors de l''appel `abs(3 - 8)`, que se passe-t-il en premier ?'
  reponses:
    - 'La fonction `abs` est appliquée à `3`, puis à `8`.'
    - 'Python évalue l''expression `3 - 8`, qui vaut `-5`, puis appelle `abs(-5)`.'
    - 'Python affiche une erreur : un argument doit être une valeur, pas un calcul.'
  bonne: 2
  explication: 'Un argument est une expression : Python l''évalue d''abord, puis appelle la fonction avec la valeur obtenue. Ici `abs(-5)` retourne `5`.'
- question: 'Après `import math`, comment calcule-t-on la racine carrée de 81 ?'
  reponses:
    - '`sqrt(81)`'
    - '`math.sqrt(81)`'
    - '`math(sqrt(81))`'
    - '`81.sqrt()`'
  bonne: 2
  explication: 'Une fonction d''un module s''utilise avec la syntaxe `module.nom` : `math.sqrt(81)` retourne `9.0`.'
- question: 'On ne sait pas comment utiliser la fonction `sum`. Que faire ?'
  reponses:
    - 'Deviner d''après son nom, puis essayer `sum(4, 7)`.'
    - 'Consulter sa documentation avec `help(sum)`.'
    - 'Importer le module `sum`.'
  bonne: 2
  explication: 'Le nom d''une fonction ne suffit pas pour savoir l''utiliser : `sum(4, 7)` provoque d''ailleurs une erreur. `help` affiche la documentation, qui indique les arguments attendus.'
{{< /qcm >}}

## Comment définir une nouvelle fonction ?

Le langage Python fournit un très grand nombre de fonctions mais il est absolument nécessaire d'être capable d'en définir de nouvelles.

### Écrire et tester sa première fonction

{{< question >}}
Dans l'éditeur, recopier le code suivant :

```python
def carre(x: float) -> float:
    return x**2
```

Puis appeler la fonction depuis la console :

```python
>>> carre(3)
>>> carre(-2)
>>> carre(1.5)
```

Identifier le nom de la fonction, son paramètre, le type de ce paramètre, le type de la valeur retournée, le rôle de `return` dans le corps de la fonction.\
Quels sont les arguments utilisés lors de l'appel de la fonction ?
{{< /question >}}

{{< solution "Réponse" >}}
La fonction se nomme `carre` et son paramètre est `x`. C'est un `float`. `return` indique la valeur que la fonction retourne ; ici c'est un `float`. Dans `carre(3)`, `3` est un argument. 
{{< /solution >}}

{{< note idea "Paramètres, arguments" >}}
Dans la définition :

```python
def carre(x: float) -> float:
    return x**2
```

`x` est un **paramètre**. Dans `carre(5)`, `5` est un **argument**.
{{< /note >}}

{{< question >}}
Tester puis corriger la définition de fonction suivante :

```python
def triple(x: float) -> float:
return 3 * x
```

Quelle règle de syntaxe met en évidence l'erreur ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def triple(x: float) -> float:
    return 3 * x
```

Le corps de la fonction doit être **indenté**.
{{< /solution >}}

### Comment décrire une fonction sans montrer son code ?

{{< question >}}
Soit la fonction `surface_rectangle` dont la définition est :

```python
def surface_rectangle(longueur: float, largeur: float) -> float:
    return longueur * largeur
```

Combien possède-t-elle de paramètres ? Quels types sont annoncés pour les paramètres et la valeur retournée ?
{{< /question >}}

{{< solution "Réponse" >}}
La fonction possède deux paramètres, `longueur` et `largeur`, annotés avec `float`. La valeur retournée est également annoncée de type `float`.
{{< /solution >}}

{{< note success "À retenir" >}}
Le **type d'une fonction** est constitué des types de ses paramètres et du type de sa valeur de retour. La **signature** associe le nom de la fonction à son type.
{{< /note >}}

{{< question >}}
On donne seulement le type de la fonction `calcul` :

```python
def calcul(x: float) -> float:
    ...
```

Peut-on savoir si cette fonction calcule le carré de $x$, son double ou son opposé ? Que manque-t-il ?
{{< /question >}}

{{< solution "Réponse" >}}
Non. La signature ne suffit pas à déterminer le traitement réalisé. Il manque une description du rôle de la fonction : sa **documentation**.
{{< /solution >}}

{{< question >}}
Observer la définition de la fonction `carre` :

```python
def carre(x: float) -> float:
    """ Retourne le carré du nombre x. """
    return x**2
```

Quelle partie explique **ce que fait** la fonction ? Quelle partie explique **comment elle le fait** ?
{{< /question >}}

{{< solution "Réponse" >}}
La chaîne de documentation explique ce que fait la fonction ; le corps `return x**2` indique comment le calcul est effectué.
{{< /solution >}}

{{< note success "À retenir" >}}
La **spécification** constitue le contrat entre le concepteur d'une fonction et son utilisateur.

$$\text{Spécification} = \text{Signature} + \text{Documentation}$$

Elle indique essentiellement **ce que fait la fonction, pas comment elle le fait**.
{{< /note >}}

### Une fonction sans erreur donne-t-elle toujours le bon résultat ?

{{< question >}}
On souhaite définir une fonction dont la spécification est :

```python
def retire_un(n: float) -> float:
    """Retourne la valeur de n diminuée de 1."""
```

Un élève propose :

```python
def retire_un(n: float) -> float:
    """Retourne la valeur de n diminuée de 1."""
    return 1 - n
```

Python accepte-t-il cette définition ? Que retourne `retire_un(5)` ? Quelle valeur devrait-elle retourner ? Corriger la fonction.
{{< /question >}}

{{< solution "Réponse" >}}
La fonction est syntaxiquement correcte mais `retire_un(5)` retourne `-4` au lieu de `4`.

```python
def retire_un(n: float) -> float:
    """Retourne la valeur de n diminuée de 1."""
    return n - 1
```
{{< /solution >}}

### Peut-on construire une fonction à partir d'une autre ?

{{< question >}}
Définir :

```python
def somme(x: float, y: float, z: float) -> float:
    """Retourne la somme de x, y et z."""
    return x + y + z
```

Puis compléter :

```python
def moyenne(a: float, b: float, c: float) -> float:
    """Retourne la moyenne de a, b et c."""
    return ...
```

La fonction `moyenne` doit utiliser la fonction `somme`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def moyenne(a: float, b: float, c: float) -> float:
    """Retourne la moyenne de a, b et c."""
    return somme(a, b, c) / 3
```
{{< /solution >}}

{{< note success "À retenir" >}}
**Définir une fonction**, c'est décrire une fois pour toutes le traitement qu'elle réalise, pour pouvoir ensuite l'**appeler** autant de fois que nécessaire.

```python
def moyenne(a: float, b: float, c: float) -> float:
    """Retourne la moyenne de a, b et c."""
    return (a + b + c) / 3
```

- On commence par le mot-clé `def`, suivi du **nom** de la fonction.
- Entre parenthèses, on liste les **paramètres**, chacun annoté par son **type** (`a: float`). Après `->`, on annonce le **type de la valeur retournée**.
- La ligne d'en-tête se termine par `:`. Le **corps** de la fonction est **indenté**.
- La **documentation** (chaîne entre triples guillemets) décrit **ce que fait** la fonction.
- `return` indique la **valeur retournée** par la fonction, puis met fin à son exécution.
- Le corps d'une fonction peut **appeler d'autres fonctions**, déjà définies ou fournies par Python.

Tant qu'elle n'est pas **appelée** (`moyenne(12, 15, 9)`), une fonction définie n'exécute aucun calcul.
{{< /note >}}

{{< qcm >}}
- question: 'Dans `def carre(x: float) -> float:`, puis l''appel `carre(5)`, quel est le paramètre et quel est l''argument ?'
  reponses:
    - '`x` est l''argument, `5` est le paramètre.'
    - '`x` est le paramètre, `5` est l''argument.'
    - '`float` est le paramètre, `5` est l''argument.'
  bonne: 2
  explication: 'Le paramètre est le nom utilisé dans la définition ; l''argument est la valeur fournie au moment de l''appel.'
- question: 'Que manque-t-il à cette définition pour que Python l''accepte ?<br>`def triple(x: float) -> float:`<br>`return 3 * x`'
  reponses:
    - 'Des parenthèses autour de `3 * x`.'
    - 'L''indentation du corps de la fonction.'
    - 'Le mot-clé `print`.'
  bonne: 2
  explication: 'Le corps d''une fonction doit être indenté (décalé vers la droite) après la ligne d''en-tête, qui se termine par `:`.'
- question: 'Que contient la spécification d''une fonction ?'
  reponses:
    - 'Son code, ligne par ligne.'
    - 'Sa signature et sa documentation.'
    - 'Uniquement son nom.'
    - 'La liste des appels déjà effectués.'
  bonne: 2
  explication: 'Spécification = signature + documentation. Elle dit ce que fait la fonction, pas comment elle le fait.'
- question: 'La fonction `retire_un` retourne `1 - n` au lieu de `n - 1`. Que se passe-t-il ?'
  reponses:
    - 'Python refuse la définition.'
    - 'Python accepte la définition, mais `retire_un(5)` retourne `-4` au lieu de `4`.'
    - 'Python corrige automatiquement l''erreur.'
  bonne: 2
  explication: 'Une fonction peut être syntaxiquement correcte et pourtant ne pas respecter sa spécification : il faut la tester.'
- question: 'Que se passe-t-il quand Python lit la définition `def moyenne(a, b, c): ...` ?'
  reponses:
    - 'Il calcule une moyenne.'
    - 'Il mémorise la fonction ; aucun calcul n''est fait tant qu''elle n''est pas appelée.'
    - 'Il demande les valeurs de `a`, `b` et `c`.'
  bonne: 2
  explication: 'Définir une fonction, c''est décrire un traitement une fois pour toutes. Il ne s''exécute qu''à l''appel, par exemple `moyenne(12, 15, 9)`.'
{{< /qcm >}}

## Exercices de synthèse

**Consigne :** pour chacune des fonctions définies ci-dessous, donner systématiquement leur spécification complète.

### Exercice 1 : Programmer une fonction polynomiale

{{< question >}}
Définir la fonction `polynomiale` qui reçoit les arguments `a, b, c, d, x` et qui retourne le résultat du calcul $a x^3 + b x^2 + c x + d$. \
Tests :
```python
>>> polynomiale(1, 1, 1, 1, 2)
15
>>> polynomiale(1, 1, 1, 1, 3)
40
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def polynomiale(a: float, b: float, c: float,
                d: float, x: float) -> float:
    """Retourne ax^3 + bx^2 + cx + d."""
    return a * x**3 + b * x**2 + c * x + d
```
{{< /solution >}}

### Exercice 2 : Programmer une moyenne pondérée

{{< question >}}
Définir la fonction `moyenne_ponderee` qui reçoit les arguments `x, y, z, a, b, c` et qui calcule la moyenne pondérée des valeurs $x, y, z$ par les coefficients $a, b, c$. La fonction doit utiliser la fonction `somme`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def moyenne_ponderee(x: float, y: float, z: float,
                     a: float, b: float, c: float) -> float:
    """Retourne la moyenne pondérée de x, y et z."""
    return (a * x + b * y + c * z) / somme(a, b, c)
```
{{< /solution >}}

### Exercice 3 : Calculer des surfaces et des volumes

{{< question >}}
Définir successivement les fonctions `surface_rectangle`, `volume_parallelepipede` en utilisant la fonction précédente, `surface_disque` avec `math.pi`, puis `surface_couronne` avec deux appels à `surface_disque`. 

![Couronne](/premieres-nsi/chap-2/2-1/couronne.svg?width=40%)
{{< /question >}}

{{< solution "Réponse" >}}
```python
def surface_rectangle(longueur: float, largeur: float) -> float:
    """Retourne la surface d'un rectangle."""
    return longueur * largeur

def volume_parallelepipede(longueur: float,
                           largeur: float,
                           hauteur: float) -> float:
    """Retourne le volume d'un parallélépipède rectangle."""
    return surface_rectangle(longueur, largeur) * hauteur

def surface_disque(r: float) -> float:
    """Retourne la surface d'un disque de rayon r."""
    return math.pi * r**2

def surface_couronne(r1: float, r2: float) -> float:
    """Retourne la surface d'une couronne."""
    return surface_disque(r2) - surface_disque(r1)
```
{{< /solution >}}

### Exercice 4 : Calculer la distance entre deux points

{{< question >}}
Dans un repère orthonormé, on peut claculer la distance $A B$ à partir des coordonnées des points $A$ et $B$ : 
$$A B = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

Définir la fonction `distance` qui reçoit les arguments `x1, y1, x2, y2` et retourne la valeur de la distance entre les deux points.\
Tests :
```python
>>> distance(0, 0, 3, 4)
5.0
>>> distance(2, 3, 2, 3)
0.0
>>> distance(3, 4, 0, 0)
5.0
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def distance(x1: float, y1: float,
             x2: float, y2: float) -> float:
    """Retourne la distance entre deux points du plan."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```
{{< /solution >}}

### Exercice 5 : Reconstruire un tirage aléatoire

{{< question >}}
Consulter la documentation de la fonction `random.randint`.

Définir la fonction `tirage_entier` qui reçoit comme argument un entier `a` et qui retourne un entier aléatoire compris entre 1 et $a$, bornes incluses. On suppose $a$ entier strictement positif.
{{< /question >}}

{{< solution "Réponse" >}}
```py
def tirage_entier(a: int) -> int:
  """ retourne un entier compris entre 1 et a.
  return random.randint(1, a)
```
{{< /solution >}}

{{< question >}}
Reprendre l'exercice précédent mais cette fois n'utiliser que la fonction `random.random` du module `random`, la multiplication, l'addition et la fonction `int`. Justifier l'expression avant de programmer.\
**Cet exercice est beaucoup plus difficile !**
{{< /question >}}

{{< solution "Réponse" >}}
`random.random()` retourne un nombre $x$ tel que $0 \leq  x < 1$. Donc $0 \leq  a x < a$ et `int(random.random() * a)` produit un entier de 0 à $a - 1$. Il suffit ensuite d'ajouter 1 pour réaliser le traitement attendu.

```python
def tirage_entier(a: int) -> int:
    """Retourne un entier aléatoire compris entre 1 et a."""
    return int(random.random() * a) + 1
```
{{< /solution >}}

## Bilan : où en suis-je ?

Pour chaque ligne, cochez la colonne qui correspond. Toute case **Pas encore** indique une partie à reprendre.

| **Je sais…** | **Oui** | **Pas encore** | **À revoir** |
|:---|:---|:---|:---|
| choisir un **type** (`int`, `float`, `str`, `bool`) pour représenter une information |  |  | Partie 1 |
| prévoir la valeur d'une **expression** et l'ordre dans lequel Python effectue les calculs |  |  | Partie 2 |
| **appeler** une fonction, puis repérer ses **arguments** et sa valeur de retour |  |  | Partie 3 |
| trouver comment utiliser une fonction inconnue avec `help`, et importer un **module** |  |  | Partie 3 |
| **définir** une fonction avec `def` et `return`, corps indenté |  |  | Partie 4 |
| rédiger la **spécification** d'une fonction et vérifier qu'elle la respecte |  |  | Partie 4 |
