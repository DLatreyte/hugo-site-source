---
title: "Les arbres binaires"
subtitle: "Chapitre 9,2"
author: ""
type: ""
date: 2020-11-05T03:38:41+04:00
draft: false
toc: true
tags: ["Arbres", "Arbres binaires"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}
Le corrigé de l'activité se trouve {{< remote "ici" "https://repl.it/@dlatreyte/arbres" >}}
{{% /note %}}
## Arbres binaires

### Définition

{{% note tip %}}
- Un **arbre binaire** est un arbre de degré 2 (dont les nœuds sont au plus de degré 2).

- Les enfants d’un nœud sont lus de gauche à droite et sont appelés : *fils gauche* et *fils droit*.
{{% /note %}}

{{% note warning %}}
Pour simplifier la présentation, on va considérer que chaque nœud possède exactement deux fils mais que **ceux-ci peuvent être vides** (`None` par exemple).
{{% /note %}}

{{% note normal %}}
Les arbres binaires forment une *structure de données abstraite qui peut se définir de façon récursive*. 

Un arbre binaire est :
- Soit vide.
- Soit composé d’une racine portant une étiquette (valeur) et d’une paire d’arbres binaires, appelés sous-arbres gauche et droit.
{{% /note %}}

### Relation entre nombre de nœuds et hauteur dans le cas des arbres binaires

{{% note tip %}}
Si $N$ désigne la taille d'un arbre binaire --- c'est à dire son nombre de nœuds non vides --- et $h$ sa hauteur, alors 
$$h \leqslant N \leqslant 2^h - 1$$
{{% /note %}}

1. Dans quel cas a-t-on $N = h$ ?
{{% solution "Réponse" %}}
On a $N = h$ lorsque chaque nœud ne possède qu'un seul nœud fils. Il s'agit donc d'une structure linéaire (liste).
{{% /solution %}}

2. Dans quel cas a-t-on $N = 2^h - 1$ ?
{{% solution "Réponse" %}}
On a $N = 2^h - 1$ lorsque l'arbre binaire est parfait, c'est à dire lorsque toutes les feuilles ont la même profondeur.
{{% /solution %}}

## Spécification des arbres binaires

{{% note tip %}}
- **Créer** un nœud (type)&nbsp;: 
    - fonction&nbsp;: `creer_nœud()` $\longrightarrow$ retourne un nœud &nbsp;;
    - `fils_gauche` et `fils_droit` sont automatiquement initialisés à `None`&nbsp;;;
    - complexité&nbsp;: $O(0)$ (pas tout à fait vrai mais suffisant pour comprendre la suite).
- **Lire** dans le champ `valeur`&nbsp;:
    - fonction&nbsp;: `lire_valeur(n: Noeud[T])` $\longrightarrow$ `T`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Écrire** dans le champ `valeur`&nbsp;:
    - fonction&nbsp;: `modifier_valeur(n: Noeud[T], valeur: T)` $\longrightarrow$ `None`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Lire** dans le champ `fils_gauche`&nbsp;:
    - fonction&nbsp;: `lire_filsG(n: Noeud[T])` $\longrightarrow$ `Noeud[T]`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Écrire** dans le champ `fils_gauche`&nbsp;:
    - fonction&nbsp;: `modifier_filsG(n: Noeud[T], m: Noeud[T])` $\longrightarrow$ `None`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Lire** dans le champ `fils_droit`&nbsp;:
    - fonction&nbsp;: `lire_filsD(n: Noeud[T])` $\longrightarrow$ `Noeud[T]`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
- **Écrire** dans le champ `fils_droit`&nbsp;:
    - fonction&nbsp;: `modifier_filsD(n: Noeud[T], m: Noeud[T])` $\longrightarrow$ `None`&nbsp;;
    - complexité&nbsp;: 1 opération élémentaire.
{{% /note %}}

{{% note warning %}}
*Tout comme on a désigné les listes chaînées par leur première cellule, on va désigner les arbres par leur nœud racine.* 
{{% /note %}}

## Implémentation de la spécification en Python

Il existe de nombreuses façons de d'implémenter la structure d'arbre en Python. Dans cette partie on va utiliser une classe.

2. Écrire le code de la classe `Noeud` respectant la spécification. Les trois attributs seront nommés `valeur`, `gauche`, `droit`.

3. Écrire le code permettant de construire l'arbre :
{{< mermaid >}}
graph TD
  A("A") --> B("B")
  B --> G(None)
  B --> C("C")
  C --> H(None)
  C --> I(None)
  A --> D("D")
  D --> E(None)
  D --> F(None)
{{< /mermaid >}}

{{% solution "Réponse" %}}

