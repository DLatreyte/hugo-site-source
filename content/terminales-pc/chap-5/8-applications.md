---
title: "Applications : le dipôle (R, C)"
subtitle: "Doc. 5,4"
date: 2026-11-17T12:00:00+04:00
draft: false
toc: true
tags: ["débit de charges", "capacité", "condensateur plan", "capteur capacitif", "supercondensateur", "dipôle RC", "équation différentielle", "charge", "décharge", "constante de temps", "incertitude-type composée", "écart normalisé", "annales"]
categories: ["Physique", "Terminale Spé PC"]
solution_est_visible: true
auto_numbering: true
weight: 800
---
- {{< remote "Énoncé au format pdf" "/terminales-pc/chap-5/5-4/5-4-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/terminales-pc/chap-5/5-4/5-4-corrige.pdf" >}}

{{< note goal "Objectif" >}}
Réinvestir toutes les notions du chapitre sur des exercices, pour l'essentiel extraits de sujets du baccalauréat : intensité et débit de charges, capacité et géométrie d'un condensateur, capteurs capacitifs, équations différentielles de charge et de décharge, détermination graphique de $\tau$, incertitudes-types et écart normalisé, charge et énergie stockées.
{{< /note >}}

{{< note warning "Méthode de travail" >}}
Traiter chaque exercice **sans le cours sous les yeux**. Ce n'est qu'une fois l'exercice terminé que l'on ouvre le cours (Doc. 5,2 et 5,3) pour vérifier ses réponses et repérer ce qui n'était pas su. Les coups de pouce ne se lisent qu'après avoir cherché.

Les exemples résolus se lisent attentivement, crayon en main : chaque étape y est commentée. L'exercice qui suit applique la même méthode à une situation différente.
{{< /note >}}

## Charge, intensité et capacité

### Exemple résolu : charge d'un condensateur à intensité constante

**Énoncé**

Un condensateur de capacité $C = \pu{470 \mu F}$, initialement déchargé, est chargé par un générateur de courant qui impose une intensité constante $I = \pu{2,0 mA}$. Quelle est la tension $u_C$ à ses bornes au bout de $\Delta t = \pu{5,0 s}$ ?

**Résolution commentée**

*On commence par se demander ce que « intensité » veut dire.* L'intensité est le débit de charges : la charge qui arrive chaque seconde sur l'armature. Ici ce débit est constant, donc la charge accumulée grandit régulièrement, comme le volume d'eau dans un seau rempli par un robinet qui coule toujours au même débit :
$$i = \frac{\mathrm{d} q}{\mathrm{d} t} = I \quad\ \text{constante}\ \quad \Rightarrow  \quad q = I \Delta t$$
**A.N.** $q = {2{,}0 \times 10^{-3}\ \pu{A}} \times \pu{5,0 s} = {1{,}0 \times 10^{-2}\ \pu{C}}$.

*On relie ensuite la charge à la tension.* Pour un condensateur, la charge de l'armature et la tension sont proportionnelles : $q = C u_C$, donc $u_C = {\displaystyle \frac{q}{C}}$.

**A.N.** $u_C = {\displaystyle \frac{{1{,}0 \times 10^{-2}\ \pu{C}}}{{470 \times 10^{-6}\ \pu{F}}}} = \pu{21 V}$.

*On contrôle la vraisemblance :* quelques dizaines de volts pour quelques millicoulombs dans un condensateur de quelques centaines de microfarads, l'ordre de grandeur est cohérent. On note aussi que, à intensité constante, $u_C$ augmente **proportionnellement** au temps : ce n'est pas l'exponentielle du dipôle $(R, C)$, car le générateur n'est pas une source de tension.

### Exercice 1 : Flash d'appareil photo

Le flash d'un appareil photo contient un condensateur de capacité $C = \pu{100 \mu F}$, chargé sous une tension $U = \pu{300 V}$.
1. Calculer la charge $q$ portée par l'armature positive du condensateur chargé.
1. Lors de l'éclair, le condensateur se décharge complètement en $\Delta t = \pu{1,0 ms}$. Calculer l'intensité moyenne du courant pendant l'éclair.
1. Pour se recharger, le condensateur reçoit un courant d'intensité constante $I = \pu{10 mA}$. Calculer la durée de la recharge.

{{< solution "Réponse" >}}
1. $q = C U$.

   **A.N.** $q = {100 \times 10^{-6}\ \pu{F}} \times \pu{300 V} = {3{,}0 \times 10^{-2}\ \pu{C}}$.
1. L'intensité moyenne est le débit moyen de charges : $I_\text{moy} = {\displaystyle \frac{q}{\Delta t}}$.

   **A.N.** $I_\text{moy} = {\displaystyle \frac{{3{,}0 \times 10^{-2}\ \pu{C}}}{{1{,}0 \times 10^{-3}\ \pu{s}}}} = \pu{30 A}$. C'est une intensité très élevée, possible seulement parce que la décharge est très brève.
1. À intensité constante, $q = I \Delta t'$, donc $\Delta t' = {\displaystyle \frac{q}{I}}$.

   **A.N.** $\Delta t' = {\displaystyle \frac{{3{,}0 \times 10^{-2}\ \pu{C}}}{{10 \times 10^{-3}\ \pu{A}}}} = \pu{3,0 s}$. On retrouve les quelques secondes d'attente entre deux photos au flash.
{{< /solution >}}

### Exercice 2 : Les supercondensateurs

*D'après Bac 2021, Liban.*

Un supercondensateur permet de stocker et de restituer rapidement de l'énergie électrique. Dans certains transports en commun, un supercondensateur est utilisé pour emmagasiner un maximum d'énergie électrique en quelques secondes lors des phases de freinage. Si des condensateurs classiques étaient utilisés à la place des supercondensateurs, il faudrait *des armatures de très grandes surfaces et très rapprochées*, séparées par un excellent diélectrique.

Données constructeur du supercondensateur étudié : dimensions 35 mm × 60 mm ; capacité 400 F ; tension maximale 2,5 V.

La capacité d'un condensateur plan s'écrit $C = {\displaystyle \frac{\varepsilon S}{d}}$, où $S$ est la surface en regard des deux armatures, $d$ l'écartement entre les armatures et $\varepsilon$ une constante caractéristique de l'isolant placé entre elles.
1. Comparer la capacité du supercondensateur aux valeurs usuelles des capacités des condensateurs utilisés au lycée ou en électronique.
1. Justifier qualitativement la partie soulignée du texte.

