---
title: "Contrôles des transformations chimiques : estérification"
subtitle: "Chapitre 15,2"
author: ""
type: ""
date: 2021-04-12T09:05:04+04:00
draft: false
toc: true
tags: []
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de ce document est de présenter à partir de l'exemple de l'équilibre d'estérification-hydrolyse des méthodes généralisables que le chimiste utilise au quotidien pour répondre aux questions :
- Comment accélérer une transformation lente ?
- Comment augmenter le rendement d'une transformation limitée ?

## Équilibre estérification - hydrolyse

### Synthèse d'un ester : estérification

{{% note exercise %}}
L'éthanoate de benzyle, un ester à odeur de jasmin, peut être synthétisé par réaction de l'acide éthanoïque (ou acétique) $\ce{CH3-CO2H}$ avec l'alcool benzylique $\ce{C6H5-CH2-OH}$, en présence de traces d'acide sulfurique, Sa formation s'accompagne de celle d'eau.
1. Écrire l'équation de la réaction de synthèse de l'éthanoate de benzyle à l'aide de formules semi-développées.
2. Écrire l'équation de la réaction de synthèse de l'éthanoate de benzyle à l'aide de formules topologiques.
3. Quel est le rôle de l'acide sulfurique ?
{{% /note %}}
{{% solution "Solution" %}}
1. $ \ce{CH3-CO2H (liq) + C6H5-CH2-OH  (liq) -> CH3-CO2-H2C-C6H5 (liq) + H2O (liq)} $\
Noter qu'il faut écrire $\ce{(liq)}$ et pas $\ce{(aq)}$ car on ne travaille pas en solution aqueuse. *Les réactifs et produits sont purs*.
2. À venir.
3. L'acide sulfurique joue le rôle de catalyseur.
{{% /solution %}}

### Hydrolyse d'un ester

{{% note exercise %}}
Chauffons à reflux pendant environ trente minutes un mélange constitué de $\pu{10 mL}$ d'éthanoate de benzyle $\ce{CH3-CO2-CH2-C6H5}$, de $\pu{40 mL}$ d'eau et d'une dizaine de gouttes d'acide sulfurique. Il se forme de l'alcool benzylique et de l'acide éthanoïque.
1. Écrire l'équation de la réaction entre l'éthanoate de benzyle et l'eau.
2. Quel est le rôle de l'acide sulfurique ?
3. Pourquoi la réaction porte-t-elle le nom d'« hydrolyse » ?
{{% /note %}}
{{% solution "Solution" %}}
1. $\ce{CH3-CO2-CH2-C6H5  (liq) + H2O  (liq) -> CH3-CO2H  (liq) + C6H5-CH2-OH  (liq)} $
2. L'acide sulfurique joue le rôle de catalyseur.
3. « Hydrolyse signifie « coupure par l'eau ». Il s'agit d'une réaction dont l'un des réactifs est l'eau.
{{% /solution %}}

### Équilibre estérification - hydrolyse

{{% note exercise %}}
1. À partir des deux exemples ci-dessus, expliquer pourquoi toute transformation s'appuyant sur une réaction d'estérification ou sur une réaction d'hydrolyse ne peut pas être totale.
2. Écrire correctement l'équation de la réaction d'estérification entre l'acide acétique et l'alcool benzylique.
{{% /note %}}
{{% solution "Solution" %}}
1. 
- La réaction d'estérification conduit à la formation d'un ester et d'eau.
- La réaction d'hydrolyse est une réaction entre un ester et l'eau. Elle conduit à la formation d'un acide carboxylique et d'un alcool.
On voit que ces deux réactions conduisent à la formation de produits capables de réagir entre eux. *Les transformations modélisées par ces réactions ne peuvent donc pas être totales.*
2. $ \ce{CH3-CO2H(liq) + C6H5-CH2-OH(liq) <=> CH3-CO2-H2C-C6H5(liq) + H2O(liq)} $
{{% /solution %}}

### Rendement d'une transformation chimique

