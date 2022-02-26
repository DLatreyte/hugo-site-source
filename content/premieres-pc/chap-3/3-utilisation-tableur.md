---
title: "Utilisation d'un tableur pour déterminer une incertitude de mesure de type A"
subtitle: "Chapitre 3,3"
author: ""
type: ""
date: 2020-10-08T16:43:09+04:00
draft: false
toc: true
tags: ["Erreurs", "Incertitudes"]
categories: ["Premières Spé PC", "Physique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Problème 

Un groupe d'élèves effectue la mesure de la célérité des ultrasons dans l'air dans une pièce à $\pu{20 °C}$.
Leurs résultats sont regroupés dans le tableau ci-dessous&nbsp;:

<center>

| N° mesure | Valeur ($\pu{m/s}$) | N° mesure | Valeur ($\pu{m/s}$) |
|:-:| :-: |:-:|:-:|
| 1 | 338 | 11 | 338 |
| 2 | 341 | 12 | 336 |
| 3 | 338 | 13 | 342 |
| 4 | 340 | 14 | 341 |
| 5 | 337 | 15 | 337 |
| 6 | 339 | 16 | 342 |
| 7 | 342 | 17 | 336 |
| 8 | 338 | 18 | 338 |
| 9 | 340 | 19 | 339 |
| 10 | 339 | 20 | 343 |

</center>

> À partir des mesures obtenues, évaluer la célérité des ultrasons dans l'air à $\pu{20 °C}$ en calculant l'incertitude de répétabilité avec un niveau de confiance de 95 % puis à 99 %.

Ce calcul sera effectué en utilisant un tableur.

## Travail

{{% note normal %}}
Un fichier du tableur Google Sheet a déjà été préparé et partagé. **Dupliquer ce fichier avant de le modifier&nbsp;:** <kbd>Fichier</kbd> > <kbd>Créer une copie</kbd>.
{{% /note %}}

### Création d'un histogramme

{{% note tip %}}
Un histogramme est un moyen rapide pour étudier la répartition d’une grandeur. C'est une représentation graphique dans laquelle on affiche le nombre de fois que chaque valeur de la variable apparaît. On peut alors **qualitativement** évaluer la dispersion des valeurs.
{{% /note %}}

1. Sélectionner la colonne `B`.
2. Choisir&nbsp;: <kbd>Insertion</kbd> $>$ <kbd>Graphique</kbd>.
    - Dans la partie <kbd>Type de graphique</kbd>, sélectionner <kbd>Histogramme</kbd>.
    - Choisir l'onglet <kbd>Personnaliser </kbd> puis <kbd>Histogramme</kbd>, <kbd>Taille des barres</kbd>&nbsp;: 1.
    - Choisir l'onglet <kbd>Personnaliser</kbd> puis <kbd>Axe horizontal</kbd>&nbsp;:
        - Min&nbsp;: 335
        - Max&nbsp;: 345
3. Quelle est la vitesse la plus représentée ?
{{% solution "Réponse" %}}
<img src="/premieres-pc/chap-3/chap-3-3-1.svg" alt="" width="60%" />
$v=\pu{338 m/s}$
{{% /solution %}}

### Estimation de la valeur de la vitesse

4. Dans la cellule <kbd>C2</kbd>, faire calculer par le tableur la moyenne de la série de mesures.
{{% solution "Réponse" %}}
- Formule à entrer&nbsp;: <kbd>=MOYENNE(B2:B21)</kbd>
- Valeur&nbsp;: $v=\pu{339,2 m/s}$
{{% /solution %}}

5. Dans la cellule <kbd>D2</kbd>, faire calculer par le tableur la moyenne des six premiers termes de la série de mesures.
{{% solution "Réponse" %}}
- Formule à entrer&nbsp;: <kbd>=MOYENNE(B2:B7)</kbd>
- Valeur&nbsp;: $v=\pu{338,8 m/s}$
{{% /solution %}}

6. Pourquoi les deux moyennes calculées aux questions précédentes ne sont-elles pas égales&nbsp;?
{{% solution "Réponse" %}}
On a calculé des moyennes de séries différentes, il est donc normal que ces 
moyennes soient différentes.   
**La valeur moyenne est une grandeur aléatoire.**
{{% /solution %}}

7. Comment faire en sorte que la valeur moyenne caractérise au mieux «&nbsp;la série de mesures&nbsp;»&nbsp;?
{{% solution "Réponse" %}}
Il faut réaliser le plus grand nombre d'expériences possible.
{{% /solution %}}

{{% note tip %}}
La valeur moyenne, *si le nombre de mesures est suffisamment grand*, est une bonne **estimation** de la valeur de la grandeur mesurée.
{{% /note %}}

### Incertitude de répétabilité

L'incertitude de mesure $U(m)$ correspondant à des mesures répétées d'une même 
grandeur est appelée **incertitude de répétabilité** . Elle est liée à 
l'**écart-type** de la série de mesures.

{{% note tip %}}
- Pour une série de $n$ *mesures indépendantes* donnant des valeurs mesurées $m_{k}$ l'écart-type de la série de mesures est donné par la formule&nbsp;:
$$ \sigma_{n - 1} = \sqrt{\dfrac{\sum_{k = 1}^n (m_{k} - \overline{m})^2}{n - 1}} $$
où $\overline{m}$ est la valeur moyenne de la série de mesures.   
L'écart type est obtenu en utilisant les fonctions statistiques d'une calculatrice, d'un tableur ou d'un programme écrit en Python.

- L'**incertitude de répétabilité**  associée à la mesure se calcule alors grâce à la formule&nbsp;:
$$ U (m) = k \hspace{0.17em} \dfrac{\sigma_{n - 1}}{\sqrt{n}} $$

Elle dépend du nombre $n$ de mesures indépendantes réalisées, de l'écart type de la série de mesures et d'un coefficient $k$ appelé **facteur d'élargissement** (ou coefficient de Student).

- Le **facteur d'élargissement** $k$ dépend du *nombre de mesures réalisées* $n$ et du *niveau de confiance* choisi.
{{% /note %}}

**Quelques valeurs de $k$&nbsp;:**

| nn | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $k$ 95%| 12,7 | 4,30 | 3,18 | 2,78 | 2,57 | 2,45 | 2,37 | 2,31 | 2,26 | 2,23 | 2,20 | 2,18 | 2,16 | 2,15 | 2,13 |
| $k$ 99% | 63,7 | 9,93 | 5,84 | 4,60 | 4,03 | 3,71 | 3,50 | 3,36 | 3,25 | 3,17 | 3,11 | 3,06 | 3,01 | 2,98 | 2,95 |

8. Pour un *même nombre de mesures*, comment évolue $k$ avec le niveau de confiance&nbsp;? Qu'est-ce que cette évolution traduit&nbsp;?

{{% solution "Réponse" %}}
Pour un même nombre de mesures, $k_{\pu{95 }} < k_{\pu{99}}$. Plus grande est l'incertitude $U (m)$, plus grande est la 
probabilité que la «&nbsp;valeur vraie&nbsp;» se trouve dans l'intervalle 
$\overline{m} \pm U (m)$.
{{% /solution %}}

9. Pour un *même niveau de confiance*, comment évolue $k$ avec le nombre de 
mesures réalisées&nbsp;? Qu'est-ce que cette évolution traduit&nbsp;?

{{% solution "Réponse" %}}
$k$ diminue lorsque le nombre de mesures augmente. Plus le nombre de mesures 
est grand, plus la valeur moyenne de la série est représentative de la valeur 
mesurée et plus petit peut donc être l'intervalle autour de cette valeur 
moyenne. On retrouve l'idée qu'il est préférable de faire un grand nombre de 
mesures.
{{% /solution %}}

#### Pourquoi choisir l'écart type&nbsp;?

<figure>
<img src="/terminales-pc/chap-0/Chap-0-2-1.png" width="70%" />
</figure>

On cherche maintenant à calculer la somme des écarts à la valeur moyenne&nbsp;:

$$ \sum\_{k = 1}^n (m\_{k} - \overline{m}) $$

10. Dans la colonne <kbd>E</kbd> faire calculer par le tableur l'écart de toutes les mesures à la moyenne.   
Pourquoi certaines valeurs sont-elles négatives ?
{{% solution "Réponse" %}}
- Dans la cellule <kbd>E2</kbd>, entrer la formule <kbd>=B2-$C$2</kbd> puis «&nbsp; tirer&nbsp;» vers le bas.
- L'écart à la moyenne est une grandeur algébrique, parfois $m_k > \bar{m}$, parfois $m_k < \bar{m}$. 
{{% /note %}}

11. Dans la cellule <kbd>F2</kbd>, calculer la somme des écarts à la moyenne.   
Le résultat obtenu était-il prévisible ?
{{% solution "Réponse" %}}
- Entrer la formule <kbd>=SOMME(E2:E21)</kbd>.
- On obtient une valeur nulle (aux arrondis près). Ce résultat était tout à fait prévisible puisque la valeur moyenne est le point d'équilibre de la série de valeurs&nbsp;: *les écarts positifs sont donc compensés par les écarts négatifs.*
{{% /solution %}}

12. L'écart-type ne considère pas les écarts à la valeur moyenne mais les 
carrés de ces écarts (cf. formule ci-dessus). Ils ne peuvent donc pas se 
compenser.   
Dans la colonne <kbd>G</kbd>, faire calculer par le tableur le carré des écarts à la moyenne.

{{% solution "Réponse" %}}
Dans la cellule <kbd>G2</kbd>, entrer la formule <kbd>=E2*E2</kbd> puis «&nbsp;tirer&nbsp;» vers le bas.
{{% /solution %}}

13. Dans la cellule <kbd>H2</kbd>, calculer la valeur de l'écart-type $\sigma_{n-1}$.

{{% solution "Réponse" %}}
Dans la cellule <kbd>H2</kbd>, entrer la formule <kbd>=RACINE(SOMME(G2:G21)/19)</kbd>.
{{% /solution %}}

14. Tout tableur possède, en interne, une fonction <kbd>ECARTYPE</kbd> capable de calculer directement l'écart-type d'une série de mesures. Utiliser cette fonction pour vérifier que le résultat obtenu à la question **13.** est correct.

{{% solution "Réponse" %}}
Dans la cellule <kbd>I2</kbd>, entrer la formule <kbd>=ECARTYPE(B2:B21)</kbd>.
{{% /solution %}}

15. Dans les cellules <kbd>J2</kbd> et <kbd>K2</kbd>, calculer les incertitudes $U_95$ et $U_99$ associées à la série de mesure.   
Pour une série de $n$ échantillons, $k_{95} = \pu{2,09}$ et $k_{99} = \pu{2,85}$.

{{% solution "Réponse" %}}
- Dans la cellule <kbd>J2</kbd>, entrer la formule <kbd>=I2*2,09/RACINE(20)</kbd>&nbsp;;
- Dans la cellule <kbd>K2</kbd>, entrer la formule <kbd>=I2*2,85/RACINE(20)</kbd>.
{{% /solution %}}

16. Donner la célérité des ultrasons pour une confiance de 95&nbsp;% puis pour une confiance de 99&nbsp;%.
{{% solution "Réponse" %}}
- Pour une confiance de 95&nbsp;%, $v = \pu{339 \pm 1) m.s-1}$&nbsp;;
- Pour une confiance de 99&nbsp;%, $v = \pu{339 \pm 2) m.s-1}$&nbsp;;
{{% /solution %}}

## Application

La mesure $\Delta t$ de la durée de chute d'un objet depuis une fenêtre a 
été répétée 16 fois avec un chronomètre de qualité. Les résultats 
obtenus, exprimés en seconde, sont les suivants&nbsp;:
<center>

|  |  |  |  |  |  |  |  |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1,38 | 1,45 | 1,41 | 1,45 | 1,43 | 1,41 | 1,46 | 1,39 |
|  |  |  |  |  |  |  |  |
| 1,43 | 1,48 | 1,38 | 1,44 | 1,40 | 1,42 | 1,39 | 1,44 |

</center>

Donner la valeur de la durée de chute de l'objet accompagnée de son incertitude.