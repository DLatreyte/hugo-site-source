---
title: "Les tuples"
subtitle: "Doc. 3,1"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["type construit", "p-uplet", "tuple", "indice", "len", "non mutable", "concaténation", "affectation multiple", "assertion"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 10
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-3/3-1/3-1-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/premieres-nsi/chap-3/3-1/3-1-corrige.pdf" >}}

{{< note goal >}}
Regrouper plusieurs valeurs dans un seul objet, le tuple, pour qu'une fonction puisse renvoyer plusieurs résultats à la fois.
{{< /note >}}

## Une fonction peut-elle renvoyer deux valeurs ?

Dans le Doc. 2,4, la fonction `plus_grand_plus_petit` retournait une chaîne de caractères comme `"max : 18.0, min : 7.5"`. Pour un humain, c'est très lisible. Mais imaginons qu'on veuille ensuite calculer l'écart entre le maximum et le minimum. Il faudrait fouiller dans le texte pour retrouver les chiffres, puis les convertir en nombres. On a fabriqué une phrase alors qu'on voulait deux nombres.

Le vrai problème est le suivant : une instruction `return` met fin à la fonction. On ne peut donc pas écrire deux `return` à la suite en espérant récupérer deux résultats. Faisons une expérience.

{{< question >}}
Recopier la fonction suivante dans la partie principale de l'éditeur Thonny :

```python
def min_max(a: float, b: float):
    """Retourne le plus petit puis le plus grand des nombres a et b."""
    if a < b:
        return a, b
    return b, a
```

1. Appeler `min_max(9, 4)` dans la console. Qu'affiche-t-elle ?
1. Saisir ensuite `resultat = min_max(9, 4)`, puis `type(resultat)`. Combien d'objets la fonction a-t-elle retournés ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> min_max(9, 4)
(4, 9)
>>> resultat = min_max(9, 4)
>>> type(resultat)
<class 'tuple'>
```
La fonction a retourné **un seul** objet, de type `tuple`. Cet objet contient les deux nombres 4 et 9, dans cet ordre. C'est l'écriture `return b, a`, avec sa virgule, qui a demandé à Python de fabriquer ce tuple.
{{< /solution >}}

On n'a donc pas contourné la règle : une fonction renvoie toujours une seule valeur. On a simplement rangé les deux nombres dans une même boîte, et c'est la boîte qu'on renvoie.

{{< note success "À retenir" >}}
Un **tuple** (le programme dit aussi **p-uplet**) est une suite ordonnée de valeurs. On l'écrit en séparant les valeurs par des virgules, le plus souvent entre parenthèses : `(4, 9)`.

Le tuple est un **type construit** : il est fabriqué à partir de valeurs de types de base (`int`, `float`, `str`, `bool`).

Une fonction ne retourne qu'une seule valeur. Pour retourner plusieurs résultats, elle les regroupe dans un tuple : `return a, b`.
{{< /note >}}

{{< qcm >}}
- question: 'Avec la fonction `min_max` du cours, que vaut `type(min_max(9, 4))` ?'
  reponses:
    - '`<class ''tuple''>`'
    - '`<class ''int''>`'
    - 'Une erreur : une fonction ne peut retourner qu''une valeur.'
  bonne: 1
  explication: '`return a, b` regroupe les deux nombres dans un seul objet, un tuple.'
- question: 'Combien d''objets une fonction qui exécute `return a, b` retourne-t-elle ?'
  reponses:
    - 'Un seul : un tuple qui contient deux valeurs.'
    - 'Deux : `a`, puis `b`.'
    - 'Aucun : la virgule provoque une erreur.'
  bonne: 1
  explication: 'Une fonction retourne toujours un seul objet ; pour transmettre plusieurs résultats, on les regroupe dans un tuple.'
{{< /qcm >}}

## Créer un tuple et lire ses éléments

### C'est la virgule qui fait le tuple

{{< question >}}
Pour chacune des expressions suivantes, prévoir le type de la valeur obtenue, puis vérifier avec la fonction `type` dans la console :

```python
>>> type((3, 7, 12))
>>> type(3, 7, 12)
>>> type((5))
>>> type((5,))
>>> type(())
```

Le deuxième essai provoque une erreur. Pourquoi, à votre avis ? Comment écrire un tuple qui ne contient qu'un seul élément ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> type((3, 7, 12))
<class 'tuple'>
>>> type((5))
<class 'int'>
>>> type((5,))
<class 'tuple'>
>>> type(())
<class 'tuple'>
```

Dans `type(3, 7, 12)`, les virgules séparent les **arguments** de la fonction `type` : Python croit qu'on lui donne trois arguments, et non un tuple. Il faut ajouter des parenthèses pour qu'il comprenne qu'on lui donne un seul objet.

`(5)` est simplement le nombre 5 entre parenthèses, comme dans `(2 + 3) * 4`. Pour obtenir un tuple d'un seul élément, il faut une virgule : `(5,)`. Enfin, `()` est le tuple vide, qui ne contient aucun élément.
{{< /solution >}}

Les éléments d'un tuple ne sont pas forcément du même type. Une ville peut être décrite par son nom, sa latitude et sa longitude :

```python
ville = ("Paris", 48.86, 2.35)
```

Ce tuple n'a de sens que parce qu'on s'est mis d'accord sur l'ordre : d'abord le nom, ensuite la latitude, enfin la longitude. Si on écrivait `(48.86, "Paris", 2.35)`, Python ne protesterait pas, mais un programme qui attend le nom en premier serait trompé.

### Repérer un élément par son indice

Chaque élément d'un tuple occupe une position, appelée **indice**. En Python, les indices commencent à 0. Cela paraît étrange au début. Une façon de s'en souvenir : l'indice indique **combien de pas il faut faire depuis le début** pour atteindre l'élément. Le premier élément est à zéro pas du début.

| **indice** | 0 | 1 | 2 |
|:---|:---|:---|:---|
| **élément de** `t` | 3 | 7 | 12 |

On lit l'élément d'indice `i` du tuple `t` en écrivant `t[i]`. La fonction `len`, déjà rencontrée avec les chaînes de caractères, donne le nombre d'éléments du tuple.

{{< question >}}
Saisir `t = (3, 7, 12)` dans la console. Prévoir le résultat de chacune des instructions suivantes, puis vérifier :

```python
>>> t[0]
>>> t[2]
>>> len(t)
>>> t[3]
>>> t[len(t) - 1]
```

Quel est l'indice du dernier élément d'un tuple qui contient `n` éléments ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> t[0]
3
>>> t[2]
12
>>> len(t)
3
>>> t[3]
IndexError: tuple index out of range
>>> t[len(t) - 1]
12
```

Le tuple contient 3 éléments, d'indices 0, 1 et 2. L'indice 3 n'existe pas : Python signale une erreur `IndexError` (indice hors des limites). Comme on commence à compter à 0, le dernier élément d'un tuple de `n` éléments a pour indice `n - 1`.
{{< /solution >}}

{{< note tip "Indices négatifs" >}}
Python accepte aussi des indices négatifs, qui comptent à partir de la fin : `t[-1]` est le dernier élément, `t[-2]` l'avant-dernier. Avec `t = (3, 7, 12)`, `t[-1]` vaut `12`, exactement comme `t[len(t) - 1]`.
{{< /note >}}

{{< question >}}
Avec `ville = ("Paris", 48.86, 2.35)`, écrire une instruction qui affiche, à l'aide d'une f-string et des indices :

```text
Paris : latitude 48.86, longitude 2.35
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> print(f"{ville[0]} : latitude {ville[1]}, longitude {ville[2]}")
Paris : latitude 48.86, longitude 2.35
```
{{< /solution >}}

{{< note success "À retenir" >}}
Les éléments d'un tuple `t` sont repérés par leur **indice**, qui commence à 0. On lit l'élément d'indice `i` avec `t[i]`.

`len(t)` donne le nombre d'éléments de `t`. Les indices valides vont donc de `0` à `len(t) - 1`. Un indice en dehors de ces limites provoque une erreur `IndexError`.

Un tuple d'un seul élément s'écrit avec une virgule : `(5,)`. Le tuple vide s'écrit `()`.
{{< /note >}}

{{< qcm >}}
- question: 'Que vaut `type((5))` ?'
  reponses:
    - '`<class ''int''>`'
    - '`<class ''tuple''>`'
  bonne: 1
  explication: 'Les parenthèses seules ne font qu''entourer l''expression `5`. Pour un tuple d''un seul élément, il faut une virgule : `(5,)`.'
- question: 'Avec `t = (3, 7, 12)`, que produit `t[3]` ?'
  reponses:
    - '`12`'
    - '`7`'
    - 'Une erreur `IndexError`.'
  bonne: 3
  explication: 'Le tuple contient 3 éléments, d''indices 0, 1 et 2 : l''indice 3 n''existe pas.'
- question: 'Un tuple `t` contient `n` éléments. Quelles expressions donnent son dernier élément ?'
  reponses:
    - '`t[len(t) - 1]`'
    - '`t[-1]`'
    - '`t[len(t)]`'
    - '`t[n]`'
  bonne: [1, 2]
  explication: 'Les indices vont de `0` à `len(t) - 1`. L''indice négatif `-1` compte à partir de la fin. `t[len(t)]` et `t[n]` sont hors limites.'
{{< /qcm >}}

## Un tuple ne peut pas être modifié

{{< question >}}
Toujours avec `t = (3, 7, 12)`, essayer de remplacer le premier élément par 4 :

```python
>>> t[0] = 4
```

Que se passe-t-il ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> t[0] = 4
TypeError: 'tuple' object does not support item assignment
```
Python refuse : un objet de type `tuple` n'accepte pas qu'on affecte une nouvelle valeur à l'un de ses éléments.
{{< /solution >}}

Un tuple, une fois créé, ne change plus. On dit qu'il est **non mutable** (ou **immuable**). Est-ce gênant ? Pas vraiment, car on peut toujours fabriquer un **nouveau** tuple.

{{< question >}}
Prévoir, puis vérifier, le contenu de `t` et de `u` après chacune des instructions suivantes :

```python
>>> t = (3, 7, 12)
>>> u = t + (20,)
>>> u
>>> t
>>> t = (4, t[1], t[2])
>>> t
```

L'opérateur `+` a-t-il modifié `t` ? La dernière affectation a-t-elle modifié le tuple `(3, 7, 12)` ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> u = t + (20,)
>>> u
(3, 7, 12, 20)
>>> t
(3, 7, 12)
>>> t = (4, t[1], t[2])
>>> t
(4, 7, 12)
```

L'opérateur `+` **concatène** deux tuples : il met bout à bout leurs éléments dans un nouveau tuple. `t` n'a pas changé.

La dernière affectation ne modifie pas non plus le tuple `(3, 7, 12)`. Python évalue d'abord le membre de droite : il lit `t[1]` et `t[2]` et fabrique un nouveau tuple `(4, 7, 12)`. Ensuite seulement, la variable `t` référence ce nouveau tuple. Comme pour les nombres dans le Doc. 2,2, c'est la variable qui change de valeur, pas l'objet.
{{< /solution >}}

{{< question >}}
Prévoir puis vérifier le résultat de `7 in t` et de `8 in t`, avec `t = (4, 7, 12)`. De quel type est la valeur obtenue ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> 7 in t
True
>>> 8 in t
False
```
L'opérateur `in` teste si une valeur est présente dans le tuple. Il donne un booléen.
{{< /solution >}}

Pourquoi Python propose-t-il un objet qu'on ne peut pas modifier ? Parce que c'est une garantie. Les coordonnées de Paris ne vont pas changer pendant l'exécution du programme. Si on les range dans un tuple et qu'on les confie à une fonction, on est certain de les retrouver intactes, quelle que soit la façon dont cette fonction a été écrite.

{{< note success "À retenir" >}}
Un tuple est **non mutable** : on ne peut pas modifier ses éléments. L'instruction `t[0] = 4` provoque une erreur `TypeError`.

On peut en revanche construire un nouveau tuple, par exemple par **concaténation** avec l'opérateur `+` : `(3, 7) + (12,)` vaut `(3, 7, 12)`.

`valeur in t` vaut `True` si `valeur` est un élément de `t`, `False` sinon.
{{< /note >}}

{{< qcm >}}
- question: 'Avec `t = (3, 7, 12)`, que produit l''instruction `t[0] = 4` ?'
  reponses:
    - 'Une erreur `TypeError`.'
    - '`t` vaut désormais `(4, 7, 12)`.'
    - '`t` vaut désormais `(4, 3, 7, 12)`.'
  bonne: 1
  explication: 'Un tuple est non mutable : on ne peut pas affecter une nouvelle valeur à l''un de ses éléments.'
- question: 'Après `t = (3, 7, 12)` puis `u = t + (20,)`, que vaut `t` ?'
  reponses:
    - '`(3, 7, 12)`'
    - '`(3, 7, 12, 20)`'
    - '`(23, 27, 32)`'
  bonne: 1
  explication: 'La concaténation fabrique un **nouveau** tuple, rangé dans `u`. Le tuple `t` n''est pas modifié.'
- question: 'Avec `t = (4, 7, 12)`, que vaut `8 in t` ?'
  reponses:
    - '`False`'
    - '`True`'
    - '`1`'
  bonne: 1
  explication: '`in` teste la présence d''une valeur et donne un booléen : 8 n''est pas un élément de `t`.'
{{< /qcm >}}

## Parcourir un tuple

Un tuple est un objet **itérable**, au même titre que ce que produit `range` (voir Doc. 2,4). On peut donc le parcourir avec une boucle `for`. Il y a deux façons de le faire.

{{< question >}}
Recopier les deux fonctions suivantes dans l'éditeur :

```python
def somme(valeurs: tuple[float, ...]) -> float:
    """Retourne la somme des éléments du tuple valeurs."""
    total = 0
    for v in valeurs:
        total += v
    return total

def somme_2(valeurs: tuple[float, ...]) -> float:
    """Retourne la somme des éléments du tuple valeurs."""
    total = 0
    for i in range(len(valeurs)):
        total += valeurs[i]
    return total
```

1. Tester `somme((3, 7, 12))` et `somme_2((3, 7, 12))`.
1. Dans chaque fonction, quelles valeurs prend successivement la variable de boucle (`v` ou `i`) ?
1. L'annotation `tuple[float, ...]` signifie « tuple de nombres flottants, de longueur quelconque ». Pourquoi ne pas avoir écrit `tuple[float, float, float]` ?
{{< /question >}}

{{< solution "Réponse" >}}
1. Les deux appels retournent `22`.
1. Dans `somme`, `v` prend directement les **éléments** du tuple : `3`, puis `7`, puis `12`. Dans `somme_2`, `i` prend les **indices** : `0`, `1`, `2`, et on lit l'élément avec `valeurs[i]`.
1. `tuple[float, float, float]` annoncerait un tuple d'exactement trois éléments. Or la fonction doit fonctionner avec un tuple de n'importe quelle longueur.
{{< /solution >}}

La première écriture est plus courte. La seconde n'est utile que lorsqu'on a besoin de connaître la **position** des éléments, comme dans la question suivante.

{{< question >}}
Écrire la fonction `indice_max` dont la spécification est :

```python
def indice_max(valeurs: tuple[float, ...]) -> int:
    """Retourne l'indice du plus grand élément de valeurs.
    valeurs ne doit pas être vide.

    >>> indice_max((12, 5, 18, 7))
    2
    """
```

**Indication.** On suppose d'abord que le plus grand élément est celui d'indice 0, puis on compare cet élément à chacun des suivants.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def indice_max(valeurs: tuple[float, ...]) -> int:
    """Retourne l'indice du plus grand élément de valeurs.
    valeurs ne doit pas être vide.

    >>> indice_max((12, 5, 18, 7))
    2
    """
    i_max = 0
    for i in range(1, len(valeurs)):
        if valeurs[i] > valeurs[i_max]:
            i_max = i
    return i_max
```
Ici, une boucle `for v in valeurs` ne suffirait pas : elle donne les éléments, mais pas leur position.
{{< /solution >}}

{{< note success "À retenir" >}}
On parcourt un tuple `t` de deux façons :

- `for element in t:` donne directement les éléments, un par un ;
- `for i in range(len(t)):` donne les indices, et on lit l'élément avec `t[i]`. On utilise cette écriture lorsque la position de l'élément compte.
{{< /note >}}

{{< qcm >}}
- question: 'Avec `t = (3, 7, 12)`, quelles valeurs la variable `v` prend-elle dans `for v in t:` ?'
  reponses:
    - '`3`, puis `7`, puis `12`'
    - '`0`, puis `1`, puis `2`'
    - '`1`, puis `2`, puis `3`'
  bonne: 1
  explication: 'Cette écriture parcourt directement les éléments du tuple.'
- question: 'Pour écrire la fonction `indice_max`, quel parcours faut-il choisir ?'
  reponses:
    - '`for i in range(len(valeurs)):`, car on a besoin de la position des éléments.'
    - '`for v in valeurs:`, car on n''a besoin que des valeurs.'
  bonne: 1
  explication: 'La fonction doit retourner un indice : il faut connaître la position de chaque élément, donc parcourir les indices.'
{{< /qcm >}}

## Déballer un tuple

### L'affectation multiple

Quand un tuple contient peu d'éléments, il est souvent plus clair de donner un nom à chacun d'eux. Python permet de le faire en une seule ligne.

{{< question >}}
Saisir les instructions suivantes dans la console, en prévoyant le résultat avant chaque validation :

```python
>>> point = (2, 5)
>>> x, y = point
>>> x
>>> y
>>> a, b = (1, 2, 3)
```

Expliquer le message d'erreur obtenu à la dernière ligne.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> x
2
>>> y
5
>>> a, b = (1, 2, 3)
ValueError: too many values to unpack (expected 2)
```
`x, y = point` affecte à `x` le premier élément du tuple et à `y` le second. On dit qu'on **déballe** le tuple. À la dernière ligne, il y a deux variables à gauche mais trois valeurs à droite : Python ne sait pas quoi faire de la troisième (« trop de valeurs à déballer, 2 attendues »).
{{< /solution >}}

{{< question >}}
Reprendre la fonction `min_max` de la première partie. Écrire dans la console une instruction qui range le résultat de `min_max(9, 4)` dans deux variables `petit` et `grand`, puis calculer l'écart entre ces deux nombres.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> petit, grand = min_max(9, 4)
>>> grand - petit
5
```
C'est exactement ce qu'on ne pouvait pas faire facilement avec la chaîne `"max : ..., min : ..."` du Doc. 2,4.
{{< /solution >}}

### Retour sur l'échange de deux variables

Dans le Doc. 2,2, on a vu que la séquence `a = b` puis `b = a` n'échange pas les valeurs de deux variables, et qu'il fallait passer par une variable `tmp`. Avec les tuples, Python propose une écriture bien plus courte.

{{< question >}}
Saisir les instructions suivantes dans la console :

```python
>>> a = 605
>>> b = 506
>>> a, b = b, a
>>> a, b
```

1. Les valeurs ont-elles été échangées ?
1. La séquence `a = b` puis `b = a` échouait parce que la valeur de `a` était écrasée avant d'avoir été recopiée. Expliquer, en décrivant ce que fait Python dans l'ordre, pourquoi ce problème ne se pose pas ici.
{{< /question >}}

{{< solution "Réponse" >}}
1. Oui : on obtient `(506, 605)`.
1. Python évalue d'abord **tout** le membre de droite, `b, a`. Il fabrique ainsi le tuple `(506, 605)` avec les valeurs que les variables ont à ce moment-là. Ensuite seulement, il déballe ce tuple : `a` reçoit `506` et `b` reçoit `605`. Au moment où `a` change de valeur, l'ancienne valeur de `a` est déjà rangée dans le tuple : rien n'est perdu. Le tuple joue le rôle de la variable `tmp`.
{{< /solution >}}

{{< question >}}
**Pour l'épreuve écrite.** Sans utiliser Python, compléter le tableau d'état de la séquence suivante, puis vérifier dans la console.

```python
a, b = 3, 8
a, b = b, a + b
a, b = b - a, a
```

| **Instruction** | **a** | **b** |
|:---|:---|:---|
| `a, b = 3, 8` |  |  |
| `a, b = b, a + b` |  |  |
| `a, b = b - a, a` |  |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **Instruction** | **a** | **b** |
|:---|:---|:---|
| `a, b = 3, 8` | 3 | 8 |
| `a, b = b, a + b` | 8 | 11 |
| `a, b = b - a, a` | 3 | 8 |

À la deuxième ligne, `b` et `a + b` sont calculés avec les **anciennes** valeurs (`8` et `3 + 8 = 11`). À la troisième, `b - a` vaut `11 - 8 = 3` et `a` vaut encore `8`. La séquence a ramené les deux variables à leurs valeurs de départ.
{{< /solution >}}

{{< question >}}
Dans le Doc. 2,4, la fonction `fibo` utilisait une troisième variable `w` pour calculer le terme suivant de la suite de Fibonacci. Réécrire cette fonction sans la variable `w`, à l'aide d'une affectation multiple. Vérifier que `fibo(10)` retourne `'1 1 2 3 5 8 13 21 34 55 '`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def fibo(n: int) -> str:
    """Retourne les n premiers termes de la suite de Fibonacci,
    sous forme d'une chaîne de caractères.
    """
    u, v = 1, 1
    reponse = ""
    for rang in range(n):
        reponse += f"{u} "
        u, v = v, u + v
    return reponse
```
À chaque itération, `u` prend la valeur du terme suivant (`v`) et `v` celle du terme d'après (`u + v`, calculé avec l'ancienne valeur de `u`).
{{< /solution >}}

