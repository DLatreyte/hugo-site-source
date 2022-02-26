---
title: "Le dipôle (R,C)"
subtitle: "Chapitre 6,2"
author: ""
type: ""
date: 2020-10-30T20:15:29+04:00
draft: false
toc: true
tags: ["Annale", "Courant électrique", "Tension", "Potentiel électrique", "Générateur", "Dipôle", "Branche", "Maille", "Nœud", "Loi des nœuds", "Loi des mailles", "Loi d'Ohm", "Résistance","Condensateur", "Équation différentielle linéaire à coefficients constants"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

Les premiers condensateurs sont apparus vers 1745. Il s'agissait en fait d'une bouteille de Leyde : une fiole à moitié remplie d'eau dont l'ouverture était obturée par un bouchon de liège percé d'une tige métallique trempant dans l'eau.

<img src="/terminales-pc/chap-5/chap-5-2-0.png" alt="" width="30%" />

La première application de ce condensateur était de donner des commotions (chocs électriques ou électrisations) au public dans les foires. Par exemple, à Versailles, on présenta au roi Louis XV l'expérience de la décharge d'une grosse bouteille de Leyde à travers le circuit formé de plus de deux cents courtisans.

{{< youtube oFdpqii90gs >}}

Le physicien Volta a décrit le fonctionnement de la bouteille de Leyde vers 1782. Les condensateur se sont alors améliorés et surtout miniaturisés.

<img src="/terminales-pc/chap-5/chap-5-2-8.png" alt="" width="30%" />

> L'étude du condensateur va bien au-delà de la compréhension du fonctionnement de ce composant. De nombreux dispositifs, capteurs ou phénomènes (les orages par exemples) présentent sur un **comportement capacitif**. 

## Les condensateurs

### Description

{{% note tip %}}
Un condensateur est un composant électrique formé de deux armatures métalliques conductrices en regard (plaques ou films métalliques) séparés par un isolant (air, papier, céramique, ...) appelé **diélectrique**.
{{% /note %}}

> Symbole d'un condensateur
<img src="/terminales-pc/chap-5/chap-5-2-1.png" alt="" width="30%" />

### Comment se comporte un condensateur dans un circuit électrique ?

On réalise un circuit électrique comportant, en série, un condensateur, une lampe, un générateur de tension continue et un interrupteur.
<img src="/terminales-pc/chap-5/chap-5-2-2.png" alt="" width="40%" />

1. Que se passe-t-il lorsqu'on ferme l'interrupteur $K$ ?

{{% solution "Réponse" %}}
- Lorsqu'on ferme l'interrupteur $K$, la lampe s'éclaire, puis s'éteint progressivement (la durée au bout de laquelle elle s'éteint dépend du condensateur utilisé). Un courant **transitoire** apparaît donc dans le circuit.
- Le courant électrique ne peu s'établir durablement dans le circuit puisque celui-ci est en fait ouvert (coupé par la présence du diélectrique entre les armatures du condensateur). Le courant, lors du régime **permanent** est nul.
{{% /solution %}}

2. Comment expliquer l'apparition d'un courant transitoire puis l'absence de courant lors du régime permanent ?

{{% solution "Réponse" %}}
- Lorsqu'on ferme l'interrupteur, un courant électrique apparaît dans le circuit : des électrons arrivent au niveau de l'armature $B$ et des électrons quittent l'armature $A$. Comme le circuit est ouvert, *les électrons ne peuvent que s'accumuler* en $B$ ; l'*armature* $B$ *se charge négativement*.  
Dans le même temps l'*armature $A$ se charge positivement car aucun électron ne vient combler le déficit laissé par ceux qui sont partis*.

- L'intensité du courant électrique est identique en tout point du circuit : le débit avec lequel les électrons arrivent en $B$ est égal au débit avec lequel les électrons quittent $A$ : $q_A(t) = -q_B(t)$.

- Les charges électriques opposées, aux bornes du condensateur, donnent naissance à la tension électrique $u_{AB}$.  
Le courant électrique finit par disparaître dans le circuit : la tension aux bornes de la lampe s'annule donc. Une application de la loi des mailles nous apprend que, dans le régime permanent $u_{AB} = E$.  

- Dans le régime permanent, le générateur entretien donc un déséquilibre électrostatique qui le *maintien de la **charge du condensateur**, c'est à dire le **stockage de l'énergie électrique**.* 
<img src="/terminales-pc/chap-5/chap-5-2-3.png" alt="" width="40%" />
{{% /solution %}}

{{% note tip %}}
- À tout moment, les charges électriques présentes sur les armatures d'un condensateur sont liées : $$q_A(t) = -q_B(t)$$
**Rappel :** la charge électrique s'exprime en **coulomb** (symbole : C).
- Un condensateur stockant des charges électriques sur ses armatures est dit **chargé**, ce stockage correspond à un **stockage d'énergie électrique**.
{{% /note %}}

### Charge électrique et intensité du courant électrique

3. Quelle est la relation entre l'intensité du courant et les charges portées
par les armatures ?

<img src="/terminales-pc/chap-5/chap-5-2-9.png" alt="" width="35%" />

{{% solution "Réponse" %}}
- L'intensité du courant électrique est la charge électrique qui traverse une section quelconque du circuit chaque seconde, donc $i(t) = \dfrac{\mathrm{d}q(t)}{\mathrm{dt}}$.
- On **choisit** un sens de circulation pour $i(t)$ et on en déduit la relation : $i(t) = \dfrac{\mathrm{d}q_A(t)}{\mathrm{dt}}$ (les charges positives s'accumulent sur l'armature $A$) et $i(t) = -\dfrac{\mathrm{d}q_B(t)}{\mathrm{dt}}$ puisque $q_B(t) = -q_A(t)$.
{{% /solution %}}

{{% note tip %}}
Lorsqu'on souhaite exprimer la relation qui existe entre l'intensité du courant électrique et la charge portée par une armature, 
1. On choisit un sens de circulation pour le courant électrique.
2. On écrit la relation entre l'intensité du courant électrique et la charge au niveau de l'armature.

Sur l'exemple choisi, 
$$i(t) = \dfrac{\mathrm{d}q_A(t)}{\mathrm{dt}} = -\dfrac{\mathrm{d}q_B(t)}{\mathrm{dt}}$$
{{% /note %}}

{{% note normal %}}
- Si après calcul, $i>0$, alors *le courant électrique **circule effectivement dans le sens choisi*** (on a deviné correctement) et la *fonction $q_A$ est **croissante*** : les *charges positives s'accumulent* sur l'armature $A$.
- Si après calcul, $i<0$, *le courant électrique **circule dans le sens opposé au sens choisi*** et la *fonction $q_A$ est **décroissante*** : les *charges positives quittent* l'armature $A$.
{{% /note %}}


{{% note exercise %}}
On charge un condensateur (initialement déchargé) à l'aide d'un *générateur de courant* qui délivre un courant continu d'intensité $I$.  
Exprimer la charge $q_A$ aux bornes de l'armature $A$ après $\Delta t$ secondes.
{{% /note %}}
{{% solution "Réponse" %}}
- $i(t) = I = \dfrac{\mathrm{d}q_A}{\mathrm{dt}}$. 
- L'opération qui consiste à obtenir la fonction $q_A$ à partir de l'expression de sa dérivée s'appelle l'intégration. Ce concept sera développé en cours de mathématique. En Physique, il suffit de se poser la question : ***« Quelle fonction, une fois dérivée par rapport au temps, donne une constante ? »***  
Ici la réponse est simple $q_a(t) = I t + A$, où $A$ est une constante qui a la dimension d'une intensité, puisque $\dfrac{\mathrm{d}q_A}{\mathrm{dt}} = \dfrac{\mathrm{d}(I t + A))}{\mathrm{dt}} = (I t + A)\rq = I$
- En fait, $q_a(t) = I t + A$ n'est pas **la solution** mais **une famille de solutions**. Pour trouver la solution, il faut connaître une **valeur particulière** (souvent la *valeur initiale*) : ici on sait que le condensateur était initialement déchargé, donc $q_A(0) = \pu{0 A}$. On en déduit que $A = 0$ et $q_a(t) = I t$.
{{% /solution %}}

### Capacité d'un condensateur

On peut montrer que :
{{% note tip %}}
À chaque instant, la charge $q_A$ de l'armature $A$ du condensateur est proportionnelle à la tension $u_{AB}$ entre ses armatures $A$ et $B$ :

$$q_A = C \cdot u_{AB}$$

$C$ est appelée **capacité du condensateur**.  
Si $q_A$ est en coulomb (C) et $u_{AB}$ en volt (V), $C$ s'exprime en farad (F).
{{% /note %}}

**Remarque :** $C>0$ donc $q_A$ et $u_{AB}$ sont de même signe.

**Remarque :** La capacité $C$ est donc la charge stockée lorsque la tension entre les deux armatures est égale à $\pu{1 V}$.

> Quelques ordres de grandeurs

<center>

| Utilisation | Capacité en farad (F) |
| :---: | :---: |
| mémoire d'ordinateur | 0,1 à 1 |
| allumage de voiture | $10^{-4}$ |
| flash électronique | $10^{-5}$ |
| détection radio | $10^{-9}$ à $10^{-12}$ |

</center>

## Charge d'un condensateur par un échelon de tension

{{% note tip %}}
On appelle **échelon de tension** une *tension qui varierait brutalement de la valeur $\pu{0 V}$ à une valeur $E$.*
{{% /note %}}

L'association en série d'un condensateur de capacité $C$ et d'un conducteur ohmique de résistance $R$ constitue un dipôle $(R, C)$.

### Étude expérimentale

#### Résultats expérimentaux

On réalise le montage suivant :
<img src="/terminales-pc/chap-5/chap-5-2-4.png" alt="" width="80%" />
On bascule le commutateur en position 2 et on enregistre les tensions $u_{DA}$ et $u_{AB}$. On obtient les enregistrements suivants :

<iframe scrolling="no" title="Charge d'un condensateur soumis à un échelon de tension" src="https://www.geogebra.org/material/iframe/id/nhcttgqu/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="900px" height="450px" style="border:0px;"> </iframe>

4. Identifier les courbes qui correspondent :
    - à force électromotrice (fem), c'est à dire à la tension aux bornes du générateur ;
    - à la tension $u_{DA}$ aux bornes de la résistance ;
    - à la tension $u_{AB}$ aux bornes du condensateur.
{{% solution "Réponse" %}}
- La tension aux bornes du dipôle $(R, C)$ varie brutalement puisqu'elle passe de la valeur $\pu{0 V}$ à la valeur $E$. Ce comportement correspond à celui de la courbe verte.
- On sait que le courant électrique finit par disparaître dans le circuit. Comme $u_{DA}$ est la tension aux bornes de la résistance, $u_{DA} = R i_{DA}$. Si l'intensité du courant électrique s'annule, alors la tension $u_{DA}$ doit aussi s'annuler. Ce comportement correspond à celui de la courbe mauve.
- La loi des mailles nous donne : $-E + u_{DA} + u_{AB} = 0 \iff u_{AB} = E - u_{DA}$. Ce comportement est celui de la courbe orange.
{{% /solution %}}


{{% note tip %}}
- Le condensateur d'un dipôle $(R, C)$ soumis à un échelon de tension ne se charge pas instantanément : *la charge du condensateur est un **phénomène transitoire**.*
- Une fois la charge achevée, le régime est dit **permanent et constant**.
- Les tensions aux bornes du dipôle $(R,C)$ et de la résistance sont discontinues en $t=0$ mais **la tension aux bornes du condensateur est continue** à la date $t=0$.
{{% /note %}}


#### Constante de temps

5. Faire évoluer les valeurs de la résistance et de la capacité. Observer l'influence de ces deux paramètres sur la durée de charge du condensateur (ou la durée de décroissance de l'intensité du courant électrique).

{{% solution "Réponse" %}}
{{% note tip %}}
La durée de la charge du condensateur d'un dipôle $(R, C)$ augmente quand la valeur du produit $R \cdot C$ augmente.
{{% /note %}}
{{% /solution %}}

6. Démontrer que le produit $R \cdot C$ a la dimension d'un temps.
{{% solution "Réponse" %}}
- $[R] = \dfrac{U}{I}$ (une résistance est une tension sur une intensité);
- $[C] = \dfrac{[Q]}{U}$ (une capacité est une charge sur tension). Or $[Q] = I \cdot T$ (intensité fois temps). Donc $[C] = \dfrac{I \cdot T}{U}$.
- Finalement $[R\cdot C] = \dfrac{U}{I} \times \dfrac{I \cdot T}{U} = T$.
{{% /solution %}}

{{% note tip %}}
Le produit $R \cdot C = \tau$, *homogène à une durée*, est la *constante de temps* du dipôle $(R, C)$. La constante $\tau$ s'exprime en seconde (s).  
On va montrer que le régime transitoire est pratiquement achevé après une durée égale à $5\tau$.
{{% /note %}}

### Étude théorique

#### Équation différentielle

À la date $t \geqslant 0$ le circuit est :
<img src="/terminales-pc/chap-5/chap-5-2-5.png" alt="" width="60%" />

{{% note warning %}}
Toujours se placer en convention récepteur pour le condensateur !
{{% /note %}}

7. En appliquant la loi des mailles, trouver la relation entre les tensions $E$, $u_{DA}$ et $u_{AB}$.
{{% solution "Réponse" %}}
$$-E + u_{DA} + u_{AB} = 0$$
Cette équation fait intervenir deux fonctions inconnues : 
- celle que l'on cherche $u_{AB} (t)$ ;
- la fonction $u_{DA} (t)$.

L'objectif des prochaines questions est de parvenir à exprimer $u_{DA} (t)$ en fonction de $u_{AB} (t)$ de façon à pouvoir résoudre l'équation.
{{% /solution %}}

8. Écrire la relation qui existe entre l'intensité $i(t)$ du courant électrique et la tension $u_{DA}$.
{{% solution "Réponse" %}}
$$u_{DA} = R\\, i$$
{{% /solution %}}

9. Écrire la relation qui existe entre la charge $q_A$ au niveau de l'armature $A$ du condensateur et la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$q_A = C\\, u_{AB} $$
{{% /solution %}}

10. Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la charge $q_A$ au niveau de l'armature $A$ du condensateur.
{{% solution "Réponse" %}}
$$i = \dfrac{\mathrm{d}q_A}{\mathrm{dt}}$$
{{% /solution %}}

11. En déduire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$i = C\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$$
{{% /solution %}}

12. En déduire la relation qui existe entre les tensions $u_{DA}$ et $u_{AB}$.
{{% solution "Réponse" %}}
$$u_{DA} = RC\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$$
{{% /solution %}}

13. Écrire à nouveau la loi des mailles de façon à ce qu'elle ne fasse apparaître qu'une seule inconnue, la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$RC\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} + u_{AB} = E$$
ou
$$\dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} + \dfrac{u_{AB}}{RC} = \dfrac{E}{RC}$$

