---
title: "Évaluer l'atténuation du signal dans une fibre optique"
subtitle: "Chapitre 1.4"
author: ""
type: ""
date: 2020-09-18T14:52:43+04:00
draft: false
toc: true
tags: ["Absorption", "Atténuation", "Ondes", "Fibre optique"]
categories: ["Physique", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: false
auto_numbering: true
---

## Exercice

La puissance lumineuse d'un signal transmis par une fibre optique décroît avec la distance qu'il parcourt. 

Le **coefficient d'atténuation linéique** $\alpha$ caractérise cette décroissance. ll est défini par la relation&nbsp;:
$$ \alpha = \dfrac{10}{L} \\, \log \left( \dfrac{ \cal I_e }{ \cal I_s } \right) $$
$\alpha$ est exprimé en décibel par unité de longueur ($\pu{dB/m}$), $L$ est la longueur de la fibre en mètre, $\cal I_e$ et $\cal I_s$ sont respectivement les
**intensités en entrée et en sortie du signal**.

*Ce coefficient d'atténuation $\alpha$ dépend du matériau et de la longueur d'onde $\lambda$ de la radiation utilisée*.

Le graphique ci-dessous représente le coefficient d'atténuation linéique dans une fibre optique en fonction de la longueur d'onde de la radiation utilisée.

<img src="/terminales-pc/chap-1/chap-1-4-1.jpg" alt="" width="60%" />

1. Dans le domaine du spectre électromagnétique concerné, quelle radiation est transmise avec le moins d'atténuation&nbsp;?
{{% solution "Réponse" %}}
Le coefficient d'atténuation linéique est minimal pour une longueur d'onde proche de $\pu{1,6 \mu m}$. Le rayonnement à cette longueur d'onde est donc celui qui est le moins atténué lorsqu'il se propage.
{{% /solution %}}

2. Calculer alors pour cette radiation le rapport des puissances d'entrée et de sortie $\left( \dfrac{ \cal I_e }{ \cal I_s } \right)$ pour une fibre de $\pu{100 km}$ de longueur.
{{% solution "Réponse" %}}
- $ \alpha = \dfrac{10}{L} \\, \log \left( \dfrac{ \cal I_e }{ \cal I_s } \right) \Leftrightarrow \log \left( \dfrac{ \cal I_e }{ \cal I_s } \right) = \dfrac{\alpha \\, L}{10} \Leftrightarrow \left( \dfrac{ \cal I_e }{ \cal I_s } \right) = 10^{ \dfrac{\alpha \\, L}{10} }$.

- **A.N.** $ \left( \dfrac{ \cal I_e }{ \cal I_s } \right) = 10^{ \dfrac{\pu{0,2 dB/km} \times \pu{100 km} }{10} } = \pu{1e2}$.
{{% /solution %}}

3. Lequel des phénomènes suivants peut être à l'origine du pic observé pour $\lambda \approx \pu{1,4 \mu m}$&nbsp;: **la diffraction**&nbsp;; **la transmission**&nbsp;; **l'absorption**&nbsp;; **la réfraction**&nbsp;; **la réflexion**.

{{% solution "Réponse" %}}
L'atténuation est très importante pour les rayonnements de longueur d'onde $\lambda \approx \pu{1,4 \mu m}$. Le phénomène qui peut provoquer une atténuation importante est l'**absorption** de la radiation par le matériau.
{{% /solution %}}

La maîtrise des procédés de fabrication des fibres optiques permet de limiter considérablement leur coefficient d'atténuation linéique.  
Par exemple, il reste 1,00&nbsp;% de l'intensité en entrée après une propagation sur une distance de $\pu{100 km}$ de signaux de longueur d'onde dans le vide égale à $\pu{1 550 nm}$. Cette puissance est suffisante pour que ces signaux soient détectés.

4. Quel est le coefficient d'atténuation linéique&nbsp;?
{{% solution "Réponse" %}}
- D'après l'énoncé, $ \left( \dfrac{ \cal I_s }{ \cal I_e } \right) = \pu{1,00e-2}$ donc $ \left( \dfrac{ \cal I_e }{ \cal I_s } \right) = \pu{1,00e2}$.

- $ \alpha = \dfrac{10}{L} \\, \log \left( \dfrac{ \cal I_e }{ \cal I_s } \right) $, donc $ \alpha = \dfrac{ 10 }{ \pu{100 km} } \times \log \left( \pu{1,00e2} \right) = \pu{2,00e-1 dB/km}$.
{{% /solution %}}

## En résumé

{{% note tip %}}
Au cours de sa propagation une onde s'**atténue**. Cette atténuation existe&nbsp;:
- *parce que l'énergie se répartie sur des fronts d'onde de plus en plus grand au fur et à mesure que l'onde s'éloigne de sa source*&nbsp;;
- parce, **dans certains cas**, *l'onde cède une partie (ou la totalité) de son énergie au milieu dans lequel elle se propage*.
{{% /note %}}