{{% note tip %}}
Le rendement $\eta$ d'une transformation chimique est *le rapport de la quantité de produit effectivement obtenue et de la quantité maximale attendue (c'est à dire si la transformation était totale et s'il n'y avait aucune perte expérimentale)*. Il s'exprime en %.\
Dans le cas de l'estérification, 
$$
    \eta = \dfrac{n(\text{ester})}{n\_{\text{max}}(\text{ester})} = \dfrac{n(\text{ester})}{n(\text{réactif limitant})}
$$
{{% /note %}}

{{% note normal %}}
La *valeur maximale* que peut prendre le rendement d'une transformation chimique est égale au *taux de réaction final*. On néglige alors les pertes d'ordre expérimental.
{{% /note %}}

{{% note exercise %}}
On réalise l'hydrolyse, en milieu acide et en présence d'un excès d'eau, d'une quantité $n\_i(\text{ester}) = \pu{0,120 mol}$ d'un ester à odeur de muguet, l'éthanoate de 3-phénylpropyle, de formule : $$\ce{CH3-CO2-CH2-CH2-CH2-C6H5}$$
1. Donner la formule et le nom des produits obtenus.
2. On recueille, après séparation des produits, une masse $m_f = \pu{4,56 g}$ d'alcool. En déduire le rendement de cette hydrolyse.
{{% /note %}}
{{% solution "Solution" %}}
1. L'acide obtenu est l'acide éthanoïque $\ce{CH3-CO2H}$. L'alcool obtenu est le 3-phénylpropan-1-ol $\ce{HO-CH2-CH2-CH2-C6H5}$.
2. La stœchiométrie de la réaction est telle qu'il se forme autant d'acide que d'alcool. Le rendement s'écrit donc :
$$
    \eta = \dfrac{n\_f(\text{alcool})}{n\_i(\text{ester})} = \dfrac{m\_f(\text{alcool})}{n\_i(\text{ester})\cdot M(\text{alcool})}
$$
**A.N.** $\eta = \dfrac{\pu{4,56 g}}{\pu{0,120 mol} \times \pu{136,0 g.mol-1}} = \pu{0,28}$\
Le rendement vaut 28 %.
{{% /solution %}}

{{% note exercise %}}
Le benzoate de méthyle, à l'odeur d'œillet, est utilisé en parfumerie. Pour le synthétiser, on chauffe à reflux, sous la hotte pendant environ une heure, $\pu{12,2 g}$ d'acide benzoïque $\ce{C6H5-CO2H}$, $\pu{40 mL}$ de méthanol et $\pu{3 mL}$ d'acide sulfurique.

Après refroidissement du mélange réactionnel, on verse celui-ci dans une ampoule à décanter contenant $\pu{50 mL}$ de solution saturée de chlorure de sodium. Après séparation des deux phases, lavage, puis séchage de la phase organique, on récupère par distillation une masse $m_f = \pu{10,2 g}$ de benzoate de méthyle.

> Données

| Composé | acide benzoïque | méthanol | benzoate de méthyle |
| :---: | :---: | :---: | :---: |
| $M(\pu{g.mol-1})$ | 122 | 32 | 136 |
| $\mu (\pu{g.cm-3})$ | 1,321 | 0,791 | 1,089 |

Pictogrammes présents sur l'étiquette d'un flacon de méthanol :
<img src="/terminales-pc/chap-16/chap-16-2/chap-16-2-1.png" alt="" width="40%" />

1. Écrire l'équation de cette estérification.
2. Pourquoi chauffe-t-on à reflux ?
3. Pourquoi effectue-t-on cette synthèse sous la hotte? 
4. Déterminer le rendement de cette synthèse.
{{% /note %}}
{{% solution "Solution" %}}
1. Lacide benzoïque réagit avec le méthanol selon l'équation :
$$
    \ce{C6H5-CO2H + CH3-OH <=> C6H5-CO2-CH3 + H2O}