Cette expression est une équation différentielle du premier ordre à coefficients constants.
{{% /solution %}}

#### Solution de l'équation différentielle

On montre, en mathématiques, qu'une famille de solutions de cette équation différentielle est :
$$u_{AB}(t) = A + B e^{-t/\tau}$$
où $A$, $B$ et $\tau$ sont des constantes.

14. Montrer que la famille de solutions donnée vérifie bien l'équation différentielle et en déduire l'expression de $\tau$.
{{% solution "Réponse" %}}
On substitue $u_{AB}$ par la famille de solution dans l'équation différentielle.  

Puisque $\dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} = \dfrac{\mathrm{d}(A + B e^{-t/\tau})}{\mathrm{dt}} = -\dfrac{B}{\tau} \\, e^{-t/\tau}$ l'équation devient $-\dfrac{B}{\tau} \\, e^{-t/\tau} + \dfrac{A}{RC} + \dfrac{B}{RC} e^{-t/\tau} = \dfrac{E}{RC} \iff \left( - \dfrac{1}{\tau} + \dfrac{1}{RC} \right)\\, B e^{-t/\tau} + \dfrac{A}{RC} = \dfrac{E}{RC}$. 

- Le terme à droite de l'égalité, $\dfrac{E}{RC}$ ne dépend pas du temps. Celui à gauche de cette même égalité ne peut donc pas dépendre du temps. Ceci n'est possible que si $\dfrac{1}{\tau} + \dfrac{1}{RC} = 0 \iff \boxed{\tau = RC}$.

