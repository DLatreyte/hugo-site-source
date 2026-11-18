---
title: "Le dipôle (R, C)"
subtitle: "Doc. 5,2"
date: 2020-10-30T20:15:29+04:00
draft: false
toc: true
tags: ["condensateur", "armatures", "diélectrique", "capacité", "farad", "dipôle RC", "échelon de tension", "charge", "décharge", "régime transitoire", "régime permanent", "constante de temps", "équation différentielle"]
categories: ["Physique", "Terminale Spé PC"]
solution_est_visible: true
auto_numbering: true
weight: 200
---
- {{< remote "Énoncé au format pdf" "/terminales-pc/chap-5/5-2/5-2-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/terminales-pc/chap-5/5-2/5-2-corrige.pdf" >}}

{{< note goal "Objectif" >}}
Comprendre comment un condensateur se charge puis se décharge à travers une résistance : établir et résoudre l'équation différentielle vérifiée par la tension à ses bornes, puis interpréter la constante de temps $\tau = R C$.
{{< /note >}}

{{< columns >}}
Les premiers condensateurs sont apparus vers 1745. Il s'agissait en fait d'une bouteille de Leyde : une fiole à moitié remplie d'eau dont l'ouverture était obturée par un bouchon de liège percé d'une tige métallique trempant dans l'eau. La première application de ce condensateur était de donner des commotions (chocs électriques ou électrisations) au public dans les foires. Par exemple, à Versailles, on présenta au roi Louis XV l'expérience de la décharge d'une grosse bouteille de Leyde à travers le circuit formé de plus de deux cents courtisans.

*L'étude du condensateur va bien au-delà de la compréhension du fonctionnement de ce composant. De nombreux dispositifs, capteurs ou phénomènes (les orages par exemple) présentent un comportement capacitif.*
{{< column >}}
![](/terminales-pc/chap-5/5-2/Doc-1.svg?width=40%)
{{< endcolumns >}}

## Les condensateurs

### Description

{{< note success "Condensateur" >}}
Un **condensateur** est un composant électrique formé de *deux armatures métalliques conductrices en regard (plaques ou films métalliques), séparées par un isolant (air, papier, céramique, etc.)* appelé **diélectrique**.
{{< /note >}}

![](/terminales-pc/chap-5/5-2/Doc-2.svg?width=30%)

> *Figure 1 : Symbole d'un condensateur.*

### Comment se comporte un condensateur dans un circuit électrique ?

{{< columns >}}
On réalise un circuit électrique comportant, en série, un condensateur, une ampoule, un générateur de tension continue et un interrupteur.

