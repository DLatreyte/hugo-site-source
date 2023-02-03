---
title: "Manuel numérique Hatier : Exercices du chapitre"
subtitle: ""
author: ""
type: ""
date: 2023-02-02T21:29:06+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice n°43, page 233 : Boire avec une paille

1. L'eau est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides. Comme l'axe $(Oz)$ est orienté vers le haut,
$$
p(z) + \rho_{\text{eau}}\\, g z = \text{cste}
$$
Appliquée au point d'altitude $z_1$ et au point $F$, au fond du verre, la relation s'écrit,
$$
p(z_1)+\rho_{\text{eau}}\\,  g z_1 = p_\text{fond} +\rho_{\text{eau}}\\,  g \times 0
$$
​  ou
$$
p_\text{fond} = p_0+\rho_{\text{eau}}\\,  g z_1
$$
​  puisque $p(z_1) = p_0$ (ce point se trouve à l'interface de l'air et de l'eau).  
**A.N.** $p_\text{fond} =\pu{1,013e5 Pa} + \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times \pu{9,5e-2 m} = \pu{1,02e5 Pa}$  
**Remarque :** j'ai conservé plus de chiffres significatifs qu'attendus pour montrer la variation de pression.

2. On applique la loi de la statique des fluides dans la paille entre les points d'altitude $z_1$ et $z_2$ :
    $$
    p(z_1)+\rho_{\text{eau}}\\,  g z_1 = p_2 +\rho_{\text{eau}}\\,  g z_2
    $$
    Comme $p(z_1)=p_0$, on a
    $$
    p_0 - p_2 = \rho_{\text{eau}}\\,  g (z_2 - z_1)
    $$
    **Rappel :** le point d'altitude $z_1$, dans la paille, n'est pas en contact avec l'air mais, comme seule l'altitude compte pour la pression, il possède la même pression que les points à la même altitude au contact de l'air.

3. À partir de la relation précédente, on obtient :
    $$
    p_2 =p_0 - \rho_{\text{eau}}\\,  g (z_2 - z_1)
    $$
    **A.N.** $p_2 = \pu{1,013e5 Pa} - \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times(\pu{25e-2 m} - \pu{9,5e-2 m}) = \pu{0,998e5 Pa} = \pu{998 hPa}$.

    La dépression maximale que l'on peut créer dans la cavité bucale est bien supérieure à celle attendue pour élever un liquide jusqu'à l'altitude $\pu{25cm}$ depuis l'altitude $\pu{9,5 cm}$.

## Exercice n°44, page 233 : Barrage hydroélectrique

1. L'eau est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides. Comme l'axe $(Oz)$ est orienté vers le haut,
    $$
    p(z) + \rho_{\text{eau}}\\,  g z = \text{cste}
    $$
    Appliquée à la situation étudiée, la relation s'écrit,
    $$
    p(z_1) + \rho_{\text{eau}}\\,  g z_1 = p(z_2) + \rho_{\text{eau}}\\,  g z_2
    $$
    Comme le point d'altitude $z_1$ se trouve à l'interface entre l'air et l'eau, $p(z_1)=p_0$ et
    $$
    p_0 + \rho_{\text{eau}}\\,  g z_1 = p(z_2) + \rho_{\text{eau}}\\,  g z_2 \iff p(z_2) = p_0 + \rho_{\text{eau}}\\,  g (z_1 - z_2)
    $$
    **A.N.** $p(z_2) = \pu{1,013e5 Pa} + \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times (\pu{70 m} - \pu{5 m}) = \pu{7,4e5 Pa}$.

2. La valeur de la force pressante qu'exerce l'eau au niveau de la vanne a pour expression
    $$
    F_{\text{eau}} = p(z_2) S
    $$
    **A.N.** $F_{\text{eau}} = \pu{7,4e5 Pa} \times \pu{1,2 m2} = \pu{8,9e5 N}$.

3. La valeur de la force pressante qu'exerce l'air au niveau de la vanne a pour expression
    $$
    F_{\text{air}} = p_0 S
    $$
    **A.N.** $F_{\text{air}} = \pu{1,013e5 Pa} \times \pu{1,2 m2} = \pu{1,2e5 Pa}$.

    $\dfrac{F_{\text{air}}}{F_{\text{eau}}} = \dfrac{\pu{1,2e5 Pa}}{\pu{8,9e5 N}} = \pu{0,14}$.

    La force pressante qu'exerce l'eau sur la barrage est plus de 7 fois plus grande que la force pressante qu'exerce l'air sur le barrage (ces deux forces ont des sens opposés). Cette dernière n'est donc pas suffisante pour compenser la force qu'exerce l'eau ; le barrage doit posséder une structure suffisamment solide pour résister à l'action de l'eau.

4. **A.N.** $p(z_3) = \pu{1,013e5 Pa} + \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times (\pu{70 m} - \pu{35 m}) = \pu{4,4e5 Pa}$.

5. **A.N.** $F = \pu{4,4e5 Pa} \times (\pu{70 m} \times \pu{120 m}) = \pu{3,7e9 Pa}$.

## Exercice n°45, page 233 : Vinaigrette

1. $H_{\text{vinaigre}} = z_1$.

2. $H_{\text{huile}} = z_2 - z_1$.

3. L'huile est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides. Comme l'axe $(Oz)$ est orienté vers le haut,
    $$
    p(z) + \rho_{\text{huile}}\\, g z = \text{cste}
    $$
    Appliquée à la situation étudiée, la relation s'écrit,
    $$
    p(z_1) + \rho_{\text{huile}}\\, g z_1 = p(z_2) + \rho_{\text{huile}}\\, g z_2 \iff p(z_1) = p(z_2) + \rho_{\text{huile}}\\, g (z_2 - z_1)
    $$
    Comme le point d'altitude $z_2$ se trouve à l'interface entre l'air et l'eau, $p(z_2)=p_0$​ et
    $$
    p(z_1) = p_0 + \rho_{\text{huile}}\\, g H_{\text{huile}}
    $$
    **A.N.** $p(z_1) = \pu{1,013e5 Pa} + \pu{920 kg.m-3} \times \pu{9,81 N.kg-1} \times \pu{7e-2 m} = \pu{1,019e5 Pa}$.

4. Le vinaigre est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides :
    $$
    p(z_1) + \rho g z_1 = p_{\text{fond}} \iff p_{\text{fond}} = p(z_1) + \rho g H_{\text{vinaigre}}
    $$
    **A.N.** $p_{\text{fond}} = \pu{1,019e5 Pa} + \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times \pu{5e-2 m} = \pu{1,024e5 Pa}$.

## Exercice n°47, page 234 : Tube en U

1. $H=z_3-z_1$.

2. $h=z_2-z_1$.

3. L'huile est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides. Comme l'axe $(Oz)$ est orienté vers le haut,
    $$
    p(z) + \rho_{\text{huile}}\\, g z = \text{cste}
    $$
    Appliquée à la situation étudiée, la relation s'écrit,
    $$
    p(z_1) + \rho_{\text{huile}}\\, g z_1 = p(z_3) + \rho_{\text{huile}}\\, g z_3 \iff p(z_1) = p(z_3) + \rho_{\text{huile}}\\, g H
    $$
    Comme le point d'altitude $z_3$ se trouve à l'interface entre l'air et l'eau, $p(z_3)=p_0$​ et
    $$
    p(z_1) = p_0 + \rho_{\text{huile}}\\, g H
    $$

4. L'eau est considérée incompressible, il donc possible d'y appliquer la loi de la statique des fluides.
    $$
    p(z_1) + \rho_{\text{eau}}\\, g z_1 = p(z_2) + \rho_{\text{eau}}\\, g z_2
    $$
    Le point d'altitude $z_2$ se trouve à l'interface entre l'eau et l'air, on a donc $p(z_2) = p_0$.

    Finalement
    $$
    p(z_1) = p_0 + \rho_{\text{eau}}\\, g (z_2 - z_1) \iff p(z_1) = p_0 + \rho_{\text{eau}}\\, g h
    $$

5. Le point d'altitude $z_1$ se trouve dans la colonne d'eau à droite mais aussi à l'interface entre l'eau et l'huile, la pression y est donc égale à celle calculée à la question 3. On a donc
    $$
    p_0 + \rho_{\text{eau}}\\, g h =p_0 + \rho_{\text{huile}}\\, g H \iff \rho_{\text{eau}} h = \rho_{\text{huile}} H
    $$
    Finalement
    $$
    \rho_{\text{huile}} = \rho_{\text{eau}} \dfrac{h}{H}
    $$
    **A.N.** $\rho_{\text{huile}} = \pu{1,0e3 kg.m-3} \times \dfrac{\pu{8,4 cm}}{\pu{10 cm}} = \pu{8,4e2 kg.m-3}$.

6. Lorsque le dessus de la couche de pétrole est mis à l’air libre après le coup de pioche, on retrouve une situation semblable à celle de l'exercice, si ce n'est que le niveau de pétrole est plus bas que le niveau de l'huile dans le tube en U. Il se met donc en mouvement pour atteindre une hauteur similaire à celle de l'huile dans l'exercice.

## Exercice n°48, page 234 : Plongée en apnée

1.

- On considère que l'air emprisonné dans les poumons est un gaz parfait ; on peut donc appliquer la loi de Boyle-Mariotte $$p\\, V = \text{cste}$$
$$p_0\\, V_0 = p_1\\, V_R \iff p_1 = p_0 \\, \dfrac{V_0}{V_R}$$
**A.N.** $p_1 = \pu{1,013e5 Pa} \times \dfrac{\pu{6,0 L}}{\pu{1,5 L}} = \pu{4,1e5 Pa}$.

- Pour déterminer la relation avec la profondeur $h_1$, on considère que l'eau est un fluide incompressible. De plus, on utilise un axe $(Oz)$ dirigé vers le haut, dont l'origine est située à la surface de la mer. On peut alors utiliser la loi fondamentale de la statique des fluides $$p(z) + \rho_{\text{eau}}\\, g z = \text{cste}$$
Appliquée à la situation, la relation devient $$p(z_1) + \rho_{\text{eau}}\\, g z_1 = p_0 \iff z_1 = \dfrac{p_0 - p(z_1)}{\rho_{\text{eau}}\\, g}$$
Comme $h_1 = -z_1$, vu le choix de position de l'origine,
$$h_1 = \dfrac{p(z_1) - p_0}{\rho_{\text{eau}}\\, g}$$
**A.N.** $h_1 = \dfrac{\pu{4,1e5 Pa} - \pu{1,013e5 Pa}}{\pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1}} = \pu{3,1e1 m}$

