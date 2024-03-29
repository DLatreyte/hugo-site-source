---
title: "Le tri fusion"
subtitle: ""
author: ""
type: ""
date: 2020-11-18T17:12:24+04:00
draft: false
toc: true
tags: ["Diviser pour régner", "Tri"]
categories: ["Terminales Spé NSI"]
image: ""
solution_est_visible: false
auto_numbering: true
---


## Le tri fusion d'un tableau

### Description du tri

Dans cette partie, nous allons essayer de comprendre les principes sur lesquels s'appuie ce tri. Son implémentation, pour des tableaux ou des listes chaînées, sera développée dans les prochaines sections.

Le tri fusion s'appuie sur la méthode **Diviser pour régner** pour trier les $n$ éléments d'une séquence $S$ :

1. **Diviser :** Si la séquence $S$ est composée de 0 ou un élément, retourner $S$ immédiatement ; cette séquence est déjà triée. Si la séquence $S$ est composée de plus de deux éléments, la diviser en deux sous-séquences $S_1$ et $S_2$ contenant chacune environ la moitié des éléments de $S$ ; donc $S_1$ est formée des $\left\lfloor \dfrac{n}{2} \right\rfloor$ premiers éléments de $S$ contient les $\left\lceil \dfrac{n}{2} \right\rceil$ derniers éléments de $S$.

2. **Régner :** Trier récursivement $S_1$ et $S_2$.

3. **Combiner :** Reformer la séquence $S$ en combinant, dans l'ordre, les éléments des séquences triées $S_1$ et $S_2$.

{{% note normal %}}

- $\left\lfloor \dfrac{n}{2} \right\rfloor$ est la notation mathématique pour l'opération en Python `n // 2`, c'est à dire *le plus grand entier inférieur au résultat de la division de* $n$ *par 2*.
- $\left\lceil \dfrac{n}{2} \right\rceil$ est la notation mathématique pour l'opération en Python `n // 2 + 1`, c'est à dire pour *le plus petit entier supérieur au résultat de la division de* $n$ *par 2*.
{{% /note %}}

Pour bien comprendre la méthode employée, le plus simple est de construire un arbre binaire dans lequel chaque nœud est le résultat d'un appel récursif.

