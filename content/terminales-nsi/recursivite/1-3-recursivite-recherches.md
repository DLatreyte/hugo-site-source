---
title: "Recherche d'un élément dans un tableau : algorithmes itératifs et récursifs"
subtitle: ""
date: 2020-09-09T21:33:15+04:00
draft: false
toc: true
tags: ["Récursivité", "Recherche linéaire", "Recherche dichotomique", "Complexité", "Terminaison", "Correction"]
categories: ["Informatique", "Terminales Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 103
---

{{< note goal >}}
Écrire les versions itératives et récursives de la recherche séquentielle et de la recherche dichotomique, et justifier leur terminaison, leur correction et leur complexité.
{{< /note >}}

Avant de commencer&nbsp;: on cherche à deviner un nombre entier compris entre 1 et 100, en posant des questions auxquelles on répond seulement «&nbsp;plus grand&nbsp;», «&nbsp;plus petit&nbsp;» ou «&nbsp;trouvé&nbsp;». Quelle stratégie adopter&nbsp;? Combien de questions faut-il, au maximum, avec cette stratégie&nbsp;?

{{< solution "Réponse" >}}
On propose à chaque fois le nombre situé au milieu des valeurs encore possibles&nbsp;: chaque réponse élimine la moitié des candidats. Il reste au plus 50 candidats après la première question, 25 après la deuxième, puis 12, 6, 3, 1. Il faut donc au plus 7 questions, alors qu'en proposant les nombres dans l'ordre, il en faudrait jusqu'à 100. C'est l'idée de la recherche dichotomique.
{{< /solution >}}

## Recherche d'un élément dans un tableau

La recherche d'éléments dans un tableau a déjà été évoquée en classe de première. Les deux algorithmes mis en œuvre à cette occasion, la **recherche linéaire** et la **recherche dichotomique**, utilisaient des boucles.  
L'objectif de cette séance est de rapidement revoir ces algorithmes et de mettre en œuvre des algorithmes récursifs de même complexité. Cinq algorithmes de recherche vont donc être implémentés&nbsp;:

- *La recherche linéaire itérative*, en deux versions&nbsp;;
- *La recherche linéaire récursive*&nbsp;;
- *La recherche dichotomique itérative*&nbsp;;
- *La recherche dichotomique récursive*.

## Travail à faire

- Implémenter en Python les cinq algorithmes suivants et répondre aux questions.
{{< note warning >}}
Penser à donner la **spécification** de chacune des fonctions et écrire une **série de tests** pour chacune d'elles.
{{< /note >}}

## Recherche séquentielle (ou linéaire)

{{< note tip >}}
La **recherche séquentielle (ou linéaire)**  consiste à
*comparer la valeur recherchée à toutes les valeurs présentes dans le tableau*.  
{{< /note >}}

### Recherche séquentielle itérative

{{< note normal >}}

#### Algorithme 1

**Fonction&nbsp;:** recherche(tab, valeur)  
**Action&nbsp;:** recherche la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;»  
**Début**  
<span style="margin-left: 2em">i ⟵ 0  </span><br />
<span style="margin-left: 2em">i_val ⟵ -1  </span><br />
<span style="margin-left: 2em">nb ⟵ Longueur(tab)  </span><br />
<span style="margin-left: 2em">**TantQue** i < nb *Faire*    </span><br />
<span style="margin-left: 4em">**Si** tab[i] = valeur **Alors**  </span><br />
<span style="margin-left: 6em">i_val ⟵ i  </span><br />
<span style="margin-left: 4em">**FinSi**  </span><br />
<span style="margin-left: 4em">i ⟵ i + 1  </span><br />
<span style="margin-left: 2em">**FinTantQue**  </span><br />
<span style="margin-left: 2em">**Renvoyer** i_val  </span><br />
**Fin**  
{{< /note >}}

1. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 8, 3, 5, 9]` et `val = 3`.
{{< solution "Réponse" >}}
`nb` vaut 5. La boucle examine successivement `tab[0]`, `tab[1]`, …, `tab[4]`. Seul `tab[2]` est égal à 3&nbsp;: `i_val` prend la valeur 2 lors du troisième tour. La boucle continue pourtant jusqu'à `i = 5`&nbsp;: elle effectue 5 tours, puis l'algorithme renvoie 2.

Si la valeur est présente plusieurs fois, `i_val` est modifié à chaque occurrence&nbsp;: l'algorithme renvoie l'indice de la **dernière** occurrence.
{{< /solution >}}

2. Démontrer que l'algorithme se termine.
{{< solution "Réponse" >}}
Pour démontrer que l'algorithme se termine il faut définir un variant de boucle car c'est au niveau
de la boucle TantQue qu'un problème peut intervenir.

La fonction dont l'expression est $f(i) = nb -i$ est-elle un variant de boucle ?

- $i$ et $nb$ sont des entiers naturels. De plus la boucle « tourne » tant que $i<nb$.
$f(i)$ est donc un entier naturel.
- $f(i_{k+1}) - f(i_k) = nb - i_{k+1} - ( nb - i_{k} ) = i_{k} - i_{k+1}$. Comme
$i_{k+1} = i_{k} + 1$, $f(i_{k+1}) - f(i_k) = i_{k} - (i_{k} + 1) = -1$. La valeur
de $f$ diminue de 1 à chaque tour : elle est strictement décroissante.

$f$ prend des valeurs entières naturelles et diminue strictement à chaque tour ;
elle ne peut donc diminuer qu'un nombre fini de fois : c'est un variant de boucle.

L'algorithme se termine.
{{< /solution >}}

3. Démontrer que l'algorithme est correct.
{{< solution "Réponse" >}}
Pour déterminer qu'un algorithme qui comporte une boucle est correct, il faut trouver
un invariant de boucle.

L'algorithme 1 ne s'arrête pas quand il trouve la valeur. Un invariant qui convient est&nbsp;: « `i_val` est l'indice de la dernière occurrence de la valeur recherchée parmi les éléments d'indices 0 à $i - 1$, ou $-1$ si elle n'y figure pas. »

- **Initialisation :** avant la première itération, $i = 0$ : aucun élément n'a été examiné et `i_val` vaut $-1$. L'invariant est vrai.
- **Conservation :** supposons l'invariant vrai au début d'un tour. Si `tab[i]` est égal à la valeur, `i_val` prend la valeur $i$, qui est bien l'indice de la dernière occurrence parmi les indices 0 à $i$. Sinon, `i_val` ne change pas, et la dernière occurrence parmi les indices 0 à $i$ est la même que parmi les indices 0 à $i - 1$. Dans les deux cas, après `i ⟵ i + 1`, l'invariant est de nouveau vrai.
- **Conclusion :** la boucle s'arrête quand $i = nb$. L'invariant dit alors que `i_val` est l'indice de la dernière occurrence de la valeur dans tout le tableau, ou $-1$ si elle n'y figure pas. C'est le résultat attendu.
{{< /solution >}}

4. Démontrer que l'algorithme est en O(N).
{{< solution "Réponse" >}}
L'algorithme contient une boucle dont le nombre de tours est toujours
égal au nombre $n$ d'éléments du tableau, et chaque tour effectue un nombre
constant d'opérations. La complexité est donc linéaire, $O(n)$.
{{< /solution >}}

5. Comment pourrait-on améliorer l'efficacité de cet algorithme&nbsp;?
{{< solution "Réponse" >}}
Il faudrait quitter la boucle dès l'instant où la valeur a été trouvée, si elle
est bien présente dans la liste.
{{< /solution >}}

{{< note normal >}}

##### Algorithme 2

**Fonction&nbsp;:** recherche(tab, valeur)  
**Action&nbsp;:** recherche de la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;»  
**Début**  
<span style="margin-left: 2em">trouvé ⟵ Faux  </span><br />
<span style="margin-left: 2em">i ⟵ 0  </span><br />
<span style="margin-left: 2em">nb ⟵ Longueur(tab)  </span><br />
<span style="margin-left: 2em">**TantQue** i < nb et (Non trouvé) **Faire**  </span><br />
<span style="margin-left: 4em">**Si** tab[i] = valeur **Alors**  </span><br />
<span style="margin-left: 8em">trouvé ⟵ Vrai  </span><br />
<span style="margin-left: 4em">**Sinon**  </span><br />
<span style="margin-left: 8em">i ⟵ i + 1  </span><br />
<span style="margin-left: 4em">**FinSi**  </span><br />
<span style="margin-left: 2em">**FinTantQue**  </span><br />
<span style="margin-left: 2em">**Si** trouvé = Vrai **Alors**  </span><br />
<span style="margin-left: 4em">**Renvoyer** i  </span><br />
<span style="margin-left: 2em">**Sinon**  </span><br />
<span style="margin-left: 4em">**Renvoyer** -1  </span><br />
 **Fin**
{{< /note >}}

6. Expliquer pourquoi l'algorithme 2 est plus efficace que l'algorithme 1.
{{< solution "Réponse" >}}
On quitte la boucle dès l'instant où la valeur a été trouvée, si elle
est bien présente dans la liste. Dans le pire des cas (valeur absente ou en
dernière position), les deux algorithmes effectuent $n$ tours ; la complexité
reste en $O(n)$, mais l'algorithme 2 est souvent bien plus rapide.

Attention : l'algorithme 2 renvoie l'indice de la **première** occurrence,
alors que l'algorithme 1 renvoie celui de la dernière.
{{< /solution >}}

### Recherche séquentielle récursive

{{< note normal >}}

#### Algorithme 3

**Fonction&nbsp;:** recherche(tab, valeur, i)  
**Action&nbsp;:** recherche la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;» à l'aide de l'indice i.  
**Début**  
<span style="margin-left: 2em">nb ⟵ **Longueur**(tab)  </span><br />
<span style="margin-left: 2em">**Si** i == nb **Alors**  </span><br />
<span style="margin-left: 4em">**Renvoyer** -1  </span><br />
<span style="margin-left: 2em">**Sinon**    </span><br />
<span style="margin-left: 4em">**Si** tab[i] = valeur **Alors**  </span><br />
<span style="margin-left: 6em">**Renvoyer** i  </span><br />
<span style="margin-left: 4em">**Sinon**  </span><br />
<span style="margin-left: 6em">**Renvoyer** recherche(tab, valeur, i + 1)  </span><br />
<span style="margin-left: 4em">**FinSi**  </span><br />
<span style="margin-left: 2em">**FinSi**  </span><br />
**Fin**  
{{< /note >}}

7. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 8, 3, 5, 9]`, `i = 0` et `val = 3`.  
Établir, en particulier, l'arbre des appels.
{{< solution "Réponse" >}}
- `recherche(tab, 3, 0)` : `tab[0]` vaut 1, différent de 3 ; on appelle `recherche(tab, 3, 1)`.
- `recherche(tab, 3, 1)` : `tab[1]` vaut 8 ; on appelle `recherche(tab, 3, 2)`.
- `recherche(tab, 3, 2)` : `tab[2]` vaut 3 ; cet appel renvoie 2.

