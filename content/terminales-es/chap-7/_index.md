---
title: "Optimisation du transport de l’électricité"
subtitle: "Chapitre 3"
author: ""
type: ""
date: 2021-01-20T22:07:17+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
layout: "single"
---

## Au programme

La minimisation des pertes par effet Joule dans la distribution d’électricité le long d’un réseau entre dans le cadre général des problèmes mathématiques de transport et d’optimisation sous contraintes. Ces problèmes, très difficiles à résoudre car non linéaires, nécessitent des traitements numériques lorsqu’ils mettent en jeu un nombre important d’inconnues ou de données.

Présentés ici dans le cadre du transport d’électricité, les graphes sont des modèles mathématiques utilisés pour traiter des problèmes relevant de domaines variés : transport d’information dans un réseau informatique, réseaux sociaux, transactions financières, analyses génétiques, etc.

| **Savoirs** | **Savoir-faire** |
|:---------|:---------|
|- Au cours du transport, une partie de l’énergie électrique, dissipée dans l’environnement par effet Joule, ne parvient pas à l’utilisateur.<br />- L’utilisation de la haute tension dans les lignes électriques limite les pertes par effet Joule, à puissance transportée fixée. | - Faire un schéma d’un circuit électrique modélisant une ligne à haute tension.<br />- Utiliser les formules littérales reliant la puissance à la résistance, l’intensité et la tension pour identifier l’influence de ces grandeurs sur l’effet Joule. |
|- Un réseau de transport électrique peut être modélisé mathématiquement par un graphe orienté dont les arcs représentent les lignes électriques et dont les sommets représentent les sources distributrices, les nœuds intermédiaires et les cibles destinatrices.<br />- Dans ce modèle, l’objectif est de minimiser les pertes par effet Joule sur l’ensemble du réseau sous les contraintes suivantes :<br />- l’intensité totale sortant d’une source est limitée par la puissance maximale distribuée ;<br />- l’intensité totale entrant dans chaque nœud intermédiaire est égale à l’intensité totale qui en sort ; <br />- l’intensité totale arrivant à chaque cible est imposée par la puissance qui y est utilisée. | - Modéliser un réseau de distribution électrique simple par un graphe orienté. Exprimer mathématiquement les contraintes et la fonction à minimiser.<br />- Sur l’exemple d’un réseau comprenant uniquement deux sources, un nœud intermédiaire et deux cibles, formuler le problème de minimisation des pertes par effet Joule et le résoudre pour différentes valeurs numériques correspondant aux productions des sources et aux besoins des cibles. |

#### Prérequis et limites

Les relations quantitatives associées à l’effet Joule sont connues pour le courant continu. Elles sont admises ou fournies pour le courant alternatif. La notion de facteur de puissance est hors programme.

La notion de graphe, abordée dans l’enseignement de sciences numériques et technologie de seconde, est ici mobilisée. Il convient d’insister sur la différence entre les deux types de modèles introduits dans ce sous-thème, le modèle de circuit électrique et le modèle mathématique de graphe.

Les connaissances sur les fonctions sont mobilisées.

## Documents

----

{{< remote "Cours sur le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663190" >}}

----

- **Chap. 3,1 :** [*L'effet Joule*](1-effet-joule)

- **Chap. 3,2 :** [*Optimisation du transport de l'électricité*](2-optimisation-transport-electricite)

- **Chap. 3,3 :** [*Exercices du chapitre*](3-exercices)

- **Chap. 3,4 :** [*Carte mentale du chapitre*](/terminales-es/chap-7/optimisation-transport-electricite.svg)