- On en déduit que $\boxed{A = E}$

Finalement, la famille de solutions convient à la condition qu'elle s'écrive $$\boxed{u_{AB}(t) = E + B e^{-t/\tau} }$$ avec $\tau = RC$.
{{% /solution %}}

15. À partir des conditions initiales --- le condensateur est initialement déchargé ---, déterminer la fonction solution du problème.
{{% solution "Réponse" %}}
- $u_{AB}(0) = 0 = E + B e^{-0/\tau}= E + B \iff \boxed{B = -E}$

Finalement
$$\boxed{u_{AB}(t) = E (1 - e^{-t/\tau}) }$$ avec $\tau = RC$.  
On retrouve donc bien le comportement de l'étude expérimentale. En particulier, **la fonction est bien continue** en $t=0$ et sa limite à l'infini est $E$.
{{% /solution %}}

#### Signification physique de $\tau$

16. Donner l'expression de la tension $u_{AB}$ à la date $t=\tau$.
{{% solution "Réponse" %}}
$u_{AB}(\tau) = E (1 - e^{-\tau / \tau}) = E (1 - e^{-1}) = \pu{0,63}\\, E$.
{{% /solution %}}

{{% note tip %}}
La constante de temps $\tau$ donne l'ordre de grandeur de la durée de la charge du condensateur :
    - Après une durée égale à $\tau$, le condensateur est chargé à 63&nbsp;% de sa valeur maximale.
    - Après une durée égale à $5\tau$, il est chargé à plus de 99&nbsp;%.
{{% /note %}}