L'arbre des appels est une simple chaîne de trois appels. La valeur 2 remonte ensuite telle quelle jusqu'au premier appel : c'est une récursivité terminale.
{{< /solution >}}

## Recherche dichotomique

Dès que le nombre de données devient important, la recherche séquentielle n'est plus envisageable. Sa complexité en $O(N)$ pénalise les autres traitements qui l'utilisent. Il faut diminuer le temps de traitement par l'emploi d'algorithmes plus performants, comme celui de la **recherche dichotomique**.

{{< note tip >}}
La **recherche dichotomique** est basée sur le principe de «&nbsp;diviser pour régner&nbsp;». On divise l'ensemble de recherche en deux sous-ensembles égaux. On détermine ensuite dans quel sous-ensemble doit se trouver la valeur recherchée, puis on poursuit la recherche dans ce sous-ensemble.
{{< /note >}}

{{< note warning >}}
Le préalable à la méthode de recherche dichotomique est de disposer d'un **ensemble trié** de données, car la détermination du sous-ensemble dans lequel se poursuit la recherche se fait par comparaison entre la valeur recherchée et les valeurs de début et de ﬁn du sous-ensemble.
{{< /note >}}

{{< note tip >}}
La division par deux de l'ensemble de données de recherche à chaque appel indique que la complexité est en $O(\log N)$.
{{< /note >}}

