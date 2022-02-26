---
title: "Optimisation du transport de l'électricité"
subtitle: "Chapitre 3,2"
author: ""
type: ""
date: 2021-01-28T05:07:41+04:00
draft: false
toc: true
tags: []
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Réseaux électriques et graphes

### Modélisation d'un réseau électrique

<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-1.png" alt="" width="50%" style="float: right; padding-left: 15px;" />

Un réseau électrique fait apparaître :
- des **sources** (centrale nucléaire, station photovoltaïque, centrale géothermique, ...) ;
- des **cibles** (usines, villes, villages, particuliers, ...) ;
- des **équipements intermédiaires**, qui assurent les liaison entre les réseaux, ou alors l'élévation ou l'abaissement de la tension électrique (**transformateurs**).

Si on représente chaque entité évoquée ci-dessus par un point et les câbles qui les relient par des traits, on forme une structure qu'on appelle **graphe** en mathmétique (ou en informatique).


### Un peu d'histoire : Les Ponts de Königsberg

La ville de Königsberg (aujourd'hui Kaliningrad en Russie) est construite autour de deux îles situées sur le Pregel et reliées entre elles par un pont. Six autres ponts relient les rives de la rivière à l'une ou l'autre des deux îles. 
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-3.png" alt="" width="50%" />

> Existe-t-il une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de *passer une et une seule fois par chaque pont*, et de *revenir à son point de départ*, étant entendu qu'on ne peut traverser le Pregel qu'en passant sur les ponts ?

{{% solution "Réponse (intuitive)" %}}
Non. Si une telle promenade existait, chaque quartier devrait être relié à un nombre pair de ponts : un premier pour arriver dans le quartier, un second pour quitter le quartier.
{{% /solution %}}

> Existe-t-il une promenade dans les rues de Königsberg permettant, à partir d'un point de départ au choix, de *passer une et une seule fois par chaque pont* ?
{{% solution "Réponse (intuitive)" %}}
Non. Si une telle promenade existait, les quartiers, à l'exception des quartiers de départ et d'arrivée, devraient être reliés à un nombre pair de ponts : un premier pour arriver dans le quartier, un second pour quitter le quartier.
{{% /solution %}}

**Comment Euler a-t-il résolu le problème en 1735 ?**\
Il a représenté les quartiers par des nœuds et les ponts par des arêtes et cherché si un parcours passant par toutes les arêtes une et une seule fois existait.
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-4.png" alt="" width="50%" />


### Qu'est-ce qu'un graphe ?


{{% note tip %}}
#### Graphe 

- Un **graphe non orienté** est constitué d’un ensemble de points, appelés **nœuds**, et d’un ensemble de **couples de nœuds distincts** appelés **arêtes**.

- Un **graphe orienté** est constitué d’un ensemble de points, appelés **nœuds**, et d’un ensemble de **couples de nœuds distincts** appelés **arcs**. *Les arcs sont alors représentés par des flèches*.

- Un graphe, orienté ou non peut être **pondéré par des valeurs numériques** affectées à ses arêtes ou à ses arcs.

- On appelle parcours dans un graphe un chemin qui relie deux nœuds.
{{% /note %}}

Dans le cas d’un graphe pondéré, la valeur numérique associée à une arête (poids) peut être la distance entre ses deux extrémités ou le coût pour aller de l’une à l’autre.

De nombreux problèmes d’optimisation sur les graphes ont été étudiés, l’un des plus connus étant celui du {{< remote "voyageur de commerce" "https://fr.wikipedia.org/wiki/Problème_du_voyageur_de_commerce" >}} : *« Étant donné une liste de villes, et des distances entre toutes les paires de villes, déterminer un plus court chemin qui visite chaque ville une et une seule fois et qui termine dans la ville de départ. »*\
Ce problème est encore un domaine actif de recherche et il existe seulement des algorithmes imparfaits qui ne trouvent pas toujours le meilleur chemin.

#### Exemples de modélisations de situations par des graphes

- Routage de l'information sur internet ;
- Relations entre personnes dans les réseaux sociaux ;
- Réseau autoroutier ;
- Réseau ferré ;
- ...

{{% note exercise %}}
Pour chacun des graphes ci-dessous, indiquer le nombre de nœuds, d'arêtes (ou d'arcs), s'il est orienté ou pas, s'il est pondéré ou pas.
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-2.png" alt="" width="60%" />
{{% /note %}}
{{% solution "Réponses" %}}
a) Graphe non orienté constitué de 4 nœuds et de 5 arêtes.   
b) Graphe non orienté constitué de 4 nœuds et de 7 arêtes (graphe du problème des {{< remote "7 ponts de Königsberg" "https://fr.wikipedia.org/wiki/Problème_des_sept_ponts_de_Königsberg" >}}).    
c) Graphe orienté constitué de 4 nœuds et 6 arcs.    
d) Graphe orienté et pondéré constitué de 4 nœuds et 5 arcs.   
{{% /solution %}}

