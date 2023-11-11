---
title: "Les arbres binaires"
subtitle: ""
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
mathjax: true
---

## Arbres binaires

### Définition

{{% note tip %}}

Un **arbre binaire** est une **structure de données abstraite** formée d'un ensemble de nœuds organisés hiérarchiquement selon la définition par récurrence suivante :

Un arbre binaire est :

- soit un arbre vide, noté $E$, ne contenant aucun nœud ;
- soit un nœud, appelé **racine**, relié à exactement deux arbres binaires $g$ et $d$, respectivement appelés **sous-arbres gauche** et **sous-arbre droit**.

On note $T(r,g,d)$ l'arbre non vide dont la racine $r$ (on peut aussi indiquer l'étiquette de cette racine).

{{% /note %}}

### Vocabulaire et remarques

- Un nœud dont les **deux sous-arbres sont vides** est appelé une **feuille**.
- Un nœud qui n'est pas une feuille est un **nœud interne**.
- Un arbre binaire est dit **parfait** si **toutes les feuilles sont à la même profondeur**.
- La racine d'un arbre $T$ est le seul nœud de $T$ sans parent.

### Propriétés

{{% note normal %}}

#### Position des sous-arbres

- La position des sous-arbres gauche et droite est fondamentale : $$T(r,g,d) \neq T(r,d,g)$$

{{% /note %}}

{{% note normal %}}

#### Taille d'un arbre

- La taille d'un arbre est égale **au nombre de nœuds qu'il comporte**.
- Le **nombre de nœuds** d'un arbre binaire $T$, noté $n(T)$, se calcule récursivement :
  - $n(E)=0$
  - $n(T)=1+n(g)+n(d)$

{{% /note %}}

{{% note normal %}}

#### Profondeur d'un nœud

- La profondeur d'un nœud $n$, notée $h(n)$, est sa **distance à la racine**.
- La profondeur d'un nœud $n$, notée $h(n)$, est définie récursivement par :
  - $h(\text{racine})=0$
  - $h(n)=1+h(\text{parent de }n)$
- **La profondeur d'un nœud dans un arbre est donc le nombre d'arrêtes qu'il faut parcourir, depuis la racine, pour parvenir au nœud.**  

{{% /note %}}

{{% note warning %}}

La définition de la profondeur d'un nœud peut varier ! Il est impératif de vérifier celle choisie avant tout travail.

{{% /note %}}

{{% note normal %}}

#### Hauteur d'un arbre

- La hauteur d'un arbre est la profondeur du nœud le plus éloigné de la racine.  
La hauteur d'un arbre est aussi sa profondeur.
- La hauteur d'un arbre binaire $T$, notée $h(T)$ est définie récursivement par :
  - $h(E)=-1$ si l'arbre est vide ;
  - $h(T)=1+\mathrm{max}(h(g), h(d))$

{{% /note %}}

#### Remarque

On peut aussi définir la hauteur d'un nœud : *la **hauteur** d'un nœud est la distance entre ce nœud et la feuille la plus profonde ayant une relation de descendance avec ce nœud*.  

{{% note warning %}}

La définition de la hauteur d'un arbre peut varier ! Il est impératif de vérifier celle choisie avant tout travail.

{{% /note %}}

{{% note normal %}}

#### Relation entre le nombre de nœuds $n$ et la hauteur d'un arbre

- Soit $T$ un arbre binaire, $n$ son nombre de nœuds et $h$ sa hauteur. Ces grandeurs sont liées par les relations suivantes :
- $h + 1 \leq n \leq 2^{h+1} - 1$

- le nombre de sous-arbres vides de $T$ est $n+1$.

{{% /note %}}

1. Dans quel cas a-t-on $N = h+1$ ?
{{% solution "Réponse" %}}
On a $N = h+1$ lorsque chaque nœud ne possède qu'un seul nœud fils. Il s'agit donc d'une structure linéaire (liste).
{{% /solution %}}