```python
arbre_1 = Noeud('A',
                Noeud('B',
                        None,
                        Noeud('C')),
                Noeud('D')
                )
```

{{% /solution %}}

4. Quel arbre correspond à ce code ?
```python
Noeud('r', Noeud('a', Noeud('c', None, Noeud('h')), Noeud('d', Noeud('i'),
 Noeud('j', Noeud('m'), None))), Noeud('b', Noeud('e', Noeud('k', None, None),
  None), Noeud('f')))
``` 
{{% solution "Réponse" %}}
<img src="/terminales-nsi/chap-9/chap-9-2-1.svg" alt="" width="100%" />
<img src="/terminales-nsi/chap-9/chap-9-2-2.png" alt="" width="100%" />
{{% /note %}}

5. Écrire la spécification et le code de la fonction `est_vide` dont la spécification est&nbsp;:
```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si un arbre est vide.
    """
```

6. Écrire la spécification et le code de la fonction `ajoute_filsG` dont la spécification est&nbsp;:
```python
def ajoute_filsG(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils gauche. 
    """
```

7. Écrire la spécification et le code de la fonction `ajoute_filsD` dont la spécification est&nbsp;:
```python
def ajoute_filsD(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
``` 

8. Écrire la spécification et le code de la fonction `est_feuille` dont la spécification est&nbsp;:
```python
def est_feuille(n: Noeud) -> bool:
    """
    Teste si un noeud est une feuille.
    """
``` 

9. Écrire la spécification et le code de la fonction `degre_noeud` dont la spécification est&nbsp;:
```python
def degre_noeud(n: Noeud) -> int:
    """
    Détermine le degré du noeud passé en argument.
    """
``` 

{{% solution "Réponses aux questions précédentes" %}}

```python
from __future__ import annotations


class Noeud():
    """
    Implémentation d'un noeud.
    """

    def __init__(self: Noeud,
                 valeur: str,
                 gauche: Noeud = None,
                 droit: Noeud = None) -> None:
        self.valeur = valeur
        self.gauche = gauche
        self.droit = droit


def est_vide(n: Noeud) -> bool:
    """
    Teste si un arbre est vide.
    """
    return n is None


def ajoute_filsG(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils gauche. 
    """
    if est_vide(n.gauche):
        new_n = Noeud(valeur)
        n.gauche = new_n
    else:
        raise Exception("Noeud possède déjà un fils à gauche.")


def ajoute_filsD(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
    if est_vide(n.droit):
        new_n = Noeud(valeur)
        n.droit = new_n
    else:
        raise Exception("Noeud possède déjà un fils à droite.")


def est_feuille(n: Noeud) -> bool:
    """
    Teste si un noeud est une feuille.
    """
    return est_vide(n.gauche) and est_vide(n.droit)


def degre_noeud(n: Noeud) -> int:
    """
    Détermine le degré du noeud passé en argument.
    """
    nbre = 0
    if not est_vide(nbre.gauche):
        nbre += 1
    if not est_vide(nbre.droit):
        nbre += 1
    return nbre


if __name__ == "__main__":
    n1 = Noeud('A')
    ajoute_filsG(n1, 'B')
    ajoute_filsD(n1.gauche, 'C')
    ajoute_filsD(n1, 'D')

    print("Pour n1, D est-il une feuille : {}".format(est_feuille(n1.droit)))
    print("Pour n1, B est-il une feuille : {}".format(est_feuille(n1.gauche)))
    print("Pour n1, C est-il une feuille : {}".format(est_feuille(n1.gauche.droit)))

    print("Degré de la racine : {}".format(degre_noeud(n1)))
    print("Degré de B : {}".format(degre_noeud(n1.gauche)))
    print("Degré de D : {}".format(degre_noeud(n1.droit)))
    print("Degré de C : {}".format(degre_noeud(n1.gauche.droit)))
```

{{% /solution %}}
## Quelques algorithmes de manipulation des arbres binaires

### Algorithmes récursifs

10. Écrire la spécification et le code de la fonction `taille` dont la spécification est&nbsp;:
```python
def taille(n: Noeud) -> int:
    """
    Retourne le nombre de noeud dans l'arbre.
    """
``` 

{{% solution "Réponse" %}}

```python
def taille(n: Noeud) -> int:
    """
    Retourne le nombre de noeud dans l'arbre depuis le noeud n
    """
    if est_vide(n):
        return 0
    else:
        return 1 + taille(n.gauche) + taille(n.droit)
``` 

{{% /solution %}}

11. Écrire la spécification et le code de la fonction `profondeur` dont la spécification est&nbsp;:
```python
def profondeur(n: Noeud) -> int:
    """
    Retourne la profondeur de l'arbre. 
    """
``` 