{{< solution "Réponse" >}}
1. Les condensateurs utilisés au lycée ou en électronique ont des capacités de l'ordre du millifarad au picofarad (mF, µF, nF, pF). Avec 400 F, le supercondensateur a une capacité des millions de fois plus grande.
1. D'après $C = {\displaystyle \frac{\varepsilon S}{d}}$, la capacité est proportionnelle à la surface $S$ : des armatures de grande surface augmentent $C$. Elle est inversement proportionnelle à l'écartement $d$ : des armatures très rapprochées augmentent aussi $C$. Pour atteindre des centaines de farads avec un condensateur classique, il faudrait donc des surfaces immenses et des écartements minuscules.
{{< /solution >}}

## Équations différentielles de charge et de décharge

### Exemple résolu : établir et résoudre l'équation de charge

*D'après Bac 2022, Nouvelle-Calédonie.*

{{< columns >}}
Un générateur idéal de tension $E = \pu{12 V}$ est branché en série avec un conducteur ohmique de résistance $R$ et un condensateur de capacité $C$, initialement déchargé. À l'instant $t = 0$, on ferme l'interrupteur. On cherche l'équation différentielle vérifiée par $u_C$, sa solution, et la signification de la constante qui y apparaît.
{{< column >}}
![](/terminales-pc/chap-5/5-4/circuit-charge.svg?width=35%)
{{< endcolumns >}}

**Résolution commentée**

*Étape 1 : écrire ce que l'on sait des tensions.* La loi des mailles donne $E = u_R + u_C$. Il y a deux inconnues, $u_R$ et $u_C$ : il faut exprimer $u_R$ à l'aide de $u_C$.

*Étape 2 : relier chaque tension au courant.* Loi d'Ohm : $u_R = R i$. Pour le condensateur, $q = C u_C$ et $i = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ (le courant arrive sur l'armature qui porte $+q$). Comme $C$ est constante :
$$i = C \frac{\mathrm{d} u_C}{\mathrm{d} t} \quad\ \text{donc}\ \quad u_R = R C \frac{\mathrm{d} u_C}{\mathrm{d} t}$$

*Étape 3 : remplacer et ordonner.*
$$E = R C \frac{\mathrm{d} u_C}{\mathrm{d} t} + u_C \quad \Leftrightarrow  \quad \frac{\mathrm{d} u_C}{\mathrm{d} t} + \frac{u_C}{\tau} = \frac{E}{\tau} \quad\ \text{avec}\ \quad \tau = R C$$

*Étape 4 : vérifier que $\tau$ est une durée.* $[R] = {\displaystyle \frac{U}{I}}$ et $[C] = {\displaystyle \frac{[Q]}{U}} = {\displaystyle \frac{I T}{U}}$, donc $[R C] = T$. On peut aussi le lire dans l'équation : ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ s'exprime en V/s et ${\displaystyle \frac{u_C}{\tau}}$ doit avoir la même unité, donc $\tau$ s'exprime en secondes.

*Étape 5 : résoudre.* On admet que les solutions sont de la forme $u_C (t) = A + B e^{-t / \tau}$. En remplaçant dans l'équation, les termes en $e^{-t / \tau}$ se compensent et il reste $A / \tau = E / \tau$, donc $A = E$. La condition initiale $u_C (0) = 0$ donne $E + B = 0$, donc $B = -E$ :
$$u_C (t) = E (1 - e^{-t / \tau})$$

*Étape 6 : contrôler.* En $t = 0$, $u_C = 0$ ; quand $t \to  \infty$, $u_C \to  E$. C'est bien le comportement attendu pour une charge.

### Exercice 3 : Décharge d'un supercondensateur

*D'après Bac 2022, Amérique du Nord.*

{{< columns >}}
Un supercondensateur de capacité $C$, complètement chargé sous sa tension nominale $E$, est placé dans le circuit ci-contre. À l'instant $t = 0$, on ferme l'interrupteur $K$. On note $q(t)$ la charge portée par l'armature positive.

Sur le schéma, la flèche de $u_C$ et la flèche de $i$ sont orientées dans le même sens : le courant $i$ **sort** par l'armature positive.

Données : $u_C (0) = E = \pu{2,7 V}$ ; $R = \pu{100 m\Omega}$.
{{< column >}}
![](/terminales-pc/chap-5/5-4/fig-1.svg?width=45%)
{{< endcolumns >}}

1. Montrer qu'au cours de la décharge l'intensité s'exprime par $i(t) = -C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$.
1. En déduire que la tension $u_C$ obéit à l'équation différentielle $R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C = 0$.
1. La solution est de la forme $u_C (t) = A + B e^{-t / (R C)}$. En détaillant la démarche, déterminer les valeurs de $A$ et $B$.

{{< note tip "Coup de pouce" >}}
Question 1 : le courant $i$ sort de l'armature positive. Pendant ce temps, $q$ augmente-t-elle ou diminue-t-elle ? Quel signe faut-il donc placer devant ${\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ pour obtenir $i > 0$ ?
{{< /note >}}

{{< solution "Réponse" >}}
1. Le courant sort par l'armature qui porte $q$ : des charges positives quittent cette armature, donc $q$ diminue quand $i > 0$. On a donc $i = -{\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ (convention générateur pour le condensateur). Avec $q = C u_C$ et $C$ constante : $i = -C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$.

   On vérifie le signe : pendant la décharge, $u_C$ diminue, donc ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} < 0$ et $i > 0$. Le courant circule bien dans le sens de la flèche.
1. La loi des mailles donne $u_C - u_R = 0$, et la loi d'Ohm $u_R = R i$ (convention récepteur pour la résistance). Donc $u_C = R i = -R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$, soit :
   $$R C \frac{\mathrm{d} u_C}{\mathrm{d} t} + u_C = 0$$
1. Quand $t \to  \infty$, le condensateur est déchargé : $u_C \to  0$. Comme $e^{-t / (R C)} \to  0$, il reste $A = 0$.

   À $t = 0$ : $u_C (0) = A + B = E$, donc $B = E = \pu{2,7 V}$. Finalement $u_C (t) = E e^{-t / (R C)}$.
{{< /solution >}}

### Exercice 4 : Défibrillateur cardiaque implantable

*D'après Bac 2022, Amérique du Sud.*

