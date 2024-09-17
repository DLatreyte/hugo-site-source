---
title: "Recherche d'un élément dans un tableau : algorithmes itératifs et récursifs"
subtitle: ""
author: ""
type: ""
date: 2020-09-09T21:33:15+04:00
draft: false
toc: true
tags: ["Récursivité", "Recherche linéaire", "Recherche dichotomique", "Complexité", "Terminaison", "Correction"]
categories: ["Informatique", "Terminales Spé NSI"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Recherche d'un élément dans un tableau

La recherche d'éléments dans un tableau a déjà été évoquée en classe de première. Les deux algorithmes mis en œuvre à cette occasion, la **recherche linéaire** et la **recherche dichotomique**, utilisaient des boucles.  
L'objectif de cette séance est de rapidement revoir ces algorithmes et de mettre en œuvres des algorithmes récursifs de même complexité. Quatre algorithmes de recherche vont donc être implémentés&nbsp;:

- *La recherche linéaire itérative*&nbsp;;
- *La recherche linéaire récursive*&nbsp;;
- *La recherche dichotomique itérative*&nbsp;;
- *La recherche dichotomique récursive*.

## Travail à faire

- Implémenter en Python les cinq algorithmes suivants et répondre aux questions.
{{% note warning %}}
Penser à donner la **spécification** de chacune des fonctions et écrire une **série des tests** pour chacune d'elles.
{{% /note %}}
<!--
- Un corrigé se trouve à cette adresse&nbsp;: {{< remote "<https://repl.it/join/azqimfmv-dlatreyte>" "<https://repl.it/join/azqimfmv-dlatreyte">}}>
-->

## Recherche séquentielle (ou linéaire)

{{% note tip %}}
La **recherche séquentielle (ou linéaire)**  consiste à
*comparer la valeur recherchée à toutes les valeurs présentes dans le tableau*.  
{{% /note %}}

### Recherche séquentielle itérative

{{% note normal %}}

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
{{% /note %}}

1. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 8, 3, 5, 9]` et `val = 3`.
{{% solution "Réponse" %}}

{{% /solution %}}

2. Démontrer que l'algorithme se termine.
{{% solution "Réponse" %}}
Pour démontrer que l'algorithme se termine il faut définir un variant de boucle car c'est au niveau
de la boucle TantQue qu'un problème peut intervenir.

La fonction dont l'expression est $f(i) = nb -i$ est-elle un variant de boucle ?

- $i$ et $nb$ sont des entiers naturels. De plus la boucle « tourne » tant que $i<nb$.
$f(i)$ est donc un entier naturel.
- $f(i_{k+1}) - f(i_k) = nb - i_{k+1} - ( nb - i_{k} ) = i_{k} - i_{k+1}$. Comme
$i_{k+1} = i_{k} + 1$, $f(i_{k+1}) - f(i_k) = i_{k} - (i_{k} + 1) = -1$. La fonction
est décroissante.

$f$ est une fonction qui retourne forcément un entier naturel et qui est décroissante ;
elle est donc bornée par la valeur 0, c'est un variant de boucle.

L'algorithme se termine.
{{% /solution %}}

3. Démontrer que l'algorithme est correct.
{{% solution "Réponse" %}}
Pour déterminer qu'un algorithme qui comporte une boucle est correct, il faut trouver
un invariant de boucle.

On peut par exemple dire que « La valeur recherchée n'est pas présente dans les éléments du tableau d'indices 0 à i-1, où i est l'indice courant. »

- **Initialisation :** Avant la première itération, $i = 0$, donc l'invariant est vrai trivialement car aucun élément n'a encore été examiné.
- **Conservation :** À chaque itération, on vérifie si l'élément à l'indice $i$ est la valeur recherchée. Si ce n'est pas le cas, on passe à l'élément suivant $(i + 1)$. Ainsi, on sait que la valeur recherchée n'est pas dans les éléments précédents.
- **Terminaison :** La boucle se termine soit quand on trouve la valeur (auquel cas l'invariant n'est plus nécessaire), soit quand on a parcouru tout le tableau sans la trouver (auquel cas l'invariant assure que la valeur n'est pas dans le tableau).
{{% /solution %}}

4. Démontrer que l'algorithme est en O(N).
{{% solution "Réponse" %}}
L'algorithme contient une boucle dont le nombre de tours est, dans le pire des cas,
égal au nombre d'éléments dans la liste. La complexité est donc linéaire, $O(n)$.
{{% /solution %}}

5. Comment pourrait-on améliorer l'efficacité de cet algorithme&nbsp;?
{{% solution "Réponse" %}}
Il faudrait quitter la boucle dès l'instant où la valeur a été trouvée, si elle
est bien présente dans la liste.
{{% /solution %}}

{{% note normal %}}

##### Algorithme 2

**Fonction&nbsp;:** recherche(tab, valeur)  
**Action&nbsp;:** recherche de la valeur «&nbsp;valeur&nbsp;» dans le tableau «&nbsp;tab&nbsp;»  
**Début**  
<span style="margin-left: 2em">trouvé ⟵ Faux  </span><br />
<span style="margin-left: 2em">i ⟵ 0  </span><br />
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
{{% /note %}}

6. Expliquer pourquoi l'algorithme 2 est plus efficace que l'algorithme 1.
{{% solution "Réponse" %}}
On quitte la boucle dès l'instant où la valeur a été trouvée, si elle
est bien présente dans la liste.
{{% /solution %}}

### Recherche séquentielle récursive

{{% note normal %}}

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
{{% /note %}}

7. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 8, 3, 5, 9]`, `i = 0` et `val = 3`.  
Établir, en particulier, l'arbre des appels.

