---
title: "Décroissance radioactive"
subtitle: ""
author: ""
type: ""
date: 2021-03-09T06:35:58+04:00
draft: false
toc: true
tags: []
categories: ["Physique", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
mathjax: true
---

<!--

- {{< remote "Énoncé de l'activité" "/terminales-pc/chap-15/chap-15-3/chap-15-3-Q.pdf" >}}

- {{< remote "Corrigé de l'activité" "/terminales-pc/chap-15/chap-15-3/chap-15-3-QR.pdf" >}}
-->

## Loi de décroissance

### Évolution du nombre de noyaux d'un échantillon de noyaux radioactifs

Soit un échantillon contenant des atomes radioactifs susceptibles de se désintégrer selon l'un des modes définis dans le cours.

1. Écrire l'équation de désintégration du césium 137, émetteur $\beta^-$.
{{% solution "Réponse" %}}

$$
\ce{_{55}^{137}Cs --> _{56}^{137}Ba + _{-1}^{0}e + \bar{\nu}_e}
$$
{{% /solution %}}

Une désintégration radioactive est par nature probabiliste : c'est un phénomène **aléatoire**. À chaque instant, il y existe une certaine probabilité pour qu'un noyau se désintègre entre deux dates $t$ et $t + \Delta t$. On note cette probabilité $\lambda\, \Delta t$ où $\lambda$ est une *constante caractéristique du noyau considéré et indépendante du temps*.

{{% note tip %}}

On appelle **constante radioactive** $\lambda$ d'une famille de noyaux tous identiques la *probabilité de désintégration par seconde* des noyaux de cette famille.

{{% /note %}}

#### Remarque

Puisque la constante radioactive $\lambda$ ne varie pas en fonction du temps on dit souvent, de manière imagée, que *les noyaux meurent sans vieillir* : pour les « jeunes » ou pour les « vieux » la probabilité de se désintégrer est identique.

On considère donc un ensemble des noyaux radioactifs (*radionucléides*). Un détecteur peut compter le nombre de particules émises (par exemple les électrons) par cet échantillon, pendant une durée $\Delta t$. Ce nombre de particules est égal au nombre de désintégrations qui ont eu lieu pendant la durée $\Delta t$. On cherche à déterminer, à partir de cette donnée l'évolution du nombre de noyaux dans l'échantillon au cours du temps.

{{% note normal %}}

Le nombre $| \Delta N |$ de noyaux qui se désintègrent pendant la durée $\Delta t$ est aléatoire ; *il fluctue autour d'une valeur moyenne*. On ne peut donc pas définir avec certitude le nombre $N (t)$ de noyaux qui existeront toujours à la date $t + \Delta t$. On peut par contre évaluer une *valeur moyenne* de $N (t)$ que nous noterons $\bar{N} (t)$.

{{% /note %}}

{{% note normal %}}

#### Qu'est-ce qu'une probabilité ?

Pour un évènement aléatoire donné, si on note $N_{\text{fav}}$ le nombre de cas favorables, c'est à dire le nombre de fois où l'évènement aléatoire s'est réalisé, et $N_{\text{tot}}$ le nombre total d'issues possibles, la probabilité pour que l'évènement se réalise est donnée par
$$
p = \dfrac{N_{\text{fav}}}{N_{\text{tot}}}
$$
{{% /note %}}

2. Par analogie avec l'expression d'une probabilité donnée dans le document ci-dessus, donner l'expression de la probabilité $\lambda \Delta t$ de désintégration entre les dates $t$ et $t+\Delta t$ en fonction de $\bar{N}(t)$ le nombre moyen de noyaux présents à la date $t$ et de $|\Delta \bar{N} |$ le nombre moyen de noyaux qui se sont désintègré entre les dates $t$ et $t+\Delta t$.
{{% solution "Réponse" %}}

- $|\Delta \bar{N} |$ est le nombre de cas favorables,
- $\bar{N}(t)$ est le nombre total d'issues possibles,
donc

$$
\lambda\\, \Delta t = \dfrac{|\Delta \bar{N} |}{\bar{N}(t)}
$$
{{% /solution %}}

3. En déduire l'expression de $\Delta \bar{N}$, la variation du nombre moyen de noyaux entre les dates $t$ et $t+\Delta t$.
{{% solution "Réponse" %}}

Par définition, $\Delta \bar{N} = \bar{N}(t+\Delta t) - \bar{N}(t)$. Puisque le nombre moyen de noyaux diminue dans l'échantillon, $\bar{N}(t+\Delta t) < \bar{N}(t)$ et $\Delta \bar{N} < 0$.  
À partir de l'expression trouvée à la question 2, on peut écrire :
$$
\Delta \bar{N} = -\lambda\\, \Delta t\\, \bar{N}(t)
$$

{{% /solution %}}

4. En déduire l'équation différentielle linéaire du premier ordre qui donne l'évolution du nombre moyen de noyaux dans l'échantillon radioactif.
{{% solution "Réponse" %}}

À partir de l'expression obtenue à la question précédente on peut écrire :
$$
\dfrac{\Delta \bar{N}}{\Delta t} = -\lambda\\, \bar{N}(t)
$$
Si on prend la limite lorsque $\Delta t \rightarrow 0$ à gauche et à droite de l'expression, on obtient :
$$
\lim_{\Delta t \rightarrow 0} \left( \dfrac{\Delta \bar{N}}{\Delta t} \right) = \lim_{\Delta t \rightarrow 0} \left( -\lambda\\, \bar{N}(t) \right)
$$
Comme $-\lambda\\, \bar{N}(t)$ ne dépend pas du temps à la date $t$, l'expression s'écrit aussi
$$
\lim_{\Delta t \rightarrow 0} \left( \dfrac{\Delta \bar{N}}{\Delta t} \right) = -\lambda\\, \bar{N}(t)
$$
ou
$$
\dfrac{\mathrm{d}N}{\mathrm{dt}} = -\lambda\\, \bar{N}(t)
$$
ce qui est équivalent à :
$$
\dfrac{\mathrm{d}N}{\mathrm{dt}} + \lambda\\, \bar{N}(t) = 0
$$

{{% /solution %}}

5. La famille la plus générale de solutions de l'équation différentielle précédente est :

$$
\bar{N}(t) = A + B\\, e^{- Ct}
$$
où $A$, $B$ et $C$ sont des constantes.  
Déterminer les expressions de ces constantes afin que $\bar{N} (t)$ soit **la solution au problème étudié**, en considérant qu'il existait, dans
l'échantillon, $N_0$ noyaux à la date $t = 0$.

{{% solution "Réponse" %}}

#### Étape 1 : À quelle condition cette famille de solutions convient-elle ?

Puisque l'expression de $\bar{N} (t)$ donnée constitue une famille de
solutions possibles, **elle doit vérifier l'équation différentielle** pour $t \geqslant 0$ :
$$
\begin{eqnarray}
\dfrac{\mathrm{d} (A + B\\, e^{- Ct})}{\mathrm{dt}} + \lambda\\, (A + B\\, e^{- Ct}) & = & 0 \\\\

B\\, Ce^{- Ct} + \lambda A + \lambda B\\, e^{- Ct} & = & 0 \\\\
\lambda A + B (- C + \lambda) e^{- \lambda t} & = & 0 \\\\

B (- C + \lambda) e^{- \lambda t} & = & - \lambda A
\end{eqnarray}
$$
Le terme à gauche du signe égal dépend du temps alors que celui à droite
est constant au cours du temps. La seule possibilité est donc que le terme de
gauche soit nul, pour $t \geqslant 0$ :
\[ B (- C + \mathlambda) e^{- \mathlambda t} = 0 \Longleftrightarrow
   \left\{\begin{array}{l}
     B = 0\\
     \text{et / ou}\\

- C + \mathlambda = 0
   \end{array}\right. \]
La première solution est impossible, car si $B = 0$, $\bar{N} (t)$ est une
constante au cours du temps ; le nombre de noyaux radioactifs reste constant
au cours du temps !\\
La solution est donc
\[ - C + \mathlambda = 0 \Longleftrightarrow \begin{array}{|c|}
     \hline
     C = \mathlambda\\
     \hline
   \end{array} \]
Si on injecte cette solution dans l'équation (1), on obtient
\[ \begin{array}{|c|}
     \hline
     A = 0\\
     \hline
   \end{array} \]
La famille de solutions peut donc s'écrire :
\[ \bar{N} (t) = Be^{- \mathlambda t} \]
{{% /solution %}}
