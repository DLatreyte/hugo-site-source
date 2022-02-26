---
title: "Les interactions qui gouvernent l'Univers"
subtitle: "Chapitre 7,1"
author: ""
type: ""
date: 2021-01-27T08:46:53+04:00
draft: false
toc: true
tags: []
categories: ["Premières Spé PC", "Physique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## La matière à différentes échelles

{{% note tip %}}
L'**ordre de grandeur** d'une grandeur physique est une représentation simplifiée et approximative du résultat de la mesure de cette grandeur : **c'est la puissance de 10 la plus proche de ce résultat**.
{{% /note %}}


Les ordres de grandeurs de différentes grandeurs de même nature permettent de les comparer rapidement.

#### Quelques ordres de grandeur :

- Rayon moyen d'un noyau : $\pu{10^{-15} m}$ ;

- Rayon moyen d'un atome : $\pu{10^{-10} m}$ ;

- Longueur moyenne d'une bactérie : $\pu{10^{- 6} m}$ ;

- Taille d'un être humain : $\pu{1 m}$ ;

- Rayon de la Terre : $\pu{10^7 m}$ ;

- Diamètre de la Voie Lactée : $\pu{10^{21} m}$.

{{% note tip %}}
#### Détermination d'un ordre de grandeur :

1. Écriture de la valeur en notation scientifique :
    $$a \times 10^n  \qquad \text{avec} \qquad 1 \le a < 10$$

2. Détermination de la puissance de 10 : 
$$
   \begin{cases}
        a < 5 & \text{l'ordre de grandeur est } 10^n \cr
        a \geqslant 5 & \text{l'ordre de grandeur est } 10^{n + 1} 
\end{cases}
$$
{{% /note %}}


##### Exemples :

1. Le rayon de l'atome d'hydrogène vaut $r = \pu{53 pm}$. Donner son ordre de grandeur.
{{% solution "Réponse" %}}
$r = \pu{53 pm} = \pu{5,3e-11 m} \approx \pu{10^{- $10} m}$
{{% /solution %}} 

2. Le diamètre d'une molécule d'ADN vaut $d = \pu{2 nm}$. Donner son ordre de grandeur.
{{% solution "Réponse" %}}
$d = \pu{2 nm} = \pu{2e-9 m} \approx \pu{10^{-9} m}$.
{{% /solution %}}

3. La longueur d'une molécule d'ADN dépliée vaut $l = \pu{2 m}$. Donner son ordre de grandeur.
{{% solution "Réponse" %}}
$l = \pu{2 m} \approx \pu{1}{m}$.
{{% /solution %}}


## Charge  élémentaire


{{% note tip %}}

- La charge électrique élémentaire est notée $e$ et a pour valeur, en **coulomb**, 
$$
    e = \pu{1,602176565(35)}\cdot\pu{10^{-19} C}
$$
- Depuis sa première mesure par Robert Millikan en 1909, *la charge élémentaire est considérée comme indivisible*. Toute charge électrique $Q$ peut donc s'écrire : 
$$
    Q = n\\, e
$$ 
où $n$ est un nombre entier relatif.
{{% /note %}}

- La **charge élémentaire** est la *charge électrique d'un proton*. C'est aussi l'opposé de la charge électrique d'un électron.

{{% note normal %}}
Les **quarks**, *constituants des nucléons*, possèdent une charge électrique fractionnaire (des multiples
de $e / 3$) mais *ils sont confinés à l'intérieur des *hadrons* (protons, neutrons, etc.)*, *particules dont la charge est un multiple de la charge élémentaire*, et n'ont pour l'instant jamais été détectés libres.
{{% /note %}}


## Interactions fondamentales


Quatre interactions fondamentales sont responsables de *tous les phénomènes physiques observés dans l'Univers* :

- l'interaction *nucléaire forte* ;

- l'interaction *nucléaire faible* ;

- l'interaction *gravitationnelle* ;

- l'interaction *électromagnétique*.

### Interaction gravitationnelle

- L'interaction gravitationnelle concerne les **masses**, *immobiles et/ou en mouvement*. Elle fait intervenir un *champ gravitationnel* (cf. section 3).

- L'interaction gravitationnelle est *toujours attractive*.

- La loi de Newton modélise l'interaction gravitationnelle sous forme d'une force : la force de Newton.

#### La loi de Newton

{{% note tip %}}

L'interaction gravitationnelle entre deux corps *ponctuels* $A$ et $B$, de masses respectives $m_A$ et $m_B$, séparés d'une distance $d$, est modélisée par des forces $\vec{F}\_{A / B}$ et $\vec{F}\_{B / A}$ dont les
caractéristiques sont les suivantes :

- *Point d'application :* $A$ pour $\vec{F}\_{B / A}$ et $B$ pour $\vec{F}\_{A / B}$

- la direction de la droite $(AB)$

- vers le centre attracteur ($A$ pour $\vec{F}\_{A / B}$ et $B$ pour $\vec{F}\_{B / A}$)

- *Valeur :* 
$$
    F\_{A / B} = F\_{B / A} = G \\, \dfrac{m\_A \cdot m\_B}{d^2}
$$ 
    où $m_A$ et $m_B$ sont exprimées en kilogramme
    (kg), $d$ en mètre (m) et $F\_{A / B}$ et $F\_{B / A}$ en newton (N).

    $G$ est appelée **constante de gravitation universelle**, sa valeur est :
    $$G = \pu{6,67e-11 N.m2.kg-2}$$

- Si l'on ne prend pas en compte les points d'application des deux vecteurs, on constate que : $$\vec{F}\_{A / B} = - \vec{F}\_{B / A}$$

{{% /note %}}

#### Représentation des forces.

<img src="/premieres-pc/chap-8/chap-8-1/chap-08-2.png" alt="" width="70%" />

- Si l'on ne prend pas en compte les points d'application des deux vecteurs, on constate que : $$\vec{F}\_{A / B} = - \vec{F}\_{B / A}$$

- La loi de Newton se généralise telle quelle à des corps à répartition de masse sphérique :
<img src="/premieres-pc/chap-8/chap-8-1/chap-08-4.png" alt="" width="80%" />

{{% note tip %}}

#### À retenir.

L'interaction gravitationnelle est **toujours attractive** et de **portée infinie**.

L'interaction gravitationnelle possède la plus faible intensité parmi toutes les interactions : $10^{38}$ fois plus petite que celle l'interaction nucléaire forte.
{{% /note %}}

### Interaction électromagnétique


- L'interaction électromagnétique concerne les **charges
    électriques**, *immobiles et/ou en mouvement*. Elle fait intervenir
    des *champ électrique* et *magnétique*.

- L'interaction électromagnétique peut être *attractive ou répulsive* selon les cas.

- La loi de Coulomb modélise la seule interaction électrique sous forme d'une force : la force électrique.

{{% note tip %}}

#### La loi de Coulomb

L'interaction électrique entre deux corps *ponctuels* $A$ et $B$, portant les charges respectives $q_A$ et $q_B$, séparés d'une distance $d$, est modélisée par des forces $\vec{F}\_{A / B}$ et $\vec{F}\_{B / A}$ dont les caractéristiques sont les suivantes :

- *Point d'application :* $A$ pour $\vec{F}\_{B / A}$ et $B$ pour $\vec{F}\_{A / B}$

- *Direction :* la droite $(AB)$

- *Sens :* dépend du signe des deux charges électriques

- *Valeur :* 
$$
    F\_{A / B} = F\_{B / A} = k \\, \dfrac{|q_A | \cdot |q_B|}{d^2}
$$ 
    où $q_A$ et $q_B$ sont exprimées en **coulomb**
    (C), $d$ en mètre (m) et $F_{A / B}$ et $F_{B / A}$ en newton (N).
    $$k = \pu{9,0e9 N.m2.C-2}$$

{{% /note %}}

##### Représentation des forces

- *Charges de signes opposés : l'interaction est attractive* :
<img src="/premieres-pc/chap-8/chap-8-1/chap-08-6.png" alt="" width="70%" />

- *Charges de mêmes signes, l'interaction est répulsive* :
<img src="/premieres-pc/chap-8/chap-8-1/chap-08-8.png" alt="" width="100%" />

- Si l'on ne prend pas en compte les points d'application des deux vecteurs, on constate que : $$\vec{F}\_{A / B} = - \vec{F}\_{B / A}$$

- La loi de Coulomb se généralise telle quelle à des corps à répartition de masse sphérique (cf. section 3.1).

{{% note tip %}}

#### À retenir

L'interaction électrique entre deux corps est de **portée infinie**. Si les charges électriques *sont de même signe*, elle est **répulsive**, si les charges électriques *sont de signes opposés*, elle est
**attractive**.

L'intensité de l'interaction électrique est environ $10^2$ *fois plus petite que celle de l'interaction forte*.
{{% /note %}}

### Interaction forte

{{% note normal %}}

L'**interaction forte** possède les propriétés suivantes :

- Elle est *attractive* ;

- Elle est responsable de la *cohésion des nucléons* (en fait de toutes les particules de la famille des <a href="https://fr.wikipedia.org/wiki/Hadron" target="_blank"> hadrons</a>) ;

- Elle est donc responsable, indirectement, de la *cohesion des noyaux atomiques* ;

- Elle possède une portée de l'ordre de $\pu{10^{-15} m}$ ;

- Elle est la plus puissante de toutes les interactions connues.
{{% /note %}}

### Interaction faible

{{% note normal %}}

L'**interaction faible** possède les caractéristiques suivantes :

- Elle est responsable d'un des types de radioactivité, la radioactivité $\beta$. Elle joue aussi un rôle important dans la fusion nucléaire (comme au centre du Soleil) ;

- Elle possède une portée de l'ordre de $\pu{10^{-17} m}$ ;

- Elle est $10^{-5}$ fois moins intense que l'interaction forte.
{{% /note %}}

### Domaines de prédominance des différentes interactions

{{% note normal %}}
#### À l'échelle astronomique.

À l'échelle astronomique, la matière est globalement **neutre** alors que les masses sont gigantesques :

- *L'interaction gravitationnelle prédomine à l'échelle astronomique*.

#### De l'échelle microscopique à l'échelle humaine.

De l'échelle microscopique à l'échelle humaine, les masses sont trop petites pour que l'interaction gravitationnelle soit importante. De plus, *localement*, les charges électriques ne se compensent pas :

- *L'interaction électromagnétique prédomine de l'échelle microscopique à l'échelle humaine*.

#### À l'échelle du noyau.

Dans le noyau, les interactions forte, faible et électromagnétique sont présentes. *L'interaction électromagnétique tend à rendre les noyaux instables alors que l'interaction forte, 100 fois plus intense, tend à les stabiliser*.

- *Les interactions forte et faible prédominent à l'échelle des noyaux (pas trop gros).*

- *La stabilité d'un noyau est le résultat de la compétition qui existe entre l'interaction forte et l'interaction électromagnétique*.
{{% /note %}}


## Notion de champ

### Champ en physique

{{% note tip %}}

En physique, *un champ est la donnée, pour chaque point de l'espace, de la valeur d'une grandeur physique*.

Cette grandeur physique peut être **scalaire**, c'est à dire un nombre, (température, pression, etc.) ou **vectorielle** (vitesse des particules d'un fluide, champ électrique, etc.).
{{% /note %}}

- Un exemple de **champ scalaire** est donné par la *carte des températures* d'un bulletin météorologique : *la température atmosphérique prend, en chaque point, une valeur particulière.*

- Un exemple de **champ vectoriel** est donné par la carte des vents d'un bulletin météorologique : les particules de fluides possèdent, en chaque point, un vecteur vitesse caractérisé par une direction, un sens et une valeur.

{{% note warning %}}
On définit un champ pour toutes les interactions fondamentales.
{{% /note %}}

{{% note tip %}}
Une **ligne de champ vectoriel** est une *ligne tangente en chacun de ses points au vecteur champ*. Elle est *orientée par une flèche dans le même sens que celui du champ*.
{{% /note %}}

{{% note tip %}}
Un **champ uniforme** est un champ dont *les caractéristiques (direction, sens et valeur) ne dépendent pas du point de l'espace considéré*.
{{% /note %}}

### Champ gravitationnel $\vec{\mathcal{G}}$

<img src="/premieres-pc/chap-8/chap-8-1/chap-08-9.png" alt="" width="50%" />

Considérons, en un point $O$ de l'espace, un objet ponctuel de masse $M$ et, en un point $P$, un objet ponctuel de masse $m$. La force gravitationnelle exercée par la masse $M$ sur la masse $m$ s'écrit :
$$
    \vec{F}\_{M / m} = - G\\, \dfrac{Mm}{r^2}\\,  \vec{u}\_{OP} = m \left( -G\\, \dfrac{M}{r^2}\\, \vec{u}\_{OP} \right)
$$
donc 
$$
   \dfrac{\vec{F}\_{M / m}}{m} = \vec{\mathcal{G}} (P) = - G\\, \dfrac{M}{r^2}\\, \vec{u}\_{OP}
$$ 
{{% note tip %}}
Le vecteur $$\vec{\mathcal{G}} (P) = - G\\, \dfrac{M}{r^2}\\, \vec{u}\_{OP}$$ est appelé **vecteur
champ de gravitation** créé par la masse $M$ en tout point $P$ de l'espace. *Il caractérise une propriété de l'espace due à la présence de l'objet ponctuel de masse $M$ situé en $O$ ; il ne dépend pas de la masse placée en $P$.*
{{% /note %}}

- Comme tout vecteur, le vecteur champ de gravitation $\vec{\mathcal{G}}$ possède une direction, un sens et une valeur.

- Le champ de gravitation s'exprime en mètre par seconde-carré ($\pu{m.s-2}$).

#### Champ gravitationnel en n'importe quel point de l'espace.

$\vec{\mathcal{G}} (P)$ et $\vec{u}\_{OP}$
sont deux vecteurs colinéaires de sens opposés puisque
$- G\\, \dfrac{M}{r^2} < 0$ :

<img src="/premieres-pc/chap-8/chap-8-1/chap-08-10.png" alt="" width="100%" />

{{% note tip %}}
#### À retenir.

Le champ de gravitation, créé en un point $P$ par un objet de masse $M$,
*n'est pas qu'un objet mathématique* ; il **existe même en l'absence de
masse** en $P$.

C'est seulement *en plaçant en* $P$ *une masse témoin* $m$ *que l'on
peut le détecter* ; on mesure alors une force et on en déduit la valeur
du champ.
{{% /note %}}

### Champ électrique $\vec{E}$

<img src="/premieres-pc/chap-8/chap-8-1/chap-08-11.png" alt="" width="50%" />

Considérons, en un point $O$ de l'espace, un objet ponctuel immobile de
charge électrique $Q$ et, en un point $P$, un objet ponctuel immobile de
charge électrique $q$. La force électrique exercée par la charge $Q$ sur
la charge $q$ s'écrit :
$$\vec{F}\_{Q / q} = k \dfrac{Q\\, q}{r^2}\\,  \vec{u}\_{OP} = q\\, \left( k \dfrac{Q}{r^2}  \vec{u}\_{OP} \right)$$
donc $$\dfrac{\vec{F}\_{Q / q}}{q} = \vec{E} (P) = k \dfrac{Q}{r^2}\\, \vec{u}\_{OP}$$ 

{{% note tip %}}
Le vecteur $$\vec{E} (P) = k \dfrac{Q}{r^2}\\, \vec{u}\_{OP}$$ est appelé **vecteur champ électrique** créé par la charge $Q$ en tout point $P$ de l'espace. *Il
caractérise une propriété de l'espace due à la présence de l'objet ponctuel de charge $Q$ situé en $O$ ; il ne dépend pas de la charge
placée en $P$.*
{{% /note %}}

- Comme tout vecteur, le vecteur champ électrique $\vec{E}$ possède une direction, un sens et une valeur.

- Le champ électrique s'exprime en volt par mètre ($\pu{V.m-1}$).


#### Champ électrique en quelques points de l'espace.

- Si $Q > 0$, $\vec{E} (P)$ et $\vec{u}\_{OP}$ sont deux vecteurs colinéaires de même sens puique $k\\, \dfrac{Q}{r^2} > 0$. 
<img src="/premieres-pc/chap-8/chap-8-1/chap-08-12.png" alt="" width="100%" />

- Si $Q < 0$, $\vec{E} (P)$ et $\vec{u}\_{OP}$ sont deux vecteurs colinéaires de sens opposés puique
    $k\\, \dfrac{Q}{r^2} < 0$.
<img src="/premieres-pc/chap-8/chap-8-1/chap-08-13.png" alt="" width="100%" />

{{% note tip %}}
#### À retenir

Le champ électrique, créé en un point $P$ par un objet de charge $Q$,
*n'est pas qu'un objet mathématique* ; il **existe même en l'absence de
charge** en $P$.

C'est seulement *en plaçant en* $P$ *une charge témoin* $q$ *que l'on
peut le détecter* ; on mesure alors une force et on en déduit la valeur
du champ.
{{% /note %}}

## Exercices

### Interactions

{{% note exercise %}}
#### Exercice 1
En 1964, les physiciens M. Gell-Mann et G. Zweig ont avancé l'hypothèse
que les nucléons étaient constitués de trois quarks. Il en existe plusieurs types de quarks, les quarks $u$ (up) portant une charge
$+2/3\\, e$ et $d$ (down) portant une charge $- 1/3\\, e$. Le proton est formé des quarks $u$, $u$, $d$ et le neutron, des quarks $u$, $d$, $d$.
{{% /note %}}

1. Rappeler la valeur de la charge élémentaire.

2. Depuis 1964, peut-on encore parler de $e$ comme étant la charge électrique élémentaire&nbsp;?

3. Vérifier la valeur des charges portées par le proton et le neutron dans cette théorie.

4. Quel type d'interaction permet de maintenir les quarks à l'intérieur des nucléons&nbsp;?

{{% note exercise %}}
#### Exercice 

L'un des modes de fission de l'uranium se produisant dans une centrale
nucléaire est le suivant :

$$
   \ce{ ^235_92U + _0^1n --> _53^139I + _39^94Y + 3 _0^1n } 
$$

On observe l'émission d'un rayonnement $\gamma$, l'éjection de trois neutrons et la formation de deux nouveaux éléments chimiques.
{{% /note %}}

1. Pourquoi cette réaction n'est-elle pas une réaction chimique&nbsp;?

2. Quels sont les deux nouveaux éléments chimiques&nbsp;?

3. Vérifier la conservation du nombre de nucléons.

4. Quelle est l'interaction concernée par cette fission&nbsp;?

5. La fission d'un noyau d'uranium libère environ $\pu{200 MeV}$. Calculer l'énergie libérée par la fission d'une mole de noyaux d'uranium.

6. L'énergie libérée par la combustion d'une mole de carbone est égale à $\pu{393 kJ}$.

7. Quelle est l'interaction concernée par cette combustion&nbsp;?

8. Comparer les valeurs de ces deux énergies. Conclure.

### Interaction gravitationnelle

{{% note exercise %}}
#### Exercice 3

Le Soleil a une masse égale à 
$M\_S = \pu{1,99e30 kg}$. La Terre a une masse égale à $M\_T = \pu{5,98e24 kg}$. Le rayon moyen de l'orbite de la Terre autour du Soleil vaut $\pu{1,49e11 m}$.
{{% /note %}}

1. Pourquoi peut-on appliquer la loi de Newton initialement destinée aux corps ponctuels au cas de l'interaction entre la Terre et le Soleil&nbsp;?

2. Calculer la valeur de la force $\vec{F}\_{S/T}$. Représenter le vecteur sur un schéma en précisant l'échelle.

{{% note exercise %}}
#### Exercice 4
Une boule de pétanque a une masse de $\pu{730 g}$ et un rayon de $\pu{4 cm}$. Le cochonnet a une masse de $\pu{12 g}$ et un rayon de $\pu{1,5 cm}$.
{{% /note %}}

1. Ces corps ont-ils une répartition sphérique de masse&nbsp;?

2. Calculer la valeur de la force d'interaction gravitationnelle s'exerçant entre le cochonnet et la boule, distants de $\pu{20 cm}$.

3. Schématiser la situation et représenter les forces.

{{% note exercise %}}
#### Exercice 5
La Lune est considérée comme un corps à répartition sphérique de masse, de rayon $R\_L = \pu{1740 km}$ et de masse $M\_L = \pu{7,34e22 kg}$.
{{% /note %}}

1. Donner l'expression de la valeur du champ gravitationnel $\vec{\mathcal{G}}\_L$ créé par la Lune à une distance $r \geqslant R\_L$.

2. Calculer la valeur du champ gravitationnel $\vec{\mathcal{G}}\_L$ créé par la Lune à sa surface.

3. Comparer la valeur de $\vec{\mathcal{G}}\_L$ à celle de $\vec{\mathcal{G}}\_T$, champ gravitationnel créé par la Terre à sa surface.

Données

:   $R\_T = \pu{6380 km}$ et
    $M\_T = \pu{5,98e24 kg}$.

4. Lors de la dernière mission lunaire (APOLLO XVII), les astronautes ont ramené $\pu{117 kg}$ de roches. Quel était le poids de ces roches :

    1. à la surface de la Lune&nbsp;?

    2. à la surface de la Terre&nbsp;?

{{% note exercise %}}
#### Exercice 6
Les étoiles à neutrons sont plus denses que le Soleil. Pour une étoile à neutrons de masse double de la masse du Soleil, on évalue son rayon
$R\_N$ à $\pu{10 km}$.

Donnée

:   Masse du Soleil :
    $M\_S = \pu{2e30 kg}$.
{{% /note %}}

1. Calculer la valeur $\mathcal{G}\_N$ du champ de gravitation à la surface de l'étoile à neutrons.

2. Comparer la valeur précédente à celle du champ gravitationnel que crée le Soleil à sa surface : $\mathcal{G}\_S = \pu{270 m.s-2}$.

3. Calculer la valeur de la force exercée sur
    $\pu{1 kg}$ de matière au voisinage de
    la surface de l'étoile à neutrons.

{{% note exercise %}}
#### Exercice 7
Un trou noir résulte de l'effondrement gravitationnel du cœur d'une étoile massive.

« Le rayon d'un trou noir peut être très petit, et évidemment fonction de sa masse : il est de 3&nbsp;km pour un trou noir d'une masse solaire
($M\_S = \pu{2e30 kg}$), et de
$\pu{10^{-27} m}$ pour un trou noir de
$\pu{1 kg}$. »\
(Renaud Foy, *Astronomie Larousse*)
{{% /note %}}

1. Calculer la valeur du champ gravitationnel à la surface de chacun des trous noirs décrits dans la citation ci-dessus.

2. À quelle distance du centre de chacun des trous noirs la valeur du champ gravitationnel serait-elle égale au champ solaire à la surface du Soleil, soit $\pu{270 m.s-2}$&nbsp;?

### Interaction électrique

{{% note exercise %}}
#### Exercice 8
La molécule de dichlore est constituée de deux atomes de chlore dont les noyaux comportent 17 protons. Ces noyaux, considérés comme ponctuels,
sont à une distance $d = \pu{0,198 nm}$
l'un de l'autre.
{{% /note %}}

1. Calculer la valeur des forces d'interaction électrique entre les noyaux.

2. Donner l'expression vectorielle de ces forces et les représenter avec une échelle à préciser.

{{% note exercise %}}
#### Exercice 9

Par beau temps, le champ électrostatique au voisinage de la surface terrestre est quasiment uniforme. Sa valeur est de l'ordre de
$\pu{150 V.m-1}$ et il est dirigé vers le sol.

<img src="/premieres-pc/chap-8/chap-8-1/chap-08-14.png" alt="" width="100%" />

Par temps d'orage, on observe la formation de cumulonimbus. Ces nuages
ont une base quasiment horizontale, chargée négativement. Au voisinage
de cette base, le sol se charge positivement. L'accumulation de charges
électriques est telle que la valeur du champ électrostatique peut
dépasser $\pu{20 kV.m-1}$. Le champ est si intense que l'air est ionisé, ce qui le rend beaucoup plus conducteur qu'habituellement.

Une décharge électrique est donc possible ; c'est l'éclair.
{{% /note %}}

1. Par beau temps, quel est le signe de la charge électrique de la surface du sol&nbsp;?

2. Expliquer pourquoi la surface du sol se charge positivement sous un cumulonimbus.

3. En considérant un sol horizontal et plan, par quoi peut-on modéliser le système formé par le sol et la partie inférieure du cumulonimbus&nbsp;?

4. Que peut-on dire du champ électrostatique entre le sol et la base du nuage&nbsp;?

5. Reproduire le schéma ci-dessus et représenter quelques lignes de champ électrostatique.

{{% solution "Solution" %}}
{{< remote "Corrigés des exercices au format pdf" "/premieres-pc/chap-8/chap-8-1/chap-8-1-15.pdf" >}}
{{% /solution %}}