La défibrillation consiste à appliquer un « choc électrique » très bref au cœur d'un patient. Un défibrillateur implanté contient une pile, un montage qui élève la tension jusqu'à 800 V, et un condensateur de capacité $C = \pu{50 \mu F}$ qui stocke l'énergie du choc. Le fonctionnement se décompose en deux phases :
- **phase 1** : le condensateur, initialement déchargé, se charge sous 800 V à travers une résistance $R$ ($K_1$ fermé, $K_2$ ouvert) ;
- **phase 2** : à la date $t_1$, on ouvre $K_1$ et on ferme $K_2$ ; le condensateur se décharge dans la résistance $r = \pu{10 \Omega}$, qui modélise le cœur.

![](/terminales-pc/chap-5/5-4/fig-2.svg?width=95%)

1. Parmi les quatre graphiques, lequel représente la tension $u_C$ pendant la phase 1 ? Justifier.
1. Établir l'équation différentielle vérifiée par $u_C (t)$ pendant la phase 2.
1. Vérifier que la solution de cette équation peut s'écrire $u_C (t) = A e^{-(t - t_1) / \tau}$. Exprimer $\tau$ en fonction de $r$ et $C$, et calculer sa valeur.
1. Déterminer $A$, sachant que $u_C (t_1) = \pu{800 V}$.
1. Estimer la durée du « choc électrique ». Commenter.
1. Représenter l'allure de $u_C (t)$ pendant un cycle complet charge puis décharge.

{{< note tip "Coup de pouce" >}}
Question 2 : pendant la phase 2, le circuit ne comporte plus que le condensateur et la résistance $r$. On peut reprendre exactement la démarche de l'exercice précédent.

Question 3 : dériver $e^{-(t - t_1) / \tau}$ se fait comme pour $e^{-t / \tau}$ : le décalage $t_1$ est une constante.
{{< /note >}}

{{< solution "Réponse" >}}
1. Pendant la phase 1, le condensateur part de 0 (déchargé), se charge et sa tension tend vers 800 V. La tension est continue, croissante et positive : c'est le graphique n°3.
1. La maille ne contient que $C$ et $r$. Avec $u_C = r i$ et $i = -C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ (comme dans l'exercice précédent) :
   $$r C \frac{\mathrm{d} u_C}{\mathrm{d} t} + u_C = 0$$
1. ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} = -{\displaystyle \frac{A}{\tau}} e^{-(t - t_1) / \tau}$. En remplaçant : $-r C {\displaystyle \frac{A}{\tau}} e^{-(t - t_1) / \tau} + A e^{-(t - t_1) / \tau} = 0$, vrai pour tout $t$ à condition que $\tau = r C$.

   **A.N.** $\tau = \pu{10 \Omega} \times {50 \times 10^{-6}\ \pu{F}} = {5{,}0 \times 10^{-4}\ \pu{s}} = \pu{0,50 ms}$.
1. En $t = t_1$ : $u_C (t_1) = A e^0 = A$, donc $A = \pu{800 V}$.
1. La décharge est pratiquement terminée au bout de $5 \tau$.

   **A.N.** $5 \tau = 5 \times \pu{0,50 ms} = \pu{2,5 ms}$. Le choc dure quelques millisecondes : il est bien « très bref ».
1. De $0$ à $t_1$ : montée continue de 0 vers 800 V, d'allure exponentielle (graphique n°3). À partir de $t_1$ : décroissance exponentielle rapide de 800 V vers 0, en quelques millisecondes (allure du graphique n°1, décalée à $t_1$). La courbe est continue en $t_1$.
{{< /solution >}}

## Détermination graphique de $\tau$ et incertitudes

### Exemple résolu : lire $\tau$ sur une courbe de charge, puis évaluer une incertitude

*D'après Bac 2022, Nouvelle-Calédonie, complété.*

On reprend le circuit de l'exemple résolu précédent avec $E = \pu{12 V}$ et $R = \pu{30 k\Omega}$. On enregistre la tension $u_C$ pendant la charge.

![](/terminales-pc/chap-5/5-4/fig-3.svg?width=95%)

> *Charge du condensateur. En bleu : méthode des 63 % ; en vert : tangente à l'origine.*

**Résolution commentée**

*Étape 1 : choisir la méthode adaptée à la courbe.* La courbe est croissante et tend vers $E$ : c'est une charge. À $t = \tau$, $u_C (\tau) = E (1 - e^{-1}) \approx 0{,}63 E$.

**A.N.** $0{,}63 \times \pu{12 V} = \pu{7,6 V}$.

*Étape 2 : construire.* On trace l'horizontale $u = \pu{7,6 V}$ ; elle coupe la courbe en un point dont on lit l'abscisse : $\tau = \pu{0,90 ms}$. Contrôle par la tangente à l'origine : elle coupe l'asymptote $u = E$ à la même abscisse.

*Étape 3 : exploiter.* $\tau = R C$, donc $C = {\displaystyle \frac{\tau}{R}}$.

**A.N.** $C = {\displaystyle \frac{{0{,}90 \times 10^{-3}\ \pu{s}}}{{30 \times 10^{3}\ \pu{\Omega}}}} = {3{,}0 \times 10^{-8}\ \pu{F}} = \pu{30 nF}$.

*Étape 4 : évaluer l'incertitude-type.* On estime l'incertitude-type de lecture à $u(\tau) = \pu{0,05 ms}$. La résistance porte l'indication « $\pm \pu{1 \%}$ » : $a = \pu{0,3 k\Omega}$, donc $u(R) = a / \sqrt{3} = \pu{0,17 k\Omega}$. La relation d'incertitude-type composée (fournie) est :
$$u(C) = C \sqrt{(\frac{u(\tau)}{\tau})^2 + (\frac{u(R)}{R})^2}$$
**A.N.** $u(C) = \pu{30 nF} \times \sqrt{({\displaystyle \frac{\pu{0,05 ms}}{\pu{0,90 ms}}})^2 + ({\displaystyle \frac{\pu{0,17 k\Omega}}{\pu{30 k\Omega}}})^2} = \pu{1,7 nF}$.

*Étape 5 : comparer.* Le fabricant annonce $C_\text{réf} = \pu{33 nF}$. On calcule l'écart normalisé :
$$z = \frac{\left|C - C_\text{réf}\right|}{u(C)} = \frac{\left|\pu{30 nF} - \pu{33 nF}\right|}{\pu{1,7 nF}} = 1{,}8$$
Comme $z \leq  2$, la mesure est compatible avec la valeur du fabricant. On note que c'est l'incertitude de lecture sur $\tau$ (6 %) qui domine, loin devant celle sur $R$ (0,6 %).

### Exercice 5 : Le supercondensateur d'un totem de recharge

