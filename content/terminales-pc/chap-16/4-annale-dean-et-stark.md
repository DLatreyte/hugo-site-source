---
title: "Annale : Synthèse d'un ester à l'aide d'un appareil de Dean et Stark"
subtitle: "Chapitre 15,4"
author: ""
type: ""
date: 2021-04-12T18:51:08+04:00
draft: false
toc: true
tags: []
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Protocole

- Dans un ballon, introduire successivement $\pu{9,00 g}$ d'acide éthanoïque, $\pu{10,80 g}$ d'alcool benzylique ou phénylméthanol, $\ce{C6H5-CH2-OH}$, $\pu{10 mL}$ de cyclohexane, 10 gouttes d'acide sulfurique et quelques grains de pierre ponce. Installer l'appareil de Dean et Stark et le remplir de cyclohexane, installer le condenseur à eau puis porter le mélange à ébullition et l'y maintenir pendant environ 45 minutes.
<img src="/terminales-pc/chap-16/chap-16-4/chap-14-4-1.png" alt="" width="50%" />

- Retirer le chauffe-ballon puis, en laissant branché le condenseur, refroidir le ballon d'abord à l'air puis dans un bain d'eau froide. Éliminer l'eau recueillie dans l'appareil de Dean et Stark.

- Verser le mélange réactionnel et la phase organique restant dans l'appareil de Dean et Stark, dans une ampoule à décanter.

- Laver le tout avec $\pu{50 mL}$ de solution de chlorure de sodium puis, après avoir éliminé la phase inférieure aqueuse, avec $\pu{50 mL}$ de solution d'hydrogénocarbonate de sodium.

- Éliminer à nouveau la phase aqueuse et sécher la phase organique sur sulfate de magnésium anhydre.

- Transvaser la phase organique séchée dans un ballon à distiller. Ajouter quelques grains de pierre ponce et réaliser un montage de distillation fractionnée.

- Distiller le mélange tant que la température reste voisine de 80 °C. Récupérer le résidu dans un ballon taré et déterminer sa masse $m$.

## Données

|   | Masse volumique ($\pu{g.mL-1}$) | Température d'ébullition (°C) | Solubilité dans l'eau | Solubilité dans le cyclohexane |
| :---:  | :---: | :---: | :---: | :---: |
| acide acétique  | 1,050 | 118 | totale | bonne |
| phénylméthanol | 1,042 | 206 | faible | très bonne |
| ester $E$ | 1,056 | 215 | très faible | très bonne |
| eau | 1,000 | 100 | -- | très faible |
|cyclohexane | 0,780 | 81 | très faible | -- |

## Questions

1. Sachant que le cyclohexane n'a qu'un rôle de solvant, écrire l'équation de l'estérification étudiée.\
Citer le nom de l'ester formé.
{{% solution "Solution" %}}
L'acide éthanoïque a pour formule $\ce{CH3-CO2H}$. L'équation de l'estérification s'écrit donc 
$$\ce{CH3-CO2H (l) + C6H5-CH2-OH (l) <=> CH3-CO2-CH2-C6H5 (l) + H2O}$$
L'ester formé est l'éthanoate de phénylméthyle (ou acétate de benzyle).
{{% /solution %}}

Durant le chauffage, on observe que les vapeurs qui se condensent dans le réfrigérant se séparent dans l'appareil de Dean et Stark en une phase aqueuse qui s'accumule dans le réservoir de récupération et une phase organique qui, mélangée au cyclohexane préalablement introduit dans ce réservoir, retourne dans le ballon par effet de trop plein.

2. Où se situe la « phase aqueuse qui s'accumule dans le réservoir de récupération » par rapport à la phase organique ? Pourquoi ?
{{% solution "Solution" %}}
La densité de l'eau ($d=\pu{1,000}$) est supérieure à celle du cyclohexane ($d = \pu{0,780}$) ; la phase aqueuse se trouve donc sous la phase organique dans le réservoir.
{{% /solution %}}

3. Quel test simple permet de vérifier la présence d'eau dans la partie inférieure de l'appareil de Dean et Stark ?
{{% solution "Solution" %}}
Lorsque les premières gouttes d'eau se forment, il n'est pas facile de constater la formation des deux phases dans le réservoir de récupération. On peut cependant, dès que l'on pense qu'un peut d'eau s'est formée, laisser tomber une goutte de liquide (en ouvrant le robinet) dans une coupelle contenant du sulfate de cuivre anhydre blanc. Au contact de l'eau ce sulfate de cuivre se colore en bleu (test vu au collège pour la première fois).
{{% /solution %}}

4. Quel intérêt présente ce dispositif pour la synthèse de l'ester ?
{{% solution "Solution" %}}
Ce dispositif permet de retirer progressivement l'eau du mélange réactionnel. L'hydrolyse de l'ester est donc limitée et, par déplacement d'équilibre, le rendement de l'estérification augmente.
{{% /solution %}}

5. Quelle masse maximale d'eau peut-on ainsi recueillir ?
{{% solution "Solution" %}}
<center>

| État | Avancement | acide | alcool || ester | eau |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Initial | 0 | $n_1$ | $n_2$ || $0$ | $0$ |
| Final | $x_f$ | $n_1 - x_f$ | $n_2 - x_f$ || $x_f$ | $x_f$ |

</center>

La masse d'eau formée est maximale dans le cas d'une transformation totale. Dans ce cas, $x_f = x_{max}$ et $x_max = min(n_1 ; n_2)$.

