---
title: "Exploration du système saturnien"
subtitle: "Chapitre 9,7"
author: ""
type: ""
date: 2020-12-29T17:38:14+04:00
draft: false
toc: true
tags: ["Champ gravitationnel", "Force gravitationnelle", "Repère de Frenet", "Deuxième loi de Newton", "Période de révolution", "Mouvement uniforme", "Accélération normale"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---
> Saturne, à cause de sa distance à la Terre et au Soleil, est une destination spatiale complexe qui nécessite un savoir-faire et des ressources financières très importants. La mission Cassini-Huygens reste, à ce jour, la seule mission à avoir placé une sonde, Cassini, en orbite autour de Saturne, et à avoir pu mener une étude approfondie de son système.

Cet exercice se propose d'étudier l'une des particularités de la planète Saturne, *ses anneaux*, puis se concentre sur l'étude de deux aspects de la mission Cassini-Huygens : l'*atterrissage en douceur de l'atterrisseur* Huygens sur le sol de la lune la plus grosse de Saturne, Titan et *une erreur de conception qui aurait pu faire échouer la partie la plus importante de la mission*.

<center>
<strong>Les trois parties de cet exercice (1., 2. et 3.) sont indépendantes.</strong> 
</center>

## Les anneaux de Saturne

<img src="/terminales-pc/chap-8/chap-8-7/chap-8-7-1.jpg" alt="" width="40%" style="float: right; padding-left: 20px;" />

Les anneaux de Saturne sont les anneaux planétaires les plus importants du Système solaire. *Bien qu'ils semblent continus vus depuis la Terre, ils sont en fait constitués d'innombrables particules de glace* (95 à 99 % de glace d'eau pure selon les analyses spectroscopiques) et de poussière dont la taille varie de quelques micromètres à quelques centaines de mètres ; ils ont chacun une orbite différente. Les anneaux forment un disque dont le diamètre est de $\pu{360000 km}$ (les anneaux principaux s'étendent de $\pu{7000}$ à $\pu{72000 km}$) comportant plusieurs divisions de largeurs variées et dont l'épaisseur va de 2 à 10 mètres. [etc.]

La sonde Cassini, a permis de montrer que la masse des anneaux est faible et que leur date de formation serait récente (quelques centaines de millions d'années peut-être alors qu'on admettait généralement qu'ils dataient de la formation du système solaire).

<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Anneaux_de_Saturne" target="_blank">https://fr.wikipedia.org/wiki/Anneaux_de_Saturne</a>
</div>

----

L'objectif de cette partie est de juger de la compatibilité d'un modèle avec la phrase en italique ci-dessus.

### L'interaction gravitationnelle

On considère une planète $S$, de symétrie sphérique, de masse $M$ et un objet $O$ assez petit (assimilable à un point matériel) de masse $m$, gravitant autour de $S$ avec un mouvement circulaire. On note $r$ la distance séparant le centre de la planète $S$ et l'objet $O$.

1. Reprendre, sur votre feuille, le schéma ci-dessous, et y représenter le vecteur force $\vec{F}\_{S / O}$ qu'exerce la planète $S$ sur l'objet $O$ (sans considération d'échelle).
<img src="/terminales-pc/chap-8/chap-8-7/chap-8-7-2.png" alt="" width="50%" />

2. Donner l'expression vectorielle de la force gravitationnelle $\vec{F}\_{S / O}$ en fonction du vecteur unitaire $\vec{n}$.

### Satellite gravitant sur une orbite circulaire

3. Lors de l'étude du mouvement d'un satellite de la Terre, on utilise généralement le référentiel géocentrique. Dans le cas présent, quel référentiel analogue doit-on choisir pour étudier le mouvement de l'objet $O$ ?

4. Déterminer, en utilisant la deuxième loi de Newton, l'expression du vecteur accélération $\vec{a}$ de l'objet $O$ lors de ce mouvement, en fonction de $G$, $M$, $r$ et $\vec{n}$.

5. Représenter ce vecteur accélération $\vec{a}$ sur le schéma établi à la question 2.

6. Rappeler la définition du repère de Frenet et donner l'expression du vecteur accélération $\vec{a}$ de l'objet $O$ dans ce repère.

7. En déduire que la valeur $v$ de la vitesse de l'objet reste constante au cours du mouvement.

8. Montrer que la valeur $v$ de la vitesse de l'objet a pour expression 
$$
 v = \sqrt{\dfrac{GM}{r}}
$$

9. Rappeler la définition de la période de révolution $T$ de l'objet $O$ au cours de son mouvement et donner son expression, en fonction de $G$, $M$, et $r$.

10. Montrer qu'à la question précédente on a retrouvé la troisième loi de Kepler, pour le cas des mouvements circulaires.

### Disposition d'une série d'objets ponctuels sur une même orbite

<img src="/terminales-pc/chap-8/chap-8-7/chap-8-7-3.png" alt="" width="30%" />

Soit un chapelet d'objets, assimilables à des points matériels, mais de tailles et de *masses différentes*, satellisés autour de Saturne sur une même orbite circulaire de rayon $r$ qu'ils parcourent tous dans le même sens.

La figure ci-dessus donne la configuration de ces objets à un instant donné (les échelles de taille des objets par rapport à Saturne n'ont pas été respectées). On fait l'hypothèse que les interactions gravitationnelles entre ces objets sont négligeables et que seule celle avec Saturne intervient.

11. Tous ces objets ont-ils la même vitesse sur l'orbite ? Justifier.

12. Comment évolue la structure de l'ensemble au cours du temps ?

### Disposition de deux objets ponctuels sur deux orbites de rayons différents

<img src="/terminales-pc/chap-8/chap-8-7/chap-8-7-4.png" alt="" width="30%" />

Soient deux objets $A$ et $B$, assimilables à des points matériels, satellisés autour de Saturne sur deux orbites circulaires de rayon $r\_{A}$ et $r\_{B}$ différents ($r\_{A} > r\_{B}$) mais de valeurs voisines. La figure ci-dessus donne la configuration de ces objets à un instant $t$ : ils sont disposés de façon que la direction $(AB)$ passe par $S$, le centre de Saturne ; la flèche indique le sens du mouvement (les échelles des rayons n'ont pas été respectées). On considère que l'interaction gravitationnelle entre ces deux objets est négligeable et que seule celle avec Saturne intervient.

À une date ultérieure, l'objet satellite $B$ a effectué exactement une révolution autour de Saturne. On souhaite savoir où se trouve l'objet $A$ sur son orbite.

13. Indiquer en justifiant la réponse, laquelle des trois configurations proposées ci-dessous est possible :

<img src="/terminales-pc/chap-8/chap-8-7/chap-8-7-5.png" alt="" width="" />

### Les anneaux de Saturne

14. À l'aide de l'étude qui précède, en supposant valides les hypothèses faites dans la partie 1.3., montrer que si les anneaux de Saturne ont été à un moment donné d'un seul tenant (soudés les uns aux autres), il est peu probable qu'ils aient pu le rester par la suite.

## La mission Cassini-Huygens

À la fin des années 1980, la NASA et l'Agence spatiale européenne ont planifié une mission conjointe ayant pour objectifs l'étude des principaux corps célestes présents dans le système saturnien : Saturne, ses anneaux, Titan (le plus gros satellite de Saturne),  et leurs interactions. Après des années de recherche et de construction, le 15 octobre 1997 une fusée transportant la sonde spatiale (constituée de l'orbiteur Cassini et l'atterrisseur Huygens) a été lancée. En 2004 cette sonde spatiale s'est placée en orbite autour de Saturne et finalement, en 2005, l'atterrisseur européen Huygens, après s'être détaché de la sonde mère, s'est posé à la surface de la lune Titan, et est parvenu à retransmettre des informations collectées durant la descente et après son atterrissage. L'orbiteur Cassini est resté en orbite autour de Saturne, et a poursuivi l'étude scientifique de la planète géante, en profitant de ses passages à faible distance de ses satellites pour collecter des données détaillées sur ceux-ci, jusqu'en 2017.

### Atterrissage en douceur de Huygens
 
L'atterrisseur Huygens s'est désolidarisé de l'orbiteur à $\pu{1270 km}$ d'altitude au dessus de Titan. Arrivé dans la haute atmosphère de Titan, à plus de $\pu{20000 km.h-1}$ et seulement freiné par ses boucliers thermiques, l'atterrisseur a alors progressivement ralenti grâce à une succession de parachutes. *À $\pu{110 km}$ d'altitude, le parachute final s'est ouvert alors que la vitesse de Huygens était égale à $v\_{0} = \pu{95,0 m.s-1}$ ; le mouvement est alors très rapidement devenu rectiligne et vertical, jusqu'à l'arrivée au sol, sur une surface solide mais molle, à la vitesse $v\_{F} = \pu{6,0 m.s-1}$.* 

#### Données
- Masse de Huygens : $m = \pu{320 kg}$ ;
- Masse de Titan : $m\_{T} = \pu{1,35e23 kg}$ ;
- Champ de pesanteur de Titan : $g\_{T} = \pu{1,35 m.s-2}$.
- La trajectoire est matérialisée par un axe vertical $(z' Oz)$ orienté vers le haut, dont l'origine $O$ se trouve au niveau du sol de Titan. 
- La poussée d'Archimède est négligeable dans ce problème.
- Le mouvement de Huygens sera étudié dans un référentiel titanocentrique considéré galiléen.

15. Quelles sont les deux forces qui agissent sur l'atterrisseur dans la dernière phase du mouvement (phrase en italique dans le texte ci-dessus).
 
16. Calculer la valeur de la variation de l'énergie mécanique du système lors de cette dernière phase.

17. On suppose que la force de frottement fluide reste constante lors de cette dernière phase. Déduire de la question précédente la valeur du travail de cette force lors de toute cette phase.

18. En déduire finalement la valeur de la force de frottement.

### Défaut de conception du système de communication entre Cassini et Huygens

Comme Huygens n'avait pas la taille nécessaire pour émettre directement ses informations à destination de la Terre, il était prévu qu'il transmette ses données télémétriques, au cours de sa traversée de l'atmosphère de Titan, par radio à Cassini. Ce dernier devait alors relayer les données vers la Terre à l'aide de son antenne principale de $\pu{4 m}$ de diamètre. *Le système de communication entre Huygens et Cassini a été testé sur Terre avant le lancement (émetteur et récepteur étant alors immobiles), sans poser le moindre problème. Le lancement effectué, deux ingénieurs du projet ont cependant très vite découvert que ce système n'avait pas suffisamment bien pris en compte le fait que, lors de la descente, la vitesse de Huygens par rapport à Cassini, importante, entraînerait une modification du signal émis par Huygens.* 

19. Expliquer quelle modification sur le signal émis par Huygens pourrait résulter de son mouvement par rapport à Cassini. En particulier, nommer le phénomène et indiquer quelle caractéristique du signal est affectée.\
Tout élément de réponse sera pris en compte.

## Corrigé

{{% solution "Corrigé" %}}
{{< remote "Corrigé au format pdf" "/terminales-pc/chap-8/chap-8-7/chap-8-7-6.pdf" >}}
{{% /solution %}}