*D'après Bac 2022, Amérique du Nord.*

On reprend le supercondensateur de l'exercice 3 ($E = \pu{2,7 V}$, $R = \pu{100 m\Omega}$ avec $u(R) = \pu{2 m\Omega}$). On enregistre la tension $u_C$ pendant sa décharge.

![](/terminales-pc/chap-5/5-4/fig-4.svg?width=95%)

1. Déterminer le temps caractéristique $\tau$ de la décharge. Faire apparaître la construction graphique.
1. En déduire la valeur de la capacité $C$ du supercondensateur. Commenter l'ordre de grandeur obtenu.
1. L'incertitude-type sur la lecture de $\tau$ est estimée à $u(\tau) = \pu{25 s}$. On donne $u(C) = C \sqrt{({\displaystyle \frac{u(\tau)}{\tau}})^2 + ({\displaystyle \frac{u(R)}{R}})^2}$. Calculer $u(C)$, puis comparer la valeur obtenue à la valeur annoncée par le constructeur, $C_\text{réf} = \pu{3000 F}$.

Le totem de recharge des bus contient une association de supercondensateurs qui se comporte comme un condensateur unique de capacité $C_\text{totem} = \pu{20 F}$, chargé sous 760 V. Voici sa tension lors d'une décharge dans une résistance.

![](/terminales-pc/chap-5/5-4/fig-5.svg?width=95%)

4. Déterminer la valeur de l'intensité maximale $I_\text{max}$ lors de cette décharge. Commenter, sachant que, d'après le constructeur, « l'intensité du courant peut atteindre plusieurs milliers d'ampères en début de transfert ».

{{< note tip "Coup de pouce" >}}
Question 1 : la courbe décroît vers 0. Le pourcentage à utiliser n'est pas celui de l'exemple résolu.

Question 4 : d'après l'exercice 3, $\left|i\right| = C \left|{\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}\right|$. À quelle date la pente de la courbe est-elle la plus forte ? Comment mesurer une pente sur une courbe ?
{{< /note >}}

{{< solution "Réponse" >}}
1. C'est une décharge : $u_C (\tau) = E e^{-1} \approx 0{,}37 E$.

   **A.N.** $0{,}37 \times \pu{2,7 V} = \pu{1,0 V}$. L'horizontale $u = \pu{1,0 V}$ coupe la courbe à l'abscisse $\tau = {2{,}9 \times 10^{2}\ \pu{s}}$.
1. $C = {\displaystyle \frac{\tau}{R}}$.

   **A.N.** $C = {\displaystyle \frac{{2{,}9 \times 10^{2}\ \pu{s}}}{{100 \times 10^{-3}\ \pu{\Omega}}}} = {2{,}9 \times 10^{3}\ \pu{F}}$. C'est des millions de fois plus que les condensateurs usuels (µF, nF).
1. **A.N.** $u(C) = {2{,}9 \times 10^{3}\ \pu{F}} \times \sqrt{({\displaystyle \frac{\pu{25 s}}{\pu{290 s}}})^2 + ({\displaystyle \frac{\pu{2 m\Omega}}{\pu{100 m\Omega}}})^2} = {2{,}6 \times 10^{2}\ \pu{F}}$.

   $z = {\displaystyle \frac{\left|C - C_\text{réf}\right|}{u(C)}} = {\displaystyle \frac{\left|\pu{2900 F} - \pu{3000 F}\right|}{\pu{260 F}}} = 0{,}4$. Comme $z \leq  2$, la mesure est compatible avec la valeur annoncée.
1. L'intensité est maximale en valeur absolue au début de la décharge, là où la pente est la plus forte. On trace la tangente à l'origine : elle passe par $(0 ; \pu{760 V})$ et coupe l'axe des temps en $t = \pu{2,0 s}$ (c'est $\tau$). Sa pente vaut ${\displaystyle \frac{0 - 760}{2{,}0}} = \pu{-380 V/s}$.

   **A.N.** $I_\text{max} = \pu{20 F} \times \pu{380 V/s} = {7{,}6 \times 10^{3}\ \pu{A}}$. C'est bien « plusieurs milliers d'ampères ».
{{< /solution >}}

## Exercices de synthèse

Les exercices qui suivent mélangent les notions du chapitre. À chaque question, il faut identifier soi-même la méthode à employer.

### Exercice 6 : Mesurer la capacité d'un supercondensateur

*D'après Bac 2021, Liban.*

On étudie la charge du supercondensateur de l'exercice 2 (capacité de référence $C_\text{réf} = \pu{400 F}$) à travers un conducteur ohmique de résistance $R = \pu{2,0 \Omega}$, sous une tension $E = \pu{2,5 V}$. Le schéma est celui du premier exemple résolu. Le supercondensateur est initialement déchargé ; à $t = 0$, on ferme l'interrupteur.

1. Donner la relation entre $i(t)$ et la dérivée de la charge $q(t)$, puis la relation entre $i(t)$, $C$ et la dérivée de $u_C (t)$.
1. Montrer que $u_C$ vérifie ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + {\displaystyle \frac{1}{\tau}} u_C = {\displaystyle \frac{E}{\tau}}$ et exprimer $\tau$.
1. Vérifier que les solutions sont de la forme $u_C (t) = A e^{-t / \tau} + E$, puis déterminer $A$.
1. À partir de la courbe ci-dessous, déterminer la valeur $C_1$ de la capacité. Expliciter la démarche.

![](/terminales-pc/chap-5/5-4/fig-6.svg?width=95%)

Un microcontrôleur reproduit l'expérience dix fois et détermine à chaque fois $\tau$ (date à laquelle le condensateur est chargé à 63 %). Valeurs obtenues, en secondes :

| 811,614 | 818,076 | 810,301 | 810,495 | 818,526 |
|:---|:---|:---|:---|:---|
| 812,067 | 811,327 | 813,109 | 817,838 | 819,474 |

La moyenne vaut $\overline{\tau} = \pu{814,28 s}$ et la calculatrice donne une incertitude-type $u(\overline{\tau}) = \pu{1,175 s}$.

5. Écrire le résultat de la mesure de $\tau$ avec son incertitude-type.
1. On estime $u(R) = \pu{0,1 \Omega}$, et on donne $u(C_2) = C_2 \sqrt{({\displaystyle \frac{u(R)}{R}})^2 + ({\displaystyle \frac{u(\overline{\tau})}{\overline{\tau}}})^2}$. Déterminer la capacité $C_2$ et son incertitude-type.
1. Comparer $C_2$ à la valeur de référence. Conclure.