2. Dans quel cas a-t-on $N = 2^{h+1} - 1$ ?
{{% solution "Réponse" %}}
On a $N = 2^{h+1} - 1$ lorsque l'arbre binaire est parfait, c'est à dire lorsque toutes les feuilles ont la même profondeur.
{{% /solution %}}

## Spécification d'un arbre binaire

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

## Implémentation de la spécification en Python à l'aide d'une classe

Il existe de nombreuses façons de d'implémenter la structure d'arbre en Python. Dans cette partie on va utiliser une classe.

{{% note warning %}}

Le paradigme de programmation utilisé ci-dessous est le **paradigme impératif** : *on crée dans un premier temps une structure élémentaire qui ne sert qu'à stocker les différentes valeurs et on définit ensuite des fonctions qui manipulent cette structure.*

La structure utilisée peut être :

- Une classe qui définit trois attributs `valeur`, `gauche` et `droit` et **aucune méthode** ;
- Une liste Python de trois éléments ;
- Un dictionnaire comportant trois clés : `valeur`, `gauche` et `droit`.

*On peut même imaginer utiliser un tableau ou une liste chaînée !*

On ne créera pas de structure « arbre binaire » (accompagnée de méthodes) dans ce document.

{{% /note %}}

2. Écrire le code de la classe `Noeud` respectant la spécification. Les trois attributs seront nommés `valeur`, `gauche`, `droit`.

{{% solution "Réponse" %}}

```python
from __future__ import annotations

class Noeud:
    """
    Structure de stockage pour créer des arbres binaires.
    """

    def __init__(self: Noeud, val: str, g: Noeud = None, d: Noeud = None) -> None:
        """ Initialisation de l'objet. """
        self.valeur = val
        self.gauche = g
        self.droit = d
```

{{% /solution %}}

3. Écrire le code permettant de construire l'arbre :
{{< mermaid >}}
graph TD
  A("A") --- B("B")
  B --- G(None)
  B --- C("C")
  C --- H(None)
  C --- I(None)
  A --- D("D")
  D --- E(None)
  D --- F(None)
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

ou

```python
abr1 = Noeud('A')
abr1.gauche = Noeud('B')
abr1.droit = Noeud('D')
abr1.gauche.droit = Noeud('C')
```

{{% /solution %}}

4. Quel arbre correspond à ce code ?

```python
abr = Noeud('r', Noeud('a', Noeud('c', None, Noeud('h')), Noeud('d', Noeud('i'),
 Noeud('j', Noeud('m'), None))), Noeud('b', Noeud('e', Noeud('k', None, None),
  None), Noeud('f')))
```

{{% solution "Réponse" %}}

<img src="/terminales-nsi/chap-9/chap-9-2-1.svg" alt="" width="100%" />

<br />

<img src="/terminales-nsi/chap-9/chap-9-2-2.png" alt="" width="100%" />
{{% /note %}}

Écrire le code différemment en créant les nœuds les uns après les autres.

{{% solution "Réponse" %}}

```python
abr = Noeud('r')
abr.gauche = Noeud('a')
abr.droit = Noeud('b')
abr.gauche.gauche = Noeud('c')
abr.gauche.droit = Noeud('d')
abr.gauche.gauche.droit = Noeud('h')
abr.gauche.droit.gauche = Noeud('i')
abr.gauche.droit.droit = Noeud('j')
abr.gauche.droit.droit.gauche = Noeud('m')
abr.droit.gauche = Noeud('e')
abr.droit.gauche.gauche = Noeud('k')
abr.droit.droit = Noeud('f')
```

{{% /solution %}}

5. Écrire le code de la fonction `est_vide` dont la spécification est&nbsp;:

```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si un arbre est vide.
    """
```

{{% solution "Réponse" %}}

```python
def est_vide(n: Noeud) -> bool:
    """
    Teste si un arbre est vide.
    """
    return n == None
```