### Modélisation d'un réseau électrique

{{% note tip %}}
#### La répartition des courants électriques dans un réseau doit satisfaire plusieurs contraintes

- L’intensité du courant électrique qui quitte une source ne peut pas dépasser sa capacité de production ;
- L’intensité totale du courant électrique qui entre dans chaque nœud doit être égale à l’intensité du courant électrique qui en sort (c’est la **loi des nœuds**) ;
- L’intensité du courant électrique qui arrive au niveau de chaque cible est fixée par ses besoins en énergie électrique.
{{% /note %}}


{{% note tip %}}
#### Modélisation d'un réseau électrique

Un **réseau électrique** peut être modélisé par un **graphe pondéré et orienté**. Les sommets du graphe représentent les sources, les cibles et un certain nombre de nœuds intermédiaires. Les arcs du graphe représentent les lignes électriques, elles **sont pondérées par l’intensité du courant électrique** dans le câble et orientées par le sens du courant (des sources vers les cibles).
{{% /note %}}

{{% note warning %}}
Le problème d'optimisation du transport du courant électrique est donc un **problème d'optimisation sous contrainte**.
{{% /note %}}

{{% note exercise %}}
#### Application : 

{{< remote "Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663400?docId=2e7BWRI03T0y579PXQ9RS" >}}

Une île comporte quatre villes. Pour répondre aux besoins énergétiques de ces quatre villes, un champ éolien, une centrale marémotrice et une centrale thermique ont été construits.

La répartition du courant se fait par l’intermédiaire de deux postes de distribution reliés entre eux. La centrale marémotrice et le champ éolien sont chacun reliés à un poste différent. La centrale thermique est reliée au même poste que le champ éolien. Deux villes sont connectées à un poste et les deux autres villes à l’autre.


**Travail :** Construire le graphe modélisant le réseau électrique. En particulier, identifier les différents sommets du graphe, les différents arcs du graphe et le sens des arcs.
{{% /note %}}

{{% solution "Réponse" %}}
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-5.png" alt="" width="80%" />
- Les quatre villes, les deux postes de distribution, le champ éolien, la centrale thermique et la centrale marémotrice constituent les sommets du graphe.
- La ville 1 et la ville 2 sont reliées au poste de distribution 1 par un arc orienté vers la ville (le poste distribue l’électricité).
- La ville 3 et la ville 4 sont reliées au poste de distribution 2 par un arc orienté vers la ville (le poste distribue l’électricité).
- Le champ éolien et la centrale thermique sont reliés au poste de distribution 1 par un arc orienté vers le poste (les centrales distribuent l’électricité vers le poste).
- La centrale marémotrice est reliée au poste de distribution 2 par un arc orienté vers le poste (la centrale distribue l’électricité vers le poste).
- Les postes de distribution sont reliés par un arc non orienté, afin d’assurer le transport de l'électricité vers les 4 villes à partir des 3 centrales de production de l’électricité.
{{% /solution %}}

