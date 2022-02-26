---
title: "Lancement d'une fusée et retour sur Terre"
subtitle: "Chapitre 8,7"
author: ""
type: ""
date: 2020-12-18T17:44:22+04:00
draft: false
toc: true
tags: []
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---

## Lancement d'une fusée

#### Doc. 1 : Ariane

Ariane est le nom générique d'une famille de lanceurs civils européens de 
satellites. Le programme Ariane est lancé en 1973 par l'Agence spatiale 
européenne afin de donner les moyens à l'Europe de mettre en orbite ses 
satellites sans dépendre des autres puissances spatiales. Ce projet avait 
été précédé d'un échec avec la fusée Europa. La première version, 
Ariane 1, effectue son vol inaugural depuis la base de Kourou (Guyane 
française) le 24 décembre 1979. Elle est rapidement remplacée par des 
versions plus puissantes, Ariane 2, Ariane 3 et Ariane 4 qui effectuent leur 
premier vol respectivement en 1984, 1986 et 1988. Pour faire face à 
l'augmentation de la masse des satellites, le lanceur est complètement 
refondu, donnant naissance à la version Ariane 5 capable de placer maintenant 
plus de $\pu{10,7 t}$ en orbite de transfert géostationnaire. Son premier vol a eu lieu en 1996.

<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Ariane_(fusée)" target="_blank" > http://fr.wikipedia.org/wiki/Ariane_(fusée)</a>
</div>

#### Doc. 2 : Ariane 4

Le lanceur Ariane 4 était commercialisé dans 6 configurations différentes 
permettant de lancer un ou deux satellites en orbite de transfert 
géostationnaire (GTO) avec une masse totale de $\pu{2100 kg}$ à $\pu{4950 kg}$. Il possédait 
selon les versions des propulseurs supplémentaires (zéro, deux ou quatre) de 
types variables : à propergol liquide  ou bien à propergol solide (également 
qualifiés de « à poudre »).

##### Version Ariane 40

* Masse totale *au décollage*  : $M\_{0} = \pu{210e3 kg}$.
* Masse totale de propergol contenu dans le premier étage *au décollage*  : 
  $M\_{p} = \pu{147e3 kg}$.
* Masse de propergol consommé chaque seconde lors du fonctionnement du 
  premier étage (c'est aussi le débit d'éjection des gaz) : $D = \pu{1,0e3 kg.s-1}$.
* Vitesse d'éjection des gaz par rapport à la fusée, *au décollage* : $v\_{g} = \pu{2,5e3 m.s-1}$.
* Durée de fonctionnement du premier étage : $\pu{147 s}$.
* Poussée totale moyenne fournie par les moteurs du premier étage : $F = \pu{2,45e6 N}$.
* Pendant la phase de propulsion du premier étage, la poussée des moteurs 
  reste pratiquement constante et la fusée suit une trajectoire sensiblement rectiligne et verticale.

#### Doc. 3 : Poussée exercée par un moteur à réaction type moteur-fusée

La *poussée*  ou plus exactement la *force de poussée*  $\vec{F}$ est la 
modélisation de l'action qu'exercent les gaz éjectés vers l'arrière par la 
fusée, à la vitesse $\vec{v}\_{g}$ *par rapport à la fusée*.    
Dans les conditions optimales du fonctionnement d'une fusée, on peut définir 
la force de poussée par la relation

$$
 \vec{F} = - D\\, \vec{v}\_{g}
$$

où $D$ est la masse de gaz éjectée par seconde (débit d'éjection).

----

Les mesures télémétriques effectuées pendant la phase de fonctionnement du 
premier étage, ont permis de dresser le tableau donné en **annexe**. Ce 
tableau indique l'altitude atteinte par la fusée depuis son point de lancement 
en fonction du temps écoulé depuis l'instant du décollage (dans un 
référentiel terrestre donc).

Remarques.
: On considère dans cet exercice que l'intensité de la 
pesanteur reste constante jusqu'à l'altitude maximale considérée : $g = \pu{9,8 N.kg-1}$. On se placera aussi, lors de toutes les 
études à suivre, dans le référentiel terrestre supposé galiléen.

<center>
<strong>Les différentes parties de ce problème sont indépendantes.</strong>
</center>

### Étude cinématique du mouvement pendant la phase de propulsion du premier Étage

1. À partir d'un examen rapide du tableau donné en annexe, que peut-on dire de la nature du mouvement de la fusée ?

