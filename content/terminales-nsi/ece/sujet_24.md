---
title: "NUMERIQUE et SCIENCES INFORMATIQUES"
subtitle: "Partie pratique"
author: ""
type: ""
date: 2021-12-07T07:57:06+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Exercice 1 (50% des points)

Écrire une fonction `recherche` qui prend en paramètres `elt` un nombre et `tab` un tableau de nombres, et qui renvoie l’*indice de la dernière occurrence* de `elt` dans `tab` si `elt` est dans `tab` et le -1 sinon.

#### Jeu de tests possible

```python
if __name__ == "__main__":
    assert recherche(1, [2, 3, 4]) == -1
    assert recherche(1, [10, 12, 1, 56]) == 2
    assert recherche(1, [1, 50, 1]) == 2
    assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5
```

{{% solution "Solution" %}}

```python
def recherche(elt: int, tab: List[int]) -> int:
    """
    Retourne l’indice de la dernière occurrence de `elt` dans `tab` si `elt` est dans `tab` et le -1 sinon.
    """
    indice = -1
    i = len(tab) - 1   # Dernier indice du tableau
    trouve = False
    while i > 0 and not trouve:
        if tab[i] == elt:
            indice = i
            trouve = True
        i = i - 1
    return indice


if __name__ == "__main__":
    assert recherche(1, [2, 3, 4]) == -1
    assert recherche(1, [10, 12, 1, 56]) == 2
    assert recherche(1, [1, 50, 1]) == 2
    assert recherche(1, [8, 1, 10, 1, 7, 1, 8]) == 5
```

{{% /solution %}}

## Exercice 2 (50% des points)

On définit une classe gérant une adresse IPv4.    
On rappelle qu’une adresse IPv4 est une adresse de longueur 4 octets, notée en décimale à point, en séparant chacun des octets par un point. 

On considère un réseau privé avec une plage d’adresses IP de 192.168.0.0 à 192.168.0.255.    
On considère que les adresses IP saisies sont valides.    
Les adresses IP 192.168.0.0 et 192.168.0.255 sont des adresses réservées.

Le code ci-dessous implémente la classe `AdresseIP` :

```python
from __future__ import annotations
from typing import List


class AdresseIP:
    def __init__(self: AdresseIP, adresse: str) -> None:
        self.adresse = ....

    def liste_octet(self: AdresseIP) -> List[int]:
        """
        Retourne une liste de nombres entiers : la liste des octets de l'adresse IP
        """
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self: AdresseIP) -> bool:
        """
        Retourne True si l'adresse IP est une adresse réservée, False sinon
        """
        return .... or ....

    def adresse_suivante(self: AdresseIP) -> AdresseIP:
        """
        Retourne un objet de AdresseIP avec l'adresse IP qui suit l’adresse self si elle existe et False sinon
        """
        octet = ....
        if .... < 254:
            octet_nouveau = .... + ....
            return AdresseIP('192.168.0.' + ....)
        else:
            return False
````

Compléter le code ci-dessus et instancier trois objets : `adresse1`, `adresse2`, `adresse3` avec respectivement les arguments suivants : `'192.168.0.1'`, `'192.168.0.2'`, `'192.168.0.0'`.

#### Jeu de tests possible

```python
if __name__ == "__main__":
    assert adresse1.est_reservee() == False
    assert adresse3.est_reservee() == True
    assert adresse2.adresse_suivante().adresse == '192.168.0.3'
``` 

{{% solution "Solution" %}}

```python
from __future__ import annotations
from typing import List


class AdresseIP:
    def __init__(self: AdresseIP, adresse: str) -> None:
        self.adresse = adresse

    def liste_octet(self: AdresseIP) -> List[int]:
        """
        Retourne une liste de nombres entiers : la liste des octets de l'adresse IP
        """
        return [int(i) for i in self.adresse.split(".")]

    def est_reservee(self: AdresseIP) -> bool:
        """
        Retourne True si l'adresse IP est une adresse réservée, False sinon
        """
        return self.adresse == '192.168.0.0' or self.adresse == '192.168.0.255'

    def adresse_suivante(self: AdresseIP) -> AdresseIP:
        """
        Retourne un objet de AdresseIP avec l'adresse IP qui suit l’adresse self si elle existe et False sinon
        """
        octet = self.liste_octet()[-1]
        if octet < 254:
            octet_nouveau = octet + 1
            return AdresseIP('192.168.0.' + str(octet_nouveau))
        else:
            return False


if __name__ == "__main__":
    adresse1 = AdresseIP('192.168.0.1')
    adresse2 = AdresseIP('192.168.0.2')
    adresse3 = AdresseIP('192.168.0.0')

    assert adresse1.est_reservee() == False
    assert adresse3.est_reservee() == True
    assert adresse2.adresse_suivante().adresse == '192.168.0.3'
```

{{% /solution %}}