17. On note $t_{1/2}$ la durée au bout de laquelle $u_{AB} = \dfrac{E}{2}$. Donner l'expression de $t_{1/2}$ en fonction de $\tau$ (nous retrouverons la grandeur $t_{1/2}$, demi-charge, plusieurs fois cette année).
{{% solution "Réponse" %}}
$u_{AB}(t_{1/2}) = E (1 - e^{-t_{1/2} / \tau}) = \dfrac{E}{2} \iff e^{-t_{1/2} / \tau} = \dfrac{1}{2} \iff \dfrac{-t_{1/2}}{\tau} = \ln \left( \dfrac{1}{2} \right) \iff \boxed{t_{1/2} = \tau \ln 2}$.
{{% /solution %}}

{{% note tip %}}
On peut déterminer graphiquement la valeur de la constante de temps $\tau$ : <strong>la tangente en 0 à la courbe $u_{AB}(t)$ coupe la droite $U_g = E$ en un point d'abscisse $\tau$.</strong>
{{% /note %}}

<iframe scrolling="no" title="Charge d'un condensateur soumis à un échelon de tension" src="https://www.geogebra.org/material/iframe/id/nhcttgqu/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="900px" height="450px" style="border:0px;"> </iframe>

#### Expression de l'intensité du courant électrique

