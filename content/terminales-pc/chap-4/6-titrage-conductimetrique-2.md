---
title: "Titrage conductimétrique d'une solution de sérum physiologique"
subtitle: "Chapitre 5,6"
author: ""
type: ""
date: 2020-10-10T21:32:37+04:00
draft: false
toc: true
tags: ["Tableau d'avancement", "Équivalence", "Conductimétrie", "Titrage", "Conductivité molaire ionique", "Conductivité"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Documents

### Solution physiologique

{{% note normal %}}

Une **solution physiologique** est un *liquide isotonique* au sang, c’est-à-dire exerçant la même pression osmotique sur les membranes cellulaires que les principaux fluides corporels, en particulier le sang humain. Une telle solution est également nommée liquide physiologique ou, improprement, sérum physiologique (en fait il ne s'agit pas d'un sérum car il ne provient pas directement du sang).

La solution est généralement composée d'eau distillée et de chlorure de sodium ($\ce{NaCl}$) dilué à 9 pour $1\\,000$ (c'est-à-dire une solution à 0,9&nbsp;% de masse/volume de $\ce{NaCl}$, soit $\pu{9 g.L-1}$).

Certaines solutions physiologiques d'usage commun sont commercialement disponibles à diverses concentrations à des fins différentes.
<div style="text-align: right;"> 
<a href="https://fr.wikipedia.org/wiki/Solution_physiologique">Wikipedia</a>
</div>

{{% /note %}}

### La méthode de Mohr : un titrage par précipitation

{{% note normal %}}

Lorsqu'on ajoute à une solution contenant des ions chlorure $\ce{ Cl^-(aq) }$ à titrer une solution de nitrate d'argent il se forme un précipité de chlorure d'argent $\ce{ AgCl(s) }$. La solution titrée, incolore au départ, se trouble d'un voile blanc et devient finalement opaque à cause du précipité formé. Ceci se produit jusqu'à ce que tous les ions chlorures aient précipité. *On est alors à l'équivalence* du titrage.    
*Malheureusement, il est impossible de visualiser directement cette équivalence puisque le précipité de chlorure d'argent est présent depuis le début*.
    
On peut utiliser  un **indicateur coloré** de présence d'ions argent pour déterminer l'*instant de l'arrêt de leur consommation* : le *chromate de potassium*. Les ions argent en présence d'ions chromate forment un précipité rouge de chromate d'argent $\ce{ Ag2CrO4(s) }$. Ce précipité est moins stable que le précipité de chlorure d'argent donc *si l'argent est en présence d'ions chlorure et d'ions chromate, il réagit d'abord avec les ions chlorure puis, après, avec les ions chromate*.

Au cours du dosage, tous les ions $\ce{ Ag^+(aq) }$ réagissent avec les ions chlorure $\ce{ Cl^-(aq) }$ jusqu'au point d'équivalence. Dès l'équivalence franchie, les ions $\ce{ Ag^+(aq) }$ sont en excès et réagissent avec l'ion chromate pour former le précipité rouge. Une lecture du volume au point d'équivalence permet alors de déterminer la concentration en ions chlorure de la solution.

{{% /note %}}


### Équivalence d'un titrage

{{% note tip %}}
- On appelle **équivalence** d'un titrage le *point du titrage où on change de réactif limitant*.
- À l'**équivalence** les *réactifs ont été introduits dans les proportions stœchiométriques*.
{{% /note %}}

## Objectif

> L'objectif de cette séance est de vérifier que l'information sur la concentration massique en chlorure de sodium de sérum physologique annoncée sur Wikipedia est correcte.

## Partie expérimentale

### Données : conductivités molaires ioniques

$\lambda_{\ce{Na^+}} = \pu{5,0e-3 S.m2.mol-1}$ ; $\lambda_{\ce{Cl^-}} = \pu{7,6e-3 S.m2.mol-1}$ ; $\lambda_{\ce{Ag^+}} = \pu{6,2e-3 S.m2.mol-1}$ ; $\lambda_{\ce{NO^-_{3}}} = \pu{7,1e-3 S.m2.mol-1}$.

### Matériel à disposition

<img src="/terminales-pc/chap-4/chap-4-6-1.jpg" alt="" width="55%" style="float: right; padding-left: 15px;" />

- Sérum physiologique de concentration $C$ en chlorure de sodium **dilué 10 fois**. On prélève $V=\pu{10 mL}$ de ce sérum dilué 10 fois&nbsp;; 

- Solution de nitrate d’argent $\ce{ Ag^+(aq) + NO^-_3(aq) }$ de concentration $C_2 = \pu{2,0e-2 mol.L-1}$&nbsp;; 