{{< mermaid >}}
flowchart TD
    S("85 &nbsp;&nbsp; 24  &nbsp;&nbsp;  63  &nbsp;&nbsp;  45  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("85  &nbsp;&nbsp;  24  &nbsp;&nbsp;  63  &nbsp;&nbsp;  45")
    S --> S2("17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50")
    S1 --> S11("85  &nbsp;&nbsp;  24")
    S1 --> S12("63  &nbsp;&nbsp;  45")
    S11 --> S111(("85"))
    S11 --> S112(("24"))
    S12 --> S121(("63"))
    S12 --> S122(("45"))
    S2 --> S21("17  &nbsp;&nbsp;  31")
    S21 --> S211((17))
    S21 --> S212((31))
    S2 --> S22("96  &nbsp;&nbsp; 50")
    S22 --> S221((96))
    S22 --> S222((50))
{{< /mermaid >}}
> Résultats des différents appels récursifs (Partie **Diviser**).

{{< mermaid >}}
flowchart BT
    S111((85)) --> S11("24 &nbsp;&nbsp; 85")
    S112((24)) --> S11
    S121((63)) --> S12("45 &nbsp;&nbsp; 63")
    S122((45)) --> S12
    S11 --> S1("24 &nbsp;&nbsp; 45 &nbsp;&nbsp; 63 &nbsp;&nbsp; 85")
    S12 --> S1
    S1 --> S("17 &nbsp;&nbsp; 24 &nbsp;&nbsp; 31 &nbsp;&nbsp; 45 &nbsp;&nbsp; 50 &nbsp;&nbsp; 63 &nbsp;&nbsp; 85 &nbsp;&nbsp; 96")
    S211((17)) --> S21("17 &nbsp;&nbsp; 31")
    S212((31)) --> S21
    S221((96)) --> S22("50 &nbsp;&nbsp; 96")
    S222((50)) --> S22
    S21 --> S2("17 &nbsp;&nbsp; 31 &nbsp;&nbsp; 50 &nbsp;&nbsp; 96")
    S22 --> S2
    S2 --> S
{{< /mermaid >}}
> Résultats progressifs après les étapes **Régner** et **Fusionner**.

### Décomposition de l'exécution de l'algorithme

----

#### Légende

- *Chaque nœud représente un appel récursif* ;
- **Nœud avec une bordure en pointilles :** *appels récursifs non encore effectués* ;
- **Nœud avec une bordure en gras :** *appel récursif en cours* ;
- **Nœud vide avec une bordure :** *partie déjà traitée* ;
- **Nœud en partie vide (contenant tout de même des valeurs) :** *appels récursifs en attente*.

----

{{< mermaid >}}
flowchart TD
    S("85 &nbsp;&nbsp; 24  &nbsp;&nbsp;  63  &nbsp;&nbsp;  45  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") -.- S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 -.- S11("—  &nbsp;&nbsp;  —")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 -.- S111(("—"))
    S11 -.- S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S1,S2,S11,S12,S21,S22,S111,S112,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("85  &nbsp;&nbsp;  24  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 -.- S11("—  &nbsp;&nbsp;  —")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 -.- S111(("—"))
    S11 -.- S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S11,S12,S21,S22,S111,S112,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S1 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 --> S11("85  &nbsp;&nbsp;  24")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 -.- S111(("—"))
    S11 -.- S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S12,S21,S22,S111,S112,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S11 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 --> S11("—  &nbsp;&nbsp;  24")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 --> S111(("85"))
    S11 -.- S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S12,S21,S22,S112,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S111 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 --> S11("85  &nbsp;&nbsp;  —")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 <--> S111(("—"))
    S11 --> S112(("24"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S12,S21,S22,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S112 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 --> S11("24 &nbsp;&nbsp;  85")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S12,S21,S22,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S11 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  85  &nbsp;&nbsp; 63 &nbsp;&nbsp;  45")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 -.- S12("—  &nbsp;&nbsp;  —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S12,S21,S22,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S1 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  85  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 --> S12("63  &nbsp;&nbsp;  45")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 -.- S121(("—"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S21,S22,S121,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S12 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  85  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 --> S12("—  &nbsp;&nbsp;  45")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 --> S121(("63"))
    S12 -.- S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S21,S22,S122,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S121 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  85  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 --> S12("63  &nbsp;&nbsp; —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 --> S122(("45"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S21,S22,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S122 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  85  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 --> S12("45  &nbsp;&nbsp; 63")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 <--> S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S21,S22,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S12 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("— &nbsp;&nbsp; —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50") --> S1("24  &nbsp;&nbsp;  45  &nbsp;&nbsp; 63 &nbsp;&nbsp;  85")
    S -.- S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 <--> S12("—  &nbsp;&nbsp; —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 <--> S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S2,S21,S22,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S1 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("24 &nbsp;&nbsp; 45  &nbsp;&nbsp;  63  &nbsp;&nbsp;  85  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —") <--> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S --> S2("17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  96  &nbsp;&nbsp;  50")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 <--> S12("—  &nbsp;&nbsp; —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 <--> S122(("—"))
    S2 -.- S21("—  &nbsp;&nbsp;  —")
    S21 -.- S211(("—"))
    S21 -.- S212(("—"))
    S2 -.- S22("—  &nbsp;&nbsp; —")
    S22 -.- S221(("—"))
    S22 -.- S222(("—"))
    classDef pointillet stroke-dasharray: 5 5;
    class S21,S22,S211,S212,S221,S222 pointillet;
    classDef gras stroke-width:3px;
    class S2 gras;
{{< /mermaid >}}

<center>
<strong>... et après quelques appels supplémentaires...</strong>
</center>

{{< mermaid >}}
flowchart TD
    S("24 &nbsp;&nbsp; 45  &nbsp;&nbsp;  63  &nbsp;&nbsp;  85  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —") <--> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S --> S2("17  &nbsp;&nbsp;  31  &nbsp;&nbsp;  50  &nbsp;&nbsp;  96")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 <--> S12("—  &nbsp;&nbsp; —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 <--> S122(("—"))
    S2 <--> S21("—  &nbsp;&nbsp;  —")
    S21 <--> S211(("—"))
    S21 <--> S212(("—"))
    S2 <--> S22("—  &nbsp;&nbsp; —")
    S22 <--> S221(("—"))
    S22 <--> S222(("—"))

    classDef gras stroke-width:3px;
    class S2 gras;
{{< /mermaid >}}

{{< mermaid >}}
flowchart TD
    S("17 &nbsp;&nbsp; 24  &nbsp;&nbsp;  31  &nbsp;&nbsp;  45  &nbsp;&nbsp;  50  &nbsp;&nbsp;  63  &nbsp;&nbsp;  85  &nbsp;&nbsp;  96") <--> S1("—  &nbsp;&nbsp;  —  &nbsp;&nbsp; — &nbsp;&nbsp;  —")
    S <--> S2("—  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —  &nbsp;&nbsp;  —")
    S1 <--> S11("— &nbsp;&nbsp;  —")
    S1 <--> S12("—  &nbsp;&nbsp; —")
    S11 <--> S111(("—"))
    S11 <--> S112(("—"))
    S12 <--> S121(("—"))
    S12 <--> S122(("—"))
    S2 <--> S21("—  &nbsp;&nbsp;  —")
    S21 <--> S211(("—"))
    S21 <--> S212(("—"))
    S2 <--> S22("—  &nbsp;&nbsp; —")
    S22 <--> S221(("—"))
    S22 <--> S222(("—"))

    classDef gras stroke-width:3px;
    class S gras;
{{< /mermaid >}}

{{% note normal %}}
On peut montrer que la *hauteur de l'arbre des appels récursifs* est voisine (en fonction de la définition choisie pour la hauteur) de $\log_2 (n)$ où $n$ est le nombre d'éléments dans la séquence.
{{% /note %}}

## Implémentation du tri fusion pour un tableau

1. Étudier le code suivant et remplacer les ... pour chaque numéro.

```python
def tri_fusion(S: list[int]) -> None:
    """
    Implémentation du tri fusion.
    La liste S est modifiée en place.
    """
    n = len(S)  # ... (0)

    if n < 2:
        return None  # ... (1)

    # Diviser, Régner, Combiner ? ... (2)
    milieu = n // 2
    S1 = S[:milieu]  # .... (3)
    S2 = S[milieu:]  # .... (4)

    # Diviser, Régner, Combiner ? ... (5)
    tri_fusion(S1)  # ... (6)
    tri_fusion(S2)  # ... (7)

    # Diviser, Régner, Combiner ? ... (8)
    fusion(S1, S2, S)  # ... (9)
```

2. Étudier le code suivant et expliquer comment s'effectue la fusion.

```python
def fusion(S1: list[int], S2: list[int], S: list[int]) -> None:
    """
    Combine les éléments des deux listes S1 et S2 dans la liste S (en place).
    i est le nombre d'élément(s) de S1 copié(s) dans S. 
    j est le nombre d'élément(s) de S2 copié(s) dans S. 
    On doit donc avoir i + j <= len(S).
    """
    i = 0
    j = 0

    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            S[i + j] = S1[i]
            i = i + 1
        else:
            S[i + j] = S2[j]
            j = j + 1
```

3. Étudier le comportement du programme complet à l'aide de pythontutor.
Construire la liste à l'aide de l'instruction :

```python
liste = [randint(1, 400) for i in range(5)]
```

4. Quelle est la complexité de la fonction `fusion` ?

5. Essayer d'évaluer la complexité de l'algorithme sans faire de calcul.

---

{{% solution "Solution" %}}

{{< remote "Code Python" "https://repl.it/@dlatreyte/tri-fusion-tableaux" >}}

{{% /solution %}}

---

## Le tri fusion d'une liste chaînée

Dans cette section, on cherche à adapter l'algorithme de tri fusion à une liste chaînée.

1. Écrire le code de la classe `Cellule` permettant d'implémenter une liste chaînée. Cette classe sert juste de structure et définit les champs `valeur`, de type `int`, et `suivant`, de type `Cellule`, initialisé à `None`.
{{% solution "Réponse" %}}

```python
class Cellule():
    """
    Implémentation d'une cellule
    """

    def __init__(self: Cellule, valeur: int, 
                 suivant: Cellule = None) -> None:
        self.valeur = valeur
        self.suivant = suivant
```

{{% /solution %}}

2. Dans la partie principale du programme, écrire le code qui crée la liste chaînée `[14, 11, 2, 35, 9, 1]`.
{{% solution "Réponse" %}}

```python
if __name__ == "__main__":
    lst = Cellule(14, Cellule(11, Cellule(2, Cellule(35, Cellule(9, Cellule(1))))))
```

{{% /solution %}}

3. Définir le code de la fonction `tri_fusion` dont la spécification est

```python
def tri_fusion(lst: Cellule) -> Cellule:
    """
    Implémente l'algorithme de tri-fusion.
    Une nouvelle liste chaînée est créée.
    """
```

Cette fonction doit utiliser la fonction `coupe` (définie un peu plus bas), qui découpe une liste chaînée en deux sous-listes, et la fonction `fusion` (définie elle aussi un peu plus bas) qui réalise la fusion de deux listes triées.  

La fonction `tri_fusion` doit mettre en œuvre le principe « Diviser pour régner ».

{{% solution "Réponse" %}}

```python
def tri_fusion(lst: Cellule) -> Cellule:
    """
    Implémente l'algorithme de tri-fusion.
    Une nouvelle liste chaînée est créée.
    """
    if lst is None or lst.suivant is None:
        return lst

    l1, l2 = coupe(lst)

    return fusion(tri_fusion(l1), tri_fusion(l2))
```

{{% /solution %}}

4. Définir la fonction `coupe` dont la spécification est

```python
def coupe(lst: Cellule) -> Cellule:
    """
    Découpe la liste L2 est deux sous-listes de même
    longueur à un élément près.
    """
```

{{% solution "Réponse" %}}

```python
def coupe(lst: Cellule) -> Cellule:
    """
    Découpe la liste L2 est deux sous-listes de même
    longueur à un élément près.
    """
    l1, l2 = None, None

    while lst is not None:
        l1, l2 = Cellule(lst.valeur, l2), l1
        lst = lst.suivant

    return l1, l2
```

ou

```python
def coupe(lst: "Cellule") -> "Cellule":
    """
    Découpe la liste L2 est deux sous-listes de même
    longueur à un élément près.
    """
    l1, l2 = None, None

    i = 0
    while lst is not None:
        if i % 2 == 0:
            l1 = Cellule(lst.valeur, l1)
        else:
            l2 = Cellule(lst.valeur, l2)
        i += 1
        lst = lst.suivant

    return l1, l2
```

ou

```python
def coupe(lst: Cellule, l1: Cellule = None, l2: Cellule = None, i: int = 0) -> Tuple[Cellule, Cellule]:
    """
    Découpe la liste L2 est deux sous-listes de même
    longueur à un élément près.
    """
    if lst is None:
        return l1, l2
    else:
        if i % 2 == 0:
            return coupe(lst.suivant, Cellule(lst.valeur, l1), l2, i + 1)
        else:
            return coupe(lst.suivant, l1, Cellule(lst.valeur, l2), i + 1) 
```

{{% /solution %}}

5. Définir la fonction `fusion` dont la spécification est

```python
def fusion(l1: Cellule, l2: Cellule) -> Cellule:
    """
    Réalise la fusion des deux listes l1 et l2 
    triées.

    Algorithme récursif.
    """
```

{{% solution "Réponse" %}}

```python
def fusion(l1: "Cellule", l2: "Cellule") -> "Cellule":
    """
    Réalise la fusion des deux listes l1 et l2 
    triées.
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1
        
    if l1.valeur <= l2.valeur:
        return Cellule(l1.valeur, fusion(l1.suivant, l2))
    else:
        return Cellule(l2.valeur, fusion(l1, l2.suivant))
```

{{% /solution %}}
