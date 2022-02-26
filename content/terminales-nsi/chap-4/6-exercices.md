---
title: "Exercices de programmation objet"
subtitle: "Chapitre 4,6"
author: ""
type: ""
date: 2021-01-13T19:12:34+04:00
draft: false
toc: true
tags: ["Objet", "Classe", "Attribut", "Méthode", "Instance", "Encapsulation"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note warning %}}
Chaque méthode définie devra être accompagnée de sa spécification.
{{% /note %}}

## Manipulation de points

On considère la classe nommée `Point` ayant les attributs suivants :
- `__abs` : attribut privé de type `float` pour représenter l'abscisse du point ;
- `__ord` : attribut privé de type `float` pour représenter l'ordonnée du point.

1. Définir la class `Point` et le constructeur `__init__` permettant d'initialiser les deux attributs.

{{% note normal %}}

L'**encapsulation** est un concept fondamental de la conception objet. L'idée est de *ne pas laisser accessibles les attributs depuis l'extérieur de la classe/objet* ; les attributs sont alors dits **privés** (ou **protégés** si l'accès est nécessaire dans une sous-classe).

En pratique
:
```python
p1 = Point()
p1.__abs = 1     # Interdit
p1.set_abs = 1   # Bonne pratique
```

En Python, par convention, le nom des attributs privés commence par `__`.

L'*accès et la modification* des attributs nécessitent alors la définition de méthodes appellées **getters** et **setters**.\
Les noms de ces méthodes sont, par exemple pour l'attribut `__abs`, `get_abs` et `set_abs`.
{{% /note %}}

2. Définir les getters et les setters pour les deux attributs.\
Modifier la méthode `__init__` de façon à ce qu'elle utilise les setters.

3. Définir la méthode `__str__` qui retourne la représentation mathématique d'un point sous forme d'une chaîne de caractères : `"(abs, ord)"`.

4. Définir la méthode `calcul_distance` qui calcule la distance du point courant à un point passé en argument.\
La signature de la fonction est `calcul_distance(self: Point, p: Point) -> float`.

{{% note normal %}}
On rappelle que la distance entre deux points $A(x\_1, y\_1)$ et $B(x\_2, y\_2)$ est égale à : $\sqrt{(x\_2 - x\_1)^2 + (y\_2 - y\_1)^2 }$.
{{% /note %}}

5. Définir la méthode `calcul_milieu` qui retourne un objet situé à égale distance du point courant et d'un point passé en argument.\
La signature de la fonction est `calcul_milieu(self: Point, p: Point) -> Point`.

{{% note normal %}}
On rappelle que la point situé à égale distance de deux points $A(x\_1, y\_1)$ et $B(x\_2, y\_2)$ a pour coordonnées $x\_M = \dfrac{x\_1 + x\_2}{2}$ et $y\_M = \dfrac{y\_1 + y\_2}{2}$.
{{% /note %}}

On considère maintenant la classe nommée `TroisPoints` ayant les attributs suivants :
- `__premier` : attribut privé de type `Point` ;
- `__deuxieme` : attribut privé de type `Point` ;
- `__troisieme` : attribut privé de type `Point` ;

6. Définir la class `TroisPoints` et le constructeur `__init__` permettant d'initialiser les trois attributs.

7. Définir les getters et les setters pour les trois attributs.\
Modifier la méthode `__init__` de façon à ce qu'elle utilise les setters.

8. Définir la méthode `sont_alignes` qui retourne `True` si les trois points sont alignés, `False` sinon.\
La signature de la fonction est `sont_alignes(self) -> True`.

{{% note normal %}}
On rappelle que trois points $A$, $B$ et $C$ sont alignés si $AB=AC+BC$, $AC=AB+BC$ ou $BC=AC+AB$ ($AB$, $AC$ et $BC$ sont des distances).
{{% /note %}}

9. Définir la méthode `est_isocele` qui retourne `True` si les trois points forment un triangle isocèle et `False` sinon.

{{% note normal %}}
On rappelle qu'un triangle est isocèle si$AB=AC$ ou $AB=BC$ ou $AC=BC$ ($AB$, $AC$ et $BC$ sont des distances).
{{% /note %}}

10. **(Facultatif car HP)** Implémenter une version statique (méthodes décorées par le décorateur `@staticmethod`) des deux méthodes `calcul_distance` et `calcul_milieu`.

{{% note normal %}}
{{< remote "Pour découvrir ce que sont les méthodes de classe, les méthodes statiques" "https://www.geeksforgeeks.org/class-method-vs-static-method-python/" >}}
{{% /note %}}

11. Tester tous les objets et méthodes depuis la fonction `main` du programme.

## Carnet d'adresses

On considère les deux classes `Personne` et `Adresse`.

Les attributs de la classe `Adresse` sont :

- `__rue` : un attribut privé de type chaîne de caractères.
- `__ville` : un attribut privé de type chaîne de caractères.
- `__code_postal` : un attribut privé de type chaîne de caractères.

Les attributs de la classe `Personne` sont :

- `__nom` : un attribut privé de type chaîne de caractères.
- `__sexe` : un attribut privé de type chaîne de caractères (cet attribut aura comme valeur soit
`’M’` soit `’F’`).
- `__adresses` : un attribut privé de type tableau d’objet de la classe `Adresse`.

1. Définir les deux classes `Adresse` et `Personne` dans deux fichiers différents. Ne pas oublier de
définir les getters/setters et les constructeurs.

2. Définir une troisième classe `ListePersonnes` ayant un seul attribut `personnes` : un tableau
d’objets `Personne`.\
Définir les getters/setters et le constructeur de cette classe. La signature de la fonction `set_personnes` est `set_personnes(self, p: Personne) -> None`.

3. Définir la méthode `recherche_par_nom`, de signature `recherche_par_nom(n: str) -> Personne`, qui permet de chercher dans le tableau `personnes` si l’attribut `__nom` d’un objet de type `Personne` est égal à la valeur du paramètre `n`. Si c’est le cas, la méthode retourne le premier objet correspondant, sinon `None`.

4. Définir la méthode `test_code_postal`, de signature `test_code_postal(cp: str) -> bool` qui permet de vérifier dans le tableau `personnes` si un objet possède au moins une adresse dont le code postal égal au paramètre `cp`. Si c’est le cas, elle retourne `True`, sinon `False`.

5. Définir la méthode `compte_personne_ville`, de signature `compte_personne_ville(ville: str) -> int`, qui permet de calculer le nombre d’objets dans le tableau `personnes` ayant une adresse dans la ville passée en paramètre.

6. Définir la méthode `edit_personne_nom`, de signature `edit_personne_nom(ancien_nom: str, nouveau_nom: str) -> None`, qui remplace les noms
de personnes ayant un nom égal à la valeur `ancien_nom` par `nouveau_nom`.

7. Définir la méthode `edit_personne_ville`, de signature `edit_personne_ville(nom: str, nouvelle_ville: str) -> None`, qui remplace les villes
de personnes ayant un nom égal à la valeur du paramètre `nom` par `nouvelle_ville`.

8. Dans la fonction `main`, tester toutes les méthodes réalisées dans les questions précédentes.