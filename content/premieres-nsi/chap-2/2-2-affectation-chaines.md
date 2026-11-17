---
title: "Opérateurs d'affectation, formatage des chaînes"
subtitle: "Doc. 2,2"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["variable", "identificateur", "affectation", "opérateur d'affectation", "chaîne de caractères", "f-string", "concaténation", "formatage"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 20
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-2/2-2/2-2-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/premieres-nsi/chap-2/2-2/2-2-corrige.pdf" >}}

{{< note goal >}}
Manipuler des variables et des chaînes de caractères dans la console Python pour découvrir comment nommer et mettre à jour une information, puis comment l'insérer proprement dans un message.
{{< /note >}}

## Comment nommer une information à l'aide d'une variable ?

{{< question >}}
Tester dans la console les instructions suivantes :

```python
>>> age = 15
>>> age
```

Puis tester chacune des instructions ci-dessous, une par une :

```python
>>> 1age = 15
>>> mon-age = 15
>>> for = 15
```

Laquelle de ces trois dernières instructions fonctionne ? Pour les autres, à quel endroit Python signale-t-il une erreur ?
{{< /question >}}

{{< solution "Réponse" >}}
Aucune des trois dernières instructions ne fonctionne : Python renvoie à chaque fois une `SyntaxError`.

- `1age = 15` : un identificateur ne peut pas commencer par un chiffre.
- `mon-age = 15` : le caractère `-` n'est pas autorisé dans un identificateur (il serait interprété comme une soustraction).
- `for = 15` : `for` est un mot réservé du langage, il ne peut pas servir d'identificateur.
{{< /solution >}}

{{< question >}}
Tester dans la console :

```python
>>> help("keywords")
```

À quoi correspond la liste affichée ? Pourquoi  est-il plus utile de retenir l'appel de la fonction `help` : `help("keywords")`, que la liste elle-même ?
{{< /question >}}

{{< solution "Réponse" >}}
Cette liste contient tous les **mots réservés** du langage Python : ils ont un rôle particulier dans la grammaire du langage (`for`, `if`, `def`, `return`, ...) et ne peuvent donc jamais être utilisés comme identificateur.

Plutôt que de mémoriser cette liste, il suffit de savoir qu'elle est consultable à tout moment avec `help("keywords")`.
{{< /solution >}}

{{< question >}}
Tester dans la console :

```python
>>> ma_variable = 1
>>> maVariable = 2
>>> ma_variable
>>> maVariable
```

Ces deux identificateurs désignent-ils la même variable ?
{{< /question >}}

{{< solution "Réponse" >}}
Non, on obtient successivement `1` puis `2` : `ma_variable` et `maVariable` sont deux variables **différentes**. Python distingue les majuscules des minuscules dans un identificateur.
{{< /solution >}}

{{< note success "À retenir" >}}
Une **variable** est repérée par un **identificateur**, qui doit respecter certaines règles :

- il commence par une lettre ou un blanc souligné (`_`) ;
- il ne peut ensuite contenir que des lettres, des chiffres ou des blancs soulignés ;
- Python distingue les majuscules des minuscules (`age` et `Age` sont deux identificateurs différents) ;
- un **mot réservé** du langage (liste consultable avec `help("keywords")`) ne peut pas être choisi comme identificateur.
{{< /note >}}

{{< qcm >}}
- question: 'Lequel de ces identificateurs est valide en Python ?'
  reponses:
    - '`1age`'
    - '`mon-age`'
    - '`mon_age`'
    - '`for`'
  bonne: 3
  explication: 'Un identificateur commence par une lettre ou `_`, puis ne contient que des lettres, des chiffres ou `_`. `1age` commence par un chiffre, `mon-age` contient un tiret (Python y voit une soustraction) et `for` est un mot réservé.'
- question: 'Après `ma_variable = 1` puis `maVariable = 2`, que vaut `ma_variable` ?'
  reponses:
    - '`1`'
    - '`2`'
    - 'Une erreur : la variable a été définie deux fois.'
  bonne: 1
  explication: '`ma_variable` et `maVariable` sont deux identificateurs différents : la seconde affectation crée une autre variable.'
- question: 'Comment obtenir la liste des mots réservés de Python, interdits comme identificateurs ?'
  reponses:
    - '`help("keywords")`'
    - '`print(keywords)`'
    - '`import keywords`'
  bonne: 1
  explication: 'Inutile de retenir la liste par cœur : `help("keywords")` l''affiche à tout moment.'
{{< /qcm >}}

## Que se passe-t-il lors d'une affectation ?

{{< question >}}
Sans utiliser Python, prévoir le résultat de l'évaluation de `a` et de `b` après ces instructions, puis tester dans la console :

```python
>>> a = 3
>>> b = a
>>> a = 5
>>> a
>>> b
```

La variable `b` a-t-elle changé de valeur lorsque `a` a été modifiée ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient `5` puis `3` : `b` garde la valeur qu'elle avait au moment de l'instruction `b = a`. Modifier `a` par la suite ne change pas `b`.
{{< /solution >}}

{{< question >}}
Prévoir le résultat de l'évaluation de `x`, `y` et `z` après ces instructions, puis tester dans la console :

```python
>>> x = y = z = 1
>>> x
>>> y
>>> z
```

Dans quel sens faut-il lire la première instruction pour comprendre ce qu'elle fait : de la gauche vers la droite, ou de la droite vers la gauche ?
{{< /question >}}

{{< solution "Réponse" >}}
Les trois variables valent `1`. Il faut lire l'instruction de la **droite vers la gauche** : on affecte `1` à `z`, puis la valeur de `z` à `y`, puis la valeur de `y` à `x`.
{{< /solution >}}

{{< question >}}
Prévoir le résultat de l'évaluation de `a`, `b` et `c` après cette instruction, puis tester dans la console :

```python
>>> a, b, c = 1, 2, 3
>>> a
>>> b
>>> c
```

Combien de valeurs sont affectées en une seule instruction ?
{{< /question >}}

{{< solution "Réponse" >}}
Trois valeurs sont affectées simultanément : `a` reçoit `1`, `b` reçoit `2` et `c` reçoit `3`.
{{< /solution >}}

{{< note success "À retenir" >}}
Une **affectation** (opérateur `=`) donne une valeur à une variable ; elle se lit toujours de la **droite vers la gauche**.

- **Affectation simple** : `a = 3`.
- **Affectation multiple** : `x = y = z = 1` affecte la même valeur à plusieurs variables.
- **Affectation groupée** : `a, b, c = 1, 2, 3` affecte plusieurs valeurs différentes en une instruction.

Python est un langage à **typage dynamique** : il n'est pas nécessaire de préciser le type d'une variable avant de lui affecter une valeur.
{{< /note >}}

{{< qcm >}}
- question: 'Après `a = 3`, `b = a`, puis `a = 5`, que vaut `b` ?'
  reponses:
    - '`3`'
    - '`5`'
    - '`a`'
  bonne: 1
  explication: '`b = a` donne à `b` la valeur de `a` à ce moment-là, soit 3. Modifier `a` ensuite ne change pas `b`.'
- question: 'Dans quel sens se lit l''instruction `x = y = z = 1` ?'
  reponses:
    - 'De la gauche vers la droite : `x` reçoit `y`, qui reçoit `z`…'
    - 'De la droite vers la gauche : `z` reçoit `1`, puis `y` reçoit la valeur de `z`, puis `x` celle de `y`.'
    - 'Elle provoque une erreur.'
  bonne: 2
  explication: 'Une affectation se lit toujours de la droite vers la gauche. Les trois variables valent finalement `1`.'
- question: 'Après `a, b, c = 1, 2, 3`, que vaut `b` ?'
  reponses:
    - '`1`'
    - '`2`'
    - '`(1, 2, 3)`'
  bonne: 2
  explication: 'C''est une affectation groupée : les valeurs sont attribuées dans l''ordre, `a` reçoit `1`, `b` reçoit `2`, `c` reçoit `3`.'
{{< /qcm >}}

## Comment mettre à jour la valeur d'une variable ?

{{< question >}}
Un article coûte 20 € hors taxe ; la TVA est de 18,6 %. Prévoir le résultat de l'évaluation de `prix` après ces instructions, puis tester dans la console :

```python
>>> prix = 20
>>> tva = 18.6
>>> prix = prix + prix * tva / 100
>>> prix
```

Que représente l'expression à droite du signe `=` dans la troisième instruction ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient `23.72`. L'expression `prix + prix * tva / 100` est évaluée avec l'**ancienne** valeur de `prix` ; le résultat est ensuite affecté à la variable `prix`, qui prend sa nouvelle valeur.
{{< /solution >}}

{{< question >}}
On suit maintenant le score d'un jeu. Prévoir le résultat de l'évaluation de `score` pour chacune des deux séquences suivantes, puis tester dans la console :

```python
>>> score = 0
>>> score = score + 10
>>> score
```

```python
>>> score = 0
>>> score += 10
>>> score
```

Que remarquez-vous ?
{{< /question >}}

{{< solution "Réponse" >}}
Les deux séquences donnent `10` : `score += 10` est un raccourci d'écriture pour `score = score + 10`.
{{< /solution >}}

{{< question >}}
Par analogie avec `+=`, prévoir le résultat de l'évaluation de `x` après chacune des instructions suivantes, puis tester dans la console :

```python
>>> x = 10
>>> x -= 3
>>> x
>>> x *= 2
>>> x
>>> x //= 5
>>> x
>>> x %= 2
>>> x
```

Pour chaque opérateur d'affectation utilisé, réécrire l'instruction équivalente utilisant `=` et l'opérateur arithmétique correspondant.
{{< /question >}}

{{< solution "Réponse" >}}
| **Instruction** | **Équivalent** | **Valeur de `x`** |
|:---|:---|:---|
| `x = 10` |  | `10` |
| `x -= 3` | `x = x - 3` | `7` |
| `x *= 2` | `x = x * 2` | `14` |
| `x //= 5` | `x = x // 5` | `2` |
| `x %= 2` | `x = x % 2` | `0` |
{{< /solution >}}

{{< note success "À retenir" >}}
Un **opérateur d'affectation** met à jour la valeur d'une variable à partir de sa propre valeur, en une seule écriture (à lire de la droite vers la gauche) :

| **Opérateur** | **Équivalent** |
|:---|:---|
| `+=` | `variable = variable + expression` |
| `-=` | `variable = variable - expression` |
| `*=` | `variable = variable * expression` |
| `/=` | `variable = variable / expression` |
| `//=` | `variable = variable // expression` |
| `%=` | `variable = variable % expression` |
{{< /note >}}

### Peut-on échanger les valeurs de deux variables ?

{{< question >}}
Dans la partie principale de l'éditeur Thonny, écrire :

```python
a = 605
b = 506
a = b
b = a
print(a, b)
```

Lancer le programme en mode **débogage** puis utiliser la touche <kbd>F7</kbd>.

Ce programme permute-t-il bien les valeurs de `a` et `b` ? Compléter le tableau d'état ci-dessous.

| **Instruction** | **a** | **b** |
|:---|:---|:---|
| `a = 605` |  |  |
| `b = 506` |  |  |
| `a = b` |  |  |
| `b = a` |  |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **Instruction** | **a** | **b** |
|:---|:---|:---|
| `a = 605` | 605 |  |
| `b = 506` | 605 | 506 |
| `a = b` | 506 | 506 |
| `b = a` | 506 | 506 |

Non : au moment où `b = a` est exécutée, `a` a déjà perdu sa valeur initiale. Les deux variables valent finalement `506` : la permutation a échoué.
{{< /solution >}}

{{< question >}}
**Essentiel pour l'épreuve écrite.** Sans utiliser Python, compléter le tableau d'état ci-dessous en suivant, ligne par ligne, l'exécution de la séquence d'instructions suivante (la colonne `c` reste vide tant que cette variable n'existe pas encore). Vérifier ensuite en testant la séquence dans la console.

```python
>>> a = 7
>>> b = 4
>>> b = a + b
>>> a = b - a
>>> c = a * b
>>> a += c
>>> b -= 1
```

| **Instruction** | **a** | **b** | **c** |
|:---|:---|:---|:---|
| `a = 7` |  |  |  |
| `b = 4` |  |  |  |
| `b = a + b` |  |  |  |
| `a = b - a` |  |  |  |
| `c = a * b` |  |  |  |
| `a += c` |  |  |  |
| `b -= 1` |  |  |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **Instruction** | **a** | **b** | **c** |
|:---|:---|:---|:---|
| `a = 7` | 7 |  |  |
| `b = 4` | 7 | 4 |  |
| `b = a + b` | 7 | 11 |  |
| `a = b - a` | 4 | 11 |  |
| `c = a * b` | 4 | 11 | 44 |
| `a += c` | 48 | 11 | 44 |
| `b -= 1` | 48 | 10 | 44 |

On obtient finalement `a = 48`, `b = 10` et `c = 44`. Chaque instruction utilise les valeurs des variables **telles qu'elles sont juste avant son exécution** : par exemple, dans `a = b - a`, c'est l'**ancienne** valeur de `a` (`7`) qui est utilisée, pas la nouvelle.
{{< /solution >}}

{{< question >}}
Corriger le programme précédent, dans la partie principale de l'éditeur, en utilisant **une** variable supplémentaire nommée `tmp`, de façon à obtenir `a = 506` et `b = 605` après exécution.
{{< /question >}}

{{< solution "Réponse" >}}
```python
a = 605
b = 506
tmp = a
a = b
b = tmp
print(a, b)
```
{{< /solution >}}

{{< question >}}
**Plus difficile.** En utilisant uniquement les opérateurs `+=` et `-=`, permuter dans la partie principale de l'éditeur les valeurs de `a` et `b` **sans utiliser aucune variable supplémentaire**. Lancer le programme en mode débogage (<kbd>F7</kbd>) pour vérifier votre proposition en complétant le tableau d'état ci-dessous, avec `a = 605` et `b = 506`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
a = 605
b = 506
a += b   # a = 1111
b = a - b   # b = 605
a -= b   # a = 506
print(a, b)
```

| **Instruction** | **a** | **b** |
|:---|:---|:---|
| initialement | 605 | 506 |
| `a += b` | 1111 | 506 |
| `b = a - b` | 1111 | 605 |
| `a -= b` | 506 | 605 |
{{< /solution >}}

{{< qcm >}}
- question: 'Après `x = 10`, puis `x -= 3`, puis `x *= 2`, que vaut `x` ?'
  reponses:
    - '`14`'
    - '`4`'
    - '`7`'
    - '`17`'
  bonne: 1
  explication: '`x -= 3` équivaut à `x = x - 3` (x vaut 7), puis `x *= 2` équivaut à `x = x * 2` (x vaut 14).'
- question: 'Le programme `a = 605`, `b = 506`, `a = b`, `b = a` échange-t-il les valeurs de `a` et `b` ?'
  reponses:
    - 'Oui : à la fin, `a` vaut 506 et `b` vaut 605.'
    - 'Non : à la fin, `a` et `b` valent toutes les deux 506.'
    - 'Non : à la fin, `a` et `b` valent toutes les deux 605.'
  bonne: 2
  explication: 'Après `a = b`, l''ancienne valeur de `a` (605) est perdue : `b = a` recopie donc 506. Pour échanger, il faut d''abord sauvegarder la valeur dans une variable supplémentaire (`tmp = a`).'
- question: 'Après `prix = 20`, puis `prix = prix + prix * 10 / 100`, que vaut `prix` ?'
  reponses:
    - '`22.0`'
    - '`20`'
    - 'Une erreur : `prix` apparaît des deux côtés du `=`.'
  bonne: 1
  explication: 'Python évalue d''abord la partie droite avec l''ancienne valeur de `prix` (20), ce qui donne `22.0`, puis affecte ce résultat à `prix`.'
{{< /qcm >}}

## Comment insérer une valeur dans une chaîne de caractères ?

{{< question >}}
Tester dans la console :

```python
>>> type("abcd")
>>> type('abcd')
>>> type("Python, c'est top !")
>>> type('Python, c'est top !')
```

L'une de ces quatre instructions provoque une erreur. Laquelle, et pourquoi ?
{{< /question >}}

{{< solution "Réponse" >}}
La quatrième instruction, `type('Python, c'est top !')`, provoque une `SyntaxError` : l'apostrophe de `c'est` referme prématurément la chaîne ouverte par `'`. En délimitant la chaîne avec des guillemets doubles `"`, l'apostrophe ne pose plus de problème.
{{< /solution >}}

{{< question >}}
Prévoir le résultat de l'évaluation de chacune des expressions suivantes, puis tester dans la console :

```python
>>> prenom = "Alice"
>>> "Bonjour " + prenom
>>> age = 15
>>> "Tu as " + age + " ans"
```

L'une de ces deux dernières instructions échoue. Laquelle, et que dit le message d'erreur ?
{{< /question >}}

{{< solution "Réponse" >}}
La seconde échoue avec `TypeError: can only concatenate str (not "int") to str` : l'opérateur `+` entre chaînes de caractères exige que **les deux opérandes** soient des `str` ; il ne convertit pas automatiquement un entier en texte.
{{< /solution >}}

{{< question >}}
Python propose une écriture appelée **f-string** pour éviter ce problème. Prévoir le résultat de l'évaluation de chacune des expressions suivantes, puis tester dans la console :

```python
>>> prenom = "Alice"
>>> age = 15
>>> f"Bonjour {prenom}, tu as {age} ans."
>>> f"L'année prochaine, tu auras {age + 1} ans."
```

Que remarquez-vous sur le contenu des accolades `{}` dans la seconde instruction ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient `'Bonjour Alice, tu as 15 ans.'` puis `"L'année prochaine, tu auras 16 ans."`.

Le contenu des accolades n'est pas limité au nom d'une variable : c'est une **expression**, que Python évalue avant de l'insérer (après conversion automatique) dans le texte.
{{< /solution >}}

{{< note idea "f-string" >}}
Une **f-string** s'écrit `f"..."` : la lettre `f` juste avant les guillemets indique à Python de rechercher des accolades `{}` dans le texte. Chaque expression entre accolades est **évaluée**, convertie en `str`, puis insérée à cet endroit.
{{< /note >}}

{{< question >}}
On souhaite afficher un prix avec exactement deux chiffres après la virgule. Prévoir le résultat de l'évaluation de chacune des expressions suivantes, puis tester dans la console :

```python
>>> montant = 3333.3333
>>> f"{montant:.0f} €"
>>> f"{montant:.1f} €"
>>> f"{montant:.2f} €"
```

À quoi correspond le nombre placé juste avant la lettre `f`, après les deux points `:` ?
{{< /question >}}

{{< solution "Réponse" >}}
On obtient successivement `'3333 €'`, `'3333.3 €'` puis `'3333.33 €'`. Le nombre précédant le `f` indique le **nombre de chiffres affichés après la virgule** ; la valeur est arrondie en conséquence.
{{< /solution >}}

{{< question >}}
La méthode `.format()`, plus ancienne, permet d'obtenir le même résultat et se rencontre encore dans d'anciens programmes. Prévoir le résultat de l'évaluation de chacune des expressions suivantes, puis tester dans la console :

```python
>>> prenom = "Alice"
>>> age = 15
>>> "Bonjour {}, tu as {} ans.".format(prenom, age)
>>> f"Bonjour {prenom}, tu as {age} ans."
```

Ces deux instructions produisent-elles le même résultat ?
{{< /question >}}

{{< solution "Réponse" >}}
Oui, les deux instructions donnent `'Bonjour Alice, tu as 15 ans.'`. La f-string est toutefois plus lisible, car la variable apparaît directement dans le texte plutôt que dans une liste d'arguments séparée.
{{< /solution >}}

{{< note success "À retenir" >}}
Pour insérer une valeur dans un texte, on préfère une **f-string** :

`f"...{expression}...{expression:.Nf}..."`

- `{expression}` insère le résultat de l'évaluation de l'expression, converti en `str` ;
- `{expression:.Nf}` affiche un nombre flottant arrondi à `N` chiffres après la virgule ;
- la méthode `"...{}...".format(...)`, plus ancienne, produit le même résultat mais reste moins lisible.
{{< /note >}}

### Exercices de synthèse

{{< note warning "Consigne" >}}
Écrire chaque fonction dans la partie principale de l'éditeur, en respectant sa spécification et en utilisant une f-string pour construire le message retourné. Tester ensuite son appel dans la console.
{{< /note >}}

{{< question >}}
Écrire la fonction `conversion_franc_euro` dont la spécification est :

```python
def conversion_franc_euro(francs: float) -> str:
    """Conversion d'une somme en francs en euros.
    Le message retourné donne les deux valeurs.

    >>> conversion_franc_euro(100)
    '100 francs correspondent à 15.24 euros.'
    """
```

Le franc était la monnaie utilisée en France avant l'euro (jusqu'en 2002) ; 1 euro correspond à 6,55957 francs. Le montant en euros sera affiché avec deux chiffres après la virgule.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def conversion_franc_euro(francs: float) -> str:
    """Conversion d'une somme en francs en euros.
    Le message retourné donne les deux valeurs.

    >>> conversion_franc_euro(100)
    '100 francs correspondent à 15.24 euros.'
    """
    change = 6.55957
    euros = francs / change
    return f"{francs} francs correspondent à {euros:.2f} euros."
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `salutation` dont la spécification est :

```python
def salutation(nom: str, prenom: str, naissance: int) -> str:
    """À partir des nom, prénom et date de naissance, retourne un
    message d'accueil indiquant l'âge de la personne en 2026.

    >>> salutation("Dupond", "Patrick", 1961)
    'Bonjour Patrick Dupond, vous avez 65 ans.'
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def salutation(nom: str, prenom: str, naissance: int) -> str:
    """À partir des nom, prénom et date de naissance, retourne un
    message d'accueil indiquant l'âge de la personne en 2026.

    >>> salutation("Dupond", "Patrick", 1961)
    'Bonjour Patrick Dupond, vous avez 65 ans.'
    """
    annee_en_cours = 2026
    age = annee_en_cours - naissance
    return f"Bonjour {prenom} {nom}, vous avez {age} ans."
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `age_aleatoire` dont la spécification est :

```python
def age_aleatoire(age_min: int, age_max: int) -> str:
    """À partir de deux ages limites, retourne un message contenant
    un age déterminé aléatoirement entre age_min et age_max inclus.

    >>> age_aleatoire(20, 100)
    'Votre age est : 85 ans !'
    """
```
**Remarque :** utiliser la fonction `randint` du module `random` pour déterminer aléatoirement un nombre.
{{< /question >}}

{{< solution "Réponse" >}}
```python
import random

def age_aleatoire(age_min: int, age_max: int) -> str:
    """À partir de deux ages limites, retourne un message contenant
    un age déterminé aléatoirement entre age_min et age_max inclus.

    >>> age_aleatoire(20, 100)
    'Votre age est : 85 ans !'
    """
    age = random.randint(age_min, age_max)
    return f"Votre age est : {age} ans !"
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `ticket` qui réutilise le principe de la section précédente (prix hors taxe et TVA), et dont la spécification est :

```python
def ticket(article: str, prix_ht: float, tva: float) -> str:
    """Retourne une ligne de ticket de caisse donnant le nom de
    l'article et son prix TTC, arrondi à deux chiffres après la
    virgule.

    >>> ticket("Cahier", 2.5, 5.5)
    'Cahier : 2.64 €'
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def ticket(article: str, prix_ht: float, tva: float) -> str:
    """Retourne une ligne de ticket de caisse donnant le nom de
    l'article et son prix TTC, arrondi à deux chiffres après la
    virgule.

    >>> ticket("Cahier", 2.5, 5.5)
    'Cahier : 2.64 €'
    """
    prix_ttc = prix_ht + prix_ht * tva / 100
    return f"{article} : {prix_ttc:.2f} €"
```
{{< /solution >}}

### Exercices de synthèse (Doc. 2,1 et Doc. 2,2)

**Consigne :** réinvestir les fonctions du Doc. 2,1 (spécification, module `math`) avec les notions du Doc. 2,2 (opérateur d'affectation, f-string). Écrire chaque fonction dans la partie principale de l'éditeur, puis tester son appel dans la console.

{{< question >}}
Écrire la fonction `prix_ttc` dont la spécification est :

```python
def prix_ttc(prix_ht: float, tva: float) -> float:
    """Retourne le prix TTC d'un article, à partir de son prix HT
    et du taux de TVA en pourcentage.

    >>> prix_ttc(20, 18.6)
    23.72
    """
```

Dans la partie principale de l'éditeur, à la suite de cette fonction, calculer le montant total TTC d'un panier contenant trois articles de prix HT 12 €, 8 € et 25 € (TVA à 20 % pour chacun), en partant de `total = 0` et en ajoutant chaque article avec l'opérateur `+=`. Afficher enfin, avec une f-string affichée par `print`, un message de la forme `Total du panier : 54.00 €`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def prix_ttc(prix_ht: float, tva: float) -> float:
    """Retourne le prix TTC d'un article, à partir de son prix HT
    et du taux de TVA en pourcentage.

    >>> prix_ttc(20, 18.6)
    23.72
    """
    return prix_ht + prix_ht * tva / 100

total = 0
total += prix_ttc(12, 20)
total += prix_ttc(8, 20)
total += prix_ttc(25, 20)
print(f"Total du panier : {total:.2f} €")
```
{{< /solution >}}

{{< question >}}
On reprend la fonction `distance` du Doc. 2,1 (à recopier dans la partie principale de l'éditeur si nécessaire) :

```python
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Retourne la distance entre deux points du plan."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
```

Écrire, à la suite, la fonction `message_distance` dont la spécification est :

```python
def message_distance(x1: float, y1: float, x2: float, y2: float) -> str:
    """Retourne un message donnant la distance entre les points
    (x1, y1) et (x2, y2), arrondie à deux chiffres après la virgule.

    >>> message_distance(0, 0, 3, 4)
    'La distance entre les deux points est de 5.00 unités.'
    """
```

La fonction `message_distance` doit utiliser la fonction `distance`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def message_distance(x1: float, y1: float,
                      x2: float, y2: float) -> str:
    """Retourne un message donnant la distance entre les points
    (x1, y1) et (x2, y2), arrondie à deux chiffres après la virgule.

    >>> message_distance(0, 0, 3, 4)
    'La distance entre les deux points est de 5.00 unités.'
    """
    d = distance(x1, y1, x2, y2)
    return f"La distance entre les deux points est de {d:.2f} unités."
```
{{< /solution >}}

{{< note success "Bilan : où en suis-je ?" >}}
Pour chaque ligne, cochez la colonne qui correspond. Toute case **Pas encore** indique une partie à reprendre.

| **Je sais…** | **Oui** | **Pas encore** | **À revoir** |
|:---|:---|:---|:---|
| choisir un **identificateur** valide pour une variable |  |  | Partie 1 |
| prévoir l'effet d'une affectation simple, multiple ou groupée |  |  | Partie 2 |
| utiliser un **opérateur d'affectation** (`+=`, `-=`, ...) pour mettre à jour une variable |  |  | Partie 3 |
| échanger les valeurs de deux variables à l'aide d'une variable supplémentaire |  |  | Partie 3 |
| insérer une valeur ou une expression dans un texte avec une **f-string** |  |  | Partie 4 |
| afficher un nombre flottant avec un nombre choisi de chiffres après la virgule |  |  | Partie 4 |
{{< /note >}}

{{< qcm >}}
- question: 'Avec `age = 15`, que produit `"Tu as " + age + " ans"` ?'
  reponses:
    - '`''Tu as 15 ans''`'
    - 'Une `TypeError` : on ne peut pas concaténer un `str` et un `int`.'
    - '`''Tu as age ans''`'
  bonne: 2
  explication: 'L''opérateur `+` entre chaînes exige deux `str` : il ne convertit pas l''entier. Avec une f-string, `f"Tu as {age} ans"` fonctionne.'
- question: 'Avec `prenom = "Alice"` et `age = 15`, que vaut `f"{prenom} aura {age + 1} ans"` ?'
  reponses:
    - '`''Alice aura 16 ans''`'
    - '`''Alice aura 151 ans''`'
    - '`''{prenom} aura {age + 1} ans''`'
  bonne: 1
  explication: 'Chaque expression entre accolades est évaluée, convertie en `str`, puis insérée : `age + 1` vaut 16.'
- question: 'Avec `montant = 3333.3333`, que vaut `f"{montant:.2f} €"` ?'
  reponses:
    - '`''3333.33 €''`'
    - '`''33.33 €''`'
    - '`''3333.3333 €''`'
    - '`''3300 €''`'
  bonne: 1
  explication: '`:.2f` affiche le flottant arrondi à 2 chiffres après la virgule.'
- question: 'Laquelle de ces chaînes provoque une erreur ?'
  reponses:
    - '`"Python, c''est top !"`'
    - '`''Python, c''est top !''`'
    - '`"abcd"`'
  bonne: 2
  explication: 'Dans `''Python, c''est top !''`, l''apostrophe de « c''est » referme la chaîne ouverte par `''`. Quand le texte contient une apostrophe, on le délimite avec des guillemets doubles.'
{{< /qcm >}}
