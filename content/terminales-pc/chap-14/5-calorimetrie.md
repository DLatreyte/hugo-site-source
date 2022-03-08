---
title: "Détermination de la capacité thermique massique du granite"
subtitle: "Chapitre 14,4"
author: ""
type: ""
date: 2022-03-06T17:40:40+04:00
draft: false
toc: true
tags: []
categories: ["Terminale Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

On trouve sur la page Wikipedia dédiée au [granite](https://fr.wikipedia.org/wiki/Granite) : « Le granite et ses roches associées forment l'essentiel de la croûte continentale de la planète. C'est un matériau résistant très utilisé en construction, dallage, décoration, sculpture, sous l'appellation granit.\
Le granite est le résultat du refroidissement lent, en profondeur, de grandes masses de magma [...]\
De manière plus anecdotique, **le granite peut aussi servir d'alternative aux glaçons pour refroidir les boissons. Contrairement aux glaçons, la pierre ne fond pas et ne risque donc pas de dénaturer le goût de la boisson par dilution**. [...]»

> L'objectif de cette séance est d'essayer de comprendre cette dernière phrase : au-delà de la non modification du goût, quelle caractéristique du granite permet son utilisation en remplacement d'un glaçon ?

{{% note normal %}}

#### Calorimètre

Le calorimètre est un appareil destiné à mesurer les *échanges de chaleur* (*transfert d'énergie thermique*). Cet échange peut se produire *entre plusieurs corps*, mettre en jeu des *changements d'état* ou des *réactions chimiques*. **Le calorimètre constitue un système thermodynamique isolé**, ce qui implique qu'*il n'y a pas d'échange de matière et d'énergie (travail ou chaleur) avec le milieu extérieur*. Néanmoins, cela ne signifie pas qu'il n'y a pas des transferts de chaleur entre les différentes parties de l'ensemble calorimétrique (*composés objets de l'étude*, *accessoires* et*paroi du calorimètre*...).

<div style="text-align: right;">
    <a href="https://fr.wikipedia.org/wiki/Calorimètre">Wikipedia</a>
</div>

{{% /note %}}

## Capacité thermique du calorimètre

> Une partie de l'énergie échangée par les corps placés dans un calorimètre sert à modifier la température de ce dernier. Il est donc *nécessaire de déterminer avant toute expérience sa capacité thermique* $C$.

### Protocole

- Élever un volume d'eau environ égal à $\pu{60 mL}$ à une température de $\pu{50 °C}$.\
Noter $m_2$ la masse de cette « eau chaude » et $\theta_2$ sa température.

- Verser dans le calorimètre un volume d'eau environ égal à $\pu{100 mL}$ à la température ambiante.\
Noter $m_1$ la masse de cette « eau froide » et $\theta_1$ sa température.

- Verser rapidement l'eau chaude dans le calorimètre. Couvrir et agiter (doucement).

- Noter $\theta_3$ la température d'équilibre.

### Exploitation

{{% note normal %}}

Capacité thermique massique de l'eau : $c_{\text{eau}} = \pu{4,18 J.K-1.g-1}$.

{{% /note %}}

1. Mettre en œuvre un raisonnement qui permet de déterminer la capacité thermique du calorimètre.

{{% solution "Réponse" %}}

- Système étudié : $\\{m_1 + m_2 + \text{paroi interne calorimètre} \\}$

- Puisque le système est isolé, $$\Delta U(\text{eau froide}) + \Delta U(\text{eau chaude}) + \Delta U(\text{calorimètre}) = 0$$
donc
$$ m_1 c_{\text{eau}} (\theta_3 - \theta_1) + m_2 c_{\text{eau}} (\theta_3 - \theta_2) + C (\theta_3 - \theta_1) = 0 $$
Finalement
$$
C = \dfrac{m_1 c_{\text{eau}} (\theta_3 - \theta_1) + m_2 c_{\text{eau}} (\theta_3 - \theta_2)}{\theta_1 - \theta_3}
$$
{{% /solution %}}

2. Effectuer le calcul en fonction des résultats des mesures.
{{% solution "Réponse" %}}

- Eau froide : $m_1 = \pu{105,1 g}$, $\theta_1 = \pu{19,0 °C}$ ;
- Eau chaude : $m_2 = \pu{76,5 g}$, $\theta_2 = \pu{38,5 °C}$ ;
- Température d'équilibre : $\theta_3 = \pu{26,5 °C}$.

$$
C = \dfrac{\pu{105,1 g} \times \pu{4,18 J.°C-1.g-1} \times (\pu{26,5 °C} - \pu{19,0 °C}) + \pu{76,5 g} \times \pu{4,18 J.°C-1.g-1} \times (\pu{26,5 °C} - \pu{38,5 °C}) }{\pu{19,0 °C} - \pu{26,5 °C}}
$$

$$
C = \pu{72,3 J.°C-1}
$$

{{% /solution %}}

3. Récolter les résultats de tous les groupes et utiliser le programme à [cette adresse](https://dlatreyte.github.io/jupyter-lite/lab?path=incertitude-type-a.ipynb) afin de déterminer la valeur de la capacité thermique $C$ du calorimètre.

4. Le constructeur donne la valeur $C = \pu{70 J.K-1}$. Est-elle en accord avec le résultat expérimental obtenu ?

## Détermination de la capacité thermique du granite

### Protocole

- Peser le morceau de granite. Noter $m_2$ sa masse.

- Le plonger pendant $\pu{15 min}$ environ dans de l'eau bouillante.

- Verser dans le calorimètre un volume d'eau environ égal à $\pu{100 mL}$ à la température ambiante.\
Noter $m_1$ la masse de cette « eau froide » et $\theta_1$ sa température.

- Transvaser rapidement le morceau de granite dans le calorimètre. Couvrir et agiter (doucement).

- Noter $\theta_3$ la température d'équilibre.

### Exploitation

1. Mettre en œuvre un raisonnement qui permet de déterminer la capacité thermique massique du granite.

2. Effectuer le calcul en fonction des résultats des mesures.

3. Récolter les résultats de tous les groupes et utiliser le programme à [cette adresse](https://dlatreyte.github.io/jupyter-lite/lab?path=incertitude-type-a.ipynb) afin de déterminer la valeur de la capacité thermique massique $c$ du granite.

4. Rechercher la valeur attendue de la capacité thermique massique du granite à [cette adresse](https://fr.wikipedia.org/wiki/Capacité_thermique_massique#Valeurs_courantes). Y a-t-il adéquation entre votre résultat et celui attendu ?

5. Expliquer en quoi la valeur de la capacité thermique massique du granite est importante pour le refroidissement (ou le chauffage) de la boisson.
