---
title: "Décrire un système thermodynamique : exemple du modèle du gaz parfait"
subtitle: "Chapitre 13,1"
author: ""
type: ""
date: 2021-02-21T04:32:27+04:00
draft: false
toc: true
tags: []
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Le langage de la thermodynamique

### Système

- On désigne ainsi l'objet d'étude ; il s'agit en général d'un système matériel, une « portion d'Univers ».\
Le système est défini par séparation avec le reste de l'Univers appelé le milieu extérieur.

- Un système thermodynamique est plus riche qu'un système mécanique ; il ne peut généralement pas être uniquement décrit, après modélisation, par un simple ensemble de paramètres géométriques : positions, vitesses, orientations, ... des constituants. Sa description nécessite l'introduction d'autres grandeurs fondamentales ; l'une d'elles est la **température**.

### Système isolé, ouvert, fermé

{{% note tip %}}
- On dit qu'un système est **isolé** s'*il ne peut échanger quoi que ce soit avec le milieu extérieur*.
{{% /note %}}

Les échanges d'un système avec l'extérieur peuvent être classés en :
- *échange de matière* ;
- *échange d'énergie* sous des formes diverses que nous aurons à distinguer et classer en *travail* et *transfert thermique ou « chaleur »* ;
- *échange de volume*.

- Un système qui *peut échanger de la matière avec le milieu extérieur* est dit **ouvert** ; dans le cas contraire il est dit **fermé**.

### Système homogène, inhomogène

Si le système est identique en tout point, c'est-à-dire si *les paramètres qui le décrivent sont les mêmes en tout point*, le système est dit **homogène**. Dans le cas contraire. il est **inhomogène**.

{{% note warning %}}
La pesanteur peut être une cause d'inhomogénéité dans un fluide en équilibre ; l'homogénéité n'est alors assurée que pour des systèmes de hauteur suffisamment faibles.
{{% /note %}}

### États d'un système

{{% note tip %}}

- On appelle **état microscopique** d'un système thermodynamique la connaissance, à un instant donné, des positions, des vitesses, des orientations, etc., de toutes les molécules qui le constituent.

{{% /note %}}

Le dénombrement des état microscopiques dans lesquels un système peut se trouver doit être effectué dans le cadre de la mécanique quantique et est à la base de la thermodynamique (ou physisque) statistique.

{{% note exercise %}}
On considère un système constitué de $\pu{3 g}$ d'eau, par exemple contenue dans un petit cylindre fermé par un piston mobile, qui permet de faire varier la pression.

1. Quel est l'ordre de grandeur du nombre de molécules d'eau dans le système ?

On considère, en première approximation, que les molécules d'eau n'ont aucune structure interne ; ce sont des points matériels.

2. En utilisant les connaissances acquises en mécanique (lois de Newton), indiquer combien de paramètres il faut utiliser pour décrire un état microscopique de ce système.

On considère, en seconde approximation, la molécule d'eau telle qu'elle existe : trois atomes associés occupant un certain volume dans l'espace.

3. Cette seconde modélisation augmente-t-elle ou diminue-t-elle le nombre de paramètres dont la connaissance est nécessaire pour la description d'un état microscopique du système.

4. Peut-on, selon vous, décrire et suivre l'évolution de l'état microscopique d'un système thermodynamique ?
{{% /note %}}

{{% solution "Réponses" %}}

1. $N=\dfrac{m}{M}=\dfrac{\pu{3 g} \times \pu{6,02e23 mol-1}}{\pu{18,0 g.mol-1}} \approx \pu{1e23}$.
2. Il faut trois coordonnées de position et trois coordonnées de vitesse pour chacune des particules. Au total, il faut connaître $\pu{6e23}$ paramètres pour pouvoir décrire un état microscopique du système.
3. Lorsqu'on prend tous les paramètres en considération, on doit tenir compte, en plus des seules positions et vitesses, des vibrations de la molécule, de ses rotations, des excitations au niveau électronique, des charges électriques partielles, etc. Le nombre de paramètre augmente donc beaucoup.
4. Même si l'on parvenait à accumuler toutes les informations nécessaires à la description d'un état microscopique du système, aucun ordinateur (actuel ou à venir) ne parviendrait à les manipuler.
{{% /solution %}}

{{% note tip %}}