Lorsqu'on ferme l'interrupteur $K$, la lampe s'éclaire, puis s'éteint progressivement (la durée au bout de laquelle elle s'éteint dépend du condensateur utilisé).
{{< column >}}
![](/terminales-pc/chap-5/5-2/Doc-3.svg?width=35%)
{{< endcolumns >}}

{{< question >}}
Que peut-on déduire des résultats de l'expérience ?
{{< /question >}}

{{< solution "Réponse" >}}
Puisque la lampe s'allume, un courant électrique circule dans le circuit. La lampe finit par s'éteindre : le courant électrique finit donc par disparaître.
{{< /solution >}}

{{< question >}}
Comment expliquer l'apparition d'un courant transitoire, puis l'absence de courant lors du régime permanent ?
{{< /question >}}

{{< solution "Réponse" >}}
{{< columns >}}
Lorsqu'on ferme l'interrupteur, sous l'action du générateur, un courant électrique apparaît dans le circuit : des électrons arrivent au niveau de l'armature $B$ et des électrons quittent l'armature $A$. Comme le diélectrique est isolant, les électrons ne peuvent pas le traverser : ils s'accumulent en $B$, et l'armature $B$ se charge négativement. Dans le même temps, l'armature $A$ se charge positivement, car aucun électron ne vient combler le déficit laissé par ceux qui sont partis.

L'intensité du courant électrique est identique en tout point du circuit : le débit avec lequel les électrons arrivent en $B$ est égal au débit avec lequel les électrons quittent $A$. On a donc $q_A (t) = -q_B (t)$.
{{< column >}}
![](/terminales-pc/chap-5/5-2/Doc-4.svg?width=30%)
{{< endcolumns >}}

Les charges électriques opposées portées par les armatures du condensateur donnent naissance à la tension électrique $u_{A B}$. Le courant électrique finit par disparaître dans le circuit : la tension aux bornes de la lampe s'annule donc. Une application de la loi des mailles nous apprend que, dans le régime permanent, $u_{A B} = E$.

Dans le régime permanent, le générateur entretient donc un déséquilibre électrostatique qui maintient la charge du condensateur, c'est-à-dire le stockage de l'énergie électrique.
{{< /solution >}}

{{< note success "Charges des armatures" >}}
- À tout moment, les charges électriques présentes sur les armatures d'un condensateur sont liées par la relation :
  $$q_A (t) = -q_B (t)$$
  **Rappel :** la charge électrique s'exprime en coulomb (C).
- Un condensateur qui stocke des charges électriques sur ses armatures est dit *chargé* ; ce stockage correspond à un stockage d'énergie électrique.
{{< /note >}}

### Charge électrique et intensité du courant électrique

{{< question >}}
Quelle est la relation entre l'intensité du courant et les charges portées par les armatures ?
![](/terminales-pc/chap-5/5-2/Doc-5.svg?width=25%)
{{< /question >}}

{{< solution "Réponse" >}}
L'intensité du courant électrique est la charge électrique qui traverse une section quelconque du circuit chaque seconde, donc $i(t) = {\displaystyle \frac{\mathrm{d} q(t)}{\mathrm{d} t}}$.

On choisit un sens de circulation pour $i(t)$ et on en déduit la relation $i(t) = {\displaystyle \frac{\mathrm{d} q_A (t)}{\mathrm{d} t}}$ (les charges positives s'accumulent sur l'armature $A$), et $i(t) = - {\displaystyle \frac{\mathrm{d} q_B (t)}{\mathrm{d} t}}$ puisque $q_B (t) = -q_A (t)$.
{{< /solution >}}

{{< note success "Intensité et charge d'une armature" >}}
Lorsqu'on souhaite exprimer la relation qui existe entre l'intensité du courant électrique et la charge portée par une armature :
1. on **choisit** un sens de circulation pour le courant électrique ;
1. on écrit la relation entre l'intensité du courant électrique et la charge de l'armature.

Sur l'exemple choisi :
$$i(t) = \frac{\mathrm{d} q_A (t)}{\mathrm{d} t} = - \frac{\mathrm{d} q_B (t)}{\mathrm{d} t}$$
{{< /note >}}

{{< note info "Remarque" >}}
Si, après calcul, $i > 0$, alors *le courant électrique circule effectivement dans le sens choisi* (on a deviné correctement) et *la fonction $q_A$ est croissante* : *les charges positives s'accumulent sur l'armature $A$.*

Si, après calcul, $i < 0$, *le courant électrique circule dans le sens opposé au sens choisi* et *la fonction $q_A$ est décroissante* : *les charges positives quittent l'armature $A$.*
{{< /note >}}

### Capacité d'un condensateur

Le mouvement des charges électriques est dû à la différence de potentiel électrique $u_{A B}$ ; on pose donc que :

{{< note success "Capacité d'un condensateur" >}}
À chaque instant, la charge $q_A$ de l'armature $A$ du condensateur est proportionnelle à la tension $u_{A B}$ entre ses armatures $A$ et $B$ :
$$q_A = C \cdot u_{A B}$$
$C$ est appelée **capacité** du condensateur. Si $q_A$ est en coulomb (C) et $u_{A B}$ en volt (V), $C$ s'exprime en farad (F).

La capacité $C$ est donc *la charge stockée lorsque la tension entre les deux armatures est égale à 1 V*.
{{< /note >}}

{{< note info "Remarque" >}}
$C > 0$, donc $q_A$ et $u_{A B}$ sont de même signe.
{{< /note >}}

{{< note info "Remarque" >}}
La capacité $C$ d'un condensateur dépend de sa construction.
{{< /note >}}

| **Utilisation** | **Capacité en farad (F)** |
|:---|:---|
| mémoire d'ordinateur | 0,1 à 1 |
| allumage de voiture | $10^{-4}$ |
| flash électronique | $10^{-5}$ |
| détection radio | $10^{-9}$ à $10^{-12}$ |

> *Quelques ordres de grandeur de capacités. **Le farad est une unité très grande.***

## Charge d'un dipôle (R, C) soumis à un échelon de tension

{{< note success "Échelon de tension" >}}
On appelle **échelon de tension** une tension qui varie brutalement de la valeur 0 V à une valeur $E$.
{{< /note >}}

{{< note info "Remarque" >}}
L'association en série d'un condensateur de capacité $C$ et d'un conducteur ohmique de résistance $R$ constitue un dipôle $(R, C)$.
{{< /note >}}

### Étude expérimentale

**Résultats expérimentaux**

{{< columns >}}
On réalise le montage ci-contre.

On bascule le commutateur en **position 2** à la date $t = \pu{0 s}$ et on enregistre l'évolution dans le temps des tensions $u_C$ et $u_R$.

On obtient les enregistrements représentés ci-dessous.
{{< column >}}
![](/terminales-pc/chap-5/5-2/Doc-6.svg?width=55%)
{{< endcolumns >}}

![](/terminales-pc/chap-5/5-2/Doc-7.svg?width=100%)

> *Figure 2 : Résultats expérimentaux lors de la charge d'un dipôle $(R, C)$.*

<iframe scrolling="no" title="Charge d'un condensateur soumis à un échelon de tension" src="https://www.geogebra.org/material/iframe/id/nhcttgqu/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" style="border:0; width:100%; aspect-ratio: 1271 / 607;"></iframe>

{{< question >}}
Dessiner la maille constituée lorsque $t \geq  0$.
{{< /question >}}

{{< solution "Réponse" >}}
![](/terminales-pc/chap-5/5-2/Doc-8.svg?width=45%)
{{< /solution >}}

{{< question >}}
Identifier, sur la figure 2, les courbes qui correspondent :
- à la force électromotrice (fem), c'est-à-dire à la tension aux bornes du générateur ;
- à la tension $u_R$ aux bornes de la résistance ;
- à la tension $u_C$ aux bornes du condensateur.

Justifier les choix.
{{< /question >}}

{{< solution "Réponse" >}}
**Observations :**
- Les fonctions représentées par les courbes verte et mauve sont **discontinues** à la date $t = 0$, puisqu'elles passent de 0 V à des tensions non nulles.
- La fonction représentée par la courbe verte est constante pour $t > 0$.
- La fonction représentée par la courbe mauve est décroissante pour $t > 0$.
- La fonction représentée par la courbe orange est continue et croissante.

**Interprétations :**
- La tension aux bornes du dipôle $(R, C)$ varie brutalement, puisqu'elle passe de la valeur 0 V à la valeur $E$. Ce comportement correspond à celui de la courbe verte.
- On sait que le courant électrique finit par disparaître dans le circuit. Comme $u_R$ est la tension aux bornes de la résistance, $u_R = R i$. Si l'intensité du courant électrique s'annule, alors la tension $u_R$ doit aussi s'annuler. Ce comportement correspond à celui de la courbe mauve.
- La loi des mailles nous donne : $-E + u_R + u_C = 0 \Leftrightarrow  u_C = E - u_R$.

  Comme $u_R (\infty) = 0$, $u_C (\infty) = E$. De plus, d'après ce qui a été dit ci-dessus, $u_R (0) = E$, donc $u_C (0) = 0$. Ce comportement correspond à celui de la courbe orange.
{{< /solution >}}

{{< note success "Charge d'un condensateur" >}}
- Le condensateur d'un dipôle $(R, C)$ soumis à un échelon de tension ne se charge pas instantanément : *la charge du condensateur est un **phénomène transitoire***.
- Une fois la charge achevée, le régime est dit **permanent et constant**.
- Les tensions aux bornes du dipôle $(R, C)$ et de la résistance sont discontinues à la date $t = 0$, mais *la tension aux bornes du condensateur est continue à la date* $t = 0$.
{{< /note >}}

**Constante de temps**

{{< question >}}
Démontrer que le produit $R C$ a la dimension d'un temps.
{{< /question >}}

{{< solution "Réponse" >}}
- $[R] = {\displaystyle \frac{U}{I}}$ (*une résistance est une tension divisée par une intensité*).
- $[C] = {\displaystyle \frac{[Q]}{U}}$ (une capacité est une charge divisée par une tension).
- Comme $[Q] = I T$ (intensité fois temps), alors $[C] = {\displaystyle \frac{I T}{U}}$.
- Finalement, $[R C] = {\displaystyle \frac{U}{I} \times \frac{I T}{U}} = T$.
{{< /solution >}}

{{< note success "Constante de temps" >}}
Le produit $\tau = R C$, *homogène à une durée*, est la **constante de temps** du dipôle $(R, C)$. La constante $\tau$ s'exprime en seconde (s).

On va montrer que le **régime transitoire** est *pratiquement achevé après une durée égale à $5 \tau$.*
{{< /note >}}

### Étude théorique

#### Équation différentielle

![](/terminales-pc/chap-5/5-2/Doc-9.svg?width=45%)

> *Figure 3 : Constitution du circuit pour $t \geq  0$.*

**Condition initiale**

$u_C (0) = 0$ : le condensateur est initialement déchargé.

{{< note warning "Attention" >}}
*Toujours se placer en convention récepteur pour le condensateur !*
{{< /note >}}

{{< question >}}
En appliquant la loi des mailles, trouver la relation entre les tensions $E$, $u_R$ et $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
Loi des mailles :
$$-E + u_R + u_C = 0$$
Cette équation fait intervenir deux fonctions inconnues :
- celle que l'on cherche, $u_C (t)$ ;
- la fonction $u_R (t)$.

L'objectif des prochaines questions est de parvenir à exprimer $u_R (t)$ en fonction de $u_C (t)$, de façon à pouvoir résoudre l'équation.
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_R$.
{{< /question >}}

{{< solution "Réponse" >}}
*Pour le sens du courant choisi*,
$$u_R = R i$$
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre la charge $+q$ de l'armature du condensateur et la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$q = C u_C$$
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la charge $+q$ de l'armature du condensateur.
{{< /question >}}

{{< solution "Réponse" >}}
$$i = \frac{\mathrm{d} q}{\mathrm{d} t}$$
{{< /solution >}}

{{< question >}}
En déduire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$i = \frac{\mathrm{d} q}{\mathrm{d} t} = \frac{\mathrm{d} (C u_C)}{\mathrm{d} t}$$
Comme $C$ est une constante,
$$i = C \frac{\mathrm{d} u_C}{\mathrm{d} t}$$
{{< /solution >}}

{{< question >}}
En déduire la relation qui existe entre les tensions $u_R$ et $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$u_R = R i = R C \frac{\mathrm{d} u_C}{\mathrm{d} t}$$
{{< /solution >}}

{{< question >}}
Dans la relation issue de la loi des mailles, remplacer la tension $u_R$ par l'expression déterminée à la question précédente, de façon à ce que la seule inconnue qui apparaisse au final soit la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$R C \frac{\mathrm{d} u_C}{\mathrm{d} t} + u_C = E \quad\ \text{pour}\ t \geq  0$$
ou
$$\frac{\mathrm{d} u_C}{\mathrm{d} t} + \frac{u_C}{R C} = \frac{E}{R C} \quad\ \text{pour}\ t \geq  0$$
Cette expression est une équation différentielle linéaire du premier ordre, à coefficients constants et à second membre constant.
{{< /solution >}}

Avant de résoudre l'équation, on peut déjà prévoir l'allure de la courbe $u_C (t)$ en lisant l'équation différentielle comme une information sur la pente de cette courbe.

{{< question >}}
À partir de l'équation différentielle, exprimer la pente ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ en fonction de $u_C$. Que vaut cette pente à la date $t = 0$ ? Comment évolue-t-elle lorsque $u_C$ se rapproche de $E$ ?
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Isoler ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ dans l'équation $R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C = E$, puis utiliser la condition initiale $u_C (0) = 0$.
{{< /note >}}

{{< solution "Réponse" >}}
$$\frac{\mathrm{d} u_C}{\mathrm{d} t} = \frac{E - u_C}{R C}$$
À $t = 0$, $u_C (0) = 0$, donc la pente vaut ${\displaystyle \frac{E}{R C}} > 0$ : la tension commence par augmenter rapidement.

Tant que $u_C < E$, la pente reste positive : $u_C$ augmente. Mais plus $u_C$ se rapproche de $E$, plus $E - u_C$ est petit, donc plus la pente est faible. Lorsque $u_C = E$, la pente est nulle : la tension cesse d'évoluer.
{{< /solution >}}

{{< question >}}
En déduire l'allure attendue pour la courbe $u_C (t)$. La comparer à la courbe orange de la figure 2.
{{< /question >}}

{{< solution "Réponse" >}}
La courbe part de 0 avec une pente maximale, puis elle monte de moins en moins vite et s'approche de la droite $u = E$ sans jamais la dépasser (la pente s'annulerait avant). C'est exactement l'allure de la courbe orange de la figure 2.