$$
2. En chauffant, on accélère la réaction. C'est à l'ébullition, température maximale que peut atteindre le mélange, que la vitesse de la réaction est la plus élevée.
Le condenseur à eau du montage à reflux refroidit les vapeurs qui s'élèvent et les condense. Le liquide alors obtenu retourne dans le ballon, ce qui permet d'éviter la perte de réactifs et de produits par évaporation.
3. Le méthanol est un liquide toxique dont il convient d'éviter de respirer les vapeurs ; d'où la nécessité d'effectuer cette synthèse sous la hotte. Inflammable, on devra le manipuler en l'absence de toute flamme.
4. 
- La quantité d'acide utilisé pour cette synthèse est :
$$
    n\_i(\text{acide}) = \dfrac{m\_i (\text{acide})}{M(\text{acide})} = \dfrac{\pu{12,2 g}}{\pu{122,0 g.mol-1}} = \pu{0,100 mol}
$$
- La quantité d'alcool utilisé est :
$$
    n\_i(\text{alcool}) = \dfrac{m\_i (\text{alcool})}{M(\text{alcool})} = \dfrac{V\_i (\text{alcool}) \cdot \mu (\text{alcool})}{M(\text{alcool})}
$$
**A.N.** $n\_i(\text{alcool}) = \dfrac{\pu{40 mL} \times \pu{0,791 g.mL-1}}{ \pu{32 g.mol-1} } = \pu{0,99 mol}$
$$
    \eta = \dfrac{n\_f(\text{ester})}{n\_i(\text{acide})} = \dfrac{m\_f(\text{ester})}{n\_i(\text{acide})\cdot M(\text{ester})}
$$
**A.N.** $\eta = \dfrac{\pu{10,2 g}}{\pu{0,100 mol})\times M(\pu{136 g.mol-1})} = \pu{0,75}$.\
Le rendement vaut 75 %.
{{% /solution %}}

### Synthèse

{{% note tip %}}
- Un ester peut être obtenu par la réaction d'un acide $\ce{R-CO2-H}$ avec un alcool $\ce{R'-OH}$ suivant l'équation :
$$
    \ce{R-CO2-H (liq) + R'-OH (liq) <=> R-CO2-R' (liq) + H2O (liq)}
$$
Les ions H+ catalysent cette synthèse.

- L'eau hydrolyse l'ester $\ce{R-CO2-R'}$ pour donner l'acide carboxylique $\ce{R-CO2-H}$ et l'alcool $\ce{R'-OH}$ correspondants suivant l'équation : 
$$
    \ce{R-CO2-R' (liq) + H2O (liq) <=> R-CO2-H (liq) + R'-OH (liq)}
$$
Les ions H+ catalysent cette synthèse.

- Les réactions d'estérification et d'hydrolyse sont *inverses l'une de l'autre et **ont lieu simultanément**.* *Elles se limitent l'une l'autre et conduisent à un état d'équilibre chimique*.\
Cet état est atteint lorsque *la vitesse de formation de l'ester par la réaction d'estérification est exactement égale à sa vitesse de disparition par hydrolyse*.


- *Toute transformation modélisée par une réaction d'estérification ou d'hydrolyse est **lente** et **limitée**.*

- L'équilibre d'estérification-hydrolyse est caractérisé par la constante d'équilibre $K$ telle que, pour l'équation écrite dans le send de l'estérification :
$$
    K = \dfrac{[\text{ester}]\\, [\text{eau}]}{[\text{acide}]\\, [\text{alcool}]}
$$
{{% /note %}}

{{% note warning %}}
**L'eau est un produit de la réaction d'estérification et non le solvant.** Sa concentration figure donc dans l'expression de $K$ ou dans celle du quotient de réaction $Q_r$.
{{% /note %}}

{{% note normal %}}
Le rendement d'estérification *dépend très peu de la nature de l'acide carboxylique utilisé*.\
Il *dépend par contre beaucoup de la classe de l'alcool utilisé*.\
Pour des **mélanges équimolaires** en acide carboxylique et en alcool :
- Le rendement est voisin de 67 % si l'alcool est primaire ;
- Le rendement est compris entre 56 % et 65 % si l'alcool est secondaire ;
- Le rendement est inférieur à 10 % si l'alcool est tertiaire.
{{% /note %}}

## Contrôle cinétique : comment modifier la vitesse de formation d'un produit

### Influence de la température