{{< note tip "Coup de pouce" >}}
Question 5 : l'incertitude-type s'écrit avec un ou deux chiffres significatifs, et la valeur s'arrondit à la même décimale.
{{< /note >}}

{{< solution "Réponse" >}}
1. $i = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ et $q = C u_C$, donc $i = C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ car $C$ est constante.
1. Loi des mailles : $E = u_R + u_C = R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C$. En divisant par $R C$ : ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + {\displaystyle \frac{u_C}{R C}} = {\displaystyle \frac{E}{R C}}$, donc $\tau = R C$.
1. ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} = -{\displaystyle \frac{A}{\tau}} e^{-t / \tau}$. En remplaçant : $-{\displaystyle \frac{A}{\tau}} e^{-t / \tau} + {\displaystyle \frac{A}{\tau}} e^{-t / \tau} + {\displaystyle \frac{E}{\tau}} = {\displaystyle \frac{E}{\tau}}$ : l'égalité est vérifiée. Condition initiale $u_C (0) = 0$ : $A + E = 0$, donc $A = -E$.
1. Charge : on cherche $u_C = 0{,}63 E$.

   **A.N.** $0{,}63 \times \pu{2,5 V} = \pu{1,6 V}$, lu à $\tau = \pu{750 s}$. Alors $C_1 = {\displaystyle \frac{\tau}{R}} = {\displaystyle \frac{\pu{750 s}}{\pu{2,0 \Omega}}} = {3{,}8 \times 10^{2}\ \pu{F}}$.
1. $\tau = \pu{814,3 s}$ avec $u(\tau) = \pu{1,2 s}$.
1. **A.N.** $C_2 = {\displaystyle \frac{\pu{814,3 s}}{\pu{2,0 \Omega}}} = {4{,}1 \times 10^{2}\ \pu{F}}$ et $u(C_2) = {4{,}1 \times 10^{2}\ \pu{F}} \times \sqrt{({\displaystyle \frac{\pu{0,1 \Omega}}{\pu{2,0 \Omega}}})^2 + ({\displaystyle \frac{\pu{1,2 s}}{\pu{814 s}}})^2} = \pu{20 F}$.

   L'incertitude vient presque entièrement de $R$ (5 % contre 0,15 % pour $\tau$).
1. $z = {\displaystyle \frac{\left|\pu{407 F} - \pu{400 F}\right|}{\pu{20 F}}} = 0{,}35$. Comme $z \leq  2$, la mesure est compatible avec la valeur du constructeur.
{{< /solution >}}

### Exercice 7 : Détecteur capacitif d'humidité

*D'après Bac 2023, Métropole.*

Un système d'arrosage automatique peut être déclenché par un détecteur capacitif d'humidité du sol. Ce détecteur est modélisé par un condensateur plan : deux plaques métalliques de surface $S$, séparées d'une distance $d$, sont plantées dans le sol. La capacité vaut $C = {\displaystyle \frac{\varepsilon S}{d}}$, où $\varepsilon$ est la permittivité du sol. On appelle **teneur en eau** le pourcentage volumique d'eau dans le sol. La permittivité d'un sol argileux dépend de sa teneur en eau :

![](/terminales-pc/chap-5/5-4/fig-7.svg?width=80%)

Le détecteur est branché en série avec un conducteur ohmique de résistance $R = {2{,}2 \times 10^{5}\ \pu{\Omega}}$ et un générateur de tension constante $E$. On a $S = {1{,}0 \times 10^{-1}\ \pu{m^2}}$ et $d = {1{,}0 \times 10^{-2}\ \pu{m}}$.