On cherche donc une fonction qui part de 0, croît de plus en plus lentement et tend vers $E$ : c'est ce que fournit la famille de solutions donnée ci-dessous.
{{< /solution >}}

#### Solution de l'équation différentielle

On montre, en mathématiques, qu'une **famille de solutions** de cette équation différentielle est :
$$u_C (t) = A + B e^{-t / \tau}$$
où $A$, $B$ et $\tau$ sont des constantes.

*L'objectif de la suite de cette section est de déterminer l'expression de **la solution au problème**.*

{{< question >}}
Montrer que la famille de solutions donnée vérifie bien l'équation différentielle et en déduire l'expression de $\tau$.
{{< /question >}}

{{< solution "Réponse" >}}
**Méthode.** On remplace, dans l'équation différentielle, $u_C$ par la famille de solutions.

Puisque ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} = {\displaystyle \frac{\mathrm{d} (A + B e^{-t / \tau})}{\mathrm{d} t}} = -{\displaystyle \frac{B}{\tau}} e^{-t / \tau}$, l'équation devient :
$$-\frac{B}{\tau} e^{-t / \tau} + \frac{A}{R C} + \frac{B}{R C} e^{-t / \tau} = \frac{E}{R C} \Leftrightarrow  (-\frac{1}{\tau} + \frac{1}{R C}) B e^{-t / \tau} + \frac{A}{R C} = \frac{E}{R C}$$
Le terme à droite de l'égalité, ${\displaystyle \frac{E}{R C}}$, ne dépend pas du temps. Celui à gauche de cette même égalité ne peut donc pas dépendre du temps. Ceci n'est possible que si
$$-\frac{1}{\tau} + \frac{1}{R C} = 0 \Leftrightarrow  \tau = R C$$
On en déduit alors que $A = E$.

