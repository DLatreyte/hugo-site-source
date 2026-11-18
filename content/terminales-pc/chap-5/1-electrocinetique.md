---
title: "Rappels d'électrocinétique"
subtitle: "Doc. 5,1"
date: 2020-10-30T20:15:15+04:00
draft: false
toc: true
tags: ["courant électrique", "intensité", "charge électrique", "potentiel électrique", "tension électrique", "analogie hydraulique", "puissance électrique", "dipôle", "nœud", "branche", "maille", "loi d'Ohm", "effet Joule", "loi des nœuds", "loi des mailles"]
categories: ["Physique", "Terminale Spé PC"]
solution_est_visible: true
auto_numbering: true
weight: 100
---
- {{< remote "Énoncé au format pdf" "/terminales-pc/chap-5/5-1/5-1-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/terminales-pc/chap-5/5-1/5-1-corrige.pdf" >}}

{{< note goal "Objectif" >}}
Rappeler les notions de base d'électrocinétique vues dans les classes antérieures : courant, intensité, tension, puissance, loi d'Ohm et lois de Kirchhoff. Ces outils serviront à étudier le dipôle RC.
{{< /note >}}

## Introduction

L'**électrocinétique** est l'*étude de la circulation des courants électriques dans des dispositifs reliés à une alimentation électrique* : l'étude de l'installation électrique d'une maison ou d'un appartement est typiquement un problème d'électrocinétique. Dans le domaine de l'électrocinétique, les circuits sont en général composés d'éléments simples : un *générateur*, des *résistances*, des *inductances* et des *capacités*. On peut également y trouver des transformateurs et d'autres machines électriques. L'objectif est, au final, de distribuer la **puissance électrique délivrée par le générateur (quel qu'il soit) aux différents éléments du circuit**.

## Courant électrique

### Qu'est-ce que le courant électrique ?

{{< question >}}
Qu'appelle-t-on **courant électrique** ?
{{< /question >}}

{{< solution "Réponse" >}}
Un courant électrique est un **mouvement d'ensemble** (ordonné) de *charges électriques*.
{{< /solution >}}

{{< question >}}
  Indiquer quelles sont les charges électriques qui se déplacent dans les différents milieux considérés :

1. dans un conducteur solide ;
1. dans un isolant ;

1. dans une solution électrolytique ;
1. dans un plasma.
{{< /question >}}

{{< solution "Réponse" >}}
1. Les seules charges libres de se déplacer dans les *solides conducteurs* sont les **électrons**.
1. *Aucune charge ne peut se déplacer dans un isolant.* Aucun courant électrique ne circule donc dans les isolants.
1. Les charges électriques capables de se déplacer dans une *solution électrolytique* sont les **ions** (cations et anions). *Il n'existe pas d'électrons libres dans les solutions.*
1. Un plasma (étoile, lampes fluorescentes, etc.) est un gaz dans lequel on a séparé, à l'aide d'un champ électrique, les électrons des noyaux. Ces entités peuvent donc se déplacer (dans des sens opposés).
{{< /solution >}}

{{< question >}}
Quel est le **sens conventionnel** du courant électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
***À l'extérieur du générateur**, le courant électrique circule de la borne positive jusqu'à la borne négative de ce générateur.*
{{< /solution >}}

{{< question >}}
Au déplacement de quel type de charges correspond le **sens conventionnel du courant électrique** ?
{{< /question >}}

{{< solution "Réponse" >}}
Le sens conventionnel du courant électrique a été choisi par Benjamin Franklin à une époque où la constitution de la matière n'était pas connue.

*Le sens du courant électrique est le sens de déplacement des charges positives.*
{{< /solution >}}

### Qu'est-ce que l'intensité du courant électrique ?

![](/terminales-pc/chap-5/5-1/Doc-1.svg?width=30%)

{{< question >}}
Qu'appelle-t-on **intensité $I$ du courant électrique** ?
{{< /question >}}

{{< solution "Réponse" >}}
L'**intensité du courant électrique** est la *charge électrique $Q$ qui traverse une section $S$ du circuit chaque seconde*.

L'**intensité du courant électrique** est donc le *débit de charges électriques à travers une section $S$ du circuit électrique*.
{{< /solution >}}

{{< question >}}
À partir de la définition de l'intensité du courant électrique, établir l'expression de l'**intensité moyenne** $I_\text{moy}$ du courant électrique entre les dates $t$ et $t + \Delta t$ en fonction de la charge $\Delta q$ qui traverse une section $S$ du circuit entre ces deux dates.
{{< /question >}}

{{< solution "Réponse" >}}
L'intensité du courant électrique étant la charge électrique qui traverse une section $S$ du circuit chaque seconde,
$$I_\text{moy} = \frac{q(t + \Delta t) - q(t)}{\Delta t} = \frac{\Delta q}{\Delta t}$$
si on note $\Delta q$ la charge électrique qui traverse la section du circuit pendant les $\Delta t$ secondes, entre $t$ et $t + \Delta t$.

