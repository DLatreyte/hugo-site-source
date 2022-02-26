---
title: "L'effet Joule"
subtitle: "Chapitre 3,1"
author: ""
type: ""
date: 2021-01-20T22:25:02+04:00
draft: false
toc: true
tags: ["Tension", "Courant électrique", "Intensité du courant électrique", "Ligne à haute tension", "Effet Joule"]
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> Cette activité explique le phénomène de l’effet Joule, en précise les avantages et les inconvénients, et explique pourquoi la tension a une influence sur l’énergie dissipée par effet Joule.

## Documents

- {{< remote "Accès aux documents sur le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663319" >}}

- {{< remote "Page Wikipedia sur les lignes à haute tension" "https://fr.wikipedia.org/wiki/Ligne_à_haute_tension" >}}

## Exploitation

1. Expliquer les inconvénients de l’effet Joule dans le transport de l’électricité.
{{% solution "Réponse" %}}
L’effet Joule a plusieurs inconvénients dans le transport de l’électricité. En effet, il est une perte d’énergie sous forme thermique (chaleur), l'élévation de température peut endommager le réseau (en entraînant la fusion des gaines par exemple) ou entraîner des incendies (depuis les boîtiers situés sur les pylônes). *Bien évidemment, la perte d'énergie représente en elle-même un problème*.
{{% /solution %}}

2. Calculer la valeur de la résistance de l’âme d’un câble de 1 000 m de long transportant de très hautes tensions.
{{% solution "Réponse" %}}

- $S = \pu{2500 mm2} = 2500\\ (10^{-3} \text{ m})^2 = \pu{2,5e-3 m2}$.

- La résistance de l’âme (en cuivre) d’un câble de longueur $\pu{1000 m}$ se calcule à partir de l'expression : $ R = \dfrac{\rho \cdot L}{S} $.
    
    **A.N.** $ R = \dfrac{\pu{1,7e-8 \Omega.m} \times \pu{1000 m}}{\pu{2,5e-3 m2}} = \pu{6,8e-3 \Omega} $.
{{% /solution %}}

3. Déterminer l’évolution de la puissance dissipée par effet Joule lorsque l'intensité augmente, puis lorsque la résistance augmente.
{{% solution "Réponse" %}}
La puissance dissipée par effet Joule a pour expression $P = U \\, I = R \\, I^2$ puisque la tension aux bornes d'une résistance est liée à l'intensité du courant électrique qui la traverse par la relation $U = R\\, I^2$.

- *À **résistance constante**, si l’intensité du courant électrique augmente, alors la puissance dissipée par effet Joule augmente*. 
- *À **intensité de courant constante**, si la résistance augmente, alors la puissance dissipée par effet Joule augmente.*
{{% /solution %}}

4. Indiquer l’influence de l’utilisation de la haute tension sur l’intensité.
{{% solution "Réponse" %}}
La puissance électrique à transporter a pour expression $P = U \\, I$. Si on considère cette puissance $P$ comme **constante**, une augmentation de la tension $U$ s'accompagne forcément d'une diminution de l’intensité $I$ du courant électrique.
{{% /solution %}}

5. Déduire des questions 3. et 4. l’intérêt des hautes tensions pour le transport du courant.
{{% solution "Réponse" %}}
Le courant est transporté sous haute tension, car *si on considère que la puissance transportée est constante*, plus la tension est élevée, plus l’intensité du courant électrique est faible, ce qui réduit la puissance dissipée par effet Joule.
{{% /solution %}}

6. Rechercher quel pourcentage de la consommation totale d'électricité correspond aux pertes d'énergie lors du transport de l'électricité en France.
{{% solution "Réponse" %}}
Pour le réseau de transport d'électricité en France, ces pertes sont estimées en moyenne à 2,5&nbsp;% de la consommation globale, soit 11,5 TWh par an.
{{% /solution %}}

7. Résumer rapidement les débats actuels sur l'impact éventuel des lignes à haute tension sur la santé ou sur l'environnement.