**Conclusion.** La famille de solutions convient à la condition qu'elle s'écrive :
$$u_C (t) = E + B e^{-t / \tau}$$
avec $\tau = R C$.

{{< note info "Remarque" >}}
La solution au problème n'est pas encore déterminée, puisque la constante $B$ reste à déterminer.
{{< /note >}}
{{< /solution >}}

{{< question >}}
À partir de la condition initiale (*le condensateur est initialement déchargé*), déterminer la fonction solution du problème.
{{< /question >}}

{{< solution "Réponse" >}}
**Méthode.** On écrit l'expression de la tension aux bornes du condensateur à la date $t = 0$ :
$$u_C (0) = 0 = E + B e^{-0 / \tau} = E + B \Leftrightarrow  B = -E$$

**Conclusion.**
$$u_C (t) = E (1 - e^{-t / \tau})$$
avec $\tau = R C$.

On retrouve donc bien le comportement de l'étude expérimentale : *la fonction est bien continue en $t = 0$ et sa limite à l'infini est $E$*.
{{< /solution >}}

#### Signification physique de $\tau$

{{< question >}}
Donner l'expression de la tension $u_C$ à la date $t = \tau$.
{{< /question >}}

{{< solution "Réponse" >}}
$$u_C (\tau) = E (1 - e^{-\tau / \tau}) = E (1 - e^{-1}) = 0{,}63 E$$
{{< /solution >}}