{{< note info "Remarque" >}}
Si l'intensité du courant électrique est indépendante du temps, $I = I_\text{moy}$.
{{< /note >}}
{{< /solution >}}

{{< question >}}
Quelle est l'unité de l'intensité du courant électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
$I$ s'exprime en ampère (A).

{{< note info "Remarque" >}}
1 A $=$ 1 C/s.
{{< /note >}}
{{< /solution >}}

{{< question >}}
Comment et avec quel instrument mesure-t-on l'intensité du courant électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
Pour mesurer l'intensité du courant électrique, on utilise un **ampèremètre**.

L'appareil doit être traversé par le courant électrique pour pouvoir mesurer son intensité. Il doit donc être **placé en série dans la branche** dans laquelle on souhaite mesurer l'intensité du courant électrique.
{{< /solution >}}

**Quelques ordres de grandeur**

| **Courant** | **Composants ou appareils** |
|:---|:---|
| 10 mA | DEL commune |
| 100 mA | Risque d'électrocution |
| 0,5 A | Ampoule à incandescence sous 230 V |
| 10 A | Four, chauffage, chauffe-eau sous 230 V |
| 100 A | Démarreur automobile |
| 10 kA à 100 kA | Foudre |

{{< question >}}
*En général, l'intensité du courant électrique varie dans le temps ; elle n'est alors pas égale à sa valeur moyenne.* À partir de l'expression de l'intensité moyenne du courant électrique, établir l'expression de l'intensité $i(t)$ du courant électrique à la date $t$.
{{< /question >}}

{{< solution "Réponse" >}}
En physique, lorsqu'on introduit une nouvelle grandeur, on réfléchit toujours dans un premier temps à partir d'une variation moyenne, *sur une durée finie* $\Delta t$. Par la suite, lorsqu'on souhaite établir l'expression de cette grandeur à une date $t$ donnée, on passe à la limite (c'est-à-dire qu'*on observe la variation de la grandeur sur un intervalle de temps $\mathrm{d} t$ infiniment petit mais non nul*).
$$i(t) = \lim_{\Delta t \to  0} \frac{q(t + \Delta t) - q(t)}{\Delta t} = \frac{\mathrm{d} q}{\mathrm{d} t} = q'(t)$$
L'intensité du courant électrique à la date $t$ est la **dérivée par rapport au temps** de la fonction $t \mapsto  q(t)$.
{{< /solution >}}

### Exercice 1

Un courant électrique *continu*, c'est-à-dire constant, d'intensité $I = \pu{0,50 A}$ circule dans un circuit électrique.
1. Quelle est (la valeur absolue de) la charge électrique qui traverse une section $S$ quelconque du circuit en une minute ?
1. Combien d'électrons traversent une section $S$ quelconque de ce circuit chaque minute ?

{{< solution "Réponse" >}}
1. Puisque le courant électrique est continu, sa valeur reste constante au cours du temps. On a alors $I = {\displaystyle \frac{\Delta q}{\Delta t}}$, soit $\Delta q = I \Delta t$.

   **A.N.** $\Delta q = \pu{0,50 A} \times \pu{60 s} = \pu{0,50 C/s} \times \pu{60 s} = \pu{30 C}$.
1. Chaque électron porte la charge électrique $-e$, donc $\Delta q = N |-e|$, où $N$ est le nombre d'électrons qui traversent la section $S$. On obtient donc $N = {\displaystyle \frac{\Delta q}{|-e|}}$.

   **A.N.** $N = {\displaystyle \frac{\pu{30 C}}{{1{,}6 \times 10^{-19}\ \pu{C}}}} = 1{,}9 \times 10^{20}$ électrons.
{{< /solution >}}

### Qu'est-ce qui donne naissance à un courant électrique ?

#### Rôle d'un générateur, potentiel électrique

{{< question >}}
Quel est le rôle d'un générateur au sein d'un circuit électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
Un générateur (pile, alternateur, etc.) a pour rôle d'entretenir une différence de potentiel électrique (exprimé en volt) entre ses bornes.

La borne notée $\oplus$ est le point du circuit où le potentiel électrique est maximal.

La borne notée $\ominus$ est le point du circuit où le potentiel électrique est minimal.
{{< /solution >}}

{{< question >}}
Sachant qu'une charge électrique $q$ située en un point où le potentiel électrique est $V$ possède *l'énergie potentielle électrique* $E_\text{Pel} = q V$, décrire le rôle d'un générateur d'un point de vue énergétique.
{{< /question >}}

{{< solution "Réponse" >}}
L'énergie potentielle électrique des charges est plus grande au niveau de la borne $\oplus$ qu'au niveau de la borne $\ominus$.

La diminution (en valeur absolue) de l'énergie potentielle des charges électriques est transférée aux éléments du circuit électrique (*en effet, l'énergie cinétique des porteurs de charge ne varie pas lors de leur déplacement*).

