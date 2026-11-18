---
title: "Étude expérimentale du dipôle (R, C)"
subtitle: "Doc. 5,3"
date: 2022-11-15T18:42:27+04:00
draft: false
toc: true
tags: ["dipôle RC", "constante de temps", "temps caractéristique", "charge", "décharge", "tangente à l'origine", "tolérance", "code des couleurs", "incertitude-type", "incertitude-type composée", "écart normalisé", "acquisition"]
categories: ["Physique", "Terminale Spé PC"]
solution_est_visible: true
auto_numbering: true
weight: 700
---
- {{< remote "Énoncé au format pdf" "/terminales-pc/chap-5/5-3/5-3-enonce.pdf" >}}
- {{< remote "Énoncé et réponses au format pdf" "/terminales-pc/chap-5/5-3/5-3-corrige.pdf" >}}

{{< note goal "Objectif" >}}
L'objectif de la séance est l'étude des différents paramètres qui influent sur le temps caractéristique du dipôle $(R, C)$ lors de la charge ou de la décharge du condensateur.
{{< /note >}}

## Documents

### Temps caractéristique

{{< note success "Temps caractéristique d'un dipôle $(R, C)$" >}}
- Le **temps caractéristique** (ou **constante de temps**) d'un dipôle $(R, C)$ a pour expression $\tau = R C$.
- Le temps caractéristique peut se déterminer comme *la durée au bout de laquelle la tension aux bornes du condensateur est égale à 63 % de sa valeur finale (maximale) **lors d'une charge***, ou comme *la durée au bout de laquelle la tension aux bornes du condensateur est égale à 37 % de sa valeur initiale **lors d'une décharge***.
- Le temps caractéristique peut aussi se déterminer comme *la durée au bout de laquelle la tangente à l'origine à la courbe de charge (ou de décharge) croise son asymptote horizontale*.
{{< /note >}}

Ces trois manières de déterminer le temps caractéristique sont liées à *une évolution exponentielle*, ou, de façon équivalente, à *un comportement décrit par une équation différentielle linéaire du premier ordre à coefficients constants*. *Elles peuvent donc être utilisées indifféremment à partir de la courbe d'évolution de l'intensité du courant ou de celle de la tension aux bornes du condensateur.*

### Tolérance

{{< note success "Tolérance" >}}
La valeur de la capacité d'un condensateur est accompagnée de sa tolérance. Si un condensateur est étiqueté « 1000 µF $\pm$ 20 % », alors sa capacité réelle est comprise entre 800 µF et 1200 µF.

Le principe est identique pour la résistance d'un conducteur ohmique.
{{< /note >}}

### Lecture de la valeur de la résistance d'un conducteur ohmique

{{< columns >}}
Le code des couleurs des résistances à quatre anneaux est simple : *trois couleurs expriment la valeur de la résistance et une couleur indique la tolérance*.

