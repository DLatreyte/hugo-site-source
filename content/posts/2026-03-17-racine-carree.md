---
title: "Contrôler une valeur à l’aide du typage"
subtitle: "...en Python"
author: ""
type: ""
date: 2026-03-18T14:58:15+01:00
draft: true
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---


 Lorsqu’une fonction n’accepte en réalité qu’une partie des valeurs d’un type, il peut être utile de créer un type spécifique qui représente exactement les valeurs autorisées.



## Idée de départ

On prend l’exemple de la fonction `square_root`. Cette fonction ne peut pas recevoir n’importe quelle valeur : elle attend une valeur *compatible avec la racine carrée*.

{{% note warning %}}

  - Le point important n’est pas la racine carrée elle-même.
  - Le point important est : _comment faire apparaître dans le code une contrainte sur les valeurs autorisées_.

{{%  /note %}}



## Le problème avec les types primitifs


Si on définit de cette fonction comme :
```py
def square_root(number: float) -> float:
```
on dit seulement que `number` est un `float`. Il peut donc aussi bien être `4.0`, que `-3.0`, ou encore `NaN`. _La fonction doit donc vérifier elle-même que la valeur reçue est valide_, et cette vérification peut être oubliée.

{{% note tip %}}

  `float` décrit une *catégorie technique large*, pas une *valeur métier valide*.

{{%  /note %}}

## Première conséquence : la validation est dispersée


```py
def square_root(number: float) -> float:
    if not math.isfinite(number):
        raise ValueError("La valeur doit être un nombre fini.")
    if number < 0:
        raise ValueError(f"Une valeur non négative ne peut pas valoir {number}.")
    return number**0.5
```

{{% note tip %}}

Un type primitif comme `float` est souvent *trop général* pour exprimer une contrainte métier précise.

{{%  /note %}}

## Approche basée sur les types


Une autre approche consiste à créer un *objet-valeur (value object)* chargé de garantir cette contrainte dès sa création :

```py
from dataclasses import dataclass
import math


@dataclass(frozen=True)
class NonNegativeFloat:
    value: float

    def __post_init__(self):
        if not math.isfinite(self.value):
            raise ValueError("La valeur doit être un nombre fini")
        if self.value < 0:
            raise ValueError(f"Une valeur non négative ne peut pas valoir {self.value}")
```

On peut alors définir plus simplement la fonction `square_root` :

```py
def square_root(number: NonNegativeFloat) -> float:
    return number.value**0.5
```

La fonction `square_root` n’a pas besoin de vérifier si `number.value` est négatif, _le type l'assure_. En effet, si un objet de type `NonNegativeFloat` existe, alors il respecte déjà l’*invariant du type*.



#idea(breakable: true)[
  Un *invariant* est une propriété qui doit être vraie pour toute instance valide d’un type.

  Dans le cas présent, l’invariant de `NonNegativeFloat` est : *« la valeur stockée n’est ni négative, ni NaN »*.
]

On a déplacé la *validation* :
- *avant* : la fonction vérifie à chaque appel ;
- *après* : le type garantit la validité une fois pour toutes à la construction.

On a donc réduit :

- les vérifications répétées ;
- les oublis ;
- les incohérences dans le code.

Cette approche permet de mieux exprimer l’intention du programme.

#info(breakable: true)[
  Les types peuvent servir à modéliser des contraintes métier, et pas seulement à classifier des données.
]