{{< note success "Signification de la constante de temps" >}}
La constante de temps $\tau$ donne l'ordre de grandeur de la durée de la charge du condensateur :
- après une durée égale à $\tau$, le condensateur est chargé à 63 % ;
- après une durée égale à $5 \tau$, il est chargé à plus de 99 %.
{{< /note >}}

{{< question >}}
On note $t_{1/2}$ la durée au bout de laquelle $u_C = {\displaystyle \frac{E}{2}}$. Donner l'expression de $t_{1/2}$ en fonction de $\tau$.

{{< note info "Remarque" >}}
Nous retrouverons la grandeur $t_{1/2}$ plusieurs fois cette année : *chaque fois que le phénomène sera gouverné par une équation différentielle linéaire du premier ordre à coefficients constants*.
{{< /note >}}
{{< /question >}}

{{< solution "Réponse" >}}
$$u_C (t_{1/2}) = E (1 - e^{-t_{1/2} / \tau}) = \frac{E}{2} \Leftrightarrow  e^{-t_{1/2} / \tau} = \frac{1}{2} \Leftrightarrow  -\frac{t_{1/2}}{\tau} = \ln(\frac{1}{2}) \Leftrightarrow  t_{1/2} = \tau \ln 2$$
{{< /solution >}}

{{< note success "Détermination graphique de $\tau$" >}}
On peut aussi *déterminer graphiquement* la valeur de la constante de temps $\tau$ : la tangente à l'origine ($t = 0$) de la courbe $u_C (t)$ coupe la droite d'équation $u = E$ en un point d'abscisse $\tau$.
{{< /note >}}

<iframe scrolling="no" title="Charge d'un condensateur soumis à un échelon de tension" src="https://www.geogebra.org/material/iframe/id/nhcttgqu/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" style="border:0; width:100%; aspect-ratio: 1271 / 607;"></iframe>

