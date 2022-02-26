---
title: "Pourquoi créer une nouvelle grandeur pour exprimer le nombre d’objets ?"
subtitle: "Chapitre 1,2"
author: ""
type: ""
date: 2020-09-08T20:15:37+04:00
draft: false
toc: true
tags: []
categories: ["Premières Spé PC", "Chimie"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Et si nous étions en charge de la gestion du papier pour les photocopieurs du lycée&nbsp;?

### Informations&nbsp;: une feuille de papier

- Dimensions : $210 \times \pu{297 mm}$&nbsp;;
- Masse : $m = \pu{80 g/m2}$.


### Étude des besoins pour une chaîne d'approvisionnement

1. Est-il possible de déterminer, à l’aide d’une règle graduée, l’épaisseur d’une feuille de papier&nbsp;?
{{% solution "Réponse" %}}
La dernière graduation de la règle est le millimètre, longueur bien supérieure à l'épaisseur d'une feuille de papier.
{{% /solution %}}

2. Dans le cas où la réponse à la question précédente serait « Non », indiquer pourquoi cette détermination **directe** est impossible.
{{% solution "Réponse" %}}
La règle n'est pas l'instrument de mesure adapté pour effectuer une **mesure directe**.
{{% /solution %}}

3. Essayer de trouver un **moyen indirect** de réaliser cette tache.
{{% solution "Réponse" %}}
On peut imaginer mesurer l'épaisseur d'un «&nbsp;paquet&nbsp;» de feuilles et diviser le résultat de cette mesure par le nombre de feuilles dans ce «&nbsp;paquet&nbsp;».
{{% /solution %}}

4. Qu’est ce qui **caractérise** une « rame de papier » ?
{{% solution "Réponse" %}}
Une «&nbsp;rame de papier&nbsp;» est un paquet de 500 feuilles.
{{% /solution %}}

5. Déterminer finalement l’épaisseur d’une feuille.
{{% solution "Réponse" %}}
$e = \dfrac{\pu{5,1 cm}}{500} = \pu{0,010 cm}$.
{{% /solution %}}

6. Dans un établissement scolaire comportant un grand nombre d’élèves, le nombre de photocopies par an peut être supérieur à 2&nbsp;000&nbsp;000. Quelle commande le gestionnaire passe-t-il au fournisseur de feuilles de papier de façon à ce que le stockage et la distribution des feuilles soient les plus pratiques possibles ?
{{% solution "Réponse" %}}
Pour transport, la manipulation, le stockage, il est plus **aisé** de commander $\dfrac{\pu{2e6}}{500} = \pu{4e3}$ rames de papier.
{{% /solution %}}

7. Pour réaliser la livraison le fournisseur possède une camionnette « Renault Trafic » dont le volume utile est environ égal à $\pu{9 m3}$. Combien de voyages doit-il effectuer pour livrer le lycée&nbsp;?
{{% solution "Réponse" %}}
- Dans un premier temps, il est **pratique** de déterminer le volume d'une «&nbsp;rame de papier&nbsp;» (parallélépipède rectangle)&nbsp;: $V(1 \text{ rame}) = \pu{5,1 cm} \times \pu{21,0 cm} \times \pu{29,7 cm} = \pu{3,2e3 cm3} = \pu{3,2e-3 m3}$.
- On peut maintenant déterminer le nombre maximal (c'est une approximation) de rames que le transporteur peut charger dans son véhicule&nbsp;: $N = \dfrac{V(\text{camion})}{V(1 \text{ rame})}$ $N = \dfrac{ \pu{9 m3} }{ \pu{3,2e-3 m3} } = \pu{2812} < \pu{4e3}$.
Le transporteur devra donc effectuer au moins deux livraisons. 
{{% /solution %}}

8. Quelle masse maximale de papier est transportée lors de chacune des livraisons&nbsp;?
{{% solution "Réponse" %}}
- Dans un premier temps, il est **pratique** de déterminer la masse d'une «&nbsp;rame de papier&nbsp;»&nbsp;: $M(1 \text{ rame}) = \pu{80 g/m2} \times (\pu{210e-3 m} \times \pu{297e-3 m}) \times 500 =  \pu{2,5e3 g} = \pu{2,5 kg}$.
- Au cours d'une livraison le transporteur peut livrer au maximum 2812 rames, donc $m_{\text{max}} = 2812 \times \pu{2,5 kg} = \pu{7,3e3 kg}$.
{{% /solution %}}

9. Un « Renault Trafic » peut transporter une charge utile environ égale à $\pu{1,2e3 kg}$. Le transporteur étant tenu de respecter cette valeur, le nombre de voyages calculé à la question 7 convient-il ?
{{% solution "Réponse" %}}
La masse maximale calculée à la question précédente est bien trop importante comparée à la capacité de livraison de la camionnette. Le transporteur devra effectuer davantage de livraisons.  
Se baser sur le volume de charge comme nous l'avons fait dans cet exercice n'était pas une bonne idée. Il aurait été préférable de d'abord réfléchir à partir des masses.
{{% /solution %}}

10. En conclusion, quelles sont les caractéristiques d'une «&nbsp;rame de papier&nbsp;»&nbsp;?
{{% solution "Réponse" %}}
Une «&nbsp;rame de papier&nbsp;»&nbsp;:
- contient 500 feuilles&nbsp;;
- possède une masse&nbsp;: $M(1 \text{ rame}) = \pu{2,5 kg}$&nbsp;;
- possède un volume&nbsp;: $V(1 \text{ rame}) = \pu{3,2e-3 m3}$.
{{% /solution %}}

11. Serait-il possible de parler « d’une rame de crayons » (supposés tous identiques) ? En cas de réponse affirmative, indiquer ce qu’auraient en commun une « rame de papier » et une « rame de crayons ».
{{% solution "Réponse" %}}
Une «&nbsp;rame de papier&nbsp;» et une «&nbsp;rame de crayons&nbsp;» seraient constitués de 500 objets.
{{% /solution %}}

## Conclusion


{{% note tip %}}
On peut être amené à créer de **nouvelles grandeurs** pour exprimer le *nombre d'objets*&nbsp;:
- Parce que les instruments de mesures ne sont pas toujours adaptés aux caractéristiques de ces objets&nbsp;;
- Parce qu'il peut être plus pratique de manipuler les objets par «&nbsp;paquets&nbsp;».
{{% /note %}}

{{% note tip %}}
La **nouvelle grandeur**&nbsp;:
- **est définie** par le nombre d'objets quelle regroupe&nbsp;;
- **possède des caractéristiques** pratiques à connaître telles qu'une **masse** et un **volume**.
{{% /note %}}

12. Indiquer des grandeurs semblables à la «&nbsp;rame de papier&nbsp;» que l'on utilise dans la vie de tous les jours et donner leur définition.
{{% solution "Réponse" %}}
- Le «&nbsp;pack&nbsp;» de lait, d'eau, de Coca, etc. Il s'agit d'un regroupement de 6 objets.
- La «&nbsp;douzaine&nbsp;» d'huîtres, d'œufs, etc. Il s'agit d'un regroupement de 12 objets.
{{% /solution %}}