{{% /solution %}}

6. Écrire le code de la fonction `ajoute_filsG` dont la spécification est&nbsp;:

```python
def ajoute_filsG(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils gauche. 
    """
```

{{% solution "Réponse" %}}

```python
def ajoute_filsG(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils gauche. 
    """
    if est_vide(n.gauche):
        n.gauche = Noeud(valeur)
    else:
        raise Exception("Le nœud possède déjà un fils gauche !")
```

{{% /solution %}}

7. Écrire le code de la fonction `ajoute_filsD` dont la spécification est&nbsp;:

```python
def ajoute_filsD(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
```

{{% solution "Réponse" %}}

```python
def ajoute_filsD(n: Noeud, valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
    if est_vide(n.droit):
        n.droit = Noeud(valeur)
    else:
        raise Exception("Le nœud possède déjà un fils droit !")
```

{{% /solution %}}

8. Écrire le code de la fonction `est_feuille` dont la spécification est&nbsp;:

```python
def est_feuille(n: Noeud) -> bool:
    """
    Teste si un noeud est une feuille.
    """
```

{{% solution "Réponse" %}}

```python
def est_feuille(n: Noeud) -> bool:
    """
    Teste si un noeud est une feuille.
    """
    return est_vide(n.gauche) and est_vide(n.droit)
```

{{% /solution %}}

9. Écrire le code de la fonction `degre_noeud` dont la spécification est&nbsp;:

```python
def degre_noeud(n: Noeud) -> int:
    """
    Détermine le degré du noeud passé en argument.
    """
```

## Quelques algorithmes de manipulation des arbres binaires

Tous les algorithmes qui suivent sont récursifs.

10. Écrire le code de la fonction `taille` dont la spécification est&nbsp;:

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
    Retourne le nombre de noeud dans l'arbre.
    """
    if est_vide(n):
        # Cas de base : un arbre vide ne contient aucun noeud.
        return 0
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        taille_gauche = taille(n.gauche)
        taille_droit = taille(n.droit)

        # Calcul de la taille
        return 1 + taille_gauche + taille_droit
```

{{% /solution %}}

11. Écrire le code de la fonction `profondeur` dont la spécification est&nbsp;:

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
    Retourne la profondeur de l'arbre. 
    """
    if est_vide(n):
        # Cas de base : si le nœud est vide, il n'est pas dans l'arbre.
        return -1
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        arbre_gauche = profondeur(n.gauche)
        arbre_droit = profondeur(n.droit)

        # Détermine la profondeur
        return 1 + max(arbre_gauche, arbre_droit)
```

{{% /solution %}}

12. Écrire le code de la fonction `nbre_feuilles` dont la spécification est&nbsp;:

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
    if est_vide(n):
        # Cas de base : un arbre vide ne contient aucune feuille
        return 0
    elif est_feuille(n):
        # Cas de base : on ajoute 1 au total dès qu'on rencontre une feuille
        return 1
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        nbre_feuilles_gauche = nbre_feuilles(n.gauche)
        nbre_feuilles_droit = nbre_feuilles(n.droit)

        # Calcul du nombre de feuilles
        return nbre_feuilles_gauche + nbre_feuilles_droit
```

{{% /solution %}}

13. Écrire le code de la fonction `profondeur_noeud` dont la spécification est&nbsp;:

```python
def profondeur_noeud(n: Noeud, val: str, prof: int = 0) -> int:
    """
    Détermine la profondeur du noeud de valeur val.
    """
```

{{% solution "Réponse" %}}