### Recherche dichotomique itérative

{{< note normal >}}

#### Algorithme 4

**Fonction&nbsp;:** recherche(tab, valeur)  
**Action&nbsp;:** recherche la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;»  
**Début**
<span style="margin-left: 2em">trouvé ⟵ FAUX  </span><br />
<span style="margin-left: 2em">résultat ⟵ -1  </span><br />
<span style="margin-left: 2em">gauche ⟵ 0  </span><br />
<span style="margin-left: 2em">droite ⟵ **Longueur**(tab) - 1  </span><br />
<span style="margin-left: 2em">**TantQue**  (gauche <= droite) ET (NON trouvé) **Faire** </span><br />
<span style="margin-left: 4em">milieu ⟵ (droite + gauche) // 2 </span><br />
<span style="margin-left: 4em">**Si** tab[milieu] = valeur **Alors**  </span><br />
<span style="margin-left: 6em">résultat ⟵ milieu  </span><br />
<span style="margin-left: 6em">trouvé ⟵ VRAI  </span><br />
<span style="margin-left: 4em">**SinonSi** tab[milieu] < valeur **Alors** </span><br />
<span style="margin-left: 6em">gauche ⟵ milieu + 1  </span><br />
<span style="margin-left: 4em">**Sinon** </span><br />
<span style="margin-left: 6em">droite ⟵ milieu - 1  </span><br />
<span style="margin-left: 4em">**FinSi** </span><br />
<span style="margin-left: 2em">**FinTantQue**  </span><br />
<span style="margin-left: 2em">**Renvoyer** résultat  </span><br />
**Fin**  
{{< /note >}}

8. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 3, 5, 8, 9]` et `val = 3`.
{{< solution "Réponse" >}}
| tour | gauche | droite | milieu | `tab[milieu]` | décision |
|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 4 | 2 | 5 | $5 > 3$ : droite ⟵ 1 |
| 2 | 0 | 1 | 0 | 1 | $1 < 3$ : gauche ⟵ 1 |
| 3 | 1 | 1 | 1 | 3 | trouvé : résultat ⟵ 1 |

La boucle s'arrête après 3 tours et l'algorithme renvoie 1.
{{< /solution >}}

9. Démontrer que l'algorithme se termine.
{{< solution "Réponse" >}}

- **Variant de boucle :** $f(g, d) = d - g + 1$ où $d$ signifie « droite » et $g$ « gauche ».
- Au début, $g = 0$ et $d = n-1$ (où $n$ est la taille du tableau).
Le variant initial est donc $n$, qui est un entier naturel.
- À chaque itération, on a trois cas :
  - Si l'élément est trouvé, la boucle se termine.
  - Si l'élément cherché est plus grand que le milieu, on met à jour $g = m + 1$
  - Si l'élément cherché est plus petit que le milieu, on met à jour $d = m - 1$
Dans les deux derniers cas, la taille de l'intervalle est réduite de moitié (ou presque).
Donc, le variant diminue strictement à chaque itération.

Comme $g \leqslant d + 1$ à chaque étape, le variant est un entier naturel. Il diminue strictement à chaque itération, et la boucle s'arrête au plus tard quand il atteint 0 (intervalle vide, $g > d$). L'algorithme se termine donc toujours en un nombre fini d'étapes.

{{< /solution >}}

10. Démontrer que l'algorithme est correct.
{{< solution "Réponse" >}}
**Invariant de boucle :** À chaque itération de la boucle, l'élément recherché, s'il est présent dans le tableau, se trouve dans la sous-section de l'intervalle [gauche, droite], où :

- gauche est l'indice de début de l'intervalle actuel,
- droite est l'indice de fin de l'intervalle actuel.

- **Initialisation (avant la première itération)**

Initialement, les indices gauche et droite sont positionnés de telle sorte que :

- gauche = 0, qui représente le premier indice du tableau.
- droite = n - 1, qui représente le dernier indice du tableau.
Ainsi, avant la première itération, l'élément recherché se trouve potentiellement dans l'intervalle entier du tableau [0, n - 1], ce qui respecte bien l'invariant de boucle.

Conclusion : L'invariant est vérifié avant la première itération.

- **Conservation (pendant l'itération)**

Supposons que l'invariant soit vrai au début d'une itération, c'est-à-dire que si l'élément recherché est présent, il se trouve dans l'intervalle [gauche, droite].

L'algorithme calcule ensuite l'indice médian : milieu

Il compare l'élément à l'indice milieu avec l'élément recherché x :

- *Si l'élément au milieu est égal à x :* L'algorithme s'arrête, et l'élément est trouvé, ce qui n'est pas en contradiction avec l'invariant.
- *Si l'élément au milieu est strictement inférieur à x :* L'algorithme met à jour la borne gauche : gauche = milieu + 1
Cela signifie que x ne peut pas se trouver dans la sous-partie gauche du tableau (de l'indice gauche à milieu), car les éléments dans cette partie sont tous inférieurs à x. Par conséquent, l'élément recherché, s'il existe, se trouve dans le nouvel intervalle [gauche, droite], et l'invariant est préservé.
- *Si l'élément au milieu est strictement supérieur à x :* L'algorithme met à jour la borne droite : droite = milieu − 1
Cela signifie que x ne peut pas se trouver dans la sous-partie droite du tableau (de milieu à droite), car les éléments dans cette partie sont tous supérieurs à x. Par conséquent, l'élément recherché, s'il existe, se trouve dans le nouvel intervalle [gauche, droite], et l'invariant est préservé.

Conclusion : L'invariant est préservé à chaque itération.

- **Terminaison**

La boucle se termine lorsque l'intervalle devient vide, c'est-à-dire lorsque gauche > droite. Cela signifie que l'élément recherché n'existe pas dans le tableau (sinon, il aurait été trouvé lors des itérations précédentes).

Ainsi, lorsque l'algorithme se termine :

- Soit il a trouvé l'élément recherché, ce qui est cohérent avec l'invariant.
- Soit l'intervalle est vide, et donc l'élément n'est pas présent dans le tableau, ce qui est également conforme à l'invariant, car l'invariant stipule seulement que si l'élément est présent, il se trouve dans l'intervalle.

Conclusion : À la fin de l'algorithme, l'invariant reste valide et garantit que le résultat final est correct.
{{< /solution >}}

11. Démontrer que l'algorithme est en $O(\log_2 N)$.
{{< solution "Réponse" >}}
L'algorithme fonctionne en divisant l'intervalle de recherche par 2 à chaque itération. Ainsi, si le tableau contient $n$ éléments, après une itération, la taille de l'intervalle est réduite à $n/2$, puis $n/4$, et ainsi de suite. En général, après $k$ itérations, la taille de l'intervalle est réduite à $n / 2^k$.

Dans le pire des cas, la boucle continue tant que l'intervalle n'est pas vide. Après $k$ itérations, il contient au plus $n / 2^k$ éléments ; il ne contient plus qu'un élément quand $2^k \geqslant n$, c'est-à-dire pour $k \geqslant \log_2(n)$, et une dernière itération suffit alors à conclure. L'algorithme effectue donc au plus $\lfloor \log_2(n) \rfloor + 1$ itérations : pour $n = 5$, au plus 3 ; pour un million d'éléments, au plus 20. La complexité est en $O(\log_2 n)$.
{{< /solution >}}

### Recherche dichotomique récursive

{{< note normal >}}

#### Algorithme 5

**Fonction&nbsp;:** recherche(tab, valeur, gauche, droite)  
**Action&nbsp;:** recherche la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;»  
**Début**
<span style="margin-left: 2em">**Si** gauche > droite **Alors**  </span><br />
<span style="margin-left: 4em">**Renvoyer** -1  </span><br />
<span style="margin-left: 2em">**Sinon**  </span><br />
<span style="margin-left: 4em">milieu ⟵ (droite + gauche) // 2 </span><br />
<span style="margin-left: 4em">**Si** tab[milieu] = valeur **Alors**  </span><br />
<span style="margin-left: 6em">**Renvoyer** milieu  </span><br />
<span style="margin-left: 4em">**SinonSi**  tab[milieu] < valeur </span><br />
<span style="margin-left: 6em">**Renvoyer** recherche(tab, valeur, milieu + 1, droite)</span><br />
<span style="margin-left: 4em">**Sinon**  </span><br />
<span style="margin-left: 6em">**Renvoyer** recherche(tab, valeur, gauche, milieu - 1) </span><br />
<span style="margin-left: 4em">**FinSi** </span><br />
<span style="margin-left: 2em">**FinSi** </span><br />
**Fin**  
{{< /note >}}

12. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 3, 5, 8, 9]`, `gauche = 0`, `droite = 4`, et `val = 3`.
{{< solution "Réponse" >}}
- `recherche(tab, 3, 0, 4)` : milieu vaut 2 et `tab[2]` vaut 5, plus grand que 3 ; on appelle `recherche(tab, 3, 0, 1)`.
- `recherche(tab, 3, 0, 1)` : milieu vaut 0 et `tab[0]` vaut 1, plus petit que 3 ; on appelle `recherche(tab, 3, 1, 1)`.
- `recherche(tab, 3, 1, 1)` : milieu vaut 1 et `tab[1]` vaut 3 ; cet appel renvoie 1.

