---
title: "Annale : Condensateur d'un flash"
subtitle: "Chapitre 6,6"
author: ""
type: ""
date: 2020-11-07T14:18:10+04:00
draft: false
toc: true
tags: ["Annale", "Courant électrique", "Tension", "Potentiel électrique", "Générateur", "Dipôle", "Branche", "Maille", "Nœud", "Loi des nœuds", "Loi des mailles", "Loi d'Ohm", "Résistance","Condensateur", "Équation différentielle linéaire à coefficients constants"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

On se propose d'étudier le fonctionnement d'un flash d'appareil photographique jetable. Pour obtenir un éclair de puissance lumineuse suffisante, on utilise un tube flash qui nécessite pour son amorçage, une forte tension (au moins $\pu{250 V}$) pour émettre un éclair très bref. Pour stocker l'énergie nécessaire au fonctionnement du tube flash, on utilise un condensateur de capacité $C$. Ce condensateur est chargé à l'aide d'un circuit électronique alimenté par une pile.

On schématise le fonctionnement de ce dispositif sur le schéma ci-dessous :
- l'alimentation est assurée par une pile de tension continue $U_1 = \pu{1,50 V}$&nbsp;;
- un circuit électronique permettant d'élever la tension $U_1$ à une tension continue $U_2 = \pu{300 V}$&nbsp;;
- un conducteur ohmique de résistance $R = \pu{1,00 k\Omega}$ permettant la charge du condensateur de capacité $C = \pu{150 \mu F}$ en plaçant l'interrupteur $K_2$ en position 1 et en fermant l'interrupteur $K_1$&nbsp;;
- le tube flash qui est déclenché (une fois le condensateur chargé) en basculant l'interrupteur $K_2$ en position 2.

<img src="/terminales-pc/chap-5/chap-5-6-1.pdf" alt="" width="100%" />

**Remarque.** Énergie électrique stockée par un condensateur&nbsp;: $E_{el} = \dfrac{C u^2}{2} = \dfrac{q^2}{2C}$ si on note $u$ la tension électrique aux bornes du condensateur et $q$ la charge sur l'armature positive du condensateur. 

## Charge du condensateur

On charge le condensateur en fermant l'interrupteur $K_1$.

1. On donne l'expression de la constante de temps $\tau = RC$. Vérifier par analyse dimensionnelle l'homogénéité de cette formule.
2. Calculer numériquement $\tau$. 
3. Calculer l'énergie emmagasinée $E_{el}$ par le condensateur de capacité $C$ une fois la charge terminée à la tension $U_2$.
4. En calculant l'énergie $E_{el}\rq$ qu'aurait stockée le condensateur s'il avait été chargé directement à l'aide de la pile (tension $U_1$), justifier l'intérêt de charger le condensateur avec une haute tension de 300&nbsp;V.

## Décharge du condensateur
En plaçant l'interrupteur inverseur $K_2$ sur la position 2 on provoque le flash grâce à la restitution de l'énergie stockée dans le condensateur.    
On enregistre la tension $u$ aux bornes du condensateur $C$ (voir graphique en annexe).

5. Déterminer graphiquement la constante de temps $\tau'$ correspondant à la décharge en précisant la méthode employée (l'annexe complétée sera rendu avec la copie). 
6. Comparer les constantes de charge $\tau$ et de décharge $\tau'$. Ce constat est-il en accord avec les conditions de fonctionnement du tube flash&nbsp;? 

<img src="/terminales-pc/chap-5/chap-5-6-2.pdf" alt="" width="40%" style="float: right;"/>

7. On assimilera, après son amorçage, le tube flash à un conducteur ohmique de résistance $r$. À partir du schéma électrique ci-contre montrer que l'équation différentielle de la décharge du condensateur à travers un conducteur ohmique de résistance r est de la forme&nbsp;: 
$$\dfrac{\mathrm{d}u}{\mathrm{dt}} + \dfrac{1}{rC} u = 0 $$

8. Vérifier que la solution est de la forme $u = U_0\\, e^{-t / \tau'}$.
9. Que représente la tension $U_0$ pour le fonctionnement du tube flash&nbsp;? 
10. Déterminer $U_0$. Cette valeur est-elle en accord avec la production de l'éclair&nbsp;?

## Annexe

<img src="/terminales-pc/chap-5/chap-5-6-3.pdf" alt="" width="100%"/>


## Corrigé

{{< remote "Corrigé au format pdf" "/terminales-pc/chap-5/chap-5-6-4.pdf" >}}




