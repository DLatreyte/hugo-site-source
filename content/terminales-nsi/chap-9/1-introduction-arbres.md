---
title: "Structures de données abstraites arborescentes : les arbres"
subtitle: "Chapitre 9,1"
author: ""
type: ""
date: 2020-11-05T03:37:56+04:00
draft: false
toc: true
tags: ["Arbres", "Listes"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> La notion de listes chaînées est parfaite pour structurer un ensemble d'élements destinés à être énumérés séquentiellement. Elle permet aussi d'implémenter les structures de piles et de files. *Elle n'est cependant pas adaptée aux accès spécifiques à des positions données dans la séquence*, puisqu'il faut alors parcourir toutes les cellules depuis le début de la liste jusqu'à la position souhaitée (complexité en $O(N)$).

{{< remote "Document de référence pour ce cours"  "https://isn-icn-ljm.pagesperso-orange.fr/NSI-TLE/co/section_chapitre3.html" >}}

## Structures arborescentes

Lorsqu'on manipule une information présentant une certaine hiérarchie, il est commun de la représenter graphiquement&nbsp;:

#### Arbre généalogique

{{< mermaid >}}
graph TD
    A(Jules) --> B(Mireille)
    A(Jules) --> C(Gérard)
    A(Jules) --> D(Guy)
    B --> E(David)
    E --> F(Gabriel)
    E --> G(Louise)
    C --> H(Fabien)
    D --> I(Sandra)
    D --> J(Marion)
{{< /mermaid >}}

#### Arborescence d'un système de fichier

{{< mermaid >}}
graph TD
  A(/) --> B(bin)
  A --> C(root)
  A --> D(home)
  A --> F(etc)
  A --> G(var)
  A --> H(usr)
  A --> I(tmp)
  D --> J(mats)
  J --> K(Documents)
  J --> L(Images)
  J --> M(Vidéos)
  K --> N(Terminale)
  N --> O(NSI)
  N --> P(PC)
{{< /mermaid >}}

#### Expression mathématique

{{< mermaid >}}
graph TD
  A(+) --> B(*)
  B --> C(3)
  B --> D(8)
  A --> E(6)
{{< /mermaid >}}

{{% note exercise %}}
Écrire l'expression mathématique représentée par l'arbre ci-dessus.
{{% /note %}}
{{% solution "Réponse" %}}
$3 \times 8 + 6$
{{% /solution %}}

{{% note exercise %}}
Écrire l'arbre représentant l'expression mathématique $ a\\, sin( \dfrac{2\pi}{T}t)$.
{{% /note %}}

{{% solution "Réponse" %}}
<img src="/terminales-nsi/chap-9/chap-9-1-1.svg" alt="" width="">
{{% /solution %}}

 


#### Arbre lexicographique 
Un arbre lexicographique, ou arbre en parties communes, ou dictionnaire, représente un ensemble de mots. *Les préfixes communs à plusieurs mots n'apparaissent qu'une seule fois dans l’arbre*.

{{< mermaid >}}
graph TD
  A(.) --> B(m)
  B --> C(a)
  C --> D(i)
  D --> E(s)
  E --> F(o)
  F --> G(n)
  D --> H(t)
  H --> I(r)
  I --> J(i)
  J --> K(s)
  K --> L(e)
  L --> M(r)
  C --> N(t)
  N --> O(e)
  O --> P(l)
  P --> Q(a)
  Q --> R(t)
  P --> S(o)
  S --> T(t)
  A --> U(v)
  U --> V(a)
  V --> W(l)
  W --> X(i)
  X --> Y(s)
  Y --> Z(e)
{{< /mermaid >}}

{{% note exercise %}}
Quels sont les mots représentés dans l'arbre&nbsp;?
{{% /note %}}

{{% note exercise %}}
Ajouter les mots «&nbsp;matériel&nbsp;» et «&nbsp;vallon&nbsp;».

**Remarque&nbsp;:** ne pas différencier les lettres é et e.
{{% /note %}}
{{% solution "Réponse" %}}
<img src="/terminales-nsi/chap-9/chap-9-1-2.svg" alt="" width="">
{{% /solution %}}

## Définitions et vocabulaire

### Arbre (enraciné)

{{% note tip %}}
- Un **arbre** (nom complet **arbre enraciné**) est une *structure de données abstraite arborescente dans laquelle les données sont hiérarchisées depuis un **nœud racine**.*

- Un arbre dont tous les nœuds sont nommés est dit **étiqueté**. L’étiquette (ou nom du sommet) représente la «&nbsp;valeur&nbsp;» du nœud ou bien l’information associée au nœud.
{{% /note %}}

### Racine, noeud, branche, feuille

{{% note tip %}}
- Un arbre est un ensemble organisé de **nœuds** dans lequel *chaque nœud a un **père**, sauf un nœud que l’on appelle le **nœud racine**.*
- *Si le nœud n’a pas de fils*, on dit que c’est une **feuille**.
- Les nœuds sont reliés par des **branches**.
{{% /note %}}

{{% note exercise %}}
- Nommer les nœuds puis les feuilles dans l'arbre représenté ci-dessous.
- Compter le nombre de branches.
{{% /note %}}
{{< mermaid >}}
graph TD
  A(a) --> B(b)
  A --> C(c)
  B --> D(d)
  B --> E(e)
  E --> F(f)
  E --> G(g)
  B --> H(h)
  H --> I(i)
{{< /mermaid >}}
{{% solution "Réponses" %}}
- **Nœuds**&nbsp;: a (racine), b, e, h et **feuilles**&nbsp;: c, d, f, g, i.
- 8 branches.
{{% /solution %}}

### Hauteur d'un nœud, profondeur d'un arbre

{{% note tip %}}
La **hauteur** (ou **profondeur** ou **niveau**) d'un nœud est égale au *nombre de nœuds rencontrés en descendant de la racine jusqu'au nœud (**racine et nœud inclus**)*.
{{% /note %}}

{{% note tip %}}
La **hauteur** (ou **profondeur**) d’un *arbre* est égale à *la profondeur du nœud le plus profond*.
{{% /note %}}

{{% note normal %}}
La hauteur d'un arbre est très importante. En effet, la plupart des algorithmes que nous verrons dans la suite ont une *complexité qui dépend de la hauteur de l'arbre*. Ainsi plus l'arbre aura une hauteur élevée, plus l'algorithme mettra de temps à s'exécuter. 
{{% /note %}}

{{% note warning %}}
Dans notre convention, la hauteur de la racine est égale à 1. *Tous les auteurs n'utilisent pas cette convention !* Pour certains, la **hauteur** d’un *nœud* est égale au *nombre d’arêtes qu’il faut parcourir à partir de la racine pour parvenir au nœud*&nbsp;; la hauteur de la racine est alors de 0.   
{{% /note %}}

{{% note exercise %}}
- Donner la hauteur du nœud `e` dans l'arbre représenté ci-dessus.
- Quelle est la profondeur de cet arbre&nbsp;?
{{% /note %}}
{{% solution "Réponses" %}}
- Hauteur de `e`&nbsp;: 3.
- Profondeur de l'arbre&nbsp;: 4.
{{% /solution %}}

### Taille d'un arbre

{{% note tip %}}
La **taille** d’un arbre est égale au *nombre de nœuds de l’arbre (nœuds internes et feuilles)*.   
{{% /note %}}

{{% note exercise %}}
- Indiquer la taille de l'arbre représenté ci-dessus.
{{% /note %}}
{{% solution "Réponses" %}}
- Taille de l'arbre&nbsp;: 9.
{{% /solution %}}

### Degré d’un noeud, degré d’un arbre 

{{% note tip %}}
- Le **degré d’un nœud** est égal au *nombre de ses descendants (fils)*.
- Le **degré d’un arbre** est égal au *plus grand des degrés de ses nœuds*.
{{% /note %}}

{{% note exercise %}}
- Quel est le degré du nœud `b` dans l'arbre représenté ci-dessus&nbsp;?
- Quel est le degré du nœud `a`&nbsp;?
- Quel est le degré de l'arbre&nbsp;?
{{% /note %}}
{{% solution "Réponses" %}}
- Degré de `b`&nbsp;: 3.
- Degré de `a`&nbsp;: 2.
- Degré de l'arbre&nbsp;: 3.
{{% /solution %}}

## Relation entre les liste et les arbres 

{{% note tip %}}
Un arbre dont tous les nœuds n’ont qu’un seul fils est en fait une liste.
{{% /note %}}