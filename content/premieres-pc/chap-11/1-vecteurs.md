---
title: "Les vecteurs en Physique : application au vecteur vitesse"
subtitle: ""
author: ""
type: ""
date: 2021-03-17T08:33:45+04:00
draft: false
toc: true
tags: ["Vecteur", "Composantes d'un vecteur", "Projection", "Produit scalaire", "Addition de deux vecteurs", "Approximation d'une dérivée", "Tracé de vecteurs vitesses", "Simulation en Python", "Trajectoire"]
categories: ["Premières Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---


La mécanique, l'étude du mouvement des objets et des objets à l'origine de ce mouvement s'appuie sur le formalisme vectoriel. Il est donc nécessaire de bien le maîtriser afin de pouvoir se concentrer sur la physique.

## Vecteurs

{{% note tip %}}

#### Vecteur

Un **vecteur** est un objet mathématique qui possède trois caractéristiques&nbsp;:

- une *direction*&nbsp;;
- un *sens*&nbsp;;
- une *norme* (ou *longueur*).
On peut représenter un vecteur par un segment muni d'une flèche&nbsp;; la longueur du segment étant égale à la norme du vecteur.
{{% /note %}}

{{% note tip %}}

#### Propriétés des vecteurs

- On peut **sommer deux vecteurs**. *Le résultat est un nouveau vecteur*&nbsp;;
- On peut **multiplier un vecteur par un scalaire (nombre)**. *Le résultat est un  vecteur*.
{{% /note %}}

<div class="row" style=".row::after {
  content: ''; clear: both; display: table;">
  <div style="float: left; width: 50%; padding: 5px;">
    <img src="/terminales-pc/chap-7/chap-7-1-1.png" alt="" width="90%" />
<center><strong>Méthode du parallélogramme</strong></center>
  </div>
  <div style="float: left; width: 50%; padding: 5px;">
    <img src="/terminales-pc/chap-7/chap-7-1-2.png" alt="" width="75%" />
<center><strong>Méthode tête-queue</strong></center>
  </div>
</div>

- {{< remote "Étapes de la construction pour la méthode du parallélogramme" "https://ggbm.at/zgf6xn7b" >}}
- {{< remote "Étapes de la construction pour la méthode du parallélogramme" "https://ggbm.at/kjcnhtjj" >}}

{{% note warning %}}
La méthode du parallélogramme ne s'applique pas lorsque les deux vecteurs à sommer sont colinéaires.
{{% /note %}}

{{% note normal %}}
{{< remote "Document au format pdf pour les exercices" "/terminales-pc/chap-7/chap-7-1-12.pdf">}}
{{% /note %}}

{{% note exercise %}}

#### Exercice 1

Pour chacune des situations présentées ci-dessous, construire les vecteurs $\vec{a} + \vec{b}$, $\vec{a} - \vec{b}$, $2\vec{a} + \vec{b}$, $\dfrac{1}{2}(\vec{a} + \vec{b})$.
{{% /note %}}

<img src="/terminales-pc/chap-7/chap-7-1-11.png" alt="" width="100%" />

{{% solution "Solutions" %}}
{{< remote "Solution avec Geogebra" "https://www.geogebra.org/m/vue4xavk" >}}
{{% /solution %}}

## Vecteurs en physique

{{% note tip %}}
En physique, on *modélise* les grandeurs dont la description nécessite la donnée d'une **direction**, d'un **sens**, d'une **valeur** par un vecteur.

Les grandeurs modélisée étant de *différentes natures*, quelques adaptations sont nécessaires par rapport à une utilisation des vecteurs purement mathématique&nbsp;:

- Il peut être nécessaire de préciser un **point d'application**&nbsp;;
- On ne parle plus de *norme ou longueur* d'un vecteur mais de **valeur** car cette dernière est **dimensionnée** (**unités&nbsp;:** *mètre pour un vecteur position*, *mètre par seconde pour un vecteur vitesse*, *newton pour un vecteur force*, etc.).
- La représentation d'un vecteur nécessite la définition et l'affichage de l'**échelle** utilisée.
{{% /note %}}

{{% note warning %}}
**Attention !** *Il est nécessaire de définir une échelle distincte pour chaque type de grandeur représentée.*
{{% /note %}}

{{% note exercise %}}

#### Exercice 2

Un solide indéformable de masse $m = \pu{30 kg}$ est posé, immobile, sur le sol. Une étude rapide montre que ce système est soumis à son poids $\overrightarrow{P}$ et à la réaction du sol $\overrightarrow{R}$.

On rappelle que le poids est modélisé par un vecteur de direction la verticale du lieu, dirigé vers la Terre et de valeur $P = mg$ où l'intensité du champ de pesanteur sera prise égale à $g = \pu{10 N.kg-1}$.

1. Représenter le vecteur $\overrightarrow{P}$ sur le schéma, sachant que son point d'application est le centre d'inertie de l'objet $G$.
**Indiquer l'échelle utilisée.**
2. L'objet étant immobile dans le référentiel terrestre *que l'on peut ici considérer galiléen*, la première loi de Newton nous indique qu'il est soumis à un ensemble d'interactions qui se compensent (il est **pseudo-isolé**). On peut traduire cette affirmation par la relation mathématique suivante&nbsp;: $$\overrightarrow{P} + \overrightarrow{R} = \overrightarrow{0}$$
Déterminer les caractéristiques du vecteur $\overrightarrow{R}$.
3. Représenter le vecteur $\overrightarrow{R}$ sur le schéma, sachant que son point d'application est le centre de la surface de contact entre l'objet et le sol.
{{% /note %}}

<img src="/terminales-pc/chap-7/chap-7-1-3.png" alt="" width="45%" />

{{% solution "Réponses" %}}
{{< remote "Solution utilisant Geogebra" "https://www.geogebra.org/m/qu7kumap" >}}
{{% /solution %}}

## Composantes d'un vecteur

{{% note tip %}}

#### Projection d'un vecteur sur un axe

La *projection d'un vecteur sur un **axe orienté*** est une opération au cours de laquelle on cherche à déterminer la **longueur algébrique** (**mesure algébrique**) de ce vecteur sur l'axe.
Une projection est dite **orthogonale** *si la droite sur laquelle on projette et la direction de projection sont orthogonales*.

<img src="/terminales-pc/chap-7/chap-7-1-4.png" alt="" width="55%" />

L'opérateur mathématique permettant de réaliser une projection est le **produit scalaire**.

Si $\vec{u}$ est un vecteur unitaire de la droite $(x'x)$ sur laquelle on projette orthogonalement le vecteur, la projection orthogonale $a_x$ est&nbsp;:

<div class="row" style=".row::after {
  content: ''; clear: both; display: table;">
  <div style="float: left; width: 50%; padding: 5px;">
    <img src="/terminales-pc/chap-7/chap-7-1-5.png" alt="" width="95%" />
$$
\begin{aligned}
a_x &= \vec{a}\cdot\vec{u} \cr
&= \Vert \vec{a} \Vert \times \Vert \vec{u} \Vert \times \cos(\theta) \cr
&= \Vert \vec{a} \Vert \times \cos(\theta) \cr
&> 0
\end{aligned}
$$
  </div>
  <div style="float: left; width: 50%; padding: 5px;">
    <img src="/terminales-pc/chap-7/chap-7-1-6.png" alt="" width="95%" />
$$
\begin{aligned}
a_x &= \vec{a}\cdot\vec{u} \cr
&= \Vert \vec{a} \Vert \times \Vert \vec{u} \Vert \times \cos(\theta) \cr
&= \Vert \vec{a} \Vert \times \cos(\theta) \cr
&< 0
\end{aligned}
$$
  </div>
</div>
{{% /note %}}

{{% note tip %}}

#### Composantes d'un vecteur

On appelle composantes (coordonnées) d'un vecteur le doublet (à 2D) ou le triplet (à 3D) de scalaires représentant les valeurs des projections de ce vecteur sur les directions des vecteurs du repère de référence.
<img src="/terminales-pc/chap-7/chap-7-1-7.png" alt="" width="45%" />  

$$
\vec{v} = \left(
\begin{aligned}
v_x &= v \cos(\theta) \cr
v_y &= v \sin(\theta) \cr
\end{aligned}
\right)
$$

{{% /note %}}

{{% note exercise %}}

#### Exercice 3

Trouver la valeur des composantes, dans le repère $(O; \vec{i}, \vec{j})$, d'un vecteur force de valeur $\pu{20 N}$ faisant un angle de $\text{60°}$ avec l'axe $(Ox)$.
{{% /note %}}

{{% solution "Réponse" %}}

{{% /solution %}}

{{% note exercise %}}

#### Exercice 4

Déterminer les composantes de la résultante (somme) des trois forces représentées sur le graphique.
<img src="/terminales-pc/chap-7/chap-7-1-8.png" alt="" width="45%" />
{{% /note %}}

{{% solution "Réponse" %}}

{{% /solution %}}

## Vecteur vitesse à partir de données expérimentales

{{% note tip %}}

#### Vecteur vitesse

La vitesse, à la date $t$, d'un système, **dans un référentiel donné**, est définie par $$\vec{v}(t) = \lim_{\Delta t \to 0} \dfrac{\overrightarrow{OM}(t + \Delta t) - \overrightarrow{OM}(t)}{\Delta t}  = \dfrac{\mathrm{d} \overrightarrow{OM} }{ \mathrm{dt} }$$
C'est donc un vecteur dont les caractéristiques sont&nbsp;:

- **Direction&nbsp;:** droite tangente à la trajectoire, à la position du système à la date $t$&nbsp;;
- **Sens&nbsp;:** celui du mouvement&nbsp;;
- **Valeur&nbsp;:** $v(t) = \left\Vert \dfrac{\mathrm{d} \overrightarrow{OM} }{ \mathrm{dt} }   \right\Vert$.
{{% /note %}}

Lorsque les équations horaires ne sont pas connues --- *c'est le cas pour tous les enregistrement expérimentaux* ---, on ne peut pas déterminer la dérivée de la position et on doit se contenter de **rechercher un vecteur vitesse approché**.

Si on observer l'expression du paragraphe précédent, on se rend compte que la difficulté pour calculer la dérivée dans ce cas de figure est l'impossibilité de passer à la limite&nbsp;: **impossible de considérer $\Delta t \to 0$ !**

La première idée consiste à écrire
$$\vec{v}(t) \approx \dfrac{\overrightarrow{OM}(t + \Delta t) - \overrightarrow{OM}(t)}{\Delta t} $$
soit
$$\vec{v}(t_i) \approx \dfrac{\overrightarrow{OM_{i+1}} - \overrightarrow{OM_{i}}}{t_{i+1}-t_{i}} = \dfrac{\overrightarrow{M_iM_{i+1}}}{t_{i+1}-t_{i}} $$

On montre cependant que

{{% note tip %}}

#### Détermination du vecteur vitesse à partir de données expérimentales

La meilleure approximation pour le vecteur vitesse au point $A_i$ à la date $t_i$ est&nbsp;:
$$
\vec{v}(A_i) \approx \dfrac{\overrightarrow{A_{i-1}A_{i+1}}}{t_{i+1}-t_{i-1}}
$$
Les vecteurs $\vec{v}(A_i)$ et $\overrightarrow{A_{i-1}A_{i+1}}$ sont <strong>colinéaires</strong>, ils ont <strong>même direction</strong> et <strong>même sens</strong> (puisque le coefficient de colinéarité est positif). On peut donc en déduire que&nbsp;:
$$
v(A_i) \approx \dfrac{A_{i-1}A_{i+1}}{t_{i+1}-t_{i-1}}
$$
{{% /note %}}

{{% note warning %}}
La déduction finale qui a permis de passer de la relation vectorielle à la relation scalaire **n'est valable que parce que les vecteur sont colinéaires et de même sens**. Il faut toujours prendre le temps de la réflexion lors du passage d'une relation vectorielle à une relation scalaire. **La valeur de la somme de deux vecteurs n'est généralement pas égale à la somme des valeurs de chacun des vecteurs !**
{{% /note %}}

{{% note warning %}}
L'étude menée dans cette partie n'est pas limitée à la vitesse ! **Elle concerne la dérivation de toute grandeur vectorielle déterminée à partir de données expérimentales**.
{{% /note %}}

{{% note exercise %}}

#### Exercice 5

On a enregistré la position d'un mobile toutes les $\pu{50 ms}$ sur une table à coussin d'air. Une partie de la trajectoire ainsi obtenue est affichée ci-dessous.
L'échelle des **longueurs** est la suivante (document - réalité)&nbsp;: $\pu{1 cm} \longleftrightarrow \pu{1 cm}$.

1. Est-il possible, en utilisant la formule donnée dans le document ci-dessus, de déterminer les vecteurs vitesses $\vec{v}(A_0)$ et $\vec{v}(A_6)$&nbsp;? Pourquoi&nbsp;?
2. Calculer les valeurs du vecteur vitesse du mobile aux points $A_1$, $A_3$ et $A_5$.
3. Représenter les vecteurs vitesses aux points $A_1$, $A_3$ et $A_5$.
4. Le mouvement est-il uniforme&nbsp;?

On s'intéresse à la variation du vecteur vitesse alors que le mobile se trouve au point $A_2$. On peut définir cette variation de la sorte&nbsp;:
$$
\Delta \vec{v}(A_2) = \vec{v}(A_3) - \vec{v}(A_1)
$$

5. Déterminer les caractéristiques du vecteur «&nbsp;variation du vecteur vitesse&nbsp;» $\Delta \vec{v}(A_2)$ au point $A_2$ et le représenter.
6. Même question au point $A_4$.
7. Ces deux dernières questions confirment-elles la réponse à la question 4.&nbsp;?
{{% /note %}}

<img src="/terminales-pc/chap-7/chap-7-1-10.png" alt="" width="100%" />

{{% solution "Correction" %}}
{{< remote "Solution sous forme de simulation" "https://www.geogebra.org/m/atg9wdgv" >}}
{{% /solution %}}

{{% note exercise %}}

#### Exercice 6 : Rotation autour d'un axe fixe à l'aide d'un fil inextensible

Un mobile autoporteur relié à un point fixe $O$ par un fil inextensible, est lancé sur une table. Les positions successives de son centre d'inertie $G$ sont enregistrées à intervalles de temps réguliers $\Delta t = \pu{40 ms}$ (échelle des longueurs : $\pu{1 cm} \longleftrightarrow \pu{1 cm}$).

<img src="/premieres-pc/chap-11/chap-11-1/chap-11-1-1.png" alt="" width="80%" />

<img src="/premieres-pc/chap-11/chap-11-1/chap-11-1-2.png" alt="" width="60%" />

{{% note warning %}}
{{<remote "Positions du mobile au cours de son mouvement (document à imprimer)" "/premieres-pc/chap-11/chap-11-1/chap-11-1-3.pdf" >}}
{{% /note %}}

1. Quelle est la nature de la trajectoire de $G$ ?
2. Définir le vecteur vitesse $\vec{v}(A_2)$.
3. Déterminer la valeur de la vitesse $v_(A_2)$.
4. Représenter $\vec{v}(A_2)$ sur la feuille. **Indiquer l'échelle utilisée**.
5. Mêmes questions pour le point $A_3$.
6. Au point $A_2$, construire $\Delta \vec{v}(A_2) = \vec{v}(A_3) - \vec{v}(A_1)$.
7. Déterminer $|| \Delta \vec{v}(A_2) ||$ graphiquement.
8. Tracer la direction de la résultante (somme) des forces qui agissent sur le mobile lorsqu'il se situe au point $A_2$. Quelle remarque peut-on formuler ?
9. Au point $A_8$, construire $\Delta \vec{v}(A_8) = \vec{v}(A_9) - \vec{v}(A_7)$ et déterminer $|| \Delta \vec{v}(A_8) ||$ graphiquement.
10. Tracer, au point $A_8$, la résultante des forces qui agissent sur le mobile. Quelle remarque peut-on formuler ?
11. Qualifier le mouvement.
{{% /note %}}

{{% solution "Correction" %}}

{{< remote "Toutes les constructions de l'exercice." "/premieres-pc/chap-11/chap-11-1/chap-11-1-4.pdf">}}

{{% /solution %}}

{{% note exercise %}}

#### Exercice 7 : Viaduc de Millau

{{% remote "Accès à l'activité" "https://dlatreyte.github.io/jupyter-lite/lab?path=prem-pc%2Fmecanique%2Fviaduc-millau-eleves.ipynb" %}}

{{% /note %}}

{{% solution "Correction" %}}
{{< remote "Corrigé en ligne" "https://dlatreyte.github.io/jupyter-lite/lab?path=prem-pc%2Fmecanique%2Fviaduc-millau.ipynb" >}}
{{% /solution %}}

## Exercice

{{% note exercise %}}

#### Exercice 8

Un homme tire une valise reposant sur le sol (horizontal), **à vitesse constante** et **en ligne droite**, en tirant sur une corde attachée à cette valise. L'homme exerce une force constante sur la corde de valeur $\pu{300 N}$&nbsp;; la corde fait un angle de $\text{20°}$ avec l'horizontale.

1. Déterminer les composantes horizontale et verticale de la valeur de la force que l'homme exerce sur la valise.
2. Après analyse du problème et utilisation du principe de l'inertie, déterminer le poids de la valise puis en déduire sa masse.

**Rappel.** $g=\pu{9,81 m.s-2}$.
{{% /note %}}