18. Déterminer l'expression de la fonction $i(t)$ et donner ses caractéristiques.
{{% solution "Réponse" %}}
- $i(t) = \dfrac{\mathrm{d}q_A}{\mathrm{dt}}$ et $q_A = C\\, u_{AB}$, donc $i(t) = C\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$.

- Si on substitue $u_{AB}$ par son expression, on obtient $i(t) = C\\, \dfrac{\mathrm{d}(E (1 - e^{-t / \tau}) )}{\mathrm{dt}}$ donc $ i(t) = \dfrac{CE}{\tau}\\, e^{-t / \tau}  \iff \boxed{i(t) = \dfrac{E}{R}\\, e^{-t / \tau} }$

- À la date $t = O^-$, aucun courant ne circule dans le circuit (puisqu'il est ouvert), donc $i(0^-) = 0$. À la date $t = 0^+$, $i(0^+) = \dfrac{E}{R} > 0$. L'intensité du courant électrique est une fonction discontinue.

- $i(t)$ est une fonction décroissante qui a pour limite 0 à l'infini.
{{% /solution %}}

19. Démontrer que $i(t_{1/2}) = \dfrac{I_0}{2}$ avec $I_0 = \dfrac{E}{R}$.


## Décharge d'un condensateur dans une résistance

Comment varient la tension aux bornes d'un condensateur d'un dipôle $(R, C)$ et l'intensité du courant qui le traverse lors de la décharge du condensateur à travers la résistance ?

### Étude expérimentale

On bascule le commutateur en position 1 et on enregistre les tensions $u_{DA}$ et $u_{AB}$. On obtient les enregistrements suivants :
<iframe scrolling="no" title="Décharge d'un condensateur dans une résistance" src="https://www.geogebra.org/material/iframe/id/vcth5yzh/width/1271/height/607/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="900px" height="450px" style="border:0px;"> </iframe>

20. Identifier les courbes qui correspondent :
    - à la tension $u_{DA}$ aux bornes de la résistance ;
    - à la tension $u_{AB}$ aux bornes du condensateur.
{{% solution "Réponse" %}}
- La tension aux bornes d'un condensateur est une **fonction continue** : $u_{AB}(O^-) = E$, donc $u_{AB}(O^+) = E$. De plus, les charges électriques quittent l'armature $A$ ; la tension $u_{AB}(t)$ doit donc diminuer au cours du temps jusqu'à s'annuler... tout en restant positive.  
Ce comportement est celui de la courbe bleu.

- La tension aux bornes de la résistance est l'image de l'intensité du courant qui circule dans le circuit. Comme les charges quittent l'armature $A$, le courant électrique ne circule pas dans le sens **choisi** mais dans le sens opposé. Cette intensité est négative.  
De plus, le courant électrique finit par disparaître, une fois l'équilibre électrique retrouvé sur les armatures du condensateur. L'intensité de ce courant doit donc s'annuler.   
Ce comportement est celui de la courbe mauve.
{{% /solution %}}

### Étude théorique

#### Équation différentielle

- À la date $t \geqslant 0$ le circuit est :
<img src="/terminales-pc/chap-5/chap-5-2-6.png" alt="" width="60%" />
- $u_{AB}(0) = E$ et $u_{DA}(0)=0$.

{{% note warning %}}
Toujours se placer en convention récepteur pour le condensateur !
{{% /note %}}

21. En appliquant la loi des mailles, trouver la relation entre les tensions $u_{DA}$ et $u_{AB}$.
{{% solution "Réponse" %}}
$$u_{DA} + u_{AB} = 0$$
Cette équation fait intervenir deux fonctions inconnues : 
- celle que l'on cherche $u_{AB} (t)$ ;
- la fonction $u_{DA} (t)$.

L'objectif des prochaines questions est de parvenir à exprimer $u_{DA} (t)$ en fonction de $u_{AB} (t)$ de façon à pouvoir résoudre l'équation.
{{% /solution %}}

22. Écrire la relation qui existe entre l'intensité $i(t)$ du courant électrique et la tension $u_{DA}$.
{{% solution "Réponse" %}}
$$u_{DA} = R\\, i$$
{{% /solution %}}

23. Écrire la relation qui existe entre la charge $q_A$ au niveau de l'armature $A$ du condensateur et la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$q_A = C\\, u_{AB} $$
{{% /solution %}}

24. Écrire la relation qui existe entre l'intensité $i$ du courant électrique et la charge $q_A$ au niveau de l'armature $A$ du condensateur.
{{% solution "Réponse" %}}
$$i = \dfrac{\mathrm{d}q_A}{\mathrm{dt}}$$
{{% /solution %}}

25. En déduire la relation qui existe entre l'intensité $i$ du courant électrique et la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$i = C\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$$
{{% /solution %}}

26. En déduire la relation qui existe entre les tensions $u_{DA}$ et $u_{AB}$.
{{% solution "Réponse" %}}
$$u_{DA} = RC\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$$
{{% /solution %}}

27. Écrire à nouveau la loi des mailles de façon à ce qu'elle ne fasse apparaître qu'une seule inconnue, la tension $u_{AB}$.
{{% solution "Réponse" %}}
$$RC\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} + u_{AB} = 0$$
ou
$$\dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} + \dfrac{u_{AB}}{RC} = 0$$

