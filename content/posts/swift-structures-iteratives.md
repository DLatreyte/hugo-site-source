---
title: "Langage Swift, les structures itératives"
subtitle: ""
author: ""
type: ""
date: 2025-12-23T21:58:03+01:00
draft: true
toc: true
tags: ["Swift"]
categories: ["Informatique"]
image: ""
solution_est_visible: true
auto_numbering: false
---

### Exercice 1 ###

Soit la fonction suivante :
```swift
func inconnue(a: Int, b: Int) -> Int {
    var x = a
    var y = b

    var r = x % y
    while r != 0 {
        x = y
        y = r
        r = x % y
    }
    return y
}
``` 

**Remarque :** En Swift, les paramètres de fonction sont des constantes (`let`) par défaut, donc on ne peut pas leur réaffecter une valeur.

1. Examiner le code, repérer les instructions concernées par la boucle et déterminer l'instruction de fin de boucle.

---
{{% details "**Solution**" %}}
Boucle :
```swift
while r != 0 {
        x = y
        y = r
        r = x % y
    }
```
Instruction de fin de boucle : `r != 0`.
{{% /details %}}
---

2. Quelle est l'instruction qui permet de modifier le résultat de l'évaluation du test de sortie de boucle ?

---
{{% details "**Solution**" %}}
Instruction qui permet de modifier le résultat de l'évaluation : `r = x % y`.
{{% /details %}}
---

3. On considère l’appel `inconnue(30, 42)`.
En détaillant chaque étape de l’exécution de la boucle, déterminer la valeur retournée par la fonction.
On présentera le raisonnement sous la forme d’un tableau d’évolution des variables. <br /> Vérifier le résultat obtenu en exécutant le programme.

---
{{% details "**Solution**" %}}

{{% /details %}}
---

4. En supposant que la fonction soit appelée avec les valeurs 35 et 6, exécuter le programme à la main et déterminer la valeur retournée. Pour s'aider, construire un tableau d'évolution du contenu de chaque variable utilisée. <br /> Vérifier le résultat obtenu en exécutant le programme.
6. Quel est le calcul réalisé par ce programme ?
