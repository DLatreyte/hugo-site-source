---
title: "Énergie stockée dans un barrage"
subtitle: "Chapitre 2,3"
author: ""
type: ""
date: 2021-01-14T08:14:58+04:00
draft: false
toc: true
tags: ["Rendement", "Énergie"]
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> Cette activité permet d’étudier une chaîne énergétique complète en partant de l’eau du barrage pour aller jusqu’à l’appareil électrique, et donc de calculer le rendement global du système. Chaque conversion énergétique entraîne des pertes plus ou moins importantes, les rendements des dispositifs ne sont pas égaux à 1.

## Documents

- {{< remote "Accès aux documents sur le Livre Scolaire" "https://www.lelivrescolaire.fr/page/5413672" >}}

- Quelques ressources supplémentaires (pas indispensables pour répondre aux questions) :
    - Principes des batteries Lithium-Ion :
    {{< youtube "VQyooUrr5B8">}}

    - Usages des batteries au Lithium-Ion
    {{< youtube "n4PzflXG3Rk" >}}

    - Les voitures du futur au Lithium-ion
    {{< youtube "Ln7m3_mquY0" >}}

## Exploitation

1. Déterminer l’énergie nécessaire pour remplir complètement la batterie du smartphone. Convertir cette énergie en joule ($\pu{1 J = 1 W⋅s}$, d’où $\pu{1 W⋅h = 3 600 J}$).
{{% solution "Réponse" %}}
L’énergie nécessaire pour remplir complètement la batterie du smartphone est : $E\_{el} = \pu{11,40 W.h}$ soit $E\_{el} = \pu{11,40 W.h} \times \pu{3 600 J/(W.h)}  = \pu{41,04e3 J} =  \pu{41,04 kJ}$.
{{% /solution %}}

2. Réaliser la chaîne énergétique décrivant le parcours de l’énergie du stockage jusqu’à la batterie.
{{% solution "Réponse" %}}
<img src="/terminales-es/chap-6/chap-6-3/batterie.png" alt="" width="" />
{{% /solution %}}

3. Identifier l’origine des pertes énergétiques lors de la production de l’électricité dans la centrale.
{{% solution "Réponse" %}}
Les pertes énergétiques au niveau de la centrale hydroélectrique viennent de l’alternateur (pertes thermiques) et des frottements de l’eau sur la conduite forcée.
{{% /solution %}}

4. Calculer le rendement de la centrale hydroélectrique.
{{% solution "Réponse" %}}
- Rappel : Rendement 
$$ r = \dfrac{E\_{\text{utile}}}{E\_{\text{fournie}}}  $$

- $r = \dfrac{\pu{2080 MJ}}{\pu{3600 MJ} - \pu{1270 MJ} - \pu{60 MJ}} = \pu{0,92}$\
Il faut penser à ne compter que l’énergie mécanique qui a été réellement fournie à l’alternateur, et donc tenir compte de l’énergie mécanique à la sortie du barrage.
{{% /solution %}}

5. Calculer le rendement global du système, de la production d’électricité jusqu’au stockage dans la batterie.
{{% solution "Réponse" %}}
Pour répondre à cette question, il faut procéder par étapes (on peut aussi appliquer sans comprendre la formule donnée dans le document mais c'est dommage) :

- Énergie fournie par le barrage qui va être transférée sur le réseau électrique : $E\_1 = r\_1 \cdot E\_{\text{fournie}}$ avec $r\_1$ le rendement juste calculé à la question précédente.

- Énergie qui parvient au niveau de la batterie : $E\_2 = r\_2 \cdot E\_1$ où $r\_2$ est le rendement du transport. $r\_2 = \pu{0,94}$ puisqu'il y a 6&nbsp;% de pertes.

- Énergie restituée par la batterie : $E\_3 = r\_3 \cdot E\_2$ où $r\_3$ est le rendement lors du fonctionnement de la batterie. $r\_3 = \pu{0,90}$

Finalement $E\_3 = r\_3 \cdot r\_2 \cdot E\_1$ et $E\_3 = r\_3 \cdot r\_2 \cdot r\_1 \cdot E\_{\text{fournie}}$ donc
$$
    r\_{\text{global}} = \frac{E\_3}{E\_{\text{fournie}}} = r\_3 \cdot r\_2 \cdot r\_1
$$

**A.N.** $r\_{\text{global}} = \pu{0,90} \times \pu{0,94} \times \pu{0,92} =  \pu{0,78}$. Le rendement global est égale à 78&nbsp;%.
{{% /solution %}}

6. Calculer l’énergie prélevée au barrage pour la charge de la batterie.
{{% solution "Réponse" %}}
L’énergie prélevée dans l’eau du barrage pour recharger la batterie est :
$$ E\_{\text{fournie}} = \dfrac{E\_{\text{utile}}}{r\_{\text{global}}}$$

**A.N.** $E\_{\text{fournie}} = \dfrac{\pu{41,04 kJ}}{\pu{0,78}} = \pu{53 kJ}$
{{% /solution %}}