{{< note success "À retenir" >}}
L'**affectation multiple** `x, y = point` déballe un tuple : chaque variable de gauche reçoit l'élément de même position. Il doit y avoir autant de variables que d'éléments, sinon Python signale une erreur `ValueError`.

Dans `a, b = b, a`, Python évalue d'abord tout le membre de droite, qui forme un tuple, puis affecte les variables. C'est pourquoi cette instruction échange les valeurs de `a` et de `b`.
{{< /note >}}

{{< qcm >}}
- question: 'Après `point = (2, 5)` puis `x, y = point`, que vaut `y` ?'
  reponses:
    - '`5`'
    - '`2`'
    - '`(2, 5)`'
  bonne: 1
  explication: 'Chaque variable de gauche reçoit l''élément de même position : `x` vaut 2 et `y` vaut 5.'
- question: 'Que produit `a, b = (1, 2, 3)` ?'
  reponses:
    - 'Une erreur `ValueError`.'
    - '`a` vaut 1 et `b` vaut `(2, 3)`.'
    - '`a` vaut 1, `b` vaut 2 et le 3 est ignoré.'
  bonne: 1
  explication: 'Il doit y avoir autant de variables que d''éléments dans le tuple.'
- question: 'Que valent `a` et `b` après `a, b = 2, 5` puis `a, b = b, a + b` ?'
  reponses:
    - '`a` vaut 5 et `b` vaut 7.'
    - '`a` vaut 5 et `b` vaut 10.'
    - '`a` vaut 2 et `b` vaut 7.'
  bonne: 1
  explication: 'Le membre de droite est entièrement évalué avec les anciennes valeurs : il forme le tuple `(5, 7)`, puis les deux variables sont affectées.'
{{< /qcm >}}

