---
title: "Les nombres flottants"
subtitle: "Doc. 4,5"
date: 2026-11-17T06:00:00+04:00
draft: false
toc: true
tags: ["nombre réel", "flottant", "float", "virgule en base 2", "multiplications successives", "écriture périodique", "arrondi", "égalité de flottants"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: true
auto_numbering: true
weight: 50
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-4/4-5/4-5-enonce.pdf" >}}

{{< note goal >}}
Comprendre pourquoi un ordinateur ne peut écrire la plupart des nombres à virgule que de façon approchée, et en tirer une règle de programmation : ne jamais tester l'égalité de deux flottants.
{{< /note >}}

{{< question >}}
Sans utiliser l'ordinateur, prévoir ce qu'affiche Python pour l'instruction `0.1 + 0.2 == 0.3`. Vérifier ensuite dans la console, puis afficher `0.1 + 0.2`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> 0.1 + 0.2 == 0.3
False
>>> 0.1 + 0.2
0.30000000000000004
```
Presque tout le monde prévoit `True`. Le résultat n'est pas une erreur de Python : il vient de la façon dont l'ordinateur écrit 0,1 et 0,2. Cette activité explique pourquoi.
{{< /solution >}}

Les nombres à virgule sont représentés en Python par le type `float`. Le mot vient de l'anglais *floating point*, « virgule flottante ». Pour comprendre ce qui se passe, il faut d'abord savoir écrire un nombre à virgule en base 2.

## Des chiffres après la virgule en base 2

En base 10, les chiffres après la virgule ont pour poids $10^{-1} = 1/10$, $10^{-2} = 1/100$, etc. : $\text{0,375} = 3/10 + 7/100 + 5/1000$.

En base 2, on prolonge de la même façon les poids vers la droite de la virgule, en divisant chaque fois par 2 :

| **poids** | $2^1$ | $2^0$ | **,** | $2^{-1}$ | $2^{-2}$ | $2^{-3}$ |
|:---|:---|:---|:---|:---|:---|:---|
| **valeur** | 2 | 1 | **,** | $1/2 = \text{0,5}$ | $1/4 = \text{0,25}$ | $1/8 = \text{0,125}$ |

Par exemple, $(\text{0,101})_2 = 1/2 + 0/4 + 1/8 = \text{0,5} + \text{0,125} = \text{0,625}$.

{{< question >}}
Calculer la valeur décimale de $(\text{0,11})_2$, de $(\text{0,01})_2$ et de $(\text{10,1})_2$.
{{< /question >}}

{{< solution "Réponse" >}}
- $(\text{0,11})_2 = \text{0,5} + \text{0,25} = \text{0,75}$.
- $(\text{0,01})_2 = \text{0,25}$.
- $(\text{10,1})_2 = 2 + \text{0,5} = \text{2,5}$.
{{< /solution >}}

{{< qcm >}}
- question: 'Quel est le poids du premier chiffre après la virgule en base 2 ?'
  reponses:
    - '$2^{-1} = \text{0,5}$'
    - '$10^{-1} = \text{0,1}$'
    - '$2^{1} = 2$'
  bonne: 1
  explication: 'On prolonge les poids vers la droite de la virgule en divisant chaque fois par 2.'
- question: 'Que vaut $(\text{0,011})_2$ en base 10 ?'
  reponses:
    - '$\text{0,375}$'
    - '$\text{0,011}$'
    - '$\text{0,75}$'
  bonne: 1
  explication: '$0 \times \text{0,5} + 1 \times \text{0,25} + 1 \times \text{0,125} = \text{0,375}$.'
{{< /qcm >}}

## Écrire un nombre à virgule en base 2

Pour la partie entière, on utilise la méthode des divisions successives (Doc. 4,1). Pour la partie après la virgule, on fait l'inverse : on multiplie par 2. Chaque multiplication fait passer un chiffre binaire devant la virgule.

{{< note success "Exemple résolu : écrire 0,625 en base 2" >}}
On multiplie par 2. La partie entière du résultat donne le chiffre suivant ; on continue avec la partie après la virgule :

| **calcul** | **chiffre obtenu** | **on continue avec** |
|:---|:---|:---|
| $\text{0,625} \times 2 = \text{1,25}$ | **1** | $\text{0,25}$ |
| $\text{0,25} \times 2 = \text{0,5}$ | **0** | $\text{0,5}$ |
| $\text{0,5} \times 2 = 1$ | **1** | $0$ : on s'arrête |

Les chiffres se lisent cette fois **de haut en bas** : $\text{0,625} = (\text{0,101})_2$. On retrouve le résultat de la partie 1.
{{< /note >}}

{{< question >}}
Écrire $\text{0,25}$ puis $\text{0,75}$ en base 2 par la méthode des multiplications successives.
{{< /question >}}

{{< solution "Réponse" >}}
- $\text{0,25} \times 2 = \text{0,5}$ (0), puis $\text{0,5} \times 2 = 1$ (1) : $\text{0,25} = (\text{0,01})_2$.
- $\text{0,75} \times 2 = \text{1,5}$ (1), puis $\text{0,5} \times 2 = 1$ (1) : $\text{0,75} = (\text{0,11})_2$.
{{< /solution >}}

{{< question >}}
Appliquer la méthode à $\text{0,1}$. Effectuer au moins six multiplications. Que remarque-t-on ?
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Après quelques étapes, on retombe sur un nombre déjà rencontré. Que va-t-il se passer ensuite ?
{{< /note >}}

{{< solution "Réponse" >}}
| **calcul** | **chiffre** | **on continue avec** |
|:---|:---|:---|
| $\text{0,1} \times 2 = \text{0,2}$ | 0 | $\text{0,2}$ |
| $\text{0,2} \times 2 = \text{0,4}$ | 0 | $\text{0,4}$ |
| $\text{0,4} \times 2 = \text{0,8}$ | 0 | $\text{0,8}$ |
| $\text{0,8} \times 2 = \text{1,6}$ | 1 | $\text{0,6}$ |
| $\text{0,6} \times 2 = \text{1,2}$ | 1 | $\text{0,2}$ |
| $\text{0,2} \times 2 = \text{0,4}$ | 0 | $\text{0,4}$ |

On retombe sur $\text{0,2}$, déjà rencontré à la deuxième ligne : les calculs vont se répéter sans fin. On obtient $\text{0,1} = (\text{0,000110011001100}...)_2$, avec le motif $0011$ répété indéfiniment. L'écriture de $\text{0,1}$ en base 2 est **infinie**, alors qu'elle est très courte en base 10.
{{< /solution >}}

{{< question >}}
En base 10, on sait déjà qu'un nombre simple peut avoir une écriture infinie : $1/3 = \text{0,333}...$

1. Écrire $1/3$ en base 2 en partant de $1/3 \times 2 = 2/3$. Travailler avec des fractions.
1. Proposer une explication : pourquoi $\text{0,25}$ et $\text{0,625}$ ont-ils une écriture finie en base 2, mais pas $\text{0,1}$ ?
{{< /question >}}

{{< solution "Réponse" >}}
1. $1/3 \times 2 = 2/3$ (0), $2/3 \times 2 = 4/3 = 1 + 1/3$ (1), puis on retombe sur $1/3$ : $1/3 = (\text{0,010101}...)_2$, écriture infinie.
1. $\text{0,25} = 1/4$ et $\text{0,625} = 5/8$ : ce sont des fractions dont le dénominateur est une puissance de 2. En les multipliant plusieurs fois par 2, on finit par tomber sur un entier, et l'algorithme s'arrête. $\text{0,1} = 1/10$ a un dénominateur qui contient le facteur 5 : multiplier par 2 ne peut pas faire disparaître ce facteur, et la partie après la virgule ne devient jamais nulle. C'est la même raison qui rend $1/3$ infini en base 10 : 3 ne divise aucune puissance de 10.
{{< /solution >}}

{{< qcm >}}
- question: 'Quelle est l''écriture de $\text{0,5}$ en base 2 ?'
  reponses:
    - '$(\text{0,1})_2$'
    - '$(\text{0,101})_2$'
    - '$(\text{0,01})_2$'
  bonne: 1
  explication: '$\text{0,5} \times 2 = 1$ : on obtient le chiffre 1, puis la partie après la virgule est nulle et on s''arrête.'
- question: 'Quels nombres ont une écriture **finie** en base 2 ?'
  reponses:
    - '$\text{0,75}$'
    - '$\text{0,625}$'
    - '$\text{0,1}$'
    - '$1/3$'
  bonne: [1, 2]
  explication: '$\text{0,75} = 3/4$ et $\text{0,625} = 5/8$ ont un dénominateur qui est une puissance de 2. Les dénominateurs de $\text{0,1} = 1/10$ et de $1/3$ contiennent un autre facteur que 2.'
- question: 'Dans la méthode des multiplications successives, dans quel ordre lit-on les chiffres obtenus ?'
  reponses:
    - 'De haut en bas, dans l''ordre où on les obtient.'
    - 'De bas en haut, comme pour les divisions successives.'
  bonne: 1
  explication: 'Chaque multiplication par 2 fait passer devant la virgule le chiffre suivant : le premier obtenu est le premier après la virgule.'
{{< /qcm >}}

## Ce que l'ordinateur range vraiment

Un flottant Python est rangé sur 64 bits. Le nombre est écrit en base 2 sous une forme qui rappelle l'écriture scientifique : des chiffres significatifs, appelés **mantisse**, multipliés par une puissance de 2. Le nombre de chiffres de la mantisse est limité. Une écriture binaire infinie, comme celle de $\text{0,1}$, doit donc être **coupée** : l'ordinateur range le nombre le plus proche de $\text{0,1}$ qu'il sait écrire, mais pas $\text{0,1}$ lui-même.

{{< question >}}
Python arrondit l'affichage des flottants pour qu'il soit lisible. On peut demander davantage de chiffres avec une f-string (Doc. 2,2). Exécuter :

```python
>>> f"{0.1:.20f}"
>>> f"{0.25:.20f}"
>>> f"{0.1 + 0.2:.20f}"
>>> f"{0.3:.20f}"
```

Expliquer à l'aide de ces résultats pourquoi `0.1 + 0.2 == 0.3` vaut `False`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
>>> f"{0.1:.20f}"
'0.10000000000000000555'
>>> f"{0.25:.20f}"
'0.25000000000000000000'
>>> f"{0.1 + 0.2:.20f}"
'0.30000000000000004441'
>>> f"{0.3:.20f}"
'0.29999999999999998890'
```
$\text{0,25}$ est rangé exactement, car son écriture binaire est finie. $\text{0,1}$ et $\text{0,2}$ sont rangés avec une petite erreur. Ces erreurs s'additionnent, et le résultat de l'addition n'est pas le flottant le plus proche de $\text{0,3}$ : la machine compare deux nombres réellement différents.
{{< /solution >}}

{{< question >}}
Prévoir, puis vérifier : `0.5 + 0.25 == 0.75`. Le résultat contredit-il la règle « il ne faut pas tester l'égalité de deux flottants » ?
{{< /question >}}

{{< solution "Réponse" >}}
Le résultat est `True` : $\text{0,5}$, $\text{0,25}$ et $\text{0,75}$ s'écrivent exactement en base 2, le calcul est donc exact. Cela ne contredit pas la règle : dans un programme, on ne sait pas en général si les valeurs manipulées ont une écriture binaire finie. Un test d'égalité peut fonctionner pour certaines valeurs et échouer pour d'autres, ce qui est le pire des cas pour trouver une erreur.
{{< /solution >}}

Ces petites erreurs peuvent avoir des conséquences graves. Le 25 février 1991, pendant la guerre du Golfe, une batterie de missiles Patriot n'a pas intercepté un missile Scud, qui a tué 28 soldats à Dhahran, en Arabie saoudite. L'horloge du système comptait le temps en dixièmes de seconde, et la valeur $\text{0,1}$ était rangée sur 24 bits, donc tronquée : à chaque dixième de seconde, l'horloge prenait un retard d'environ $\text{0,000} \, 000 \, 095$ s.

{{< question >}}
La batterie fonctionnait sans interruption depuis 100 heures. Combien de dixièmes de seconde l'horloge avait-elle comptés ? Quel était alors son retard ? Un Scud vole à environ $1 \, 676$ m/s : quelle distance parcourt-il pendant ce retard ?
{{< /question >}}

{{< solution "Réponse" >}}
100 h correspondent à $100 \times 3600 = 360 \, 000$ s, soit $3 \, 600 \, 000$ dixièmes de seconde.

**A.N.** Retard : $3 \, 600 \, 000 \times \text{0,000} \, 000 \, 095 \approx \text{0,34}$ s.

**A.N.** Distance : $1 \, 676 \times \text{0,34} \approx 570$ m.

Le système cherchait le missile à plus d'un demi-kilomètre de sa position réelle. Une erreur minuscule, répétée des millions de fois, est devenue énorme.
{{< /solution >}}

{{< qcm >}}
- question: 'Pourquoi `0.1 + 0.2 == 0.3` vaut-il `False` en Python ?'
  reponses:
    - '$\text{0,1}$ et $\text{0,2}$ ont une écriture binaire infinie : la machine range des valeurs approchées, et leur somme n''est pas le flottant le plus proche de $\text{0,3}$.'
    - 'Python fait une erreur dans les additions de flottants.'
    - 'L''opérateur `==` ne fonctionne pas avec les flottants.'
  bonne: 1
  explication: 'Le calcul est fait correctement, mais sur des valeurs déjà arrondies : on compare deux nombres réellement différents.'
- question: 'Que vaut `0.5 + 0.25 == 0.75` ?'
  reponses:
    - '`True`'
    - '`False`'
  bonne: 1
  explication: 'Ces trois nombres s''écrivent exactement en base 2 : le calcul est exact. Cela ne permet pas pour autant de tester l''égalité de flottants en général.'
- question: 'Pourquoi l''horloge du système Patriot avait-elle pris du retard ?'
  reponses:
    - 'La valeur $\text{0,1}$, rangée sur 24 bits, était tronquée, et cette petite erreur s''est répétée à chaque dixième de seconde.'
    - 'Le compteur de dixièmes de seconde avait subi un dépassement de capacité.'
    - 'Le système avait été redémarré.'
  bonne: 1
  explication: 'Une erreur d''environ $\text{0,000} \, 000 \, 095$ s, répétée des millions de fois en 100 heures, a donné un retard d''environ $\text{0,34}$ s.'
{{< /qcm >}}

## Programmer avec des flottants

{{< question >}}
On considère le programme suivant :

```python
x = 0
while x != 1:
    x = x + 0.1
```

1. Combien d'itérations l'auteur de ce programme pensait-il faire ?
1. Expliquer pourquoi la boucle ne s'arrête jamais. Ne pas l'exécuter telle quelle ; pour le vérifier, exécuter plutôt :

```python
x = 0
for i in range(10):
    x = x + 0.1
print(x, x == 1)
```
{{< /question >}}

{{< solution "Réponse" >}}
1. Il pensait faire 10 itérations : $10 \times \text{0,1} = 1$.
1. Le second programme affiche `0.9999999999999999 False`. Après 10 additions, `x` n'est pas égal à 1 à cause des erreurs d'arrondi accumulées. À l'itération suivante, `x` dépasse 1 et ne lui sera plus jamais égal : la condition `x != 1` reste vraie indéfiniment. C'est une boucle infinie.
{{< /solution >}}

Pour comparer deux flottants, on ne teste pas leur égalité. On vérifie que leur écart est très petit, par exemple inférieur à $10^{-9}$. La fonction `abs` donne la valeur absolue d'un nombre, et $10^{-9}$ s'écrit `1e-9` en Python.

{{< question >}}
Écrire la fonction `sont_proches` dont la spécification est :

```python
def sont_proches(a: float, b: float) -> bool:
    """
    Retourne True si l'écart entre a et b est strictement
    inférieur à 1e-9, False sinon.

    >>> sont_proches(0.1 + 0.2, 0.3)
    True
    >>> sont_proches(0.3, 0.31)
    False
    """
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def sont_proches(a: float, b: float) -> bool:
    return abs(a - b) < 1e-9
```
La valeur absolue rend le test indépendant de l'ordre de `a` et `b`. Erreur fréquente : écrire `a - b < 1e-9`, qui retourne `True` dès que `a` est plus petit que `b`, même de beaucoup. La bibliothèque standard propose une fonction semblable : `math.isclose`.
{{< /solution >}}

{{< question >}}
Réécrire la boucle de la question précédente pour qu'elle effectue exactement 10 itérations et que `x` prenne les valeurs $\text{0,1}$ ; $\text{0,2}$ ; … ; $1$ aussi précisément que possible. Justifier le choix.
{{< /question >}}

{{< note tip "Coup de pouce" >}}
Les entiers, eux, sont toujours exacts en Python. Quelle variable pourrait compter les itérations sans erreur ?
{{< /note >}}

{{< solution "Réponse" >}}
```python
for i in range(1, 11):
    x = i / 10
```
Le compteur `i` est un entier : il est exact, et la boucle fait exactement 10 itérations. On calcule `x` à partir de `i` à chaque tour, au lieu d'ajouter `0.1` au résultat précédent : chaque valeur de `x` ne subit qu'un seul arrondi, et les erreurs ne s'accumulent pas. Par exemple, `3 / 10` donne `0.3`, alors que trois additions de `0.1` donnent `0.30000000000000004`.
{{< /solution >}}

{{< qcm >}}
- question: 'Pourquoi la boucle `x = 0`, `while x != 1: x = x + 0.1` ne s''arrête-t-elle jamais ?'
  reponses:
    - 'Après 10 additions, `x` vaut `0.9999999999999999`, puis il dépasse 1 sans jamais lui être égal.'
    - 'Parce que `0.1` est un entier.'
    - 'Parce que la condition `x != 1` est mal écrite.'
  bonne: 1
  explication: 'Les erreurs d''arrondi s''accumulent : la condition d''arrêt `x == 1` n''est jamais remplie.'
- question: 'Quel test compare correctement deux flottants `a` et `b` ?'
  reponses:
    - '`abs(a - b) < 1e-9`'
    - '`a == b`'
    - '`a - b < 1e-9`'
  bonne: 1
  explication: 'Sans la valeur absolue, `a - b < 1e-9` est vrai dès que `a` est plus petit que `b`, même de beaucoup.'
- question: 'Pour faire prendre à `x` les valeurs $\text{0,1}$ ; $\text{0,2}$ ; … ; $1$, quelle boucle est la plus précise ?'
  reponses:
    - '`for i in range(1, 11): x = i / 10`'
    - '`for i in range(10): x = x + 0.1`, avec `x = 0` au départ'
  bonne: 1
  explication: 'Le compteur entier est exact, et chaque valeur de `x` ne subit qu''un seul arrondi : les erreurs ne s''accumulent pas.'
{{< /qcm >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- calculer la valeur décimale d'un nombre à virgule écrit en base 2 ;
- écrire un nombre comme $\text{0,25}$, $\text{0,1}$ ou $1/3$ en base 2 par la méthode des multiplications successives ;
- expliquer pourquoi certains nombres, comme $\text{0,1}$, ont une écriture binaire infinie et ne sont rangés en machine que de façon approchée ;
- expliquer pourquoi `0.1 + 0.2 == 0.3` vaut `False` ;
- éviter de tester l'égalité de deux flottants, et comparer leur écart à une petite valeur ;
- préférer un compteur entier à l'accumulation de flottants pour contrôler une boucle.
{{< /note >}}

Le Doc. 4,6 propose des exercices qui mêlent toutes les représentations étudiées dans ce chapitre.