- On appelle état macroscopique d'un système thermodynamique la connaissance, à un instant donné, des quelques grandeurs macroscopiques qui permettent de décrire ce système.
- La description macroscopique d'un système simple ne réclame la *connaissance que d'un petit nombre de paramètres*. C'est l'expérience qui permet de déterminer le nombre $n$ de paramètres nécessaires et suffisants pour décrire le système : on dit que ce sont des **variables d'état indépendantes**.

{{% /note %}}

Parmi ces variables figurent des **paramètres mécaniques** (*pression*, *volume*) ou **électriques** (*charge électrique*, *potentiel électrique*) mais aussi des grandeurs typiquement thermodynamiques dont l'introduction est nécessaire pour *pallier l'ignorance que l'on s'impose du comportement microscopique du système* ; ce sont la **température** et l'**entropie**.

### État d'équilibre

{{% note normal %}}
On dit qu'un système est en équilibre lorsque toutes ses variables d'état demeurent constantes au cours du temps, et si, lorsqu'il n'est pas isolé, il n'existe aucun échange (matière, énergie, charge électrique, etc.) avec le milieu extérieur.
{{% /note %}}

### Équilibre thermique, température

Considérons deux systèmes $A$ et $B$, *à parois fixes*, initialement isolés. Mettons-les en contact par l'intermédiaire d'une cloison commune fixe et imperméable à toute matière. On observe le plus souvent une évolution jusqu'à un nouvel état d'équilibre caractérisé pour $A$ et $B$ par des valeurs finales de leurs paramètres différentes de leurs valeurs initiales.
- Le système total est isolé ; 
- Il n'y a pas eu d'échange de travail entre $A$ et $B$ puisque la cloison commune est fixe ;
- Un échange d'énergie entre eux a eu lieu puisque les variables d'état ont évolué.

{{% note tip %}}
- On appelle **transfert thermique** (ou **chaleur**) *l'échange d'énergie entre deux système qui n'est pas du travail (soit qui n'implique pas le déplacement du point d'application d'une force)*.
- Lorsque l'équilibre final est atteint par transfert thermique, on dit que les deux systèmes sont en **équilibre thermique**.
{{% /note %}}

{{% note warning %}}
L'équilibre thermodynamique impose l'équilibre mécanique (électrique, etc.) mais aussi l'équilibre thermique.
{{% /note %}}

{{% note normal %}}
Deux systèmes en équilibre thermique avec un même troisième sont en équilibre thermique entre eux.
{{% /note %}}

On dit alors que deux systèmes en équilibre thermique sont à la même température. On peut alors associer à chaque état thermique, donc à chaque température, un nombre. Cela se fait en choisissant un système particulier, le **thermomètre**, puis un paramètre de ce système dépendant de l'état thermique (pression, longueur, résistance électrique, volume, etc.) et enfin en y associant par une loi (comportant un certain degré d'arbitraire) un nombre qui sera la température associée à un état thermique. On a alors construit ce que l'on appelle une *échelle de températures*.

{{% note tip %}}
La température est ainsi une grandeur macroscopique caractéristique d'un état d'équilibre thermique. 
{{% /note %}}


## Un système modèle : le gaz parfait

Les fluides, et tout particulièrement les fluides gazeux, sont des exemples de systèmes privilégiés dans tout exposé des bases de la thermodynamique. L'une des raisons est qu'*un très faible nombre de paramètres suffit pour décrire leur état macroscopique*. De plus, pour les gaz, un modèle simple permet de décrire la réalité avec une approximation satisfaisante dans de très nombreux cas ; c'est le modèle du *gaz parfait*.

### Modèle du gaz parfait

{{% note tip %}}
À tout gaz réel, monoatomique ou non, on associe un gaz parfait, gaz idéal dont les molécules :

- sont les mêmes que celles du gaz réel ;
- sont **considérées comme ponctuelles** et n'ont **pas d'interaction à distance** entre elles.
{{% /note %}}

### Signification de la température dans le cadre du modèle du gaz parfait

On peut montrer que dans un gaz parfait l'**énergie cinétique moyenne** des molécules prend une valeur qui *ne dépend que de l'état thermique dans lequel se trouve ce gaz*.

{{% note tip %}}
Dans le cadre du modèle du gaz parfait la *température est une grandeur macroscopique qui traduit le degré d'agitation au niveau microscopique*.
{{% /note %}}

### Équation d'état des gaz parfaits

