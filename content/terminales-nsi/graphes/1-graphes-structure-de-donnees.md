---
title: "Les graphes : structure de données"
subtitle: ""
author: ""
type: ""
date: 2021-04-20T07:56:25+04:00
draft: false
toc: true
tags: ["Graphe", "Structure de données"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

- {{< remote "Cours et exercices non corrigés" "/terminales-nsi/chap-15/chap-15-1/Introduction-graphes-Q.pdf" >}}

{{% solution "Solutions" %}}
{{< remote "Cours et exercices corrigés" "/terminales-nsi/chap-15/chap-15-1/Introduction-graphes-QR.pdf" >}}
{{% /solution %}}

<!--
## Un peu d'histoire : Les Ponts de Königsberg

La ville de Königsberg (aujourd'hui Kaliningrad en Russie) est construite autour de deux îles situées sur le Pregel et reliées entre elles par un pont. Six autres ponts relient les rives de la rivière à l'une ou l'autre des deux îles.

<img src="/terminales-nsi/chap-15/chap-15-1/im1.png" alt="" width="50%" />

1. Existe-t-il une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de *passer une et une seule fois par chaque pont*, et de *revenir à son point de départ*, étant entendu qu'on ne peut traverser le Pregel qu'en passant sur les ponts ?

{{% solution "Réponse" %}}

Non. Si une telle promenade existait, chaque quartier devrait être relié à un nombre pair de ponts : un premier pour arriver dans le quartier, un second pour quitter le quartier.

{{% /solution %}}

2. Existe-t-il une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de *passer une et une seule fois par chaque pont* ?

{{% solution "Réponse" %}}

Non. Si une telle promenade existait, les quartiers, à l'exception des quartiers de départ et d'arrivée, devraient être reliés à un nombre pair de ponts : un premier pour arriver dans le quartier, un second pour quitter le quartier.

{{% /solution %}}

#### Comment Euler a-t-il résolu le problème en 1735 ?

Il a représenté les quartiers par des nœuds et les ponts par des arêtes et cherché si un parcours passant par toutes les arêtes une et une seule fois existait.

<img src="/terminales-nsi/chap-15/chap-15-1/im2.png" alt="" width="50%" />

## Graphes

Un **graphe** est un objet abstrait composé d'**éléments** — les *sommets* — qui modélisent des objets de la vie réelle et de **relations entre ces éléments** — les *arêtes* (graphes non orientés) ou les *arcs* (graphes orientés).

Un graphe permet de représenter des liens d'amitié entre des personnes, des lignes aériennes entre des villes, des câbles entre des ordinateurs et des routeurs, des références entre des pages web, etc. Ce concept est utilisé dans l'industrie (informatique, recherche opérationnelle, etc) mais aussi dans la recherche (étude de réseaux sociaux, biologie, mathématiques, etc.)

Un graphe peut être :

- **orienté** ou **non orienté** ;
- **pondéré** ou **non pondéré**.

----

#### Exemples supplémentaires de graphes

- **Graphe du flot de contrôle d'un programme**  
Les sommets sont les instructions ou les tests, les flèches indiquent les enchaînements possibles entre ceux-ci.

<img src="/terminales-nsi/chap-15/chap-15-1/im3.png" alt="" width="50%" />

3. Le graphe associé à ce flot de contrôle est-il orienté ou non orienté ?
{{% solution "Réponse" %}}

Le graphe est orienté.

{{% /solution %}}

- **Organisation de tâches qui doivent être exécutées séquentiellement**  
Les sommets sont les tâches, des relations existent entre les tâches terminées et celles qui les suivent.
<img src="/terminales-nsi/chap-15/chap-15-1/im4.png" alt="" width="80%" />

> Préparation d'un curry d'agneau.

4. Pourquoi une structure de **file** ne peut-elle convenir ici ?
{{% solution "Réponse" %}}

Certaines tâches doivent être réalisées en parallèle.

{{% /solution %}}

## Graphes non orientés

### Définitions

{{% note tip %}}

#### Graphe non orienté

Un graphe non orienté $G$ est défini par un couple $G = (V, E)$, où $V$ est un **ensemble de sommets** et $E$ un **ensemble d'arêtes**.

{{% /note %}}

<img src="/terminales-nsi/chap-15/chap-15-1/im5.svg" alt="" width="50%" />

5. Pour le graphe ci-dessus, donner l'ensemble $V$ des nœuds, puis l'ensemble $E$ des arêtes.
{{% solution "Réponse" %}}

- Ensemble des nœuds : $V = \lbrace a, b, c, d, e \rbrace$ ;
- Ensemble des arêtes : $E = \lbrace \lbrace a, b \rbrace, \lbrace a, c \rbrace, \lbrace b, d \rbrace, \lbrace c, d \rbrace, \lbrace c, e \rbrace, \lbrace b, e \rbrace, \lbrace d, e \rbrace \rbrace$.

{{% /solution %}}

6. Soit le graphe $G = (V, E)$ tel que $V = \lbrace a, b, c, d, e, f \rbrace$ et $E = \lbrace \lbrace a, b \rbrace, \lbrace c, d \rbrace, \lbrace c, e \rbrace, \lbrace a, c \rbrace, \lbrace b, d \rbrace, \lbrace f, d \rbrace \rbrace$.  
Représenter $G$.

{{% solution "Réponse" %}}

<img src="/terminales-nsi/chap-15/chap-15-1/im6.svg" alt="" width="50%" />

{{% /solution %}}

{{% note tip %}}

Soit $G = (V, E)$ un graphe non orienté.

- Une **boucle** est une arête $\lbrace u, u \rbrace$ avec $u \in V$ ;
- Une arête $e = \lbrace u, v \rbrace$ est **multiple** s'il existe au moins deux arêtes $\lbrace u, v \rbrace$ dans $E$.

{{% /note %}}

<img src="/terminales-nsi/chap-15/chap-15-1/im7.svg" alt="" width="40%" />

{{% note tip %}}

#### Graphe orienté simple

Un graphe non orienté simple $G$ est un graphe sans boucle ni arête multiple.

{{% /note %}}

*Dans ce cours, on suppose a priori que tous les graphes non orientés sont simples.*

### Vocabulaire

{{% note tip %}}

- Tous les **sommets voisins** $v\_{i}$ d'un sommet $u$, c'est à dire liés à $u$ par la formation d'une arête, $\lbrace u, v\_{i} \rbrace$ constituent l'**ensemble des sommets adjacents** à $u$.

- On appelle **degré d'un sommet** le nombre de sommets adjacents à ce sommet.  
Le degré d'un sommet est le *cardinal de l'ensemble des sommets voisins.*

{{% /note %}}

7. Indiquer l'ensemble des sommets adjacents au sommet `d` du graphe ci-dessous, ainsi que son degré.
<img src="/terminales-nsi/chap-15/chap-15-1/im5.svg" alt="" width="50%" />

{{% solution "Réponse" %}}

- Ensemble des sommets adjacents à `d` : $\lbrace c,b,e  \rbrace$ ;
- Degré de `d` : $d=3$.

{{% /solution %}}

8. Même question pour le sommet `a` du graphe.
{{% solution "Réponse" %}}

- Ensemble des sommets adjacents à `a` : $\lbrace c,b  \rbrace$ ;
- Degré de `d` : $d=2$.

{{% /solution %}}

9. Pour le graphe ci-dessous indiquer l'ensemble des sommets adjacents au sommet `e` et son degré.  
<img src="/terminales-nsi/chap-15/chap-15-1/im8.svg" alt="" width="50%" />

{{% solution "Réponse" %}}

- Ensemble des sommets adjacents à `e` : $\lbrace c  \rbrace$ ;
- Degré de `d` : $d=1$.

{{% /solution %}}

{{% note normal %}}

Pour tout graphe $G = (V,E)$ non orienté la somme des degrés de tous les sommets est égale à deux fois le nombre d'arrêtes.

{{% /note %}}

{{% note tip %}}

#### Chaîne

Une chaîne (walk) est une séquence de sommets et d'arêtes $v = v\_{1} e\_{1} v\_{2} e\_{2} \ldots v\_{n} e\_{n} v\_{n + 1}$ avec $v\_{i} \in V$ pour $i \in \lbrace 1, \ldots, n + 1 \rbrace$ et $e\_{i} = \lbrace v\_{i}, v\_{i + 1} \rbrace \in E$ pour $i \in 1, \ldots, n$.

{{% /note %}}

-->