#### Expression de l'intensité du courant électrique

{{< question >}}
Déterminer l'expression de la fonction $i(t)$ et donner ses caractéristiques.
{{< /question >}}

{{< solution "Réponse" >}}
$i(t) = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ et $q = C u_C$, donc $i(t) = C \, {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$.

Si on remplace $u_C$ par son expression, on obtient $i(t) = C \, {\displaystyle \frac{\mathrm{d} (E (1 - e^{-t / \tau}))}{\mathrm{d} t}}$, donc
$$i(t) = \frac{C E}{\tau} e^{-t / \tau} \Leftrightarrow  i(t) = \frac{E}{R} e^{-t / \tau}$$
Juste avant la date $t = 0$ (date notée $0^-$), aucun courant ne circule dans le circuit (puisqu'il est ouvert), donc $i(0^-) = 0$. Juste après ($t = 0^+$), $i(0^+) = {\displaystyle \frac{E}{R}} > 0$.

*L'intensité du courant électrique $i(t)$ est une fonction discontinue à la date $t = 0$. Pour $t \geq  0$, $i(t)$ est une fonction décroissante qui a pour limite 0 à l'infini.*
{{< /solution >}}

{{< question >}}
Démontrer que $i(t_{1/2}) = {\displaystyle \frac{I_0}{2}}$ avec $I_0 = {\displaystyle \frac{E}{R}}$.
{{< /question >}}

{{< solution "Réponse" >}}
D'après la question précédente, $i(t) = I_0 e^{-t / \tau}$. Or $t_{1/2} = \tau \ln 2$, donc :
$$i(t_{1/2}) = I_0 e^{-\tau \ln 2 / \tau} = I_0 e^{-\ln 2} = \frac{I_0}{e^{\ln 2}} = \frac{I_0}{2}$$
{{< /solution >}}

## Décharge d'un condensateur dans une résistance

Comment varient la tension aux bornes du condensateur d'un dipôle $(R, C)$ et l'intensité du courant qui le traverse lors de la décharge du condensateur à travers la résistance ?

### Étude expérimentale

On bascule le commutateur en **position 1** à une date que l'on considère comme la date $t = \pu{0 s}$ (on redéfinit l'origine des temps) et on enregistre l'évolution dans le temps des tensions $u_C$ et $u_R$.

{{< note info "Remarque" >}}
*Le condensateur est alors chargé.*
{{< /note >}}

On obtient les enregistrements représentés ci-dessous.

![](/terminales-pc/chap-5/5-2/Doc-10.svg?width=100%)

> *Figure 4 : Résultats expérimentaux lors de la décharge d'un condensateur dans une résistance.*

<iframe scrolling="no" title="Décharge d'un condensateur dans une résistance" src="https://www.geogebra.org/material/iframe/id/vcth5yzh/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" style="border:0; width:100%; aspect-ratio: 1271 / 607;"></iframe>

{{< question >}}
Dessiner la maille constituée lorsque $t \geq  0$.
{{< /question >}}

{{< solution "Réponse" >}}
![](/terminales-pc/chap-5/5-2/Doc-11.svg?width=40%)
{{< /solution >}}

{{< question >}}
On choisit le sens du courant indiqué sur le schéma ci-dessous. L'intensité vérifie alors $i = {\displaystyle \frac{\mathrm{d} q_A}{\mathrm{d} t}}$. Pendant la décharge, la charge $q_A$ de l'armature $A$ augmente-t-elle ou diminue-t-elle ? Prédire le signe de $i$, puis celui de $u_R$.
![](/terminales-pc/chap-5/5-2/Doc-11.svg?width=40%)
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Au début de la décharge, l'armature $A$ porte des charges positives. À la fin, le condensateur est déchargé. Quel est le signe de la dérivée d'une fonction décroissante ?
{{< /note >}}

{{< solution "Réponse" >}}
Au début de la décharge, $q_A = C E > 0$ ; à la fin, $q_A = 0$. La charge $q_A$ diminue, donc sa dérivée est négative : $i = {\displaystyle \frac{\mathrm{d} q_A}{\mathrm{d} t}} < 0$. Le courant circule dans le sens opposé au sens choisi.

Comme $u_R = R i$ avec $R > 0$, la tension $u_R$ est elle aussi négative.

{{< note info "Remarque" >}}
Le signe négatif ne signifie pas une erreur : il indique seulement que le courant réel circule dans le sens opposé à la flèche dessinée.
{{< /note >}}
{{< /solution >}}

{{< question >}}
Identifier, sur la figure 4, les courbes qui correspondent :
- à la tension $u_R$ aux bornes de la résistance ;
- à la tension $u_C$ aux bornes du condensateur.
{{< /question >}}

{{< solution "Réponse" >}}
La tension aux bornes d'un condensateur est une *fonction continue*. Comme le condensateur est chargé, $u_C (0^-) = E$, donc $u_C (0^+) = E$. De plus, les charges électriques quittent l'armature $A$ ; la tension $u_C (t)$ doit donc diminuer au cours du temps jusqu'à s'annuler, tout en restant positive. Ce comportement est celui de la courbe bleue.

La tension aux bornes de la résistance est l'image de l'intensité du courant qui circule dans le circuit. D'après la question précédente, *le courant électrique ne circule pas dans le sens choisi, mais dans le sens opposé* : l'intensité est négative, donc $u_R$ aussi. De plus, le courant électrique finit par disparaître, une fois l'équilibre électrique retrouvé sur les armatures du condensateur. L'intensité de ce courant doit donc s'annuler. Ce comportement est celui de la courbe mauve.
{{< /solution >}}

### Étude théorique

#### Équation différentielle

![](/terminales-pc/chap-5/5-2/Doc-12.svg?width=40%)

> *Figure 5 : Constitution du circuit pour $t \geq  0$.*

**Condition initiale**

$u_C (0) = E$ : le condensateur est initialement chargé.

{{< note warning "Attention" >}}
*Toujours se placer en convention récepteur pour le condensateur !*
{{< /note >}}

{{< question >}}
En appliquant la loi des mailles, trouver la relation entre les tensions $u_R$ et $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
Loi des mailles :
$$u_R + u_C = 0$$
Cette équation fait intervenir deux fonctions inconnues :
- celle que l'on cherche, $u_C (t)$ ;
- la fonction $u_R (t)$.

L'objectif des prochaines questions est de parvenir à exprimer $u_R (t)$ en fonction de $u_C (t)$, de façon à pouvoir résoudre l'équation.
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_R$.
{{< /question >}}

{{< solution "Réponse" >}}
$$u_R = R i$$
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre la charge $+q$ de l'armature du condensateur et la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$q = C u_C$$
{{< /solution >}}

{{< question >}}
Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la charge $q$ de l'armature du condensateur.
{{< /question >}}

{{< solution "Réponse" >}}
$$i = \frac{\mathrm{d} q}{\mathrm{d} t}$$
{{< /solution >}}

{{< question >}}
En déduire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$i = \frac{\mathrm{d} (C u_C)}{\mathrm{d} t} = C \frac{\mathrm{d} u_C}{\mathrm{d} t}$$
car $C$ est une constante.
{{< /solution >}}

{{< question >}}
En déduire la relation qui existe entre les tensions $u_R$ et $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$u_R = R i = R C \frac{\mathrm{d} u_C}{\mathrm{d} t}$$
{{< /solution >}}

{{< question >}}
Dans la relation issue de la loi des mailles, remplacer la tension $u_R$ par l'expression déterminée à la question précédente, de façon à ce que la seule inconnue qui apparaisse au final soit la tension $u_C$.
{{< /question >}}

{{< solution "Réponse" >}}
$$R C \frac{\mathrm{d} u_C}{\mathrm{d} t} + u_C = 0 \quad\ \text{pour}\ t \geq  0$$
ou
$$\frac{\mathrm{d} u_C}{\mathrm{d} t} + \frac{u_C}{R C} = 0 \quad\ \text{pour}\ t \geq  0$$
Cette expression est une équation différentielle linéaire du premier ordre, à coefficients constants et sans second membre.
{{< /solution >}}

#### Solution de l'équation différentielle

On montre, en mathématiques, qu'une **famille de solutions** de cette équation différentielle est :
$$u_C (t) = A + B e^{-t / \tau}$$
où $A$, $B$ et $\tau$ sont des constantes.

*L'objectif de la suite de cette section est de déterminer l'expression de **la solution au problème**.*

{{< question >}}
Montrer que la famille de solutions donnée vérifie bien l'équation différentielle et en déduire l'expression de $\tau$.
{{< /question >}}

{{< solution "Réponse" >}}
**Méthode.** On remplace, dans l'équation différentielle, $u_C$ par la famille de solutions.

Puisque ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} = {\displaystyle \frac{\mathrm{d} (A + B e^{-t / \tau})}{\mathrm{d} t}} = -{\displaystyle \frac{B}{\tau}} e^{-t / \tau}$, l'équation devient :
$$-\frac{B}{\tau} e^{-t / \tau} + \frac{A}{R C} + \frac{B}{R C} e^{-t / \tau} = 0 \Leftrightarrow  (-\frac{1}{\tau} + \frac{1}{R C}) B e^{-t / \tau} + \frac{A}{R C} = 0$$
Le terme à droite de l'égalité est nul, donc indépendant du temps. Celui à gauche de cette même égalité ne peut donc pas dépendre du temps. Ceci n'est possible que si
$$-\frac{1}{\tau} + \frac{1}{R C} = 0 \Leftrightarrow  \tau = R C$$
On en déduit alors que $A = 0$.

