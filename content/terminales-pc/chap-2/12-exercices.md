---
title: "Exercices et Annale"
subtitle: "Chapitre 3,3,4"
author: ""
type: ""
date: 2020-09-28T12:01:30+04:00
draft: false
toc: true
tags: ["Différence de marche", "Superposition", "Période temporelle", "Longueur d'onde", "Retard", "Déphasage", "Ondes", "Interférences", "Doppler"]
categories: ["Physique", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Livre scolaire
- {{< remote "32, 34, 33 pages 509 et 510" "https://www.lelivrescolaire.fr/page/16301719" >}}

{{% solution "Solutions" %}}
{{< remote "Fichier au format pdf" "/terminales-pc/chap-2/chap-2-12-1-bis.pdf" >}}
{{% /solution %}}

## Annale
- {{< remote "Autour du papillon" "/terminales-pc/chap-2/chap-2-12-2.pdf" >}}

*Ne pas traiter les première et deuxième partie (seulement la partie 3).*

- {{< remote "D'où viennent les couleurs des ailes des papillons ?" "https://youtu.be/yriopuT98ZU" >}}

{{% solution "Correction de l'annale" %}}
**1.1.1.** Les chauve-souris émettent des ondes dont la fréquence est $f_e = \pu{50 kHz}$. L'homme peut entendre les sons dont les fréquences sont comprises entre $\pu{20 Hz}$ et $\pu{20 kHz}$. Les chauve-souris émettent donc des sons situés dans le domaine des ultra-sons.

**1.1.2.** Les ondes sonores sont la propagation de la « déformation » de l'air. Elle nécessitent donc un milieu matériel pour se déplacer : ce sont des ondes mécaniques.

**1.1.3.** Les ondes sonores sont des ondes de compression : le milieu est déformé selon la même direction que la direction de propagation de l'onde.   
Les ondes sonores sont des ondes longitudinales.

**1.2.1.** $f_r = f_e \\, \dfrac{v_{\text{onde}}}{v_{\text{onde}} - v_{\text{émetteur}}}$ donc $f_r = f_e \\, \dfrac{1}{1 - \dfrac { v_{\text{émetteur}} }{ v_{\text{onde}} }} \Leftrightarrow 1 - \dfrac { v_{\text{émetteur}} }{ v_{\text{onde}} } = \dfrac{f_e}{f_r}\Leftrightarrow \dfrac { v_{\text{émetteur}} }{ v_{\text{onde}} } = 1 - \dfrac{f_e}{f_r} \Leftrightarrow v_{\text{émetteur}} = v_{\text{onde}} \left( 1 - \dfrac{f_e}{f_r} \right)$.

**A.N.** $ v_{\text{émetteur}} = \pu{340 m.s-1} \times \left(1 - \dfrac{ \pu{50,0 kHz} }{ \pu{50,8 kHz} } \right) = \pu{5,35 m.s-1} = \pu{19,3 km.h-1} $.

**1.2.2.** $ \dfrac{v_{\text{onde}}}{v_{\text{émetteur}}} = \dfrac{ \pu{340 m.s-1} }{ \pu{5,35 m.s-1} } = \pu{ 63,6 } $ La célérité de l'onde est donc plus de 63 fois plus grande que celle de l'émetteur.  
Ce point est très important car l'objectif de la chauve-souris est la localisation des obstacles ou des proies. Si elle a le temps de parcourir une grande distance entre le moment où l'onde est émise et celui où elle est reçue, cette localisation serait très imprécise (puisque ce qu'elle déterminer c'est la distance à l'obstacle)... dans le pire scénario, on peut même imaginer que la chauve-souris entre en contact avec l'obstacle avant d'avoir appris qu'il existe.

**1.3.** Pendant la durée $\tau$ l'onde parcourt le trajet chauve-souris - proie, proie - chauve-souris, soit la distance $2d$ si on note $d$ la distance initiale chauve-souris - proie.

**Important.** On fait ici l'hypothèse que la chauve-souris ne s'est pratiquement pas déplacée pendant la durée $\tau$. En fait, l'énoncé aurait du être beaucoup plus précis à ce sujet !

La distance $2d$ est parcourue à la célérité $v_{\text{onde}}$ par l'onde, donc $2d = v_{\text{onde}} \\, \tau \Leftrightarrow d = \dfrac{v_{\text{onde}} \\, \tau}{2}$.

**A.N.** $d = \dfrac{ \pu{340 m.s-1} \times \pu{16,7e-3 s} }{2} = \pu{2,8 m}$.

**Et sans l'hypothèse absente de l'énoncé ?** Pendant la durée $\tau$ l'onde parcourt la distance $d + (d - v_{\text{émetteur}}\\, \tau)$ (si la chauve-souris se déplace directement vers la proie), donc $2d - v_{\text{émetteur}}\\, \tau = v_{\text{onde}} \\, \tau \Leftrightarrow d = \dfrac{1}{2}\\, ( v_{\text{émetteur}} + v_{\text{onde}} ) \tau $.

**A.N.** $d = \dfrac{1}{2} \times (\pu{5,35 m.s-1} + \pu{340 m.s-1}) \times \pu{16,7e-3 s} = \pu{ 2,9 m } $.

**3.1.** 
- Pour que les interférences soient constructives, il faut que les ondes arrivent en phase dans l'œil de l'observateur. Le retard doit donc être tel que $\tau = 0 + k T = k T$ avec $k$ un entier.
- Pour que les interférences soient destructives, il faut que les ondes arrivent en opposition de phase dans l'œil de l'observateur. Le retard doit donc être tel que $\tau = \dfrac{T}{2} + k T = (k + \dfrac{1}{2}) T$ avec $k$ un entier.

**3.2.1.** Lorsque l'incidence est normale, $\tau = \dfrac{2ne}{c} + \dfrac{T}{2}$. Or on sait que les interférences sont constructives si $\tau = k T$, donc $\dfrac{2ne}{c} + \dfrac{T}{2} = k T \Leftrightarrow \dfrac{2ne}{c} = (2k -1) \dfrac{T}{2} \Leftrightarrow T = \dfrac{4 n e}{(2k - 1) c}$.   
Comme $T = \dfrac{\lambda}{c}$, la relation précédente s'écrit $\dfrac{\lambda}{c} = \dfrac{4 n e}{(2k - 1) c}  \Leftrightarrow \lambda = \dfrac{4 n e}{(2k - 1)}$

- Pour $k = 0$, on obtient une longueur d'onde négative, ce qui est impossible.
- Pour $k = 1$, $\lambda = \dfrac{ 4\times \pu{1,5} \times \pu{100e-9 m} }{ 2 \times 1 - 1 } = \pu{6,0e-7 m} = \pu{6,0e2 nm}$.
- Pour $k = 2$, $\lambda = \dfrac{ 4\times \pu{1,5} \times \pu{100e-9 m} }{ 2 \times 2 - 1 } = \pu{2,0e-7 m} = \pu{2,0e2 nm}$.
- Ce n'est pas la peine de poursuivre puisqu'on n'est déjà plus dans le domaine du visible.

**3.2.2.** La radiation de longueur d'onde $\lambda = \pu{6,0e2 nm}$ se situe dans l'orange.

**3.3.** Le raisonnement mis en œuvre à la question 3.2.1 donne, pour expression de la longueur d'onde, $ \lambda = \dfrac{4 n e \cos (\theta )}{(2k - 1)}$. On constate que la longueur d'onde du rayonnement qui interfère constructivement dépend de l'angle $\theta$ sous lequel on regarde l'aile.  
La couleur de l'aile varie donc en fonction de l'angle $\theta$ sous lequel on la regarde.

{{% /solution %}}