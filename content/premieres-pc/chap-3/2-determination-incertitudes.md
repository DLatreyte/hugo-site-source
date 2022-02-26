---
title: "Détermination pratique des incertitudes"
subtitle: "Chapitre 3,2"
author: ""
type: ""
date: 2020-10-07T07:51:11+04:00
draft: false
toc: true
tags: ["Erreurs", "Incertitudes"]
categories: ["Premières Spé PC", "Physique"]
image: ""
solution_est_visible: true
auto_numbering: true
---
[^1]: $U(m)$ est l'incertitude sur la mesure.

{{% note warning %}}
#### Avertissement. 
Aucune des formules présentées dans ce document ne doit être apprise par cœur car **elles seront systématiquement données si nécessaire**.

En revanche, il faudra être capable de choisir la formule à utiliser et il sera impératif de savoir l'utiliser.
{{% /note %}}


Le résultat d'une mesure *n'est pas une valeur mais un intervalle de valeurs*, que l'on note $\pu{m±U(m)}$[^1], dans lequel on peut considérer, *avec un certain niveau de confiance*, que la «&nbsp;valeur vraie&nbsp;» se trouve.

{{% note normal %}}
Comment détermine-t-on $U(m)$ en pratique&nbsp;?
{{% /note %}}

## Quelle stratégie mettre en œuvre lors du calcul d'une incertitude&nbsp;?

{{% note tip %}}
Lors du calcul d'une incertitude trois cas de figure peuvent se présenter&nbsp;:

1. L'incertitude porte sur une **mesure expérimentale que l'on peut répéter 
  plusieurs fois**&nbsp;: *on parle d'incertitude de **type A***&nbsp;;
2. L'incertitude porte sur une **mesure expérimentale que l'on ne peut pas 
  répéter** plusieurs fois&nbsp;: *on parle d'incertitude de **type B***&nbsp;;
3. L'incertitude est celle du **résultat d'un calcul effectué à partir de 
  grandeurs pour lesquelles les incertitudes sont connues**.
{{% /note %}}

Le point n°1 ci-dessus a été abordé en classe de seconde, le point n°2 sera abordé cette année, le dernier point sera étudié en classe de terminale.

{{% note normal %}}
Votre travail consiste à être capable de reconnaître ces différentes situations et 
ensuite à mettre en œuvre les techniques décrites dans la suite de ce document.
{{% /note %}}

## Détermination de l'incertitude lorsqu'on peut effectuer une série de mesures

Lorsqu'un *même opérateur répète plusieurs fois la mesure de la même 
grandeur dans les mêmes conditions expérimentales*, il trouve généralement des 
résultats différents. Il en est de même lorsque des opérateurs différents 
réalisent simultanément le mesurage de la même grandeur avec du matériel 
similaire.

{{% note tip %}}
Lorsqu'on peut réaliser plusieurs fois un mesurage, on utilise des notions de statistiques pour déterminer la valeur du résultat&nbsp;: 
- *La **valeur estimée** est assimilée à la valeur moyenne de la série de mesures*&nbsp;;
- *L'**incertitude** est calculée à partir de l'écart-type de la série de mesures.*
{{% /note %}}

<!--
### La valeur moyenne d'une série de mesures est une grandeur aléatoire

Un corrigé de cette activité se trouve à l'adresse&nbsp;: 
{{< remote "https://repl.it/@dlatreyte/incertitudes" "https://repl.it/@dlatreyte/incertitudes" >}}.

La mesure $\Delta t$ de la durée de chute d'un objet depuis une fenêtre a 
été répétée 16 fois avec un chronomètre de qualité. Les résultats 
obtenus, exprimés en seconde, sont les suivants&nbsp;:

<center>

|  |  |  |  |  |  |  |  |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1,38 | 1,45 | 1,41 | 1,45 | 1,43 | 1,41 | 1,46 | 1,39 |
|  |  |  |  |  |  |  |  |
| 1,43 | 1,48 | 1,38 | 1,44 | 1,40 | 1,42 | 1,39 | 1,44 |

</center>

