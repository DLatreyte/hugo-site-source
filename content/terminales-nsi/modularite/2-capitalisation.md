---
title: "Capitalisation d'une valeur"
subtitle: ""
date: 2020-09-15T05:05:07+04:00
draft: false
toc: true
tags: ["Modules", "Exceptions", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
solution_est_visible: true
auto_numbering: true
weight: 200
---
{{< note goal >}}
Créer un module de calcul documenté, le tester, gérer les erreurs que peuvent provoquer des arguments incorrects, puis l'utiliser depuis un autre programme.
{{< /note >}}

Cette séance a pour objectif de vous familiariser avec la *création et la
manipulation de modules*.

Avant de commencer&nbsp;: on place 100 euros à 10&nbsp;% d'intérêts par an, et les intérêts de chaque année rapportent à leur tour des intérêts. Le capital au bout de deux ans vaut-il 120 euros&nbsp;?

{{< solution "Réponse" >}}
Non. Au bout d'un an, le capital vaut $100 \times \text{1,1} = 110$ euros. La deuxième année, les intérêts portent sur 110 euros&nbsp;: $110 \times \text{1,1} = 121$ euros. Chaque période multiplie le capital par le même coefficient, d'où la puissance $n$ dans la formule ci-dessous, où la période est le jour.
{{< /solution >}}

{{< note normal >}}
Comme il est maintenant de tradition vous diviserez le code de votre programme
principal en trois parties&nbsp;:

1. *Importation des modules*&nbsp;;
1. *Définitions des fonctions*&nbsp;;
1. *Partie principale*  (lieu d'appel des fonctions).

*Vous documenterez aussi **systématiquement**  vos fonctions*  (une aide sera
fournie dans les questions relatives à la définition de chacune de ces
fonctions).
{{< /note >}}

En mathématiques, on démontre qu'un capital placé à un certain taux
d'intérêt évolue selon la formule&nbsp;:

$$
C = C_{0}  \left( 1 + \dfrac{t}{360 \times 100} \right)^n
$$

où $C$ est le montant du capital considéré le jour de l'examen, $C_{0}$ le
montant initial du capital, $t$ le taux d'intérêt (en pourcentage) et $n$ le
nombre de jours écoulés depuis le dépôt.

#### Remarque

Pour une durée de placement exprimée en jours, l'usage fait que l'intérêt est calculé sur la base de l'année financière ou commerciale comptant 360 jours et non pas l'année civile de 365 jours (ou 366 jours). Par ailleurs, lorsque la durée est exprimée en jours, les mois sont comptés à leur nombre exact de jours.

Selon le problème à résoudre on peut bien évidemment aussi écrire&nbsp;:

$$
C_{0} = C \left( 1 + \dfrac{t}{360 \times 100} \right)^{- n}
$$

$$
  n = \frac{\ln \left( \dfrac{C}{C_{0}} \right)}{\ln \left( 1 + \frac{t}{360
  \times 100} \right)}
$$

$$
  t = 360 \times 100 \left( \left( \dfrac{C}{C_{0}} \right)^{1 / n} - 1
  \right)
$$

1. Créer un module, nommé `capitalisation`, qui contient les quatre
   fonctions `montant_actuel`, `montant_initial`,
   `jours_ecoules` et `taux_annuel` qui implémentent les quatre
   expressions données ci-dessus.  
   Les spécifications des fonctions sont les suivantes&nbsp;:

```python
def montant_actuel(c0: float, t: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du taux
    d'intérêt et de la durée de dépôt, le montant actuel.
    """
```

```python
def montant_initial(c: float, t: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant actuel, du taux
    d'intérêt et de la durée de dépôt, le montant initial déposé.
    """
```

```python
def jours_ecoules(c0: float, c: float, t: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et du taux d'intérêt, la durée écoulée en jours.
    """
```

```python
def taux_annuel(c0: float, c: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et de la durée de dépôt (en jours), le taux annuel.
    """
```

Dans le code, les montants $C$ et $C_0$ sont notés `c` et `c0`&nbsp;: en Python, les noms de variables et de paramètres s'écrivent en minuscules.

{{< note warning >}}
Penser à gérer les exceptions (le module `sys` possède une fonction `exit`
qui permet d'interrompre proprement un programme lorsqu'on lui passe le
nombre 1 en argument).
{{< /note >}}

{{< note tip "Coup de pouce" >}}
Chercher, pour chaque formule, les valeurs des arguments qui empêchent le calcul&nbsp;: une division par zéro (`ZeroDivisionError`), un logarithme d'un nombre négatif ou nul (`ValueError`), un résultat trop grand (`OverflowError`). Ce sont les exceptions à intercepter. Un `except:` sans nom d'exception intercepterait aussi les erreurs de programmation&nbsp;: c'est à éviter.
{{< /note >}}

2. Placer un commentaire au début du module qui décrit son fonctionnement.

3. Incorporer à ce module un bloc `if __name__ == '__main__':` permettant de
   tester ces fonctions.  
    Choisir les valeurs suivantes pour les variables de test&nbsp;: `c = 2.2133983053266699`,
   `c0 = 2.0`, `t = 5.000000000000782`, `n = 730` et vérifier que chacune des fonctions
   donne le bon résultat. Comme les résultats sont des flottants, on vérifie que l'écart avec la valeur attendue est très petit, plutôt que de tester l'égalité avec `==`.

4. Écrire un programme qui importe le module créé.
    Vérifier que les
   commentaires intégrés au module sont accessibles à l'aide de la fonction
   `help()`.

À l'aide de ce programme, répondre aux questions suivantes&nbsp;:

5. On place 10&nbsp;000 euros à 7&nbsp;% d'intérêt. Quelle est la valeur du montant au
    bout d'une année&nbsp;?
6. On place 10&nbsp;000 euros à 7&nbsp;% d'intérêt. Au bout de quelle durée ce
    montant est-il doublé&nbsp;?
7. On place 10&nbsp;000 euros. Au bout de 60 jours, le montant est de 10&nbsp;042 euros.
    À quel taux d'intérêt a été placée cette somme&nbsp;?

{{< solution "Corrigé" >}}

```python
"""
Module permettant d'effectuer des calculs de capitalisation.

Variables : c est le montant à l'instant considéré, c0 est le
montant initial, t est le taux d'intérêt (en pourcentage) et n
le nombre de jours écoulés depuis le dépôt.

À partir de 3 paramètres, le 4e peut être calculé à partir de :
    c = montant_actuel(c0, t, n)
    c0 = montant_initial(c, t, n)
    n = jours_ecoules(c0, c, t)
    t = taux_annuel(c0, c, n)
"""

import sys
from math import log

ERREURS_DE_CALCUL = (ZeroDivisionError, ValueError, OverflowError)


def montant_actuel(c0: float, t: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du taux
    d'intérêt et de la durée de dépôt, le montant actuel.
    """
    try:
        c = c0 * (1 + t / (360 * 100)) ** n
    except ERREURS_DE_CALCUL:
        print("Un des arguments passés à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return c


def montant_initial(c: float, t: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant actuel, du taux
    d'intérêt et de la durée de dépôt, le montant initial déposé.
    """
    try:
        c0 = c * (1 + t / (360 * 100)) ** (-n)
    except ERREURS_DE_CALCUL:
        print("Un des arguments passés à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return c0


def jours_ecoules(c0: float, c: float, t: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et du taux d'intérêt, la durée écoulée en jours.
    """
    try:
        n = log(c / c0) / log(1 + t / (360 * 100))
    except ERREURS_DE_CALCUL:
        print("Un des arguments passés à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return n


def taux_annuel(c0: float, c: float, n: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et de la durée de dépôt (en jours), le taux annuel.
    """
    try:
        t = 360 * 100 * ((c / c0) ** (1 / n) - 1)
    except ERREURS_DE_CALCUL:
        print("Un des arguments passés à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return t


if __name__ == "__main__":
    c = 2.2133983053266699
    c0 = 2.0
    t = 5.000000000000782
    n = 730
    # Test des fonctions : on compare des flottants avec une tolérance
    assert abs(montant_actuel(c0, t, n) - c) < 1e-9
    assert abs(montant_initial(c, t, n) - c0) < 1e-9
    assert abs(jours_ecoules(c0, c, t) - n) < 1e-9
    assert abs(taux_annuel(c0, c, n) - t) < 1e-9
```

Programme qui utilise le module, enregistré dans le même dossier&nbsp;:

```python
import capitalisation

help(capitalisation)

print(capitalisation.montant_actuel(10_000, 7, 360))
print(capitalisation.jours_ecoules(10_000, 20_000, 7))
print(capitalisation.taux_annuel(10_000, 10_042, 60))
```

5. Avec la convention de l'année de 360 jours, `montant_actuel(10_000, 7, 360)` donne un montant d'environ 10&nbsp;725,01 euros.
6. `jours_ecoules(10_000, 20_000, 7)` donne environ 3565,1 jours&nbsp;: le montant est doublé au bout de 3566 jours, soit un peu moins de 10 années de 360 jours.
7. `taux_annuel(10_000, 10_042, 60)` donne un taux d'environ 2,51&nbsp;%.

{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- écrire un module dont chaque fonction est documentée, avec une docstring de module lisible par `help` ;
- tester les fonctions d'un module dans un bloc `if __name__ == "__main__":` ;
- comparer des flottants avec une tolérance ;
- repérer les arguments qui empêchent un calcul et intercepter les exceptions correspondantes, en les nommant ;
- importer mon module dans un autre programme et l'utiliser pour répondre à un problème.
{{< /note >}}