```python
def profondeur_noeud(n: Noeud, val: str, prof: int = 0) -> int:
    """
    Détermine la profondeur du noeud de valeur val.
    Retourne -1 si le noeud n'est pas dans l'arbre.

    prof est la profondeur.
    """
    if est_vide(n):
        # Cas de base : si le nœud est vide, il n'est pas dans l'arbre.
        return -1
    elif n.valeur == val:
        # On a trouvé le noeud
        return prof
    else:
        # Recherche récursive dans les sous-arbres gauche et droit.
        # Incrémente la profondeur
        prof_gauche = profondeur_noeud(n.gauche, val, prof + 1)
        prof_droite = profondeur_noeud(n.droit, val, prof + 1)

        # Valeur retournée
        return max(prof_gauche, prof_droite)
```

#### Exemple : recherche de la profondeur du nœud de valeur 3

Les nœuds passés en argument sont repérés par la notation 1n, 2n, ...

```shell
p(1n, 3, 0)
    p(2n, 3, 1)           -> -1
        p(4n, 3, 2)       -> -1
            p(None, 3, 3) -> -1
            p(None, 3, 3) -> -1
        p(5n, 3, 2)       -> -1
            p(None, 3, 3) -> -1
            p(None, 3, 3) -> -1
    p(3n, 3, 1)           -> 1 
```

{{% /solution %}}

14. Écrire le code de la fonction `remplace` dont la spécification est&nbsp;:

```python
def remplace(n: Noeud, val_ini: str, val_fin: str) -> None:
    """
    Cherche tous les noeuds de valeur val_ini et remplace ces
    dernières par val_fin.
    """
```

{{% solution "Réponse" %}}

```python
def remplace(n: Noeud, val_ini: str, val_fin: str) -> None:
    """
    Cherche tous les noeuds de valeur val_ini et remplace ces
    dernières par val_fin.
    """
    if est_vide(n):
        return None
    elif n.valeur == val_ini:
        n.valeur = val_fin
    else:
        remplace(n.gauche, val_ini, val_fin)
        remplace(n.droit, val_ini, val_fin)
```

{{% /solution %}}

15. Écrire le code de la fonction `ajoute` dont la spécification est&nbsp;:

```python
def ajoute(n: Noeud, parent: str, enfant: str, gauche: bool) -> None:
    """
    Ajoute un noeud de valeur enfant comme enfant du noeud de valeur
    parent.
    Le noeud enfant est placé par défaut à gauche.

    HYPOTHÈSE : Le noeud de valeur parent existe.
    """
```

{{% solution "Réponse" %}}

```python
def ajoute(n: Noeud, parent: str, enfant: str, gauche: bool) -> None:
    """
    Ajoute un noeud de valeur enfant comme enfant du noeud de valeur
    parent.
    Le noeud enfant est placé par défaut à gauche.

    HYPOTHÈSE : Le noeud de valeur parent existe.
    """
    if est_vide(n):
        return None
    elif n.valeur == parent:
        if gauche and not est_vide(n.gauche):
            raise Exception("Le noeud enfant gauche existe déjà !")
        if not gauche and not est_vide(n.droit):
            raise Exception("Le noeud enfant droit existe déjà !")
        if gauche:
            n.gauche = Noeud(enfant)
        else:
            n.droit = Noeud(enfant)
    else:
        ajoute(n.gauche, parent, enfant, gauche)
        ajoute(n.droit, parent, enfant, gauche)
```

{{% /solution %}}

16. Écrire le code de la fonction `supprime` dont la spécification est&nbsp;:

```python
def supprime(n: Noeud, val: str) -> None:
    """
    Supprime le noeud de valeur val ainsi que tous ses descendants.
    """
```

{{% solution "Réponse" %}}

```python
def supprime(n: Noeud, val: str) -> None:
    """
    Supprime le noeud de valeur val ainsi que tous ses descendants.
    """
    if est_vide(n):
        return None
    elif est_feuille(n):
        return None
    elif n.gauche.valeur == val:
        n.gauche = None
    elif n.droit.valeur == val:
        n.droit = None
    else:
        supprime(n.gauche, val)
        supprime(n.droit, val)
```

{{% /solution %}}