Cette expression est une équation différentielle du premier ordre à coefficients constants.
{{% /solution %}}

#### Solution de l'équation différentielle

On montre, en mathématiques, qu'une famille de solutions de cette équation différentielle est :
$$u_{AB}(t) = A + B e^{-t/\tau}$$
où $A$, $B$ et $\tau$ sont des constantes.

28. Montrer que la famille de solutions donnée vérifie bien l'équation différentielle et en déduire l'expression de $\tau$.
{{% solution "Réponse" %}}
On substitue $u_{AB}$ par la famille de solution dans l'équation différentielle.  

Puisque $\dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}} = \dfrac{\mathrm{d}(A + B e^{-t/\tau})}{\mathrm{dt}} = -\dfrac{B}{\tau} \\, e^{-t/\tau}$ l'équation devient $-\dfrac{B}{\tau} \\, e^{-t/\tau} + \dfrac{A}{RC} + \dfrac{B}{RC} e^{-t/\tau} = 0 \iff \left( -\dfrac{1}{\tau} + \dfrac{1}{RC} \right)\\, B e^{-t/\tau} + \dfrac{A}{RC} = 0$. 

- Le terme à droite de l'égalité, $0$ ne dépend pas du temps. Celui à gauche de cette même égalité ne peut donc pas dépendre du temps. Ceci n'est possible que si $\dfrac{1}{\tau} + \dfrac{1}{RC} = 0 \iff \boxed{\tau = RC}$.