2. Déterminer la vitesse moyenne de la fusée au cours de la phase de 
fonctionnement du premier étage.

On se propose de déterminer des valeurs approchées de la vitesse et de 
l'accélération à différentes dates.

3. Calculer (en indiquant la méthode employée) la valeur de la vitesse $v\_{9}$ à la date $t = \pu{9 s}$ et la valeur de la vitesse $v\_{11}$ à la date $t = \pu{11 s}$.

4. En déduire (en indiquant la méthode employée) une valeur approchée de 
l'accélération $a\_{10}$ à la date $t = \pu{10 s}$.

Aux dates $t = \pu{70 s}$ et $t = \pu{140 s}$ l'application du 
raisonnement mis en œuvre aux questions précédentes conduit aux valeurs suivantes pour l'accélération : $a\_{70} = \pu{7,50 m.s-2}$ et $a\_{140} = \pu{25,0 m.s-2}$.

5. Le mouvement de la fusée est-il uniformément accéléré ?

### Étude dynamique du mouvement pendant la phase de propulsion du premier étage

6. Donner toutes les caractéristiques de la force de poussée.

7. Faire un schéma du système fusée et représenter les forces qui 
s'appliquent sur ce système *lors de son ascension*.

Remarque.
: Les mesures télémétriques montrent que l'on peut négliger les 
frottements de la fusée avec l'air.

Le modèle utilisé dans cet exercice permet d'écrire le principe fondamental 
de la dynamique (2ème loi de Newton) pour la fusée, à la date $t$, sous la 
forme $M \vec{a}\_{G} = \sum \vec{F}^{ext}$ **bien que sa masse 
varie**.

8. Donner la direction et le sens du vecteur accélération $\vec{a}$. Justifier la réponse.

9. Déterminer l'expression littérale de la valeur $a$ du vecteur accélération $\vec{a}$ en fonction de $F$, $g$ et de la masse $M (t)$ de la fusée à l'instant $t$.

10. Justifier que la masse de la fusée à la date $t$ s'écrit

$$
M (t) = M\_{0} - Dt
$$

11. Calculer la valeur $M\_{70}$ de la masse à la date $t = \pu{70 s}$.

12. À partir des relations établies aux questions précédentes, calculer la 
valeur de l'accélération $a\_{70}$ à la date $t = \pu{70 s}$.

13. La valeur de l'accélération à la date $t = \pu{70 s}$ permet-elle de 
valider l'étude effectuée dans cette partie ?

## Retour sur Terre

Pour revenir sur Terre, les cosmonautes de Soyouz mettent en route pendant 
quelques minutes des rétrofusées qui modifient la trajectoire et font 
pénétrer l'engin dans les couches denses de l'atmosphère à environ $\pu{75 km}$ d'altitude. Les seuls frottements de l'air sur l'engin produisent un important freinage. À $\pu{10800 m}$ d'altitude, alors que la vitesse est de $\pu{250 m.s-1}$, un premier parachute s'ouvre et réduit la vitesse à $\pu{50 m.s-1}$. Vers $\pu{8000 m}$ d'altitude le premier parachute est remplacé par un deuxième plus important qui stabilise la vitesse de descente à $\pu{10 m.s-1}$.

