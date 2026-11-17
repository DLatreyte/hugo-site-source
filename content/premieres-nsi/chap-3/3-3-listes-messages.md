---
title: "Une liste est un objet auquel on peut passer des messages"
subtitle: "Doc. 3,3"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["objet", "message", "méthode", "notation pointée", "liste vide", "append", "pop", "insert", "remove", "None", "effet de bord", "alias", "pile", "file"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 30
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-3/3-3/3-3-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/premieres-nsi/chap-3/3-3/3-3-corrige.pdf" >}}

{{< note goal >}}
Faire grandir et rétrécir une liste en lui envoyant des messages, en particulier `append` et `pop`, et savoir si un message modifie la liste ou renvoie une valeur.
{{< /note >}}

{{< question >}}
On veut noter la liste des courses au fur et à mesure qu'on y pense. Au départ, on n'a pensé à rien : la liste est vide. Prévoir ce qui se passe lorsqu'on saisit les deux instructions suivantes dans la console, puis vérifier :

```python
>>> courses = []
>>> courses[0] = "pain"
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> courses[0] = "pain"
IndexError: list assignment index out of range
```
La liste vide n'a aucun élément, donc aucun indice valide. `courses[0] = ...` ne peut que **remplacer** un élément qui existe déjà. On ne peut pas, de cette façon, ajouter un élément à une liste.
{{< /solution >}}

Dans le Doc. 3,2, on contournait la difficulté en fabriquant d'abord une liste de la bonne taille, par exemple `[0] * 6`, puis en la remplissant. Cela suppose de connaître la taille à l'avance. Pour une liste de courses, ce n'est pas le cas : on ne sait pas combien de choses on va y écrire. Il faut un moyen de dire à la liste « ajoute cet élément au bout ».

## Envoyer un message à une liste

### Objets, messages et méthodes

En Python, chaque valeur est un **objet** : un nombre, une chaîne de caractères, un tuple, une liste. Pour l'instant, retenons qu'un objet regroupe des données et des actions qu'il sait effectuer sur ces données. Les objets seront étudiés en détail en terminale. Ici, on apprend seulement à s'en servir : pour demander à un objet d'effectuer l'une de ses actions, on lui **envoie un message**. On écrit le nom de l'objet, un point, puis le message suivi de parenthèses :

```python
courses.append("pain")
```

Cette instruction se lit : « on envoie à la liste `courses` le message `append` (ajouter, en anglais), avec l'argument `"pain"` ». La liste reçoit le message et réagit : elle place `"pain"` à sa fin. La façon dont un objet réagit à un message s'appelle une **méthode**. On dit indifféremment « envoyer le message `append` » ou « appeler la méthode `append` ».

Ce n'est pas la première fois que vous envoyez un message. Dans le Doc. 2,2, l'écriture `"...{}...".format(...)` envoyait le message `format` à une chaîne de caractères.

Comparons avec une fonction. Pour connaître la longueur d'une liste, on écrit `len(courses)` : on **donne** la liste à la fonction `len`, qui l'examine. Avec `courses.append("pain")`, on **s'adresse** à la liste elle-même, et c'est elle qui se modifie.

{{< question >}}
Saisir les instructions suivantes dans la console, en prévoyant le résultat de chaque ligne avant de la valider :

```python
>>> courses = []
>>> courses.append("pain")
>>> courses
>>> len(courses)
>>> courses.append("lait")
>>> courses.append("œufs")
>>> courses
>>> courses[2]
```

À quel indice se trouve l'élément qu'on vient d'ajouter avec `append` ? Exprimer cet indice à l'aide de `len(courses)`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> courses
['pain']
>>> len(courses)
1
>>> courses
['pain', 'lait', 'œufs']
>>> courses[2]
'œufs'
```
La ligne `courses.append("pain")` n'affiche rien : elle modifie la liste sans rien renvoyer. Chaque `append` allonge la liste d'un élément. L'élément ajouté est toujours le dernier, il se trouve donc à l'indice `len(courses) - 1`.
{{< /solution >}}

{{< note success "À retenir" >}}
En Python, une liste est un **objet**. On lui envoie un **message** avec la notation pointée : `liste.message(arguments)`. La façon dont l'objet réagit au message s'appelle une **méthode**.

`t.append(x)` ajoute l'élément `x` à la fin de la liste `t`. La liste est modifiée, sa longueur augmente de 1. Cela fonctionne aussi à partir de la liste vide `[]`.
{{< /note >}}

### Construire une liste en partant de la liste vide

La méthode `append` permet une façon de construire une liste qu'on utilisera très souvent : partir de la liste vide, puis ajouter les éléments un par un, au fil d'une boucle.

**Exemple résolu**

On veut la liste des multiples de `k` compris entre 1 et `n`.

```python
def multiples(n: int, k: int) -> list[int]:
    """Retourne la liste des multiples de k compris entre 1 et n.

    >>> multiples(20, 3)
    [3, 6, 9, 12, 15, 18]
    """
    resultat = []                # 1. on part de la liste vide
    for i in range(1, n + 1):    # 2. on examine chaque entier de 1 à n
        if i % k == 0:           # 3. s'il convient...
            resultat.append(i)   #    ... on l'ajoute au bout de la liste
    return resultat              # 4. on retourne la liste construite
```

Suivons l'appel `multiples(20, 3)`. Au départ, `resultat` vaut `[]`. Pour `i` égal à 1 et 2, le test est faux : rien ne se passe. Pour `i` égal à 3, le test est vrai : la liste devient `[3]`. Elle devient `[3, 6]` au tour où `i` vaut 6, et ainsi de suite. On n'a jamais eu besoin de savoir combien de multiples on allait trouver : la liste grandit d'elle-même.

{{< question >}}
En suivant la même méthode, écrire la fonction `diviseurs` dont la spécification est :

```python
def diviseurs(n: int) -> list[int]:
    """Retourne la liste des diviseurs de l'entier n, avec n >= 1,
    rangés dans l'ordre croissant.

    >>> diviseurs(12)
    [1, 2, 3, 4, 6, 12]
    >>> diviseurs(7)
    [1, 7]
    """
```

Pourquoi la méthode `[0] * taille` du Doc. 3,2 serait-elle mal adaptée ici ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def diviseurs(n: int) -> list[int]:
    """Retourne la liste des diviseurs de l'entier n, avec n >= 1,
    rangés dans l'ordre croissant.
    """
    resultat = []
    for d in range(1, n + 1):
        if n % d == 0:
            resultat.append(d)
    return resultat
```
Avec `[0] * taille`, il faudrait connaître à l'avance le nombre de diviseurs de `n`. Or on ne le connaît qu'après les avoir tous cherchés. Les diviseurs étant examinés dans l'ordre croissant, ils sont ajoutés dans cet ordre.
{{< /solution >}}

{{< question >}}
**Retour sur le Loto.** Dans le Doc. 3,2, la fonction `loto` partait de `[0] * 6` et utilisait une variable `nbre_tirees` pour savoir où ranger le prochain numéro. Réécrire cette fonction en partant de la liste vide et en utilisant `append` :

```python
def loto() -> list[int]:
    """Retourne une liste de 6 entiers différents, tirés au hasard
    entre 1 et 49 (bornes incluses).
    """
```

Quelle variable de l'ancienne version devient inutile ? Par quoi est-elle remplacée ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
import random

def loto() -> list[int]:
    """Retourne une liste de 6 entiers différents, tirés au hasard
    entre 1 et 49 (bornes incluses).
    """
    tirage = []
    while len(tirage) < 6:
        boule = random.randint(1, 49)
        if boule not in tirage:
            tirage.append(boule)
    return tirage
```
La variable `nbre_tirees` devient inutile. Le nombre de numéros déjà tirés est la longueur de la liste, `len(tirage)`, et `append` range lui-même le numéro à la première place libre, c'est-à-dire au bout. Le programme est plus court, et il ne contient plus de zéros de remplissage.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. On ne sait pas combien de tirages il faudra, puisqu'un numéro déjà sorti est rejeté. La boucle reste donc une boucle `while`.
1. La boucle doit s'arrêter quand la liste contient 6 numéros. Quelle expression donne le nombre de numéros déjà rangés ?
{{< /note >}}

{{< qcm >}}
- question: 'Après `t = []`, `t.append(4)` puis `t.append(9)`, que vaut `t` ?'
  reponses:
    - '`[4, 9]`'
    - '`[9, 4]`'
    - '`[13]`'
  bonne: 1
  explication: '`append` ajoute chaque élément à la fin de la liste.'
- question: 'Que représente l''écriture `t.append(x)` ?'
  reponses:
    - 'L''envoi du message `append` à l''objet liste `t`, avec l''argument `x`.'
    - 'L''appel d''une fonction `append` qui reçoit deux arguments.'
    - 'La création d''une nouvelle liste qui contient `x`.'
  bonne: 1
  explication: 'C''est la notation pointée : `objet.message(arguments)`. La liste `t` elle-même est modifiée.'
- question: 'Pour construire la liste des diviseurs de `n` en partant de `[]`, quelle instruction faut-il placer dans la boucle, quand `d` divise `n` ?'
  reponses:
    - '`resultat.append(d)`'
    - '`resultat = resultat.append(d)`'
    - '`resultat[d] = d`'
  bonne: 1
  explication: 'On ajoute `d` à la fin de la liste. La deuxième proposition remplacerait la liste par `None` ; la troisième provoquerait une erreur `IndexError`, car la liste est trop courte.'
{{< /qcm >}}

## Retirer un élément : le message pop

Le message `pop` fait l'inverse de `append` : il retire un élément de la liste. Mais il fait aussi autre chose, que l'on va découvrir.

{{< question >}}
Saisir les instructions suivantes dans la console, en prévoyant le résultat de chaque ligne avant de la valider :

```python
>>> pile = [3, 7, 12, 5]
>>> pile.pop()
>>> pile
>>> x = pile.pop(0)
>>> x
>>> pile
>>> pile.pop()
>>> pile.pop()
>>> pile.pop()
```

1. Quel élément `pop()` retire-t-il lorsqu'on ne lui donne pas d'argument ? Et `pop(0)` ?
1. Contrairement à `append`, la ligne `pile.pop()` affiche quelque chose. Que représente ce qui est affiché ?
1. Pourquoi la dernière ligne provoque-t-elle une erreur ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> pile.pop()
5
>>> pile
[3, 7, 12]
>>> x = pile.pop(0)
>>> x
3
>>> pile
[7, 12]
>>> pile.pop()
12
>>> pile.pop()
7
>>> pile.pop()
IndexError: pop from empty list
```
1. Sans argument, `pop()` retire le **dernier** élément. Avec un argument, `pop(i)` retire l'élément d'indice `i` : `pop(0)` retire le premier.
1. `pop` fait deux choses à la fois : il retire l'élément de la liste **et** il renvoie cet élément. C'est pour cela qu'on peut le ranger dans une variable, comme avec `x = pile.pop(0)`.
1. Après deux `pop()`, la liste est vide. On ne peut rien retirer d'une liste vide.
{{< /solution >}}

{{< note success "À retenir" >}}
`t.pop()` retire le dernier élément de la liste `t` et le renvoie. `t.pop(i)` retire l'élément d'indice `i` et le renvoie. Dans les deux cas, la longueur de la liste diminue de 1.

Envoyer `pop` à une liste vide provoque l'erreur `IndexError`. Avant un `pop`, il faut donc s'assurer que la liste n'est pas vide, par exemple avec `len(t) > 0`.
{{< /note >}}

Les deux messages `append` et `pop()` agissent sur la **fin** de la liste. Utilisés ensemble, ils font de la liste une pile d'assiettes : on pose une assiette sur le dessus, on reprend toujours celle du dessus. C'est exactement ce que fait la commande « Annuler » d'un traitement de texte. Chaque action est ajoutée au bout d'un historique. Annuler, c'est retirer la dernière action effectuée.

{{< question >}}
**Sans exécuter le programme**, prévoir les affichages du programme suivant. Écrire le contenu de la liste `historique` après chaque ligne qui la modifie. Vérifier ensuite.

```python
historique = []
historique.append("écrire Bonjour")
historique.append("mettre en gras")
historique.append("écrire Monde")
derniere = historique.pop()
print("Annulé :", derniere)
historique.append("souligner")
derniere = historique.pop()
print("Annulé :", derniere)
derniere = historique.pop()
print("Annulé :", derniere)
print(historique)
```
{{< /question >}}

{{< solution "Réponse" >}}
Contenu de `historique` après chaque modification :
- `["écrire Bonjour"]` ;
- `["écrire Bonjour", "mettre en gras"]` ;
- `["écrire Bonjour", "mettre en gras", "écrire Monde"]` ;
- après le premier `pop` : `["écrire Bonjour", "mettre en gras"]` ;
- `["écrire Bonjour", "mettre en gras", "souligner"]` ;
- après le deuxième `pop` : `["écrire Bonjour", "mettre en gras"]` ;
- après le troisième `pop` : `["écrire Bonjour"]`.

Affichages :
```text
Annulé : écrire Monde
Annulé : souligner
Annulé : mettre en gras
['écrire Bonjour']
```
Chaque annulation retire l'action la plus récente qui n'a pas encore été annulée.
{{< /solution >}}

{{< question >}}
Un élève veut écrire une fonction qui retourne les éléments d'une liste dans l'ordre inverse. Il a l'idée de vider la liste avec `pop()`, en ajoutant au fur et à mesure chaque élément retiré dans une nouvelle liste :

```python
def inverser(t: list[int]) -> list[int]:
    """Retourne une nouvelle liste formée des éléments de t
    pris dans l'ordre inverse.

    >>> inverser([12, 15, 9, 14])
    [14, 9, 15, 12]
    """
    resultat = []
    while len(t) > 0:
        resultat.append(t.pop())
    return resultat
```

1. Recopier la fonction, puis saisir dans la console :
   ```python
   >>> releve = [12, 15, 9, 14]
   >>> r = inverser(releve)
   >>> r
   >>> releve
   ```
   La fonction retourne-t-elle le bon résultat ? Quel autre effet a-t-elle ?
1. Expliquer cet effet à l'aide du Doc. 3,2.
1. Corriger la fonction pour que la liste reçue en argument ne soit pas modifiée, en conservant l'idée de l'élève.
{{< /question >}}

{{< solution "Réponse" >}}
1. `r` vaut bien `[14, 9, 15, 12]`. Mais `releve` vaut maintenant `[]` : la fonction a vidé la liste du programme principal.
1. Lors de l'appel, le paramètre `t` devient un alias de `releve` : les deux noms référencent la même liste. Chaque `t.pop()` retire un élément de cette liste unique. C'est un effet de bord, et il n'est pas annoncé dans la documentation.
1. On travaille sur une copie, construite en compréhension comme dans le Doc. 3,2 :
```python
def inverser(t: list[int]) -> list[int]:
    """Retourne une nouvelle liste formée des éléments de t
    pris dans l'ordre inverse.
    """
    copie = [x for x in t]
    resultat = []
    while len(copie) > 0:
        resultat.append(copie.pop())
    return resultat
```
On vide la copie, et `releve` reste intacte.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. Au moment de l'appel `inverser(releve)`, combien de listes existent en mémoire ? Combien de noms les référencent ?
1. Le message `pop` modifie la liste qui le reçoit. Sur quelle liste faudrait-il l'envoyer pour que `releve` ne soit pas touchée ?
{{< /note >}}

{{< qcm >}}
- question: 'Après `pile = [3, 7, 12, 5]` puis `x = pile.pop()`, que valent `x` et `pile` ?'
  reponses:
    - '`x` vaut `5` et `pile` vaut `[3, 7, 12]`.'
    - '`x` vaut `3` et `pile` vaut `[7, 12, 5]`.'
    - '`x` vaut `None` et `pile` vaut `[3, 7, 12]`.'
  bonne: 1
  explication: 'Sans argument, `pop` retire le dernier élément et le renvoie.'
- question: 'Après `t = [3, 7, 12]` puis `t.pop(0)`, que vaut `t` ?'
  reponses:
    - '`[7, 12]`'
    - '`[3, 7]`'
    - '`[0, 7, 12]`'
  bonne: 1
  explication: '`pop(0)` retire l''élément d''indice 0, c''est-à-dire le premier.'
- question: 'Que produit `[].pop()` ?'
  reponses:
    - 'Une erreur `IndexError`.'
    - '`None`'
    - '`[]`'
  bonne: 1
  explication: 'On ne peut rien retirer d''une liste vide : il faut le vérifier avant, par exemple avec `len(t) > 0`.'
{{< /qcm >}}

## Un message qui modifie la liste ne renvoie rien

{{< question >}}
Une élève veut ajouter le lait à sa liste de courses. Elle écrit :

```python
>>> courses = ["pain"]
>>> courses = courses.append("lait")
>>> print(courses)
None
```

Sa liste a disparu. Elle essaie alors de ranger des notes dans l'ordre croissant avec le message `sort` (trier) :

```python
>>> notes = [12, 15, 9, 14]
>>> print(notes.sort())
None
>>> notes
[9, 12, 14, 15]
```

1. Que renvoie le message `append` ? Et le message `sort` ?
1. Expliquer, étape par étape, ce qui s'est passé lors de l'instruction `courses = courses.append("lait")`.
1. Comment fallait-il écrire cette instruction ?
{{< /question >}}

{{< solution "Réponse" >}}
1. Ni `append` ni `sort` ne renvoient de liste. Ils renvoient la valeur spéciale `None`, qui signifie « rien ». Ces deux messages modifient la liste qui les reçoit : c'est leur seul rôle.
1. Python évalue d'abord le membre de droite. Le message `append` est envoyé à la liste `["pain"]`, qui devient `["pain", "lait"]`. Le message renvoie `None`. Ensuite seulement, l'affectation fait référencer `None` par la variable `courses`. La liste `["pain", "lait"]` existe toujours, mais plus aucune variable ne la référence : elle est perdue.
1. Il suffisait d'écrire `courses.append("lait")`, sans affectation.
{{< /solution >}}

Cette erreur est l'une des plus fréquentes chez les débutants, et chez les autres. Elle vient d'une confusion entre deux sortes de messages. Certains messages, comme `append` ou `sort`, **modifient** la liste et renvoient `None`. D'autres, comme `pop`, modifient la liste **et** renvoient une valeur utile. Il en existe enfin qui ne modifient rien et se contentent de renvoyer une information sur la liste, comme on va le voir dans la partie 4.

Puisque `append` modifie la liste elle-même, tous les alias de cette liste voient la modification. L'opérateur `+`, qui met deux listes bout à bout, se comporte autrement.

{{< question >}}
Prévoir, puis vérifier, le contenu de `n` et de `m` à la fin de chacune des deux séquences :

{{< columns >}}
```python
>>> n = [1, 2, 3]
>>> m = n
>>> m.append(4)
>>> n
>>> m
```
{{< column >}}
```python
>>> n = [1, 2, 3]
>>> m = n
>>> m = m + [4]
>>> n
>>> m
```
{{< endcolumns >}}

Expliquer la différence.
{{< /question >}}

{{< solution "Réponse" >}}
Première séquence : `n` et `m` valent tous les deux `[1, 2, 3, 4]`.

Seconde séquence : `n` vaut `[1, 2, 3]` et `m` vaut `[1, 2, 3, 4]`.

Dans les deux cas, après `m = n`, les deux noms référencent la même liste. Le message `append` modifie cette liste unique : la modification se voit par les deux noms. En revanche, `m + [4]` fabrique une **nouvelle** liste, et l'affectation fait référencer cette nouvelle liste par `m`. La liste de départ n'est pas touchée, et `n` la référence toujours. On retrouve la différence entre `reinitialiser_1` et `reinitialiser_2` du Doc. 3,2.
{{< /solution >}}

{{< note success "À retenir" >}}
Un message qui modifie la liste, comme `append` ou `sort`, renvoie `None`. On l'écrit seul sur sa ligne, **sans affectation** : `t.append(x)` et jamais `t = t.append(x)`.

`pop` modifie la liste et renvoie l'élément retiré, qu'on peut ranger dans une variable : `x = t.pop()`.

Un message envoyé à une liste agit sur la liste elle-même : tous ses alias voient la modification. L'expression `t + [x]`, elle, fabrique une nouvelle liste.
{{< /note >}}

{{< qcm >}}
- question: 'Après `courses = ["pain"]` puis `courses = courses.append("lait")`, que vaut `courses` ?'
  reponses:
    - '`None`'
    - '`[''pain'', ''lait'']`'
    - '`[''lait'']`'
  bonne: 1
  explication: '`append` modifie la liste puis renvoie `None`, et c''est cette valeur qui est affectée à `courses`.'
- question: 'Après `n = [1, 2, 3]`, `m = n` puis `m.append(4)`, que vaut `n` ?'
  reponses:
    - '`[1, 2, 3, 4]`'
    - '`[1, 2, 3]`'
  bonne: 1
  explication: '`m` et `n` sont des alias : le message modifie la liste unique qu''ils référencent.'
- question: 'Après `n = [1, 2, 3]`, `m = n` puis `m = m + [4]`, que vaut `n` ?'
  reponses:
    - '`[1, 2, 3]`'
    - '`[1, 2, 3, 4]`'
  bonne: 1
  explication: '`m + [4]` fabrique une nouvelle liste, que l''on affecte à `m`. La liste référencée par `n` n''est pas touchée.'
{{< /qcm >}}

## D'autres messages

Une liste comprend d'autres messages que `append` et `pop`. La commande `help(list)`, dans la console, en donne la liste complète, en anglais. En voici quelques-uns, traduits :

| **Message** | **Effet** | **Renvoie** |
|:---|:---|:---|
| `t.insert(i, x)` | insère `x` juste avant l'élément d'indice `i` | `None` |
| `t.remove(x)` | retire la première occurrence de `x` ; erreur `ValueError` si `x` est absent | `None` |
| `t.index(x)` | ne modifie pas la liste ; erreur `ValueError` si `x` est absent | l'indice de la première occurrence de `x` |
| `t.count(x)` | ne modifie pas la liste | le nombre d'occurrences de `x` |
| `t.reverse()` | renverse l'ordre des éléments | `None` |
| `t.sort()` | range les éléments dans l'ordre croissant | `None` |
| `t.copy()` | ne modifie pas la liste | une nouvelle liste, copie de `t` |

{{< question >}}
À l'aide de ces descriptions, et **sans exécuter les instructions**, prévoir le résultat de chaque ligne. Indiquer pour chacune si la liste `t` est modifiée. Vérifier ensuite dans la console.

```python
>>> t = [5, 8, 2, 8]
>>> t.insert(1, 10)
>>> t
>>> t.remove(8)
>>> t
>>> t.index(2)
>>> t.count(8)
>>> t.remove(7)
>>> t.reverse()
>>> t
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> t.insert(1, 10)
>>> t
[5, 10, 8, 2, 8]
>>> t.remove(8)
>>> t
[5, 10, 2, 8]
>>> t.index(2)
2
>>> t.count(8)
1
>>> t.remove(7)
ValueError: list.remove(x): x not in list
>>> t.reverse()
>>> t
[8, 2, 10, 5]
```
`insert`, `remove` et `reverse` modifient la liste et n'affichent rien, puisqu'ils renvoient `None`. `remove(8)` n'a retiré que le **premier** 8. `index` et `count` ne modifient pas la liste : ils renvoient une information. Le `remove(7)` provoque une erreur, puisque 7 n'est pas dans la liste, et la liste n'est pas modifiée.
{{< /solution >}}

{{< note info "Remarque" >}}
Dans la question sur la fonction `inverser`, on aurait pu écrire `copie = t.copy()` à la place de `copie = [x for x in t]`. Les deux instructions fabriquent une nouvelle liste contenant les mêmes éléments.
{{< /note >}}

{{< note success "À retenir" >}}
Avant d'utiliser un message, il faut savoir répondre à deux questions : modifie-t-il la liste ? que renvoie-t-il ?

`insert`, `remove`, `reverse` et `sort` modifient la liste et renvoient `None`. `pop` la modifie et renvoie l'élément retiré. `index`, `count` et `copy` ne la modifient pas et renvoient une information ou une nouvelle liste.
{{< /note >}}

{{< qcm >}}
- question: 'Après `t = [5, 8, 2, 8]` puis `t.remove(8)`, que vaut `t` ?'
  reponses:
    - '`[5, 2, 8]`'
    - '`[5, 2]`'
    - '`[5, 8, 2]`'
  bonne: 1
  explication: '`remove` retire la **première** occurrence de la valeur.'
- question: 'Quels messages modifient la liste qui les reçoit ?'
  reponses:
    - '`insert`'
    - '`sort`'
    - '`index`'
    - '`count`'
  bonne: [1, 2]
  explication: '`insert` et `sort` modifient la liste et renvoient `None`. `index` et `count` renvoient une information sans modifier la liste.'
- question: 'Avec `t = [5, 10, 2, 8]`, que vaut `t.index(2)` ?'
  reponses:
    - '`2`'
    - '`10`'
    - '`1`'
  bonne: 1
  explication: '`index` renvoie l''indice de la première occurrence de la valeur : 2 se trouve à l''indice 2.'
{{< /qcm >}}

## Exercices de synthèse

{{< note warning "Consigne" >}}
Écrire chaque fonction dans la partie principale de l'éditeur, avec sa spécification complète (signature et documentation). Tester ensuite chacun des exemples de la documentation dans la console. Aucune de ces fonctions ne doit modifier la liste qu'elle reçoit en argument.
{{< /note >}}

{{< question >}}
**Sans doublons.** Écrire la fonction `sans_doublons` dont la spécification est :

```python
def sans_doublons(t: list[int]) -> list[int]:
    """Retourne une nouvelle liste contenant les éléments de t,
    chacun une seule fois, dans l'ordre de leur première apparition.

    >>> sans_doublons([3, 1, 3, 2, 1])
    [3, 1, 2]
    >>> sans_doublons([])
    []
    """
```

Pourquoi ne peut-on pas obtenir ce résultat simplement avec une liste en compréhension filtrée par `if x not in t` ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def sans_doublons(t: list[int]) -> list[int]:
    """Retourne une nouvelle liste contenant les éléments de t,
    chacun une seule fois, dans l'ordre de leur première apparition.
    """
    resultat = []
    for x in t:
        if x not in resultat:
            resultat.append(x)
    return resultat
```
Le test porte sur la liste `resultat` **en cours de construction** : on n'ajoute `x` que s'il n'a pas déjà été ajouté. Dans une compréhension, la condition `x not in t` porte sur `t`, qui contient toujours `x` : elle serait toujours fausse. Une compréhension ne peut pas consulter la liste qu'elle est en train de fabriquer.
{{< /solution >}}

{{< question >}}
**Pairs et impairs.** Écrire la fonction `separer` dont la spécification est :

```python
def separer(valeurs: list[int]) -> tuple[list[int], list[int]]:
    """Retourne un tuple (pairs, impairs) : pairs est la liste des
    éléments pairs de valeurs, impairs celle des éléments impairs,
    dans l'ordre où ils apparaissent dans valeurs.

    >>> separer([4, 7, 10, 3, 8])
    ([4, 10, 8], [7, 3])
    """
```

Tester ensuite, dans la console, l'affectation multiple `p, i = separer([4, 7, 10, 3, 8])` (Doc. 3,1).
{{< /question >}}

{{< solution "Réponse" >}}
```python
def separer(valeurs: list[int]) -> tuple[list[int], list[int]]:
    """Retourne un tuple (pairs, impairs) : pairs est la liste des
    éléments pairs de valeurs, impairs celle des éléments impairs,
    dans l'ordre où ils apparaissent dans valeurs.
    """
    pairs = []
    impairs = []
    for v in valeurs:
        if v % 2 == 0:
            pairs.append(v)
        else:
            impairs.append(v)
    return pairs, impairs
```
On parcourt la liste une seule fois, et chaque élément est envoyé dans l'une des deux listes. Après l'affectation multiple, `p` vaut `[4, 10, 8]` et `i` vaut `[7, 3]`.
{{< /solution >}}

### Pour aller plus loin

{{< question >}}
**Une file d'attente.** À un guichet, les clients sont servis dans leur ordre d'arrivée : le premier arrivé est le premier servi. On décrit une matinée par une liste d'événements. Un prénom signale l'arrivée d'un client, qui se place au bout de la file. Le caractère `"*"` signale que le guichetier sert un client : celui qui attend depuis le plus longtemps.

```python
def guichet(evenements: list[str]) -> tuple[list[str], list[str]]:
    """Retourne un tuple (servis, en_attente) : servis est la liste
    des clients servis, dans l'ordre où ils l'ont été, en_attente
    celle des clients qui attendent encore à la fin.
    On suppose que la file n'est jamais vide quand "*" survient.

    >>> guichet(["Ana", "Bilal", "*", "Chloé", "Dylan", "*"])
    (['Ana', 'Bilal'], ['Chloé', 'Dylan'])
    """
```

1. Écrire la fonction `guichet`.
1. Un élève a écrit `pop()` au lieu de `pop(0)`. **Sans exécuter son programme**, prévoir ce que renvoie l'appel de la documentation. Pourquoi les clients ont-ils raison de se plaindre ?
{{< /question >}}

{{< solution "Réponse" >}}
1. ```python
   def guichet(evenements: list[str]) -> tuple[list[str], list[str]]:
       """Retourne un tuple (servis, en_attente) : servis est la liste
       des clients servis, dans l'ordre où ils l'ont été, en_attente
       celle des clients qui attendent encore à la fin.
       On suppose que la file n'est jamais vide quand "*" survient.
       """
       file = []
       servis = []
       for e in evenements:
           if e == "*":
               servis.append(file.pop(0))
           else:
               file.append(e)
       return servis, file
   ```
   Les clients arrivent au bout de la file (`append`) et sont servis au début (`pop(0)`).
1. Avec `pop()`, on obtient `(['Bilal', 'Dylan'], ['Ana', 'Chloé'])`. Au premier `"*"`, la file est `['Ana', 'Bilal']` : `pop()` sert Bilal, le dernier arrivé. Au second, la file est `['Ana', 'Chloé', 'Dylan']` : c'est Dylan qui est servi. Ana, arrivée la première, n'est jamais servie. La liste se comporte alors comme une pile d'assiettes, et non comme une file d'attente.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. La file est une liste qui part vide. Que faut-il lui envoyer quand un client arrive ?
1. Le client servi est celui qui est arrivé le premier. À quel indice de la file se trouve-t-il ?
1. Le client servi doit à la fois quitter la file et rejoindre la liste `servis`. Un seul message renvoie l'élément qu'il retire.
{{< /note >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- expliquer la différence entre appeler une fonction, comme `len(t)`, et envoyer un message à une liste, comme `t.append(x)` ;
- construire une liste en partant de la liste vide et en ajoutant ses éléments avec `append` dans une boucle ;
- retirer le dernier élément d'une liste, ou celui d'indice `i`, avec `pop`, et utiliser l'élément renvoyé ;
- éviter d'envoyer `pop` à une liste vide ;
- dire, pour un message donné, s'il modifie la liste et ce qu'il renvoie, et ne jamais écrire `t = t.append(x)` ;
- prévoir l'effet d'un message envoyé à une liste qui a plusieurs alias, notamment lorsqu'elle est passée en argument à une fonction ;
- utiliser une liste comme une pile (`append` et `pop()`) ou comme une file (`append` et `pop(0)`).
{{< /note >}}