Un générateur fournit donc de l'énergie (d'origine chimique, mécanique, etc.) aux éléments du circuit électrique auquel il est connecté.
{{< /solution >}}

#### L'analogie hydraulique

On utilise souvent une [analogie hydraulique](https://en.wikipedia.org/wiki/Hydraulic_analogy) pour se représenter ce qu'est le potentiel électrique. On compare le circuit électrique à un circuit d'eau fermé, entièrement rempli d'eau, dans lequel une pompe fait circuler l'eau.

Des tubes verticaux ouverts, appelés *piézomètres*, sont branchés sur la canalisation du haut, tous au même niveau. L'eau monte dans chaque tube d'autant plus haut que sa **pression** est grande au point où le tube est branché. On lit donc la pression de l'eau en $A$, $C$, $D$ et $E$ directement sur la hauteur de l'eau dans les tubes.

On note $D_v$ le **débit volumique** de l'eau : c'est le volume d'eau qui traverse une section de la canalisation chaque seconde, en $\pu{m^3/s}$.

![](/terminales-pc/chap-5/5-1/fig-1.svg?width=80%)

> *Circuit d'eau fermé. La pompe fait circuler l'eau dans le sens des flèches.*

![](/terminales-pc/chap-5/5-1/fig-2.svg?width=85%)

> *Circuit électrique correspondant.*

{{< question >}}
Comparer le débit de l'eau dans la canalisation large et dans le tube étroit. Quelle grandeur électrique joue le rôle du débit volumique $D_v$ ?
{{< /question >}}

{{< note tip "Coup de pouce" >}}
L'eau ne peut ni s'accumuler ni disparaître dans le tube étroit : il est déjà plein.
{{< /note >}}

{{< solution "Réponse" >}}
L'eau est incompressible et le circuit est plein : chaque seconde, il sort du tube étroit autant d'eau qu'il en entre. Le débit est donc le même partout dans la boucle, même dans le tube étroit, où l'eau va simplement plus vite.

Le débit volumique (volume par seconde) joue le rôle de l'intensité du courant (charge par seconde). Le volume d'eau joue le rôle de la charge électrique.
{{< /solution >}}

{{< question >}}
Indiquer quel est le rôle de la pompe.
{{< /question >}}

{{< solution "Réponse" >}}
La pompe prend l'eau à basse pression, en $E$, et la renvoie à haute pression, en $A$. Elle entretient une différence de pression entre sa sortie et son entrée, et c'est cette différence de pression qui fait circuler l'eau dans tout le circuit. La pompe joue le rôle du générateur, qui entretient une différence de potentiel entre ses bornes.
{{< /solution >}}

{{< question >}}
D'après les piézomètres, à quel endroit du circuit la pression de l'eau diminue-t-elle ? En déduire la grandeur physique qui joue un rôle équivalent au potentiel électrique.
{{< /question >}}

{{< solution "Réponse" >}}
La hauteur d'eau est la même en $A$ et en $C$, puis la même en $D$ et en $E$ : la pression ne diminue pratiquement pas dans la canalisation large. Elle diminue nettement entre $C$ et $D$, c'est-à-dire dans le tube étroit.

La grandeur analogue au potentiel électrique est donc la **pression** $p$ de l'eau. La différence de pression $p_C - p_D$ est l'analogue de la tension $U_{C D} = V_C - V_D$. La canalisation large se comporte comme un fil (pas de chute de potentiel), le tube étroit comme une résistance (chute de potentiel à ses bornes).
{{< /solution >}}

On peut rendre l'analogie plus précise en regardant les unités. La pression est une énergie par unité de volume :
$$\pu{1 Pa} = \pu{1 N/m^2} = \pu{1 N m/m^3} = \pu{1 J/m^3}$$
Quand un mètre cube d'eau traverse le tube étroit, il cède à ce tube une énergie égale à $p_C - p_D$ (en joule), qui sert à vaincre les frottements et chauffe très légèrement l'eau.

Le potentiel électrique joue exactement le même rôle pour les charges électriques : c'est une énergie par unité de charge, en joule par coulomb. Quand un coulomb traverse une résistance, il lui cède une énergie égale à $U_{C D}$ (en joule), qui la chauffe : c'est l'effet Joule.

| **Circuit d'eau fermé** | **Circuit électrique** |
|:---|:---|
| volume d'eau $V$ ($\pu{m^3}$) | charge électrique $q$ (C) |
| débit volumique $D_v$ ($\pu{m^3/s}$) | intensité $I$ (A $=$ C/s) |
| pression $p$ (Pa $=$ $\pu{J/m^3}$) | potentiel électrique $V$ (V $=$ J/C) |
| différence de pression $p_C - p_D$ | tension $U_{C D} = V_C - V_D$ |
| pompe | générateur |
| canalisation large | fil de connexion |
| tube étroit | résistance |

> *Correspondances entre le circuit d'eau fermé et le circuit électrique.*

{{< note success "Énergie potentielle électrique et potentiel électrique" >}}
Une charge électrique $q$ placée en un point où le potentiel électrique vaut $V$ possède l'**énergie potentielle électrique** (énergie potentielle d'interaction électrique) :
$$E_\text{Pel} = q V$$
avec $E_\text{Pel}$ en joule (J), $q$ en coulomb (C) et $V$ en volt (V).

