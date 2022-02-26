---
title: "Loi de Boyle-Mariotte"
subtitle: "Chapitre 9,2"
author: ""
type: ""
date: 2022-02-03T17:59:51+04:00
draft: false
toc: true
tags: []
categories: ["Premières Spé PC"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}

À la fin du document [Chap. 9,1](../1-description-fluide), on a précisé que pour décrire **l'état d'un gaz au niveau macroscopique**, il est nécessaire de prendre en compte les paramètres **volume**, **pression**, **température** et **quantité de matière**, et que ces quatre paramètres ne sont pas indépendant les uns des des autres.

{{% /note %}}


> L'objectif de cette séance est de *mettre en évidence la relation qui existe entre la pression au sein d'un gaz et son volume, la température et la quantité de matière restant constantes*. Cette relation porte le nom de **loi de Boyle-Mariotte**.

## Manipulations 

- Choisir pour la seringue à disposition le volume le plus grand possible.
- Connecter la seringue au pressiomètre.
- Relever les valeurs des pressions pour les volumes ci-dessous et compléter le tableau :

<center>

| Volume ($\pu{cm3}$) | 60 | 55 | 50 | 45 | 40 | 35 | 30 |
| :--: | :--: | :--: | :--: | :--: | :--: | :--: | :--: |
| Pression (hPa) | ... | ... | ... | ... | ... | ... | ... |

</center>

## Préparation des variables du problème

{{% note normal %}}

Le fichier de travail se trouve à cette {{% remote "adresse" "https://dlatreyte.github.io/jupyter-lite/lab?path=premiere-spe-pc%2Fdescription-fluide-au-repos%2Fboyle-mariotte-eleves.ipynb" %}}

{{% /note %}}

1. Compléter les instructions suivantes :
```python
V = [....]  # cm³
P = [....]  # hPa
```

{{% solution "Réponse" %}}

```python
V = [30, 35, 40, 45, 50, 55, 60]  # cm³
P = [1935, 1680, 1521, 1338, 1218, 1093, 1004]  # hPa
```

{{% /solution %}}

2. Convertir les volumes en $\pu{m3}$.
```python
for i in range(len(V)):
    V[i] = ....
```

{{% solution "Réponse" %}}

```python
for i in range(len(V)):
    V[i] = V[i] * 1e-6
```

{{% /solution %}}

3. De la même façon, convertir les pressions en Pa (pascal).
```python
.... :
    ....
```

{{% solution "Réponse" %}}

```python
for i in range(len(P)):
    P[i] = P[i] * 100
```

{{% /solution %}}

## Évolution de la pression en fonction du volume

4. Compléter les instructions suivantes de façon à afficher l'évolution de la pression lorsque le volume varie.
```python
sns.set()
plt.figure()
plt.plot(...., ...., 'o', label="Pression (Pa)")
plt.xlabel(r"$V\ (\mathrm{m}^3)$")
plt.ylim(50000, 250000)
plt.xlim(1e-5, 8e-5)
plt.legend()
plt.show()
```

{{% solution "Réponse" %}}

```python
sns.set()
plt.figure()
plt.plot(V, P, 'o', label="Pression (Pa)")
plt.xlabel(r"$V\ (\mathrm{m}^3)$")
plt.ylim(50000, 250000)
plt.xlim(1e-5, 8e-5)
plt.legend()
plt.show()
```

{{% /solution %}}

5. La relation entre $P$ et $V$ est-elle linéaire ?

{{% solution "Réponse" %}}

$P$ n'est pas proportionnel à $V$.

{{% /solution %}}

6. La variable `invV` doit référencer une liste dont les valeurs sont les inverses des valeurs de la liste référencée par la variable `V`. Écrire le code qui réalise cette opération.
```python
invV = []
for elt in V:
    ....
```

{{% solution "Réponse" %}}

```python
invV = []
for elt in V:
    invV.append(1 / elt)
```

{{% /solution %}}

7. Compléter les instructions suivantes de façon à afficher l'évolution de la pression P en focntion de `invV`.
```python
plt.plot(...., ...., 'o', label="Pression (Pa)")
plt.xlabel(r"$1/V\ (\mathrm{m}^{-3})$")
plt.legend()
plt.show()
```

{{% solution "Réponse" %}}

