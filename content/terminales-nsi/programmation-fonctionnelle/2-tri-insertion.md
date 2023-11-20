---
title: "Tri par insertion"
subtitle: "Chapitre 5,2"
author: ""
type: ""
date: 2020-10-07T21:53:32+04:00
draft: false
toc: true
tags: ["Tri", "Récursivité", "Fonction"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Objectifs

> Le tri par insertion a été étudié en classe de 1ère. Dans ce document, après un rappel du cours de 1ère, nous allons implémenter une *version récursive* de cet algorithme et ensuite utiliser la possibilité que les fonctions en Python ont d'accepter des fonctions comme paramètres, afin de *rendre plus générale et utile* cette fonction de tri.

## Tri du joueur de cartes

<img src="/terminales-nsi/chap-5/chap-5-2-1.jpg" alt="" width="40%" style="float: right;" />
Le tri par insertion est un tri « naturel » souvent qualifié de « tri du joueur de carte ». Comment un joueur de carte fait-il pour trier les cartes ?
-  Au début, la main gauche du joueur est vide et ses cartes sont posées sur la table.
-  Le joueur prend alors sur la table les cartes, une par une avec sa main droite, pour les placer dans sa main gauche.
-  Pour savoir où placer une carte dans son jeu, le joueur la compare avec chacune des cartes déjà présentes dans sa main gauche, *en examinant les cartes de la droite vers la gauche*.
-  *À tout moment, les cartes tenues par la main gauche sont triées* ; ces cartes étaient, à l'origine, les cartes situées au sommet de la pile sur la table. 

## Tri par insertion

{{% note warning %}}
Une correction du code à développer ci-dessous se trouve {{< remote "ici" "https://repl.it/@dlatreyte/triparinsertion" >}}
{{% /note %}}

### Introduction

La méthode du tri par insertion est ilustré à {{< remote "ici" "https://youtu.be/K4CuPzdiAIo" >}}, ou, de façon plus folklorique, {{< remote "ici" "https://youtu.be/ROalU379l3U" >}}.

1. Visualiser la première vidéo (s'arrêter au bout de 4min40). Essayer de bien comprendre la méthode.

### Algorithme itératif

Le tri par insertion est efficace lorsqu'on cherche à trier un tableau contenant un petit nombre d'élements ou un tableau dans lequel les éléments sont déjà pratiquement triés.

{{% note tip %}}
#### Idée
À chaque étape du processus, le tableau est divisé en deux sous-tableaux : le premier (indices plus petits que l'indice courant) est trié, le second (indices plus grands que l'indice courant n'est pas encore trié). On cherche la place de l'élément courant (non encore trié) dans le tableau trié.

Le tri par insertion est basé sur l'*utilisation de deux boucles imbriquées* :
- La première boucle, une boucle `Pour`, *parcourt la liste des valeurs, de la deuxième à la dernière* ;
-  La seconde boucle, une boucle `TantQue`, *cherche à placer l'élément courant dans la première partie triée du tableau* (indices inférieurs à l'indice courant). 
{{% /note %}}

{{% note normal %}}
#### Algorithme 1
**Fonction** tri_iter

**Déclaration**</span><br />
<span style="margin-left: 2em">**Paramètre** tab : tableau d'Entiers</span><br />
<span style="margin-left: 2em">**Variables** nb, i, j, clé : Entiers</span><br />

**Début**</span><br />
1.<span style="margin-left: 2em">nb ⟵ **len**(tab)</span><br />
2.<span style="margin-left: 2em">**Pour** i variant de 1 à nb-1 **Faire**</span><br />
3.<span style="margin-left: 4em">clé ⟵ tab[i]</span><br />
4.<span style="margin-left: 4em">j ⟵ i - 1</span><br />
5.<span style="margin-left: 4em">**TantQue** j >= 0 et tab[j] > clé **Faire**</span><br />
6.<span style="margin-left: 6em">tab[j + 1] ⟵ tab[j]</span><br />
7.<span style="margin-left: 6em">j ⟵ j - 1</span><br />
8.<span style="margin-left: 4em">**FinTantQue**</span><br />
9.<span style="margin-left: 4em">tab[j + 1] ⟵ clé</span><br />
10.<span style="margin-left: 2em">**FinPour**</span><br />
**Fin**

{{% /note %}}

**Remarque.** L'algorithme du tri par insertion est un algorithme de tri en place. La réorganisation du tableau ne nécessite pas la création d'un nouveau tableau, ce qui économise de la place en mémoire.

2. Faire tourner « à la main » l'algorithme lorsque la fonction reçoit le tableau `tab = [5,2,4,6,1,3]`.

3. À quoi sert l'instruction, ligne 2 ?

4. Expliquer les conditions d'arrêt de la boucle `while`, ligne 5.

5. Implémenter la fonction en langage Python et la tester en l'appelant avec les arguments donnés à la question précédente.
{{% solution "Réponse" %}}
```python
def tri(tab: List[int]) -> List[int]:
    """
    Implémentation du tri par insertion.
    Algorithme itératif.
    """
    for i in range(1, len(tab)):
        val = tab[i]
        j = i - 1
        while tab[j] > val and j >= 0:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = val

    return tab
```
{{% /note %}}

6. Comment prouve-t-on, de façon générale, la terminaison d'un algorithme ?
{{% solution "Réponse" %}}
On définit un variant de boucle.
{{% /solution %}}

7. Est-il nécessaire de prouver la terminaison de la boucle externe de cet algorithme ? De la boucle interne ?
{{% solution "Réponse" %}}
La boucle externe est une boucle Pour. Il n'est donc pas nécessaire de prouver sa terminaison. Par contre la boucle interne est une boucle TantQue. Il faut donc prouver sa terminaison.
{{% /solution %}}

8. Démontrer la terminaison de cet algorithme.
{{% solution "Réponse" %}}
La fonction $f$ définie par $f(j) = j$ est-elle un variant de boucle ?

- Première valeur de $j$ : $i-1$, donc première valeur de $f$ : $f(j) = i - 1 >0$ puisque $i > 1$.
- $f$ est-elle décroissante ?   
    $f\_{j+1} - f\_{j} = j-1 - j = -1$, La fonction est bien décroissante.
- Dernière valeur de $j$ : $-1$, donc $f(j) = -1$.
$f$ est une fonction positive, décroissante dont la dernière valeur est négative : c'est bien un variant de boucle. La boucle se termine.
{{% /solution %}}

9. Comment prouve-t-on, de façon générale, la correction d'un algorithme ?
{{% solution "Réponse" %}}
On recherche un invariant de boucle.
{{% /solution %}}

10. Définir un invariant de boucle et prouver que l'algorithme est correct.
{{% solution "Réponse" %}}
#### Invariant de boucle.
La question à se poser est : « Qu'est ce qui est constant à chaque étape de cet algorithme ? »    
Au début de chaque itération de la boucle Pour externe le tableau `tab[0, ... , i-1]` est un tableau trié constitué des i plus petits éléments du tableau `tab`, dans l'ordre croissant.

#### Rappels.
Nous devons montrer trois choses, concernant un invariant de boucle :
- **Initialisation.** Il est vrai avant la première itération de la boucle.
- **Conservation.** S'il est vrai avant une itération de la boucle, il le reste avant l'itération suivante.
- **Terminaison.** Une fois terminée la boucle, l'invariant fournit une propriété utile qui aide à montrer la validité de l'algorithme.

Si les deux premières propriétés sont vérifiées, alors l'invariant est vrai avant chaque itération de la boucle.    
La troisième propriété est peut-être la plus importante : elle est utilisée pour prouver la validité de l'algorithme.

#### Démonstration de la correction de l'algorithme. 

**Initialisation.** `i=1`, `tab[0]` est alors un tableau à un élément, trié de façon évidente.

**Conservation.** Par hypothèse, pour `i` compris entre 1 et `nb-2`, `tab[0,  ,i-1]` est un tableau trié. Lors de l'itération `i`, on recherche le plus petit élément du tableau `tab[i, ... ,nb-1]` et on le place à la position d'indice `i`. À partir de l'hypothèse, cet élément est plus grand que n'importe quel élément du tableau `tab[0,  ,i-1]` (sinon il appartiendrait déjà à ce tableau) ; le tableau `tab[0, ... ,i]` est donc trié.

**Terminaison.** Au début de la boucle dans laquelle `i=nb-2, tab[0, ... ,nb-3]` est un tableau trié. À l'issue de cette boucle, on a déterminé le plus petit élément entre `tab[nb-2]` et `tab[nb-1]` et on a placé correctement ces éléments ; le tableau `tab[0, ... ,nb-1]` est donc trié et l'algorithme est correct. 
{{% /solution %}}

11. Déterminer la complexité de l'algorithme.
{{% solution "Réponse" %}}
#### Rappels. 
Au chapitre précédent, la notion de complexité a été introduite. Nous allons rappeller, dans cette partie, quelques règles simples qui permettent de se faire une idée de l'efficacité d'un algorithme.
-  Une affectation ou l'évaluation d'une expression ont un temps d'exécution petit que l'on considère constant. Cette durée constitue souvent l'unité de base dans laquelle on mesure le temps d'exécution d'un algorithme.
-  Le temps pris pour exécuter une séquence d'instructions `p` puis `q` est la somme des temps pris pour exécuter les instructions `p` puis `q`.
-  Le temps pris pour exécuter un test `Si (b) Alors p Sinon q FinSi` est inférieur ou égal au maximum des temps pris pour exécuter les instructions `p` et `q`, plus une unité qui correspond au temps d'évaluation de l'expression `b`.
-  Le temps pris pour exécuter une boucle `Pour i variant de 1 à m par pas de 1 Faire p FinPour` est m fois le temps pris pour exécuter l'instruction `p` si ce temps ne dépend pas de la valeur de i.   
En particulier, quand deux boucles sont imbriquées, le corps de la boucle interne est répété à cause de cette boucle, mais aussi parce qu'elle-même est répétée dans son intégralité. Ainsi, si les deux boucles sont répétées respectivement m et m' fois, alors le corps de la boucle interne est exécuté m * m' fois en tout.   
Quand le temps d'exécution du corps de la boucle dépend de la valeur de l'indice i, le temps total d'exécution de la boucle est la somme des temps d'exécution du corps de la boucle pour chaque valeur de i.
-  Le cas des boucles `Tantque` est plus complexe puisque le nombre d'itérations n'est en général pas connu à priori.

On étudie seulement la complexité du pire et **on se limite à l'influence des boucles**. Si on note $N$ le nombre d'élements dans le tableau, 
-  pour $i=0$, la boucle interne effectue $N-1$ tours ;
-  pour $i=1$, la boucle interne effectue $N-2$ tours ;
-  pour $i=3$, la boucle interne effectue $N-3$ tours ;
-    
-  pour $i=N-3$, la boucle interne effectue 2 tours ;
-  pour $i=N-2$, la boucle interne effectue 1 tour.

Finalement, il y a $1+2+\ldots+(N-2)+(N-1)=\sum_{k=1}^{N-1} k=\dfrac{(N-1)*N}{2}=\dfrac{N^2}{2}-\dfrac{N}{2}$. La complexité de l'algorithme est en $O(N^2)$.
{{% /solution %}}

## Algorithme récursif

{{% note normal %}}
#### Algorithme 2
**Fonction** tri_rec

**Déclaration**</span><br />
<span style="margin-left: 2em">**Paramètre** tab : tableau d'Entiers</span><br />
<span style="margin-left: 2em">**Paramètre** i : Entier</span><br />
<span style="margin-left: 2em">**Variable** nb : Entier</span><br />

**Début**</span><br />
1.<span style="margin-left: 2em">nb ⟵ **len**(tab)</span><br />
2.<span style="margin-left: 2em">**Si** i == nb **Alors**</span><br />
3.<span style="margin-left: 4em">**Retourner** tab</span><br />
4.<span style="margin-left: 2em">**Sinon**</span><br />
5.<span style="margin-left: 4em">insere(tab, i)</span><br />
6.<span style="margin-left: 4em">**Retourner** tri_rec(tab, i + 1)</span><br />
7.<span style="margin-left: 2em">**FinSi**</span><br />
**Fin**
{{% /note %}}

{{% note normal %}}
#### Algorithme 3
**Fonction** insere

**Déclaration**</span><br />
<span style="margin-left: 2em">**Paramètre** tab : tableau d'Entiers</span><br />
<span style="margin-left: 2em">**Paramètre** i : Entier</span><br />
<span style="margin-left: 2em">**Variable** temp : Entier</span><br />

**Début**</span><br />
1.<span style="margin-left: 2em">**Si** i == 0 **ou** tab[i - 1] <= tab[i] **Alors**</span><br />
2.<span style="margin-left: 4em">**Retourner** tab[i]</span><br />
3.<span style="margin-left: 2em">**Sinon**</span><br />
4.<span style="margin-left: 4em">temp ⟵ tab[i - 1]</span><br />
5.<span style="margin-left: 4em">tab[i - 1] ⟵ tab[i]</span><br />
6.<span style="margin-left: 4em">tab[i] ⟵ temp</span><br />
7.<span style="margin-left: 4em">**Retourner** insere(tab, i - 1)</span><br />
7.<span style="margin-left: 2em">**FinSi**</span><br />
**Fin**
{{% /note %}}

12. Décrire le fonctionnement de l'algorithme récursif avec soin lorsque la fonction reçoit le tableau `tab = [5,2,4,6,1,3]`.

13. Implémenter en Python l'algorithme récursif.
{{% solution "Réponse" %}}
```python
def tri_rec(tab: List[int], i: int = 1) -> List[int]:
    """
    Implémentation du tri par insertion
    """
    if i == len(tab):
        return tab
    else:
        insere(tab, i)
        return tri_rec(tab, i + 1)


def insere(tab: List[int], i: int) -> List[int]:
    """
    Insère tab[i] dans le tableau tab[:i] déjà trié, récursivement.
    """
    if i == 0 or tab[i - 1] <= tab[i]:
        return tab[i]
    else:
        temp = tab[i - 1]
        tab[i - 1] = tab[i]
        tab[i] = temp
        return insere(tab, i - 1)
```
{{% /solution %}}

## Ajout d'une fonctionnalité au tri par insertion

Le tri par insertion, tel que nous l'avons implémenté, permet de trier des tableaux contenant tous les objets qui admettent `<` comme opérateur : `int`, `float`, `str`, ... mais aussi `tuple` !!!

12. Vérifier que la fonction `tri_rec` est bien capable de trier la liste `[(7, 8), (3, 4), (1, 2), (5, 6)]`.   
Quel est le critère de tri ?

> Comment doit-on modifier nos fonctions de tri pour qu'elles trient par ordre décroissant ? Pour qu'elles trient le second élément de tuples passés comme arguments ?

**Exemple de problème à traiter :** Trier la liste suivante par année de naissance (ordre croissant)
```python
eleves = [("Brian", 1, 1, 1942),
            ("Grace", 9, 12, 1906),
            ("Linus", 28, 12, 1969),
            ...]
```

{{% note normal %}}
L'idée est de confier la relation d'ordre à une fonction auxiliaire que l'on passe comme argument à la fonction de tri.   
Cette fonction auxiliaire doit être un prédicat.
{{% /note %}}

13. Modifier les fonction `tri-rec` et `insere` de façon à ce qu'elles admettent la fonction `inf` comme argument. La fonction `inf` est responsable de la relation d'ordre lors du tri.
{{% solution "Réponse" %}}
```python
def tri_g(inf: Callable, tab: List[int], i: int = 1) -> List[int]:
    """
    Implémentation d'un algorithme générique de tri par insertion. 
    Algorithme récursif.
    """
    if i == len(tab):
        return tab
    else:
        insere_g(inf, tab, i)
        return tri_g(inf, tab, i + 1)


def insere_g(inf: Callable, tab: List[int], i: int) -> List[int]:
    """
    Insère tab[i] dans le tableau tab[:i] déjà trié, récursivement.
    """
    if i == 0 or inf(tab[i], tab[i - 1]):
        return tab[i]
    else:
        temp = tab[i - 1]
        tab[i - 1] = tab[i]
        tab[i] = temp
        return insere_g(inf, tab, i - 1)
```
{{% /solution %}}

14. Écrire une fonction `inf` qui permet de trier un tableau d'entiers par ordre croissant.
{{% solution "Réponse" %}} 
```python
def infe(x, y):
    """
    Relation d'ordre générique.
    Pas vraiment possible de donner les types.
    """
    return y <= x
```
{{% /solution %}}

15. Modifier la fonction `inf` de façon à ce que le tableau soit trié par ordre décroissant.



