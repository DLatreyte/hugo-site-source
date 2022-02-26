---
title: "Comment fonctionne un alternateur ?"
subtitle: "Chapitre 1,2"
author: ""
type: ""
date: 2020-11-25T19:02:34+04:00
draft: false
toc: true
tags: ["Alternateur", "Rotor", "Stator", "Induction", "Fréquence", "Champ magnétique","Courant électrique"]
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Première approche de la production de l'électricité

{{< youtube "LCIU6yZmCSk" >}}

1. Qu'est-ce que le courant électrique ?
{{% solution "Réponse" %}}
Le courant électrique est un mouvement d'ensemble de charges électriques.
{{% /solution %}}

2. Comment appelle-t-on le phénomène physique au cours duquel un courant électrique dans un conducteur est induit par le mouvement d'un aimant ?
{{% solution "Réponse" %}}
Ce phénomène est l'induction magnétique. Il intervient plus généralement chaque fois qu'un conducteur se trouve dans une zone dans laquelle le champ magnétique varie :
- Conducteur mobile dans un champ magnétique indépendant du temps (stationnaire) mais inhomogène dans l'espace ;
- Conducteur fixe dans un champ magnétique qui varie dans le temps.
{{% /solution %}}

3. Combien de parties retrouve-t-on dans un alternateur ?
{{% solution "Réponse" %}}
Deux parties : aimant qui tourne et bobines (enroulements de fils électriques) fixes.
{{% /solution %}}

4. La production d'électricité dépend-elle finalement des différentes sources d'énergies utilisées (gaz, charbon, pétrole, noyaux, etc.) ?
{{% solution "Réponse" %}}
- La production d'électricité est en fait identique dans tous ces cas : on fait tourner un axe auquel est attaché aimant de façon à produire un champ magnétique variable afin d'induire un courant électrique dans les bobines électriques placées autour.
{{% /solution %}}


## Fonctionnement (trop) détaillé d'un alternateur

{{< youtube "8d5g-_6-LG8" >}}

5. Quelles sont les deux situations présentées qui permettent de réaliser le phénomène d'induction ?
{{% solution "Réponse" %}}
- Bobine (enroulement de fils conducteurs) mobile dans un champ magnétique constant ;
- Champ magnétique variable et bobine fixe. 
{{% /solution %}}

6. Quelle situation est retenue lors de la conception d'un alternateur ?
{{% solution "Réponse" %}}
- Champ magnétique variable et bobine fixe. 
{{% /solution %}}

7. Les deux parties principales d'un alternateur sont le **rotor** et le **stator**. Dire à quoi elles correspondent.
{{% solution "Réponse" %}}
- *Partie mobile qui produit le champ magnétique variable* : **rotor**.
- *Partie fixe constituée des bobines électriques* : **stator**.
{{% /solution %}}

8. Un alternateur utilise-t-il réellement un aimant au niveau du rotor, comme présenté dans la première vidéo ?
{{% solution "Réponse" %}}
Utiliser des aimants est très peu pratique : 
- ils sont généralement lourds ; il faut donc beaucoup d'énergie pour les mettre en mouvement et d'importantes contraintes mécaniques existent.
- *il est impossible de faire varier l'intensité du champ magnétique* si le besoin se fait sentir.

On génère donc le champ magnétique variable en faisant circuler un courant électrique continu dans des bobines fixées au rotor.
{{% /solution %}}

9. De quoi dépend la fréquence du courant électrique induit ?
{{% solution "Réponse" %}}
La fréquence du courant électrique induit dépend du **nombre de pôles sur le rotor** et de la **vitesse de rotation** de ce dernier.
{{% /solution %}}

10. Combien de fois par minute se reproduit un phénomène périodique de fréquence $f=\pu{60 Hz}$ ?
{{% solution "Réponse" %}}
La fréquence d'un phénomène périodique est le nombre de fois qu'il se répète identique à lui-même chaque seconde, donc $f=\pu{60 Hz} = \pu{60 s-1}$. On en déduit donc que $N = \pu{60 s-1} \times \pu{60 s} = \pu{3600}$. Le phénomène se produit 3600 fois par minute.
{{% /solution %}}

11. Comment produit-t-on le courant électrique continu nécessaire à la génération du champ magnétique créé par les bobines attachées au rotor ?
{{% solution "Réponse" %}}
On utilise une source de courant continu externe ou un générateur alimenté par le même axe en rotation.
{{% /solution %}}

## Rendement d'un alternateur

- {{< remote "Activité du Livre Scolaire" "https://www.lelivrescolaire.fr/page/82784" >}}

12. Calculer la puissance $P_f$ fournie par l’eau à un turbo-alternateur du barrage des Trois-Gorges. En déduire le rendement $r$ du turbo-alternateur. 
{{% solution "Réponse" %}}
- $P_f = h \cdot d \cdot \rho \cdot g$ donc $P_f = \pu{80,6 m} \times \pu{1065 m3.s-1} \times \pu{1,0e3 kg.m-3} \times \pu{9,81 m.s-2} = \pu{8,4e8 W}$.
- Rendement : $r = \dfrac{P_u}{P_f}$ donc $r = \dfrac{\pu{710e6 W}}{\pu{8,4e8 W}} = \pu{0,84}$. Le rendement est donc de 84&nbsp;%.
{{% /solution %}}

13. Proposer une explication à la différence entre la valeur du rendement calculée et celle annoncée.
{{% solution "Réponse" %}}
Lors de sa chute l'eau est soumise à des frottements, toute son énergie potentielle de pesanteur n'est donc pas convertie en énergie cinétique. La valeur calculée de $P_f$ est donc trop optimiste.
{{% /solution %}}

14. La puissance délivrée par le second plus puissant barrage du monde, à Itaipu, est de 14&nbsp;GW. Vérifier par le calcul que la puissance totale délivrée par le barrage des Trois-Gorges est environ une fois et demie supérieure. 
{{% solution "Réponse" %}}
- Le barrage des Trois-Gorges est constitué de 32 turbo-alternateurs, la puissance totale délivrée est donc $P_t = 32 \times \pu{710e6 W} = \pu{22,7e9 W} = \pu{22,7 GW}$.
- $\dfrac{\pu{22,7 GW}}{\pu{14 GW}} = \pu{1,6}$ La puissance délivrée par le barrage des Trois-Gorges est 1,6 fois plus grande que celle délivrée par le barrage à Itaipu.
{{% /solution %}}