17. Quelles sont les complexités des algorithmes implémentés dans cette section ?
{{% solution "Réponse" %}}
Les algorithmes parcourent une fois chaque nœud de l'arbre. La complexité est donc proportionnelle au nombre de nœuds.
{{% /solution %}}

#### Parcours en profondeur d'un arbre

Les fonction écrites jusqu'à présent parcourent en profondeur tous les nœuds des arbres sans que l'ordre dans lequel ce parcourt est effectué ait la moindre importance.

{{% note tip %}}

Si on souhaite donner un affichage de l'arbre, la façon dont on le parcourt prend alors une grande importance. On peut :

- Parcourir le sous-arbre gauche, afficher la valeur du nœud racine puis enfin parcourir le sous-arbre droit. On parle d'un **parcours infixe**.
- Afficher la valeur du nœud racine avant de parcourir le sous-arbre gauche puis le sous-arbre droit. On parle d'un **parcours préfixe**.
- Parcourir le sous-arbre gauche, le sous-arbre droit puis afficher les valeurs. On parle d'un **parcours suffixe**.

{{% /note %}}

18. Pour l'arbre ci-dessous, donner les parcours préfixe, infixe et suffixe.
{{% mermaid %}}
graph TD
    0(0) --- 1(1)
    0 --- 8(8)
    1 --- 2(2)
    2 --- 3(3)
    1 --- 4(4)
    4 --- 5(5)
    4 --- 6(6)
    6 --- 7(7)
    8 --- 9(9)
    8 --- 13(13)
    9 --- 10(10)
    10 --- 11(11)
    10 --- 12(12)
    13 --- 14(14)
    13 --- 15(15)
{{% /mermaid %}}
{{% solution "Réponses" %}}

- Préfixe : 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15
- Infixe : 3, 2, 1, 5, 4, 6, 7, 0, 9, 11, 10, 12, 8, 14, 13, 15
- Suffixe : 3, 2, 5, 7, 6, 4, 1, 11, 12, 10, 9, 14, 15, 13, 8, 0

{{% /solution %}}

19. Écrire le code des fonctions `parcours_infixe`, `parcours_prefixe` et `parcours_suffixe` dont les spécifications sont :

```python
def parcours_infixe(n: Noeud) -> str:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
```

{{% solution "Réponse" %}}

```python
def parcours_infixe(n: Noeud) -> str:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
    if est_vide(n):
        return ""
    else:
        chaine = parcours_infixe(n.gauche)
        chaine += str(n.valeur)
        chaine += parcours_infixe(n.droit)
        return chaine
```

{{% /solution %}}

```python
def parcours_prefixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
```

{{% solution "Réponse" %}}

```python
def parcours_prefixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
    if est_vide(n):
        return ""
    else:
        chaine = str(n.valeur)
        chaine += parcours_prefixe(n.gauche)
        chaine += parcours_prefixe(n.droit)
        return chaine
```

{{% /solution %}}

```python
def parcours_suffixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
```

{{% solution "Réponse" %}}

```python
def parcours_suffixe(n: Noeud) -> None:
    """
    Parcourt le sous-arbre gauche, affiche la valeur du nœud puis parcourt le sous-arbre droit.
    Retourne le parcours sous forme d'une chaîne de caractères.
    """
    if est_vide(n):
        return ""
    else:
        chaine = parcours_suffixe(n.gauche)
        chaine += parcours_suffixe(n.droit)
        chaine += str(n.valeur)
        return chaine
```

{{% /solution %}}

## Algorithmes itératifs --- Parcours d'un arbre à l'aide d'une file ou d'une pile

### Parcours en largeur d'un arbre

20. Décrire le fonctionnement de l'algorithme suivant et montrer qu'il réalise un parcours en largeur d'un arbre.

