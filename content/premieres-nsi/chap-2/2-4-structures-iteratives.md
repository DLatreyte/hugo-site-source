---
title: "Structures itératives"
subtitle: "Doc. 2,4"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["boucle", "itération", "boucle déterministe", "boucle non déterministe", "compteur de boucle", "condition d'arrêt", "boucle infinie", "while", "for", "range", "break", "continue"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 40
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-2/2-4/2-4-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/premieres-nsi/chap-2/2-4/2-4-corrige.pdf" >}}

{{< note goal >}}
En manipulant les boucles `for` et `while` dans la console et dans Thonny, vous allez apprendre à répéter des instructions un nombre de fois connu ou inconnu à l'avance, et à choisir la structure itérative adaptée à chaque situation.
{{< /note >}}

## Combien de fois une instruction doit-elle être répétée ?

Un programme est souvent amené à répéter plusieurs fois les mêmes instructions : afficher les nombres de 1 à 1000, demander un mot de passe jusqu'à ce qu'il soit correct, ou additionner les notes d'une classe entière. Écrire autant de fois l'instruction à répéter serait absurde ; les langages de programmation proposent pour cela des **structures itératives**, plus couramment appelées **boucles**. Chaque passage dans une boucle est appelé une **itération**.

{{< question >}}
Pour chacune des situations suivantes, indiquer si le nombre de répétitions est connu **avant** de commencer à répéter, ou s'il n'est découvert qu'**au fur et à mesure** de l'exécution :

- afficher les nombres de 1 à 100 ;
- demander un mot de passe jusqu'à ce qu'il soit correct ;
- additionner les 12 notes d'un bulletin ;
- lancer un dé jusqu'à l'obtention d'un 6.
{{< /question >}}

{{< solution "Réponse" >}}
Le nombre de répétitions est connu à l'avance dans les deux premiers cas (100 affichages, 12 notes). Il ne l'est pas dans les deux autres cas : il dépend du déroulement de l'exécution, qu'on ne peut pas prévoir avant de commencer.
{{< /solution >}}

{{< note success "À retenir" >}}
- Une **boucle déterministe** (ou boucle **Pour**) répète un nombre d'itérations **connu à l'avance** ; elle utilise une variable, le **compteur de boucle**, pour compter les itérations effectuées.
- Une **boucle non déterministe** (ou boucle **conditionnelle**) répète des itérations **tant qu'une condition d'arrêt n'est pas vérifiée** ; ce nombre n'est pas connu à l'avance.

Python ne fournit qu'une seule boucle non déterministe, la boucle `while` (**Tant que**). Une boucle non déterministe peut toujours remplacer une boucle déterministe ; l'inverse n'est pas vrai.
{{< /note >}}

{{< qcm >}}
- question: 'On demande un mot de passe jusqu''à ce qu''il soit correct. Quel type de boucle convient ?'
  reponses:
    - 'Une boucle déterministe (boucle Pour), car on connaît le nombre d''essais à l''avance.'
    - 'Une boucle non déterministe (boucle Tant que), car le nombre d''essais n''est pas connu à l''avance.'
  bonne: 2
  explication: 'On ne sait pas combien d''essais seront nécessaires : on répète tant que la condition d''arrêt (mot de passe correct) n''est pas vérifiée.'
- question: 'Quelle est la seule boucle non déterministe disponible en Python ?'
  reponses:
    - '`for`'
    - '`while`'
    - '`repeat`'
  bonne: 2
  explication: 'La boucle `while` répète son bloc tant qu''une condition est vraie, sans connaître à l''avance le nombre d''itérations.'
{{< /qcm >}}

## La boucle "Tant que" : l'instruction `while`

### Syntaxe et fonctionnement

La syntaxe d'une boucle `while` est :

```python
while <condition>:
    instructions à répéter
```

La **condition** est une expression booléenne, évaluée **au début de chaque itération**. Tant qu'elle vaut `True`, le bloc indenté est exécuté, puis la condition est évaluée à nouveau. Dès qu'elle vaut `False`, la boucle s'arrête et l'exécution reprend après le bloc. Il est même possible que le bloc ne soit exécuté **aucune fois**, si la condition est déjà fausse dès la première évaluation.

{{< question >}}
Recopier la fonction suivante dans la partie principale de l'éditeur Thonny :

```python
def affiche_jusqua(n: int) -> None:
    """
    Affiche les entiers de 1 à n, un par ligne, à l'aide d'une boucle Tant que.
    """
    i = 1            # (1)
    while i <= n:    # (2)
        print(i)     # (3)
        i += 1       # (4)
```

Remplacer chacun des numéros ci-dessus par une phrase qui décrit ce que l'instruction réalise.
{{< /question >}}

{{< solution "Réponse" >}}
1. On affecte la valeur entière 1 à la variable `i` ;
1. Tant que la valeur référencée par la variable `i` est inférieure ou égale à la valeur référencée par la variable `n` ;
1. On affiche la valeur référencée par la variable `i` ;
1. On incrémente de 1 la valeur que référence la variable `i`.
{{< /solution >}}

{{< question >}}
Appeler ensuite, dans la console, la fonction : `affiche_jusqua(5)` puis `affiche_jusqua(0)`. \
Combien de fois le bloc indenté est-il exécuté dans le premier appel ? Dans le second appel ? 
{{< /question >}}

{{< solution "Réponse" >}}
`affiche_jusqua(5)` affiche les nombres de 1 à 5. `affiche_jusqua(0)` n'affiche rien : dès la première évaluation, `i <= n` vaut `False` (`1 <= 0`) ; le bloc n'est donc exécuté aucune fois.
{{< /solution >}}

{{< question >}}
Quelle instruction fait progresser `i` vers la condition d'arrêt ?
{{< /question >}}

{{< solution "Réponse" >}}
L'instruction `i += 1` fait progresser `i` à chaque itération, jusqu'à ce que la condition devienne fausse.
{{< /solution >}}

{{< note warning "Boucle infinie" >}}
Si aucune instruction du bloc ne fait progresser la condition vers sa fin (si, par exemple, `i += 1` avait été oublié), la condition `i <= n` resterait indéfiniment vraie : la boucle s'exécuterait sans jamais s'arrêter. Ce défaut porte un nom : la **boucle infinie**.
{{< /note >}}

{{< note success "À retenir" >}}
Écrire une boucle `while` suppose de réunir trois éléments :

1. une **initialisation** de la ou des variables testées par la condition ;
1. une **condition d'arrêt**, expression booléenne évaluée avant chaque itération ;
1. une instruction qui **fait progresser** cette condition à chaque itération, jusqu'à ce qu'elle devienne fausse.

Oublier ce troisième élément est la cause la plus fréquente de **boucle infinie**.
{{< /note >}}

### Faire tourner une boucle à la main

Vérifier qu'une boucle fait ce qu'on attend d'elle exige de savoir la « faire tourner à la main » : appliquer méthodiquement les instructions, itération après itération, en notant dans un tableau l'évolution du contenu de chaque variable.

{{< question >}}
On donne la fonction suivante, dont il faut déterminer l'action :

```python
def inconnue(a: int, b: int) -> int:
    """ Fonction dont il faut déterminer l'action. """
    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return b
```

1. Repérer les instructions répétées par la boucle et l'instruction qui teste la fin de la boucle.
1. Quelle instruction modifie le résultat de l'évaluation de ce test ?
1. Sans utiliser Python, compléter le tableau d'évolution ci-dessous pour l'appel `inconnue(30, 42)`, puis vérifier en exécutant le programme.

| **Étape** | **a** | **b** | **r** |
|:---|:---|:---|:---|
| avant la boucle | 30 | 42 |  |
| itération 1 |  |  |  |
| itération 2 |  |  |  |
| itération 3 |  |  |  |

4. Visualiser le fonctionnement de cette fonction à l'aide du débogueur intégré à Thonny.
1. Reprendre la question précédente pour l'appel `inconnue(35, 6)`, sans reconstruire de tableau : donner uniquement la valeur retournée.
1. Quel calcul réalise cette fonction ?
{{< /question >}}

{{< solution "Réponse" >}}
1. Structure répétée :
   ```python
   while r != 0:
       a = b
       b = r
       r = a % b
   ```
   Fin de boucle lorsque `r == 0`.

1. L'instruction `r = a % b` modifie le résultat du test `r != 0`.

1. | **Étape** | **a** | **b** | **r** |
   |:---|:---|:---|:---|
   | avant la boucle | 30 | 42 | 30 |
   | itération 1 | 42 | 30 | 12 |
   | itération 2 | 30 | 12 | 6 |
   | itération 3 | 12 | 6 | 0 |

   La condition `r != 0` devient fausse après l'itération 3 : la fonction retourne `b`, soit `6`.

1. Lancer le programme en mode débogage puis utiliser la touche <kbd>F7</kbd>.

1. Valeur retournée : `1`.

1. Cette fonction calcule le **PGCD** (plus grand commun diviseur) de deux nombres, par l'**algorithme d'Euclide**.
{{< /solution >}}

{{< question >}}
Voici une autre fonction, dont il faut également déterminer l'action :

```python
def inconnue_deux(a: int) -> int:
    """ Fonction dont il faut déterminer l'action. """
    b = 1
    i = 2
    while i <= a:
        b *= i
        i += 1
    return b
```

1. Quelle est la valeur initiale de `i` ? Quelle est sa valeur lorsque la boucle s'arrête ?
1. Sans utiliser Python, compléter le tableau d'évolution ci-dessous pour l'appel `inconnue_deux(6)`, puis vérifier en exécutant le programme.

| **Étape** | **i** | **b** |
|:---|:---|:---|
| avant la boucle | 2 | 1 |
| itération 1 |  |  |
| itération 2 |  |  |
| itération 3 |  |  |
| itération 4 |  |  |
| itération 5 |  |  |

3. Quel calcul réalise cette fonction ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `i` vaut `2` avant la boucle. Elle s'arrête lorsque `i` atteint `7` (`i <= a` devient alors fausse).

1. | **Étape** | **i** | **b** |
   |:---|:---|:---|
   | avant la boucle | 2 | 1 |
   | itération 1 | 3 | 2 |
   | itération 2 | 4 | 6 |
   | itération 3 | 5 | 24 |
   | itération 4 | 6 | 120 |
   | itération 5 | 7 | 720 |

   La fonction retourne `720`.

1. Cette fonction calcule la **factorielle** de `a`, notée $a!$, c'est-à-dire le produit $1 \times 2 \times \dots \times a$.
{{< /solution >}}

{{< qcm >}}
- question: 'Dans `affiche_jusqua(n)` (`i = 1`, puis `while i <= n:` avec `print(i)` et `i += 1`), combien de fois le bloc est-il exécuté pour `affiche_jusqua(0)` ?'
  reponses:
    - '0 fois'
    - '1 fois'
    - 'Une infinité de fois'
  bonne: 1
  explication: 'La condition est évaluée avant chaque itération. Dès le départ, `1 <= 0` vaut `False` : le bloc n''est jamais exécuté.'
- question: 'Dans cette même fonction, que se passe-t-il si on oublie l''instruction `i += 1` ?'
  reponses:
    - 'La boucle s''arrête immédiatement.'
    - 'La condition `i <= n` reste vraie : c''est une boucle infinie.'
    - 'Python ajoute automatiquement 1 à `i`.'
  bonne: 2
  explication: 'Rien ne fait progresser la condition vers sa fin : la boucle ne s''arrête jamais.'
- question: 'Quels sont les trois éléments d''une boucle `while` bien écrite ?'
  reponses:
    - 'Une initialisation, une condition d''arrêt et une instruction qui fait progresser la condition.'
    - 'Un `range`, un compteur et un `return`.'
    - 'Une condition, un `print` et un `break`.'
  bonne: 1
  explication: 'Oublier le troisième élément est la cause la plus fréquente de boucle infinie.'
{{< /qcm >}}

## La boucle "Pour chaque" : l'instruction for et l'itérateur range

### Syntaxe de la boucle "Pour chaque"

En Python, l'instruction `for` implémente en réalité une boucle **Pour chaque** : elle parcourt, un par un, les éléments d'un objet **itérable**, et non un simple compteur comme dans d'autres langages.

```python
for element in itérable:
    instructions à répéter
```

À chaque itération, la variable `element` prend la valeur de l'élément courant de l'itérable, pour être utilisée dans le bloc indenté. **Cette variable ne doit jamais être modifiée dans le corps de la boucle** : dans le cas contraire, le comportement de la boucle devient imprévisible.

{{< question >}}
Recopier la fonction suivante dans la partie principale de l'éditeur :

```python
def affiche_intervalle(n: int) -> None:
    """Affiche, séparés par un espace, les entiers produits par
    range(1, n + 1).
    """
    for nbre in range(1, n + 1):
        print(nbre, end=' ')
```

Appeler `affiche_intervalle(10)` dans la console. Quels entiers sont produits par `range(1, 11)` ? Combien y en a-t-il ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> affiche_intervalle(10)
1 2 3 4 5 6 7 8 9 10
```
`range(1, 11)` produit les dix entiers de 1 à 10 (11 exclu) : c'est **l'itérable** que parcourt ensuite la boucle `for`.
{{< /solution >}}

{{< question >}}
Recopier la fonction suivante dans la partie principale de l'éditeur :

```python
def table_de(n: int) -> str:
    """ Retourne la table de multiplication de n, de 1 à 10. """
    reponse = ""
    for nbre in range(1, 11):
        calcul = n * nbre
        reponse += str(calcul) + " "
    return reponse
```

Cette fonction parcourt le même itérable que la précédente. Sans exécuter le programme, prévoir le résultat de `table_de(4)`, puis vérifier dans la console.

Réécrire ensuite l'instruction `reponse += str(calcul) + " "` à l'aide d'une f-string (voir Doc. 2,2), et vérifier que `table_de(4)` retourne toujours le même résultat.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> table_de(4)
'4 8 12 16 20 24 28 32 36 40 '
```
```python
reponse += f"{calcul} "
```
{{< /solution >}}

### L'itérateur range

{{< note success "L'itérateur range" >}}
L'itérateur `range` génère, à la volée, des entiers compris entre une valeur de départ `début` et une valeur finale `fin` (exclue), par pas de `pas`. Trois écritures sont possibles :

| `range(fin)` | entiers de 0 à `fin` (exclu), par pas de 1 |
|:---|:---|
| `range(début, fin)` | entiers de `début` à `fin` (exclu), par pas de 1 |
| `range(début, fin, pas)` | entiers de `début` à `fin` (exclu), par pas de `pas` |

Comme pour les tranches, la valeur `fin` n'est **jamais** atteinte : Python considère systématiquement les intervalles sous la forme $[\text{début}, \text{fin}[$.
{{< /note >}}

{{< question >}}
Recopier la fonction suivante dans la partie principale de l'éditeur :

```python
def demo_range(debut: int, fin: int, pas: int) -> None:
    """Affiche, séparés par un espace, les entiers produits par
    range(debut, fin, pas).
    """
    for i in range(debut, fin, pas):
        print(i, end=' ')
```

Prévoir puis vérifier dans la console le résultat de chacun des appels suivants :

```python
>>> demo_range(1, 10, 1)
>>> demo_range(1, 10, 3)
>>> demo_range(10, 1, -1)
>>> demo_range(10, -15, -3)
```

Le pas `pas` peut-il être négatif ? Que se passe-t-il alors ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> demo_range(1, 10, 1)
1 2 3 4 5 6 7 8 9
>>> demo_range(1, 10, 3)
1 4 7
>>> demo_range(10, 1, -1)
10 9 8 7 6 5 4 3 2
>>> demo_range(10, -15, -3)
10 7 4 1 -2 -5 -8 -11 -14
```
Le pas peut être négatif : `range` produit alors une suite **décroissante**, tant que la valeur reste strictement supérieure à `fin`.
{{< /solution >}}

{{< question >}}
Écrire, dans la partie principale de l'éditeur, deux fonctions `demo_range_1arg` et `demo_range_2arg`, qui affichent respectivement, séparés par un espace, les entiers produits par `range(fin)` et par `range(debut, fin)`.

Tester `demo_range_1arg(10)` et `demo_range_2arg(1, 10)` dans la console.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def demo_range_1arg(fin: int) -> None:
    """Affiche les entiers produits par range(fin)."""
    for i in range(fin):
        print(i, end=' ')

def demo_range_2arg(debut: int, fin: int) -> None:
    """Affiche les entiers produits par range(debut, fin)."""
    for i in range(debut, fin):
        print(i, end=' ')
```
```python
>>> demo_range_1arg(10)
0 1 2 3 4 5 6 7 8 9
>>> demo_range_2arg(1, 10)
1 2 3 4 5 6 7 8 9
```
{{< /solution >}}

{{< note success "À retenir" >}}
La boucle `for element in itérable:` parcourt un par un les éléments d'un itérable ; la variable `element` ne doit jamais être modifiée dans le corps de la boucle.

L'itérateur `range(début, fin, pas)` génère les entiers de `début` (inclus) à `fin` (exclu), par pas de `pas`. Avec un seul argument, `range(fin)` part de 0 avec un pas de 1 ; avec deux arguments, `range(début, fin)` utilise un pas de 1.

Une boucle `for` peut toujours être réécrite avec une boucle `while`, en gérant soi-même le compteur ; l'inverse n'est vrai que si le nombre d'itérations est connu à l'avance.
{{< /note >}}

{{< qcm >}}
- question: 'Quels entiers sont produits par `range(1, 5)` ?'
  reponses:
    - '1, 2, 3, 4, 5'
    - '1, 2, 3, 4'
    - '0, 1, 2, 3, 4'
    - '2, 3, 4, 5'
  bonne: 2
  explication: '`range(début, fin)` produit les entiers de `début` (inclus) à `fin` (exclu).'
- question: 'Quels entiers sont produits par `range(4)` ?'
  reponses:
    - '0, 1, 2, 3'
    - '1, 2, 3, 4'
    - '0, 1, 2, 3, 4'
  bonne: 1
  explication: 'Avec un seul argument, `range(fin)` part de 0, avec un pas de 1, et `fin` est exclu.'
- question: 'Quels entiers sont produits par `range(10, 1, -3)` ?'
  reponses:
    - '10, 7, 4'
    - '10, 7, 4, 1'
    - 'Aucun : la fin est plus petite que le début.'
  bonne: 1
  explication: 'Avec un pas négatif, on descend : 10, 7, 4. La valeur suivante, 1, est la fin : elle est exclue.'
- question: 'Dans une boucle `for element in iterable:`, peut-on modifier `element` dans le corps de la boucle ?'
  reponses:
    - 'Oui, c''est même ainsi qu''on accélère la boucle.'
    - 'Non : cette variable ne doit jamais être modifiée dans le corps de la boucle.'
  bonne: 2
  explication: 'C''est la boucle `for` qui donne ses valeurs à `element`, une à une. Le modifier rend le programme difficile à comprendre.'
{{< /qcm >}}

## Interrompre une boucle ou passer à l'itération suivante : break et continue

### L'instruction break

`break` **met fin immédiatement à la boucle en cours** et poursuit l'exécution juste après elle. On l'utilise généralement lorsqu'une condition testée avec `if` doit provoquer une sortie immédiate de la boucle. `break` s'utilise aussi bien dans une boucle `for` que dans une boucle `while` ; elle est en particulier indispensable pour sortir d'une boucle délibérément infinie, écrite avec `while True:`.

{{< question >}}
Les deux fonctions suivantes déterminent, par une méthode peu efficace, le plus grand diviseur d'un entier `nbre` (différent de `nbre` lui-même) : on teste, en partant de `nbre - 1`, tous les diviseurs possibles, jusqu'à en trouver un qui convient.

```python
def plus_grand_diviseur(nbre: int) -> str:
    """Retourne un message donnant le plus grand diviseur de nbre,
    différent de nbre lui-même.
    """
    diviseur = nbre - 1
    while diviseur > 0:
        if nbre % diviseur == 0:
            break
        diviseur -= 1
    return f"Le plus grand diviseur de {nbre} est {diviseur}."

def plus_grand_diviseur_2(nbre: int) -> str:
    """Retourne un message donnant le plus grand diviseur de nbre,
    différent de nbre lui-même.
    """
    for diviseur in range(nbre - 1, 0, -1):
        if nbre % diviseur == 0:
            break
    return f"Le plus grand diviseur de {nbre} est {diviseur}."
```

Tester les deux fonctions avec `nbre = 18`. Pourquoi est-il inutile de continuer la boucle une fois un diviseur trouvé ? Dans la seconde fonction, à quel endroit du programme la variable `diviseur` reste-t-elle accessible, alors qu'elle est définie par la boucle `for` ?
{{< /question >}}

{{< solution "Réponse" >}}
Les deux fonctions retournent `"Le plus grand diviseur de 18 est 9."`. Une fois le premier diviseur trouvé en partant du plus grand possible, c'est nécessairement le plus grand diviseur cherché : poursuivre la boucle ne changerait rien au résultat, `break` l'évite.

Dans la seconde fonction, la variable `diviseur` reste accessible **après** la boucle `for`, dans l'instruction `return` : contrairement à d'autres langages, une variable définie par une boucle `for` en Python est accessible en dehors de cette boucle.
{{< /solution >}}

### L'instruction continue

`continue` **interrompt seulement l'itération courante** et reprend au début de l'itération suivante : nouvelle évaluation de la condition pour une boucle `while`, élément suivant pour une boucle `for`.

{{< question >}}
Les deux fonctions suivantes retournent une chaîne de caractères formée des entiers, inférieurs à `nbre`, qui **ne le divisent pas** :

```python
def non_diviseur(nbre: int) -> str:
    """Retourne les entiers de 1 à nbre - 1 qui ne divisent pas nbre."""
    reponse = ""
    diviseur = nbre - 1
    while diviseur > 0:
        if nbre % diviseur == 0:
            diviseur -= 1
            continue
        reponse += str(diviseur) + " "
        diviseur -= 1
    return reponse

def non_diviseur_2(nbre: int) -> str:
    """Retourne les entiers de 1 à nbre - 1 qui ne divisent pas nbre."""
    reponse = ""
    for diviseur in range(nbre - 1, 0, -1):
        if nbre % diviseur == 0:
            continue
        reponse += str(diviseur) + " "
    return reponse
```

Tester les deux fonctions avec `nbre = 18`. Dans `non_diviseur`, pourquoi l'instruction `diviseur -= 1` apparaît-elle à deux endroits différents ?
{{< /question >}}

{{< solution "Réponse" >}}
Les deux fonctions retournent `'17 16 14 13 11 10 8 7 5 4 2 1 '`.

Dans `non_diviseur`, `continue` fait immédiatement remonter l'exécution au test `while diviseur > 0`, **sans exécuter la suite du bloc**. Si `diviseur -= 1` n'apparaissait qu'après `reponse += ...`, la variable ne serait jamais décrémentée lorsque `nbre % diviseur == 0` : la boucle deviendrait infinie.
{{< /solution >}}

{{< question >}}
Réécrire la fonction `non_diviseur_2` sous la forme `non_diviseur_3`, **sans utiliser** `continue`, à l'aide d'un simple `if`, et en construisant `reponse` à l'aide d'une f-string plutôt que de `str(diviseur) + " "`. Cette nouvelle version est-elle plus lisible ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def non_diviseur_3(nbre: int) -> str:
    """Retourne les entiers de 1 à nbre - 1 qui ne divisent pas nbre."""
    reponse = ""
    for diviseur in range(nbre - 1, 0, -1):
        if nbre % diviseur != 0:
            reponse += f"{diviseur} "
    return reponse
```
Ici, `continue` n'apportait rien : inverser la condition (`!=` au lieu de `==`) suffit et rend le code plus direct. `continue` devient surtout utile lorsque plusieurs instructions doivent être ignorées avant de revenir au test.
{{< /solution >}}

{{< note success "À retenir" >}}
- `break` **arrête définitivement** la boucle en cours ; l'exécution reprend juste après elle.
- `continue` **arrête seulement l'itération en cours** ; l'exécution reprend au début de l'itération suivante.

Ces deux instructions s'utilisent aussi bien dans une boucle `for` que dans une boucle `while`.
{{< /note >}}

{{< qcm >}}
- question: 'Que fait l''instruction `break` ?'
  reponses:
    - 'Elle arrête définitivement la boucle ; l''exécution reprend juste après la boucle.'
    - 'Elle passe directement à l''itération suivante.'
    - 'Elle arrête tout le programme.'
  bonne: 1
  explication: '`break` sort de la boucle en cours. C''est `continue` qui passe à l''itération suivante.'
- question: 'Que fait l''instruction `continue` ?'
  reponses:
    - 'Elle arrête définitivement la boucle.'
    - 'Elle termine seulement l''itération en cours et reprend au début de l''itération suivante.'
    - 'Elle n''a aucun effet ; elle sert seulement de commentaire.'
  bonne: 2
  explication: 'Les instructions qui suivent `continue` dans le bloc sont sautées pour cette itération seulement.'
- question: '`break` et `continue` s''utilisent :'
  reponses:
    - 'uniquement dans une boucle `for`'
    - 'uniquement dans une boucle `while`'
    - 'dans les deux types de boucles'
  bonne: 3
  explication: 'Ces deux instructions fonctionnent aussi bien dans une boucle `for` que dans une boucle `while`.'
{{< /qcm >}}

## Exercices de synthèse

{{< note warning "Consigne" >}}
Écrire chaque fonction dans la partie principale de l'éditeur, avec sa spécification complète (signature + documentation), en utilisant des f-strings pour construire les chaînes de caractères (voir Doc. 2,2). Tester ensuite son appel dans la console.
{{< /note >}}

### Construire un résultat au fil des itérations

{{< question >}}
Écrire la fonction `triple_du_precedent` dont la spécification est :

```python
def triple_du_precedent(a: int) -> str:
    """
    Retourne une chaîne de caractères formée d'une suite de 12 entiers dont chaque terme est 
    le triple du précédent, à partir du premier entier a (positif) passé en argument.

    >>> triple_du_precedent(1)
    '1 3 9 27 81 243 729 2187 6561 19683 59049 177147 '
    >>> triple_du_precedent(5)
    '5 15 45 135 405 1215 3645 10935 32805 98415 295245 885735 '
    """
```

Utiliser une boucle `while`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def triple_du_precedent(a: int) -> str:
    """Retourne une chaîne de caractères formée d'une suite de 12
    entiers dont chaque terme est le triple du précédent, à partir
    du premier entier a (positif) passé en argument.

    >>> triple_du_precedent(1)
    '1 3 9 27 81 243 729 2187 6561 19683 59049 177147 '
    >>> triple_du_precedent(5)
    '5 15 45 135 405 1215 3645 10935 32805 98415 295245 885735 '
    """
    reponse = ""
    compteur = 1
    val_max_compteur = 12
    while compteur <= val_max_compteur:
        reponse += f"{a} "
        a *= 3
        compteur += 1
    return reponse
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `multiplication_multiple_trois` dont la spécification est :

```python
def multiplication_multiple_trois(a: int) -> str:
    """Retourne les 10 premiers termes de la table de multiplication
    de a, en signalant par un astérisque ceux qui sont multiples de 3.

    >>> multiplication_multiple_trois(2)
    '2 4 6* 8 10 12* 14 16 18* 20 '
    >>> multiplication_multiple_trois(7)
    '7 14 21* 28 35 42* 49 56 63* 70 '
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def multiplication_multiple_trois(a: int) -> str:
    """Retourne les 10 premiers termes de la table de multiplication
    de a, en signalant par un astérisque ceux qui sont multiples de 3.

    >>> multiplication_multiple_trois(2)
    '2 4 6* 8 10 12* 14 16 18* 20 '
    >>> multiplication_multiple_trois(7)
    '7 14 21* 28 35 42* 49 56 63* 70 '
    """
    reponse = ""
    compteur = 1
    val_max_compteur = 10
    while compteur <= val_max_compteur:
        valeur = a * compteur
        reponse += f"{valeur}"
        if valeur % 3 == 0:
            reponse += "*"
        reponse += " "
        compteur += 1
    return reponse
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `multiplication_multiple_sept` dont la spécification est :

```python
def multiplication_multiple_sept(a: int) -> str:
    """Calcule les 50 premiers termes de la table de multiplication
    de a et retourne une chaîne de caractères contenant uniquement
    les multiples de 7.

    >>> multiplication_multiple_sept(2)
    '14 28 42 56 70 84 98 '
    >>> multiplication_multiple_sept(9)
    '63 126 189 252 315 378 441 '
    """
```

En quoi cette fonction diffère-t-elle de `multiplication_multiple_trois` : marque-t-elle simplement des valeurs, ou en sélectionne-t-elle certaines ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def multiplication_multiple_sept(a: int) -> str:
    """Calcule les 50 premiers termes de la table de multiplication
    de a et retourne une chaîne de caractères contenant uniquement
    les multiples de 7.

    >>> multiplication_multiple_sept(2)
    '14 28 42 56 70 84 98 '
    >>> multiplication_multiple_sept(9)
    '63 126 189 252 315 378 441 '
    """
    reponse = ""
    compteur = 1
    val_max_compteur = 50
    while compteur <= val_max_compteur:
        valeur = a * compteur
        if valeur % 7 == 0:
            reponse += f"{valeur} "
        compteur += 1
    return reponse
```
`multiplication_multiple_trois` ajoute **toutes** les valeurs à la chaîne, en marquant certaines d'un astérisque. `multiplication_multiple_sept` **sélectionne** les valeurs à ajouter : l'instruction `reponse += ...` est placée à l'intérieur du `if`, et non plus après.
{{< /solution >}}

{{< question >}}
Écrire la fonction `diviseurs` dont la spécification est :

```python
def diviseurs(a: int) -> str:
    """Retourne une chaîne de caractères formée de la liste des
    diviseurs de a, de a lui-même jusqu'à 1.

    >>> diviseurs(18)
    '18 9 6 3 2 1 '
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def diviseurs(a: int) -> str:
    """Retourne une chaîne de caractères formée de la liste des
    diviseurs de a, de a lui-même jusqu'à 1.

    >>> diviseurs(18)
    '18 9 6 3 2 1 '
    """
    n = a - 1
    reponse = f"{a} "
    while n > 0:
        if a % n == 0:
            reponse += f"{n} "
        n -= 1
    return reponse
```
{{< /solution >}}

{{< question >}}
Écrire et exécuter la fonction `loto_naif` dont la spécification est :

```python
def loto_naif() -> str:
    """Retourne 6 entiers sélectionnés aléatoirement dans
    l'intervalle [1, 49].
    """
```

**Remarque.** Normalement, un numéro déjà tiré ne peut pas réapparaître. On acceptera ici qu'un même numéro apparaisse plusieurs fois, faute de disposer encore d'une structure de données adaptée pour mémoriser les numéros déjà sortis.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def loto_naif() -> str:
    """Retourne 6 entiers sélectionnés aléatoirement dans
    l'intervalle [1, 49].
    """
    import random
    reponse = ""
    i = 1
    nbre_boules = 6
    while i <= nbre_boules:
        boule = random.randint(1, 49)
        reponse += f"{boule} "
        i += 1
    return reponse
```
{{< /solution >}}

### Boucles imbriquées

{{< question >}}
Écrire la fonction `table_multiplication` dont la spécification est :

```python
def table_multiplication() -> str:
    """Retourne les tables de multiplication de 1 à 10, chaque table
    étant écrite sur une ligne distincte.
    """
```

**Indication.** Utiliser deux boucles `while` imbriquées, et le caractère `"\n"` pour passer à la ligne. Tester avec `print(table_multiplication())` dans la console, pour visualiser le résultat sous forme de tableau.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def table_multiplication() -> str:
    """Retourne les tables de multiplication de 1 à 10, chaque table
    étant écrite sur une ligne distincte.
    """
    i = 1
    j = 1
    reponse = ""
    val_max = 10
    while i <= val_max:
        while j <= val_max:
            reponse += f"{i * j} "
            j += 1
        reponse += "\n"
        i += 1
        j = 1
    return reponse
```
{{< /solution >}}

### Demander une information à l'utilisateur

La fonction `input` retourne **toujours** une chaîne de caractères ; une conversion est donc nécessaire pour récupérer un nombre :

```python
valeur = float(input("Entrez votre valeur : "))
```

{{< question >}}
Écrire la fonction `plus_grand_plus_petit` dont la spécification est :

```python
def plus_grand_plus_petit(nbre_valeurs: int) -> str:
    """Demande à l'utilisateur nbre_valeurs valeurs et retourne une
    chaîne de caractères donnant le maximum et le minimum obtenus.
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def plus_grand_plus_petit(nbre_valeurs: int) -> str:
    """Demande à l'utilisateur nbre_valeurs valeurs et retourne une
    chaîne de caractères donnant le maximum et le minimum obtenus.
    """
    valeur = float(input("Entrez la valeur 1 : "))
    valeur_plus_grande = valeur
    valeur_plus_petite = valeur
    i = 2
    while i <= nbre_valeurs:
        valeur = float(input(f"Entrez la valeur {i} : "))
        if valeur > valeur_plus_grande:
            valeur_plus_grande = valeur
        elif valeur < valeur_plus_petite:
            valeur_plus_petite = valeur
        i += 1
    return f"max : {valeur_plus_grande}, min : {valeur_plus_petite}"
```
{{< /solution >}}

{{< question >}}
Écrire la fonction `moyenne` dont la spécification est :

```python
def moyenne(nbre_notes: int) -> float:
    """Demande à l'utilisateur nbre_notes notes et retourne leur
    moyenne.
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def moyenne(nbre_notes: int) -> float:
    """Demande à l'utilisateur nbre_notes notes et retourne leur
    moyenne.
    """
    somme = 0
    i = 1
    while i <= nbre_notes:
        note = float(input(f"Entrez la note {i} : "))
        somme += note
        i += 1
    return somme / nbre_notes
```
{{< /solution >}}

### Boucles pilotées par un événement imprévisible

Dans les deux fonctions précédentes, le nombre de saisies est un paramètre fixé à l'avance : une boucle `while` n'était donc pas indispensable. Il existe des situations où ce nombre ne peut au contraire **pas** être connu avant l'exécution.

{{< question >}}
On souhaite ne plus imposer le nombre de notes à saisir : l'utilisateur arrête la saisie en entrant une note négative. Écrire la fonction `moyenne_ter` dont la spécification est :

```python
def moyenne_ter() -> str:
    """Demande des notes à l'utilisateur et retourne un message
    donnant leur nombre et leur moyenne. La saisie s'arrête dès
    qu'une note négative est entrée.
    """
```

**Indication.** Écrire `while True:` et utiliser `break` pour sortir de la boucle. Pourquoi une boucle `for` ne convient-elle pas ici ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def moyenne_ter() -> str:
    """Demande des notes à l'utilisateur et retourne un message
    donnant leur nombre et leur moyenne. La saisie s'arrête dès
    qu'une note négative est entrée.
    """
    somme = 0
    nbre_notes = 0
    while True:
        note = float(input(f"Entrez la note {nbre_notes + 1} : "))
        if note < 0:
            break
        somme += note
        nbre_notes += 1
    return f"Nbre de notes : {nbre_notes}, moyenne : {somme / nbre_notes:.2f}"
```
Le nombre de notes n'est pas connu avant de commencer la saisie : c'est une situation **non déterministe**, qui exige une boucle `while`.
{{< /solution >}}

{{< question >}}
Écrire et exécuter la fonction `devine` dont la spécification est :

```python
def devine() -> None:
    """Détermine aléatoirement un entier compris entre 1 et 50 et
    demande à l'utilisateur de le deviner. À chaque proposition,
    affiche si elle est trop grande ou trop petite. S'arrête et
    annonce le nombre de tentatives lorsque le nombre est deviné.
    """
```

**Indication.** Le module `random` et sa fonction `randint` ont été présentés dans le Doc. 2,1.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def devine() -> None:
    """Détermine aléatoirement un entier compris entre 1 et 50 et
    demande à l'utilisateur de le deviner. À chaque proposition,
    affiche si elle est trop grande ou trop petite. S'arrête et
    annonce le nombre de tentatives lorsque le nombre est deviné.
    """
    import random
    nbre_a_deviner = random.randint(1, 50)
    nbre_tentatives = 0
    while True:
        nbre = int(input(f"Proposition n° {nbre_tentatives + 1} : "))
        nbre_tentatives += 1
        if nbre == nbre_a_deviner:
            print(f"Bravo, le nombre a été deviné en {nbre_tentatives} tentatives.")
            break
        elif nbre > nbre_a_deviner:
            print("Trop grand !")
        else:
            print("Trop petit !")
```
{{< /solution >}}

### Manipuler le code ASCII

{{< question >}}
Écrire et exécuter la fonction `alphabet` dont la spécification est :

```python
def alphabet(sens: str) -> str:
    """Retourne les 26 lettres de l'alphabet dans l'ordre croissant
    si sens vaut 'croissant', dans l'ordre décroissant si sens vaut
    'decroissant'.
    """
```

**Indication.** `ord(car)` retourne le code ASCII du caractère `car` ; `chr(code)` retourne le caractère correspondant à `code`. Le code de `'a'` est `97`, celui de `'z'` est `122`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def alphabet(sens: str) -> str:
    """Retourne les 26 lettres de l'alphabet dans l'ordre croissant
    si sens vaut 'croissant', dans l'ordre décroissant si sens vaut
    'decroissant'.
    """
    nbre_lettres = 26
    i = 1
    reponse = ""
    if sens == "croissant":
        indice = 97
    elif sens == "decroissant":
        indice = 122
    else:
        raise Exception("Il faut choisir 'croissant' ou 'decroissant'.")
    while i <= nbre_lettres:
        reponse += chr(indice)
        if sens == "croissant":
            indice += 1
        else:
            indice -= 1
        i += 1
    return reponse
```
{{< /solution >}}

### Suites définies par récurrence

{{< question >}}
On rappelle la suite de Fibonacci, définie par $u_1 = 1$, $u_2 = 1$ et, pour $n > 2$, $u_n = u_{n-1} + u_{n-2}$.

Écrire la fonction `fibo` dont la spécification est :

```python
def fibo(n: int) -> str:
    """Retourne les n premiers termes de la suite de Fibonacci,
    sous forme d'une chaîne de caractères.
    """
```

**Indication.** Traiter séparément les cas `n == 1` et `n == 2`, puis utiliser deux variables `u` et `v` qui mémorisent les deux derniers termes calculés.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def fibo(n: int) -> str:
    """Retourne les n premiers termes de la suite de Fibonacci,
    sous forme d'une chaîne de caractères.
    """
    if n == 1:
        return "1"
    elif n == 2:
        return "1 1"
    else:
        u, v = 1, 1
        reponse = "1 1 "
        rang = 3
        while rang <= n:
            w = u + v
            u = v
            v = w
            reponse += f"{w} "
            rang += 1
        return reponse
```
{{< /solution >}}

### Choisir entre for et while

{{< question >}}
Reprendre les fonctions `triple_du_precedent`, `multiplication_multiple_trois`, `multiplication_multiple_sept`, `diviseurs`, `table_multiplication`, `plus_grand_plus_petit`, `moyenne`, `loto_naif` et `alphabet`, et les réécrire à l'aide de l'instruction `for`.

Pourquoi `moyenne_ter` et `devine` ne peuvent-elles pas, elles, être réécrites avec `for` ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def triple_du_precedent(a: int) -> str:
    """Retourne une chaîne de caractères formée d'une suite de 12
    entiers dont chaque terme est le triple du précédent, à partir
    du premier entier a (positif) passé en argument.
    """
    reponse = ""
    val_max_compteur = 12
    for i in range(1, val_max_compteur + 1):
        reponse += f"{a} "
        a *= 3
    return reponse

def multiplication_multiple_trois(a: int) -> str:
    """Retourne les 10 premiers termes de la table de multiplication
    de a, en signalant par un astérisque ceux qui sont multiples de 3.
    """
    reponse = ""
    val_max_compteur = 10
    for compteur in range(1, val_max_compteur + 1):
        valeur = a * compteur
        reponse += f"{valeur}"
        if valeur % 3 == 0:
            reponse += "*"
        reponse += " "
    return reponse

def multiplication_multiple_sept(a: int) -> str:
    """Calcule les 50 premiers termes de la table de multiplication
    de a et retourne une chaîne de caractères contenant uniquement
    les multiples de 7.
    """
    reponse = ""
    val_max_compteur = 50
    for compteur in range(1, val_max_compteur + 1):
        valeur = a * compteur
        if valeur % 7 == 0:
            reponse += f"{valeur} "
    return reponse

def diviseurs(a: int) -> str:
    """Retourne une chaîne de caractères formée de la liste des
    diviseurs de a, de a lui-même jusqu'à 1.
    """
    reponse = ""
    for n in range(a, 0, -1):
        if a % n == 0:
            reponse += f"{n} "
    return reponse

def table_multiplication() -> str:
    """Retourne les tables de multiplication de 1 à 10, chaque table
    étant écrite sur une ligne distincte.
    """
    reponse = ""
    val_max = 10
    for i in range(1, val_max + 1):
        for j in range(1, val_max + 1):
            reponse += f"{i * j} "
        reponse += "\n"
    return reponse

def plus_grand_plus_petit(nbre_valeurs: int) -> str:
    """Demande à l'utilisateur nbre_valeurs valeurs et retourne une
    chaîne de caractères donnant le maximum et le minimum obtenus.
    """
    valeur = float(input("Entrez la valeur 1 : "))
    valeur_plus_grande = valeur
    valeur_plus_petite = valeur
    for i in range(2, nbre_valeurs + 1):
        valeur = float(input(f"Entrez la valeur {i} : "))
        if valeur > valeur_plus_grande:
            valeur_plus_grande = valeur
        elif valeur < valeur_plus_petite:
            valeur_plus_petite = valeur
    return f"max : {valeur_plus_grande}, min : {valeur_plus_petite}"

def moyenne(nbre_notes: int) -> float:
    """Demande à l'utilisateur nbre_notes notes et retourne leur
    moyenne.
    """
    somme = 0
    for i in range(1, nbre_notes + 1):
        note = float(input(f"Entrez la note {i} : "))
        somme += note
    return somme / nbre_notes

def loto_naif() -> str:
    """Retourne 6 entiers sélectionnés aléatoirement dans
    l'intervalle [1, 49].
    """
    import random
    reponse = ""
    nbre_boules = 6
    for i in range(nbre_boules):
        boule = random.randint(1, 49)
        reponse += f"{boule} "
    return reponse

def alphabet(sens: str) -> str:
    """Retourne les 26 lettres de l'alphabet dans l'ordre croissant
    si sens vaut 'croissant', dans l'ordre décroissant si sens vaut
    'decroissant'.
    """
    reponse = ""
    if sens == "croissant":
        indices = range(97, 123)
    elif sens == "decroissant":
        indices = range(122, 96, -1)
    else:
        raise Exception("Il faut choisir 'croissant' ou 'decroissant'.")
    for indice in indices:
        reponse += chr(indice)
    return reponse
```

`moyenne_ter` et `devine` ne peuvent pas être réécrites avec `for` : le nombre d'itérations (le nombre de notes saisies, le nombre de tentatives) n'est pas connu avant l'exécution. Seule une boucle `while` permet d'arrêter une boucle sur un événement imprévisible.
{{< /solution >}}

{{< note success "À retenir" >}}
Le choix entre `for` et `while` dépend de la nature du problème, pas des préférences du programmeur :

- si le nombre d'itérations est **connu avant l'exécution** (un nombre de termes, une taille fixée), `for` est le choix naturel et le plus lisible ;
- si ce nombre **dépend du déroulement de l'exécution** (une saisie jusqu'à une valeur correcte, une recherche jusqu'à un résultat), seule une boucle `while` convient.
{{< /note >}}

### Pour aller plus loin (difficile)

{{< question >}}
**Code ISBN.** Le code ISBN (« International Standard Book Number ») identifie un livre à l'aide de dix chiffres. Le dernier chiffre est une **somme de contrôle**, calculée à partir des neuf premiers : si $d_1, \dots, d_9$ désignent ces neuf chiffres et $d_{10}$ le dixième, la somme $d_1 + 2 d_2 + 3 d_3 + \dots + 10 d_{10}$ doit être un multiple de 11.

Écrire une fonction qui demande à l'utilisateur les neuf premiers chiffres d'un code ISBN et retourne le code complet sous forme d'une chaîne de caractères.
{{< /question >}}

{{< question >}}
**Calendrier.** Écrire une fonction qui affiche un calendrier allant du 1ᵉʳ janvier 2001 au 31 décembre 3000, en indiquant pour chaque jour le nombre de jours écoulés depuis le 1ᵉʳ janvier 2001, le jour de la semaine, le quantième, le mois et l'année.

**Indication.** Une année est bissextile si son millésime est multiple de 4, sauf s'il est multiple de 100 sans être multiple de 400 (1900 n'était pas bissextile, 2000 l'a été).
{{< /question >}}

{{< question >}}
**Le taxi de Ramanujan.** Trouver tous les entiers inférieurs ou égaux à un nombre $N$ choisi par l'utilisateur qui peuvent s'écrire comme somme de deux cubes, de deux façons différentes : trouver quatre entiers $a$, $b$, $c$, $d$, inférieurs à $N$, tels que $a^3 + b^3 = c^3 + d^3$.

**Indication.** Quatre boucles imbriquées suffisent, même si le résultat n'est pas optimisé.
{{< /question >}}

## Bilan : où en suis-je ?

{{< note success "Bilan : où en suis-je ?" >}}
Pour chaque ligne, cochez la colonne qui correspond. Toute case **Pas encore** indique une partie à reprendre.

| **Je sais…** | **Oui** | **Pas encore** | **À revoir** |
|:---|:---|:---|:---|
| distinguer une **boucle déterministe** (`for`) d'une **boucle non déterministe** (`while`) |  |  | Partie 1 |
| écrire une boucle `while` (initialisation, condition d'arrêt, mise à jour) et prévoir si elle peut ne jamais s'exécuter |  |  | Partie 2 |
| « faire tourner une boucle à la main » à l'aide d'un **tableau d'évolution** |  |  | Partie 2 |
| écrire une boucle `for` en utilisant `range` avec un, deux ou trois arguments |  |  | Partie 3 |
| utiliser `break` pour interrompre une boucle et `continue` pour passer à l'itération suivante |  |  | Partie 4 |
| écrire une fonction qui accumule un résultat (chaîne, somme, maximum) au fil d'une boucle |  |  | Partie 5 |
| choisir entre `for` et `while` selon que le nombre d'itérations est connu ou non à l'avance |  |  | Partie 5 |
{{< /note >}}