## Écrire une fonction qui renvoie un tuple

Pour annoncer qu'une fonction retourne un tuple, on indique dans sa signature le type de chaque élément, dans l'ordre : `-> tuple[int, int]` signifie « retourne un tuple de deux entiers ». Pour un tuple de longueur quelconque dont tous les éléments ont le même type, on écrit `tuple[float, ...]`.

{{< note warning "Consigne" >}}
Écrire chaque fonction dans la partie principale de l'éditeur, avec sa spécification complète (signature et documentation). Tester ensuite chacun des exemples de la documentation dans la console.
{{< /note >}}

{{< question >}}
**Division euclidienne.** Écrire la fonction `division_euclidienne` dont la spécification est :

```python
def division_euclidienne(a: int, b: int) -> tuple[int, int]:
    """Retourne le quotient et le reste de la division euclidienne
    de a par b (b non nul).

    >>> division_euclidienne(17, 5)
    (3, 2)
    >>> division_euclidienne(20, 4)
    (5, 0)
    """
```

Comparer avec le résultat de la fonction `divmod(17, 5)`, fournie par Python.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def division_euclidienne(a: int, b: int) -> tuple[int, int]:
    """Retourne le quotient et le reste de la division euclidienne
    de a par b (b non nul).
    """
    return a // b, a % b
