---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2021-11-07T04:57:44+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Soit le couple `(note, coefficient)`&nbsp;:
- `note` est un nombre de type flottant (`float`) compris entre 0 et 20&nbsp;;
- `coefficient` est un nombre entier positif.

Les résultats aux évaluations d'un élève sont regroupés dans une liste composée de
couples `(note,coefficient)`.       
Écrire une fonction `moyenne` (*accompagnée de sa spécification*) qui renvoie la moyenne pondérée de cette liste donnée en paramètre.     
Par exemple, l’expression `moyenne([(15, 2), (9, 1), (12, 3)])` devra renvoyer le résultat du calcul suivant&nbsp;:
$$
    \dfrac{2 \times 15 + 1 \times 9 + 3 \times 12}{2 + 1 + 3} = \pu{12,5}
$$

#### Test possible 
```python
if __name__ == "__main__":
    notes = [(15, 2), (9, 1), (12, 3)]
    assert moyenne(notes) == 12.5
``` 

{{% solution "Corrigé" %}}

```python 
from typing import List, Tuple

def moyenne(notes: List[Tuple[float]]) -> float:
    """
    Retourne la moyenne des notes pondérées passées en argument dans la liste de tuples. 
    """
    somme_notes = 0
    somme_coefs = 0

    for note in notes:
        v_note = note[0]
        v_coef = note[1]

        somme_notes += v_note * v_coef
        somme_coefs += v_coef

    return somme_notes / somme_coefs
``` 

{{% /solution %}}

## Exercice 2 (50% des points)

On cherche à déterminer les valeurs du triangle de Pascal. Dans ce tableau de forme triangulaire, chaque ligne commence et se termine par le nombre 1. Par ailleurs, la valeur qui occupe une case située à l’intérieur du tableau s’obtient en ajoutant les valeurs des deux cases situées juste au-dessus, comme l’indique la figure suivante&nbsp;:

<img src="/terminales-nsi/ece/sujet_9.png" alt="" width="70%" />

Compléter la fonction `pascal` ci-après. Elle doit renvoyer une liste correspondant au triangle de Pascal de la ligne 1 à la ligne $n$ où $n$ est un nombre entier supérieur ou égal à 2 (le tableau sera contenu dans la variable `C`). La variable `Ck` doit, quant à elle, contenir, à l’étape numéro $k$, la $k$-ième ligne du tableau.

```python
from typing import List, Tuple

def pascal(n: int) -> List[List[int]]:
    """
    Détermine les valeurs du triangle de Pascal. 
    """
    C = [[1]]
    for k in range(1, .....):
        Ck = [.....]
        for i in range(1, k):
            Ck.append(C[.....][i - 1] + C[.....][.....])
        Ck.append(.....)
        C.append(Ck)
    return C
```

#### Tests possibles

```python
if __name__ == "__main__":
    assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
``` 

{{% solution "Corrigé" %}}

```python
from typing import List, Tuple

def pascal(n: int) -> List[List[int]]:
    """
    Détermine les valeurs du triangle de Pascal. 
    """
    C = [[1]]
    for k in range(1, n + 1):
        Ck = [1]
        for i in range(1, k):
            Ck.append(C[k - 1][i - 1] + C[k - 1][i])
        Ck.append(1)
        C.append(Ck)
    return C


if __name__ == "__main__":
    assert pascal(4) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert pascal(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
```

{{% /solution %}}