Les deux derniers kilomètres se font sur une trajectoire pratiquement 
rectiligne et verticale à la vitesse constante de $\pu{10 m.s-1}$. Cette trajectoire sera matérialisée par un axe vertical $(z' z)$ *orienté vers le haut* et dont l'origine $O$ se trouvera au niveau du sol. Les frottements de l'air sur la cabine elle-même deviennent négligeables.

Donnée.
: Masse du vaisseau Soyouz : $m\_{S} = \pu{3,00e3 kg}$.

14. Représenter les forces appliquées sur la cabine. Donner toutes les 
caractéristiques de ces forces.

Lorsque la cabine se trouve à $\pu{1 m}$ au dessus du sol à la vitesse de 
$\pu{10 m.s-1}$, une rétrofusée entre en action pour annuler la vitesse au moment de l'atterrissage. On se propose d'étudier cette dernière phase de freinage.

15. Représenter les forces appliquées sur la cabine.

16. Soit $\vec{F}$ la somme de toutes les forces appliquées. On suppose $\vec{F}$ constante. Énoncer le théorème de l'énergie cinétique et utiliser ce théorème pour calculer la valeur de $\vec{F}$.

17. Déduire de $\vec{F}$ la valeur de la poussée $\vec{R}$ de la rétrofusée lors de sa mise à feu.

18. Quelles sont les caractéristiques du vecteur accélération $\vec{a}$ du centre d'inertie $G$ de la cabine ?

19. Quelle est la durée du freinage ?

**Informations.** Les données numériques concernant le retour sur Terre du 
vaisseau Soyouz sont issues de renseignements fournis par le C.N.E.S.

## Annexe

<center>
    <p style="margin-top: 0.5em; margin-bottom: 0.5em">
    <table style="display: inline-table; vertical-align: middle">
        <tbody><tr>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Dates (s)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Altitude (m)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Dates (s)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Altitude (m)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Dates (s)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Altitude (m)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Dates (s)</strong></td>
        <td style="text-align: center; vertical-align: middle; border-top: 1px solid; border-bottom: 1px solid"><strong>Altitude (m)</strong></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">0</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">0,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">39</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2002,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">78</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">11019,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">117</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">33675,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">0,90</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">40</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2125,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">79</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">11393,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">118</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">34525,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3,80</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">41</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2251,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">80</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">11776,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">119</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">35391,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8,50</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">42</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2382,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">81</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">12168,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">120</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">36275,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">15,30</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">43</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2518,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">82</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">12569,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">121</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">37176,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">5</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">24,20</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">44</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2659,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">83</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">12979,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">122</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">38094,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">6</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">35,10</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">45</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2805,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">84</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">13399,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">123</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">39030,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">7</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">48,30</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">46</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">2956,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">85</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">13828,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">124</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">39985,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">63,70</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">47</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3112,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">86</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">14267,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">125</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">40958,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">9</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">81,40</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">48</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3273,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">87</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">14716,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">126</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">41950,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">10</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">101,40</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">49</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3439,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">88</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">15175,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">127</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">42961,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">11</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">123,90</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">50</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3611,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">89</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">15644,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">128</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">43992,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">12</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">148,90</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">51</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3788,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">90</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">16123,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">129</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">45042,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">13</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">176,40</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">52</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">3971,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">91</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">16613,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">130</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">46113,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">14</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">206,50</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">53</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4159,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">92</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">17114,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">131</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">47204,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">15</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">239,20</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">54</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4353,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">93</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">17626,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">132</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">48317,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">16</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">274,70</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">55</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4553,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">94</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">18148,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">133</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">49450,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">17</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">313,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">56</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4759,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">95</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">18682,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">134</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">50606,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">18</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">354,20</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">57</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">4971,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">96</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">19228,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">135</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">51784,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">19</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">398,30</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">58</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">5190,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">97</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">19784,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">136</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">52985,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">20</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">445,30</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">59</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">5414,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">98</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">20353,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">137</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">54208,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">21</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">495,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">60</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">5645,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">99</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">20934,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">138</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">55455,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">22</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">549,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">61</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">5882,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">100</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">21526,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">139</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">56726,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">23</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">605,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">62</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">6126,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">101</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">22132,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">140</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">58022,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">24</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">665,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">63</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">6377,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">102</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">22749,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">141</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">59343,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">25</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">728,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">64</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">6634,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">103</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">23380,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">142</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">60689,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">26</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">794,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">65</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">6898,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">104</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">24023,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">143</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">62061,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">27</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">864,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">66</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">7170,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">105</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">24680,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">144</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">63459,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">28</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">938,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">67</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">7448,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">106</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">25350,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">145</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">64885,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">29</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1015,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">68</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">7734,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">107</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">26034,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">146</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">66338,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">30</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1096,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">69</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8027,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">108</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">26732,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">147</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">67819,00</td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">31</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1181,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">70</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8328,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">109</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">27444,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">32</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1269,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">71</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8636,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">110</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">28170,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">33</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1361,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">72</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">8952,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">111</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">28910,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">34</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1458,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">73</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">9276,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">112</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">29666,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">35</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1558,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">74</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">9608,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">113</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">30437,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">36</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1663,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">75</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">9948,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">114</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">31222,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">37</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1772,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">76</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">10297,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">115</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">32024,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr><tr>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">38</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">1885,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">77</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">10654,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">116</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid">32841,00</td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        <td style="text-align: center; vertical-align: middle; border-bottom: 1px solid"></td>
        </tr></tbody>
    </table>
    </p>
</center>

## Corrigé

{{% solution "Corrigé" %}}
{{< remote "Corrigé au format pdf" "/terminales-pc/chap-7/chap-7-7-1.pdf"  >}}
{{% /solution %}}