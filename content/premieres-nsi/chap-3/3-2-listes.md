---
title: "Les listes"
subtitle: "Doc. 3,2"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["type construit", "liste", "indice", "mutable", "liste en compréhension", "alias", "effet de bord", "liste de listes", "matrice"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: false
auto_numbering: true
weight: 20
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-3/3-2/3-2-enonce.pdf" >}}

{{< note goal >}}
Ranger des valeurs de même type dans une liste, modifier et parcourir ses éléments, puis construire des listes, y compris des listes de listes.
{{< /note >}}

## Quand un tuple ne suffit plus

Un professeur range les notes d'un devoir dans un tuple :

```python
notes = (12, 15, 9, 14)
```

En relisant les copies, il s'aperçoit que la troisième note est fausse : c'est 11 et non 9. Avec un tuple, l'instruction `notes[2] = 11` provoque une erreur, puisqu'un tuple n'est pas mutable (Doc. 3,1). Il faudrait reconstruire un tuple complet, `(notes[0], notes[1], 11, notes[3])`, pour changer une seule valeur. Avec 35 élèves, ce serait pénible.

Python propose pour cela un autre type construit, la **liste**, qui s'écrit entre crochets.

{{< question >}}
Saisir les instructions suivantes dans la console :

```python
>>> notes = [12, 15, 9, 14]
>>> type(notes)
>>> notes[2] = 11
>>> notes
```

La modification a-t-elle été acceptée ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> type(notes)
<class 'list'>
>>> notes[2] = 11
>>> notes
[12, 15, 11, 14]
```
Oui : contrairement au tuple, la liste accepte qu'on remplace l'un de ses éléments. On dit qu'une liste est **mutable**.
{{< /solution >}}

{{< note success "À retenir" >}}
Une **liste** est une suite ordonnée de valeurs, écrite entre crochets et séparées par des virgules : `[12, 15, 9, 14]`. Son type est `list`.

Une liste est **mutable** : on peut modifier ses éléments après sa création, alors qu'un tuple ne le permet pas.

Dans cette activité, tous les éléments d'une même liste ont le même type.
{{< /note >}}

{{< note info "Remarque" >}}
Il ne faut pas confondre une liste avec un **tableau**. Un tableau est un ensemble de valeurs de même type, rangées les unes à la suite des autres dans la mémoire : on dit qu'elles sont **contiguës**. Une liste Python ne répond pas à cette définition : ses éléments peuvent être de types différents, et ils ne sont pas rangés côte à côte dans la mémoire. Python se sert de tableaux pour fabriquer ses listes, mais une liste n'est pas un tableau.
{{< /note >}}

{{< qcm >}}
- question: 'Après `notes = [12, 15, 9, 14]` puis `notes[2] = 11`, que vaut `notes` ?'
  reponses:
    - '`[12, 15, 11, 14]`'
    - '`[12, 11, 9, 14]`'
    - 'Une erreur `TypeError`, comme avec un tuple.'
  bonne: 1
  explication: 'Une liste est mutable : on peut remplacer l''élément d''indice 2, qui est le troisième.'
- question: 'Quelles affirmations sont exactes ?'
  reponses:
    - 'Une liste s''écrit entre crochets, un tuple le plus souvent entre parenthèses.'
    - 'Une liste est mutable, un tuple ne l''est pas.'
    - 'Une liste Python est un tableau : ses éléments sont contigus en mémoire.'
  bonne: [1, 2]
  explication: 'Une liste Python n''est pas un tableau : ses éléments ne sont pas rangés côte à côte en mémoire, et ils peuvent être de types différents.'
{{< /qcm >}}

## Lire et modifier les éléments d'une liste

Bonne nouvelle : tout ce qu'on a appris sur les indices des tuples reste vrai pour les listes.

{{< question >}}
Saisir `notes = [12, 15, 11, 14]` dans la console. Prévoir le résultat de chacune des instructions suivantes, puis vérifier :

```python
>>> notes[0]
>>> len(notes)
>>> notes[len(notes) - 1]
>>> notes[4]
>>> 15 in notes
>>> []
>>> len([])
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> notes[0]
12
>>> len(notes)
4
>>> notes[len(notes) - 1]
14
>>> notes[4]
IndexError: list index out of range
>>> 15 in notes
True
>>> []
[]
>>> len([])
0
```
Les indices vont de `0` à `len(notes) - 1`, soit de 0 à 3. `[]` est la liste vide, qui contient 0 élément.
{{< /solution >}}

Ce qui est nouveau, c'est qu'on peut écrire `notes[i]` à gauche du signe `=`. L'élément d'indice `i` est alors remplacé par une nouvelle valeur. Les opérateurs d'affectation du Doc. 2,2 fonctionnent aussi : `notes[1] += 2` ajoute 2 à l'élément d'indice 1.

{{< question >}}
Le professeur décide d'ajouter un point à chaque note. Un élève propose :

```python
notes = [12, 15, 11, 14]
for n in notes:
    n += 1
```

Un autre élève propose :

```python
notes = [12, 15, 11, 14]
for i in range(len(notes)):
    notes[i] += 1
```

1. Exécuter les deux propositions et afficher `notes` après chacune d'elles. Laquelle fonctionne ?
1. Expliquer pourquoi l'autre ne modifie pas la liste.
{{< /question >}}

{{< solution "Réponse" >}}
1. Seule la seconde fonctionne : on obtient `[13, 16, 12, 15]`. Avec la première, `notes` vaut toujours `[12, 15, 11, 14]`.
1. Suivons la première boucle pas à pas. Au premier tour, la variable `n` reçoit la valeur du premier élément, `12`. L'instruction `n += 1` calcule `13` et fait référencer ce nouveau nombre par `n`. À aucun moment on n'a écrit `notes[...] = ...` : la variable `n` a changé, la liste non. Au tour suivant, `n` reçoit `15`, et ainsi de suite. Pour modifier un élément de la liste, il faut savoir **où** il se trouve, donc connaître son indice.
{{< /solution >}}

{{< note success "À retenir" >}}
`t[i] = valeur` remplace l'élément d'indice `i` de la liste `t`.

Pour modifier les éléments d'une liste dans une boucle, on parcourt les **indices** : `for i in range(len(t)):`. La boucle `for element in t:` permet de lire les éléments, mais pas de les modifier.
{{< /note >}}

{{< qcm >}}
- question: 'Que vaut `len([])` ?'
  reponses:
    - '`0`'
    - '`1`'
    - 'Une erreur.'
  bonne: 1
  explication: 'La liste vide ne contient aucun élément.'
- question: 'Après `notes = [12, 15, 11, 14]` puis la boucle `for n in notes: n += 1`, que vaut `notes` ?'
  reponses:
    - '`[12, 15, 11, 14]`'
    - '`[13, 16, 12, 15]`'
    - '`[12, 15, 11, 15]`'
  bonne: 1
  explication: 'À chaque tour, `n` reçoit la valeur d''un élément ; modifier `n` ne modifie pas la liste.'
- question: 'Quelle boucle ajoute 1 à chaque élément de la liste `t` ?'
  reponses:
    - '`for i in range(len(t)): t[i] += 1`'
    - '`for x in t: x += 1`'
    - '`for i in t: t[i] += 1`'
  bonne: 1
  explication: 'Pour modifier les éléments, on parcourt les indices. Dans la troisième proposition, `i` prend les **valeurs** des éléments, qui ne sont pas des indices.'
{{< /qcm >}}

## Construire une liste

### Une liste de taille fixée à l'avance

L'opérateur `*` appliqué à une liste et à un entier répète la liste. Ainsi `[0] * 6` vaut `[0, 0, 0, 0, 0, 0]`. On obtient une liste de 6 éléments, qu'on peut ensuite remplir par indice.

{{< question >}}
Recopier et compléter la fonction suivante, qui doit construire la liste des carrés des entiers de 0 à `n - 1` :

```python
def carres(n: int) -> list[int]:
    """Retourne la liste des carrés des entiers de 0 à n - 1.

    >>> carres(5)
    [0, 1, 4, 9, 16]
    """
    resultat = [0] * n
    for i in range(n):
        ...
    return resultat
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def carres(n: int) -> list[int]:
    """Retourne la liste des carrés des entiers de 0 à n - 1."""
    resultat = [0] * n
    for i in range(n):
        resultat[i] = i * i
    return resultat
```
{{< /solution >}}

### Une liste en compréhension

En mathématiques, on décrit parfois un ensemble par une règle plutôt qu'en écrivant tous ses éléments : ${k^2 | k \in {0, 1, 2, 3, 4}}$ se lit « l'ensemble des $k^2$ pour $k$ appartenant à $\{0, 1, 2, 3, 4\}$ ». Python permet d'écrire une liste de la même façon :

```python
[k * k for k in range(5)]
```

Cette expression se lit presque comme la phrase : « la liste des `k * k` pour `k` parcourant `range(5)` ». On dit que la liste est construite **en compréhension**. Elle remplace les quatre lignes du corps de la fonction `carres`.

{{< question >}}
Prévoir la liste obtenue pour chacune des expressions suivantes, puis vérifier dans la console :

```python
>>> [2 * k + 1 for k in range(5)]
>>> [n / 2 for n in [12, 15, 11, 14]]
>>> [len(mot) for mot in ["tuple", "liste", "indice"]]
>>> [k for k in range(1, 21) if k % 3 == 0]
```

À quoi sert la partie `if k % 3 == 0` dans la dernière expression ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> [2 * k + 1 for k in range(5)]
[1, 3, 5, 7, 9]
>>> [n / 2 for n in [12, 15, 11, 14]]
[6.0, 7.5, 5.5, 7.0]
>>> [len(mot) for mot in ["tuple", "liste", "indice"]]
[5, 5, 6]
>>> [k for k in range(1, 21) if k % 3 == 0]
[3, 6, 9, 12, 15, 18]
```
La partie `if` sert de filtre : seuls les entiers `k` pour lesquels la condition est vraie, ici les multiples de 3, sont placés dans la liste.
{{< /solution >}}

{{< question >}}
Écrire une liste en compréhension qui donne :

1. les 10 premiers multiples de 7 : `[7, 14, 21, ..., 70]` ;
1. les notes de la liste `notes = [12, 15, 8, 14, 6, 17]` qui sont inférieures à 10 ;
1. la liste `[True, False, True, False, True, False]` qui indique, pour chaque entier de 0 à 5, s'il est pair.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> [7 * k for k in range(1, 11)]
[7, 14, 21, 28, 35, 42, 49, 56, 63, 70]
>>> [n for n in notes if n < 10]
[8, 6]
>>> [k % 2 == 0 for k in range(6)]
[True, False, True, False, True, False]
```
{{< /solution >}}

{{< note success "À retenir" >}}
On peut construire une liste :

- de taille fixée, avec `[valeur] * n`, puis la remplir par indice ;
- **en compréhension**, avec `[expression for element in iterable]`. On peut ajouter un filtre : `[expression for element in iterable if condition]`.
{{< /note >}}

{{< qcm >}}
- question: 'Que vaut `[0] * 4` ?'
  reponses:
    - '`[0, 0, 0, 0]`'
    - '`[0]`'
    - '`0`'
  bonne: 1
  explication: 'On obtient une liste de 4 éléments, tous égaux à 0, qu''on peut ensuite remplir par indice.'
- question: 'Que vaut `[2 * k + 1 for k in range(4)]` ?'
  reponses:
    - '`[1, 3, 5, 7]`'
    - '`[3, 5, 7, 9]`'
    - '`[1, 3, 5, 7, 9]`'
  bonne: 1
  explication: '`k` prend les valeurs 0, 1, 2 et 3.'
- question: 'Avec `notes = [12, 15, 8, 14, 6]`, que vaut `[n for n in notes if n >= 12]` ?'
  reponses:
    - '`[12, 15, 14]`'
    - '`[15, 14]`'
    - '`[True, True, False, True, False]`'
  bonne: 1
  explication: 'Le filtre `if` ne garde que les éléments pour lesquels la condition est vraie.'
{{< /qcm >}}

## Une liste, plusieurs noms

### Une surprise

{{< question >}}
Saisir les instructions suivantes dans la console, en prévoyant le résultat de la dernière ligne avant de la valider :

```python
>>> n = [12, 18, 9]
>>> m = n
>>> m[0] = 0
>>> n
```

Le résultat est-il celui que vous attendiez ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> n
[0, 18, 9]
```
On a modifié `m`, et pourtant `n` a changé.
{{< /solution >}}

Ce résultat surprend presque tout le monde la première fois. Pour le comprendre, il faut revenir à ce que fait vraiment une affectation (Doc. 2,2) : une variable **référence** une valeur. Elle ne contient pas la liste, elle indique où elle se trouve, un peu comme une étiquette collée dessus.

L'instruction `m = n` ne fabrique donc pas une deuxième liste. Elle colle une deuxième étiquette, `m`, sur la **même** liste :

{{< columns >}}
`n` $\rightarrow$
{{< column >}}
$arrow.l$ `m`
{{< endcolumns >}}

Quand on écrit `m[0] = 0`, on modifie cette liste unique. En la regardant par l'étiquette `n`, on voit forcément la modification. On dit que `m` et `n` sont des **alias**.

Avec les nombres et les tuples, ce phénomène existe aussi, mais il ne se voit jamais : comme on ne peut pas modifier un nombre ou un tuple, on ne peut pas constater que deux étiquettes désignent le même objet. C'est la mutabilité des listes qui le rend visible.

{{< question >}}
Pour obtenir une vraie copie, on peut construire une nouvelle liste en compréhension. Prévoir puis vérifier le contenu de `n` et de `c` :

```python
>>> n = [12, 18, 9]
>>> c = [x for x in n]
>>> c[0] = 0
>>> n
>>> c
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> n
[12, 18, 9]
>>> c
[0, 18, 9]
```
La compréhension a fabriqué une nouvelle liste, avec les mêmes éléments. `c` et `n` référencent maintenant deux listes différentes : modifier l'une ne change pas l'autre.
{{< /solution >}}

### Une fonction peut modifier la liste qu'on lui donne

Lors d'un appel, le paramètre reçoit la valeur de l'argument, exactement comme dans une affectation. Si l'argument est une liste, le paramètre devient donc un alias de cette liste.

{{< question >}}
Recopier les deux fonctions suivantes dans l'éditeur :

```python
def reinitialiser_1(notes: list[float]) -> None:
    notes = [0] * len(notes)

def reinitialiser_2(notes: list[float]) -> None:
    for i in range(len(notes)):
        notes[i] = 0
```

Prévoir, puis vérifier, le contenu de `releve` après chaque appel :

```python
>>> releve = [12, 15, 9, 14]
>>> reinitialiser_1(releve)
>>> releve
>>> reinitialiser_2(releve)
>>> releve
```

Expliquer la différence de comportement entre les deux fonctions.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> reinitialiser_1(releve)
>>> releve
[12, 15, 9, 14]
>>> reinitialiser_2(releve)
>>> releve
[0, 0, 0, 0]
```
Au début de chaque appel, le paramètre `notes` et la variable `releve` référencent la même liste.

Dans `reinitialiser_1`, l'instruction `notes = [0] * len(notes)` fabrique une **nouvelle** liste et y colle l'étiquette `notes`. La liste de départ n'est pas touchée. C'est ce qu'on a vu dans le Doc. 2,6 : modifier un paramètre ne modifie pas la variable passée en argument.

Dans `reinitialiser_2`, l'instruction `notes[i] = 0` ne change pas l'étiquette : elle modifie la liste elle-même. Or c'est la même liste que `releve`.
{{< /solution >}}

{{< note warning "Effet de bord" >}}
Une fonction qui modifie une liste reçue en argument agit sur la liste du programme appelant. On parle d'**effet de bord**. C'est parfois ce qu'on veut, mais il faut alors l'annoncer clairement dans la documentation de la fonction. Si on ne le veut pas, la fonction doit travailler sur une copie, ou construire et retourner une nouvelle liste.
{{< /note >}}

{{< note success "À retenir" >}}
Après `m = n`, les variables `m` et `n` référencent la **même** liste : ce sont des **alias**. Toute modification faite par l'une est visible par l'autre.

Pour obtenir une copie indépendante, on construit une nouvelle liste, par exemple `[x for x in n]`.

Une fonction qui reçoit une liste peut la modifier (effet de bord) avec `t[i] = ...`. En revanche, une nouvelle affectation du paramètre (`t = ...`) ne change pas la liste de l'appelant.
{{< /note >}}

{{< qcm >}}
- question: 'Après `n = [12, 18, 9]`, `m = n` puis `m[0] = 0`, que vaut `n` ?'
  reponses:
    - '`[0, 18, 9]`'
    - '`[12, 18, 9]`'
  bonne: 1
  explication: '`m` et `n` référencent la même liste : ce sont des alias.'
- question: 'Après `n = [12, 18, 9]`, `c = [x for x in n]` puis `c[0] = 0`, que vaut `n` ?'
  reponses:
    - '`[12, 18, 9]`'
    - '`[0, 18, 9]`'
  bonne: 1
  explication: 'La compréhension fabrique une nouvelle liste : `c` est une copie indépendante.'
- question: 'Laquelle de ces fonctions modifie la liste reçue en argument ?'
  reponses:
    - '`def f(t): t[0] = 0`'
    - '`def f(t): t = [0] * len(t)`'
  bonne: 1
  explication: '`t[0] = 0` modifie la liste partagée avec l''appelant : c''est un effet de bord. La nouvelle affectation `t = ...` fait seulement référencer une autre liste au paramètre.'
{{< /qcm >}}

## Des listes de listes

Les éléments d'une liste peuvent eux-mêmes être des listes. C'est ainsi qu'on représente des valeurs rangées en lignes et en colonnes, comme les cases d'une grille de jeu. En mathématiques, des nombres rangés de cette façon forment une **matrice**.

```python
m = [[1, 2, 3],
     [4, 5, 6]]
```

`m` est une liste de deux éléments : `m[0]` est la liste `[1, 2, 3]`, qu'on voit comme la première ligne, et `m[1]` est la liste `[4, 5, 6]`. Pour atteindre un nombre, on applique deux indices l'un après l'autre : `m[1]` donne la ligne d'indice 1, puis `m[1][2]` donne l'élément d'indice 2 de cette ligne.

{{< question >}}
Avec la liste `m` ci-dessus, prévoir puis vérifier :

```python
>>> m[0]
>>> m[1][2]
>>> len(m)
>>> len(m[0])
>>> m[0][1] = 0
>>> m
```

Que représentent `len(m)` et `len(m[0])` pour la matrice ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> m[0]
[1, 2, 3]
>>> m[1][2]
6
>>> len(m)
2
>>> len(m[0])
3
>>> m[0][1] = 0
>>> m
[[1, 0, 3], [4, 5, 6]]
```
`len(m)` est le nombre de lignes de la matrice, `len(m[0])` le nombre d'éléments d'une ligne, c'est-à-dire le nombre de colonnes.
{{< /solution >}}

{{< question >}}
Écrire la fonction `somme_matrice` dont la spécification est :

```python
def somme_matrice(m: list[list[int]]) -> int:
    """Retourne la somme de tous les éléments de la matrice m.

    >>> somme_matrice([[1, 2, 3], [4, 5, 6]])
    21
    """
```

**Indication.** Utiliser deux boucles imbriquées : l'une parcourt les indices des lignes, l'autre ceux des colonnes.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def somme_matrice(m: list[list[int]]) -> int:
    """Retourne la somme de tous les éléments de la matrice m."""
    total = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            total += m[i][j]
    return total
```
{{< /solution >}}

{{< question >}}
Dans le Doc. 2,4, la fonction `table_multiplication` retournait une chaîne de caractères. On veut maintenant une matrice, pour pouvoir retrouver chaque produit par ses indices. Écrire la fonction `table_multiplication` dont la spécification est :

```python
def table_multiplication(n: int) -> list[list[int]]:
    """Retourne la table de multiplication des entiers de 1 à n,
    sous forme d'une matrice de n lignes et n colonnes.

    >>> table_multiplication(4)
    [[1, 2, 3, 4], [2, 4, 6, 8], [3, 6, 9, 12], [4, 8, 12, 16]]
    """
```

**Indication.** Une ligne de la table est une liste en compréhension. La table entière est une liste de lignes, elle aussi en compréhension.

Avec `t = table_multiplication(10)`, que vaut `t[6][7]` ? Quel produit cet élément représente-t-il ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def table_multiplication(n: int) -> list[list[int]]:
    """Retourne la table de multiplication des entiers de 1 à n,
    sous forme d'une matrice de n lignes et n colonnes.
    """
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
```
`t[6][7]` vaut `56`. Les indices commencent à 0 alors que la table commence à 1 : l'indice 6 correspond au nombre 7, l'indice 7 au nombre 8. Il s'agit donc du produit $7 \times 8$.
{{< /solution >}}

{{< note warning "Un piège classique" >}}
Pour fabriquer une grille de 3 lignes et 3 colonnes remplie de zéros, l'écriture `[[0] * 3] * 3` semble naturelle. Pourtant :

```python
>>> g = [[0] * 3] * 3
>>> g[0][0] = 5
>>> g
[[5, 0, 0], [5, 0, 0], [5, 0, 0]]
```

Le `* 3` extérieur ne fabrique pas trois lignes : il place trois fois **la même** ligne dans la liste. Les trois lignes sont des alias. La bonne écriture fabrique une nouvelle ligne à chaque tour :

```python
>>> g = [[0] * 3 for i in range(3)]
```
{{< /note >}}

{{< note success "À retenir" >}}
Une liste de listes permet de représenter une **matrice**, c'est-à-dire des valeurs rangées en lignes et en colonnes. `m[i]` est la ligne d'indice `i`, et `m[i][j]` l'élément de la ligne `i` et de la colonne `j`.

`len(m)` donne le nombre de lignes et `len(m[0])` le nombre de colonnes. On parcourt une matrice avec deux boucles imbriquées.
{{< /note >}}

{{< qcm >}}
- question: 'Avec `m = [[1, 2, 3], [4, 5, 6]]`, que vaut `m[1][0]` ?'
  reponses:
    - '`4`'
    - '`2`'
    - '`[4, 5, 6]`'
  bonne: 1
  explication: '`m[1]` est la ligne `[4, 5, 6]`, et l''élément d''indice 0 de cette ligne vaut 4.'
- question: 'Avec la même matrice `m`, que valent `len(m)` et `len(m[0])` ?'
  reponses:
    - '`2` et `3`'
    - '`3` et `2`'
    - '`6` et `3`'
  bonne: 1
  explication: '`len(m)` est le nombre de lignes, `len(m[0])` le nombre de colonnes.'
- question: 'Après `g = [[0] * 2] * 2` puis `g[0][0] = 5`, que vaut `g` ?'
  reponses:
    - '`[[5, 0], [5, 0]]`'
    - '`[[5, 0], [0, 0]]`'
  bonne: 1
  explication: 'Le `* 2` extérieur place deux fois **la même** ligne dans la liste. Il faut écrire `[[0] * 2 for i in range(2)]`.'
{{< /qcm >}}

## Exercices de synthèse

{{< note warning "Consigne" >}}
Écrire chaque fonction dans la partie principale de l'éditeur, avec sa spécification complète (signature et documentation). Tester ensuite chacun des exemples de la documentation dans la console. Les fonctions `sum`, `min`, `max` et la méthode `index` de Python ne doivent pas être utilisées.
{{< /note >}}

{{< question >}}
**Moyenne.** Écrire la fonction `moyenne` dont la spécification est :

```python
def moyenne(notes: list[float]) -> float:
    """Retourne la moyenne des éléments de notes, qui ne doit pas être vide.

    >>> moyenne([12, 15, 9, 14])
    12.5
    """
```

Vérifier la précondition à l'aide d'une assertion (voir Doc. 3,1).
{{< /question >}}

{{< solution "Réponse" >}}
```python
def moyenne(notes: list[float]) -> float:
    """Retourne la moyenne des éléments de notes, qui ne doit pas être vide."""
    assert len(notes) > 0, "la liste ne doit pas être vide"
    total = 0
    for note in notes:
        total += note
    return total / len(notes)
```
Sans l'assertion, une liste vide provoquerait une division par zéro.
{{< /solution >}}

{{< question >}}
**Recherche d'une valeur.** Écrire la fonction `indice` dont la spécification est :

```python
def indice(valeurs: list[int], cherchee: int) -> int:
    """Retourne l'indice de la première occurrence de cherchee dans
    valeurs, ou -1 si cherchee n'est pas dans valeurs.

    >>> indice([4, 8, 15, 16, 23, 42], 16)
    3
    >>> indice([4, 8, 15, 16, 23, 42], 7)
    -1
    >>> indice([5, 3, 5], 5)
    0
    """
```

Dans le pire des cas, combien de comparaisons la fonction effectue-t-elle pour une liste de 1000 éléments ? Et pour une liste deux fois plus longue ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def indice(valeurs: list[int], cherchee: int) -> int:
    """Retourne l'indice de la première occurrence de cherchee dans
    valeurs, ou -1 si cherchee n'est pas dans valeurs.
    """
    for i in range(len(valeurs)):
        if valeurs[i] == cherchee:
            return i
    return -1
```
Le `return i` arrête la fonction dès que la valeur est trouvée. Le pire des cas est celui où la valeur est absente : il faut alors la comparer à tous les éléments, soit 1000 comparaisons, et 2000 pour une liste deux fois plus longue. Le nombre de comparaisons est proportionnel à la longueur de la liste.
{{< /solution >}}

{{< question >}}
**Statistiques d'un devoir.** On veut écrire la fonction `statistiques` dont la spécification est :

```python
def statistiques(notes: list[float]) -> tuple[float, int, int, int]:
    """Retourne un tuple (m, bas, milieu, haut) où m est la moyenne
    des notes, bas le nombre de notes strictement inférieures à m - 3,
    milieu le nombre de notes comprises entre m - 3 et m + 3 (bornes
    incluses), haut le nombre de notes strictement supérieures à m + 3.

    >>> statistiques([12, 15, 8, 14, 6, 17])
    (12.0, 2, 3, 1)
    >>> statistiques([10, 7, 13])
    (10.0, 0, 3, 0)
    """
```

1. Vérifier à la main le premier exemple de la documentation.
1. Écrire la fonction, en utilisant la fonction `moyenne` de la question précédente.
1. Un élève propose de compter les notes de chaque groupe avec une fonction qui compte les valeurs comprises dans un intervalle $[a ; b]$, bornes incluses, appelée trois fois : sur $[0 ; m - 3]$, sur $[m - 3 ; m + 3]$ et sur $[m + 3 ; 20]$. Le deuxième exemple de la documentation montre pourquoi cette idée donne un résultat faux. Expliquer.
{{< /question >}}

{{< solution "Réponse" >}}
1. La somme des notes vaut $12 + 15 + 8 + 14 + 6 + 17 = 72$ et il y a 6 notes : $m = 72 / 6 = 12$. On a donc $m - 3 = 9$ et $m + 3 = 15$. Notes inférieures à 9 : 8 et 6, soit 2 notes. Notes entre 9 et 15 : 12, 15 et 14, soit 3 notes. Notes supérieures à 15 : 17, soit 1 note. On retrouve bien `(12.0, 2, 3, 1)`.

1. On parcourt la liste une seule fois, et on range chaque note dans un seul groupe :

```python
def statistiques(notes: list[float]) -> tuple[float, int, int, int]:
    """Retourne un tuple (m, bas, milieu, haut) où m est la moyenne
    des notes, bas le nombre de notes strictement inférieures à m - 3,
    milieu le nombre de notes comprises entre m - 3 et m + 3 (bornes
    incluses), haut le nombre de notes strictement supérieures à m + 3.
    """
    m = moyenne(notes)
    bas, milieu, haut = 0, 0, 0
    for note in notes:
        if note < m - 3:
            bas += 1
        elif note <= m + 3:
            milieu += 1
        else:
            haut += 1
    return m, bas, milieu, haut
```

3. Dans le deuxième exemple, $m = 10$. La note 7 est égale à $m - 3$ : elle appartient à la fois à $[0 ; 7]$ et à $[7 ; 13]$, elle serait donc comptée deux fois. De même pour la note 13. On obtiendrait 5 notes comptées alors qu'il n'y en a que 3. Avec la structure `if` / `elif` / `else`, chaque note entre dans un seul bloc.
{{< /solution >}}

{{< question >}}
**Tirage du Loto sans répétition.** Dans le Doc. 2,4, la fonction `loto_naif` pouvait tirer deux fois le même numéro, faute de pouvoir mémoriser les numéros déjà sortis. Une liste résout ce problème. Écrire la fonction `loto` dont la spécification est :

```python
def loto() -> list[int]:
    """Retourne une liste de 6 entiers différents, tirés au hasard
    entre 1 et 49 (bornes incluses).
    """
```

**Indication.** Partir de la liste `[0] * 6`. Tirer un numéro avec `random.randint(1, 49)`. S'il n'est pas déjà dans la liste, le ranger à la première place libre. Le nombre de tirages nécessaires n'est pas connu à l'avance : quelle boucle faut-il utiliser ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
import random

def loto() -> list[int]:
    """Retourne une liste de 6 entiers différents, tirés au hasard
    entre 1 et 49 (bornes incluses).
    """
    nbre_boules = 6
    tirage = [0] * nbre_boules
    nbre_tirees = 0
    while nbre_tirees < nbre_boules:
        boule = random.randint(1, 49)
        if boule not in tirage:
            tirage[nbre_tirees] = boule
            nbre_tirees += 1
    return tirage
```
Quand un numéro déjà sorti est tiré à nouveau, il est rejeté et on recommence. On ne sait donc pas combien de tirages il faudra : la boucle `while` s'impose. La variable `nbre_tirees` donne à la fois le nombre de numéros déjà rangés et l'indice de la première place libre. Les zéros de départ ne gênent pas le test `boule not in tirage`, puisque 0 n'est jamais tiré.
{{< /solution >}}

### Pour aller plus loin

{{< question >}}
**Transposée d'une matrice.** La transposée d'une matrice s'obtient en échangeant ses lignes et ses colonnes : la première ligne devient la première colonne, et ainsi de suite. Écrire, en une seule ligne de code, la fonction `transposee` dont la spécification est :

```python
def transposee(m: list[list[int]]) -> list[list[int]]:
    """Retourne la transposée de la matrice m.

    >>> transposee([[1, 2, 3], [4, 5, 6]])
    [[1, 4], [2, 5], [3, 6]]
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def transposee(m: list[list[int]]) -> list[list[int]]:
    """Retourne la transposée de la matrice m."""
    return [[m[i][j] for i in range(len(m))] for j in range(len(m[0]))]
```
La ligne d'indice `j` de la transposée contient les éléments de la colonne d'indice `j` de `m`, pris ligne après ligne.
{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- expliquer la différence entre une liste, mutable, et un tuple, non mutable ;
- lire et modifier un élément d'une liste grâce à son indice ;
- parcourir une liste par ses éléments pour la lire, et par ses indices pour la modifier ;
- construire une liste de taille fixée avec `[valeur] * n` ;
- construire une liste en compréhension, avec ou sans filtre `if` ;
- expliquer pourquoi, après `m = n`, une modification de `m` est visible dans `n`, et faire une vraie copie d'une liste ;
- prévoir si une fonction modifie la liste qu'elle reçoit en argument ;
- représenter une matrice par une liste de listes et utiliser la notation `m[i][j]` ;
- écrire un algorithme de recherche d'une valeur, de calcul d'une moyenne, sur une liste.
{{< /note >}}