```python
plt.plot(invV, P, 'o', label="Pression (Pa)")
plt.xlabel(r"$1/V\ (\mathrm{m}^{-3})$")
plt.legend()
plt.show()
```

{{% /solution %}}

8. La relation est-elle cette fois linéaire ?

{{% solution "Réponse" %}}

$P$ et $\dfrac{1}{V}$ sont proportionnels.

{{% /solution %}}

### Modélisation du comportement de $P$ en fonction de l'inverse du volume

On effectue dans cette partie une modélisation, en postulant que la relation qui existe entre $P$ et $\dfrac{1}{V}$ est une relation de linéarité.

9. Compléter le code de la fonction `modele` de façon à ce qu'elle traduise le comportement recherché.    
Compléter aussi le code des deux instructions qui réalisent le tracé.
```python
# Fonction modèle
def modele(x, a):
    return ....

# Détermination des paramètres optimaux
popt, pcov = curve_fit(modele, invV, P)
a_mod = popt[0]

# Préparation du tracé
invV_mod = np.linspace(min(invV), max(invV), 50)
P_mod = modele(invV_mod, a_mod)

# Tracé
plt.plot(...., ...., 'o', label="Pression (Pa)")
plt.plot(...., ...., '-', label="Pression (Pa) modélisée")
plt.xlabel(r"$1/V\ (\mathrm{m}^{-3})$")
plt.legend()
plt.show()
print(popt)
```

{{% solution "Réponse" %}}

```python
# Fonction modèle
def modele(x, a):
    return a * x

# Détermination des paramètres optimaux
popt, pcov = curve_fit(modele, invV, P)
a_mod = popt[0]

# Préparation du tracé
invV_mod = np.linspace(min(invV), max(invV), 50)
P_mod = modele(invV_mod, a_mod)

# Tracé
plt.plot(invV, P, 'o', label="Pression (Pa)")
plt.plot(invV_mod, P_mod, '-', label="Pression (Pa) modélisée")
plt.xlabel(r"$1/V\ (\mathrm{m}^{-3})$")
plt.legend()
plt.show()
print(popt)
```

{{% /solution %}}

10. Afficher la valeur du paramètre `a_mod`.

{{% solution "Réponse" %}}

```python
print("a = {}".format(a_mod))
```

{{% /solution %}}

## Corrigé complet

{{% solution "Corrigé" %}}

{{% remote "Correction interactive" "https://dlatreyte.github.io/jupyter-lite/lab?path=premiere-spe-pc%2Fdescription-fluide-au-repos%2Fboyle-mariotte.ipynb" %}}

{{% /solution %}}

## À retenir

{{% note tip %}}
#### Modèle du gaz parfait

Le modèle du gaz parfait est constitue une tentative de description du comportement d'un gaz réel. Lors de cette modèlisation :
- *on néglige la structure interne des entités qui constituent le gaz ; elles sont considérées comme étant de points matériels*.
- *on néglige les interactions qui existent entre les entités qui constituent le gaz*. Ces entités n'interagissent donc qu'avec les parois du récipient qui contient le gaz.

Quatre paramètres (non indépendant entre eux) permettent de décrire un gaz parfait en équilibre (mécanique et thermique) : $P$ la pression (en pascal), $T$ la température (en kelvin), $V$ le volume (en mètre-cube) et $n$ la quantité de matière (en mole).
{{% /note %}}

{{% note warning %}}
Le modèle du gaz parfait ne décrit fidèlement le comportement d'un gaz réel qu'à *basse pression*.\
On utilise cependant régulièrement ce modèle en chimie.
{{% /note %}}


{{% note tip %}}
La loi de Boyle-Mariotte relie la *pression* et le *volume* d'un **gaz parfait** *à température constante*. Son expression mathématique est :
$$
    P\\, V = \text{cste}
$$
En d'autres termes, *maintenir la température constante pendant une augmentation de pression d'un gaz exige une diminution de volume*. Inversement, *la réduction de la pression du gaz passe par une augmentation de volume*.\
La valeur exacte de la constante n'a pas besoin d'être connue pour appliquer la loi entre deux volumes de gaz sous des pressions différentes, à la même température :
$$
    P_1\\, V_1 = P_2\\, V_2 
$$
{{% /note %}}