```shell
Fonction parcours_largeur(racine: Noeud):
    File f = File()
    f.enfiler(racine)
    TantQue non f.est_vide():
        n = f.defiler()
        print(n.valeur)
        Si non est_vide(n.filsG):
            f.enfiler(n.filsG)
        FinSi
        Si non est_vide(n.filsD):
            f.enfiler(n.filsD)
        FinSi
    FinTantQue
FinFonction
```

21. Implémenter en Python cet algorithme.

{{% solution "Réponse" %}}

```python
def parcours_largeur(n: Noeud) -> str:
    """ Réalise le parcours en largeur d'un arbre binaire. """
    message = ""

    f = File()
    f.enfiler(n)
    while not f.est_vide():
        n = f.defiler()
        message += str(n.valeur)
        if not est_vide(n.gauche):
            f.enfiler(n.gauche)
        if not est_vide(n.droit):
            f.enfiler(n.droit)

    return message
```

{{% /solution %}}

### Parcours en profondeur d'un arbre

22. Décrire le fonctionnement de l'algorithme suivant et montrer qu'il réalise un parcours en profondeur d'un arbre.  
De quel type de parcours en profondeur s'agit-il ?

```shell
Fonction parcours_profondeur(racine: Noeud):
    Pile p = Pile()
    p.empiler(racine)
    TantQue non p.est_vide():
        n = p.depiler()
        print(n)
        Si non est_vide(n.filsG):
            p.empiler(n.filsG)
        FinSi
        Si non est_vide(n.filsD):
            p.empiler(n.filsD)
        FinSi
    FinTantQue
FinFonction
```

{{% solution "Réponse" %}}

L'algorithme semble realiser un parcours préfixe mais en explorant d'abord le sous-arbre droit au lieu d'explorer le sous-arbre gauche.

{{% /solution %}}

Modifier l'algorithme de telle sorte qu'il réalise le parcours préfixe.

{{% solution "Réponse" %}}

```shell
Fonction parcours_profondeur(racine: Noeud):
    Pile p = Pile()
    p.empiler(racine)
    TantQue non p.est_vide():
        n = p.depiler()
        print(n)
        Si non est_vide(n.filsD):
            p.empiler(n.filsD)
        FinSi
        Si non est_vide(n.filsG):
            p.empiler(n.filsG)
        FinSi
    FinTantQue
FinFonction
```

{{% /solution %}}

23. Implémenter en Python cet algorithme.

{{% solution "Réponse" %}}

```python
def parcours_profondeur(n: Noeud) -> str:
    """
    Réalise un parcours en profondeur à l'aide d'une pile.
    """
    message = ""

    p = Pile()
    p.empiler(n)
    while not p.est_vide():
        n = p.depiler()
        message += str(n.valeur)
        if not est_vide(n.gauche):
            p.empiler(n.gauche)
        if not est_vide(n.droit):
            p.empiler(n.droit)
    return message
```

{{% /solution %}}

## Implémentation de la spécification en Python à l’aide d’une liste Python

24. Reprendre toutes les fonctions de ce document en n'utilisant pas la classe `Noeud` mais une liste à trois éléments. Le premier est la « valeur » du noeud, le second l'adresse du fils gauche, le troisième l'adresse du fils droit.

{{% solution "Réponse" %}}