```
`divmod(17, 5)` retourne aussi `(3, 2)` : les concepteurs de Python ont fait le même choix, un tuple (quotient, reste).
{{< /solution >}}

{{< question >}}
**Convertir une durée.** Une course de fond a duré 3725 s. On veut exprimer cette durée en heures, minutes et secondes.

1. Sans ordinateur, effectuer la conversion à la main, en détaillant le calcul.
1. Écrire la fonction `convertir_duree` dont la spécification est :

```python
def convertir_duree(duree: int) -> tuple[int, int, int]:
    """Convertit une durée donnée en secondes en un tuple
    (heures, minutes, secondes).

    >>> convertir_duree(3725)
    (1, 2, 5)
    >>> convertir_duree(59)
    (0, 0, 59)
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
1. Une heure dure 3600 s et une minute dure 60 s.

   **A.N.** 3725 s $=$ 3600 s $+$ 125 s et 125 s $= 2 \times$ 60 s $+$ 5 s.

   La course a donc duré 1 h 2 min 5 s.

1. On reprend exactement les étapes du calcul à la main :

```python
def convertir_duree(duree: int) -> tuple[int, int, int]:
    """Convertit une durée donnée en secondes en un tuple
    (heures, minutes, secondes).
    """
    heures = duree // 3600
    reste = duree % 3600
    minutes = reste // 60
    secondes = reste % 60
    return heures, minutes, secondes
```
{{< /solution >}}

{{< question >}}
**Milieu d'un segment.** Dans un repère, un point est représenté par le tuple `(x, y)` de ses coordonnées. Écrire la fonction `milieu` dont la spécification est :

```python
def milieu(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    """Retourne les coordonnées du milieu du segment [AB].

    >>> milieu((0, 0), (4, 2))
    (2.0, 1.0)
    >>> milieu((-1, 3), (1, 3))
    (0.0, 3.0)
    """
```

**Indication.** Commencer par déballer chacun des deux tuples.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def milieu(a: tuple[float, float], b: tuple[float, float]) -> tuple[float, float]:
    """Retourne les coordonnées du milieu du segment [AB]."""
    xa, ya = a
    xb, yb = b
    return (xa + xb) / 2, (ya + yb) / 2
```
{{< /solution >}}

{{< question >}}
**Distance entre deux points.** Dans le Doc. 2,1, la fonction `distance` recevait quatre arguments `x1, y1, x2, y2`. Avec des tuples, deux arguments suffisent. On veut de plus que la fonction marche aussi dans l'espace, avec des points à trois coordonnées. Dans un repère orthonormé de l'espace, la distance entre $A(x_A, y_A, z_A)$ et $B(x_B, y_B, z_B)$ est :
$$A B = \sqrt{(x_B - x_A)^2 + (y_B - y_A)^2 + (z_B - z_A)^2}$$

1. Écrire la fonction `distance` dont la spécification est :

```python
def distance(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Retourne la distance entre les points a et b, qui doivent
    avoir le même nombre de coordonnées.

    >>> distance((0, 0), (3, 4))
    5.0
    >>> distance((1, 2, 3), (1, 2, 3))
    0.0
    >>> distance((0, 0, 0), (1, 2, 2))
    3.0
    """
