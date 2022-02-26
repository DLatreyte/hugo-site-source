---
title: "Les vecteurs en physique"
subtitle: "Chapitre 8,1"
author: ""
type: ""
date: 2020-11-27T15:24:37+04:00
draft: false
toc: true
tags: ["Vecteur", "Composantes d'un vecteur", "Projection", "Produit scalaire", "Addition de deux vecteurs", "Approximation d'une dérivée", "Tracé de vecteurs vitesses", "Simulation en Python", "Trajectoire"]
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
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
Pour chacune des situations présentées ci-dessous, construire les vecteurs $\vec{a} + \vec{b}$, $\vec{a} - \vec{b}$, $2 \vec{a} + \vec{b}$, $\dfrac{1}{2}(\vec{a} + \vec{b})$.
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

Si $\vec{u}$ est un **vecteur unitaire** de la droite $(x'x)$ sur laquelle on projette orthogonalement le vecteur, la projection orthogonale $a_x$ est&nbsp;:

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
\vec{v} \ \left(
\begin{aligned}
v_x &= v \cos(\theta) \cr
v_y &= v \sin(\theta) \cr
\end{aligned}
\right)
$$

{{% /note %}}

{{% note exercise %}}
Trouver la valeur des composantes, dans le repère $(O; \vec{i}, \vec{j})$, d'un vecteur force de valeur $\pu{20 N}$ faisant un angle de $\text{60°}$ avec l'axe $(Ox)$.
{{% /note %}}

{{% solution "Réponse" %}}

{{% /solution %}}

{{% note exercise %}}
Déterminer les composantes de la résultante (somme) des trois forces représentées sur le graphique.
<img src="/terminales-pc/chap-7/chap-7-1-8.png" alt="" width="45%" />
{{% /note %}}

{{% solution "Réponse" %}}

{{% /solution %}}

{{% note exercise %}}
Un bob-sleigh descend une pente inclinée à $\text{30°}$ par rapport à l'horizontale avec une accélération constante égale à $\pu{4 m.s-2}$.
<img src="/terminales-pc/chap-7/chap-7-1-9.png" alt="" width="70%" />
Déterminer les composantes du vecteur accélération dans le repère $(O; \vec{i}, \vec{j})$.
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
La meilleure approximation pour le vecteur vitesse au point $M_i$ à la date $t_i$ est&nbsp;:
$$
\vec{v}(M_i) \approx \dfrac{\overrightarrow{M_{i-1}M_{i+1}}}{t_{i+1}-t_{i-1}}
$$	
Les vecteurs $\vec{v}(M_i)$ et $\overrightarrow{M_{i-1}M_{i+1}}$ sont <strong>colinéaires</strong>, ils ont <strong>même direction</strong> et <strong>même sens</strong> (puisque le coefficient de colinéarité est positif). On peut donc en déduire que&nbsp;:
$$
v(M_i) \approx \dfrac{M_{i-1}M_{i+1}}{t_{i+1}-t_{i-1}}
$$
{{% /note %}}

{{% note warning %}}
La déduction finale qui a permis de passer de la relation vectorielle à la relation scalaire **n'est valable que parce que les vecteur sont colinéaires et de même sens**. Il faut toujours prendre le temps de la réflexion lors du passage d'une relation vectorielle à une relation scalaire. **La valeur de la somme de deux vecteurs n'est généralement pas égale à la somme des valeurs de chacun des vecteurs !**
{{% /note %}}

{{% note warning %}}
L'étude menée dans cette partie n'est pas limitée à la vitesse ! **Elle concerne la dérivation de toute grandeur vectorielle déterminée à partir de données expérimentales**.
{{% /note %}}

{{% note exercise %}}
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

{{% solution "Solution" %}}
{{< remote "Solution sous forme de simulation" "https://www.geogebra.org/m/atg9wdgv" >}}
{{% /solution %}}

{{% note exercise %}}
On lance horizontalement une pierre dense et de petit volume du haut du viaduc de Millau, en France. La chute est filmée à l'aide d'une caméra. À l'aide d'un logiciel de pointage on obtient les valeurs suivantes pour l'altitude et la distance parcourue horizontalement par l'objet au cours du temps&nbsp;:

| **Date (s)** | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|:----:|
| **Altitude (m)** |343|338|323|299|265|220|166|103|29|
| **Distance horizontale parcourue (m)** | 0 | 10 | 20 | 30 | 40 | 50 | 60 | 70 | 80 |

On code un programme dans le langage Python afin de pouvoir répondre aux questions suivantes&nbsp;:

1. Quelle est la hauteur du parapet du pont de Millau&nbsp;?
2. Avec quelle vitesse la pierre a-t-elle été lancée&nbsp;?

Une partie du code nécessaire à l'étude de ce mouvement se trouve {{< remote "à cet emplacement" "https://repl.it/@dlatreyte/Trace-de-vecteurs-vitesses-Eleves" >}}

3. Compléter les lignes 47 à 50.

4. Quels arguments (type et signification) la fonction `affichage` attend-elle&nbsp;? Quels sont ceux qui sont obligatoires, optionnels&nbsp;?

5. Quelle instruction permet de réaliser l'affichage $y=f(x)$&nbsp;?

5. Retirer le commentaire de la ligne 55 et lancer le programme.    
Caractériser l'évolution de l'altitude $z$ au cours du temps.

6. Sur le modèle de la question précédente, afficher et caractériser l'évolution de la distance parcourue horizontalement, $x$, au cours du temps.

7. Toujours sur le même modèle (on pourra aussi étudier la ligne 66), afficher la trajectoire $z=f(x)$.

8. Retirer les commentaires des lignes 41 à 44.

9. Compléter la ligne 42. Il s'agit ici d'entrer l'instruction qui permet de calculer une valeur approchée de la vitesse.

10. Détailler l'instruction à la ligne 41.

11. Compléter les lignes 59 et 60, de façon à posséder les listes des valeurs des vitesses $v_x$ et $v_z$ (à l'éxception de la dernière valeur).

12. Retirer les commentaires des lignes 62 et 63 et lancer le programme.

13. Comment évoluent les vitesses $v_x$ et $v_z$ au cours du temps&nbsp;? Était-ce prévisible&nbsp;?

14. Retirer le commentaire de la ligne 66. Les vecteurs vitesse affichés présentent-ils bien les caractéristiques annoncées dans la section 4. de ce document&nbsp;?
{{% /note %}}

{{% solution "Correction" %}}
{{< remote "Programme complété sur repl.it" "https://repl.it/@dlatreyte/Trace-de-vecteurs-vitesses" >}}
{{% /solution %}}

## Exercices

{{% note exercise %}}
Un homme tire une valise reposant sur le sol (horizontal), **à vitesse constante** et **en ligne droite**, en tirant sur une corde attachée à cette valise. L'homme exerce une force constante sur la corde de valeur $\pu{300 N}$&nbsp;; la corde fait un angle de $\text{20°}$ avec l'horizontale.
1. Déterminer les composantes horizontale et verticale de la valeur de la force que l'homme exerce sur la valise.
2. Après analyse du problème et utilisation du principe de l'inertie, déterminer le poids de la valise puis en déduire sa masse.

**Rappel.** $g=\pu{9,81 m.s-2}$.
{{% /note %}}