1. Se rendre à l'adresse&nbsp;: {{< remote "https://repl.it/@dlatreyte/incertitudeeleves" "https://repl.it/@dlatreyte/incertitudeeleves" >}} et cliquer sur le bouton `fork`, juste à côté de `run`.

2. Exécuter le programme de façon à connaître la moyenne de l'ensemble des valeurs. Noter cette valeur.

{{% solution "Résultat" %}}
La valeur de la moyenne est $\Delta t\_{m} = \pu{1,4225 s}$.
{{% /solution %}}

3. À quoi servent les instructions du programme qui s'étendent de la ligne 6 à 
la ligne 8&nbsp;?
{{% solution "Résultat" %}}
Les instructions réalisent le calcul de la somme de tous les éléments de la 
liste de valeurs passée en argument. La variable `somme` contient tout 
d'abord l'élément neutre de l'addition. À chaque tour de boucle on 
récupère une nouvelle valeur dans la liste et on l'ajoute à la valeur 
référencée par la variable `somme`.
{{% /solution %}}

{{% note important %}}
#### Point Python 
L'instruction
```python
for elt in une_liste:
```
 doit être lue de la façon suivante&nbsp;: «&nbsp;*Pour chaque élément `elt` de la liste 
`une_liste` faire ...*&nbsp;».
{{% /note %}}

4. Modifier l'instruction `moyenne = calcul_moyenne(valeurs)` de façon à ce 
qu'elle ne calcule la moyenne que des 6 première valeurs. Noter cette valeur.

{{% solution "Réponse" %}}
`moyenne = calcul_moyenne(valeurs[:6])`.

La valeur de la moyenne est $\Delta t\_{m} = \pu{1,4216666666666666 s}$.
{{% /solution %}}

{{% note important %}}
#### Point Python