```

2. Que devrait faire la fonction si on l'appelle avec `distance((0, 0), (1, 1, 1))` ? Ajouter au début du corps de la fonction l'instruction :

```python
assert len(a) == len(b), "les deux points doivent avoir la même dimension"
```

puis tester à nouveau cet appel.
{{< /question >}}

{{< solution "Réponse" >}}
1. On ne connaît pas à l'avance le nombre de coordonnées : on parcourt donc les indices.

```python
import math

def distance(a: tuple[float, ...], b: tuple[float, ...]) -> float:
    """Retourne la distance entre les points a et b, qui doivent
    avoir le même nombre de coordonnées.
    """
    assert len(a) == len(b), "les deux points doivent avoir la même dimension"
    somme_carres = 0
    for i in range(len(a)):
        somme_carres += (b[i] - a[i]) ** 2
    return math.sqrt(somme_carres)
```

2. Un point du plan et un point de l'espace n'ont pas de distance : la fonction ne devrait pas retourner de résultat. Sans l'assertion, la boucle s'arrêterait après deux coordonnées et retournerait `1.414...`, un nombre faux qui ne déclenche aucune alerte. Avec l'assertion, l'appel s'arrête net :

```python
>>> distance((0, 0), (1, 1, 1))
AssertionError: les deux points doivent avoir la même dimension
```
{{< /solution >}}

{{< note success "À retenir" >}}
L'instruction `assert condition, "message"` vérifie qu'une condition est vraie. Si elle est fausse, le programme s'arrête avec une erreur `AssertionError` et affiche le message.

On s'en sert pour vérifier une **précondition**, c'est-à-dire une condition que les arguments doivent respecter pour que la fonction ait un sens. Mieux vaut un programme qui s'arrête en expliquant pourquoi qu'un programme qui retourne un résultat faux sans prévenir.
{{< /note >}}

{{< question >}}
**Plus petit et plus grand élément.** Écrire la fonction `min_max_tuple` dont la spécification est :

```python
def min_max_tuple(valeurs: tuple[float, ...]) -> tuple[float, float]:
    """Retourne le plus petit et le plus grand élément de valeurs,
    qui ne doit pas être vide.

    >>> min_max_tuple((12, 5, 18, 7))
    (5, 18)
    >>> min_max_tuple((4,))
    (4, 4)
    """
