---
title: "Utiliser le réseau téléphonique pour surfer sur Internet"
subtitle: "Chapitre 1,5"
author: "Hachette, TS"
type: ""
date: 2020-09-18T16:43:15+04:00
draft: false
toc: true
tags: ["Absorption", "Atténuation", "Ondes", "Fibre optique"]
categories: ["Physique", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: false
auto_numbering: true
---
[^1]: La **résistivité** est la capacité d'un matériau à s'opposer à la circulation du courant électrique.
[^2]: les technologies **xDSL** permettent la propagation de l'information numérique par les câbles téléphoniques. La transmission se fait en utilisant des hautes fréquences inutilisées par le téléphone. L'ADSL utilisée par les particuliers pour Internet fait partie de ces technologies.
[^3]: Lorsque la fréquence est élevée, le courant électrique ne circule qu'en surface du conducteur électrique, voire même uniquement sous forme d'une ondes électromagnétique. On parle d'**effet de peau**.

## Documents

### Affaiblissement des signaux

<img src="/terminales-pc/chap-1/chap-1-5-1.jpg" alt="" width="60%" />

« Un courant électrique passant au travers d'un conducteur dissipe une partie de son énergie sous forme de chaleur (pertes par effet Joule). Il en résulte une diminution de la puissance de ce signal. Les pertes augmentent avec la résistance du câble. La résistance est elle-même fonction de la longueur du câble, de son diamètre et de sa résistivité[^1] [...] Les technologies xDSL[^2] font passer des signaux électriques à haute fréquence dans les câbles téléphoniques, constitués de fils de cuivre. Compte tenu de ces hautes fréquences, un effet de peau[^3] apparaît ; il a pour conséquence d'augmenter fortement la résistance du câble, et donc d'atténuer d'autant plus le signal utile en raison du phénomène décrit précédemment. [...] Il découle de ce phénomène que certaines habitations, proches des centraux téléphoniques [...] bénéficient de débits élevés (jusqu'à $\pu{20 Mbit/s}$, permettant un grand confort d'usage et des services innovants tels que la télévision par ADSL), tandis que d'autres plus éloignés doivent se contenter de $\pu{512 kbit/s}$ — et ce pour un prix d'abonnement identique. »

<div style="text-align: right;">
Extrait de {{< remote "www.ant.developpement-durable.gouv.fr" "http://www.ant.developpement-durable.gouv.fr" >}}.
</div>

### Atténuation du signal sur une fibre optique

L'atténuation du signal sur une fibre optique qui se mesure en $\pu{dB.km-1}$ est due à plusieurs phénomènes dont : 
- la **diffusion Rayleigh** : c'est le résultat de l'interaction entre la lumière et la matière. Elle est d'autant plus grande que la longueur d'onde $\lambda$ est petite ;
- l'**absorption** : elle recouvre principalement trois causes : la *présence d'impuretés dans la fibre*, les *vibrations moléculaires*, les *transitions électroniques dans l'ultraviolet* ;
- les **connexions** : la mise bout à bout des fibres nécessite un alignement des axes parfait, au risque de produire des pertes.

### Amplification des signaux

« La portée sans amplification d'une liaison est d'environ $\pu{20 km}$ avec les conducteurs de cuivre usuels, dont le diamètre mesure entre 0,4 et $\pu{0,8 mm}$. En pratique, la distance entre un terminal et son commutateur de rattachement est assez réduite pour qu'il n'y ait pas besoin d'amplifier le signal. Il n'en va pas de même pour les liaisons entre commutateurs. Dans ce cas, on regroupe plusieurs communications sur la même artère de transmission dans laquelle les signaux doivent être amplifiés à intervalles réguliers. Faute de quoi l'atténuation des signaux serait telle que les conversations deviendraient inaudibles. L'atténuation est due aux pertes par effet Joule (*dégagement de chaleur dû à la résistance qu'offre le matériau conducteur au mouvement des électrons*) et aux pertes par rayonnement électromagnétique. Sur les liaisons de transmission à câble coaxial, une amplification est nécessaire tous les $\pu{1,6 km}$ ; les liaisons à fibre optique tolèrent des intervalles entre amplificateurs beaucoup plus grands, tous les 40 ou $\pu{50 km}$, voire $\pu{100 km}$. »

<div style="text-align: right;">
Extrait de H. Kempf, « Le téléphone », La Recherche, n°291, octobre 1996.
</div>

## Exploitation

1. Sous quelle forme le signal téléphonique est-il transmis dans un câble de cuivre ?
{{% solution "Réponse" %}}

{{% /solution %}}

2. Quelles sont les causes de l'atténuation du signal dans un câble de cuivre ?  
Que doit-on faire pour transmettre un signal sur une longue distance ?
{{% solution "Réponse" %}}

{{% /solution %}}

3. L'atténuation dépend-elle de la fréquence du signal ? Quelles conséquences cela peut-il avoir sur les abonnements ADSL ?
{{% solution "Réponse" %}}

{{% /solution %}}

4. Sous quelle forme le signal téléphonique est-il transmis dans une fibre optique ?
{{% solution "Réponse" %}}

{{% /solution %}}

5. Citer des causes de l'atténuation du signal dans une fibre optique. Quelle distance peut parcourir le signal sans être amplifié ?
{{% solution "Réponse" %}}

{{% /solution %}}

6. On amplifie le signal dans une fibre quand il reste 1&nbsp;% de la puissance initialement injectée. Évaluer le coefficient d'atténuation du signal dans une fibre optique.
{{% solution "Réponse" %}}

{{% /solution %}}

