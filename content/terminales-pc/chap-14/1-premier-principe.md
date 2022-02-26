---
title: "Premier principe de la thermodynamique"
subtitle: "Chapitre 14,1"
author: ""
type: ""
date: 2021-02-22T05:15:40+04:00
draft: false
toc: true
tags: ["Énergie mécanique", "Énergie interne", "Capacité thermique"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> À maîtriser avant le début de ce cours : Travail, Force conservative, Force non conservative, Énergie potentielle d'interaction, Énergie cinétique, Énergie mécanique.

## À la recherche d'une grandeur énergétique conservative

{{% note tip %}}
Une grandeur caractérisant l'état d'un système est dite **conservative** *si elle reste constante lorsque le **système est isolé**.*
{{% /note %}}

Les grandeurs conservatives sont très importantes en physique, leur
utilisation permet souvent de comprendre simplement l'évolution des
systèmes.

{{% note exercise %}}
Une masse $m$ est mise en mouvement au contact de la Terre. L'expérience
montre que, à cause des frottements solides, la masse finit
immanquablement par s'arrêter après avoir parcouru une distance $d$.
{{% /note %}}

<img src="/terminales-pc/chap-14/chap-14-1/chap-14-1-1.png" alt="" width="80%" />

1. Démontrer que l'énergie mécanique n'est pas une grandeur conservative.
{{% solution "Réponse" %}}
Dans le **référentiel du laboratoire**,
$E_M (t = 0) = \dfrac{1}{2} m\\, v_0^2 + E_{PP}$ et $E_M (t_{\infty}) = E_{PP}$. Donc
$\Delta E_M = E_M (t_{\infty}) - E_M(t = 0) = - \dfrac{1}{2}\\, m\\, v_0^2 < 0$.

*L'énergie mécanique n'est pas conservée bien que le système {masse + Terre} soit isolé, $E_M$ n'est pas une grandeur conservative !*
{{% /solution %}}

2. Donner, après application du théorème de l'énergie cinétique, l'expression de la valeur de la force de frottements solides (force non conservative constante) dans le cas de l'expérience proposée.
{{% solution "Réponse" %}}
$\Delta E_M = E_M (t_{\infty}) - E_M(t = 0) = W(\vec{f}) = \vec{f} \cdot \overrightarrow{AB}$ donc $- \dfrac{1}{2}\\, m\\, v_0^2 = -f \cdot d$ où $d = \Vert \overrightarrow{AB} \Vert$. Finalement 
$$
    f = \dfrac{1}{2}\\, \dfrac{m\\, v_0^2}{d}
$$
{{% /solution %}}

#### Que devient l'énergie mécanique qui disparait lorsque des forces non conservatives travaillent ?

Lorsque l'expérience précédente est réalisée, on constate que *les températures de
la masse $m$ et de la Terre augmentent*. Il est donc nécessaire
d'introduire dans le raisonnement un terme qui prend en compte les
processus qui peuvent intervenir au *niveau microscopique* ; on appelle
cette grandeur l'**énergie interne $U$ du système** (unité : joule).

3. Reprendre le bilan d'énergie de la question 1. en n'utilisant pas l'énergie mécanique $E_M$ du système mais son énergie totale qui a pour expression $E_t = E_M + U$.
{{% solution "Réponse" %}}
Si on note $E_t$ l'énergie totale du système, $U_1$ l'énergie interne de la masse $m$ et $U_2$ l'énergie interne de la Terre,
$E_t (t = 0) = E_M (t = 0) + U_1 (t = 0) + U_2 (t = 0)$ et $E_t (t_{\infty}) = E_M(t_{\infty}) + U_1 (t_{\infty}) + U_2 (t_{\infty})$.\
Donc
$\Delta E_t = \Delta E_M + \Delta U_1 + \Delta U_2 = 0$ (puisque l'ensemble est isolé et que l'énergie se conserve).\
Finalement
$$\Delta U_1 + \Delta U_2 = - \Delta E_M$$ 

*L'énergie mécanique qui a disparu est s'est transformée en énergie interne.*
{{% /solution %}}

{{% note tip %}}
*L'énergie totale d'un système, somme de son énergie mécanique et de son énergie interne, est une **grandeur conservative**.*
$$E_t = E_M + U$$
{{% /note %}}

{{% note normal %}}
L'introduction de l'énergie interne $U$ est nécessaire car *l'énergie mécanique $E_M$ ne prend en compte ni les mouvements internes des atomes et des molécules, ni les forces d'interaction s'exerçant entre ceux-ci (ou celles-ci)*.

Les forces dissipatives (de frottements) correspondent à une **description macroscopiques**. *Au niveau microscopique, il n'existe pas de force dissipative, il n'existe que des forces conservatives*.
{{% /note %}}

## Énergie interne

{{% note tip %}}
L’énergie interne d’un système thermodynamique est l'énergie qu'il renferme.\
Elle est égale à la somme de l’**énergie cinétique de chaque entité élémentaire** de masse non nulle (*agitation thermique*) et de **toutes les énergies potentielles d’interaction des entités élémentaires** de ce système (*liaisons chimiques*, *nucléaires*, *interactions électriques entre molécules (ou ions)*, etc.). En fait, elle correspond à l'énergie intrinsèque du système, définie à l'**échelle microscopique**, à l'*exclusion de l'énergie cinétique ou potentielle d'interaction du système avec son environnement, à l'échelle macroscopique*.

$$U = \sum E_{C,micro} + \sum E_{P,micro}$$

L’énergie interne est une **fonction d'état du système** : *sa variation ne dépend que de l’état final et de l’état initial d’équilibre et non pas de la nature de la transformation.*
{{% /note %}}

Remarque
: Il faut garder à l'esprit que les composants d'un système sont toujours
en mouvement au niveau microscopique, même si le système est macroscopiquement au repos.

Rappel : passage du microscopique au macroscopique
: La grandeur qui relie le monde microscopique au monde macroscopique est
la **constante d'avogadro** :
$$\mathcal{N}_A = \pu{6,02e23 mol-1}$$

{{% note normal %}}
Étant donnée la complexité des interactions au niveau microscopique, l’énergie interne 
$U$ n’est pas calculable et ne peut être connue de façon absolue. *On peut uniquement calculer sa variation*.
{{% /note %}}

## Énergie totale d'un système thermodynamique

{{% note tip %}}
L’énergie totale d'un système peut donc s’écrire :
$$E_t = \sum E_{C,macro} + \sum E_{P,macro} + \sum E_{C,micro} + \sum E_{P,micro}$$
soit
$$ E_t = E_M + U$$
L'énergie totale d'un système est une **grandeur conservative**.
{{% /note %}}

Remarque:
Seules les variations de l'énergie totale d'un système ont un sens physique.

## Comment varie l'énergie totale $E_t$ d'un système lorsqu'il n'est pas isolé ?

### Différents types de transferts d'énergie

{{% note exercise %}}
Un gaz contenu dans un ballon **calorifugé** (voir plus bas), plongé dans un liquide voit son volume réduit au fur et à mesure qu'il s'enfonce car le liquide à l'extérieur exerce une force pressante de plus en plus grande.
{{% /note %}}
<img src="/terminales-pc/chap-14/chap-14-1/chap-14-1-2.png" alt="" width="50%" />

4. Comment appelle-t-on le transfert d'énergie reçu par le gaz ?
{{% solution "Réponse" %}}
Le *point d'application de la force pressante se déplace*, cette dernière transfère donc de l'énergie par **travail** au système.
{{% /solution %}}

{{% note tip %}}
Lorsque le point d'application d'une force qui s'applique sur un système se déplace, de l'énergie est transférée au système (*algébriquement*). Ce type de transfert s'appelle le **travail** ; on le note $W$.
{{% /note %}}

{{% note exercise %}}
Un gaz contenu dans une enceinte rigide est chauffé à l'aide d'une résistance électrique placée dans l'enceinte. Sa température s'élève.
{{% /note %}}

5. Comment appelle-t-on le transfert d'énergie reçu par le gaz ?
{{% solution "Réponse" %}}
L'énergie de ce système varie (la température s'élève) mais *aucune force ne voit son point d'application se déplacer*&nbsp;! On appelle **chaleur** (ou **transfert d'énergie thermique**) le **transfert d'énergie** autre que le travail.
{{% /solution %}}