```

Les fonctions `min` et `max` de Python ne doivent pas être utilisées. Vérifier la précondition par une assertion.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def min_max_tuple(valeurs: tuple[float, ...]) -> tuple[float, float]:
    """Retourne le plus petit et le plus grand élément de valeurs,
    qui ne doit pas être vide.
    """
    assert len(valeurs) > 0, "le tuple ne doit pas être vide"
    petit = valeurs[0]
    grand = valeurs[0]
    for v in valeurs:
        if v < petit:
            petit = v
        if v > grand:
            grand = v
    return petit, grand
```
Sans l'assertion, un tuple vide provoquerait une erreur `IndexError` à la ligne `petit = valeurs[0]`, avec un message qui n'explique pas la vraie cause.
{{< /solution >}}

{{< qcm >}}
- question: 'Que retourne `division_euclidienne(17, 5)` ?'
  reponses:
    - '`(3, 2)`'
    - '`(2, 3)`'
    - '`3.4`'
  bonne: 1
  explication: '$17 = 3 \times 5 + 2$ : le quotient vaut 3 et le reste 2, dans cet ordre.'
- question: 'Que se passe-t-il à l''exécution de `assert len(valeurs) > 0, "valeurs ne doit pas être vide"` lorsque `valeurs` vaut `()` ?'
  reponses:
    - 'Le programme s''arrête avec une erreur `AssertionError` qui affiche le message.'
    - 'Rien : l''instruction est ignorée.'
    - 'La fonction retourne `False`.'
  bonne: 1
  explication: 'La condition est fausse : `assert` arrête le programme en expliquant pourquoi, au lieu de laisser la fonction produire un résultat faux.'
