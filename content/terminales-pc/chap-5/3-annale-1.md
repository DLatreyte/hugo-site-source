---
title: "Annale : Le super condensateur prêt à sortir de l'ombre"
subtitle: ""
date: 2020-11-06T11:35:19+04:00
draft: false
toc: true
tags: ["Annale", "Courant électrique", "Tension", "Potentiel électrique", "Générateur", "Dipôle", "Branche", "Maille", "Nœud", "Loi des nœuds", "Loi des mailles", "Loi d'Ohm", "Résistance","Condensateur", "Équation différentielle linéaire à coefficients constants"]
categories: ["Physique", "Terminale Spé PC"]
solution_est_visible: true
auto_numbering: true
weight: 300
---

Promis à un grand avenir, les super condensateurs sont des dispositifs de stockage de l’énergie, intermédiaires entre les accumulateurs électrochimiques et les condensateurs traditionnels. Leurs applications, qui n’en sont qu'à leurs débuts, touchent de nombreux domaines tant dans l'électronique de grande diffusion que dans l'électronique de puissance, notamment en ouvrant des perspectives intéressantes dans le domaine des véhicules hybrides.

## Charge d’un condensateur à courant constant

{{< note warning >}}
**Partie pas au programme** mais qui peut vous aider à mieux appréhender la relation entre l’intensité du courant électrique et la charge.
{{< /note >}}

Une première méthode consiste à charger le condensateur à l’aide d’un générateur délivrant un courant d’intensité I constant, selon le montage suivant.

![](/terminales-pc/chap-5/chap-5-3-1.png?width=70%)

À la date $t = \pu{0 s}$, on ferme l’interrupteur $K$ et on enregistre, à l’aide d’un système informatique, les variations au cours du temps de la tension $u_R$ aux bornes du conducteur ohmique de résistance $R = \pu{20 \Omega}$ et de la tension $u$ aux bornes du condensateur. Après traitement, on obtient les courbes ci-après&nbsp;:

![](/terminales-pc/chap-5/chap-5-3-2.png?width=70%)

> *Graphique&nbsp;: $i$ en fonction du temps.*

![](/terminales-pc/chap-5/chap-5-3-3.png?width=70%)

> *Graphique&nbsp;: $u$ en fonction du temps.*

{{< question >}}
Montrer que le graphe $i(t)$ est obtenu à partir de l’enregistrement de $u_R(t)$.
{{< /question >}}

{{< question >}}
Utiliser l’un des graphes pour déterminer la relation numérique entre la tension $u$ aux bornes du condensateur et le temps. Justifier le calcul.
{{< /question >}}

{{< question >}}
En considérant qu’à $t = \pu{0 s}$ le condensateur est déchargé, donner l’expression littérale de la charge $q_A$ portée par l’armature $A$ du condensateur en fonction du temps.
{{< /question >}}

{{< question >}}
Calculer le quotient $\dfrac{q_A}{u}$. Que représente-t-il&nbsp;?
{{< /question >}}

## Charge d’un condensateur soumis à un échelon de tension

Une autre manière de déterminer la valeur de la capacité d’un condensateur, consiste à charger ce dernier avec un générateur de tension constante $E = \pu{5,0 V}$ associé à une résistance $R = \pu{20 \Omega}$, en série avec le condensateur selon le schéma suivant&nbsp;:

![](/terminales-pc/chap-5/chap-5-3-4.png?width=55%)

On ferme l’interrupteur $K$ à $t = \pu{0 s}$, un dispositif informatique (acquisition et traitement) permet d’obtenir les variations de l’intensité dans le circuit et de la tension aux bornes du condensateur au cours du temps. On obtient les deux courbes ci-dessous&nbsp;:

![](/terminales-pc/chap-5/chap-5-3-5.png?width=70%)

> *Graphique&nbsp;: $u$ en fonction du temps.*

![](/terminales-pc/chap-5/chap-5-3-6.png?width=70%)

> *Graphique&nbsp;: $i$ en fonction du temps.*

{{< question >}}
D’après les graphes, quelles sont les valeurs de $u$ et $i$ lorsque le condensateur est chargé&nbsp;?
{{< /question >}}

{{< question >}}
Rappeler l’expression de la constante de temps $\tau$ du circuit. La déterminer graphiquement en précisant la méthode.
{{< /question >}}

{{< question >}}
En déduire la valeur de la capacité $C$ du condensateur. Comparer avec la valeur obtenue à la question 4.
{{< /question >}}

{{< question >}}
*En respectant les notations du montage*, montrer que la tension $u$ vérifie l’équation différentielle&nbsp;:
$$E = RC \, \dfrac{ \mathrm{d} u}{ \mathrm{dt} } + u$$
{{< /question >}}

{{< question >}}
La solution de cette équation différentielle est de la forme $u(t) = E\, (1 – e^{-t/\tau} )$ où $\tau$ est la constante de temps du circuit. Montrer que pour $t = 5\tau$, le condensateur est quasiment chargé. Le vérifier graphiquement.
{{< /question >}}

## Correction

{{< solution "Accès au corrigé" >}}

{{< remote "Correction au format pdf" "/terminales-pc/chap-5/chap-5-3-7.pdf" >}}

{{< /solution >}}
