---
title: "Les différentes erreurs lorsqu'on calcule à l'aide d'un ordinateur"
subtitle: "Derivation numérique"
author: ""
type: ""
date: 2020-08-21T14:08:45+04:00
draft: false
toc: true
tags: ["Erreurs numériques", "Dérivation"]
categories: ["Informatique", "Analyse numérique"]
image: ""
solution_est_visible: true
auto_numbering: true
---
[^1]: Les fonctions, dans ce chapitre, sont considérées continues et dérivables sur les intervalles sélectionnés.
[^2]: Expression à rapprocher de (1.1.).
[^3]: Nous verrons qu'il est possible de faire varier l'erreur de troncature en choisissant d'autres schémas.

Dans ce document, on s'intéresse au différentes erreurs qui interviennent lorsqu'on effectue des calculs à l'aide d'un ordinateur. On prend pour exemple le calcul numérique de la dérivée d'une fonction, qu'elle soit définie analytiquement ou numériquement (par une table de valeurs).

## Dérivation d'une fonction analytique --- idée simple

### Introduction

Le nombre dérivé $f'(x)$ en un point $x \in \mathbb{R}$, d'une fonction[^1] :
$$
\begin{array}{l|rcl}
        f: & \mathbb{R} & \longrightarrow & \mathbb{R} \cr
        & x & \longmapsto & f(x)
\end{array}
$$

est défini par :
$$f^{\prime}(x) = \lim\limits_{h \to 0} \dfrac{f(x+h) - f(x)}{h}$$

Un ordinateur ne pouvant manipuler qu'un nombre limité de chiffres, tous les nombres envisageables en mathématique ne le sont pas en informatique. La notion de limite n'a en particulier aucune signification en informatique ; on *recherche donc une valeur approchée de la dérivée* en $x$.

{{% note tip %}}
Le procédé le plus simple consiste à considérer que si $h$ est suffisamment petit *il n'est pas nécessaire de passer à la limite*. On considère alors que :
$$ f^{\prime}(x) \cong \dfrac{f(x+h) - f(x)}{h} \qquad \qquad \text{(1.1.)}$$
{{% /note %}}

### Comment évaluer l'approximation réalisée ?

L'approximation (1.1.) s'appuie sur la valeur du paramètre $h$. Il semble évident que cette valeur doit être la plus petite possible de façon à limiter le plus possible la non prise en compte de la limite dans la formule (1.1.). *Cette intuition est cependant fausse*, nous allons voir que :
{{% note tip %}}
 - la valeur de $h$ ne doit pas être plus petite que le plus petit nombre représentable dans le langage choisi ;

- la valeur de $h$ doit être assez grande pour que $f(x)$ et $f(x+h)$ soient reconnues comme deux valeurs différentes, afin d'être à l'abri d'**erreurs d'arrondi** ;

- la valeur de $h$ doit être assez petite afin que les **erreurs de troncature** soient négligeables.
{{% /note %}}

En Python, on accède facilement à certaines de ces informations :
{{< highlight py3 >}}
>>> import sys

>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, 
min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, 
mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)

>>> sys.float_info.min        # Plus petit float (positif) accessible
2.2250738585072014e-308

>>> 1./1.2250738585072014e-308
8.162773150824861e+307

>>> sys.float_info.epsilon    # plus petit intervalle entre deux float                                                                                          
2.220446049250313e-16
>>> 1./1e-309                 # Nombre non représentable
inf                           # Résultat d'une division par 0
{{< / highlight >}}


## Calcul numérique et erreurs

{{% note warning %}}
Les *opérations numériques ne sont jamais exactes et toujours entachées d'erreurs*. Ces erreurs sont généralement petites pour chaque opération mais, comme un ordinateur réalise un très grand nombre d'opérations, leur accumulation peut conduire à des résultats complètement erronés.  
{{% / note %}}

### Erreur d'arrondi