- On en déduit que $\boxed{A = 0}$

Finalement, la famille de solutions convient à la condition qu'elle s'écrive $$\boxed{u_{AB}(t) = B e^{-t/\tau} }$$ avec $\tau = RC$.
{{% /solution %}}

29. À partir des conditions initiales déterminer la fonction solution du problème.
{{% solution "Réponse" %}}
- $u_{AB}(0) = E = B e^{-0/\tau}= B \iff \boxed{B = E}$.

Finalement
$$\boxed{u_{AB}(t) = E e^{-t/\tau} }$$ avec $\tau = RC$.  
On retrouve donc bien le comportement de l'étude expérimentale. En particulier, <strong>la fonction est bien continue</strong> en $t=0$, <strong>positive</strong>, <strong>décroissante</strong> et sa limite à l'infini est $0$.
{{% /solution %}}

30. Déterminer l'expression de la fonction $i(t)$ et donner ses caractéristiques.
{{% solution "Réponse" %}}
- $i(t) = \dfrac{\mathrm{d}q_A}{\mathrm{dt}}$ et $q_A = C\\, u_{AB}$, donc $i(t) = C\\, \dfrac{\mathrm{d}u_{AB}}{\mathrm{dt}}$.

- Si on substitue $u_{AB}$ par son expression, on obtient $i(t) = C\\, \dfrac{\mathrm{d}(E e^{-t / \tau} )}{\mathrm{dt}} = CE\\, \dfrac{\mathrm{d}(e^{-t / \tau} )}{\mathrm{dt}}$, puisque $E$ est une constante, donc $ i(t) = -\dfrac{CE}{\tau}\\, e^{-t / \tau} \iff \boxed{ i(t) = -\dfrac{E}{R}\\, e^{-t / \tau} }$

- À la date $t = O^-$, aucun courant ne circule dans le circuit (puisqu'il est ouvert), donc $i(0^-) = 0$. À la date $t = 0^+$, $i(0^+) = -\dfrac{E}{R} < 0$. L'intensité du courant électrique est une fonction <strong>discontinue</strong> et <strong>négative</strong>.

- $i(t)$ est une <strong>fonction décroissante <em>en valeur absolue</em></strong> qui a pour limite 0 à l'infini.
{{% /solution %}}