## Recherche dichotomique

Dès que le nombre de données devient important, la recherche séquentielle n'est plus envisageable. Sa complexité en $O(N)$ pénalise les autres traitements qui l'utilisent. Il faut diminuer le temps de traitement par l'emploi d'algorithmes plus performants, comme celui de la **recherche dichotomique**.

{{% note tip %}}
La **recherche dichotomique** est basée sur le principe de «&nbsp;diviser pour régner&nbsp;». On divise l'ensemble de recherche en deux sous-ensembles égaux. On détermine ensuite dans quel sous-ensemble doit se trouver la valeur recherchée, puis on poursuit la recherche dans ce sous-ensemble.
{{% /note %}}

{{% note warning %}}
Le préalable à la méthode de recherche dichotomique est de disposer d'un **ensemble trié** de données, car la détermination du sous-ensemble dans lequel se poursuit la recherche se fait par comparaison entre la valeur recherchée et les valeurs de début et de ﬁn du sous-ensemble.
{{% /note %}}

{{% note tip %}}
La division par deux de l'ensemble de données de recherche à chaque appel indique que la complexité est en $O(\log N)$.
{{% /note %}}

### Recherche dichotomique itérative

{{% note normal %}}

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
<span style="margin-left: 6em">resultat ⟵ milieu  </span><br />
<span style="margin-left: 6em">trouvé ⟵ VRAI  </span><br />
<span style="margin-left: 4em">**SinonSi** tab[milieu] < valeur **Alors** </span><br />
<span style="margin-left: 6em">gauche ⟵ milieu + 1  </span><br />
<span style="margin-left: 4em">**Sinon** </span><br />
<span style="margin-left: 6em">droite ⟵ milieu - 1  </span><br />
<span style="margin-left: 4em">**FinSi** </span><br />
<span style="margin-left: 2em">**FinTantQue**  </span><br />
<span style="margin-left: 2em">**Renvoyer** résultat  </span><br />
**Fin**  
{{% /note %}}

8. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 3, 5, 8, 9]` et `val = 3`.
{{% solution "Réponse" %}}

{{% /solution %}}

9. Démontrer que l'algorithme se termine.
{{% solution "Réponse" %}}

- **Variant de boucle :** $f(g, d) = d - g + 1$ où $d$ signifie « droite » et $g$ « gauche ».
- Au début, $g = 0$ et $d = n-1$ (où $n$ est la taille du tableau).
Le variant initial est donc $n$, qui est un entier naturel.
- À chaque itération, on a trois cas :
  - Si l'élément est trouvé, la boucle se termine.
  - Si l'élément cherché est plus grand que le milieu, on met à jour $g = m + 1$
  - Si l'élément cherché est plus petit que le milieu, on met à jour $d = m - 1$
Dans les deux derniers cas, la taille de l'intervalle est réduite de moitié (ou presque).
Donc, le variant diminue strictement à chaque itération.

Puisque le variant est initialement positif, diminue strictement à chaque itération, et que la boucle se termine quand il atteint 0 ou 1, on peut conclure que l'algorithme se termine toujours en un nombre fini d'étapes.

{{% /solution %}}

10. Démontrer que l'algorithme est correct.
{{% solution "Réponse" %}}
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
{{% /solution %}}

11. Démontrer que l'algorithme est en $O(\log_2 N)$.
{{% solution "Réponse" %}}
L'algorithme fonctionne en divisant l'intervalle de recherche par 2 à chaque itération. Ainsi, si le tableau contient $n$ éléments, après une itération, la taille de l'intervalle est réduite à $n/2$, puis $n/4$, et ainsi de suite. En général, après $k$ itérations, la taille de l'intervalle est réduite à $n / 2^k$.

L'algorithme se termine lorsque l'intervalle ne contient plus qu'un seul élément, ce qui se produit lorsque :
$$
\dfrac{n}{2^k} = 1
$$
En résolvant cette équation, on obtient :
$$
k = \log_2(n)
$$
Cela signifie que l'algorithme effectue au plus $\log_2(n)$ itérations pour un tableau de taille $n$.
{{% /solution %}}

### Recherche dichotomique récursive

{{% note normal %}}

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
{{% /note %}}

12. Décrire le fonctionnement de l'algorithme pour les valeurs `tab = [1, 3, 5, 8, 9]`, `gauche = 0`, `droite = 4`, et `val = 3`.
{{% solution "Réponse" %}}

{{% /solution %}}

## Application

{{% note exercise %}}
Écrire un programme de devinette&nbsp;: l'utilisateur choisit un nombre au hasard (compris entre 1 et 50) et l'ordinateur doit découvrir ce nombre. Faire en sorte que le nombre de tentatives de l'ordinateur lui permette de trouver la bonne valeur à coup sur (choisir de façon pertinente ce nombre).
{{% /note %}}
