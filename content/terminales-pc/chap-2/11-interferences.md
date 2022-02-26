---
title: "Conditions d’interférence de deux ondes sinusoïdales"
subtitle: "Chapitre 3,3,3"
author: ""
type: ""
date: 2020-09-21T21:13:09+04:00
draft: false
toc: true
tags: ["Différence de marche", "Superposition", "Période temporelle", "Longueur d'onde", "Retard", "Déphasage", "Ondes","Interférences"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---
[^1]: Comprendre : *les rayonnements ne sont pas identiques, même si émis par le même atome*.
[^2]: Comprendre : *les rayonnements ne sont pas identiques, même si émis par le même élément chimique*.
[^4]: Phénomène d'**émission spontanée** d'une durée environ égale à $\pu{1e-8 s}$.
## Interférences

{{% note tip %}}
On appelle **interférence** le *résultat de la superposition de plusieurs ondes (mécaniques ou électromagnétiques) en un même point de l'espace*.
    
En physique, on distingue normalement deux phénomènes particuliers qui se produisent lorsqu'on additionne des ondes sinusoïdales :
- L'**interférence**, *quand les ondes ont la **même fréquence**.*
- Le **battement**, *quand les fréquences des ondes sont légèrement différentes*.
{{% /note %}}

Par la suite, toutes les ondes étudiées seront **sinusoïdales**, **de même fréquence** $f$.

## Un exemple de montage d’étude d’une figure d’interférence

### Schéma de principe

<img src="/terminales-pc/chap-2/chap-2-11-1.png" alt="" width="50%" />

Deux ondes sinusoïdales de même fréquence $f$ sont émises par les deux émetteurs $E_1$ et $E_2$. L'émission de ces ondes s'effectuant dans un cône, *ces ondes ne se superposent que dans la zone hachurée* sur le schéma : c'est le **champ d'interférence**. *Dans toute cette région, ces ondes interférent*. 

### Cas de la lumière

Les ondes lumineuses présentent quelques particularités (par rapport aux ondes sonores, par exemple) :

- L'ordre de grandeur de leur période est : $T \approx \pu{1e-15 s}$ ;
- *Les atomes émettent de la lumière lors de la phase de désexcitation*[^4]. Ils doivent à nouveau être excités avant de pouvoir reprendre une nouvelle émission. *Ces différentes émissions se font à la même fréquence $f$ mais avec des phases différentes*[^1].
- Deux atomes différents du même élément chimique émettent des ondes sinusoïdales de même fréquence $f$ mais les phases de ces rayonnements sont toujours différentes[^2].

Les récepteurs n'étant pas capables « de suivre » les vibrations de la lumière ($f \approx \pu{1e15 Hz}$), ils réalisent une « moyenne ». *Ce processus d'intégration nivelle les variations d'intensité lumineuse dans la plupart des situations et le phénomène d'interférences lumineuse n'est généralement pas visible*. 

{{% note tip %}}
*Le phénomène d'interférences n'est visible avec de la lumière qu'à la condition que les deux ondes qui interfèrent soient **issues de la même source** !*  
... et que la différence de chemin optique est inférieure à la **longueur de cohérence** (notion pas au programme).
{{% /note %}}

<img src="/terminales-pc/chap-2/chap-2-11-2.jpg" alt="" width="50%" />
> Le montage expérimental doit donc être légèrement modifié lorsqu'on réalise des interférences lumineuses : les sources secondaires sont issues du même faisceau lumineux.

## Interférence constructive, interférence destructive

**Remarque :** *En régime sinusoïdal, le retard d’une onde par rapport à une autre se traduit par un **déphasage**.*

<iframe scrolling="no" title="Interférences" src="https://www.geogebra.org/material/iframe/id/edcc43v2/width/1271/height/646/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="650px" height="350px" style="border:0px;"> </iframe>

### Ondes en phase

<img src="/terminales-pc/chap-2/chap-2-11-3.png" alt="" width="35%" style="float: right; " />

On considère une situation dans laquelle les ondes sont en phase,
- $\tau =0$ ou $\tau = T$, ou $\tau = 2T$, ... ce que l'on peut généraliser en écrivant :
$$ \tau = p T $$ 
avec $p$ entier.

- Comme $T = \dfrac{\lambda}{v}$ et $\tau = \dfrac{\delta}{v}$, 
$$ \tau = p T \Leftrightarrow \delta = p \lambda $$
avec $p$ entier.

{{% note tip %}}
#### Interférence constructive

- La différence de marche $\delta$ de deux ondes **en phase** est un multiple entier de la longueur d'onde $\lambda$ :
$$ \tau = p T \Leftrightarrow \delta = p \lambda $$
- *L'amplitude de l'addition des deux ondes en phase est égale à la somme des amplitudes de ces ondes* : l'interférence est dite **constructive**.
{{% /note %}}

#### Rappel

Les **élongations** des deux ondes qui interférent s'ajoutent toujours. *C'est seulement dans le cas d'**ondes en phase** que cela se traduit par l'addition des amplitudes !*

### Ondes en opposition de phase

<img src="/terminales-pc/chap-2/chap-2-11-4.png" alt="" width="40%" style="float: right;" />

On considère une situation dans laquelle les ondes sont en opposition de phase,
- $\tau =\dfrac{T}{2}$ ou $\tau = \dfrac{T}{2} + T$, ou $\tau = \dfrac{T}{2} + 2T$, ... ce que l'on peut généraliser en écrivant : 
$$ \tau = (2p + 1) \dfrac{T}{2}$$ 
avec $p$ entier.

- Comme $T = \dfrac{\lambda}{v}$ et $\tau = \dfrac{\delta}{v}$, 
$$ \tau = (2p + 1) \dfrac{T}{2} \Leftrightarrow \delta = (2p + 1) \dfrac{\lambda}{2} $$
avec $p$ entier.

{{% note tip %}}
#### Interférence destructive

- La différence de marche $\delta$ de deux ondes **en opposition de phase** est un multiple entier impair de la demi longueur d'onde $\lambda$ :
$$ \tau = (2p + 1) \dfrac{T}{2} \Leftrightarrow \delta = (2p + 1) \dfrac{\lambda}{2} $$

- *L'amplitude de l'addition des deux ondes en opposition de phase est égale à la différence des amplitudes de ces ondes* : l'interférence est dite **destructive**.
{{% /note %}}

#### Rappel

Les **élongations** des deux ondes qui interférent s'ajoutent toujours. *C'est seulement dans le cas d'ondes en **opposition de phase** que cela se traduit par la soustraction des amplitudes !*

### Ondes présentant un déphasage quelconque

<img src="/terminales-pc/chap-2/chap-2-11-5.png" alt="" width="40%" style="float: right;" />

On considère une situation dans laquelle les ondes présentent un déphasage quelconque,
- $\tau \neq (2p + 1) \dfrac{T}{2}$ et $\tau \neq n T$ avec $p$ et $n$ entiers.

- Comme $T = \dfrac{\lambda}{v}$ et $\tau = \dfrac{\delta}{v}$, 
$$ \delta \neq (2p + 1) \dfrac{\lambda}{2} \text{ et } \delta \neq n \lambda$$
avec $p$ et $n$ entiers. *On ne peut rien dire de plus sans l'expression des élongations*.

{{% note tip %}}
#### Interférence quelconque

- La différence de marche $\delta$ entre deux ondes ni en phase ni en opposition de phase est quelconque.
- Il est alors impossible de prédire sans calcul (ce qui est hors programme) l'amplitude du résultat de l'addition des deux ondes.
{{% /note %}}

## Fentes, trous d'Young

La configuration des fentes (ou trous) d'Young est à connaître.

<img src="/terminales-pc/chap-2/chap-2-11-6.png" alt="" width="50%" style="float: left;" />

- Une onde lumineuse sinusoïdale de fréquence $f$ éclaire deux fentes (ou deux trous) séparés d'une distance $a$.
- Ces deux fentes agissent comme des sources secondaires synchrones vibrant à la même fréquence $f$.
- Les ondes émises peuvent interférer (dans le champ d'interférences). On observe le résultat de ces interférences sur un écran disposé à une distance $D \gg a$.

### Différence de marche

- L'expression de la différence de marche n'est pas à apprendre par cœur. Sa démonstration ne figure pas au programme.  
Par contre, il est nécessaire de savoir utiliser cette expression.

{{% solution "Démonstration pour les plus curieux" %}}

{{% /solution %}}

{{% note normal %}}
Dans le cas des fentes (ou trous) d'Young, la différence de marche entre l'onde émise par $S_2$ et l'onde émise par $S_1$ a pour expression :
$$ \delta = \dfrac{ax}{D} $$
{{% /note %}}

### Résultat à l'écran

<img src="/terminales-pc/chap-2/chap-2-11-10.png" alt="" width="80%" />

### Interfrange

{{% note tip %}}
On appelle **interfrange** $i$ la *période spatiale de la figure obtenue à l’écran dans le champ d’interférence*.

Si $D \gg a$,
$$ i = \dfrac{\lambda D}{a} $$
{{% /note %}}


### Influence de la longueur d'onde sur les figures d'interférence 

<img src="/terminales-pc/chap-2/chap-2-11-9.png" alt="" width="80%" />
Les lieux où les ondes interférent constructivement (respectivement destructivement) ne sont pas identiques lorsqu’on change de longueur d’onde.  
**Chaque longueur d’onde conduit à une figure d’interférence spécifique.**
 

### Interférence en lumière blanche

<img src="/terminales-pc/chap-2/chap-2-11-8-1.png" alt="" width="80%" />
<img src="/terminales-pc/chap-2/chap-2-11-8-2.png" alt="" width="80%" />
<img src="/terminales-pc/chap-2/chap-2-11-8-3.png" alt="" width="80%" />
<img src="/terminales-pc/chap-2/chap-2-11-8-4.png" alt="" width="80%" />

{{% note tip %}}
- *Les figures d'interférence de chacune des longueurs d'onde se superposent sur l'écran*.
- La frange centrale, correspondant à une différence de marche nulle, est « brillante » pour chacune des longueurs d'onde. *Elle apparaît donc blanche à l'écran*.
- Les autres franges « brillantes » n'étant  pas disposées au même endroit dans l'espace pour toutes les longueurs d'ondes, *leur superposition conduit à un phénomène d'irisation*.
{{% /note %}}