Une liste est une **structure de données indicées** &nbsp;: on *accède/manipule 
les éléments d'une liste à partir de leur position dans la liste (la 
première position a 0 pour indice)* . Il est possible de ne prendre en compte 
qu'un nombre restreint d'éléments dans une liste (*Attention&nbsp;:* en Python les 
intervalles sont toujours du type $[a, b [$ c'est à dire fermé pour la borne 
inférieure, ouvert pour la borne supérieure)&nbsp;:

```python
>>> liste = [1, 2, 3, 4]
>>> liste[0]  # Premier élément
>>> liste[len(liste) - 1]  # Dernier élément (len donne le nombre d'éléments)
>>> liste[:3]  # Trois premiers éléments (d'indices 0, 1 et 2) [1, 2, 3]
```
{{% /note %}}

5. Pourquoi les deux moyennes calculées aux questions précédentes ne 
sont-elles pas égales&nbsp;?

{{% solution "Réponse" %}}
On a calculé des moyennes de séries différentes, il est donc normal que ces 
moyennes soient différentes.
{{% /solution %}}

6. Comment faire en sorte que la valeur moyenne caractérise au mieux «&nbsp;la chute 
de l'objet depuis la fenêtre&nbsp;»&nbsp;?

{{% solution "Réponse" %}}
Il faut réaliser le plus grand nombre d'expériences possible.
{{% /solution %}}

### Incertitude de répétabilité

L'incertitude de mesure $U(m)$ correspondant à des mesures répétées d'une même 
grandeur est appelée **incertitude de répétabilité** . Elle est liée à 
l'**écart-type** de la série de mesures.

{{% note tip %}}
* Pour une série de $n$ *mesures indépendantes* donnant des valeurs 
  mesurées $m\_{k}$ l'écart-type de la série de mesures est donné par la formule&nbsp;:
$$ \sigma \_{n - 1} = \sqrt{\dfrac{\sum\_{k = 1}^n (m\_{k} -
   \overline{m})^2}{n - 1}} $$
où $\overline{m}$ est la valeur moyenne de la série de mesures.  
L'écart type est obtenu en utilisant les fonctions statistiques d'une calculatrice, d'un tableur ou d'un programme écrit en Python.

* L'**incertitude de répétabilité**  associée à la mesure se calcule alors grâce à la formule&nbsp;:
$$ U (m) = k \hspace{0.17em} \dfrac{\sigma \_{n - 1}}{\sqrt{n}} $$

Elle dépend du nombre $n$ de mesures indépendantes réalisées, de l'écart type de la série de mesures et d'un coefficient $k$ appelé **facteur d'élargissement**  (ou coefficient de Student).

* Le **facteur d'élargissement** $k$ dépend du *nombre de mesures réalisées* $n$ et du *niveau de confiance* choisi.
{{% /note %}}

**Quelques valeurs de $k$&nbsp;:**

| nn | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $k$ 95%| 12,7 | 4,30 | 3,18 | 2,78 | 2,57 | 2,45 | 2,37 | 2,31 | 2,26 | 2,23 | 2,20 | 2,18 | 2,16 | 2,15 | 2,13 |
| $k$ 99% | 63,7 | 9,93 | 5,84 | 4,60 | 4,03 | 3,71 | 3,50 | 3,36 | 3,25 | 3,17 | 3,11 | 3,06 | 3,01 | 2,98 | 2,95 |

7. Pour un *même nombre de mesures*, comment évolue $k$ avec le niveau de confiance&nbsp;? Qu'est-ce que cette évolution traduit&nbsp;?

{{% solution "Réponse" %}}
Pour un même nombre de mesures, $k\_{95 \, \text{\%}} < k\_{99 \, 
\text{\%}}$. Plus grande est l'incertitude $U (m)$, plus grande est la 
probabilité que la «&nbsp;valeur vraie&nbsp;» se trouve dans l'intervalle 
$\overline{m} \pm U (m)$.
{{% /solution %}}

8. Pour un *même niveau de confiance* , comment évolue $k$ avec le nombre de 
mesures réalisées&nbsp;? Qu'est-ce que cette évolution traduit&nbsp;?

{{% solution "Réponse" %}}
$k$ diminue lorsque le nombre de mesures augmente. Plus le nombre de mesures 
est grand, plus la valeur moyenne de la série est représentative de la valeur 
mesurée et plus petit peut donc être l'intervalle autour de cette valeur 
moyenne. On retrouve l'idée qu'il est préférable de faire un grand nombre de 
mesures.
{{% /solution %}}

#### Pourquoi choisir l'écart type&nbsp;?

<figure>
<img src="/terminales-pc/chap-0/Chap-0-2-1.png" width="70%" />
</figure>

Le programme Python utilisé dans cette séance comporte la fonction `calcul_ecarts_a_moyenne`. Cette dernière calcule la somme des écarts à la valeur moyenne&nbsp;:

$$ \sum\_{k = 1}^n (m\_{k} - \overline{m}) $$

9. Faire en sorte que le programme appelle la fonction `calcul_ecarts_a_moyenne` (prendre les lignes 60 et 61 comme exemple) et calcule ainsi la somme des écarts à la moyenne. Que penser de la valeur obtenue&nbsp;? Était-ce prévisible&nbsp;?

{{% solution "Réponse" %}}
```python
ecart = calcul_ecarts_a_moyenne(valeurs)
print("Écart à la valeur moyenne&nbsp;: {}".format(ecart))
```
La valeur obtenue est $\pu{-2,6645352591003757e{- 15}}$, soit 0. 
C'était tout à fait prévisible puisque la valeur moyenne est le point 
d'équilibre de la série de valeurs&nbsp;: *les écarts positifs sont donc compensés par les écarts négatifs.*
{{% /solution %}}

10. L'écart-type ne considère pas les écarts à la valeur moyenne mais les 
carrés de ces écarts (cf. formule ci-dessus). Ils ne peuvent donc pas se 
compenser. Après analyse du code de la fonction `calcul_ecarts_a_moyenne`, compléter le code de la fonction `calcul_ecart_type`.

{{% solution "Réponse" %}}
```python
somme = 0
for valeur in liste_valeurs:
    somme = somme + (valeur - moyenne)**2
```
{{% /solution %}}

{{% note important %}}
#### Point Python
L'élévation à la puissance s'effectue à l'aide de l'opérateur `**`.
{{% /note %}}

11. Faire en sorte que le programme appelle la fonction `calcul_ecart_type` et 
qu'il affiche cette valeur. La noter.

{{% solution "Réponse" %}}
```python
ecart_type = calcul_ecart_type(valeurs)
print("Écart type&nbsp;: {}".format(ecart_type))
```
$\sigma \_{n - 1} = \pu{0,030000000000000023 s}$.
{{% /solution %}}

12. Compléter le code de la fonction `calcul_incertitude` à partir de la 
formule de l'incertitude donnée ci-dessus.

{{% solution "Réponse" %}}
`incertitude = k * ecart_type / m.sqrt(n)`
{{% /solution %}}

{{% note important %}}
#### Point Python
Lorsqu'on veut utiliser une fonction présente dans un module importé, il 
faut précéder ce nom par celui du module&nbsp;:

```python
import math as m
print(m.sin(m.pi))
```
{{% /note %}}


13. Faire en sorte que le programme appelle la fonction `calcul_incertitude` (prendre les lignes 60 et 61 comme exemple), avec la valeur de $k$ correspondant à un niveau de confiance de 95&nbsp;%, et qu'il affiche cette valeur. La noter.

{{% solution "Réponse" %}}
```python
incertitude_95 = calcul_incertitude(valeurs, 2.13)
print("Incertitude à 95 %&nbsp;: {}".format(incertitude_95))
```
$U (\Delta t) = \pu{0,01597500000000001 s}$.
{{% /solution %}}

14. Faire en sorte que le programme appelle la fonction `calcul_incertitude`, avec la valeur de $k$ correspondant à un niveau de confiance de 99&nbsp;%, et qu'il affiche cette valeur. La noter.

{{% solution "Réponse" %}}
```python
incertitude_99 = calcul_incertitude(valeurs, 2.95)
print("Incertitude à 99 %&nbsp;: {}".format(incertitude_99))
```
$U (\Delta t) = 0 {,} 02212500000000002 \text{s}$
{{% /solution %}}

15. Écrire le résultat de la mesure de la chute de l'objet depuis la fenêtre, 
avec un niveau de confiance à 95 % puis avec un niveau de confiance à 99 %.

{{% solution "Réponse" %}}
$\Delta t\_{95} = \pu{(1,43 \pm 0,02)  s}$ et $\Delta t\_{99} = \pu{(1,43 \pm 0,03) s}$.
{{% /solution %}}
-->

Ce type d'incertitude est étudié dans l'activité [Chap. 3,3 : Utilisation d'un tableur pour déterminer une incertitude de mesure de type A]({{% relref "./3-utilisation-tableur.md" %}}).

## Détermination de l'incertitude lorsqu'on n'effectue qu'une seule mesure

Lorsqu'une mesure ne peut pas être reproduite plusieurs fois, il est **impossible d'estimer une incertitude de répétabilité**. Il est alors nécessaire d'analyser les différentes sources d'erreurs liées à l'instrument de mesure. 

{{% note warning %}}
On rappelle qu'il ne faut surtout pas apprendre par cœur les expressions mais savoir les utiliser&nbsp;!
{{% /note %}}
 
### Utilisation d'un appareil gradué
 
 {{% note tip %}}
 #### Cas d'une lecture simple sur une échelle graduée
 <a href="" id="simple_mesure"> </a>
 Lorsque la mesure est obtenue par **une seule lecture sur une échelle ou un cadran**, pour un niveau de confiance de 95 %, l'incertitude de cette mesure a pour expression&nbsp;:
$$
U_{\text{lecture}} = \dfrac{2\times \text{Valeur Plus Petite Graduation}}{\sqrt{12}}
$$
{{% /note %}}

16. Une balance numérique au 1/100 de gramme affiche une masse $m = \pu{38,45 g}$.
Déterminer la valeur de l'incertitude $U(m)$ et écrire le résultat de la pesée.

{{% solution "Réponse" %}}
 Cette balance étant graduée à $\pu{0,01 g}$ près, $U = \dfrac{2\times \pu{0,01 g}}{\sqrt{12}} = \pu{0,00577 g}$ et le résultat de la mesure s'écrit $m = \pu{(38,450 \pm 0,006) g}$.
{{% /solution %}}


{{% note tip %}}
#### Cas d'une double lecture sur une échelle graduée
<a href="" id="double_mesure"> </a>
 Lorsque la mesure nécessite une double lecture, les incertitudes liées à la lecture peuvent se cumuler ou se compenser, totalement ou partiellement. Pour un niveau de confiance de 95 %, l'incertitude de cette mesure a pour expression&nbsp;:
 $$
 U_{\text{double lecture}} = \sqrt{2\\, \left(\dfrac{2\times \text{Valeur Plus Petite Graduation}}{\sqrt{12}}\right)^2} = \sqrt{2}\\;U_{\text{lecture}}
 $$
 {{% /note %}}

 17. La mesure de la distance séparant deux récepteurs à ultrason nécessite de repérer par rapport à une règle graduée jusqu'au millimètre les positions de ces deux dispositifs&nbsp;: c'est une **double mesure**.  
 Déterminer l'incertitude associée à toute mesure utilisant une règle graduée jusqu'au millimètre.

 {{% solution "Réponse" %}}
 La règle étant graduée au millimètre, $U = \sqrt{2}\times\dfrac{2\times \pu{1 mm}}{\sqrt{12}} = \pu{0,82 mm}$.  
 **Remarque&nbsp;:** En pratique, on peut arrondir cette incertitude à $U = \pu{1 mm}$.
 {{% /solution %}}

 18. La mesure de la période $f$ d'un signal périodique affiché sur l'écran d'un oscilloscope nécessite de repérer deux points de la courbe et de lire leurs abscisses&nbsp;: c'est une **double mesure**.  
La plus petite graduation, sur l'écran de l'oscilloscope, étant égale à $\pu{0,2 division}$, déterminer l'incertitude associée à toute mesure à l'écran d'un oscilloscope.

{{% solution "Réponse" %}}
$U = \sqrt{2}\\;\times\dfrac{2\times \pu{0,2 division}}{\sqrt{12}} = \pu{0,163 division}$. *Pour obtenir l'incertitude en secondes, il ne reste plus alors qu'à multiplier par la base de temps*.
 {{% /solution %}}

 ### Utilisation d'un appareil dont le constructeur a indiqué la tolérance

 {{% note tip %}}
#### Cas d'une mesure obtenue avec un appareil de tolérance connue
Lorsque la mesure est obtenue avec un appareil pour lequel le constructeur indique la tolérance $t$ (notée $\pm t$), l'incertitude liée à la tolérance de cet appareil a pour expression&nbsp;:
$$
U = \dfrac{2\\, t}{\sqrt{3}}
$$
 {{% /note %}}

 19. En chimie, les fabricants indiquent toujours la tolérance sur la verrerie jaugée. Par exemple, la tolérance d'une pipette jaugée de $\pu{10 mL}$, de **classe A**, est égale à $\pu{\pm 0,02 mL}$.  
Déterminer l'incertitude sur la mesure d'un volume à l'aide d'une pipette jaugée de $\pu{10 mL}$.

{{% solution "Réponse" %}}
L'incertitude sur la mesure du volume lors de l'utilisation de cette pipette jaugée vaut donc $U =  \dfrac{2 \times \pu{0,02 mL}}{\sqrt{3}} = \pu{0,023 mL}$ et le volume prélevé est égal à $\pu{(10,00 \pm 0,03) mL}$.
{{% /solution %}}

20. Un élève mesure un volume d’eau de $\pu{40,0 mL}$ avec une burette graduée de $\pu{50 mL}$ de classe A (tolérance $\pu{\pm 0,05 mL}$).  
Déterminer l'incertitude sur la mesure du volume d'eau.

{{% solution "Réponse" %}}
L'incertitude $U$ vaut donc $U = \dfrac{2 \times \pu{0,05 mL}}{\sqrt{3}} = \pu{0,0577 mL}$ et le volume mesuré est $\pu{(40,00 \pm 0,06) mL}$.
{{% /solution %}}