- Indicateur de fin de réaction : solution jaune de chromate de potassium $\ce{2 K^+(aq) + CrO^2-_4(aq) }$ (**Nous n'avons malheureusement pas ce produit à disposition, cette partie du TP ne sera pas réalisée**)&nbsp;; 

- Conductimètre et sonde, agitateur et barreau aimanté, burette graduée $\pu{25 mL}$, pipette jaugée $\pu{10 mL}$ et propipette, éprouvette graduée, béchers, erlenmeyer, eau distillée.

### Protocole

- Rédiger un protocole permettant de mettre en œuvre simultanément la méthode de Mohr et de réaliser un suivi conductimétrique du titrage.
- Mettre en œuvre le protocole.

#### Tableau de valeurs envisageable

<center>

| $V_B$ (mL) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\sigma\\, (\pu{mS.m2.mol-1})$ | .... | .... | .... | .... | .... | .... | .... | .... | .... | 


| $V_B$ (mL) | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\sigma\\, (\pu{mS.m2.mol-1})$ |.... | .... | .... | .... | .... | .... | .... | .... |

</center>

{{% solution "Résultats expérimentaux possibles" %}}

<center>

| $V_B$ (mL) | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\sigma\\, (\pu{mS.m2.mol-1})$ | 0,15 | 0,149 | 0,148 | 0,147 | 0,146 | 0,145 | 0,143 | 0,142 | 0,141 | 


| $V_B$ (mL) | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $\sigma\\, (\pu{mS.m2.mol-1})$ | 0,159 | 0,177 | 0,193 | 0,209 | 0,228 | 0,245 | 0,261 | 0,277 |

</center>

{{% /solution %}}


## Exploitation

1. Écrire l'équation de la réaction de titrage.
{{% solution "Réponse" %}}
- Les ions argent $\ce{Ag+}$ constituent le titrant ;
- Les ions chlorure $\ce{Cl-}$ sont titrés.
$$
    \ce{Ag+ (aq) + Cl- (aq) -> AgCl (s)}
$$
{{% /solution %}}

2. Quelles propriétés doit présenter une réaction chimique utilisée pour réaliser un titrage&nbsp;?
{{% solution "Réponse" %}}
{{% note tip %}}
Une réaction chimique utilisée pour réaliser un titrage doit&nbsp;:
- être **rapide**&nbsp;;
- être **unique** dans le milieu réactionnel (c'est la seule qui doit consommer les titré et titrant)&nbsp;;
- doit modéliser des **transformations chimiques totales**.
{{% /note %}}
{{% /solution %}}

3. Pourquoi la conductivité de la solution n'est-elle pas nulle au début du titrage&nbsp;?
{{% solution "Réponse" %}}
Lorsque le volume d'ions argent versé est nul, la solution est formée d'eau et contient des ions sodium $\ce{Na+}$ et chlorure $\ce{Cl-}$ capables de conduire le courant électrique. La conductivité de cette solution est donc non nulle.
{{% /solution %}}

4. Donner, de façon qualitative, la composition du bécher&nbsp;:
    - avant l'équivalence&nbsp;;
    - à l'équivalence&nbsp;;
    - après l'équivalence.
{{% solution "Réponse" %}}
- **Avant l'équivalence**     
Le titrant (les ions argent $\ce{Ag+}$), est limitant. La solution contient donc de l'eau, le titré (les ions chlorure $\ce{Cl-}$), des ions sodium $\ce{Na+}$, des ions nitrate $\ce{NO3-}$ (introduits en même temps que les ions argent) et du chlorure d'argent $\ce{AgCl}$ (produit de la réaction).

- **À l'équivalence**    
Le titrant (les ions argent $\ce{Ag+}$) et le titré (les ions chlorure $\ce{Cl-}$) sont limitants. La solution contient des ions sodium $\ce{Na+}$, des ions nitrate $\ce{NO3-}$ (introduits en même temps que les ions argent) et du chlorure d'argent $\ce{AgCl}$ (produit de la réaction).

- **Après l'équivalence**    
Le titrant (les ions argent $\ce{Ag+}$) est désormais en excès et le titré (les ions chlorure $\ce{Cl-}$) ont disparu. La solution contient des ions argent $\ce{Ag+}$, des ions sodium $\ce{Na+}$, des ions nitrate $\ce{NO3-}$ (introduits en même temps que les ions argent) et du chlorure d'argent $\ce{AgCl}$ (produit de la réaction).
{{% /solution %}}

5. Établir un tableau d'avancement pour chacune des phases décrites ci-dessus.
{{% solution "Réponse" %}}

| État | Avancement | $\ce{Ag+ (aq)}$ | $+$ | $\ce{Cl- (aq)}$ | $\ce{->}$ | $\ce{AgCl}$ |Spectateurs| $\ce{Na+}$ | $\ce{NO3-}$ |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---:| :---: | :---: |
| Initial | 0 | $n_0$ |  | $n_1$ |  | 0 | | $n_1$ | $n_0$ |
| Avant l'équivalence | $x_{av} = n_0$ | 0 |  | $n_1 - n_0$ |  | $n_0$ | | $n_1$ | $n_0$ |
| À l'équivalence | $x_E = n_1 = n_0$ | 0 |  | 0 |  | $n_1 = n_0$ | | $n_1$ | $n_0$ |
| Après l'équivalence | $x_{ap} = n_1$ | $n_0 - n_1$ |  | 0 |  | $n_1$ | | $n_1$ | $n_0$ |

{{% /solution %}}

6. À partir des tableaux d'avancement écrire les expressions des conductivités $\sigma$ de la solution en fonction des concentrations molaires des différentes entités chimiques&nbsp;:
- avant l'équivalence&nbsp;;
- à l'équivalence&nbsp;;
- après l'équivalence.
{{% solution "Réponse" %}}

{{% /solution %}}

7. Justifier l'allure de la courbe $\sigma = f(V_B)$.
{{% solution "Réponse" %}}

{{% /solution %}}

8. En déduire la concentration en ions chlorure dans le sérum physiologique.
{{% solution "Réponse" %}}

{{% /solution %}}