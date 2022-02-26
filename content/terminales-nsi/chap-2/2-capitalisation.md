---
title: "Capitalisation d'une valeur"
subtitle: "Chapitre 2,2"
author: ""
type: ""
date: 2020-09-15T05:05:07+04:00
draft: false
toc: true
tags: ["Modules", "Exceptions", "Assertions"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---
Cette séance a pour objectif de vous familiariser avec la *création et la 
manipulation de modules*.

{{% note normal %}}
Comme il est maintenant de tradition vous diviserez le code de votre programme 
principal en trois parties:

1. *Importation des modules*&nbsp;;
1. *Définitions des fonctions*&nbsp;;
1. *Partie principale*  (lieu d'appel des fonctions).

*Vous documenterez aussi **systématiquement**  vos fonctions*  (une aide sera 
fournie dans les questions relatives à la définition de chacune de ces 
fonctions).
{{% /note %}}

En mathématique, on démontre qu'un capital placé à un certain taux 
d'intérêt évolue selon la formule&nbsp;:

$$
C = C\_{0}  \left( 1 + \dfrac{t}{360 \times 100} \right)^n
$$

où $C$ est le montant du capital considéré le jour de l'examen, $C\_{0}$ le 
montant initial du capital, $t$ le taux d'intérêt (en pourcentage) et $n$ le 
nombre de jours écoulés depuis le dépôt.

#### Remarque
Pour une durée de placement exprimée en jours, l'usage fait que l'intérêt est calculé sur la base de l'année financière ou commerciale comptant 360 jours et non pas l'année civile de 365 jours (ou 366 jours). Par ailleurs, lorsque la durée est exprimée en jours, les mois sont comptés à leur nombre exact de jours.

Selon le problème à résoudre on peut bien évidemment aussi écrire:

$$
C\_{0} = C \left( 1 + \dfrac{t}{360 \times 100} \right)^{- n}
$$

$$
  n = \frac{\ln \left( \dfrac{C}{C\_{0}} \right)}{\ln \left( 1 + \frac{t}{360
  \times 100} \right)}
$$

$$
  t = 360 \times 100 \left( \left( \dfrac{C}{C\_{0}} \right)^{1 / n} - 1
  \right)
$$

1. Créer un module, nommé `capitalisation`, qui contient les quatre 
   fonctions `montant_actuel`, `montant_initial`, 
   `jours_ecoules` et `taux_annuel` qui implémentent les quatre 
   expressions données ci-dessus.  
   Les spécification des fonctions sont les suivantes&nbsp;:
```python
def montant_actuel(C0: float, t: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du taux
    d'intérêt et de la durée de dépôt, le montant actuel.
    """
```

```python
def montant_initial(C: float, t: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant actuel, du taux
    d'intérêt et de la durée de dépôt, le montant initial déposé.
    """
```

```python
def jours_ecoules(C0: float, C: float, t: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et du taux d'intérêt, la durée écoulée en jours.
    """
```

```python
def taux_annuel(C0: float, C: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et de la durée de dépôt (en jours), le taux annuel.
    """
```
{{% note warning %}}
Penser à gérer les exceptions (le module `sys` possède une fonction `exit` 
qui permet d'interrompre proprement un programme lorsqu'on lui passe le 
nombre 1 en argument).
{{% /note %}}

2. Placer un commentaire au début du module qui décrit son fonctionnement.

3. Incorporer à ce module un bloc `if __name__ == '__main__':` permettant de 
   tester ces fonctions.  
    Choisir les valeurs suivantes pour les variables de test&nbsp;: `C = 2.2133983053266699`, 
   `C0 = 2.0`, `t = 5.0`, `n = 730` et vérifier que chacune des fonctions 
   donne le bon résultat.

4. Écrire un programme qui importe le module créé. 
    Vérifier que les 
   commentaires intégrés au module sont accessibles à l'aide de la fonction 
   `help()`.

À l'aide de ce programme, répondre aux questions suivantes&nbsp;:

5. On place 10 000 euros à 7&nbsp;% d'intérêt. Quelle est la valeur du montant au 
    bout d'une année&nbsp;?
6. On place 10 000 euros à 7&nbsp;% d'intérêt. Au bout de quelle durée ce 
    montant est-il doublé&nbsp;?
7. On place 10&nbsp;000 euros. Au bout de 60 jours, le montant est de 10&nbsp;042 euros. 
    À quel taux d'intérêt a été placée cette somme&nbsp;?


{{% solution "Corrigé" %}}
```python
"""
Module permettant d'effectuer des calculs de capitalisation

Variables : C est le montant à l'instant considéré, C0 est le
montant initial, t est le taux d'intérêt (en pourcentage) et n
le nombre de jours écoulés depuis le dépôt.

À partir de 3 paramètres, le 4ème peut être calculé à partir de :
    C = montant_actuel(C0, t, n)
    C0 = montant_initial(C, t,n)
    n = jours_ecoules(C0,C,t)
    t = taux_annuel(C0,C,n)
"""
import sys
from math import log

def montant_actuel(C0: float, t: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du taux
    d'intérêt et de la durée de dépôt, le montant actuel.
    """
    try:
        C = C0*(1 + t / (360 * 100))**n
    except:
        print("Un des arguments passé à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return C

def montant_initial(C: float, t: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant actuel, du taux
    d'intérêt et de la durée de dépôt, le montant initial déposé.
    """
    try:
        C0 = C*(1 + t / (360*100))**(-n)
    except:
        print("Un des arguments passé à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return C0

def jours_ecoules(C0: float, C: float, t: float) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et du taux d'intérêt, la durée écoulée en jours.
    """
    try:
        n = log(C/C0) / log(1 + t/(360*100))
    except:
        print("Un des arguments passé à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return n

def taux_annuel(C0: float, C: float, n: int) -> float:
    """
    Cette fonction calcule, à partir du montant initial, du montant
    actuel et de la durée de dépôt (en jours), le taux annuel.
    """
    try:
        t = 360*100*( (C/C0)**(1/n) - 1)
    except:
        print("Un des arguments passé à la fonction est incorrect. Fin du programme.")
        sys.exit(1)
    return t


if __name__ == "__main__":
    C = 2.2133983053266699
    C0 = 2.0
    t = 5.0
    n = 730
    # Test des fonctions
    assert C == montant_actuel(C0, t, n)
    assert C0 == montant_initial(C, t, n)
    assert n == jours_ecoules(C0, C, t)
    assert t == taux_annuel(C0, C, n)
```
{{% /solution %}}