---
title: "Le problème du chasseur et du singe"
subtitle: ""
author: ""
type: ""
date: 2023-01-05T17:00:18+04:00
draft: false
toc: true
tags: []
categories: ["Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

<img src="/terminales-pc/chap-8/chap-8-18/monkey_and_hunter.gif" alt="" width="" />

Un chasseur vise directement, à l'aide de son arme, un singe suspendu à un arbre. À la date $t=0$, le projectile quitte l'arme.  Le singe, sur ses gardes, repère instantanément la menace et, effrayé, lache la branche à laquelle il était suspendu et se laisse tomber.

> La décision du singe vous semble-t-elle pertinente ?

#### Modélisation

- Le singe et le projectile sont modélisés par des points.
- L'interaction des systèmes avec l'air est négligée.
- On définit le repère de projection $(O; \vec{i}, \vec{j})$ tel que :
  - $O$ coïncide avec la position initiale du projectile,
  - $\vec{i}$ est le vecteur unitaire de l'axe $(Ox)$ horizontal,
  - $\vec{j}$ est le vecteur unitaire de l'axe $(Oy)$ vertical.
- Le chasseur se trouve à la distance (horizontale) $D$ de l'arbre.
- Le singe se trouve initialement à l'altitude $H$ dans le repère de projection.
- Le projectile quitte l'arme avec la vitesse $\overrightarrow{V_0}$ dont la direction passe par le singe et fait un angle $\alpha$ avec l'horizontale.
- Le champ de pesanteur $\vec{g}$ est supposé uniforme.
- On suppose que la portée du projectile est supérieur à la distance $D$.

{{% solution "Étapes de la résolution du problème" %}}

1. Établir les équation horaires du mouvement du projectile.
2. Établir les équation horaires du mouvement du singe.
3. Déterminer à quelle date $t_I$ le projectile se trouve à l'abscisse $D$.
4. En déduire l'altitude du projectile à l'instant $t_I$.
5. En déduire l'altitude du singe à l'instant $t_I$.
6. Conclure

{{% /solution %}}

{{% solution "Éléments de correction" %}}

**Remarque :** il faut bien évidemment être capable de démontrer toutes les expressions données.

1. Équations horaires du projectile :
$$
\begin{cases}
   x_P (t) = V_0 \cos (\alpha) t & \\\\
   y_P (t) = -\dfrac{1}{2} g t^2 + V_0 \sin (\alpha) t & \\\\
\end{cases}
$$

2. Équations horaires du singe :
$$
\begin{cases}
   x_S (t) = D & \\\\
   y_S (t) = -\dfrac{1}{2} g t^2 + H & \\\\
\end{cases}
$$

3. $t_I$ est telle que $x_P (t_I) = D$ donc
$$
V_0 \cos (\alpha) t_I = D \iff t_I = \dfrac{D}{V_0 \cos (\alpha)}
$$

4. $$ y_P (t_I) = -\dfrac{1}{2} g t_I^2 + V_0 \sin (\alpha) t_I = -\dfrac{1}{2} g \left( \dfrac{D}{V_0 \cos (\alpha)} \right)^2 + V_0 \sin (\alpha) \left( \dfrac{D}{V_0 \cos (\alpha)} \right)$$

En simplifiant on obtient
$$ y_P (t_I) = -\dfrac{1}{2} g \left( \dfrac{D}{V_0 \cos (\alpha)} \right)^2 +  \tan (\alpha) D$$

5. $$ y_S (t_I) = -\dfrac{1}{2} g t_I^2 + H = -\dfrac{1}{2} g \left( \dfrac{D}{V_0 \cos (\alpha)} \right)^2 + H$$

6. Pour comparer l'altitude du singe et du projectile on peut étudier le résultat de leur différence :
$$y_S (t_I) - y_P (t_I) = H - \tan (\alpha) D$$
Si on dessine le schéma de la situation, on se rend compte que $\tan (\alpha) = \dfrac{H}{D}$, on peut donc conclure que $$y_S (t_I) - y_P (t_I) = 0$$
Le projectile rencontre le singe, ce dernier n'aurait pas du se laisser tomber.

#### Comment comprendre la situation ?

Le singe et la flèche ont la même accélération, ils tombent au sol avec une accélération $a = g$. Par rapport au singe, la flèche possède donc un mouvement rectiligne dirigé vers lui puisqu'elle tombe exactement comme lui.

{{% /solution %}}