2. On utilise ici aussi la loi fondamentale de la statique des fluides,
$$p(z_2) + \rho_{\text{eau}}\\, g z_2 = p_0 \iff p(z_2) = p_0 - \rho_{\text{eau}}\\, g z_2$$
Comme $h_2 = -z_2$, vu le choix de position de l'origine,
$$ p(z_2) = p_0 + \rho_{\text{eau}}\\, g h_2$$
**A.N.** $ p(z_2) = \pu{1,013e5 Pa} + \pu{1,0e3 kg.m-3} \times \pu{9,81 N.kg-1} \times \pu{200 m} = \pu{2,1e6 Pa}$.

3. L'application de la loi de Boyle-Mariotte permet d'écrire
$$p(z_2) \\, V_2 = p_0 \\, V_0 \iff V_2 = V_0\\, \dfrac{p_0}{p(z_2)}$$
**A.N.** $V_2 = \pu{6,0 L} \times \dfrac{\pu{1,013e5 Pa}}{\pu{2,1e6 Pa}} = \pu{2,9e-1 m3}$.

4. D'après l'énoncé, le sang, liquide incompressible, assure le maintien du volume pulmonaire.

## Exercice n°49, page 234 : Presse hydraulique

1. Au sein d'un liquide la pression ne dépend que de l'altitude. Les deux pistons étant à la même altitude, la pression est identique à leur niveau.