{{% note exercise %}}
À l'aide d'enceintes thermostatées, il est possible d'étudier l'influence de la température sur les réactions d'estérification ou d'hydrolyse d'esters, donc sur l'état d'équilibre.
On peut tracer $n\_{\text{acide}} (t)$ (ou $n\_{\text{alcool}} (t)$) et $n\_{\text{ester}} (t)$ (ou $n\_{\text{eau}} (t)$) pour diverses valeurs de la température (80 °C et 30 °C ci-dessous).

<img src="/terminales-pc/chap-16/chap-16-2/chap-16-2-2.png" alt="" width="50%" />

1. Le diagramme ci-dessus correspond-il au déroulement d'une estérification ou d'une hydrolyse ?
2. Que nous enseigne le graphe ci-dessus ?
3. Si on suppose le *mélange initial équimolaire*, quel est le rendement de la transformation modélisée par cette réaction, à 80 °C ?
{{% /note %}}
{{% solution "Solution" %}}
1. Il s'agit d'une estérification puisque la quantité d'acide diminue. Il s'agit donc d'un réactif.
2. Deux conclusions se dégagent de ce graphe :
- Une élévation de température permet d'atteindre plus rapidement l'état d'équilibre.
- La composition à l'équilibre de systèmes résultant de l'évolution de mélanges initiaux identiques est indépendante de la température.
3. Puisque le mélange initial était équimolaire, l'acide est limitant et $\eta = \pu{0,67}$.
{{% /solution %}}

{{% note tip %}}
Une élévation de température permet d'atteindre *plus rapidement l'état d'équilibre d'estérification-hydrolyse* mais ne modifie pas cet état d'équilibre.
{{% /note %}}

{{% note warning %}}
*La dernière partie de la conclusion précédente, n'est pas généralisable à tous les équilibres chimiques !* Ceux-ci doivent être **athermiques**, c'est à dire avoir **une constante d'équilibre indépendant de la température**. 
{{% /note %}}

{{% note tip %}}
- Les réactions d'estérification et d'hydrolyse sont athermiques.
- Le chauffage n'a aucune influence sur l'état final de l'équilibre d'estérification-hydrolyse, donc sur le rendement.
{{% /note %}}

### Influence du catalyseur

{{% note exercise %}}
En réalisant les réactions d'estérification et d'hydrolyse en présence ou en absence d'ions hydronium $\ce{H^+}$, il est possible d'étudier le rôle du catalyseur sur la composition du mélange réactionnel.\
L'influence de la quantité de catalyseur utilisé peut aussi être étudiée.
- Que peut-on conclure ?
{{% /note %}}
{{% solution "Solution" %}}
Deux conclusions peuvent à nouveau se dégager de ces graphes :
- L'utilisation d'un catalyseur ne modifie pas l'état d'équilibre final, car il catalyse de la même façon les deux réactions inverses l'une de l'autre : l'estérification et l'hydrolyse.
- Le seul rôle du catalyseur est de permettre d'atteindre plus vite l'état d'équilibre. *L'état d'équilibre est d'autant plus vite atteint que la concentration du catalyseur est plus élevée*.
{{% /solution %}}

{{% note tip %}}
Un catalyseur ne modifie pas un état d'équilibre, car il catalyse de la même façon les deux réactions inverses l'une de l'autre.\
Il permet d'atteindre plus rapidement l'état d'équilibre.
{{% /note %}}

## Contrôle thermodynamique : comment améliorer le rendement d'une transformation chimique ?

### Loi modératrice

#### Les facteurs d'équilibre

On considère un système chimique constitué d'acide, d'alcool, d'ester et d'eau *à l'état d'équilibre*.\
Si on fait varier les concentrations des différents constituants du mélange, par exemple en rajoutant de l'eau. *L'expérience montre que le système évolue alors vers un nouvel état d'équilibre*.

{{% note tip %}}
- Pour un **système en phase liquide**, les paramètres pouvant faire évoluer l'état d'équilibre du système sont les **concentrations des différents constituants** et la **température**. On les appelle les **facteurs d'équilibre**.
- La **pression** est aussi un facteur d'équilibre, mais essentiellement en **phase gazeuse**.
{{% /note %}}

#### Évolution du système

Comment le système chimique réagit-il à une modification de l'un des facteurs d'équilibre ? La **loi de modération** permet de le prévoir qualitativement :

