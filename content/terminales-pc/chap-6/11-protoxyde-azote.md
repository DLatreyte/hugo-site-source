---
title: "Décomposition du protoxyde d’azote"
subtitle: "Chapitre 7,9"
author: ""
type: ""
date: 2020-11-24T05:27:00+04:00
draft: false
toc: true
tags: ["Vitesse de réaction", "Vitesse de formation", "Vitesse de disparition", "Tableau d'avancement", "Ordre 1", "Mécanisme réactionnel"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

Le protoxyde d’azote est utilisé comme gaz anesthésique en chirurgie. Dans la culture populaire, on emploie souvent l’expression de gaz hilarant. Sa décomposition en phase gazeuse se produit selon le *mécanisme réactionnel* en deux étapes suivant :

$$\ce{ N2O(g) -> N2(g) + O^{.}(g)  }$$
$$\ce{ O^{.}(g) + N2O(g) ->  N2(g) + O2(g) }$$

Ici, les concentrations correspondent au rapport entre la quantité de gaz et le volume total de gaz du milieu réactionnel. L’expérience est réalisée avec une concentration initiale en protoxyde d’azote égale à $C_0 = \pu{5,0 mol·L-1}$. La concentration $[\ce{N2}]$ en diazote est relevée toutes les $\pu{0,20 ms}$.

<img src="/terminales-pc/chap-6/chap-6-11-2.png" alt="" width="" />

- {{< remote "Accès aux données pour traitement avec Graphical Analysis" "/terminales-pc/chap-6/chap-6-11-1.ambl" >}}

1. Identifier les intermédiaires réactionnels apparaissant dans le mécanisme réactionnel. 
{{% solution "Réponse" %}}
Le radical $\ce{O^{.}(g)}$ est un intermédiaire réactionnel, car il est formé dans la première étape, puis consommé dans la seconde.
{{% /solution %}}

2. Écrire l’équation-bilan. 
{{% solution "Réponse" %}}
$\ce{ 2 N2O(g) -> 2  N2(g) + O2(g)  }$
{{% /solution %}}

3. Dresser le tableau d’avancement de la transformation.

4. Dans le tableau, dans le {{< remote "fichier des données" "/terminales-pc/chap-6/chap-6-11-1.ambl" >}} ajouter une colonne calculée pour exprimer la concentration $[\ce{N2O}]$ en protoxyde d'azote à chaque instant.
{{% solution "Réponse" %}}
$ [\ce{N2O}] = C_0 - 2 x $ et $ [\ce{N2}] = 2x $, donc $ [\ce{N2O}] = C_0 - [\ce{N2}] $.

<img src="/terminales-pc/chap-6/chap-6-11-3.png" alt="" width="" />
{{% /solution %}}

5. Exprimer la vitesse volumique de formation $v\_f$ de $[\ce{N2}]$.
{{% solution "Réponse" %}}
$$
    v\_f (\ce{N2}) = \dfrac{\mathrm{d} [\ce{N2}]}{\mathrm{dt}} 
$$
{{% /solution %}}

<!--
{{% note tip %}}
On appelle **vitesse volumique de formation** d'un produit $A$ la vitesse 
$$ v_f = \dfrac{\mathrm{d} [A]}{\mathrm{dt}}$$
$v_f$ est positive et s'exprime en mole par litre par seconde (en pratique).
{{% /note %}}
-->

<!--
6. Trouver la relation qui existe entre la vitesse volumique de formation de $\ce{N2}$, $v_f(\ce{N2})$, et la vitesse volumique de réaction.
{{% solution "Réponse" %}}
$v_f(\ce{N2}) = \dfrac{\mathrm{d} [\ce{N2}]}{\mathrm{dt}}$ donc $v = \dfrac{1}{2}\\, v_f(\ce{N2})$.
{{% /solution %}}
-->

6. Trouver la relation qui existe entre la vitesse volumique de formation de $\ce{O2}$, $v_f(\ce{O2})$, et la vitesse volumique de formation de de $[\ce{N2}]$.
{{% solution "Réponse" %}}

- $v\_f (\ce{N2}) = \dfrac{\mathrm{d} [\ce{N2}]}{\mathrm{dt}}$
- $v\_f (\ce{O2}) = \dfrac{\mathrm{d} [\ce{O2}]}{\mathrm{dt}}$

Or, grâce au tableau d'avancement on apprend que $n(\ce{N2})(t) = 2 x(t)$ et $n(\ce{O2})(t) = x(t)$. On en conclut donc que $n(\ce{N2})(t) = 2 n(\ce{O2})(t)$. Il se forme à chaque instant deux fois plus de diazote que de dioxygène. 

Finalement, on en déduit que $[\ce{N2}\] (t) = 2 [\ce{O2}\](t)$ et que $v\_f (\ce{N2}) = 2 v\_f (\ce{O2}) $.

{{% /solution %}}

<!--
{{% note tip %}}
On appelle **vitesse volumique de disparition** d'un réactif $A$ la vitesse 
$$ v_d = \left\lvert \dfrac{\mathrm{d} [A]}{\mathrm{dt}} \right\rvert $$
$v_d$ est positive et s'exprime en mole par litre par seconde (en pratique).
{{% /note %}}
-->

7. Dans le tableau, dans le {{< remote "fichier des données" "/terminales-pc/chap-6/chap-6-11-1.ambl" >}} ajouter deux colonnes calculées pour calculer les vitesses de formation de $\ce{N2}$ et de $\ce{O2}$.


8. Trouver la relation qui existe entre la vitesse volumique de disparition de $\ce{N2O}$, $v_d(\ce{N2O})$, et la vitesse volumique de formation de $\ce{N2}$.
{{% solution "Réponse" %}}
- $v_d(\ce{N2O}) = - \dfrac{\mathrm{d} [\ce{N2O}]}{\mathrm{dt}}$.

Or, on a démontré à la question 4. que $ [\ce{N2O}] = C_0 - [\ce{N2}] $, on peut donc écrire, après dérivation par rapport au temps de la relation précédente, que $\dfrac{\mathrm{d} [\ce{N2O}]}{\mathrm{dt}} = - \dfrac{\mathrm{d} [\ce{N2}]}{\mathrm{dt}}$, ce qui implique que $v_d(\ce{N2O}) = v_f(\ce{N2})$.
{{% /solution %}}

<!--
9. Quelle est la grandeur cinétique commune à tous les produits et réactifs de la réaction ?       
    a. La vitesse volumique de formation ou de disparition ?        
    b. La vitesse volumique de réaction ?
{{% solution "Réponse" %}}
- *Les vitesses volumiques de formation ou de disparition sont spécifiques à chacune de entités de la réaction*.
- *La vitesse volumique de réaction est commune à toutes les entités de la réaction*.
{{% /solution %}}
-->

9. Les vitesses volumiques de formation et de disparition sont-elles communes à toutes les espèces chimiques ou dépendent-elles de chaque espèce chimique&nbsp;?
{{% solution "Réponse" %}}

Les vitesses volumiques de formation ou de disparition sont spécifiques à chacune de entités de la réaction. Tout dépend des proportions dans lesquelles ces entités se forment ou disparaissent.

{{% /solution %}}

10. Dans le tableau, dans le {{< remote "fichier des données" "/terminales-pc/chap-6/chap-6-11-1.ambl" >}} ajouter une colonne calculée pour calculer la vitesse de disparition $v_d(\ce{N2O})$ du protoxyde d'azote $\ce{N2O}$ à chaque instant.
{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-11-4.png" alt="" width="" />
{{% /solution %}}

11. Tracer l’évolution de la vitesse volumique de disparition de $v_d(\ce{N2O})$ en fonction de $[\ce{N2O}]$. Conclusion.
{{% solution "Réponse" %}}
<img src="/terminales-pc/chap-6/chap-6-11-5.png" alt="" width="" />

La relation est du type $ v_d(\ce{N2O}) = k [\ce{N2O}]$. La réaction est d'ordre 1 par rapport à la concentration en protoxyde d'azote.
{{% /solution %}}