{{% note tip %}}
On appelle **chaleur** ou **transfert d'énergie thermique**, le transfert d'énergie (algébrique) qui s'effectue sans *déplacement macroscopique* du point d'application d'une force qui agit sur le système. On note $Q$ ce transfert d'énergie.    
**L'origine de ce transfert d'énergie est microscopique** et sera précisée un peu plus tard dans ce chapitre.
{{% /note %}}

{{% note normal %}}
Un système **calorifugé** est un système qui ne peut pas échanger d'énergie sur forme de chaleur avec l'environnement.
{{% /note %}}

### Premier principe de la thermodynamique

<img src="/terminales-pc/chap-14/chap-14-1/chap-14-1-3.png" alt="" width="60%" />

{{% note tip %}}
La *variation d'énergie totale* d'un système est égale à la *somme des travaux des forces non conservatives qui agissent sur lui et de la chaleur* qui lui est transférée.
$$
    \Delta E_t = \Delta E_M + \Delta U = W \left( \text{forces non conservatives} \right) + Q
$$
{{% /note %}}

{{% note tip %}}
Si l'*énergie mécanique du système ne varie pas* (système macroscopiquement immobile, par exemple),
$$
    \Delta U = W \left( \text{forces non conservative} \right) + Q
$$
{{% /note %}}