- Quantité de matière d'acide : $n_1 = \dfrac{m_1}{M_1}$. **A.N.** $n_1 = \dfrac{\pu{9,00 g}}{\pu{60,1 g.mol-1}} = \pu{1,50e-1 mol}$.
- Quantité de matière d'alcool : $n_2 = \dfrac{m_2}{M_2}$. **A.N.** $n_2 = \dfrac{\pu{10,80 g}}{\pu{108,1 g.mol-1}} = \pu{1,00e-1 mol}$.

L'avancement maximal vaut donc $x_{\text{max}} = \pu{1,00e-1 mol}$ et $m_{\text{eau}} = \pu{1,00e-1 mol} \times \pu{18,0 g.mol-1} = \pu{1,80 g}$.
{{% /solution %}}

6. Pourquoi convient-il de refroidir le mélange réactionnel avant de procéder aux lavages ?
{{% solution "Solution" %}}
Tant que le mélange réactionnel est chaud, il est possible de perdre des entités par évaporation. On refroidit donc le mélange en laissant le réfrigérant en place.
{{% /solution %}}

7. À quoi sert le lavage à l'aide de la solution de chlorure de sodium ? Comment vérifier, par un test simple, que ce rôle a bien été tenu ?
{{% solution "Solution" %}}
Un lavage permet d'éliminer les impuretés solubles dans le solvant utilisé pour le lavage.\
Par exemple, ici, l'ester est très peu soluble dans l'eau. Il est pratiquement insoluble dans de l'eau salée (**les ions renforcent le caractère polaire du solvant**) ; il va donc rester dans la phase organique. Toutes les impuretés solubles dans ce solvant vont, elles, passer en phase aqueuse.
{{% /solution %}}

Lors du lavage à l'aide de la solution d'hydrogénocarbonate de sodium, on observe un dégagement gazeux.

8. Quelle en est la nature ? Écrire l'équation de la réaction qui produit ce dégagement.
{{% solution "Solution" %}}
L'ion hydrogénocarbonate $\ce{HCO3^-}$ est la base conjuguée du dioxyde de carbone solubilisé $\ce{CO2, H2O}$. L'ion hydrogénocarbonate peut donc réagir avec l'acide éthanoïque en excès, qui n'aurait pas été éliminé lors du premier lavage à la solution aqueuse de chlorure de sodium. L'équation de la réaction est :
$$
    \ce{CH3-CO2H (aq) + HCO3^- (aq) <=> CH3-CO2^- (aq) + CO2, H2O}
$$
{{% /solution %}}


9. De quel constituant la phase organique est-elle ainsi débarrassée ? Pourquoi ce constituant quitte-t-il la phase organique ?
{{% solution "Solution" %}}
Cette question est très liée à la précédente. On élimine l'acide éthanoïque en excès. Le problème avec cette entité est qu'elle est totalement soluble dans l'eau et soluble dans le cyclohexane. Le premier lavage à l'aide d'une solution de chlorure de sodium ne permet pas de l'évacuer de la phase organique.\
L'ion éthanoate, de formule $\ce{CH3-CO2^-}$, entité chargée, est très soluble dans une solution aqueuse et pas du tout soluble dans un solvant organique apolaire comme le cyclohexane. Le lavage à l'hydrogénocarbonate de sodium permet bien d'éliminer l'acide de la phase organique.
{{% /solution %}}

10. Après le séchage, que reste-t-il dans la phase organique ?
{{% solution "Solution" %}}
Après chauffage, il ne reste que l'ester dans la phase organique.
{{% /solution %}}

La dernière étape est une distillation fractionnée.

11. Faire un schéma légendé du montage utilisé.
{{% solution "Solution" %}}
<img src="/terminales-pc/chap-16/chap-16-4/chap-14-4-2.svg" alt="" width="50%" />
{{% /solution %}}

12. Quelle est la nature du distillat ? Quelle est celle du résidu ?
{{% solution "Solution" %}}
La température d'ébullition de l'éster est très supérieure à celle du cyclohexane ; ce dernier s'évapore donc en premier et constitue le distillat. L'ester forme donc le résidu.
{{% /solution %}}

13. Dans une expérience, on a obtenu une masse $m = \pu{13,5 g}$ d'ester ; déterminer le rendement de cette synthèse. Conclure.
{{% solution "Solution" %}}
Le rendement est défini de la sorte :
$$
    \eta = \dfrac{n(\text{ester})}{n\_{\text{max}}(\text{ester})} = \dfrac{n(\text{ester})}{n(\text{réactif limitant})}
$$
puisque les nombres stœchiométriques sont tous égaux à 1.\
**Attention.** La dernière égalité n'est vraie que dans le cas de l'estérification, elle ne fait pas partie de la définition. 

- On sait déjà que $n(\text{réactif limitant}) = \pu{1,00e-1 mol}$ (question 5).
- $n(\text{ester}) = \dfrac{m(\text{ester})}{M(\text{ester})}$. **A.N.** $n(\text{ester}) = \dfrac{\pu{13,5 g}}{\pu{150,2 g.mol-1}} = \pu{9,00e-2 mol}$.

Le rendement vaut donc
$$
    \eta = \dfrac{\pu{9,00e-2 mol}}{\pu{1,00e-1 mol}} = \pu{9,00e-1}
$$ soit 90 %.
{{% /solution %}}