---
title: "Titrage des ions hydroxyde présents dans le Destop® par suivi conductimétrique"
subtitle: ""
author: ""
type: ""
date: 2022-10-26T16:13:22+04:00
draft: false
toc: true
tags: ["Tableau d'avancement", "Équivalence", "Conductimétrie", "Titrage", "Conductivité molaire ionique", "Conductivité"]
categories: ["Chimie", "Terminale Spé PC"]
image: ""
solution_est_visible: false
auto_numbering: true
---

## Documents

{{% note normal %}}

#### Le Destop®

Le Destop® est un déboucheur de canalisation, c'est à dire une solution qui dissout intégralement et rapidement les matières organiques.  
Différentes solutions existent sur le marché. Afin de préserver les canalisations, « l'agent actif » du Destop® est l'hydroxyde de sodium.  
On peut lire sur l'étiquette d'un flacon de Destop® :

- Pourcentage en masse d’hydroxyde de sodium : 20 %.
- Densité de la solution par rapport à l’eau : 1,23.

##### Stockage

Produit corrosif. Provoque des brûlures de la peau et des lésions oculaires graves. Garder sous clef. Tenir hors de portée des enfants.

##### Sécurité

- **En cas d'ingestion :** rincer la bouche. NE PAS faire vomir.
- **En cas de contact avec les yeux :** rincer avec précaution à l’eau pendant plusieurs minutes. Enlever les lentilles de contact si la victime en porte et si elles peuvent être facilement enlevées. Continuer à rincer.
- **En cas de contact avec la peau (ou les cheveux) :** enlever immédiatement les vêtements contaminés. Rincer la peau à l’eau/se doucher.

{{% /note %}}

{{% note normal %}}

#### Hydroxyde de sodium

L'hydroxyde de sodium $\ce{NaOH (s)}$ est un solide ionique qui se dissocie totalement dans l'eau et forme alors la solution de soude $(\ce{Na^+ (aq) + OH^- (aq)})$.  
L'ion hydroxyde $\ce{OH^-}$ est la base la plus forte que l'on peut trouver dans l'eau.

{{%  /note %}}

{{% note normal %}}

#### Acide chlorhydrique

Une solution d'acide chlorhydrique a pour formule $\ce{H3O^+ + Cl^- (aq)}$.  
L'ion oxonium $\ce{H3O^+}$ est l'acide le plus fort que l'on peut trouver dans l'eau.

{{% /note %}}

{{% note normal %}}

#### Équivalence d'un titrage

- On appelle **équivalence** d'un titrage le *point du titrage où on change de réactif limitant*.
- À l'**équivalence** les *réactifs ont été introduits dans les proportions stœchiométriques*.

{{% /note %}}

## Séance

### Objectif

> L'objectif de cette séance est de vérifier que les informations relatives à l'hydroxyde de sodium, sur l'étiquette d'une bouteille de Destop®, sont vraies.

### Données : conductivités molaires ioniques

$\lambda_{\ce{Na^+}} = \pu{5,01e-3 S.m2.mol-1}$ ; $\lambda_{\ce{Cl^-}} = \pu{7,63e-3 S.m2.mol-1}$ ; $\lambda_{\ce{H3O^+}} = \pu{34,97e-3 S.m2.mol-1}$ ; $\lambda_{\ce{OH^-}} = \pu{19,80e-3 S.m2.mol-1}$.

### Matériel à disposition

<img src="/terminales-pc/chap-4/chap-4-6-1.jpg" alt="" width="55%" style="float: right; padding-left: 15px;" />

- Solution de Destop® **diluée 200 fois**.

- Solution d'acide chlorhydrique de concentration $C_A = \pu{2,5e-2 mol.L-1}$.

- Conductimètre et sonde, agitateur et barreau aimanté, burette graduée $\pu{25 mL}$, pipette jaugée $\pu{10 mL}$ et propipette, éprouvette graduée, béchers, eau distillée.

### Travail expérimental

1. Élaborer un protocole expérimental permettant de titrer $V_B = \pu{10 mL}$ d'une solution de Destop® **diluée 200 fois**.

2. Écrire l'équation de la réaction de titrage.
{{% solution "Réponse" %}}

$$ \ce{ H3O^+ + OH^- (aq) --> 2 H2O } $$

{{% /solution %}}

3. Quelles propriétés doit présenter une réaction chimique utilisée pour réaliser un titrage&nbsp;?
{{% solution "Réponse" %}}

Une réaction chimique utilisée pour réaliser un titrage doit&nbsp;:

- être **rapide**&nbsp;;
- être **unique** dans le milieu réactionnel (c'est la seule qui doit consommer les titré et titrant)&nbsp;;
- doit modéliser des **transformations chimiques totales**.

{{% /solution %}}

4. Mettre en œuvre le protocole expérimental.

5. Justifier l'allure de la courbe $\sigma = f(V_A)$.
{{% solution "Réponse" %}}

##### Remarque

L'ajout des $\pu{200 mL}$ d'eau nous permet de considérer que le volume de la solution reste constant tout au long du titrage.

##### Avant l'équivalence

Les ions oxonium, le titrant, sont en défaut. La solution contient donc (hormis l'eau) :

- des ions chlorure dont la concentration augmente ;
- des ions sodium dont la concentration reste constante ;
- des ions hydroxyde dont la concentration diminue.
L'expression de la conductivité de la solution est donc
$$
\sigma_{av} = \lambda_{\ce{Na^+}} [\ce{Na^+}] + \lambda_{\ce{Cl^-}} [\ce{Cl^-}] + \lambda_{\ce{OH^-}} [\ce{OH^-}]
$$
Comme $\lambda_{\ce{OH^-}} [\ce{OH^-}]$, la partie de la conductivité de la solution due aux ions hydroxyde, est supérieure à $\lambda_{\ce{Cl^-}} [\ce{Cl^-}]$, la partie de la conductivité de la solution due aux ions chlorure, c'est elle qui donne l'allure de l'évolution de la conductivité. La concentration des ions chlorure diminuant, la conductivité de la solution diminue.

##### Après l'équivalence

Les ions hydroxyde, le titré, sont désormais en défaut. La solution contient donc (hormis l'eau) :

- des ions chlorure dont la concentration augmente ;
- des ions sodium dont la concentration reste constante ;
- des ions oxonium dont la concentration augmente.
L'expression de la conductivité de la solution est donc
$$
\sigma_{ap} = \lambda_{\ce{Na^+}} [\ce{Na^+}] + \lambda_{\ce{Cl^-}} [\ce{Cl^-}] + \lambda_{\ce{H3O^+}} [\ce{H3O^+}]
$$
On constate donc que la conductivité de la solution doit augmenter.
{{% /solution %}}

6. Quelle est la concentration en ions hydroxyde dans la solution titrée ?  
{{% solution "Réponse" %}}
 À l'équivalence, puisqu'on change de réactif limitant,

- $n_0(\ce{OH^-}) - x_E = O$ (tous les ions hydroxyde ont été consommés) ;
- $n_E(\ce{H3O^+}) - x_E = O$ (tous les ions oxonium ont été consommés).

On a donc la relation
$$
    x_E = n_0(\ce{OH^-}) = n_E(\ce{H3O^+}) \iff [\ce{OH^-}] V_B = C_A V_{AE}
$$
où $[\ce{OH^-}]$ est la concentration des ions hydroxyde **dans la solution titrée**. Finalement
$$
    [\ce{OH^-}] = C_A\\, \dfrac{V_{AE}}{V_B}
$$
**A.N.** $\ce{OH^-}] = $
{{% /solution %}}

7. Quelle est la concentration en ions hydroxyde dans le Destop® ?
{{% solution "Réponse" %}}

- La masse volumique de la solution de Destop® est $\rho = \pu{1,23e3 g.L^-1}$, la masse d'un litre de solution est donc égale à $m_D = \pu{1,23e3 g}$.

- Selon l'étiquette, la masse d'hydroxyde de sodium représente 20 % de la masse de la solution. La masse d'hydroxyde de sodium dans un litre de solution est donc égale à $m = \pu{0,20} \\; m_D = \pu{0,20} \times \pu{1,23e3 g} = \pu{2,46e2 g}$.

- La quantité de matière d'hydroxyde de sodium vaut alors $n = \dfrac{m_0}{M(\ce{NaOH})} = \dfrac{\pu{2,46e2 g}}{\pu{40,0 g.mol^-1}} = \pu{6,15 mol}$.

- Puisqu'une mole d'hydroxyde de sodium libère une mole d'ions hydroxyde lors de la dissolution, la concentration molaire en ions hydroxyde dans la solution est $[\ce{OH^-}] = \pu{6,15 mol.L^-1}$.

{{% /solution %}}

8. Les informations sur l'étiquette d'une bouteille de Destop® sont-elles correctes ?
{{% solution "Réponse" %}}

{{% /solution %}}