1. Prévoir le sens de variation de la capacité $C$ du détecteur quand la teneur en eau d'un sol argileux augmente.
1. Le condensateur, déchargé, est mis sous tension à $t = 0$. Montrer que $E = \tau {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C$, et exprimer $\tau$.
1. Vérifier que $u_C (t) = E (1 - e^{-t / \tau})$ est solution et respecte la condition initiale. Montrer que $u_C (\tau) \approx 0{,}63 E$.
1. Un microcontrôleur relève 52000 valeurs de la tension par seconde. Pour une mesure précise, il faut au moins 10 valeurs avant d'atteindre $\tau$. Montrer que $\tau$ doit être au minimum de l'ordre de 200 µs.
1. Déterminer la teneur en eau minimale d'un sol argileux mesurable avec ce dispositif.
1. Une plante pousse normalement si la teneur en eau est comprise entre 24 % et 38 %. Le microcontrôleur mesure $\tau = \pu{0,287 ms}$. Faut-il arroser ?

{{< note tip "Coup de pouce" >}}
Question 5, premier niveau : quelle grandeur du graphique peut-on calculer à partir de $\tau$ ?

Question 5, second niveau : combiner $\tau = R C$ et $C = {\displaystyle \frac{\varepsilon S}{d}}$ pour exprimer $\varepsilon$ en fonction de $\tau$, $R$, $S$ et $d$.
{{< /note >}}

{{< solution "Réponse" >}}
1. D'après le graphique, $\varepsilon$ augmente avec la teneur en eau. Comme $C = {\displaystyle \frac{\varepsilon S}{d}}$ avec $S$ et $d$ fixés, $C$ augmente aussi.
1. Loi des mailles $E = u_R + u_C$, avec $u_R = R i = R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$. Donc $E = \tau {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C$ avec $\tau = R C$.
1. ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} = {\displaystyle \frac{E}{\tau}} e^{-t / \tau}$, donc $\tau {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C = E e^{-t / \tau} + E - E e^{-t / \tau} = E$ : l'équation est vérifiée. En $t = 0$ : $u_C (0) = E (1 - 1) = 0$, le condensateur est bien déchargé. Enfin $u_C (\tau) = E (1 - e^{-1}) \approx 0{,}63 E$.
1. Une mesure toutes les ${\displaystyle \frac{1}{52000}} = \pu{19,2 \mu s}$. Dix mesures durent $10 \times \pu{19,2 \mu s} = \pu{192 \mu s}$ : il faut $\tau \geq  {2 \times 10^{2}\ \pu{\mu s}}$ environ.
1. $\tau = R C = {\displaystyle \frac{R \varepsilon S}{d}}$, donc $\varepsilon = {\displaystyle \frac{d \tau}{R S}}$.

   **A.N.** $\varepsilon_\text{min} = {\displaystyle \frac{{1{,}0 \times 10^{-2}\ \pu{m}} \times {200 \times 10^{-6}\ \pu{s}}}{{2{,}2 \times 10^{5}\ \pu{\Omega}} \times {1{,}0 \times 10^{-1}\ \pu{m^2}}}} = {9{,}1 \times 10^{-11}\ \pu{F/m}} = 0{,}91 \times 10^{-10} \pu{F/m}$.

   Sur le graphique, cela correspond à une teneur en eau d'environ 15 % : en dessous, le dispositif ne peut pas mesurer.
1. **A.N.** $\varepsilon = {\displaystyle \frac{{1{,}0 \times 10^{-2}\ \pu{m}} \times {0{,}287 \times 10^{-3}\ \pu{s}}}{{2{,}2 \times 10^{5}\ \pu{\Omega}} \times {1{,}0 \times 10^{-1}\ \pu{m^2}}}} = {1{,}3 \times 10^{-10}\ \pu{F/m}}$.

   Le graphique donne une teneur en eau d'environ 20 %, inférieure à 24 % : il faut déclencher l'arrosage.
{{< /solution >}}

### Exercice 8 : Mesure de l'épaisseur d'un film alimentaire

*D'après Bac 2025, Métropole.*

On réalise un condensateur plan en plaçant une couche de film alimentaire d'épaisseur $e$ entre deux feuilles d'aluminium de 21 cm × 28 cm. Sa capacité vaut $C = {\displaystyle \frac{\varepsilon_0 \varepsilon_r S}{e}}$.

Données : $\varepsilon_0 = {8{,}85 \times 10^{-12}\ \pu{F/m}}$ ; permittivité relative du film $\varepsilon_{r, \text{film}} = 2{,}3$ ; de l'air $\varepsilon_{r, \text{air}} = 1{,}0$ ; épaisseur de référence du film $e_\text{film, réf} = \pu{7,6 \mu m}$.

Ce condensateur est branché en série avec un conducteur ohmique $R = \pu{1,00 k\Omega}$ et un générateur idéal $E = \pu{4,9 V}$. On ferme l'interrupteur à $t = 0$, le condensateur étant déchargé.

![](/terminales-pc/chap-5/5-4/fig-8.svg?width=95%)

1. Établir l'équation différentielle ${\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + {\displaystyle \frac{1}{\tau}} u_C = {\displaystyle \frac{E}{\tau}}$ et donner l'expression de $\tau$.
1. La solution s'écrit $u_C (t) = A (1 - e^{-t / \tau})$. Déterminer $A$.
1. Exprimer $u_C (\tau)$ en fonction de $E$.
1. Déterminer $\tau$ à l'aide de la courbe. Expliciter la démarche.
1. En déduire une valeur expérimentale de la capacité $C$.
1. Des mesures répétées donnent $C = \pu{69,8 nF}$. En déduire l'épaisseur $e_\text{film}$ du film.
1. L'incertitude-type sur cette épaisseur vaut $u(e_\text{film}) = \pu{1,0 \mu m}$. Discuter de l'accord avec l'épaisseur de référence.
1. Pour expliquer l'écart, on suppose qu'une fine couche d'air d'épaisseur $e_\text{air}$ reste piégée entre les feuilles. La capacité devient alors $C' = {\displaystyle \frac{\varepsilon_0 S}{{\displaystyle \frac{e_\text{air}}{\varepsilon_{r, \text{air}}}} + {\displaystyle \frac{e_\text{film}}{\varepsilon_{r, \text{film}}}}}}$. En envisageant deux cas limites, vérifier que cette expression est compatible avec celle de $C$.
1. Déterminer $e_\text{air}$ en prenant $e_\text{film} = e_\text{film, réf}$. Commenter.

{{< note tip "Coup de pouce" >}}
Question 8 : que devient $C'$ s'il n'y a pas d'air ($e_\text{air} = 0$) ? Et s'il n'y a pas de film ?

Question 9 : isoler d'abord le dénominateur ${\displaystyle \frac{e_\text{air}}{\varepsilon_{r, \text{air}}}} + {\displaystyle \frac{e_\text{film}}{\varepsilon_{r, \text{film}}}}$, qui vaut ${\displaystyle \frac{\varepsilon_0 S}{C'}}$.
{{< /note >}}

{{< solution "Réponse" >}}
1. Loi des mailles $E = R i + u_C$ et $i = C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$, donc $E = R C {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}} + u_C$. En divisant par $R C$, on obtient l'équation demandée avec $\tau = R C$.
1. Quand $t \to  \infty$, le condensateur est chargé : $u_C \to  E$. Or $A (1 - e^{-t / \tau}) \to  A$, donc $A = E$.
1. $u_C (\tau) = E (1 - e^{-1}) \approx 0{,}63 E$.
1. **A.N.** $0{,}63 \times \pu{4,9 V} = \pu{3,1 V}$. L'horizontale $u = \pu{3,1 V}$ coupe la courbe à l'abscisse $\tau = \pu{70 \mu s}$.
1. **A.N.** $C = {\displaystyle \frac{\tau}{R}} = {\displaystyle \frac{{70 \times 10^{-6}\ \pu{s}}}{{1{,}00 \times 10^{3}\ \pu{\Omega}}}} = {7{,}0 \times 10^{-8}\ \pu{F}} = \pu{70 nF}$.
1. $e_\text{film} = {\displaystyle \frac{\varepsilon_0 \varepsilon_{r, \text{film}} S}{C}}$.

   **A.N.** $e_\text{film} = {\displaystyle \frac{{8{,}85 \times 10^{-12}\ \pu{F/m}} \times 2{,}3 \times \pu{0,21 m} \times \pu{0,28 m}}{{69{,}8 \times 10^{-9}\ \pu{F}}}} = {1{,}7 \times 10^{-5}\ \pu{m}} = \pu{17 \mu m}$.