{{% note tip %}}
**L'évolution d'un système chimique a lieu dans le sens d'une modération des actions extérieures**. Cela signifie que **le système évolue de façon à compenser toute variation des facteurs d'équilibre**.
{{% /note %}}

### Influence de l'excès d'un des réactifs

{{% note exercise %}}
1. Écrire l'expression du quotient de réaction d'une réaction d'estérification alors que l'état d'équilibre de la transformation est atteint.
2. On ajoute alors de l'acide (ou de l'alcool) dans le système. Comment évolue le quotient de réaction ?
3. Appliquer le critère d'évolution et indiquer l'évolution du système.
4. La loi de modération est-elle appliquée ?
{{% /note %}}
{{% solution "Solution" %}}
1. Si le système est à l'équilibre :
$$
    K = Q\_{r,eq} = \dfrac{n\_{eq}(\text{ester})\\, n\_{eq}(\text{eau})}{n\_{eq}(\text{acide})\\, n\_{eq}(\text{alcool})}
$$
2. Si à ce système, on ajoute de l'alcool, le quotient de réaction diminue, $Q\_r < Q\_{r,eq}$.
3. Puisque $Q\_r < Q\_{r,eq}=K$, le critère d'évolution nous apprend que le système doit évoluer de façon à ce que la valeur du quotient de réaction augmente.\
Le système consomme les réactifs et évolue dans le sens direct.
4. La loi de modération est appliquée puisqu'en réponse à un ajout d'un réactif le système consomme les réactifs.
{{% /solution %}}


{{% note tip %}}
- Si, dans l'état initial d'une transformation modélisée par une réaction d'estérification, on utilise un excès d'acide ou d'alcool au lieu d'un mélange stœchiométrique --- équimolaire donc ici (On choisit en général le moins coûteux), la loi de modération indique que l'état final de la transformation est déplacé (par rapport à celui correspondant à un mélange stœchiométrique) dans le sens de la consommation du réactif en excès (donc de l'estérification).
- Le rendement étant calculé par rapport au réactif limitant, dont la quantité de matière ne varie pas, augmente donc puisque la quantité de matière d'ester produit est plus grande.
{{% /note %}}



### Influence de l'élimination de l'un des produits

{{% note normal %}}
À partir du critère d'évolution spontanée, on vient de voir que l'*utilisation d'un excès d'acide ou d'alcool augmente le taux d'avancement final de l'estérification et permet d'en améliorer le rendement*.\
On peut cependant aussi voir, en appliquant le même critère, que diminuer la quantité d'eau ou d'ester présents dans le système à l'équilibre conduit au même résultat.\
(On peut aussi considérer que l'eau et l'ester sont les réactifs de la réaction qui limite l'estérification, leur élimination ne peut que favoriser le rendement de cette dernière)
{{% /note %}}


## Exercices

{{% note exercise %}}
On chauffe à reflux un mélange constitué d'une mole d'acide butanoïque, d'une mole d'éthanol et de quatre gouttes d'acide sulfurique. Le volume initial $V = \pu{151 mL}$ est considéré comme constant durant l'expérience.\
Toutes les 10 minutes, on prélève un volume $V_a = \pu{2 mL}$ du mélange et on le plonge dans l'eau glacée. On dose alors tout l'acide restant par une solution de soude de concentration $C_b = \pu{2 mol·L-1}$ en présence de phénolphtaléine. On note $V_{b,E}$ le volume de soude versé à l'équivalence. Un premier dosage à $t =0$ donne $V_{b,0} = \pu{6,7 mL}$.

1. Écrire l'équation de la réaction et nommer l'ester formé.
2. Pourquoi le prélèvement est-il plongé dans de l'eau glacée ? Comment s'appelle cette opération ?
3. Écrire l'équation de la réaction support du titrage.
4. Exprimer, en fonction de $V$, $V_a$, $V_{b,0}$, $V_{b,E}$ et $C_b$ la quantité d'ester formé à l'instant $t$ du prélèvement.

