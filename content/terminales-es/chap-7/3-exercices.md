---
title: "Exercices du chapitre"
subtitle: "Chapitre 3,3"
author: ""
type: ""
date: 2021-02-04T09:16:11+04:00
draft: false
toc: true
tags: []
categories: ["Terminale Enseignement Scientifique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

- Exercice n°11 : Transformateur
    - {{< remote "Lien vers le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663478" >}}

{{% solution "Correction" %}}

1. $m = \dfrac{N_2}{N_1}$     
    **A.N.** $m = \dfrac{115}{500} = \pu{0,23}$

2. $U_2 = m\, U_1$    
    **A.N.** $U_2 = \pu{0,23} \times \pu{1000 V} = \pu{230 V}$

3. On sait que $P_1 = U_1 \, I_1$, donc $I_1 = \dfrac{P_1}{U_1}$.     
    **A.N.** $I_1 = \dfrac{\pu{11,5e3 W}}{\pu{1000 V}} = \pu{11,5 A}$

4. $I_2 = \dfrac{I_1}{m}$      
    **A.N.** $I_2 = \dfrac{\pu{11,5 A}}{\pu{0,23}} = \pu{50 A}$

#### D'où provient l'énergie communiquée au secondaire ?

Si on note $P_2$ la puissance délivrée au niveau du circuit secondaire, $P_2 = U_2\, I_2$.     
**A.N.** $P_2 = \pu{230 V} \times \pu{50 A} = \pu{11,5e3 W}$

L'énergie fournie au secondaire en sortie du transformateur est égale à l'énergie fournie par le circuit primaire.
{{% /solution %}}

- Exercice n°13 : Application de la théorie des graphes
    - {{< remote "Lien vers le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663478" >}}

{{% solution "Correction" %}}

1. **Faux**. Il n'existe aucun chemin partant des nœuds $F$ et $G$.
2. **Vrai**. Tous les nœuds sont bien atteignables depuis le nœud $A$.
3. **Faux**. Il n'existe toujours aucun chemin partant des nœuds $F$ et $G$.      
    **Faux**. Aucun chemin issu de $A$ ne permet d'atteindre le sommet $D$.

{{% /solution %}}

- Exercice n°19 : Un problème de graphe
    - {{< remote "Lien vers le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663650" >}}

{{% solution "Correction" %}}

1. $M \longrightarrow 1 \longrightarrow 8 \longrightarrow 7 \longrightarrow M$
2. $T \longrightarrow 6 \longrightarrow 5 \longrightarrow 4 \longrightarrow C \longrightarrow M$    
    Il n'existe aucun chemin issu de $T$ qui permet d'atteindre $M$ sans passer par $C$.

{{% /solution %}}

- Exercice n°20 : Modélisation du réseau électrique
    - {{< remote "Lien vers le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663717" >}}

{{% solution "Correction" %}}

1. $A \longrightarrow b \longrightarrow c \longrightarrow f \longrightarrow l \longrightarrow B$      
    $A \longrightarrow a \longrightarrow g \longrightarrow h \longrightarrow k \longrightarrow B$      
    $A \longrightarrow a \longrightarrow d \longrightarrow e \longrightarrow i \longrightarrow k \longrightarrow B$

2. On postule ici que les chemins les plus courts (en terme de sommets visités) sont les plus rapides.    
    $A \longrightarrow a \longrightarrow g \longrightarrow h \longrightarrow k \longrightarrow B$      
    $A \longrightarrow b \longrightarrow e \longrightarrow i \longrightarrow k \longrightarrow B$      
    $A \longrightarrow b \longrightarrow c \longrightarrow f \longrightarrow l \longrightarrow B$      
    $A \longrightarrow b \longrightarrow e \longrightarrow f \longrightarrow l \longrightarrow B$

3. Le graphe est pondéré par les débits maximum sur chaque lien. Comme les voitures ne peuvent pas s'accumuler au niveau des nœuds, le débit envisageable de $A$ à $B$ ne peut être que le débit minimum 

{{% /solution %}}

- Exercice n°21 : Limiter les pertes
    - {{< remote "Lien vers le Livre Scolaire" "https://www.lelivrescolaire.fr/page/10663717" >}}

{{% solution "Correction" %}}

1. L’intensité maximale du courant pouvant traverser un câble haute tension de section $\pu{500 mm2}$ vaut&nbsp;: $I_{max} = \pu{0,7} \times \pu{500 mm2} = \pu{350 A}$.

2. 
- La résistance du câble est égale à : $R = \dfrac{U}{I} = \dfrac{\pu{400e3 V}}{\pu{350 A}} = \pu{1,14e3 \Omega}$&nbsp;;
-  La puissance dissipée par effet Joule est alors égale à&nbsp;: $P = R\\, I^2 = \pu{1,14e3 \Omega} \times (\pu{350 A})^2 = \pu{1,40e6 W} = \pu{140 MW}$.

3. 
- Lorsque le câble est dédoublé, l’intensité du courant électrique est divisée par deux, donc $I' = \pu{175 A}$&nbsp;;
- La nouvelle résistance vaut donc $R' = \dfrac{R}{2} = \dfrac{\pu{1,14e3 \Omega}}{2} = \pu{571 \Omega}$&nbsp;;
- La puissance dissipée  dans un câble par effet Joule est alors égale à&nbsp;: $P' = R'\\, I^2 = \pu{571 \Omega} \times (\pu{175 A})^2 = \pu{1,74e7 W} = \pu{17,4 MW}$.
{{% /solution %}}