```python
"""
Implémentation d'un arbre binaire en utilisant le 
paradigme impératif et des listes.

Structure d'un noeud : [valeur, gauche, droit]
"""


def est_vide(n: list[str, list, list]) -> bool:
    """
    Teste si un arbre est vide.
    """
    return n is None


def ajoute_filsG(n: list[str, list, list], valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils gauche. 
    """
    if est_vide(n[1]):
        n[1] = [valeur, None, None]
    else:
        raise Exception("Le nœud possède déjà un fils gauche !")


def ajoute_filsD(n: list[str, list, list], valeur: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
    if est_vide(n[2]):
        n[2] = [valeur, None, None]
    else:
        raise Exception("Le nœud possède déjà un fils droit !")


def est_feuille(n: list[str, list, list]) -> bool:
    """
    Teste si un noeud est une feuille.
    """
    return est_vide(n[1]) and est_vide(n[2])


def degre_noeud(n: list[str, list, list]) -> int:
    """
    Détermine le degré du noeud passé en argument.
    """
    if est_vide(n):
        raise Exception("Le nœud est vide !")

    nbre = 0
    if not est_vide(n[1]):
        nbre += 1
    if not est_vide(n[2]):
        nbre += 1

    return nbre


def taille(n: list[str, list, list]) -> int:
    """
    Retourne le nombre de noeud dans l'arbre.
    """
    if est_vide(n):
        return 0
    else:
        return 1 + taille(n[1]) + taille(n[2])


def profondeur(n: list[str, list, list]) -> int:
    """
    Retourne la profondeur de l'arbre. 
    """
    if est_vide(n):
        return -1
    else:
        return 1 + max(profondeur(n[1]), profondeur(n[2]))


def nbre_feuilles(n: list[str, list, list]) -> int:
    """
    Détermine le nombre de feuilles dans l'arbre. 
    """
    if est_vide(n):
        return 0
    elif est_feuille(n):
        return 1
    else:
        return nbre_feuilles(n[1]) + nbre_feuilles(n[2])


def parcours_pref(n: list[str, list, list]) -> str:
    """ Parcours en profondeur préfixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        chaine = str(n[0])
        chaine += parcours_pref(n[1])
        chaine += parcours_pref(n[2])
        return chaine


def parcours_inf(n: list[str, list, list]) -> str:
    """ Parcours en profondeur infixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        chaine = parcours_inf(n[1])
        chaine += str(n[0])
        chaine += parcours_inf(n[2])
        return chaine


def parcours_suf(n: list[str, list, list]) -> str:
    """ Parcours en profondeur infixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        chaine = parcours_suf(n[1])
        chaine += parcours_suf(n[2])
        chaine += str(n[0])
        return chaine


if __name__ == "__main__":
    arb = ['A', ['B',
                 ['C', None, None],
                 ['D', None, None]
                 ],
           ['E',
            ['F', None, None],
            ['G',
             ['H',
              None,
              None
              ],
             None
             ]
            ]
           ]
    print(est_vide(arb))
    print(f"Taille de l'arbre : {taille(arb)}")
    print(f"Profondeur (hauteur) de l'arbre : {profondeur(arb)}")
    print(f"Préfixe : {parcours_pref(arb)}")
    print(f"Infixe : {parcours_inf(arb)}")
    print(f"Suffixe : {parcours_suf(arb)}")
```

{{% /solution %}}

## Implémentation de la spécification en Python à l’aide d’un dictionnaire

25. Reprendre toutes les fonctions de ce document en n'utilisant pas la classe `Noeud` mais un dictionnaire à trois clés : `valeur`, `gauche` et `droit` pour stocker la « valeur » du noeud, l'adresse du fils gauche et l'adresse du fils droit.

{{% solution "Réponse" %}}

