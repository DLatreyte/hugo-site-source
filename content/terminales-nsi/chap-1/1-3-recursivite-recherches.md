---
title: "Recherche d'un élément dans un tableau : algorithmes itératifs et récursifs"
subtitle: "Chapitre 1,3"
author: ""
type: ""
date: 2020-09-09T21:33:15+04:00
draft: false
toc: true
tags: ["Récursivité", "Recherche linéaire", "Recherche dichotomique", "Complexité", "Terminaison", "Correction"]
categories: ["Informatique", "Terminales Spé NSI"]
image: ""
solution_est_visible: false
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
- Un corrigé se trouve à cette adresse&nbsp;: {{< remote "https://repl.it/join/azqimfmv-dlatreyte" "https://repl.it/join/azqimfmv-dlatreyte">}}

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

2.  Démontrer que l'algorithme se termine.
{{% solution "Réponse" %}}

{{% /solution %}}

3.  Démontrer que l'algorithme est correct.
{{% solution "Réponse" %}}

{{% /solution %}}

4.  Démontrer que l'algorithme est en O(N).
{{% solution "Réponse" %}}

{{% /solution %}}

5.  Comment pourrait-on améliorer l'efficacité de cet algorithme&nbsp;?
{{% solution "Réponse" %}}

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

9.  Démontrer que l'algorithme se termine.
{{% solution "Réponse" %}}

{{% /solution %}}

10.  Démontrer que l'algorithme est correct.
{{% solution "Réponse" %}}

{{% /solution %}}

11.  Démontrer que l'algorithme est en $O(\log_2 N)$.
{{% solution "Réponse" %}}

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