On retrouve exactement les étapes de l'algorithme itératif : chaque tour de boucle est remplacé par un appel récursif.
{{< /solution >}}

### Programmes Python

{{< solution "Solution" >}}

```python
def recherche_1(tab: list[int], valeur: int) -> int:
    """
    Algorithme 1 : retourne l'indice de la dernière occurrence de valeur
    dans tab, ou -1 si valeur n'est pas dans tab.

    >>> recherche_1([1, 8, 3, 5, 9], 3)
    2
    >>> recherche_1([3, 8, 3], 3)
    2
    >>> recherche_1([1, 8, 3, 5, 9], 4)
    -1
    """
    i = 0
    i_val = -1
    nb = len(tab)
    while i < nb:
        if tab[i] == valeur:
            i_val = i
        i += 1
    return i_val


def recherche_2(tab: list[int], valeur: int) -> int:
    """
    Algorithme 2 : retourne l'indice de la première occurrence de valeur
    dans tab, ou -1 si valeur n'est pas dans tab.

    >>> recherche_2([1, 8, 3, 5, 9], 3)
    2
    >>> recherche_2([3, 8, 3], 3)
    0
    >>> recherche_2([1, 8, 3, 5, 9], 4)
    -1
    """
    trouve = False
    i = 0
    nb = len(tab)
    while i < nb and not trouve:
        if tab[i] == valeur:
            trouve = True
        else:
            i += 1
    if trouve:
        return i
    else:
        return -1


def recherche_3(tab: list[int], valeur: int, i: int = 0) -> int:
    """
    Algorithme 3 (récursif) : retourne l'indice de la première occurrence
    de valeur dans tab à partir de l'indice i, ou -1.

    >>> recherche_3([1, 8, 3, 5, 9], 3)
    2
    >>> recherche_3([1, 8, 3, 5, 9], 4)
    -1
    """
    if i == len(tab):
        return -1
    elif tab[i] == valeur:
        return i
    else:
        return recherche_3(tab, valeur, i + 1)


def recherche_4(tab: list[int], valeur: int) -> int:
    """
    Algorithme 4 (dichotomie itérative) : retourne un indice de valeur
    dans le tableau trié tab, ou -1 si valeur n'est pas dans tab.

    >>> recherche_4([1, 3, 5, 8, 9], 3)
    1
    >>> recherche_4([1, 3, 5, 8, 9], 4)
    -1
    """
    trouve = False
    resultat = -1
    gauche = 0
    droite = len(tab) - 1
    while gauche <= droite and not trouve:
        milieu = (gauche + droite) // 2
        if tab[milieu] == valeur:
            resultat = milieu
            trouve = True
        elif tab[milieu] < valeur:
            gauche = milieu + 1
        else:
            droite = milieu - 1
    return resultat


def recherche_5(tab: list[int], valeur: int, gauche: int, droite: int) -> int:
    """
    Algorithme 5 (dichotomie récursive) : retourne un indice de valeur
    dans tab[gauche..droite] (tableau trié), ou -1.

    >>> recherche_5([1, 3, 5, 8, 9], 3, 0, 4)
    1
    >>> recherche_5([1, 3, 5, 8, 9], 4, 0, 4)
    -1
    """
    if gauche > droite:
        return -1
    milieu = (gauche + droite) // 2
    if tab[milieu] == valeur:
        return milieu
    elif tab[milieu] < valeur:
        return recherche_5(tab, valeur, milieu + 1, droite)
    else:
        return recherche_5(tab, valeur, gauche, milieu - 1)
```