## Minimiser les pertes pour la distribution d'énergie

{{% note exercise %}}
Deux villes de moyenne montagne sont connectées à l’ensemble du réseau, mais l’électricité provient essentiellement de deux sources : une centrale hydroélectrique et une petite centrale à charbon.
Avant d’arriver aux villes, l’électricité passe par un poste électrique qui répartit le courant électrique en fonction des besoins.

On cherche ici à déterminer l’intensité du courant dans toutes les branches du réseau avec le minimum de perte d’énergie lors du transport de l’électricité.
{{% /note %}}

1. Construire le graphe modélisant le réseau électrique.
{{% solution "Réponse" %}}
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-6.png" alt="" width="80%" />
{{% /solution %}}

- La tension au sein du réseau étudié est de $\pu{20 kV}$.
- La longueur des lignes reliant la centrale hydroélectrique au poste électrique est deux fois plus grande que celle reliant la centrale à charbon au poste électrique. La résistance est donc aussi deux fois plus grande. La résistance des autres branches est négligée.
- La ville 1 a besoin d’une puissance électrique moyenne de $\pu{4,0 MW}$. 
- La ville 2 a besoin d’une puissance électrique moyenne de $\pu{1,0 MW}$.
- La valeur de la résistance des lignes reliant la centrale à charbon au poste de distribution est arbitrairement prise comme valant $\pu{1 \Omega}$.

2. Compléter le graphe avec les informations ci-dessus.
{{% solution "Réponse" %}}
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-7.png" alt="" width="90%" />
{{% /solution %}}

3. Déterminer la valeur des intensité $I\_1$ et $I\_2$ des courants qui arrivent dans les villes 1 et 2.\
**Aide.** Utiliser les deux informations que l'on possède pour chacune des villes.
{{% solution "Réponse" %}}
$P = UI$, donc $I = \dfrac{P}{U}$.
- $I\_1 = \dfrac{\pu{4,0e6 W}}{\pu{2,0e4 V}}=\pu{2,0e2 A}$.
- $I\_2 = \dfrac{\pu{1,0e6 W}}{\pu{2,0e4 V}}=\pu{5,0e1 A}$.
{{% /solution %}}

4. Écrire la loi des nœuds au niveau du poste de distribution.\
On note $I\_C$ et $I\_H$ les intensités des courants électriques qui quittent les centrales à charbon et hydroélectrique.
{{% solution "Réponse" %}}
$I\_C + I\_H = I\_1 + I\_2 $
{{% /solution %}}

5. Écrire l'expression de la puissance joule totale dissipée, en fonction de la seule variable $I\_C$.
{{% solution "Réponse" %}}
- $P\_T = P\_C + P\_H = R\_C \\, I\_C^2 + R\_H \\, I\_H^2$.
- Comme $I\_H = I\_1 + I\_2 - I\_C = A - I\_C$ avec $A = I\_1 + I\_2 = \pu{2e2 A} + \pu{5e1 A} = \pu{2,5e2 A}$, $$P\_T = R\_C \\, I\_C^2 + R\_H \\, (A - I\_C)^2$$
{{% /solution %}}

6. Que faut-il faire pour minimiser l'énergie perdue lors du transport de l'électricité ?
{{% solution "Réponse" %}}
Le minimumn de l'énergie perdue lors du transport correspond à la minimisation de la fonction $P\_T(I\_C)$.
{{% /solution %}}

7. Compléter le code Python à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Minimisation-Puissance-Joule-Eleves" >}} afin de tracer la fonction $P\_T(I\_C)$. En déduire la valeur de $I\_C$ qui minimise l'énergie perdue.
{{% solution "Réponse" %}}
{{< remote "Code corrigé" "https://repl.it/@dlatreyte/Minimisation-Puissance-Joule" >}}
<img src="/terminales-es/chap-7/chap-7-2/chap-7-2-8.png" alt="" width="90%" />
La puissance dissipée est minimale pour $I\_C = \pu{165 A}$.
{{% /solution %}}
