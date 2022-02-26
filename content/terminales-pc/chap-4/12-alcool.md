---
title: "Annale : Les dangers de l'alcool (extraits)"
subtitle: "Chapitre 5,13"
author: ""
type: ""
date: 2020-10-28T22:10:10+04:00
draft: false
toc: true
tags: ["Beer-Lambert", "Dosage par étalonnage", "Spectroscopie IR", "Groupes caractéristiques", "Fonctions chimiques"]
categories: ["Chimie", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: true
auto_numbering: true
mermaid: true
---

On trouve dans un document publié par l'Institut suisse de prévention de l'alcoolisme (ISPA) les informations suivantes&nbsp;:  
Quand une personne consomme de l'alcool, celui-ci commence immédiatement à passer dans le sang. Plus le passage de l'alcool dans le sang est rapide, plus le taux d'alcool dans le sang augmentera rapidement, et plus vite on sera ivre. L'alcool est éliminé en majeure partie par le foie. Dans le foie, l'alcool est éliminé en deux étapes grâce à des enzymes. Dans un premier temps, l'alcool est transformé en éthanal par l'enzyme alcool déshydrogénase (ADH). L'éthanal est une substance très toxique, qui provoque des dégâts dans l'ensemble de l'organisme. Il attaque les membranes cellulaires et cause des dommages indirects en inhibant le système des enzymes. Dans un deuxième temps, l'éthanal est métabolisé par l'enzyme acétaldéhyde déshydrogénase (ALDH).

{{< mermaid >}}
graph TD;
    A[Alcool pur&nbsp;: Ethanol C] -->|Enzyme ADH| B(Ethanal);
    B --> |Dégradation ultérieure| C(Synthèse du cholestérol);
{{< /mermaid >}}

<div style="text-align: right;">
www.sfa-ispa.ch
</div>

## Spectroscopie IR

On se propose d'étudier la structure et les fonctions organiques de ces molécules par spectroscopie IR.

> Document 1a&nbsp;: Spectroscopie Infrarouge en phase liquide. Spectre IR1 (abscisse en $\pu{cm-1}$)

<img src="/terminales-pc/chap-4/chap-4-12-1.png" alt="" width="100%" />

> Document 2b&nbsp;: Spectroscopie Infrarouge en phase liquide. Spectre IR2 (abscisse en $\pu{cm-1}$)

<img src="/terminales-pc/chap-4/chap-4-12-2.png" alt="" width="100%" />

| Liaison | $\ce{C - C}$ | $\ce{C - O}$ | $\ce{C = O}$ (carbonyle) | $\ce{C - H}$ | $\ce{O - H}$ |
| :---: | :---: | :---: | :---: | :---: | :---: |
| **Nombre d'onde ($\pu{cm-1}$)** | 1000-1250 | 1050-1450 | 1650-1740 | 2800-3000 | 3200-3700 |

1. Le document en introduction évoque les molécules d'éthanol, de formule $\ce{C2H6O}$, et d'éthanal, de formule $\ce{C2H4O}$&nbsp;: représenter en formule semi-développée ces deux molécules et encadrer leurs fonctions caractéristiques.

{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-4/chap-4-12-3.png" alt="" width="40%" />
{{% /solution %}}

2. Quel est le nom du groupe fonctionnel porté par l'éthanol&nbsp;? À quelle famille appartient cette molécule&nbsp;?

{{% solution "Réponse" %}}
L'éthanol possède un groupe hydroxyle. Cette molécule fait partie de la famille des alcools.
{{% /solution %}}

3. Quel est le nom du groupe fonctionnel porté par l'éthanal&nbsp;? À quelle famille appartient cette molécule&nbsp;?

{{% solution "Réponse" %}}
L'éthanal possède un groupe carbonyle. Cette molécule fait partie de la famille des aldéhydes.
{{% /solution %}}

4. En utilisant les données spectroscopiques, associer chaque spectre infrarouge (IR) à la molécule correspondante en justifiant.

{{% solution "Réponse" %}}
- Le spectre IR2 montre une bande large et intense autour de $\pu{3300 cm–1}$ qui caractérise le groupe hydroxyle de l’éthanol.
- Le spectre IR1 montre une bande fine et intense autour de $\pu{1700 cm–1}$ qui caractérise le groupe carbonyle de l’éthanal.
{{% /solution %}}

## Contrôle de qualité d'un vin&nbsp;: dosage par spectrophotométrie de l'éthanol

On peut lire dans le *code de la santé publique* depuis juin 2000&nbsp;: catégorie *Vins doux*&nbsp;: vins, apéritifs à base de vin ne titrant pas plus de 18 degrés.   
On se propose de vérifier en laboratoire si un vin obéit à cette législation.

#### Définition
Le **titre alcoométrique**, exprimé en degré, est égal au nombre de litres d'éthanol contenus dans 100 litres de vin.

#### Données
- $M(éthanol) = \pu{46,0 g.mol-1}$&nbsp;;
- $\rho(\text{éthanol}) = \pu{0,78 g.mL-1}$.

Afin de procéder au contrôle, on réalise le titrage par spectrophotométrie du vin en suivant le protocole suivant&nbsp;:
- *Première étape&nbsp;:* On recueille l'éthanol du vin par distillation.
- *Deuxième étape&nbsp;:* L'éthanol est oxydé par la NAD+ dans une réaction catalysée par une enzyme spécifique. La réaction produit de la nicotinamide-adénine-dinucléotide réduite ($\ce{NADH}$) en quantité de matière égale à celle de l'éthanol dosé selon l'équation&nbsp;:
$$
\ce{Ethanol + NAD^+	-> Ethanal + NADH + H^+ }
$$
- *Troisième étape&nbsp;:* La $\ce{NADH}$ absorbant dans le domaine UV, on mesure son absorbance par spectrophotométrie.

L'étalonnage du spectrophotomètre avec différentes solutions d'éthanol permet de vérifier la loi de Beer-Lambert&nbsp;: $A = k \\, C_m$ avec $k = \pu{1,6e–3 L.mg-1}$ et $C_m$ la concentration massique d'éthanol dans l'échantillon.

*Réalisation de la mesure&nbsp;:*
- On distille $\pu{10 mL}$ de vin&nbsp;;
- Le distillat est ensuite ajusté à $\pu{100 mL}$ avec de l'eau distillée pour obtenir une solution appelée $S$.
- On prépare l'échantillon à doser par spectrophotométrie en introduisant dans une fiole jaugée de $\pu{100 mL}$&nbsp;:
    - $\pu{1 mL}$ de solution $S$&nbsp;;
    - le catalyseur&nbsp;;
    - $\ce{NAD^+}$ en excès&nbsp;;
	- On complète avec de l'eau distillée.

L'absorbance mesurée pour cet échantillon vaut&nbsp;: $A_e = \pu{0,15}$.

5. Déterminer à partir de l'absorbance mesurée $A_e$, la concentration massique $C_m$ en éthanol de l'échantillon étudié.

{{% solution "Réponse" %}}
D'après la loi de Beer-Lambert, $A = k \cdot C_m$, donc $C_m = \dfrac{A}{k} $.  **A.N.** $C_m = \dfrac{\pu{0,15}}{\pu{1,6e–3 L.mg-1}} = \pu{94 mg.L-1} = \pu{9,4e-2 g.L-1}$.
{{% /solution %}}

6. En tenant compte des deux dilutions successives, calculer les concentrations massiques en éthanol suivantes&nbsp;:
    - $C_S$ dans la solution $S$.
	- $C_V$ dans le vin.

{{% solution "Réponse" %}}
- Détermination de $C_S$&nbsp;:
    On a prélevé la masse $m_P = C_S \cdot V_P$ dans la solution $S$ et on a fabriqué une solution fille de volume $V_f$ et de concentration $C_m$, soit contenant la masse $m_f = V_f \cdot C_m$. Comme la masse se conserve au cours de cette opération, $C_S \cdot V_P = V_f \cdot C_m \iff C_S = C_m \\, \dfrac{V_f}{V_P}$.   
    <strong>A.N.</strong> $C_S = \pu{9,4e-2 g.L-1} \times \dfrac{\pu{100 mL}}{\pu{1 mL}} = \pu{9,4 g.L-1}$.

- Détermination de $C_V$&nbsp;: Le raisonnement est identique $C_S = \pu{9,4 g.L-1} \times \dfrac{\pu{100 mL}}{\pu{10 mL}} = \pu{94 g.L-1}$.

{{% /solution %}}

7. Quelle est la valeur du titre alcoométrique exprimé en degrés du vin&nbsp;?

{{% solution "Réponse" %}}
Le titre alcoométrique est égal au nombre de litres d'éthanol contenus dans 100 litres de vin, or 100 L de vin contiennent une masse égale à $m = 100 C_V$. Cette masse occupe un volume $V= \dfrac{m}{\rho} = \dfrac{100 C_V}{\rho}$.  
<strong>A.N.</strong> $V= \dfrac{100 \times \pu{94 g.L-1}}{\pu{0,78 g.mL-1}} = \pu{1,2e4 mL} = \pu{12 L}$.   
Le titre alcoométrique est de 12°.
{{% /solution %}}

8. Ce vin est-il conforme au code de la santé publique&nbsp;?

{{% solution "Réponse" %}}
Le titre alcoométrique est inférieur à 18°, le vin est donc conforme au code de la santé publique.
{{% /solution %}}