{{< /solution >}}

## Application

{{< note exercise >}}
Écrire un programme de devinette&nbsp;: l'utilisateur choisit un nombre au hasard (compris entre 1 et 50) et l'ordinateur doit découvrir ce nombre. Faire en sorte que le nombre de tentatives de l'ordinateur lui permette de trouver la bonne valeur à coup sûr (choisir de façon pertinente ce nombre).
{{< /note >}}

{{< note tip "Coup de pouce" >}}
L'utilisateur répond à chaque proposition par `+` (le nombre est plus grand), `-` (il est plus petit) ou `=` (trouvé). L'ordinateur garde en mémoire les bornes `gauche` et `droite` des valeurs encore possibles, comme dans l'algorithme 4. Combien de valeurs reste-t-il, au plus, après 1, 2, 3… tentatives&nbsp;?
{{< /note >}}

{{< solution "Solution" >}}

Après chaque tentative, il reste au plus la moitié des valeurs possibles : 50, puis 25, 12, 6, 3 et 1. Six tentatives suffisent donc toujours ($2^6 = 64 > 50$, alors que $2^5 = 32 < 50$).

```python
def devinette(minimum: int = 1, maximum: int = 50) -> None:
    """
    L'ordinateur devine un nombre choisi par l'utilisateur entre minimum
    et maximum, par dichotomie. L'utilisateur répond +, - ou =.
    """
    gauche, droite = minimum, maximum
    tentatives = 0
    while gauche <= droite:
        milieu = (gauche + droite) // 2
        tentatives += 1
        reponse = input(f"Je propose {milieu}. Réponse (+, - ou =) : ")
        if reponse == "=":
            print(f"Trouvé en {tentatives} tentative(s) !")
            return
        elif reponse == "+":
            gauche = milieu + 1
        else:
            droite = milieu - 1
    print("Vos réponses sont contradictoires.")


if __name__ == "__main__":
    devinette()
```

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- programmer la recherche séquentielle et la recherche dichotomique, en version itérative et en version récursive ;
- dérouler à la main ces algorithmes sur un exemple et établir un arbre des appels ;
- prouver la terminaison d'une boucle à l'aide d'un variant ;
- prouver la correction d'une boucle à l'aide d'un invariant ;
- justifier qu'une recherche séquentielle est en $O(n)$ et qu'une recherche dichotomique est en $O(\log_2 n)$ ;
- expliquer pourquoi la recherche dichotomique exige un tableau trié.
{{< /note >}}
