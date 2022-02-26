---
title: "Caractère ondulatoire de la lumière d’après Huyghens"
subtitle: "Chapitre 3,2,4"
author: ""
type: ""
date: 2020-09-14T22:51:28+04:00
draft: false
toc: true
tags: ["Annale", "Diffraction"]
categories: ["Physique", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: true
auto_numbering: true
---
[^1]: de toutes parts = dans toutes les directions.
[^2]: de tout opposés = de sens opposés.
[^3]: sans s’empêcher = sans se perturber.
[^4]: ne saurait être = ne se fait pas

Le texte ci-dessous retrace succinctement l’évolution de quelques idées à propos de la nature de la lumière. Extraits d’articles parus dans l’ouvrage «&nbsp;Physique et Physiciens&nbsp;» et dans des revues «&nbsp;Sciences et vie&nbsp;».

----
Huyghens (1629-1695) donne à la lumière un caractère ondulatoire par analogie à la propagation des ondes à la surface de l’eau et à la propagation du son.  
Pour Huyghens, le caractère ondulatoire de la lumière est fondé sur les faits suivants&nbsp;:
- «&nbsp;le son ne se propage pas dans une enceinte vide d’air tandis que la lumière se propage dans cette même enceinte. La lumière consiste dans un mouvement de la matière qui se trouve entre nous et le corps lumineux, matière qu’il nomme éther&nbsp;»&nbsp;;
- «&nbsp;la lumière s’étend de toutes parts[^1] et, quand elle vient de différents endroits, même de tout opposés[^2], les ondes lumineuses se traversent l’une l’autre sans s’empêcher[^3]&nbsp;»&nbsp;;
- «&nbsp;la propagation de la lumière depuis un objet lumineux ne saurait être[^4] par le transport d’une matière qui depuis cet objet s’en vient jusqu’à nous ainsi qu’une balle ou une flèche traverse l’air&nbsp;». 

Fresnel (1788-1827) s’attaque au problème des ombres et de la propagation rectiligne de la lumière. Avec des moyens rudimentaires, il découvre et exploite le phénomène de diffraction. Il perce un petit trou dans une plaque de cuivre. Grâce à une lentille constituée par une goutte de miel déposée sur le trou, il concentre les rayons solaires sur un fil de fer.

----

## Exploitation du document

1. Quelle erreur commet Huyghens en comparant la propagation de la lumière à celle des ondes mécaniques&nbsp;?
{{% solution "Réponse" %}}
Huyghens pense que la lumière est une onde mécanique, c'est à dire la propagation d'une perturbation de proche en proche sans transport de matière. Le milieu perturbé est l'éther, une substance spéciale et invisible qui remplirait l'Univers.  
La théorie de la relativité d'Einstein a éliminé la possibilité d'existence de l'éther en tant milieu matériel.
{{% /solution %}}

2. Citer deux propriétés générales des ondes qu’on peut retrouver dans le texte de Huyghens.
{{% solution "Réponse" %}}
- Les ondes peuvent se croiser sans se perturber.
- Les ondes se propagent sans transport de matière.
- Les ondes se propagent dans toutes les directions accessibles.
{{% /solution %}}

3. Fresnel a utilisé les rayons solaires pour effectuer son expérience. Une telle lumière est-elle monochromatique ou polychromatique&nbsp;? Justifier la réponse en faisant référence à un fait expérimental ou naturel connu.
{{% solution "Réponse" %}}
La lumière en provenance du Soleil est polychromatique, c'est à dire *la superposition d'une infinité d'ondes sinusoïdales*.  
Le caractère polychromatique de la lumière issue du Soleil apparaît lorsqu'elle est réfractée et décomposée par des gouttes d'eau dans l'atmosphère. On obtient alors un arc-en-ciel.
{{% /solution %}}

4. Fresnel exploite le phénomène de diffraction de la lumière par un fil de fer. Le diamètre du fil a-t-il une importance pour observer le phénomène de diffraction&nbsp;?  
Si oui, indiquer quel doit être l’ordre de grandeur de ce diamètre.
{{% solution "Réponse" %}}
Pour que le phénomène de diffraction soit réellement visible il faut que la dimension de l'objet diffractant soit du même ordre de grandeur que la longueur d'onde de l'onde considérée.
{{% /solution %}}

## Diffraction

<img src="/terminales-pc/chap-2/fig-2-2-4-1.jpg" alt="" width="50%" style="float: left;" />
On réalise une expérience de diffraction à l’aide d’un laser émettant une lumière monochromatique de longueur d’onde $\lambda$. À quelques centimètres du laser, on place successivement des fils verticaux de diamètres connus. On désigne par $a$ le diamètre d’un fil. La figure de diffraction obtenue est observée sur un écran blanc situé à une distance $D = \pu{1,60 m}$ des fils. Pour chacun des fils, on mesure la largeur $L$ de la tache centrale.

À partir de ces mesures et des données, il est possible de calculer l’écart angulaire $\theta$ du faisceau diffracté.

5. L’angle $\theta$ étant petit, on considère que $\tan \theta \simeq \theta$. Donner la relation entre $L$ et $D$ qui permet de calculer $\theta$ pour chacun des fils.
{{% solution "Réponse" %}}
- $L$ et $D$ sont des dimensions caractéristiques du montage expérimental.  
- Le montage fait apparaître le triangle rectangle tel $\tan \theta = \dfrac{L/2}{D} = \dfrac{L}{2D}$. 
- Comme l’angle $\theta$ est petit, $\tan \theta \simeq \theta$ et $\theta \simeq \dfrac{L}{2D}$. Une mesure de $L$ et de $D$ permet de calculer la valeur de l'angle $\theta$ (en radians).
{{% /solution %}}

6. Donner la relation liant $\theta$ à $\lambda$ et $a$. Préciser les unités de $\theta$, $\lambda$ et $a$.
{{% solution "Réponse" %}}
La relation liant l'angle $\theta$ et $a$ la dimension de l'objet diffractant est&nbsp;: $\theta \simeq \dfrac{\lambda}{a}$.  
Dans cette relation $\theta$ doit être exprimé en radians, $\lambda$ et $a$ en mètres (ou tout au moins dans la même unité de longueur).
{{% /solution %}}

On trace la courbe $\theta = f(1/a)$ (les ordonnées sont exprimées en radian et les abscisses en «&nbsp;par mètre&nbsp;»).   
<img src="/terminales-pc/chap-2/fig-2-2-4-2.jpg" alt="" width="80%" />

7. Montrer que cette courbe est en accord avec l’expression de $\theta$ donnée à la question 6.
{{% solution "Réponse" %}}
- La relation $$\theta = \dfrac{\lambda}{a}$$ montre que $theta$ est inversement proportionnel à $a$.  
- Si on effectue le changement de variable $u = \dfrac{1}{a}$, la relation précédente devient&nbsp;: $$\theta = \lambda u$$ $\theta$ est proportionnel à $u$.  
- Lorsqu'on trace $\theta$ en fonction de $\dfrac{1}{a}$, comme sur le graphique, on trace en fait $\theta$ en fonction de $u$. C'est donc normal de parvenir à une relation linéaire après traitement des résultats.
{{% /solution %}}

8. Comment, à partir de la courbe précédente, pourrait-on déterminer la longueur d’onde $\lambda$ de la lumière monochromatique utilisée&nbsp;?
{{% solution "Réponse" %}}
Dans la relation $\theta = \lambda u$, $\lambda$ est le *coefficient de proportionnalité*, soit la *pente de la droite* sur le graphique.
{{% /solution %}}

9. En exploitant la courbe, préciser parmi les valeurs de longueurs d’onde proposées, quelle est celle de la lumière utilisée&nbsp;: $\pu{560 cm}$, $\pu{560 mm}$, $\pu{560 \mu m}$, $\pu{560 nm}$.
{{% solution "Réponse" %}}
$\theta = \pu{1,5e-2 rad}$ lorsque $u = \dfrac{1}{a} = \pu{2,6e4 m-1}$ donc comme $\lambda = \dfrac{\theta}{u}$, $ \lambda =  \dfrac{\pu{1,5e-2 rad}}{\pu{2,6e4 m-1}} = \pu{5,8e-7 m}$.  
La longueur d'onde du laser est donc $\lambda = \pu{560 nm}$.
{{% /solution %}}