2. **Remarque :** les pistons sont considérés sans masse, ils n'interagissent donc pas avec la Terre.

- **Grand piston**
  - Le piston est soumis à l'action de l'huile : $\overrightarrow{F}_{\text{huile}/\text{piston}}$ :
    - *Direction :* droite perpendiculaire au piston
    - *Sens :* de l'huile vers le piston (vers le haut donc)
    - *Valeur :* $F_{\text{huile}/\text{piston}} = p_{\text{huile}} S$
  - Le piston est soumis à l'action de l'air : $\overrightarrow{F}_{\text{air}/\text{piston}}$ :
    - *Direction :* droite perpendiculaire au piston
    - *Sens :* de l'air vers le piston (vers le bas donc)
    - *Valeur :* $F_{\text{air}/\text{piston}} = p_{\text{air}} S$
  - Le piston est soumis au poids de la masse $\overrightarrow{P}$ :
    - *Direction :* droite perpendiculaire au piston
    - *Sens :* vers le centre de la Terre (vers le bas donc)
    - *Valeur :* $P = M g$
  - Puisque le piston est immobile, les actions qui s'exercent sur lui se compensent :
    $$
    \overrightarrow{F}\_{\text{huile}/\text{piston}} + \overrightarrow{F}\_{\text{air}/\text{piston}} + \overrightarrow{P} = \vec{0}
    $$
    soit, si on projette sur un axe vertical orienté vers le haut,
    $$
    F_{\text{huile}/\text{piston}} - F_{\text{air}/\text{piston}} - P = 0 \iff
    F_{\text{huile}/\text{piston}} = F_{\text{air}/\text{piston}} + P
    $$
    Finalement
    $$
    p_{\text{huile}} S = p_{\text{air}} S + M g \iff
    p_{\text{huile}} = p_{\text{air}} + \dfrac{M g}{S}
    $$
  - **Petit piston**
    - À l'aide du même raisonnement, on montre qu'au niveau du petit piston,
    $$
    p_{\text{huile}} s = p_{\text{air}} s + m g \iff
    p_{\text{huile}} = p_{\text{air}} + \dfrac{m g}{s}
    $$
  - **Synthèse :** dans les deux sections précédentes, on a obtenu deux expressions différentes d'une même grandeur, la pression de l'huile à l'altitude des pistons ; ces expressions sont forcément identiques :
  $$
    p_{\text{air}} + \dfrac{m g}{s} = p_{\text{air}} + \dfrac{M g}{S} \iff \dfrac{m}{s} = \dfrac{M}{S}
  $$

3. $$M = m \\, \dfrac{S}{s}$$
    **A.N.** $M = \pu{50 kg} \times \dfrac{100 s}{s} = \pu{5,0e3 kg}$. Grâce à la presse il est possible de compenser le poids d'une masse de 5,0 t à l'aide d'une masse de 50 kg !

4. On a démontré que $$p_{\text{huile}} = p_{\text{air}} + \dfrac{M g}{S}$$  
    **A.N.** $p_{\text{huile}} = \pu{1,013e5 Pa} + \dfrac{\pu{5,0e3 kg} \times \pu{9,81 N.kg-1}}{100 \times \pu{1,0e-4 m2}} = \pu{5,0e6 Pa}$.