Donnée 
: pour $t = \pu{10 min}$, $V_b = \pu{3,4 mL}$.
{{% /note %}}
{{% solution "Solution" %}}
1. $\ce{CH3-CH2-CH2-CO2H (liq) + CH3-CH2-OH (liq) <=> CH3-CH2-CH2-CO2-CH2-CH3 (liq) + H2O} (liq)$\
L'ester se nomme le butanoate d'éthyle.
2. On plonge le prélèvement dans de l'eau glacée de façon à diminuer très fortement la vitesse de réaction ; on le « fige ». Cette opération se nomme une trempe.
3. $\ce{CH3-CH2-CH2-CO2H (aq) + OH^- (aq) -> CH3-CH2-CH2-CO2^- (aq) + H2O}$
4. 
- **Étape 1.**\
Un tableau d'avancement pour **le titrage** du prélèvement, à la date $t$, nous apprend que $n\_{\text{acide}}(t) - x_E (t) = 0$ et $n\_{\text{base versée}}(t) - x_E (t) = 0$. Donc 
$$n\_{\text{acide}}(t) = n\_{\text{base versée}}(t) = C_b \cdot V_{b,E} (t)$$
Comme $n\_{\text{acide}}(t) = n\_{\text{acide}}(0) - n\_{\text{acide}}(\text{qui a réagi à t})$,
$$n\_{\text{acide}}(0) - n\_{\text{acide}}(\text{qui a réagi à t}) = C_b \cdot V_{b,E} (t)$$
ou
$$n\_{\text{acide}}(\text{qui a réagi à t}) = n\_{\text{acide}}(0) - C_b \cdot V_{b,E} (t)$$
On peut déterminer $n\_{\text{acide}}(0)$ grâce au premier titrage (à la date $t=0$) :
$$n\_{\text{acide}}(0) = C_b \cdot V_{b,0}$$
Finalement 
$$n\_{\text{acide}}(\text{qui a réagi à t}) = C_b \cdot V_{b,0} - C_b \cdot V_{b,E} (t) = C_b\\, \left( V_{b,0} - V_{b,E} (t) \right)$$
- **Étape 2**\
Un tableau d'avancement pour **l'estérification**, à la date $t$, nous apprend que
$$n\_{\text{ester}}(\text{qui s'est formé à t}) = n\_{\text{acide}}(\text{qui a réagi à t})$$

Finalement, pour le prélèvement, 
$$n\_{\text{ester}}(\text{qui s'est formé à t}) = C_b\\, \left( V_{b,0} - V_{b,E} (t) \right)$$
Cette quantité de matière n'est cependant pas toute la quantité de matière formée puisque le prélèvement ne correspond qu'à la fraction $\dfrac{V_a}{V}$ du mélange.\
<strong>Pour tout le mélange</strong>, 
$$n\_{\text{ester}}(\text{qui s'est formé à t}) = C_b\\, \left( V_{b,0} - V_{b,E} (t) \right) \\, \dfrac{V}{V_a}$$

**A.N.** $n\_{\text{ester}}(\text{qui s'est formé à t}) = \pu{2 mol·L-1} \times \left(\pu{6,7e-3 L} - \pu{3,4e-3 L} \right) \times \dfrac{\pu{151 mL}}{\pu{2 mL}} = \pu{0,50 mol}$
{{% /solution %}}


{{% note exercise %}}
On introduit dans un ballon $\pu{0,200 mol}$ d'acide éthanoïque, $\pu{0,500 mol}$ d'éthanol et 4 gouttes d'acide sulfurique concentré. On chauffe le mélange à reflux pendant une heure.\
Après refroidissement, on dose les acides présents par de la soude à $C_b = \pu{1,5 mol.L-1}$. À l'équivalence, $V_b = \pu{18,7 mL}$. Un dosage préalable montre que 4 gouttes d'acide sulfurique concentré sont neutralisées par $V'_b = \pu{2,7 mL}$ de solution de soude.

1. Quel est le nom de l'ester formé lors de cette expérience ?
2. Le mélange initial est-il stœchiométrique ?
3. Quel rendement est attendu pour un mélange stœchiométrique dans les conditions de l'expérience (information un peu plus haut dans ce document) ?
4. Établir la composition du mélange au bout d'une heure.
5. Calculer le rendement de cette estérification. Conclusion ?
{{% /note %}}
{{% solution "Solution" %}}
1. L'ester formé est l'éthanoate d'éthyle.
2. Le mélange n'est pas stœchiométrique puisque tous les coefficients sont égaux à un dans l'équation de la réaction et que les quantités initiales des réactifs ne sont pas égales.
3. L'alcool étant primaire, on attend un rendement voisin de 67 %.
4. Le raisonnement détaillé est semblable à celui de l'exercice précédent.\
L'acide sulfurique étant un catalyseur, il n'est pas consommé. Par conséquent, le volume de base ayant servi à neutraliser l'acide éthanoïque n'est que de $(V_b - V'_b)$. La quantité d'acide éthanoïque restant est donc, après réaction :
$$n\_{\text{acide}} = C_b \cdot (V_b - V'_b)$$

**A.N.** $n\_{\text{acide}} = \pu{1,5 mol.L-1} \times (\pu{18,7e-3 L} - \pu{2,7 mL}) = \pu{2,4e-2 mol}$.

L'avancement final de la réaction d'estérification a pour valeur :
$$x_f = n\_{\text{acide}}(\text{qui a réagi à t}) = n\_{\text{acide}}(0) - n\_{\text{acide}}$$

**A.N.** $x_f = \pu{0,200 mol} - \pu{0,024 mol} = \pu{0,176 mol}$.

L'état final a pour composition
<center>

| | acide | alcool | ester | eau |
| :---: | :---: | :---: | :---: | :---: |
| État initial | 0,200 | 0,500 | 0 | 0 |
| État final | 0,024 | 0,324 | 0,176 | 0,176 |

</center>

5. $$\eta = \dfrac{n(\text{ester})}{n_i(\text{acide})}$$

**A.N.** $\eta = \dfrac{\pu{0,176 mol}}{\pu{0,200 mol}} = \pu{0,88} > \pu{0,67}$\
Le rendement vaut donc 88 %. L'introduction de l'alcool en excès a bien amélioré le rendement de l'estérification.
{{% /solution %}}

{{% note exercise %}}
#### Analyse élémentaire d'un ester

Un composé organique de formule brute $\ce{C_nH_{2n}O2}$ contient 27,6 % d'oxygène en masse.

1. Montrer que la molécule correspondant à ce composé comporte 6 atomes de carbone. Calculer sa masse molaire $M$.

Ce composé est un ester naturel possédant une odeur agréable. On le note $E$. Par hydrolyse de $E$, on obtient deux corps désignés par $A$ et $B$.

2. Quelles sont les fonctions chimiques de ces deux corps ?
3. Parmi les termes suivants, indiquer ceux qui vous paraissent convenir pour caractériser une réaction d'hydrolyse : complète, athermique, totale, exothermique, limitée, aboutissant à un équilibre chimique.

#### Étude du composé $A$

4. Sa formule brute est $\ce{C2H4O2}$. Quelques gouttes de bleu de bromothymol additionnées de $A$ donnent une solution de couleur jaune. Quels sont la formule semi-développée et le nom du composé $A$ ?

#### Étude du composé $B$

5. Quelle est la formule brute de la molécule correspondant à $B$ ?

Pour préciser la structure de $B$, on effectue une oxydation ménagée qui conduit à la formation d'un composé $C$. Puis on soumet $C$ aux tests suivants :
- *Premier test :* une solution de $C$ additionnée de DNPH conduit à la formation d'un précipité de couleur jaune ; 
- Deuxième test : une solution de $C$, additionnée de liqueur de Fehling et chauffée, ne provoque aucun changement de coloration de la liqueur.

6. Déduire de ces expériences la formule semi-développée et le nom la molécule correspondant au corps $B$. Justifier la réponse.

#### Données

- Le bleu de bromothymol est de couleur bleue pour des valeurs de pH supérieures à 7,6 et de couleur jaune pour des valeurs de pH inférieures à 6.
- La réaction de Fehling est une réaction chimique qui sert couramment à caractériser des aldéhydes par leur oxydation par des ions cuivre II.
- La 2,4-dinitrophénylhydrazine (ou 2,4-DNPH ou réactif de Brady) est utilisée comme test caractéristique du groupe carbonyle.

{{% /note %}}