```python
"""
Implémentation du type arbre binaire en utilisant
le paradigme impératif et des dictionnaires.
"""


def est_vide(n: dict[str, dict, dict]) -> bool:
    """
    Teste si un arbre est vide.
    """
    return n == None


def ajoute_filsG(n: dict[str, dict, dict], val: str) -> None:
    """
    Ajoute un noeud d'étiquette val comme fils gauche. 
    """
    if est_vide(n['gauche']):
        n['gauche'] = {'valeur': val, 'gauche': None, 'droit': None}
    else:
        raise Exception("Le nœud possède déjà un fils gauche !")


def ajoute_filsD(n: dict[str, dict, dict], val: str) -> None:
    """
    Ajoute un noeud d'étiquette valeur comme fils droit. 
    """
    if est_vide(n['droit']):
        n['droit'] = {'valeur': val, 'gauche': None, 'droit': None}
    else:
        raise Exception("Le nœud possède déjà un fils droit !")


def est_feuille(n: dict[str, dict, dict]) -> bool:
    """
    Teste si un noeud est une feuille.
    """
    return est_vide(n['gauche']) and est_vide(n['droit'])


def degre_noeud(n: dict[str, dict, dict]) -> int:
    """
    Détermine le degré du noeud passé en argument.
    """
    if est_vide(n):
        raise Exception("Le nœud est vide !")

    nbre = 0
    if not est_vide(n['gauche']):
        nbre += 1
    if not est_vide(n['droit']):
        nbre += 1

    return nbre


def taille(n: dict[str, dict, dict]) -> int:
    """
    Retourne le nombre de noeud dans l'arbre.
    """
    if est_vide(n):
        return 0
    else:
        return 1 + taille(n['gauche']) + taille(n['droit'])


def profondeur(n: dict[str, dict, dict]) -> int:
    """
    Retourne la profondeur de l'arbre. 
    """
    if est_vide(n):
        return -1
    else:
        return 1 + max(profondeur(n['gauche']), profondeur(n['droit']))


def nbre_feuilles(n: dict[str, dict, dict]) -> int:
    """
    Détermine le nombre de feuilles dans l'arbre. 
    """
    if est_vide(n):
        return 0
    elif est_feuille(n):
        return 1
    else:
        return nbre_feuilles(n['gauche']) + nbre_feuilles(n['droit'])


def parcours_pref(n: dict[str, dict, dict]) -> str:
    """ Parcours en profondeur préfixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        return str(n['valeur']) + parcours_pref(n['gauche']) +\
            parcours_pref(n['droit'])


def parcours_inf(n: dict[str, dict, dict]) -> str:
    """ Parcours en profondeur infixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        return parcours_inf(n['gauche']) + str(n['valeur']) +\
            parcours_inf(n['droit'])


def parcours_suf(n: dict[str, dict, dict]) -> str:
    """ Parcours en profondeur infixe d'un arbre binaire. """
    if est_vide(n):
        return ""
    else:
        return parcours_suf(n['gauche']) + parcours_suf(n['droit']) +\
            str(n['valeur'])


if __name__ == "__main__":
    arb = {'valeur': 'A',
           'gauche': None,
           'droit': {'valeur': 'B',
                     'gauche': {'valeur': 'C',
                                'gauche': None,
                                'droit': None},
                     'droit': {'valeur': 'D',
                               'gauche': None,
                               'droit': None}}}
    print(est_vide(arb))
    print(parcours_inf(arb))

    arb2 = {'valeur': 'A', 'droit': None, 'gauche': None}
    ajoute_filsG(arb2, "B")
    ajoute_filsD(arb2, "C")
    noeud_C = arb2['droit']
    ajoute_filsD(noeud_C, "D")
    ajoute_filsG(noeud_C, "E")
    print(f"Taille de l'arbre : {taille(arb2)}")
    print(f"Profondeur (hauteur) de l'arbre : {profondeur(arb2)}")
    print(parcours_pref(arb2))
    print(parcours_inf(arb2))
    print(parcours_suf(arb2))
```

{{% /solution %}}

## À retenir

{{% note tip %}}
Un **arbre binaire** est un ensemble fini de nœuds, qui est soit **vide** (la valeur `None` est utilisée pour représenter l'arbre vide), soit structuré à partir d'un nœud particulier, appelé **racine** de l'arbre, et de deux sous-ensembles de nœuds formant récursivement un **sous-arbre gauche** et un **sous-arbre droit**.

Un arbre peut-être implémenté en Python avec un objet par nœud, d'une **classe** qui possède trois attributs : la valeur (ou étiquette) du nœud, le sous-arbre gauche et le sous-arbre droit. Il peut aussi être implémenté en utilisant une liste à trois éléments ou un dictionnaire à trois éléments.
{{% /note %}}