1. $z = {\displaystyle \frac{\left|\pu{17 \mu m} - \pu{7,6 \mu m}\right|}{\pu{1,0 \mu m}}} = 9{,}4$. Comme $z > 2$, la mesure est en net désaccord avec la valeur de référence : le modèle ou la mesure est à remettre en cause.
1. Si $e_\text{air} = 0$ : $C' = {\displaystyle \frac{\varepsilon_0 \varepsilon_{r, \text{film}} S}{e_\text{film}}}$, on retrouve $C$ pour le film seul. Si $e_\text{film} = 0$ : $C' = {\displaystyle \frac{\varepsilon_0 \varepsilon_{r, \text{air}} S}{e_\text{air}}}$, on retrouve $C$ pour une couche d'air seule. L'expression est compatible avec les deux cas.
1. $e_\text{air} = \varepsilon_{r, \text{air}} ({\displaystyle \frac{\varepsilon_0 S}{C'}} - {\displaystyle \frac{e_\text{film}}{\varepsilon_{r, \text{film}}}})$.

   **A.N.** $e_\text{air} = 1{,}0 \times ({\displaystyle \frac{{8{,}85 \times 10^{-12}\ \pu{F/m}} \times \pu{0,21 m} \times \pu{0,28 m}}{{69{,}8 \times 10^{-9}\ \pu{F}}}} - {\displaystyle \frac{{7{,}6 \times 10^{-6}\ \pu{m}}}{2{,}3}}) = {4{,}2 \times 10^{-6}\ \pu{m}} = \pu{4,2 \mu m}$.

   Une couche d'air d'environ 4 µm, soit la moitié de l'épaisseur du film, suffit à expliquer l'écart. Comme l'air a une permittivité plus faible que le film, une fine couche d'air diminue beaucoup la capacité. C'est plausible : le film n'est jamais parfaitement plaqué contre l'aluminium.
{{< /solution >}}

### Exercice 9 : Extraction du gaz de schiste par électro-fracturation

*D'après Bac 2023, La Réunion, complété.*

L'électro-fracturation est une méthode à l'étude pour extraire le gaz de schiste. Deux électrodes sont introduites dans une cavité de la roche remplie d'eau. Des condensateurs leur appliquent une forte tension, ce qui provoque un arc électrique accompagné d'une « onde de pression » qui fracture la roche.

L'installation est modélisée ainsi :
- une alimentation de tension $E = \pu{40 kV}$ ;
- de 1 à 6 condensateurs identiques de capacité $C = \pu{200 nF}$, placés en parallèle ; ils se comportent comme un condensateur unique de capacité $C_\text{eq} = n C$, où $n$ est le nombre de condensateurs utilisés ;
- un conducteur ohmique de résistance $R_1 = \pu{160 k\Omega}$ ;
- le système {électrodes + eau}, modélisé par un conducteur ohmique de résistance $R_2 = \pu{100 \Omega}$ ;
- un interrupteur à deux positions : en position 1, le condensateur équivalent se charge à travers $R_1$ ; en position 2, il se décharge dans $R_2$.

Données : l'énergie stockée par un condensateur de capacité $C$ soumis à la tension $u_C$ vaut $W = {\displaystyle \frac{1}{2}} C u_C^2$ ; le rendement énergétique vaut $\eta = {\displaystyle \frac{E_\text{utile}}{E_\text{consommée}}}$.

**Partie A : charge.** Le condensateur équivalent est déchargé ; à $t = 0$, on bascule l'interrupteur en position 1.

![](/terminales-pc/chap-5/5-4/fig-9.svg?width=95%)

1. Établir la relation entre $u_{C, \text{eq}}$, $u_{R 1}$ et $E$.
1. Établir l'équation différentielle vérifiée par $u_{C, \text{eq}}$ pendant la charge.
1. Vérifier que $u_{C, \text{eq}} (t) = E (1 - e^{-t / \tau_\text{charge}})$ est solution, et exprimer $\tau_\text{charge}$ en fonction de $R_1$ et $C_\text{eq}$.
1. Déterminer $C_\text{eq}$ à l'aide de la courbe, en faisant apparaître la démarche.
1. En déduire le nombre $n$ de condensateurs utilisés.

Dans la suite, on prend $C_\text{eq} = \pu{600 nF}$.

6. Exprimer la charge $q(t)$ de l'armature positive du condensateur équivalent pendant la charge. Calculer sa valeur maximale $q_\text{max}$.
1. À partir de l'expression de $q(t)$, établir celle de l'intensité $i(t)$ du courant de charge. Calculer l'intensité au début de la charge.
1. Calculer l'énergie maximale $W_\text{max}$ stockée. Montrer que cette énergie s'écrit aussi $W = {\displaystyle \frac{q^2}{2 C_\text{eq}}}$ et vérifier la valeur obtenue avec $q_\text{max}$.

**Partie B : pré-décharge.** À $t = 0$, le condensateur équivalent, chargé sous $E$, est basculé en position 2. Avant l'apparition de l'arc, il subit une pré-décharge pendant $\Delta t = \pu{12 \mu s}$, au cours de laquelle $u_{C, \text{eq}} (t) = E e^{-t / (R_2 C_\text{eq})}$.

9. Calculer la tension $u_{C, \text{eq}}$ à la fin de la pré-décharge.
1. Calculer la charge restant sur l'armature positive à la fin de la pré-décharge. En déduire la charge qui s'est écoulée dans l'eau pendant la pré-décharge, puis l'intensité moyenne du courant pendant cette phase.
1. Calculer l'énergie $W_\text{arc}$ restant dans le condensateur et disponible pour créer l'arc électrique.
1. Calculer le rendement énergétique $\eta$ de l'installation. Commenter.

{{< note tip "Coup de pouce" >}}
Question 7 : l'intensité est le débit de charges, $i = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$.

Question 8 : dans $W = {\displaystyle \frac{1}{2}} C u_C^2$, remplacer $u_C$ en utilisant la relation entre $q$ et $u_C$.

Question 10 : la charge écoulée est la différence entre la charge au début et la charge à la fin de la pré-décharge.
{{< /note >}}

{{< solution "Réponse" >}}
1. Loi des mailles : $E = u_{R 1} + u_{C, \text{eq}}$.
1. $u_{R 1} = R_1 i$ et $i = C_\text{eq} {\displaystyle \frac{\mathrm{d} u_{C, \text{eq}}}{\mathrm{d} t}}$, donc $R_1 C_\text{eq} {\displaystyle \frac{\mathrm{d} u_{C, \text{eq}}}{\mathrm{d} t}} + u_{C, \text{eq}} = E$.
1. ${\displaystyle \frac{\mathrm{d} u_{C, \text{eq}}}{\mathrm{d} t}} = {\displaystyle \frac{E}{\tau_\text{charge}}} e^{-t / \tau_\text{charge}}$. En remplaçant : ${\displaystyle \frac{R_1 C_\text{eq}}{\tau_\text{charge}}} E e^{-t / \tau_\text{charge}} + E - E e^{-t / \tau_\text{charge}} = E$, ce qui est vrai pour tout $t$ si $\tau_\text{charge} = R_1 C_\text{eq}$.
1. Charge : $u_{C, \text{eq}} (\tau) = 0{,}63 E$.

   **A.N.** $0{,}63 \times \pu{40 kV} = \pu{25 kV}$, lu à $\tau_\text{charge} = \pu{0,10 s}$. Alors $C_\text{eq} = {\displaystyle \frac{\tau_\text{charge}}{R_1}} = {\displaystyle \frac{\pu{0,10 s}}{{160 \times 10^{3}\ \pu{\Omega}}}} = {6{,}3 \times 10^{-7}\ \pu{F}} = {6{,}3 \times 10^{2}\ \pu{nF}}$.
1. $n = {\displaystyle \frac{C_\text{eq}}{C}} = {\displaystyle \frac{\pu{630 nF}}{\pu{200 nF}}} \approx 3$ : trois condensateurs ont été utilisés. L'écart avec $3 \times \pu{200 nF} = \pu{600 nF}$ vient de la précision de la lecture graphique.
1. $q(t) = C_\text{eq} u_{C, \text{eq}} (t) = C_\text{eq} E (1 - e^{-t / \tau_\text{charge}})$. Elle tend vers $q_\text{max} = C_\text{eq} E$.

   **A.N.** $q_\text{max} = {600 \times 10^{-9}\ \pu{F}} \times {40 \times 10^{3}\ \pu{V}} = {2{,}4 \times 10^{-2}\ \pu{C}}$.
1. $i(t) = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}} = {\displaystyle \frac{C_\text{eq} E}{\tau_\text{charge}}} e^{-t / \tau_\text{charge}} = {\displaystyle \frac{E}{R_1}} e^{-t / \tau_\text{charge}}$.

   **A.N.** $i(0) = {\displaystyle \frac{{40 \times 10^{3}\ \pu{V}}}{{160 \times 10^{3}\ \pu{\Omega}}}} = \pu{0,25 A}$.
1. **A.N.** $W_\text{max} = {\displaystyle \frac{1}{2}} \times {600 \times 10^{-9}\ \pu{F}} \times ({40 \times 10^{3}\ \pu{V}})^2 = \pu{480 J}$.

   Comme $u_C = {\displaystyle \frac{q}{C_\text{eq}}}$ : $W = {\displaystyle \frac{1}{2}} C_\text{eq} ({\displaystyle \frac{q}{C_\text{eq}}})^2 = {\displaystyle \frac{q^2}{2 C_\text{eq}}}$.

   **A.N.** $W_\text{max} = {\displaystyle \frac{({2{,}4 \times 10^{-2}\ \pu{C}})^2}{2 \times {600 \times 10^{-9}\ \pu{F}}}} = \pu{480 J}$. On retrouve la même valeur.
1. $R_2 C_\text{eq} = \pu{100 \Omega} \times {600 \times 10^{-9}\ \pu{F}} = \pu{60 \mu s}$.

   **A.N.** $u_{C, \text{eq}} (\Delta t) = \pu{40 kV} \times e^{-12 / 60} = \pu{33 kV}$.
1. **A.N.** $q = C_\text{eq} u_{C, \text{eq}} = {600 \times 10^{-9}\ \pu{F}} \times {32{,}7 \times 10^{3}\ \pu{V}} = {2{,}0 \times 10^{-2}\ \pu{C}}$.

   Charge écoulée : $\Delta q = q_\text{max} - q = {2{,}4 \times 10^{-2}\ \pu{C}} - {1{,}96 \times 10^{-2}\ \pu{C}} = {4{,}4 \times 10^{-3}\ \pu{C}}$.

   **A.N.** $I_\text{moy} = {\displaystyle \frac{\Delta q}{\Delta t}} = {\displaystyle \frac{{4{,}4 \times 10^{-3}\ \pu{C}}}{{12 \times 10^{-6}\ \pu{s}}}} = {3{,}6 \times 10^{2}\ \pu{A}}$. C'est plus de mille fois l'intensité du début de la charge : la décharge dans l'eau, de faible résistance, est très rapide.
1. **A.N.** $W_\text{arc} = {\displaystyle \frac{1}{2}} \times {600 \times 10^{-9}\ \pu{F}} \times ({32{,}7 \times 10^{3}\ \pu{V}})^2 = {3{,}2 \times 10^{2}\ \pu{J}}$.
1. **A.N.** $\eta = {\displaystyle \frac{W_\text{arc}}{W_\text{max}}} = {\displaystyle \frac{\pu{322 J}}{\pu{480 J}}} = 0{,}67 = \pu{67 \%}$.

   Un tiers de l'énergie stockée est perdu dans l'eau pendant la pré-décharge, avant même la création de l'arc. On remarque que $\eta = ({\displaystyle \frac{u_{C, \text{eq}}}{E}})^2 = e^{-0{,}4}$ : l'énergie diminue plus vite que la tension, car elle dépend de son carré.
{{< /solution >}}

{{< note success "À l'issue de cette planche, je sais…" >}}
- Je sais utiliser $i = {\displaystyle \frac{\mathrm{d} q}{\mathrm{d} t}}$ et $q = C u_C$ pour calculer une charge, une intensité ou une durée, et exprimer la charge $q(t)$ d'une armature (exercices 1 et 9).
- Je sais calculer l'énergie stockée par un condensateur à l'aide de la relation fournie $W = {\displaystyle \frac{1}{2}} C u_C^2$, et l'exprimer en fonction de la charge (exercice 9).
- Je sais citer des ordres de grandeur de capacités et expliquer l'effet de la surface et de l'écartement des armatures sur la capacité (exercices 2, 7 et 8).
- Je sais expliquer le principe d'un capteur capacitif : la grandeur mesurée modifie la capacité, donc $\tau$ (exercice 7).
- Je sais établir l'équation différentielle vérifiée par $u_C$ lors d'une charge et lors d'une décharge, quelle que soit la convention choisie sur le schéma (exercices 3, 4, 6, 7, 8 et 9).
- Je sais vérifier qu'une fonction est solution et utiliser la condition initiale ou finale pour déterminer les constantes (exercices 3, 4, 6, 7 et 8).
- Je sais déterminer $\tau$ graphiquement en choisissant 63 % ou 37 % selon que la courbe croît ou décroît, ou avec la tangente à l'origine (exercices 5, 6, 8 et 9).
- Je sais utiliser $5 \tau$ pour estimer la durée d'un régime transitoire (exercice 4).
- Je sais calculer une incertitude-type composée avec une relation fournie et comparer deux valeurs avec l'écart normalisé $z$ (exercices 5, 6 et 8).
{{< /note >}}
