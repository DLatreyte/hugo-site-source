---
title: "Annale : La houle et l’entrée d’un port"
subtitle: "Chapitre 3,2,3"
author: ""
type: ""
date: 2020-09-14T21:59:57+04:00
draft: false
toc: true
tags: ["Annale", "Diffraction", "Célérité"]
categories: ["Physique", "Terminale Spé PC", "Annale"]
image: ""
solution_est_visible: true
auto_numbering: true
---

On modélise l’entrée d’un port comme sur le schéma ci-dessous&nbsp;:

<img src="/terminales-pc/chap-2/fig-2-2-3-1.jpg" alt="" width="80%" />

Le port est séparé de la mer par deux digues. Une ouverture de largeur $L = \pu{25 m}$ permet aux bateaux d’y accéder.   
La houle est assimilée à une onde mécanique progressive et sinusoïdale, arrivant de l’ouest vers le port. Elle soulève périodiquement le petit bateau situé au large de l’entrée du port.  
La célérité $v$ d’une onde à la surface de l’eau dépend, entre autres, de la profondeur&nbsp;:
- Quand la profondeur $h$ de l’eau est très supérieure à la longueur d’onde $\lambda$, $v = \sqrt{ \dfrac{g \\, \lambda}{2 \\, \pi} }$&nbsp;;
- Quand la profondeur $h$ de l’eau est petite devant la longueur d’onde $\lambda$, $v = \sqrt{g \\, h}$.

Données
: Dans les relations précédentes, $g$ est l’accélération de la pesanteur et a pour valeur $g = \pu{9,8 m.s-2}$.

## En mer

Le petit bateau de pêche est en mer au large du port. La profondeur de l’eau à cet endroit est $h = \pu{800 m}$. La longueur d’onde de la houle est $\lambda = \pu{50 m}$.

1. Rappeler la définition d’une onde mécanique.
{{% solution "Réponse" %}}
*Une onde mécanique est la propagation de la perturbation d'un milieu de proche en proche, sans transport de matière*.
{{% /solution %}}

2. La houle est-elle une onde mécanique transversale ou longitudinale&nbsp;? Justifier la réponse.
{{% solution "Réponse" %}}
Le mouvement d'un bateau atteint par l'onde, à la surface de l'eau, est vertical. La houle (l'onde), elle, se déplace à la surface de l'eau, *donc perpendiculairement au déplacement de ce bateau*&nbsp;: c'est une *onde transversale*.
{{% /solution %}}

3. Rappeler la définition d’une onde sinusoïdale.
{{% solution "Réponse" %}}
Une onde sinusoïdale est une onde créée par *une source ayant un mouvement périodique sinusoïdal dans le temps*.
{{% /solution %}}

4. Rappeler les deux façons de définir la longueur d’onde.
{{% solution "Réponse" %}}
- La longueur d'onde est la **période spatiale** de l'onde&nbsp;: *c'est la plus petite distance au bout de laquelle on retrouve le même état vibratoire dans le milieu*.
- *La longueur est la distance parcourue par l'onde pendant une durée égale à la période temporelle* $T$.
{{% /solution %}}

5. Justifier, par analyse dimensionnelle, que l’expression $\sqrt{ \dfrac{g \\, \lambda}{2 \\, \pi} }$ est bien homogène à une célérité.
{{% solution "Réponse" %}}
**Remarque&nbsp;:** $[ a ]$ signifie «&nbsp;dimension de $a$&nbsp;».
- $[\lambda] = L$. La longueur d'onde est une longueur.
- $[g] = \dfrac{L}{T^2}$. $g$ est une longueur divisée par un temps au carré.   
**Remarque&nbsp;:** vous serez bientôt capable de le démontrer, pour l'instant vous pouvez vous appuyer sur les unités.
- Donc $\left[ \sqrt{ \dfrac{g \\, \lambda}{2 \\, \pi} } \right] = \left[ \sqrt{ g \\, \lambda } \right] = [g \\, \lambda]^{1/2} = \left( L \times \dfrac{L}{T^2} \right)^{1/2} = \left( \dfrac{L^2}{T^2} \right)^{1/2} = \dfrac{L}{T}$.   
C'est bien une vitesse.
{{% /solution %}}

6. Calculer la célérité de cette houle.
{{% solution "Réponse" %}}
- $h = \pu{800 m}$ et $\lambda = \pu{50 m}$, donc $h \gg \lambda$ et $v = \sqrt{ \dfrac{g \\, \lambda}{2 \\, \pi} }$.
- **A.N.** $v = \sqrt{ \dfrac{\pu{9,8 m.s-2} \times \pu{50 m}}{2 \\, \pi} } = \pu{8,8 m.s-1}$.
{{% /solution %}}