Le **potentiel électrique** en un point est donc l'énergie potentielle d'interaction électrique **par coulomb** de charge placée en ce point :
$$V = \frac{E_\text{Pel}}{q}$$
d'où 1 V $=$ 1 J/C.

Cette expression sera démontrée plus tard dans l'année, lors de l'étude du mouvement des charges électriques dans un champ électrique.
{{< /note >}}

{{< note info "Remarque" >}}
Lorsque les canalisations ne sont pas toutes à la même altitude, la grandeur analogue au potentiel n'est plus la pression seule, mais l'énergie par unité de volume $p + \rho g z$, qui tient aussi compte de l'énergie potentielle de pesanteur de l'eau ($z$ est l'altitude et $\rho$ la masse volumique de l'eau). Une chute d'eau perd de la pression motrice en descendant, comme une charge perd de l'énergie potentielle électrique en traversant un récepteur.
{{< /note >}}

{{< note info "Remarque" >}}
Fondamentalement, une analogie est possible si deux phénomènes *sont liés par des lois de conservation similaires* : ici, la conservation du volume d'eau et la conservation de la charge électrique. Il faut cependant se méfier : une analogie peut être utile pour expliquer ou décrire certains phénomènes d'un domaine (ici, ce que représente le potentiel électrique), mais cela ne signifie pas qu'elle décrit correctement tous les phénomènes de ce domaine.

Par exemple, il existe une grande différence entre le modèle hydraulique et le modèle électrique : *l'énergie cinétique des porteurs de charge électrique reste constante, alors que l'énergie cinétique de l'eau varie lors de son écoulement* (l'eau accélère dans le tube étroit).
{{< /note >}}

{{< question >}}
Un élève affirme : « Dans le tube étroit, l'eau perd de la pression, donc elle en sort avec un débit plus petit. Pareil pour le courant : il en sort moins de la résistance qu'il n'en entre. » Expliquer son erreur.
{{< /question >}}

{{< solution "Réponse" >}}
L'élève confond pression et débit, c'est-à-dire potentiel et intensité. Ce que l'eau perd dans le tube étroit, c'est de l'énergie par mètre cube (de la pression), pas du volume : le débit est le même à l'entrée et à la sortie. De même, une résistance ne « consomme » pas de charges : l'intensité est la même avant et après. Elle reçoit de l'énergie, qui se traduit par la chute de potentiel à ses bornes.
{{< /solution >}}

#### Tension électrique

{{< question >}}
Qu'appelle-t-on **tension électrique** entre deux points $A$ et $B$ d'un circuit électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
La tension électrique entre deux points $A$ et $B$ correspond à la **différence de potentiel électrique** entre ces points. On la note :
$$U_{A B} = V_A - V_B$$
et elle s'exprime en volt (V).
{{< /solution >}}

{{< question >}}
Comment et avec quel instrument mesure-t-on la tension électrique entre deux points d'un circuit ?
{{< /question >}}

{{< solution "Réponse" >}}
Pour mesurer la tension électrique entre deux points d'un circuit, on utilise un **voltmètre**.

L'appareil doit être **placé en dérivation**.
{{< /solution >}}

**Quelques ordres de grandeur**

| **Tension** | **Provenance** |
|:---|:---|
| 230 V | Réseau électrique domestique |
| plusieurs kV | Industrielle |
| 225 kV à 400 kV | Lignes haute tension |
| quelques V | Piles |

{{< note info "Remarque" >}}
Une tension électrique n'est pas en soi dangereuse pour la santé. **Le fait d'être à un certain potentiel n'est donc pas forcément dangereux.** *Toutefois, une différence de potentiel aux bornes d'un conducteur induit l'apparition d'un courant électrique, qui lui peut être dangereux.*
{{< /note >}}

{{< question >}}
Quelle relation lie les tensions électriques $U_{A B}$ et $U_{B A}$ ? Quelle propriété importante peut-on en déduire ?
{{< /question >}}

{{< solution "Réponse" >}}
$$U_{A B} = V_A - V_B = -(V_B - V_A) = -U_{B A}$$
La tension électrique est une **grandeur algébrique**.
{{< /solution >}}

{{< question >}}
Comment représente-t-on la tension $U_{A B}$ entre les points $A$ et $B$ ?
{{< /question >}}

{{< solution "Réponse" >}}
On utilise une représentation vectorielle : une flèche dirigée de $B$ vers $A$.

![](/terminales-pc/chap-5/5-1/Doc-3.svg?width=25%)
{{< /solution >}}

### Énergie et puissance

Un courant électrique transporte de l'énergie du générateur jusqu'aux différents composants du circuit.

On suppose qu'une charge électrique $\Delta q$ traverse l'élément de circuit représenté ci-dessous pendant $\Delta t$ secondes et subit une chute de potentiel.