**Conclusion.** La famille de solutions convient à la condition qu'elle s'écrive :
$$u_C (t) = B e^{-t / \tau}$$
avec $\tau = R C$.
{{< /solution >}}

{{< question >}}
À partir de la condition initiale, déterminer la fonction solution du problème.
{{< /question >}}

{{< solution "Réponse" >}}
**Méthode.** On écrit l'expression de la tension aux bornes du condensateur à la date $t = 0$ :
$$u_C (0) = E = B e^{-0 / \tau} = B \Leftrightarrow  B = E$$

**Conclusion.**
$$u_C (t) = E e^{-t / \tau}$$
avec $\tau = R C$.

On retrouve donc bien le comportement de l'étude expérimentale : *la fonction est bien continue en $t = 0$, positive et décroissante*.
{{< /solution >}}

{{< question >}}
Déterminer l'expression de la fonction $i(t)$ et donner ses caractéristiques.
{{< /question >}}

{{< solution "Réponse" >}}
$i(t) = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ et $q = C u_C$, donc $i(t) = C \, {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$.

Si on remplace $u_C$ par son expression, on obtient $i(t) = C \, {\displaystyle \frac{\mathrm{d} (E e^{-t / \tau})}{\mathrm{d} t}} = C E \, {\displaystyle \frac{\mathrm{d} (e^{-t / \tau})}{\mathrm{d} t}}$, puisque $E$ est une constante, donc
$$i(t) = -\frac{C E}{\tau} e^{-t / \tau} \Leftrightarrow  i(t) = -\frac{E}{R} e^{-t / \tau}$$
Juste avant la date $t = 0$, aucun courant ne circule dans le circuit (puisqu'il est ouvert), donc $i(0^-) = 0$. Juste après, $i(0^+) = -{\displaystyle \frac{E}{R}} < 0$.

*L'intensité du courant électrique est une fonction discontinue en $t = 0$ et négative pour $t > 0$. Sa valeur absolue $|i(t)|$ décroît et tend vers 0 à l'infini.*
{{< /solution >}}

{{< note success "À l'issue de cette activité, je sais…" >}}
- Je sais décrire un condensateur et donner son symbole.
- Je sais expliquer pourquoi un courant transitoire apparaît lors de la charge d'un condensateur, puis disparaît.
- Je sais écrire $q_A = -q_B$ et relier l'intensité du courant à la charge d'une armature, $i = {\displaystyle \frac{\mathrm{d} q_A}{\mathrm{d} t}}$, pour un sens du courant choisi.
- Je sais écrire la relation $q = C u$ entre la charge et la tension, et donner l'unité de la capacité.
- Je sais citer des ordres de grandeur de capacités usuelles.
- Je sais identifier, sur un enregistrement, les tensions aux bornes du générateur, de la résistance et du condensateur lors de la charge et de la décharge, en m'appuyant sur la continuité de $u_C$.
- Je sais montrer que $\tau = R C$ est homogène à une durée.
- Je sais établir l'équation différentielle vérifiée par $u_C$ lors de la charge et lors de la décharge.
- Je sais prévoir l'allure de $u_C (t)$ à partir de l'équation différentielle, en l'utilisant comme une information sur la pente.
- Je sais vérifier qu'une famille de fonctions est solution de cette équation et utiliser la condition initiale pour obtenir la solution.
- Je sais établir l'expression de $i(t)$ lors de la charge et de la décharge.
- Je sais prévoir le signe de l'intensité du courant à partir de l'évolution de la charge d'une armature, pour un sens du courant choisi.
- Je sais exploiter $u_C (\tau) = 0{,}63 E$, la durée $5 \tau$ et $t_{1/2} = \tau \ln 2$.
- Je sais déterminer graphiquement $\tau$ à l'aide de la tangente à l'origine.
{{< /note >}}