Positionner la résistance de façon à avoir l'anneau le plus proche de l'extrémité du corps de la résistance sur sa gauche (ou mettre l'anneau doré ou argenté sur sa droite), puis suivre l'exemple suivant :

![](/terminales-pc/chap-5/5-3/Doc-1.svg?width=40%)
{{< column >}}
![](/terminales-pc/chap-5/5-3/Doc-2.svg?width=35%)
{{< endcolumns >}}

### Incertitudes-types

{{< note success "Incertitude-type associée à une tolérance" >}}
Le fabricant garantit seulement que la valeur réelle se trouve quelque part dans l'intervalle $[m - a ; m + a]$, sans privilégier aucune valeur de cet intervalle. On note $a$ la **demi-étendue** de l'intervalle. On admet que l'incertitude-type associée vaut alors :
$$u = \frac{a}{\sqrt{3}}$$
*Exemple :* pour un condensateur étiqueté « 1000 µF $\pm$ 20 % », $a = 0{,}20 \times \pu{1000 \mu F} = \pu{200 \mu F}$.
{{< /note >}}

**Incertitude-type composée**

Lorsqu'une grandeur est le produit de deux grandeurs mesurées indépendamment, ses incertitudes relatives se combinent. Pour $\tau = R C$, on admet la relation :
$$\frac{u(\tau)}{\tau} = \sqrt{(\frac{u(R)}{R})^2 + (\frac{u(C)}{C})^2}$$

{{< note success "Comparer deux valeurs : l'écart normalisé" >}}
Pour comparer le résultat $m$ d'une mesure, d'incertitude-type $u(m)$, à une valeur de référence $m_\text{réf}$, on calcule l'**écart normalisé** (ou *z-score*) :
$$z = \frac{\left|m - m_\text{réf}\right|}{u(m)}$$
Le quotient $z$ indique combien d'incertitudes-types séparent les deux valeurs. On considère en général que les deux valeurs sont **compatibles** lorsque $z \leq  2$.
{{< /note >}}

## Travail à réaliser

### Valeur attendue de la constante de temps

{{< question >}}
Déterminer la valeur $R$ de la résistance fournie, ainsi que sa tolérance.
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Commencer par repérer l'anneau doré ou argenté : il indique la tolérance et se place à droite. Les deux premiers anneaux donnent les chiffres, le troisième donne le multiplicateur.
{{< /note >}}

{{< solution "Réponse" >}}
Les anneaux sont marron, noir, rouge et or : $R = 10 \times 10^2 \pu{\Omega} = {1{,}0 \times 10^{3}\ \pu{\Omega}}$, avec une tolérance de $\pm \pu{5 \%}$.
{{< /solution >}}

{{< question >}}
En déduire l'incertitude-type $u(R)$.
{{< /question >}}

{{< solution "Réponse" >}}
La demi-étendue de l'intervalle vaut $a = 0{,}05 \times R$.

**A.N.** $u(R) = {\displaystyle \frac{0{,}05 \times {1{,}0 \times 10^{3}\ \pu{\Omega}}}{\sqrt{3}}} = \pu{29 \Omega}$.
{{< /solution >}}

{{< question >}}
Déterminer la valeur $C$ de la capacité fournie. En déduire son incertitude-type $u(C)$.
{{< /question >}}

{{< solution "Réponse" >}}
$C = \pu{1000 \mu F} = {1{,}00 \times 10^{-3}\ \pu{F}}$, avec une tolérance de $\pm \pu{20 \%}$.

**A.N.** $u(C) = {\displaystyle \frac{0{,}20 \times {1{,}00 \times 10^{-3}\ \pu{F}}}{\sqrt{3}}} = {1{,}2 \times 10^{-4}\ \pu{F}}$.
{{< /solution >}}

{{< question >}}
Calculer la valeur de la constante de temps $\tau$ du dipôle $(R, C)$ constitué de la résistance et du condensateur fournis.
{{< /question >}}

{{< solution "Réponse" >}}
**A.N.** $\tau = R C = {1{,}0 \times 10^{3}\ \pu{\Omega}} \times {1{,}00 \times 10^{-3}\ \pu{F}} = \pu{1,0 s}$.
{{< /solution >}}

{{< question >}}
À l'aide de la relation d'incertitude-type composée, calculer l'incertitude-type $u(\tau)$.
{{< /question >}}

{{< solution "Réponse" >}}
$$u(\tau) = \tau \sqrt{(\frac{u(R)}{R})^2 + (\frac{u(C)}{C})^2}$$

**A.N.** $u(\tau) = \pu{1,0 s} \times \sqrt{({\displaystyle \frac{\pu{29 \Omega}}{{1{,}0 \times 10^{3}\ \pu{\Omega}}}})^2 + ({\displaystyle \frac{{1{,}2 \times 10^{-4}\ \pu{F}}}{{1{,}00 \times 10^{-3}\ \pu{F}}}})^2} = \pu{0,12 s}$.

On écrit le résultat : $\tau = \pu{1,0 s}$ avec $u(\tau) = \pu{0,12 s}$.
{{< /solution >}}

{{< question >}}
Laquelle des deux grandeurs, $R$ ou $C$, contribue le plus à l'incertitude-type sur $\tau$ ? Justifier.
{{< /question >}}

{{< solution "Réponse" >}}
L'incertitude relative sur $R$ vaut $0{,}029$, soit environ 3 % ; celle sur $C$ vaut $0{,}12$, soit 12 %. Les termes sont élevés au carré dans la racine : $0{,}029^2 \approx 0{,}0008$ contre $0{,}12^2 \approx 0{,}014$. Le condensateur contribue presque seul à l'incertitude sur $\tau$. Prendre une résistance plus précise ne changerait presque rien.
{{< /solution >}}

### Préparation du montage

On donne le schéma du montage expérimental :

![](/terminales-pc/chap-5/5-3/Doc-3.svg?width=65%)

> *Schéma du montage expérimental.*

{{< question >}}
Compléter le schéma en ajoutant un ampèremètre qui mesure l'intensité $i$ du courant électrique qui traverse le condensateur et un voltmètre qui mesure la tension $u_C$ à ses bornes. Préciser pour chacun s'il est branché en série ou en dérivation.
{{< /question >}}

{{< solution "Réponse" >}}
L'ampèremètre est branché **en série** avec le condensateur, dans la branche qui contient $R$ et $C$ : il doit être traversé par le même courant que le condensateur. Sa borne mA (ou A) est placée du côté où arrive le courant de charge, donc du côté de $R$.

Le voltmètre est branché **en dérivation** aux bornes du condensateur, entre $A$ et $B$, sa borne V reliée à $A$, conformément à la flèche de $u_C$.
{{< /solution >}}

- Réaliser le montage schématisé ci-dessus *avec l'interrupteur en position 1*, en incorporant l'ampèremètre et le voltmètre comme sur le schéma complété.

- Connecter l'ampèremètre et le voltmètre au logiciel « Graphical Analysis » et configurer ce dernier :
  - Basculer l'ampèremètre en mA (en bas et à droite de l'écran).
  - Acquisition (en bas et à gauche de l'écran) :
    - *Mode :* En fonction du temps.
    - *Rythme :* 100 mesures/s.
    - *Démarrer la mesure :* sur une valeur de déclenchement.
      - *Démarrer la mesure quand :* Tension augmente et passe par 0,1 V.
    - *Finir la mesure :* Après 15 s.

### Prévisions

Avant de lancer l'acquisition, on prévoit ce que l'on devrait observer, à l'aide de ce qui a été établi dans le Doc. 5,2.

{{< question >}}
Lors de la charge, esquisser l'allure attendue des courbes $u_C (t)$ et $i(t)$. Indiquer les valeurs de $u_C$ et de $i$ au début de la charge et lorsque la charge est terminée.
{{< /question >}}

{{< solution "Réponse" >}}
$u_C$ part de 0 (condensateur déchargé), croît de moins en moins vite et tend vers $E$.

$i$ passe brutalement de 0 à ${\displaystyle \frac{E}{R}}$ à la fermeture du circuit, puis décroît et tend vers 0, car $i = C \, {\displaystyle \frac{\mathrm{d} u_C}{\mathrm{d} t}}$ et la pente de $u_C (t)$ s'annule.
{{< /solution >}}

{{< question >}}
Lors de la décharge, avec le sens du courant indiqué par l'ampèremètre, quel sera le signe de l'intensité $i$ mesurée ? Justifier.
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Pendant la décharge, la charge $q_A$ de l'armature $A$ augmente-t-elle ou diminue-t-elle ? Relier le signe de $i = {\displaystyle \frac{\mathrm{d} q_A}{\mathrm{d} t}}$ à cette évolution.
{{< /note >}}

{{< solution "Réponse" >}}
Pendant la décharge, $q_A$ passe de $C E$ à 0 : elle diminue, donc $i = {\displaystyle \frac{\mathrm{d} q_A}{\mathrm{d} t}} < 0$. L'ampèremètre affichera une intensité négative. Le montage n'est pas faux : le courant circule simplement dans le sens opposé à celui de la charge.
{{< /solution >}}

{{< question >}}
Le protocole demande d'attendre 7 s environ avant de déclencher la décharge. Justifier cette durée à partir de la valeur calculée de $\tau$.
{{< /question >}}

{{< solution "Réponse" >}}
On a vu dans le Doc. 5,2 que la charge est pratiquement terminée (à plus de 99 %) au bout de $5 \tau$. Ici $5 \tau = 5 \times \pu{1,0 s} = \pu{5 s}$. Une durée de 7 s laisse donc au condensateur le temps de se charger complètement, avec une marge qui tient compte de l'incertitude sur $\tau$.
{{< /solution >}}

### Acquisition

- Lancer l'acquisition depuis le logiciel, puis basculer l'interrupteur en position 2. *Le condensateur doit se charger.*

- Attendre 7 s environ et basculer à nouveau l'interrupteur en position 1. *Le condensateur doit se décharger.*

{{< question >}}
Les courbes obtenues sont-elles conformes aux prévisions des questions précédentes ? Relever les éventuelles différences.
{{< /question >}}

{{< solution "Réponse" >}}
On observe pour la charge une courbe $u_C (t)$ croissante qui tend vers une valeur constante, et une intensité qui saute à sa valeur maximale puis décroît vers 0. Pour la décharge, $u_C (t)$ décroît vers 0, et $i$ devient brutalement négative, puis tend vers 0. Ces observations sont conformes aux prévisions.
{{< /solution >}}

### Détermination expérimentale de $\tau$

{{< question >}}
Sur la courbe de charge $u_C (t)$, déterminer $\tau$ par la méthode des 63 %. 
{{< /question >}}

{{< solution "Réponse" >}}
On lit la valeur finale $E$ de $u_C$, on calcule $0{,}63 E$, puis on lit l'abscisse du point de la courbe d'ordonnée $0{,}63 E$. On attend une valeur proche de 1,0 s.
{{< /solution >}}

{{< question >}}
Sur la courbe $i(t)$ de la charge, quel pourcentage de la valeur initiale faut-il chercher pour lire $\tau$ ? Déterminer $\tau$ par cette méthode.
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Pendant la charge, $i(t)$ a-t-elle l'allure d'une courbe de charge ou de décharge ? Le document « Temps caractéristique » indique quel pourcentage utiliser dans chaque cas.
{{< /note >}}

{{< solution "Réponse" >}}
Pendant la charge, $i(t) = {\displaystyle \frac{E}{R}} \, e^{-t / \tau}$ décroît comme une tension de décharge. Il faut donc chercher la date à laquelle $i = 0{,}37 \times {\displaystyle \frac{E}{R}}$, et non 63 % : $i(\tau) = {\displaystyle \frac{E}{R}} \, e^{-1} \approx 0{,}37 \times {\displaystyle \frac{E}{R}}$. Prendre 63 % ici est une erreur fréquente.
{{< /solution >}}

{{< question >}}
Sur la courbe de décharge $u_C (t)$, déterminer $\tau$ par la méthode de la tangente à l'origine.
{{< /question >}}

{{< solution "Réponse" >}}
On trace la tangente à la courbe au début de la décharge. Elle coupe l'asymptote horizontale $u = 0$ en un point dont l'abscisse, comptée à partir du début de la décharge, vaut $\tau$. On attend une valeur proche de 1,0 s.
{{< /solution >}}

{{< question >}}
Les valeurs obtenues par les différentes méthodes sont-elles cohérentes entre elles ? On note $\tau_\text{exp}$ leur moyenne.
{{< /question >}}

{{< solution "Réponse" >}}
Les trois valeurs doivent être proches, à la précision de lecture près, car elles mesurent le même temps caractéristique. On calcule leur moyenne $\tau_\text{exp}$.
{{< /solution >}}

{{< question >}}
On prend $\tau_\text{exp}$ comme valeur de référence, car l'incertitude de lecture sur la courbe est bien plus faible que $u(\tau)$. Calculer l'écart normalisé entre la valeur calculée de $\tau$ et $\tau_\text{exp}$. Conclure.
{{< /question >}}

{{< solution "Réponse" >}}
$$z = \frac{\left|\tau - \tau_\text{exp}\right|}{u(\tau)}$$
*Exemple :* si $\tau_\text{exp} = \pu{0,92 s}$.

**A.N.** $z = {\displaystyle \frac{\left|\pu{1,0 s} - \pu{0,92 s}\right|}{\pu{0,12 s}}} = 0{,}7$.

Comme $z \leq  2$, la valeur calculée à partir des indications du fabricant est compatible avec la valeur mesurée. Si on trouve $z > 2$, il faut chercher une cause : erreur de lecture du code des couleurs, résistance de l'ampèremètre non négligeable, condensateur vieilli dont la capacité est sortie de sa tolérance.
{{< /solution >}}

### Influence des paramètres sur $\tau$

{{< question >}}
D'après l'expression de $\tau$, la constante de temps dépend-elle de la tension $E$ du générateur ?
{{< /question >}}

{{< solution "Réponse" >}}
$\tau = R C$ ne fait pas intervenir $E$ : la durée de charge ne dépend pas de la tension du générateur. Un générateur de tension plus élevée charge le condensateur à une tension finale plus grande, dans le même temps.
{{< /solution >}}

{{< question >}}
Prédire comment varie $\tau$ si l'on remplace la résistance par une résistance $R'$ plus grande.
{{< /question >}}

{{< solution "Réponse" >}}
$\tau$ est proportionnelle à $R$ : avec $R' > R$, la constante de temps $\tau' = R' C$ est plus grande, la charge et la décharge sont plus lentes.
{{< /solution >}}

{{< question >}}
Remplacer la résistance par la résistance $R'$ fournie par le professeur. Calculer la nouvelle constante de temps $\tau'$, puis la durée minimale de charge à respecter avant de basculer l'interrupteur. Adapter si besoin la durée d'acquisition.
{{< /question >}}

{{< solution "Réponse" >}}
$\tau' = R' C$. La charge est pratiquement terminée au bout de $5 \tau'$ : il faut attendre au moins cette durée avant la décharge, et choisir une durée d'acquisition supérieure à $10 \tau'$ pour enregistrer la charge et la décharge complètes.
{{< /solution >}}

- Réaliser une nouvelle acquisition avec la résistance $R'$.

{{< question >}}
Déterminer $\tau'_\text{exp}$ par la méthode de votre choix. Comparer le rapport ${\displaystyle \frac{\tau'_\text{exp}}{\tau_\text{exp}}}$ au rapport ${\displaystyle \frac{R'}{R}}$. Conclure.
{{< /question >}}

{{< solution "Réponse" >}}
Si $\tau$ est proportionnelle à $R$, les deux rapports sont égaux, aux incertitudes près. L'expérience confirme alors que $\tau$ est proportionnelle à $R$, la capacité restant la même.
{{< /solution >}}

{{< note success "À l'issue de cette activité, je sais…" >}}
- Je sais lire la valeur de la résistance d'un conducteur ohmique et sa tolérance à l'aide du code des couleurs.
- Je sais calculer l'incertitude-type $u = a / \sqrt{3}$ associée à une tolérance du fabricant.
- Je sais calculer la constante de temps $\tau = R C$ d'un dipôle $(R, C)$ et son incertitude-type à l'aide d'une relation d'incertitude-type composée fournie.
- Je sais identifier la grandeur qui contribue le plus à l'incertitude-type d'un résultat.
- Je sais brancher un ampèremètre en série et un voltmètre en dérivation pour mesurer $i$ et $u_C$.
- Je sais prévoir l'allure de $u_C (t)$ et de $i(t)$ lors de la charge et de la décharge, et le signe de $i$ pendant la décharge.
- Je sais choisir une durée de charge à partir de $5 \tau$.
- Je sais déterminer graphiquement $\tau$ par la méthode des 63 %, des 37 % ou de la tangente à l'origine, en choisissant le pourcentage adapté à une courbe croissante ou décroissante.
- Je sais comparer deux valeurs à l'aide de l'écart normalisé $z$.
- Je sais que $\tau$ ne dépend pas de $E$ et qu'il est proportionnel à $R$.
{{< /note >}}