![](/terminales-pc/chap-5/5-1/Doc-4.svg?width=40%)

{{< question >}}
Déterminer l'expression de la *variation d'énergie potentielle $\Delta E_\text{Pel}$ de la charge électrique* $\Delta q$.
{{< /question >}}

{{< solution "Réponse" >}}
La charge électrique passe du potentiel $V_A$ au potentiel $V_B$, sa variation d'énergie potentielle électrique est donc égale à :
$$\Delta E_\text{Pel} = \Delta q (V_B - V_A) = \Delta q \, U_{B A} = -\Delta q \, U_{A B}$$

{{< note info "Remarque" >}}
Le terme « variation » signifie « fin $-$ début ».
{{< /note >}}
{{< /solution >}}

{{< question >}}
Cette énergie potentielle est cédée à l'élément de circuit. Donner l'expression de la *variation d'énergie $\Delta E$ de l'élément de circuit* lorsque la charge $\Delta q$ le traverse.
{{< /question >}}

{{< solution "Réponse" >}}
L'énergie cédée par la charge électrique est captée par l'élément de circuit ; on a donc :
$$\Delta E = -\Delta E_\text{Pel} = \Delta q \, U_{A B}$$
{{< /solution >}}

{{< question >}}
En déduire l'expression de la puissance électrique $P$ reçue par l'élément de circuit.
{{< /question >}}

{{< solution "Réponse" >}}
La puissance est l'énergie échangée chaque seconde. Si cet échange est constant au cours du temps, on peut écrire :
$$P = \frac{\Delta E}{\Delta t} = \frac{\Delta q \, U_{A B}}{\Delta t} = \frac{\Delta q}{\Delta t} U_{A B}$$
Comme ${\displaystyle \frac{\Delta q}{\Delta t}} = I_{A B}$,
$$P = I_{A B} U_{A B}$$
{{< /solution >}}

{{< note success "Puissance électrique reçue" >}}
- La puissance électrique reçue par un élément de circuit a pour expression :
  $$P = I_{A B} U_{A B}$$
- On appelle **convention récepteur** la configuration où les *flèches courant et tension sont de sens opposés*. \
  En convention récepteur, *si $P > 0$, l'énergie est effectivement reçue par l'élément de circuit*.
{{< /note >}}

{{< question >}}
Dans l'analogie hydraulique, on propose d'écrire la puissance reçue par le tube étroit sous la forme $P = (p_C - p_D) \times D_v$. Vérifier, à l'aide des unités, que ce produit est bien une puissance.
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Écrire le pascal à l'aide du newton et du mètre, puis se souvenir qu'un joule est un newton fois un mètre.
{{< /note >}}

{{< solution "Réponse" >}}
$\pu{Pa} \times \pu{m^3/s} = \pu{N/m^2} \times \pu{m^3/s} = \pu{N m/s} = \pu{J/s} = \pu{W}$.

Le produit « différence de pression $\times$ débit volumique » est bien une puissance, comme le produit « tension $\times$ intensité ».
{{< /solution >}}

### Éléments d'un circuit

#### Vocabulaire

{{< question >}}
Qu'est-ce qu'un **dipôle électrique** ?
{{< /question >}}

{{< solution "Réponse" >}}
Un dipôle électrique est un *composant électrique possédant deux pôles*.

Les ampoules, les interrupteurs, les générateurs, les piles, les condensateurs, les inductances, les diodes, les DEL, les résistances et les moteurs sont des dipôles.
{{< /solution >}}

{{< question >}}
Qu'est-ce qu'un **nœud** ?
{{< /question >}}

{{< solution "Réponse" >}}
Un **nœud** est un *point du circuit auquel sont connectés au moins trois fils*.

![](/terminales-pc/chap-5/5-1/Doc-5.svg?width=25%)
{{< /solution >}}

{{< question >}}
Qu'est-ce qu'une **branche** ?
{{< /question >}}

{{< solution "Réponse" >}}
Une **branche** est une *portion de circuit située entre deux nœuds, parcourue par le même courant électrique*.

![](/terminales-pc/chap-5/5-1/Doc-6.svg?width=60%)
{{< /solution >}}

{{< question >}}
Qu'est-ce qu'une **maille** ?
{{< /question >}}