> Les erreurs d'arrondi sont liées à la représentation en mémoire des nombres : tout nombre réel n'est connu qu'avec une précision donnée de $n$ chiffres significatifs.

Afin d'illustrer la notion d'erreur d'arrondi, on suppose, dans cette partie, que les calculs sont effectués à l'aide d'un *calculateur à trois chiffres significatifs*.

Si $f(x) = x^2$ on calcule que $f'(7)=14,0$. L'utilisation de l'expression approchée (1.1.) donne :
- avec $h=0,1$ :
    $$\dfrac{f(7,1)-f(7,0)}{0,1} = \dfrac{(7,1)^2-(7,0)^2}{0,1} = \dfrac{50,4 - 49,0}{0,1} = 14,0$$

    puisque $(7,1)^2 = 50,41$.

- avec $h=0,01$ :
    $$\dfrac{f(7,01)-f(7,00)}{0,01} = \dfrac{(7,01)^2-(7,00)^2}{0,01} = \dfrac{49,1 - 49,0}{0,01} = 10,0$$

    puisque $(7,01)^2 = 49,1401$.

> Une petite perturbation sur la valeur de $f(x)$ (**erreur d'arrondi**) peut induire une grande variation de $f'(x)$.

Si on note $\delta$ la précision relative de la machine (par exemple : 7 chiffres significatifs donnent $\delta = 10^{-7}$), l'erreur absolue sur l'évaluation d'une fonction $f$ en un point $x$ est de l'ordre de $\delta\ |f(x)|$. On peut donc **estimer** l'erreur sur le numérateur de l'expression (1.1.) par : $\delta\ |f(x+h)| + \delta\ |f(x)| \approx 2 \delta\ |f(x)|$.

{{% note tip %}}
L'erreur absolue sur l'évaluation du nombre dérivé par l'expression (1.1.) est donc :
$$
    E_a = 2 \delta\ |\dfrac{f(x)}{h}|
$$
{{% /note %}}

#### Retour à l'exemple ($\delta = 10^{-3}$ et $f(x)=x^2$) :

- avec $h=0,1$ :
$$ E_a = 2 \times 10^{-3} \times \dfrac{49}{0,1} \approx 1$$

- avec $h=0,01$ :
$$ E_a = 2 \times 10^{-3} \times \dfrac{49}{0,01} \approx 10$$


{{% note warning %}}
Les **erreurs d'arrondi** ont pour origine *la nature finie de la représentation des nombres* en mémoire. C'est une *limite imposée par le calculateur*.
{{% /note %}}

#### Script Python

{{< highlight py3 >}}
# -*- coding: utf-8 -*-

"""
Mise en évidence de l'erreur d'arrondi lors de la dérivation
"""
import matplotlib.pyplot as plt
from typing import List

 
def df(f: "function", a: float, h: float) -> float:
    """
    Retourne le nombre dérivé de la fonction f à l'abscisse
    a en appliquant le schéma des différences finies à
    droite avec le pas h.
    """
    return ( f(a + h) - f(a) ) / h


def affichage(x: List[float], y: List[float], titre: str,
              x_label: str, y_label: str, save:bool=False) -> None:
    """
    Trace erreur = f(pas).
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title(titre)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.plot(x, y)
    plt.grid()
    if (save):
        plt.savefig("Graphique-{}.png".format(compteur))
    plt.show()

def main():
    """
    Fonction principale
    """
    f = lambda x: x**2  # fonction à dériver
    a = 2               # nombre dérivé est calculé en x = 2
    f_prime = 4         # valeur théorique du nombre dérivé

    hs = [0.05 / 2**i for i in range(0, 45)]    # valeurs des pas h

    dfs = [df(f, a, h) for h in hs]             # valeurs des nombres dérivés
    erreurs = [abs(df - f_prime) / f_prime * 100 for df in dfs]    # évolution de l'erreur

    #affichage(dxs, df, "Valeur de la dérivée")
    affichage(hs, erreurs,
              "Évolution de l'erreur dans le calcul de la dérivéeen fonction du pas",
              "h", "erreur relative (%)", False)
    for i in range(len(hs)):
        print("Pas : {:.5e}, Nombre calculé : {:.9f}, erreur relative (%) : {:.9e}".format(hs[i],
                                                                              dfs[i],
                                                                              erreurs[i]))

main()
{{< /highlight >}}

{{% solution "Résultat" %}}

{{< highlight py3 >}}
Pas : 5.00000e-02, Nombre calculé : 4.050000000, erreur relative (%) : 1.250000000e+00
Pas : 2.50000e-02, Nombre calculé : 4.025000000, erreur relative (%) : 6.250000000e-01
Pas : 1.25000e-02, Nombre calculé : 4.012500000, erreur relative (%) : 3.125000000e-01
Pas : 6.25000e-03, Nombre calculé : 4.006250000, erreur relative (%) : 1.562500000e-01
Pas : 3.12500e-03, Nombre calculé : 4.003125000, erreur relative (%) : 7.812500000e-02
Pas : 1.56250e-03, Nombre calculé : 4.001562500, erreur relative (%) : 3.906249999e-02
Pas : 7.81250e-04, Nombre calculé : 4.000781250, erreur relative (%) : 1.953125001e-02
Pas : 3.90625e-04, Nombre calculé : 4.000390625, erreur relative (%) : 9.765625032e-03
Pas : 1.95313e-04, Nombre calculé : 4.000195312, erreur relative (%) : 4.882812414e-03
Pas : 9.76563e-05, Nombre calculé : 4.000097656, erreur relative (%) : 2.441406104e-03
Pas : 4.88281e-05, Nombre calculé : 4.000048828, erreur relative (%) : 1.220703689e-03
Pas : 2.44141e-05, Nombre calculé : 4.000024414, erreur relative (%) : 6.103522537e-04
Pas : 1.22070e-05, Nombre calculé : 4.000012207, erreur relative (%) : 3.051740350e-04
Pas : 6.10352e-06, Nombre calculé : 4.000006103, erreur relative (%) : 1.525862899e-04
Pas : 3.05176e-06, Nombre calculé : 4.000003052, erreur relative (%) : 7.630151231e-05
Pas : 1.52588e-06, Nombre calculé : 4.000001526, erreur relative (%) : 3.814639058e-05
Pas : 7.62939e-07, Nombre calculé : 4.000000762, erreur relative (%) : 1.903972588e-05
Pas : 3.81470e-07, Nombre calculé : 4.000000381, erreur relative (%) : 9.522773325e-06
Pas : 1.90735e-07, Nombre calculé : 4.000000195, erreur relative (%) : 4.866160452e-06
Pas : 9.53674e-08, Nombre calculé : 4.000000097, erreur relative (%) : 2.421438694e-06
Pas : 4.76837e-08, Nombre calculé : 4.000000041, erreur relative (%) : 1.024454832e-06
Pas : 2.38419e-08, Nombre calculé : 4.000000022, erreur relative (%) : 5.587935448e-07
Pas : 1.19209e-08, Nombre calculé : 4.000000060, erreur relative (%) : 1.490116119e-06
Pas : 5.96046e-09, Nombre calculé : 4.000000060, erreur relative (%) : 1.490116119e-06
Pas : 2.98023e-09, Nombre calculé : 3.999999762, erreur relative (%) : 5.960464478e-06
Pas : 1.49012e-09, Nombre calculé : 3.999999762, erreur relative (%) : 5.960464478e-06
Pas : 7.45058e-10, Nombre calculé : 4.000000954, erreur relative (%) : 2.384185791e-05
Pas : 3.72529e-10, Nombre calculé : 4.000000954, erreur relative (%) : 2.384185791e-05
Pas : 1.86265e-10, Nombre calculé : 3.999996185, erreur relative (%) : 9.536743164e-05
Pas : 9.31323e-11, Nombre calculé : 3.999996185, erreur relative (%) : 9.536743164e-05
Pas : 4.65661e-11, Nombre calculé : 4.000015259, erreur relative (%) : 3.814697266e-04
Pas : 2.32831e-11, Nombre calculé : 4.000015259, erreur relative (%) : 3.814697266e-04
Pas : 1.16415e-11, Nombre calculé : 3.999938965, erreur relative (%) : 1.525878906e-03
Pas : 5.82077e-12, Nombre calculé : 3.999938965, erreur relative (%) : 1.525878906e-03
Pas : 2.91038e-12, Nombre calculé : 4.000244141, erreur relative (%) : 6.103515625e-03
Pas : 1.45519e-12, Nombre calculé : 4.000244141, erreur relative (%) : 6.103515625e-03
Pas : 7.27596e-13, Nombre calculé : 3.999023438, erreur relative (%) : 2.441406250e-02
Pas : 3.63798e-13, Nombre calculé : 3.999023438, erreur relative (%) : 2.441406250e-02
Pas : 1.81899e-13, Nombre calculé : 4.003906250, erreur relative (%) : 9.765625000e-02
Pas : 9.09495e-14, Nombre calculé : 4.003906250, erreur relative (%) : 9.765625000e-02
Pas : 4.54747e-14, Nombre calculé : 3.984375000, erreur relative (%) : 3.906250000e-01
Pas : 2.27374e-14, Nombre calculé : 3.984375000, erreur relative (%) : 3.906250000e-01
Pas : 1.13687e-14, Nombre calculé : 4.062500000, erreur relative (%) : 1.562500000e+00
Pas : 5.68434e-15, Nombre calculé : 4.062500000, erreur relative (%) : 1.562500000e+00
Pas : 2.84217e-15, Nombre calculé : 3.750000000, erreur relative (%) : 6.250000000e+00
{{< /highlight >}}

{{% /solution %}}

### Erreur de troncature

#### Rappel : Formule de Taylor

Soit une fonction $f$ possédant $n+1$ dérivées continues sur l'intervalle $[a,b]$ et soient $x$ et $x_0$ deux points de cet intervalle. On peut alors écrire :
$$f(x) = p_n(x) + R_{n+1}(x)$$
avec
$$
\begin{array}{rcl}
   p_n(x) & = & f(x_0) + \dfrac{x - x_0}{1!} f^{\prime}(x_0) + \ldots + \dfrac{(x - x_0)^n}{n!} f^{(n)}(x_0), \cr
   R_{n+1}(x) & = & \dfrac{1}{n!} \int_{x_0}^{x} (x-t)^n f^{(n+1)}(t) dt \cr
               & = & \dfrac{(x - x_0)^{(n+1)}}{(n+1)!} f^{(n+1)}(\epsilon), \hspace{0.5cm} x_0 \leqslant \epsilon \leqslant x. \cr
\end{array}
$$

En limitant le développement de Taylor à l'ordre 2, on peut écrire :
$$f(x+h) = f(x) + f^{\prime}(x)h + f^{\prime\prime}(\epsilon)\dfrac{h^2}{2} \hspace{0.5cm} |x - \epsilon| < |h|$$

soit[^2] :
$$f^{\prime}(x) = \dfrac{f(x+h) - f(x)}{h} - f^{\prime\prime}(\epsilon)\dfrac{h}{2}$$.

{{% note tip %}}
On appelle **erreur de troncature** :
$$
    E_t = \dfrac{|h|}{2} |f^{\prime\prime}(\epsilon)|
$$
{{% /note %}}

#### Retour à l'exemple ($\delta = 10^{-3}$) et $f(x) = x^2$ :

Si $f(x) = x^2$, $f^{\prime} = 2x$ et $f^{\prime\prime} = 2$. Donc,

- avec $h=0,1$ :
$$ E_t = \dfrac{0,1 \times 2}{2} \approx 0,1$$

- avec $h=0,01$ :
$$ E_a = \dfrac{0,01 \times 2}{2} \approx 0,01$$

{{% note warning %}}
Les **erreurs de troncature** sont liées à *la précision de l'algorithme utilisé*. Si, par exemple, une fonction est approchée par son développement de Taylor, l'erreur de troncature sera obtenue par une évaluation du reste du développement. Son contrôle sera obtenu par une majoration de ce reste.
{{% /note %}}


### Erreur de méthode

{{% note warning %}}
Les **erreurs de méthode** interviennent lorsqu'une expression est mal équilibrée et/ou mélange des valeurs très différentes. C'est un problème qui engendre des *erreurs d'arrondi*. *Dans la plupart des cas, une erreur de méthode impose de modifier l'algorithme*.
{{% /note %}}

- **Exemple 1.** Détermination de la position du milieu d'un segment.  
Le calcul effectué spontanément : $$m = \dfrac{a+b}{2}$$ peut conduire à des erreurs si la somme $a+b$ dépasse les capacités de représentation des nombres du calculateur, *alors que la valeur de $m$ est représentable*. Le calcul à préférer est : $$m = a + \dfrac{b-a}{2}$$

{{< highlight py3 >}}
>>> a = 1e308                                                                                                               
>>> b = 1.7e308                                                                                                          

>>> (a + b) / 2         # a + b > 1.7976931348623157e+308 (valeur maximale)                                                                                                  
inf                     # on obtient une erreur

>>> a + (b - a) / 2     # (b -a ) < 1.7976931348623157e+308 (valeur maximale)                                                                                                 
1.35e+308               # on obtient bien la moyenne 
{{< / highlight>}}

- **Exemple 2.** Détermination des racines du polynôme du second degré.  
Par exemple, la recherche des racines du polynôme $10^{-8} x^2 - 0,8 x + 10^{-8}$, dont les deux racines sont $x_1 \cong 0.8\cdot 10^{8}$ et $x_2 \cong 1.25\cdot 10^{-8}$, nécessite le calcul du discriminant $\Delta = 0,64 - 4\cdot 10^{-16}$ dont le résultat n'est pas toujours correct car $4\cdot 10^{-16}$ peut être considéré comme négligeable par certains calculateurs, comparé à 0,64.  
Pour obtenir les racines, il est donc nécessaire de modifier l'algorithme en considérant, par exemple, la somme et le produit des racines.
\end{description}

{{< highlight py3 >}}
>>> a = 1e-8                                                                                                               
>>> b = -0.8                                                                                                               
>>> c = 1E-8                                                                                                               
>>> delta = b**2 - 4*a*c                                                                                                   
>>> from math import sqrt                                                                                                  
>>> x1 = (-b + sqrt(delta)) / (2*a)         # Première racine 
>>> x1                                                                                       
79999999.99999999
>>> x2 = (-b - sqrt(delta)) / (2*a)         # Deuxième racine                                                                                       
>>> x2
1.1102230246251565e-08
>>> somme_racines = somme_racines = -b / a  # Ici on utilise les propriétés des racines, pas les calculs précédents
>>> produit_racines = c / a                 # Idem
>>> x1 + x2, somme_racines                  # Semble identiques                                                                              
(80000000.0, 80000000.0)
>>> x1 * x2, produit_racines                                                                                               
(0.8881784197001251, 1.0)                   # Problème !
{{< /highlight>}}


### Erreur totale

L'erreur totale, dans l'exemple étudié dans ce chapitre, est définie par :
$$
E = E_a + E_t
$$

Dans le cadre de cette étude[^3], l'erreur totale a donc pour expression :
$$ E = 2 \delta |\dfrac{f(x)}{h}| + \dfrac{|h|}{2} |f^{\prime\prime}(\epsilon)|$$

Rechercher la valeur approchée la plus précise possible de l'expression (1.1.) nécessite donc de minimiser $E$. $$E = 2 \delta |\dfrac{f(x)}{h}| + \dfrac{|h|}{2} |f^{\prime\prime}(\epsilon)|$$ est minimale pour $$|h| = 2 \sqrt{\delta |\dfrac{f(x)}{f^{\prime\prime}(\epsilon)}|}$$


#### Démonstration : 
Soit $g(s) = \dfrac{a}{s} + bs$ avec $a = 2 \delta |f(x)|$ et $b = \dfrac{1}{2} |f^{\prime\prime}(\epsilon)|$. Puisque $a$ et $b$ sont positifs, $g^{\prime}(s) = 0 \Longleftrightarrow -\dfrac{a}{s^2} +b =0 \Longleftrightarrow s = \sqrt{\dfrac{a}{b}}$


#### Retour à l'exemple : $f(x) = x^2$ et $\delta = 10^{-3}$
$f^{\prime\prime}(x) = 2, h = \sqrt{2 \delta f(x)} = \sqrt{2\delta} |x|$. Pour $x=7$, $h$ a pour valeur : $h = 10\sqrt{\delta} \approx 0,3$.


### Convergence et stabilité

{{% note tip %}}
On dit qu'un *algorithme est stable si le résultat des opérations est peu sensible à l'accumulation des erreurs*.
{{% /note %}}
L'étude de stabilité se fait par des méthodes expérimentales et parfois théoriques.


## Dérivation d'une fonction analytique, les différents schémas

{{% note tip %}}
L'expression :
    $$f^{\prime}(x) = \dfrac{f(x+h) - f(x)}{h}$$
    est appelée **différence finie à droite**.

On peut aussi choisir une **différence finie à gauche** :
    $$f^{\prime}(x) = \dfrac{f(x) - f(x-h)}{h}$$
et une **différence finie centrée autour de $x$** :
    $$f^{\prime}(x) = \dfrac{f(x+h) - f(x-h)}{2h}$$
{{% /note %}}

> Dans toutes ces expressions l'**erreur d'arrondi** reste la même. Par contre, l'**erreur de troncature** est modifiée dans la dernière expression.

#### Démonstration :

À partir de la formule de Taylor,
$$
\begin{array}{rcl}
f(x+h) & = & f(x) + hf^{\prime}(x) + \frac{h^2}{2}f^{\prime\prime}(x) + \frac{h^3}{6}f^{\prime\prime\prime}(\epsilon) \hspace{1cm} \text{où } \epsilon \in [x,x+h] \cr
f(x-h) & = & f(x) - hf^{\prime}(x) + \frac{h^2}{2}f^{\prime\prime}(x) - \frac{h^3}{6}f^{\prime\prime\prime}(\eta) \hspace{1cm} \text{où } \eta \in [x-h,x] \cr
\end{array}
$$

Donc $$f^{\prime}(x) - \dfrac{f(x+h) - f(x-h)}{2h} = -\dfrac{h^2}{12}[f^{\prime\prime\prime}(\epsilon) + f^{\prime\prime\prime}(\eta)]$$
Finalement, *l'erreur de troncature est diminuée lorsqu'on utilise la différence finie centrée autour de $x$.*

#### Script Python

{{< highlight py3 >}}
"""
Différences finies centrées, ordre 02 en h.
Mise en évidence des erreurs de troncature et d'arrondis.
"""
from math import sin, cos

def df(x):
    return cos(x)


def err_centree(x, f, df, h):
    return abs(df(x) - (f(x + h / 2) - f(x - h / 2)) / h)


def err_progressive(x, f, df, h):
    return abs(df(x) - (f(x + h) - f(x)) / h)


def err_retrograde(x, f, df, h):
    return abs(df(x) - (f(x) - f(x - h)) / h)


def main():
    f = lambda x: sin(x)   # Fonction étudiée
    df = lambda x: cos(x)  # Fonction dérivée de la fonction étudiée
    x0 = 1                 # Point où le nombre dérivé est calculé
    hs = [1 / (10**i) for i in range(1, 15)]  # Liste des pas h

    print(
        "h \t\t Diff. finies Prog.   Diff. finies Retro.   Diff. finies centrées"
    )
    for h in hs:
        print("{:.1e} \t  {:.4e} \t  {:.4e} \t  {:.4e}".format(
            h, err_progressive(x0, f, df, h), err_retrograde(x0, f, df, h),
            err_centree(x0, f, df, h)))


main()
{{< /highlight >}}

{{% solution "Résultat" %}}
{{< highlight py3 >}}
h 		 Diff. finies Prog.   Diff. finies Retro.   Diff. finies centrées
1.0e-01 	  4.2939e-02 	  4.1138e-02 	  2.2510e-04
1.0e-02 	  4.2163e-03 	  4.1983e-03 	  2.2513e-06
1.0e-03 	  4.2083e-04 	  4.2065e-04 	  2.2513e-08
1.0e-04 	  4.2074e-05 	  4.2073e-05 	  2.2541e-10
1.0e-05 	  4.2074e-06 	  4.2074e-06 	  5.5898e-12
1.0e-06 	  4.2075e-07 	  4.2080e-07 	  2.7717e-11
1.0e-07 	  4.1828e-08 	  4.1439e-08 	  7.4944e-10
1.0e-08 	  1.4072e-08 	  8.1323e-09 	  2.9699e-09
1.0e-09 	  5.2541e-08 	  5.2541e-08 	  5.2541e-08
1.0e-10 	  5.8481e-08 	  5.8481e-08 	  5.8481e-08
1.0e-11 	  1.1687e-06 	  1.1687e-06 	  1.1687e-06
1.0e-12 	  4.3240e-05 	  6.7782e-05 	  4.3240e-05
1.0e-13 	  7.3392e-04 	  3.7631e-04 	  3.7631e-04
1.0e-14 	  7.3953e-03 	  3.7070e-03 	  7.3953e-03
{{< /highlight >}}
{{% /solution %}}


## Dérivation d'une fonction numérique

On peut être amené à calculer la dérivée d'une fonction définie par une table de valeurs (résultat de mesures expérimentales, par exemple). Une bonne compréhension des résultats des formules précédentes (en particulier celle de la différence finie centrée autour de $x$) nécessite de prendre en compte :

- que le pas $h$ est maintenant imposé (et pas forcément constant) ;
- que les inévitables erreurs de mesure vont être « amplifiées » par la division par $h$ (qui est « petit »).

Des méthodes existent pour l'importance du second point, ci-dessus, mais elles ne seront pas abordées cette année.


## Dérivée seconde d'une fonction

Pour déterminer une expression de la dérivée seconde, on utilise à nouveau la formule de Taylor, en « poussant » à l'ordre 4 le développement :
$$
\begin{array}{rcl}
   f(x+h) & = & f(x) + hf'(x) + \frac{h^2}{2}f^{\prime\prime}(x) + \frac{h^3}{6}f^{\prime\prime\prime}(x) + \frac{h^4}{24}f^{\prime\prime\prime\prime}(\epsilon) \text{ où } \epsilon \in [x,x+h]\cr
   f(x-h) & = & f(x) - hf'(x) + \frac{h^2}{2}f^{\prime\prime}(x) - \frac{h^3}{6}f^{\prime\prime\prime}(x) + \frac{h^4}{24}f^{\prime\prime\prime\prime}(\eta) \text{ où } \eta \in [x-h,x] \cr
\end{array}
 $$

Finalement,
$$
f^{\prime\prime}(x) = \dfrac{f(x+h)-2f(x)+f(x-h)}{h^2} - \dfrac{h^2}{12} [f^{\prime\prime\prime\prime}(\epsilon) + f^{4}(\eta)]
$$

L'erreur de troncature est donc en $h^2$.

## Ressource

- {{< remote "Méthodes numériques pour la physique" "http://www.cpt.univ-mrs.fr/~crepieux/stock/numeriq.pdf" >}}