{{% solution "Réponse" %}}

```python
def profondeur(n: Noeud) -> int:
    """
    Retourne la profondeur de l'arbre 
    """
    if est_vide(n):
        return 0
    else:
        return 1 + max(profondeur(n.gauche), profondeur(n.droit))
```

{{% /solution %}}

12. Écrire la spécification et le code de la fonction `nbre_feuilles` dont la spécification est&nbsp;:
```python
def nbre_feuilles(n: Noeud) -> int:
    """
    Détermine le nombre de feuilles dans l'arbre. 
    """
``` 

{{% solution "Réponse" %}}

```python 
def nbre_feuilles(n: Noeud) -> int:
    """
    Détermine le nombre de feuilles dans l'arbre. 
    """
    if est_vide(n):  # Cas des nœuds de degré 1 (ou de l'arbre vide)
        return 0
    elif est_feuille(n):
        return 1
    else:
        return 0 + nbre_feuilles(n.gauche) + nbre_feuilles(n.droit)
``` 


{{% /solution %}}

13. Quelles sont les complexités des algorithmes implémentés dans cette section ?
{{% solution "Réponse" %}}
Les algorithmes parcourent une fois chaque nœud de l'arbre. La complexité est donc proportionnelle au nombre de nœuds.
{{% /solution %}}

#### Parcours en profondeur d'un arbre

Les fonction écrites jusqu'à présent parcourent en profondeur tous les nœuds des arbres sans que l'ordre dans lequel ce parcourt est effectué ait la moindre importance.

{{% note tip %}}

Si on souhaite donner un affichage de l'arbre, la façon dont on le parcourt prend alors une grande importance. On peut :
- Parcourir le sous-arbre gauche, afficher la valeur du nœud puis enfin parcourir le sous-arbre droit. On parle d'un **parcours infixe**.
- Afficher la valeur de chaque nœud avant de parcourir les sous-arbres. On parle d'un **parcours préfixe**.
- Parcourir les sous-arbres puis afficher les valeurs. On parle d'un **parcours suffixe**.

{{% /note %}}

14. Écrire les spécifications et le code des fonctions `affiche_infixe`, `affiche_prefixe` et `affiche_suffixe` dont les spécifications sont :
```python
def affiche_infixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    """
``` 

```python
def affiche_prefixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    """
``` 

```python
def affiche_suffixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    """
``` 


### Algorithmes itératifs

15. Reprendre les questions précédentes en utilisant des algorithmes itératifs.

## Parcours d'un arbre à l'aide d'une file ou d'une pile

### Parcours en largeur d'un arbre

16. Décrire le fonctionnement de l'algorithme suivant et montrer qu'il réalise un parcours en largeur d'un arbre.
```shell
Fonction parcours_largeur(noeud racine):
    File f = newFile()
    enfiler(f, racine)
    Noeud n = newNoeud()
    TantQue non est_vide(f):
        n = f.valeur
        print(f.defiler())
        Si non est_vide(n.filsG):
            enfiler(n.filsG)
        FinSi
        Si non est_vide(n.filsD):
            enfiler(n.filsD)
        FinSi
    FinTantQue
FinFonction
```

17. Implémenter en Python l'algorithme précédent.


### Parcours en profondeur d'un arbre

18. Décrire le fonctionnement de l'algorithme suivant et montrer qu'il réalise un parcours en profondeur d'un arbre.   
De quel type de parcours en profondeur s'agit-il ?

```shell
Fonction parcours_profondeur(noeud racine):
    Pile p = newPile()
    empiler(p, racine)
    Noeud n = newNoeud()
    TantQue non est_vide(p):
        n = p.valeur
        print(p.depiler())
        Si non est_vide(n.filsG):
            empiler(n.filsG)
        FinSi
        Si non est_vide(n.filsD):
            empiler(n.filsD)
        FinSi
    FinTantQue
FinFonction
```

19. Implémenter en Python l'algorithme précédent.

## À retenir 

{{% note tip %}}
Un **arbre binaire** est un ensemble fini de nœuds, qui est soit **vide**, soit structuré à partir d'un nœud particulier, appelé **racine** de l'arbre, et de deux sous-ensembles de nœuds formant récursivement un **sous-arbre gauche** et un **sous-arbre droit**.   
Un arbre peut-être implémenté en Python avec un objet par nœud, d'une **classe** qui possède trois attributs : la valeur (ou étiquette) du nœud, le sous-arbre gauche et le sous-arbre droit. La valeur `None` est utilisée pour représenter l'arbre vide.
{{% /note %}}