{{< solution "Réponse" >}}
Une **maille** est une *portion fermée de circuit* (ensemble de branches qui partent d'un nœud et reviennent à ce même nœud).

![](/terminales-pc/chap-5/5-1/Doc-7.svg?width=45%)
{{< /solution >}}

#### Exercice 2

Pour le circuit suivant :

![](/terminales-pc/chap-5/5-1/Doc-8.svg?width=40%)

1. Compter le nombre de dipôles.
1. Compter le nombre de nœuds.
1. Compter le nombre de branches.
1. Combien de mailles peut-on former ?

{{< solution "Réponse" >}}
1. 4 dipôles.
1. 2 nœuds.
1. 3 branches.
1. On peut former 3 mailles.
{{< /solution >}}

### Association d'éléments de circuits

{{< question >}}
Qu'appelle-t-on **association série** de deux dipôles ?
{{< /question >}}

{{< solution "Réponse" >}}
Deux dipôles *traversés par le même courant électrique* sont **en série**.

![](/terminales-pc/chap-5/5-1/Doc-9.svg?width=60%)
{{< /solution >}}

{{< question >}}
Qu'appelle-t-on **association parallèle** (ou **en dérivation**) de deux dipôles ?
{{< /question >}}

{{< solution "Réponse" >}}
Deux dipôles *reliés aux deux mêmes nœuds* sont dits placés en **parallèle** (ou **en dérivation**).

![](/terminales-pc/chap-5/5-1/Doc-10.svg?width=45%)

*Les tensions électriques aux bornes de ces deux dipôles sont identiques.*
{{< /solution >}}

### Loi d'Ohm, résistance

{{< question >}}
Rappeler ce qu'est la **caractéristique d'un dipôle**.
{{< /question >}}

{{< solution "Réponse" >}}
On appelle **caractéristique d'un dipôle** la relation $i = f(u)$ *entre l'intensité du courant électrique qui le traverse et la tension électrique à ses bornes*.

La plupart du temps, la caractéristique ne peut être donnée que sous la forme d'une courbe.
{{< /solution >}}

{{< question >}}
Quelle est la caractéristique d'une résistance électrique ?
{{< /question >}}

{{< solution "Réponse" >}}
La caractéristique d'une résistance est :

![](/terminales-pc/chap-5/5-1/Doc-11.svg?width=40%)
{{< /solution >}}

{{< question >}}
Déduire de la forme de la caractéristique d'une résistance la loi d'Ohm, qui donne la relation entre l'intensité du courant électrique qui traverse une résistance et la tension à ses bornes.
{{< /question >}}

{{< solution "Réponse" >}}
La loi d'Ohm est la traduction mathématique de la caractéristique d'une résistance électrique :
$$U_{A B} = R I_{A B}$$
La chute de potentiel aux bornes d'une résistance est proportionnelle à l'intensité du courant électrique qui la traverse.

Cette loi est empirique et n'est valable que pour des intensités raisonnables.

La loi d'Ohm reste valable lorsque le courant est variable dans le temps.
{{< /solution >}}

{{< note info "Remarque" >}}
*On considère que la résistance d'un fil électrique est nulle.*
{{< /note >}}

{{< question >}}
Puisqu'on considère que la **résistance d'un fil électrique est nulle**, donner la valeur de la tension électrique entre deux points d'un même câble.
{{< /question >}}

{{< solution "Réponse" >}}
Puisque $R = \pu{0 \Omega}$, $U = R I = \pu{0 V}$.

*Il n'existe aucune chute de potentiel électrique le long d'un fil électrique.*
{{< /solution >}}

Le tube étroit de l'analogie hydraulique obéit lui aussi à une loi de proportionnalité. Pour un écoulement lent, la différence de pression entre ses extrémités est proportionnelle au débit : $p_C - p_D = R_h D_v$. C'est la loi de Poiseuille, analogue de la loi d'Ohm. La « résistance hydraulique » $R_h$ augmente quand le tube est plus long ou plus étroit.

{{< question >}}
Dans le circuit d'eau, on remplace le tube étroit par un tube encore plus étroit. La pompe maintient la même différence de pression entre $C$ et $D$. Prédire l'effet sur le débit, puis traduire cette prédiction pour le circuit électrique.
{{< /question >}}

{{< solution "Réponse" >}}
Le tube plus étroit freine davantage l'eau : $R_h$ augmente. Avec la même différence de pression, $D_v = {\displaystyle \frac{p_C - p_D}{R_h}}$ diminue.

En électricité : si l'on remplace la résistance par une résistance plus grande, sous la même tension, l'intensité $I = {\displaystyle \frac{U_{C D}}{R}}$ diminue.
{{< /solution >}}

{{< question >}}
Donner l'expression de la puissance électrique qu'un courant électrique cède à une résistance $R$. Cet effet s'appelle l'**effet Joule**.
{{< /question >}}

{{< solution "Réponse" >}}
$P = U_{A B} I_{A B}$ avec $U_{A B} = R I_{A B}$, donc
$$P = R I_{A B}^2 = \frac{U_{A B}^2}{R}$$
{{< /solution >}}

{{< note success "Effet Joule" >}}
La **puissance Joule** cédée par un courant électrique à une résistance a pour expression :
$$P = R I_{A B}^2 = \frac{U_{A B}^2}{R}$$
{{< /note >}}

### Lois de Kirchhoff

En classe de terminale, les courants seront soit **continus** (*constants dans le temps*), soit lentement variables. Il ne sera donc pas nécessaire de prendre en compte les temps de propagation des ondes, qui seront considérés comme nuls.

{{< note success "Intensité dans une branche" >}}
L'intensité du courant électrique est identique en tout point d'une même branche.
{{< /note >}}

#### Loi des nœuds

{{< question >}}
**La charge électrique est une grandeur qui se conserve.** Il ne peut donc pas y avoir accumulation de charges au niveau d'un nœud. Donner la relation entre les différents courants pour le nœud considéré et en déduire la loi des nœuds.

![](/terminales-pc/chap-5/5-1/Doc-12.svg?width=30%)
{{< /question >}}

{{< solution "Réponse" >}}
$$i_1 + i_4 + i_6 = i_2 + i_3 + i_5$$
*La somme des intensités de tous les courants électriques qui arrivent à un nœud est égale à la somme des intensités de tous les courants qui le quittent.*
{{< /solution >}}

{{< note info "Remarque" >}}
Dans l'analogie hydraulique, un nœud est un raccord en T entre plusieurs canalisations. L'eau ne pouvant pas s'y accumuler, le débit qui arrive au raccord est égal au débit qui en repart.
{{< /note >}}

#### Loi des mailles

{{< question >}}
Soit la maille ci-après. Calculer la somme $U_{12} + U_{41} + U_{34} + U_{23}$ (les $V_i$ sont les potentiels électriques aux différents nœuds) et en déduire la loi des mailles.

![](/terminales-pc/chap-5/5-1/Doc-13.svg?width=45%)
{{< /question >}}

{{< solution "Réponse" >}}
$$U_{12} + U_{41} + U_{34} + U_{23} = V_1 - V_2 + V_4 - V_1 + V_3 - V_4 + V_2 - V_3 = 0$$
La somme algébrique des variations de potentiel électrique le long d'une maille est nulle.

*La somme algébrique des tensions électriques le long d'une maille est nulle.*
{{< /solution >}}

{{< note info "Remarque" >}}
Dans l'analogie hydraulique, si l'on fait le tour d'une boucle de canalisations en partant d'un point, on revient au même point, donc à la même pression : la somme des différences de pression rencontrées le long de la boucle est nulle.
{{< /note >}}

#### Exercice 3

On pose $E = \pu{12 V}$, $R_1 = \pu{200 \Omega}$ et $R_2 = \pu{400 \Omega}$.

{{< columns >}}
1. Que vaut la tension $U_{A C}$ ?
1. Montrer que l'on peut remplacer les deux résistances $R_1$ et $R_2$ placées en série par une résistance unique de valeur $R_\text{eq} = R_1 + R_2$.
1. À partir de la réponse à la question précédente, calculer la valeur de l'intensité $I_{A C}$ du courant électrique qui circule dans la branche $A C$.
1. En déduire la valeur de la tension $U_{A B}$.
1. Même question pour la tension $U_{B C}$.
1. Calculer la puissance reçue par la résistance $R_1$.
1. Calculer la puissance reçue par la résistance $R_2$.
1. Vérifier que la somme des puissances reçues par $R_1$ et $R_2$ est égale à la puissance fournie par le générateur.
{{< column >}}
![](/terminales-pc/chap-5/5-1/Doc-14.svg?width=30%)
{{< endcolumns >}}

{{< solution "Réponse" >}}
1. Les fils ayant une résistance nulle, $U_{A C}$ est la tension aux bornes du générateur : $U_{A C} = E = \pu{12 V}$.
1. Les deux résistances sont traversées par le même courant $I_{A C}$. D'après la loi des mailles et la loi d'Ohm :
   $$U_{A C} = U_{A B} + U_{B C} = R_1 I_{A C} + R_2 I_{A C} = (R_1 + R_2) I_{A C}$$
   L'ensemble se comporte donc comme une résistance unique $R_\text{eq} = R_1 + R_2$.
1. $I_{A C} = {\displaystyle \frac{U_{A C}}{R_\text{eq}}} = {\displaystyle \frac{E}{R_1 + R_2}}$.

   **A.N.** $I_{A C} = {\displaystyle \frac{\pu{12 V}}{\pu{200 \Omega} + \pu{400 \Omega}}} = \pu{0,020 A} = \pu{20 mA}$.
1. **A.N.** $U_{A B} = R_1 I_{A C} = \pu{200 \Omega} \times \pu{0,020 A} = \pu{4,0 V}$.
1. **A.N.** $U_{B C} = R_2 I_{A C} = \pu{400 \Omega} \times \pu{0,020 A} = \pu{8,0 V}$. On vérifie que $U_{A B} + U_{B C} = \pu{12 V} = E$.
1. **A.N.** $P_1 = R_1 I_{A C}^2 = \pu{200 \Omega} \times (\pu{0,020 A})^2 = \pu{0,080 W}$.
1. **A.N.** $P_2 = R_2 I_{A C}^2 = \pu{400 \Omega} \times (\pu{0,020 A})^2 = \pu{0,16 W}$.
1. Le générateur fournit $P_G = E I_{A C}$.

   **A.N.** $P_G = \pu{12 V} \times \pu{0,020 A} = \pu{0,24 W}$, et $P_1 + P_2 = \pu{0,080 W} + \pu{0,16 W} = \pu{0,24 W}$. Toute la puissance fournie par le générateur est reçue par les deux résistances.
{{< /solution >}}

#### Exercice 4

On pose $E = \pu{12 V}$, $R_1 = \pu{200 \Omega}$, $R_2 = \pu{400 \Omega}$ et $R_3 = \pu{200 \Omega}$.

{{< columns >}}
1. Que vaut la tension $U_{A C}$ ?
1. Montrer que l'on peut remplacer les deux résistances $R_2$ et $R_3$ placées en parallèle par une résistance unique telle que
   $$\frac{1}{R_\text{eq}} = \frac{1}{R_2} + \frac{1}{R_3}$$
   Calculer la valeur de cette résistance équivalente.
1. À partir de la réponse à la question précédente, calculer la valeur de l'intensité $I_{A C}$ du courant électrique qui circule dans la branche $A C$.
1. En déduire la valeur de la tension $U_{A B}$.
1. Même question pour la tension $U_{B C}$.
{{< column >}}
![](/terminales-pc/chap-5/5-1/Doc-15.svg?width=35%)
{{< endcolumns >}}

{{< solution "Réponse" >}}
1. Comme dans l'exercice précédent, $U_{A C} = E = \pu{12 V}$.
1. $R_2$ et $R_3$ sont soumises à la même tension $U_{B C}$. D'après la loi des nœuds et la loi d'Ohm, l'intensité $I$ du courant qui arrive en $B$ vaut :
   $$I = I_2 + I_3 = \frac{U_{B C}}{R_2} + \frac{U_{B C}}{R_3} = (\frac{1}{R_2} + \frac{1}{R_3}) U_{B C}$$
   L'ensemble se comporte donc comme une résistance unique $R_\text{eq}$ telle que ${\displaystyle \frac{1}{R_\text{eq}} = \frac{1}{R_2} + \frac{1}{R_3}}$, soit $R_\text{eq} = {\displaystyle \frac{R_2 R_3}{R_2 + R_3}}$.

   **A.N.** $R_\text{eq} = {\displaystyle \frac{\pu{400 \Omega} \times \pu{200 \Omega}}{\pu{400 \Omega} + \pu{200 \Omega}}} = {1{,}3 \times 10^{2}\ \pu{\Omega}}$ (plus précisément $400/3 \approx \pu{133 \Omega}$).
1. Le circuit équivaut à $R_1$ en série avec $R_\text{eq}$ : $I_{A C} = {\displaystyle \frac{E}{R_1 + R_\text{eq}}}$.

   **A.N.** $I_{A C} = {\displaystyle \frac{\pu{12 V}}{\pu{200 \Omega} + \pu{133 \Omega}}} = \pu{0,036 A} = \pu{36 mA}$.
1. **A.N.** $U_{A B} = R_1 I_{A C} = \pu{200 \Omega} \times \pu{0,036 A} = \pu{7,2 V}$.
1. **A.N.** $U_{B C} = R_\text{eq} I_{A C} = \pu{133 \Omega} \times \pu{0,036 A} = \pu{4,8 V}$. On vérifie que $U_{A B} + U_{B C} = \pu{12 V} = E$.
{{< /solution >}}

{{< note success "À l'issue de cette activité, je sais…" >}}
- Je sais définir le courant électrique et indiquer les porteurs de charge mobiles dans un métal, une solution électrolytique et un plasma.
- Je sais donner le sens conventionnel du courant électrique.
- Je sais définir l'intensité du courant comme un débit de charge, écrire $I_\text{moy} = \frac{\Delta q}{\Delta t}$ et, en régime variable, $i(t) = \frac{\mathrm{d} q}{\mathrm{d} t}$.
- Je sais calculer une charge électrique et un nombre d'électrons à partir d'une intensité et d'une durée.
- Je sais expliquer le rôle d'un générateur à l'aide du potentiel électrique et de l'énergie potentielle électrique.
- Je sais définir la tension comme une différence de potentiel, $U_{A B} = V_A - V_B$, la représenter par une flèche et utiliser $U_{B A} = -U_{A B}$.
- Je sais brancher un ampèremètre en série et un voltmètre en dérivation.
- Je sais établir et utiliser l'expression de la puissance reçue par un dipôle, $P = U_{A B} I_{A B}$, en convention récepteur.
- Je sais reconnaître dans un circuit les dipôles, les nœuds, les branches et les mailles, ainsi que des dipôles en série ou en dérivation.
- Je sais utiliser la loi d'Ohm $U_{A B} = R I_{A B}$ et calculer la puissance reçue par effet Joule, $P = R I^2 = U^2 / R$.
- Je sais écrire la loi des nœuds et la loi des mailles et les relier à la conservation de la charge et à la définition de la tension.
- Je sais calculer la résistance équivalente à deux résistances en série ou en parallèle, puis les intensités et les tensions dans un circuit simple.
{{< /note >}}