- question: 'Quelle annotation de type, écrite comme dans le cours, convient à une fonction qui retourne une durée sous la forme `(heures, minutes, secondes)`, trois entiers ?'
  reponses:
    - '`-> tuple[int, int, int]`'
    - '`-> int, int, int`'
    - '`-> tuple`'
  bonne: 1
  explication: 'On indique le type de chacun des éléments du tuple retourné.'
{{< /qcm >}}

## Exercices de synthèse

{{< question >}}
**Équation du second degré.** On cherche les solutions réelles de l'équation $a x^2 + b x + c = 0$, avec $a \neq  0$. On note $\Delta = b^2 - 4 a c$ le discriminant.

- Si $\Delta > 0$, il y a deux solutions : $x_1 = (-b - \sqrt{\Delta}) / (2 a)$ et $x_2 = (-b + \sqrt{\Delta}) / (2 a)$.
- Si $\Delta = 0$, il y a une seule solution : $x_0 = -b / (2 a)$.
- Si $\Delta < 0$, il n'y a pas de solution réelle.

Le nombre de solutions change d'une équation à l'autre. Un tuple convient bien : il peut contenir deux, un ou zéro élément. Écrire la fonction `racines` dont la spécification est :

```python
def racines(a: float, b: float, c: float) -> tuple[float, ...]:
    """Retourne le tuple des solutions réelles de a x² + b x + c = 0,
    avec a non nul.

    >>> racines(1, -3, 2)
    (1.0, 2.0)
    >>> racines(1, 2, 1)
    (-1.0,)
    >>> racines(1, 0, 1)
    ()
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
import math

def racines(a: float, b: float, c: float) -> tuple[float, ...]:
    """Retourne le tuple des solutions réelles de a x² + b x + c = 0,
    avec a non nul.
    """
    assert a != 0, "a doit être non nul"
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = (-b + math.sqrt(delta)) / (2 * a)
        return x1, x2
    elif delta == 0:
        return (-b / (2 * a),)
    else:
        return ()
```
Attention à la virgule dans `(-b / (2 * a),)` : sans elle, la fonction retournerait un nombre et non un tuple.
{{< /solution >}}