7. Calculer la fréquence du mouvement vertical du bateau.
{{% solution "Réponse" %}}
- Puisque la longueur d'onde est la distance parcourue par l'onde pendant la durée $T$, $\lambda = v T$. Puisque $T = \dfrac{1}{f}$, $\lambda = \dfrac{v}{f} \Leftrightarrow f = \dfrac{v}{\lambda}$.
- **A.N.** $f = \dfrac{ \pu{8,8 m.s-1} }{ \pu{50 m} } = \pu{0,18 Hz} $.
{{% /solution %}}


> On dit qu'un milieu est **dispersif** lorsque la célérité d'une onde mécanique qui s'y propage dépend non seulement des caractéristiques du milieu mais aussi de la fréquence de cette onde.

8. Quand la profondeur est grande devant $\lambda$, la mer est-elle un milieu de propagation dispersif pour la houle&nbsp;?   
Même question quand la profondeur est petite.
{{% solution "Réponse" %}}
- Quand la profondeur $h$ de l’eau est très supérieure à la longueur d’onde $\lambda$, $v = \sqrt{ \dfrac{g \\, \lambda}{2 \\, \pi} }$&nbsp;.  
On constate, dans cette expression, que la *célérité de l'onde dépend de la longueur d'onde* $\lambda$, donc de la fréquence $f$ de l'onde&nbsp;: *le milieu est dispersif*.

- Quand la profondeur $h$ de l’eau est petite devant la longueur d’onde $\lambda$, $v = \sqrt{g \\, h}$.  
On constate, dans cette expression, que la *célérité de l'onde ne dépend pas de la longueur d'onde* $\lambda$, donc de la fréquence $f$ de l'onde&nbsp;: *le milieu n'est pas dispersif*.
{{% /solution %}}

## Près de la côte

Près de la plage, la profondeur devient petite devant la longueur d’onde de la houle.

9. On considère la vague représentée sur la figure ci-dessous. Donner l’expression de la célérité de cette vague au point $A$ et celle au point $B$.  	
En quel point la célérité est la plus grande&nbsp;?

<img src="/terminales-pc/chap-2/fig-2-2-3-2.png" alt="" width="40%" />

{{% solution "Réponse" %}}
- À l'approche du rivage la profondeur devient petite devant la longueur d'onde de la houle, donc $v = \sqrt{g \\, h}$. La célérité est proportionnelle à $h^{1/2}$&nbsp;; c'est une fonction croissante de $h$.
- Puisque $H > h$, $v_A > v_B$.
{{% /solution %}}

10. En déduire que cette vague se déforme et représenter, sur un schéma simple, l’allure de la «&nbsp;vague&nbsp;» quelques instants plus tard.
{{% solution "Réponse" %}}
La crête de la vague se déplace plus vite que la base, elle finit donc pas déferler puisqu'elle n'a alors plus d'«&nbsp;appui&nbsp;».
{{% /solution %}}

## À l’entrée du port

À l’entrée du port, la profondeur vaut $h = \pu{2,4 m}$ et on observe un phénomène de diffraction.

11. Rappeler ce qu’est un phénomène de diffraction.
{{% solution "Réponse" %}}
*La diffraction est la perturbation de la propagation d'une onde lorsque cette dernière rencontre un obstacle ou une ouverture*.
{{% /solution %}}

12. Donner l’ordre de grandeur de la longueur d’onde d’une houle qui serait diffractée par l’ouverture entre les digues.
{{% solution "Réponse" %}}
On sait que le phénomène de diffraction devient « visible&nbsp;» lorsque l'ouverture (ou l'obstacle) a une dimension du même ordre de grandeur que la longueur d'onde de l'onde (sinusoïdale), donc $\lambda \approx L = \pu{25 m}$.
{{% /solution %}}

13. Calculer la célérité de cette onde.
{{% solution "Réponse" %}}
**A.N.** $v = \sqrt{\pu{9,8 m.s-2} \times \pu{2,4 m}} = \pu{4,8 m.s-1}$.
{{% /solution %}}

14. Sur un schéma simplifié, représenter, en vue de dessus, l’entrée du port, la houle incidente et l’onde diffractée, en justifiant succinctement la forme des ondes.
{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-2/chap-2-7-1.jpg" alt="" width="40%" />
- L'ouverture se comporte comme une **source secondaire** *vibrant à la même fréquence que la source primaire*. La forme des fronts d'onde est donc modifiée.
- L'onde se propage avant et après l'ouverture dans le même milieu. Si ce dernier est non dispersif sa célérité est donc inchangée et puisque la source secondaire vibre à la même fréquence que la source primaire, la longueur d'onde est inchangée elle-aussi.
**Remarque&nbsp;:** ce n'est pas tout à fait vrai dans cet exercice puisque la profondeur de l'eau varie et donc sa vitesse aussi.
{{% /solution %}}


