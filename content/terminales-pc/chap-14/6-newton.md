---
title: "Transferts thermiques : comment modéliser l'évolution de la température d'un solide ?"
subtitle: ""
author: ""
type: ""
date: 2022-04-10T18:20:41+04:00
draft: false
toc: true
tags: ["Loi de Newton", "Transfert thermique"]
categories: ["Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: false
---

## Objectif

> Chacun sait qu’il vaut mieux éviter de laisser la cuillère dans une casserole lorsque l’on prépare une sauce, un potage ou de la confiture ! Cependant, on peut, sans risque de se brûler, utiliser une cuillère sortie du tiroir, mais pour **combien de temps**&nbsp;? Et si vous aviez le choix, prendriez-vous la vieille cuillère en argent de la grand-mère ou un autre matériau&nbsp;?

> Dans ce document, on lie donc les notions de «&nbsp;transfert thermique&nbsp;» et de «&nbsp;temps&nbsp;».

## Modélisation

Pour simplifier le problème on supposera que la cuillère est faite dans un matériau homogène, et que sa température est la même en chacun de ses points. Avec la vieille cuillère en argent, un matériau bien conducteur, nous sommes assez proche de cette situation. Nous supposerons également que le liquide a atteint sa température maximale, qui se situe le plus souvent aux environs de $T_1 = \pu{100°C}$. Le volume de liquide étant supposé important, *l’introduction de la cuillère ne modifiera pas la température du liquide*, et cette dernière sera supposée constante tout au long de l’expérience, comme dans un «&nbsp;thermostat&nbsp;».

{{% note tip %}}

#### Loi phénoménologique de Newton

Les transferts thermiques entre un corps et le milieu extérieur suivent la loi de Newton si la puissance thermique (ou flux) est proportionnelle d’une part à la surface d’échange et d’autre part à l’écart de température entre le matériau (et plus précisément sa surface) et l’extérieur.

**Remarque :** il est difficile d’obtenir une valeur précise du coefficient de proportionnalité, noté souvent $h$, et appelé **coefficient de transfert de Newton**, car il dépend fortement du milieu (nature, mouvement du liquide, température ...).

{{% /note %}}

{{% note normal %}}

#### Données

- Masse de la cuillère en argent : $\pu{70 g}$&nbsp;;
- Surface de la cuillère : $S = \pu{90 cm2}$&nbsp;;
- Capacité thermique massique de l’argent : $c_{Ag} = \pu{235 J·kg-1·K-1}$&nbsp;;
- Valeurs approximatives des coefficients de Newton pour un transfert conducto-convectif dans l’eau chaude : $h = \pu{3000 W.m-2·K−1}$, et dans l’air : $h = \pu{10 W.m-2·K−1}$&nbsp;;
- Température initiale de la cuillière : $T_0 = \pu{21 °C}$&nbsp;;
- Loi de Newton : $\varphi = hS(T^{ext} - T)$. $\varphi$ est une grandeur algébrique.

{{% /note %}}

- <a href="https://phychim.ac-versailles.fr/IMG/pdf/1-ener-transfert-e_volution-de-t-rectificatif.pdf" target="_blank"> Document de référence pour l'élaboration de cette séance </a>

## Travail à réaliser

1. Faire un schéma de la situation, en définissant le système.
{{% solution "Réponse" %}}

- Système = {cuillère}
- Milieu extérieur = {eau chaude}

{{% /solution %}}

2. Préciser le sens du transfert thermique entre le système et le liquide.
En déduire le signe de $\varphi$ donné par l'expression de la loi de Newton.
{{% solution "Réponse" %}}

- La température du milieu extérieur est supérieure à la température du système. L'énergie thermique s'écoule donc du milieu extérieur vers le système.
- La relation de Newton conduit à $\varphi > 0$, la puissance thermique est *effectivement reçue par le système*.

{{% /solution %}}

3. Écrire la relation donnée par le premier principe de la thermodynamique appliqué au système.
Cette relation doit faire apparaître $m$, $c$, $T$ et $Q$.
{{% solution "Réponse" %}}

- Le premier principe de la thermodynamique s'écrit :
$$
\Delta E_{tot} = \Delta E_M + \Delta U = Q + W
$$
avec $E_M$ l'énergie mécanique et $U$ l'énergie interne du système, $Q$ l'énergie échangée par transfert thermique et $W$ l'énergie échangée par travail.

- Comme le système est immobile et que ses interactions macroscopiques avec l'environnement ne varient pas,
$$
\Delta E_M = 0
$$
- Comme aucune force s'appliquant sur le système ne voit son point d'application se déplacer dans l'espace,
$$
W = 0
$$
- Finalement,
$$
\Delta U = Q
$$
- Comme $\Delta U = m c\\, \Delta T$,
$$
m c\\, \Delta T = Q
$$

{{% /solution %}}

4. Dériver la relation de la question 3. par rapport au temps.
{{% solution "Réponse" %}}

**Remarque :** afin de bien comprendre le processus, il est préférable de revenir à la définition de la dérivation.

- Puisque la température est une grandeur qui dépend du temps, la relation obtenue à la question précédente peut s'écrire
$$
m c\\, \Delta T = Q \iff mc\\, \left( T(t+ \Delta t) - T(t) \right) = Q
$$
- Si on divise le tout par $\Delta t$, on obtient
$$
mc\\, \dfrac{T(t+ \Delta t) - T(t)}{\Delta t} = \dfrac{Q}{\Delta t}
$$

- La température $T$ est supposée continue (hypothèse raisonnable). Il est donc possible de passer à la limite,  
$$
mc\\, \lim\limits_{\Delta t \to 0} \dfrac{T(t+ \Delta t) - T(t)}{\Delta t} = \lim\limits_{\Delta t \to 0} \dfrac{Q}{\Delta t}
$$
ce qui s'écrit
$$
mc\\, \dfrac{\mathrm{d}T}{dt} = \dfrac{\mathrm{d}Q}{dt}
$$

{{% /solution %}}

5. Donner la relation qui **définit** la puissance thermique $\varphi$ échangée par le système avec l'extérieur.
Quelle est son unité ?
{{% solution "Réponse" %}}

- $\varphi = \dfrac{\mathrm{d}Q}{dt}$
- **Unité :** $\pu{J.s-1} = \pu{W}$

{{% /solution %}}

6. Introduire la puissance thermique dans la relation de la question 4, puis son expression trouvée à la question 2.
Comment appelle-t-on la relation finale obtenue.
{{% solution "Réponse" %}}

$$
mc\\, \dfrac{\mathrm{d}T}{dt} = \varphi \iff
mc\\, \dfrac{\mathrm{d}T}{dt} = hS(T_1 - T)
$$
On peut aussi écrire cette relation
$$
\dfrac{\mathrm{d}T}{dt} + \dfrac{hS}{mc} T = \dfrac{hS}{mc} T_1
$$
Il s'agit d'une équation différentielle linéaire du premier ordre à coefficients constants. Cette équation différentielle comporte un second membre.

{{% /solution %}}

7. La famille de solutions de l'équation précédente est
$$
T = A e^{- \dfrac{t}{\tau}} + B
$$
Déterminer l'expression de la solution au problème, c'est à dire les expressions des paramètres $A$, $B$ et $\tau$.
{{% solution "Réponse" %}}

1. *La famille de solutions doit vérifier l'équation différentielle*

$$
\dfrac{\mathrm{d}T}{dt} = - \dfrac{A}{\tau} e^{- \dfrac{t}{\tau}}$$
donc lorsqu'on injecte cette dernière expression dans l'équation différentielle, on obtient
$$- \dfrac{A}{\tau} e^{- \dfrac{t}{\tau}} + \dfrac{hS}{mc} \left( A e^{- \dfrac{t}{\tau}} + B \right) = \dfrac{hS}{mc} T_1 $$
ou
$$
A \left( - \dfrac{1}{\tau} + \dfrac{hS}{mc} \right) e^{- \dfrac{t}{\tau}} + \dfrac{hS}{mc} ( B - T_1) = 0
$$

- La partie faisant intervenir l'exponentielle doit forcément être nulle puisque ce terme ne peut pas dépendre du temps. La seule solution acceptable est
$$
\tau = \dfrac{mc}{hS}
$$

- La seconde partie est aussi forcément nulle. On a donc
$$
B = T_1
$$

La famille de solution convient si on écrit
$$
T = A e^{- \dfrac{t}{\tau}} + T_1
$$
avec $\tau = \dfrac{mc}{hS}$.

2. *La solution vérifie toutes les solutions particulières* (comme la condition initiale)

$$
T(0) = T_0 = A e^{- \dfrac{0}{\tau}} + T_1 \iff T_0 = A + T_1
$$
Finalement
$$
A = T_0 - T_1
$$

3. *Solution*
$$
T = (T_0 - T_1) e^{- \dfrac{t}{\tau}} + T_1
$$
La température tend bien asymptotiquement vers $T_1$ pour $t \to \infty$. La température finale de la cuillère est celle de l'eau chaude.
{{% /solution %}}

8. Donner la valeur de $\tau$, temps caractéristique du problème.   Quelle conclusion peut-on tirer à partir de l'évaluation de ce résultat&nbsp;?
{{% solution "Réponse" %}}

- $\tau =\dfrac{mc}{hS} = \dfrac{\pu{70e-3 kg} \times \pu{235 J·kg-1·K-1}}{\pu{3000 W.m-2·K−1} \times \pu{90e-4 m2}} = \pu{0,61 s}$

- On a vu dans le cours que le régime transitoire d'un phénomène qui évolue exponentiellement dure approximativement $5 \tau$, c'est à dire ici 3 secondes. Cette cuillère n'est donc pas utilisable puisque sa température passe de $\pu{21 °C}$ à $\pu{100 °C}$ en 3 secondes.

{{% /solution %}}

9. Quelles modifications pourrait-on opérer de façon à rendre la cuillère utilisable&nbsp;?
{{% solution "Réponse" %}}

Pour augmenter la valeur de $\tau$, on peut choisir un cuillère

- de masse plus importante ;
- d'un autre matériau de capacité thermique plus grande ;
- de surface plus grande ;
- ....

{{% /solution %}}

10. La situation étudiée dans ce document est analogue à la charge d'un dipôle $(R, C)$ soumis à un échelon de tension.
Compléter le tableau suivant :

<center>

| Système | La cuillère | Le dipôle $(R,C)$ |
| :---- | :----: | :----: |
| Grandeur dont on étudie l'évolution |  |  |
| Grandeur conservée |  |  |
| Expression du flux échangé |  |  |
| Contrainte sur le système |   |  |
| Grandeurs caractéristiques du système |  |  |
| Expression du flux en fonction de la grandeur dont on étudie l'évolution |  |  |
| Loi qui traduit l'échange |   |  |
| Constante de temps |  |  |

</center>

{{% solution "Réponse" %}}

<center>

| Système | La cuillère | Le dipôle $(R,C)$ |
| :---- | :----: | :----: |
| Grandeur dont on étudie l'évolution | Température $T$ | Tension $u_C$ |
| Grandeur conservée | Énergie par transfert thermique | Énergie par transfert d'électrons |
| Expression du flux échangé | $\varphi = \dfrac{\mathrm{d}Q}{dt}$ | $i = \dfrac{\mathrm{d}q}{dt}$ (⚠️ pas un flux d'énergie !) |
| Contrainte sur le système | Température extérieure $T^{ext}$  | Tension $E$ aux bornes du dipôle |
| Grandeurs caractéristiques du système | Capacité thermique $C$ | Capacité du condensateur $C$, résistance $R$ |
| Expression du flux en fonction de la grandeur dont on étudie l'évolution | $\varphi = C\dfrac{\mathrm{d}T}{dt}$ | $i=C\dfrac{\mathrm{d}u_C}{dt}$ |
| Loi qui traduit l'échange | Loi de Newton : $\varphi = hS(T^{ext}-T)$  | Loi des mailles : $E = Ri + u_C$ ou $i = \dfrac{E - u_C}{R}$ |
| Constante de temps | $\tau = \dfrac{C}{h S}$ | $\tau = R C$ |

</center>

{{% /solution %}}

## Applications

- <a href="https://www.lelivrescolaire.fr/page/16636368?docId=o4OL5F0OfgpSoCEiCFzv8" target="_blank">Yaourt ferme (Livre scolaire)</a>
{{% solution "Corrigé" %}}

{{% /solution %}}

- <a href="https://www.lelivrescolaire.fr/page/16636368?docId=O_H9BsCNhAcyTTWYhtJZR" target="_blank">Température ressentie (Livre scolaire)</a>
{{% solution "Corrigé" %}}

{{% /solution %}}

- <a href="https://www.lelivrescolaire.fr/page/16636368?docId=TKOpO5ea93CqN8jqm7AdX" target="_blank">Bouilloire (Livre scolaire)</a>
{{% solution "Corrigé" %}}

{{% /solution %}}