{{% note tip %}}
- L'expérience montre que deux variables d'état suffisent pour décrire l'état macroscopique d'un gaz parfait si le système est fermé.

- L'équation d'état des gaz parfaits relie entre elles toutes les variables d'état d'un gaz parfait : pression $P$ (en $\pu{Pa}$, volume $V$ (en $\pu{m3}$), température $T$ (en $\pu{K}$) et quantité de matière $n$ (en $\pu{mol}$) :
$$
    P\\, V = n \\, R\\, T
$$
avec $R$, constante des gaz parfaits. La valeur de la constante des gaz parfaits précise l'échelle de température.
$$
    R = \pu{8,31441 J.K-1.mol-1}
$$
{{% /note %}}

**Remarque :** L'unité de la constante des gaz parfaits montre que le produit $P\\, V$ a la dimension d'une énergie.

{{% note normal %}}
L'échelle absolue des température est le **kelvin**. Pour les usages courants, on utilise souvent le degré Celsius ; la relation est alors
$$
    \theta(\pu{°C}) = T(\pu{K}) - \pu{273,15 K}
$$
{{% /note %}}

**Remarque :** À une température $T$ donnée, le produit $P\\,V$ est constant *quelle que soit la pression* ; c'est la *loi de Boyle-Mariotte*.

{{% note exercise %}}
Le modèle du gaz parfait est celui généralement utilisé en chimie. Déterminer le volume molaire d'un gaz à la température de $\pu{0 °C}$ et sous la pression atmosphérique.

**Remarque :** $\pu{1 atm} = \pu{1,01325e5 Pa}$.
{{% /note %}}

{{% solution "Réponse" %}}
Puisqu'on utilise le modèle du gaz parfait,
$$V\_m = \dfrac{V}{n} = \dfrac{R\\, T}{P}$$

**A.N.** $V\_m = \dfrac{\pu{8,31441 J.K-1.mol-1} \times \pu{273,15 K}}{\pu{1,01325e5 Pa}} = \pu{2,2414e-2 m3.mol-1} = \pu{22,414 L.mol-1}$.
{{% /solution %}}


### Masse volumique et densité des gaz dans le cadre du modèle du gaz parfait

{{% note exercise %}}
L'équation d'état des gaz parfait permet d'exprimer simplement la masse volumique de ce gaz en fonction de la pression, de la température et de sa masse molaire.\
Retrouver cette expression.
{{% /note %}}
{{% solution "Réponse" %}}
$P\\, V = n\\, R\\, T = \dfrac{m}{M}\\, R \\, T$. Comme $\rho = \dfrac{m}{V}$ donc 
$$\rho = \dfrac{P\\, M}{R\\, T}$$
{{% /solution %}}

{{% note exercise %}}
La masse molaire de l'air (lorsque toutes les molécules sont considérées en fonction de leurs poids) est égale à $M = \pu{28,96 g.mol-1}$.\
Calculer la masse volumique $\rho_0$ de l'air à la température de $\pu{0 °C}$ et sous la pression atmosphérique.

**Remarque :** $\pu{1 atm} = \pu{1,01325e5 Pa}$.
{{% /note %}}
{{% solution "Réponse" %}}
$\rho_0 = \dfrac{\pu{1,01325e5 Pa} \times \pu{28,96e-3 kg.mol-1}}{\pu{8,31441 J.K-1.mol-1} \times \pu{273,15 K}} = \pu{1,29 kg.m-3} = \pu{1,29 g.L-1}$.
{{% /solution %}}

{{% note exercise %}}
Déterminer l'expression de la masse volumique $\rho$ d'un gaz à une température $T$ sous la pression $P$ en fonction de sa masse volumique $\rho_0$ à la température $T_0$ sous la pression $P_0$.
{{% /note %}}
{{% solution "Réponse" %}}
$\rho = \dfrac{P\\, M}{R\\, T}$ donc $\dfrac{M}{R} = \dfrac{\rho\\, T}{P}$. Finalement $\dfrac{\rho\\, T}{P} = \dfrac{\rho_0\\, T_0}{P_0}$ ou
$$
    \rho = \rho_0\\, \dfrac{P\\, T_0}{P_0\\, T}
$$
{{% /solution %}}

{{% note tip %}}
On appelle densité d'un gaz par rapport à l'air le rapport 
$$
    d = \dfrac{\text{masse d'un certain volume du gaz}}{\text{masse du même volume d'air}}
$$
la mesure étant faite dans les mêmes conditions de température et de pression.
{{% /note %}}

{{% note exercise %}}
Exprimer la densité d'un gaz en fonction 
- de sa masse volumique $\rho$ et de la masse volumique $\rho'$ de l'air ;
- de sa masse molaire $M$ et de la masse molaire $M'$ de l'air.
{{% /note %}}
{{% solution "Réponse" %}}
- $d = \dfrac{\rho}{\rho'}$
- $d = \dfrac{P\\, M}{R\\, T} \cdot \dfrac{R\\, T}{P\\, M'} = \dfrac{M}{M'}$
{{% /solution %}}


## Limites du modèle du gaz parfait

Le modèle du gaz parfait ne prend pas en compte :
- la structure interne des molécules qui constituent le gaz (en particulier leur volume) ;
- les interactions entre les molécules.

En réalité il existe des forces petites, certes, mais pas tout à fait négligeables.

- Lorsque les molécules sont polaires ($\ce{NH3}$, $\ce{H2O}$, etc.), elles ont tendance à **s'attirer**. En fait, même en l'absence de moment dipolaire (cas de molécules à symétrie parfàitement sphérique comme celles des gaz rares), on montre qu'il subsiste une attraction résiduelle (force dite de Van der Waals-London).\
On admet que dans de nombreux cas la force attractive qui s'exerce entre deux molécules varie en fonction de leur distance comme $1/r^7$. Cette force tend assez rapidement vers zéro quand $r$ croît, et est donc à très court rayon d'action.

- Parallèlement, lorsque les molécules se rapprochent trop leurs nuages électroniques ne peuvent pas se recouvrir aisément : pour les très faibles distances $r$, les molécules ont donc tendance à se repousser.

D'autre part les molécules, n'étant pas ponctuelles, ne disposent en réalité, pour se déplacer, que d'un volume inférieur au volume $V$ du récipient.

Le modèle du gaz parfait ne modélise correctement le comportement d'un gaz réel que dans les situations ou les caractéristiques ci-dessus peuvent être négligées, c'est à dire **lorsque la pression à laquelle est soumis le gaz est faible**.

{{% note tip %}}
*À basse pression, tous les gaz peuvent être modélisés par un gaz parfait*. Lorsque la pression augmente, on ne peut plus négliger les *interactions à courte distance*, notamment l'*effet de taille des molécules* et les *interactions de type van der Waals*.
{{% /note %}}

## Exercices

{{% note exercise %}}
Quelle est la masse d'air contenue dans une pièce de $\pu{5 m} \times \pu{3 m} \times \pu{3 m}$ à $\pu{20 °C}$ sous la pression atmosphérique ?
{{% /note %}}



{{% note exercise %}}
Quelle est la densité par rapport à l'air d'un mélange gazeux renfermant $\pu{88 g}$ de $\ce{CO2}$, et $\pu{14 g}$ de $\ce{CO}$ ?
{{% /note %}}

{{% note exercise %}}
La pression d'un pneumatique est ajustée l'hiver à $\pu{-10 °C}$ à $\pu{2 atm}$ (pression préconisée « à froid » par le constructeur). Sachant que le constructeur est capable de ressentir les effets néfastes d'un écart de 10&nbsp;% par rapport à cette pression, sera-t-il nécessaire de corriger celle-ci l'été lorsque la température sera devenue $\pu{30 °C}$.
{{% /note %}}


{{% note exercise %}}

1. Quel est le volume occupé par $\pu{1 g}$ de dibrome (molécule $\ce{Br2}$) à $\pu{600 °C}$ sous la pression atmosphérique, en supposant que c'est un gaz parfait ?\
On donne la masse molaire de l'élément brome : $\pu{80 g.mol-1}$.\
À cette température on peut négliger la dissociation des molécules.

2. Que deviendrait ce volume à $\pu{1600 °C}$, toujours sous la pression atmosphérique, en supposant que l'on peut encore négliger la dissociation ?

3. L'expérience montre que ce volume est en fait $\pu{1,195 L}$. Montrer que cela peut s'expliquer en considérant qu'une certaine proportion des molécules $\ce{Br2}$, s'est dissociée en atomes de brome. Calculer le coefficient de dissociation (proportion de molécules dissociées).
{{% /note %}}