## Capacité thermique d'un système incompressible

{{% note tip %}}
On appelle *capacité thermique*, l'énergie thermique qu'il faut fournir à un système qui *ne reçoit aucun travail*, dans **des conditions et une température données**, pour élever sa température de 1&nbsp;°C (ou 1K).

Si le **système est incompressible**, 
$$C = \dfrac{\Delta U}{\Delta T}$$ 

*Unité :* Joule par kelvin ou joule par degré celsius, $\pu{J.K-1}$.
{{% /note %}}

{{% note warning %}}
La capacité thermique dépend du corps considéré et de son état physique.
{{% /note %}}

La capacité thermique des solides et des liquides (phases condensées)
dépend assez peu des conditions expérimentales.

{{% note tip %}}
Si on introduit la **capacité thermique massique** $c = C / m$ où $m$
est la masse du système :

$$
    \Delta U = m\\, c\\, \Delta T = m\\, c\\, (T_f - T_i) = W \left( \text{forces non
     conservatives} \right) + Q
$$ 

*Unité de la capacité thermique massique :* joule par kelvin et par kilogramme ($\pu{J.K-1.kg-1}$).
{{% /note %}}

## Transferts thermiques

### Différents transferts thermiques

{{% note tip %}}
Un transfert thermique peut s'effectuer selon plusieurs modes :

Conduction

:   *L'agitation thermique se transmet de proche en proche dans la
    matière, sans que celle-ci se déplace macroscopiquement.*

Convection

:   *L'agitation thermique se transmet de proche en proche dans la
    matière, avec un déplacement d'ensemble de celle-ci.*

Rayonnement

:   *L'absorption ou l'émission d'un rayonnement modifie l'agitation
    thermique. Ce mode de transfert ne nécessité pas la présence d'un
    milieu et peut s'effectuer dans le vide.*

{{% /note %}}


*Les transferts d'énergie d'origine thermique (la chaleur) se font
**spontanément** toujours du corps de température la plus élevée (corps
« chaud ») vers le corps de température la plus basse (corps « froid »)
; jamais dans l'autre sens. L'échange d'énergie est donc
**irréversible**.*


Fondamentalement, cette irréversibilité a pour source le comportement de
la nature à l'échelle microscopique : *le désordre au niveau
microscopique a une tendance naturelle à toujours augmenter, jamais à
diminuer* (si on considère les systèmes dans leur ensemble).

### Flux et résistance thermique

{{% note tip %}}
On appelle **flux thermique** l'énergie thermique transférée à travers une paroi par unité de temps.\
Ce transfert s'effectue toujours depuis le côté de la paroi dont la température est la plus élevée vers le côté de la paroi dont la température est la plus basse.
$$\varphi = \frac{Q}{\Delta t}$$ 

*Unité :* joule par seconde, soit watt.
{{% /note %}}

<img src="/terminales-pc/chap-14/chap-14-1/chap-14-1-4.png" alt="" width="60%" />

{{% note normal %}}
Si les températures $T_1$ et $T_2$ sont **constantes**, on peut montrer (doc. 14,3) que le flux thermique est proportionnel à la différence de ces températures
$\Delta T = T_1 - T_2$ :
$$
    \varphi = \dfrac{\Delta T}{R_{\text{th}}}
$$

$R_{\text{th}}$, par analogie avec l'électrocinétique, est appelée <strong>résistance thermique du matériau</strong> qui constitue la paroi et a pour expression
$$
    R_{\text{th}} = \dfrac{e}{S \lambda}
$$

où $e$ est l'épaisseur de la paroi, $S$ sa surface et $\lambda$ une constante <em>caractéristique du matériau</em>.

<em>Unité de $R_{\text{th}}$ :</em> kelvin seconde par joule, soit kelvin par watt.
{{% /note %}}

{{% note warning %}}
Pour une différence de températures donnée, plus la résistance thermique est grande, plus le flux thermique qui traverse la paroi est petit ; plus le matériau est **bon isolant thermique**.
{{% /note %}}