{{< question >}}
**Comparer deux dates.** Une date est représentée par un tuple `(jour, mois, annee)`. Écrire la fonction `est_avant` dont la spécification est :

```python
def est_avant(d1: tuple[int, int, int], d2: tuple[int, int, int]) -> bool:
    """Retourne True si la date d1 est strictement antérieure
    à la date d2, False sinon.

    >>> est_avant((14, 7, 1789), (11, 11, 1918))
    True
    >>> est_avant((25, 12, 2025), (1, 1, 2025))
    False
    >>> est_avant((3, 5, 2026), (3, 5, 2026))
    False
    >>> est_avant((3, 5, 2026), (4, 5, 2026))
    True
    """
```

**Indication.** Comparer d'abord les années. Si elles sont égales, comparer les mois, et ainsi de suite.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def est_avant(d1: tuple[int, int, int], d2: tuple[int, int, int]) -> bool:
    """Retourne True si la date d1 est strictement antérieure
    à la date d2, False sinon.
    """
    j1, m1, a1 = d1
    j2, m2, a2 = d2
    if a1 != a2:
        return a1 < a2
    if m1 != m2:
        return m1 < m2
    return j1 < j2
```
{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- créer un tuple, y compris un tuple d'un seul élément `(5,)` et le tuple vide `()` ;
- lire un élément d'un tuple grâce à son indice, en sachant que les indices vont de `0` à `len(t) - 1` ;
- expliquer pourquoi `t[0] = 4` provoque une erreur, et construire un nouveau tuple à la place ;
- tester la présence d'une valeur dans un tuple avec `in` ;
- parcourir un tuple par ses éléments ou par ses indices, et choisir l'écriture adaptée ;
- déballer un tuple par une affectation multiple, et expliquer pourquoi `a, b = b, a` échange deux valeurs ;
- écrire une fonction qui renvoie un tuple de valeurs, avec une signature du type `-> tuple[int, int]` ;
- vérifier une précondition à l'aide d'une assertion.
{{< /note >}}
