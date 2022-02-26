---
title: "Du schéma entités/associations au schéma relationnel"
subtitle: "Chapitre 12,3"
author: ""
type: ""
date: 2021-02-02T04:31:48+04:00
draft: false
toc: true
tags: []
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Concepts relationnels


### Modèle relationnel


Le modèle relationnel tire son nom de la notion de *relation*
mathématique entre les éléments. Chacun de ces éléments peut prendre des
valeurs dans un ensemble défini.

Par exemple, les appareils électroménagers d'une cuisine peuvent être
contenus dans l'ensemble des valeurs suivantes : {*Réfrigérateur*,
*Cuisinière*, *Hotte*, *Robot*, *Lave-vaisselle*}. On peut, par ailleurs,
aussi considérer l'ensemble des couleurs que peuvent prendre ces
appareils : {*Rouge*, *Vert*, *Bleu*, *Jaune*, *Blanc*, *Noir*, *Rose*}.
Les combinaisons possibles entre les appareils et les couleurs sont au
nombre de 35. Parmi toutes ces combinaisons possibles, on effectue une
sélection qui représente la description d'une cuisine :

```
(Réfrigérateur, Rouge)
(Robot, Mauve)
(Cuisinière, Jaune)
(Lave-vaisselle, Rouge)
```

Cet ensemble de couples de valeurs liées entre elles, que l'on nomme
**tuples** dans le modèle relationnel, représente la
**relation** entre les éléments « Appareil » et « Couleur ». On
désigne les éléments constitutifs de ces tuples par les termes
**attributs** (ou **champs**).

On peut écrire formellement la relation à partir de son schéma
relationnel : `ma_cuisine(Appareil, Couleur)`. Cette écriture représente le **schéma relationnel** de
la relation `ma_cuisine`. Les valeurs énoncées précédemment pour les champs
représentent leurs **domaines**, c'est à dire *les ensembles de toutes
les valeurs possibles pour un champ*.

On voit, à partir de cet exemple, qu'il est nécessaire de préciser les
concepts qui seront utilisés dans la suite de ce chapitre.


{{% note tip %}}
*Un **schéma relationnel** $R$ est formé par un
ensemble fini de $n$ attributs $U = \{ u\_1, \ldots, u\_n \}$. On le note
$R [u_1, \ldots, u_n]$ ou $R [U]$.*
{{% /note %}}

1. Quel est le schéma relationnel de la relation `ma_cuisine` ?
{{% solution "Réponse" %}}
Le schéma relationnel de la relation `ma_cuisine` est `ma_cuisine(Appareil, Couleur)`.
{{% /solution %}}


{{% note tip %}}
*L'**arité** (ou **degré**) d'un schéma relationnel $R$ est égale à son *nombre d'attributs*.*
{{% /note %}}


2. Quelle est l'arité du schéma `ma_cuisine(Appareil, Couleur)` ?
{{% solution "Réponse" %}}
L'arité du schéma `ma_cuisine(Appareil, Couleur)` est 2.
{{% /solution %}}

{{% note tip %}}
*Un **schéma de base de donnée** $R_B$ est un ensemble
fini de $p$ schémas relationnels. On le note
$R_B \{ R_1 [U_1], \ldots, R_p [U_p] \}$.*
{{% /note %}}

3. On donne le schéma de base de donnée suivant :\
```
Rb { Lecteur(Num_carte, Nom, Num_établissement), 
     Établissement(Num_établissement, Ville, Nom) }
``` 

3. De combien de schémas relationnels ce schéma de base de données est-il constitué ?
{{% solution "Réponse" %}}
Ce schéma de base de donnée et constitué de deux schéma relationnel : `Lecteur` et `Établissement`.
{{% /solution %}}

4. 

$$
    \begin{aligned}
        R_B & \{ \text{Lecteur} \left( \text{Numero\_carte}
        , \text{Nom}, \text{Numero\_Etablissement} \right) ,\cr
        &  \text{Établissement} \left( \text{Num\_Établissement}, \text{Ville}, \text{Nom\_Etablissement} \right) \} 
    \end{aligned}
$$

::: {.definition}
**Definition 5**. *Un **n-uplet** (ou tuple) $u$ sur $U$ est une
fonction de $U$ dans $\ensuremath{\operatorname{dom}}$. Si $u$ est un
n-uplet sur $U$ et $A \epsilon U$, $u (A)$ est la valeur de $u$ pour
l'attribut $A$.*

*L'écriture d'un n-uplet peut préciser les attributs : (Appareil :
Robot, Couleur : Mauve).*
:::

::: {.definition}
**Definition 6**. *Une **relation**, ou **instance d'un schéma
relationnel** $R [U]$, est un ensemble fini $I$ de n-uplets sur $U$. La
cardinalité de la relation est égale à celle de l'ensemble $I$.*

*Une **relation** est donc totalement décrite par :*

-   *le schéma relationnel ;*

-   *les domaines des différents champs ;*

-   *les tuples ou n-uplets qui la constituent.*

*On représente une relation par une table, correspondant à la notion de
tableau. Les tuples correspondent aux lignes et les attributs de la
relation aux colonnes.*

***Une relation étant constituée d'un ensemble de n-uplets, ceux-ci
doivent y être tous différents.***
:::

La relation (cf. tableau 1) est d'arité 2 et de cardinalité 4.

    **Appareil**    **Couleur**
  ---------------- -------------
   Réfrigérateur       Rouge
       Robot           Mauve
     Cuisinière        Jaune
   Lave-vaisselle      Rouge

  : *Relation*

::: {.definition}
**Definition 7**. *Une **base de données** $B$, ou **instance d'un
schéma de base de données** $R_B$, est une fonction, dont l'ensemble de
définition est un schéma de base de données $R_B$, telle que pour tout
$r
  \epsilon R_B$, $B (r)$ est une relation.*

*Une base de données est donc un ensemble de relations reliées entre
elles par des liens sémantiques.*
:::

Notion de clé d'une relation et dépendance fonctionnelle
--------------------------------------------------------

Lorsqu'on utilise une base de données, il est nécessaire d'accéder à un
enregistrement par le contenu d'un ou de plusieurs champs. On nomme
***clé*** d'une relation un champ, ou un ensemble de champs, qui permet
d'*identifier précisément un enregistrement.* Une relation peut
comprendre plusieurs clés possibles ; ce sont les *clés candidates*.

::: {.definition}
**Definition 8**. *On appelle **clé primaire** d'une relation la clé
minimale parmi toutes les clés candidates de la relation. Une clés
primaire doit toujours contenir une valeur et celle-ci doit être unique
pour chacun des enregistrements de la relation*
:::

Dans l'exemple de la relation , le choix de la clé n'est pas simple
car :

-   Plusieurs appareils différents peuvent être de même couleur ;

-   Une cuisine peut comporter plusieurs réfrigérateurs, robots, \...

Pourrait-on envisager d'utiliser le couple (appareil, couleur) comme clé
? La réponse est toujours négative, les réfrigérateurs présents dans la
pièce peuvent être de même couleur.

Pour désigner une clé (primaire), il faut donc prendre en compte le «
sens » des données contenues dans la relation. *Si aucun champ ne peut
constituer une clé, il est nécessaire d'introduire un champ formel, tel
qu'un identifiant numérique.*

::: {.definition}
**Definition 9**. *Une **dépendance fonctionnelle** existe entre deux
ensembles de champs si les valeurs contenues dans l'un des ensembles de
champs permettent de déterminer les valeurs contenues dans l'autre
ensemble.*
:::

Les dépendances fonctionnelles expriment la relation de hiérarchie qui
existe entre les champs.

::: {#relation-lecteur}
   **Numero_carte**    **Nom**    **Age**   **Ville**       **Etablissement**
  ------------------ ----------- --------- ----------- ---------------------------
          1             Henri       10        Paris        Université Sorbonne
          2           Stanislas     34        Paris        Université Jussieu
          3           Henriette     44        Lyon              CHU Bron
          4           Dominique     19        Nancy        Université Poincaré
          5           Isabelle      56        Nancy               INPL
          6            Olivier      51      Marseille   Université Saint Charles
          7             Henri       98        Paris        Université Sorbonne
          8            Jérôme       23        Nancy               INPL
          9           Laurence      34      Bordeaux    Université Victor Segalen
          10          Christian     41        Paris                ENS
          11           Antoine      16      Marseille   Université Saint Charles
          12          Laurence      34        Paris        Université Jussieu

  : *Relation lecteur(Numero_carte, Nom, Age, Ville,
  Etablissement)*[\[relation-lecteur\]]{#relation-lecteur
  label="relation-lecteur"}
:::

Si l'on examine les données de la relation , **Tableau
[1](#relation-lecteur){reference-type="ref"
reference="relation-lecteur"}.**, on remarque :

-   qu'il ne peut y avoir de dépendance fonctionnelle entre les
    ensembles (Ville, Etablissement) et (Nom, Age). En effet, le couple
    (Laurence, 34) correspond aux deux couples (Paris, Université de
    Jussieu) et (Bordeaux, Université Victor Segalen).

    *À un couple (Ville, Etablissement) ne correspond donc pas un unique
    couple (Nom, Age).*

-   que si l'on suppose qu'un établissement n'est situé que dans une
    seule ville, il existe une dépendance fonctionnelle entre le champ «
    Etablissement » et le champ « Ville ».

    *À une valeur du champ « Etablissement » correspond une et une seule
    valeur du champ « Ville ». Cette valeur n'est cependant pas unique.*

-   La valeur du champ « Numero_carte » est unique pour chacun des
    enregistrements. Ses valeurs sont identifiantes pour tous les champs
    de la relation. Chaque champ dépend fonctionnellement de ce champ.
    Ses valeurs ne sont jamais vides, c'est une clé candidate !

    Comme c'est aussi la seule clé de la relation, ce champ constitue la
    **clé primaire**.

Tous les champs qui ne font pas partie d'une clé candidate d'une
relation possèdent des dépendances fonctionnelles avec cette clé.

*On indique la clé primaire d'un schéma relationnel en soulignant le
champ, dans le schéma relationnel* : lecteur([Numero_carte]{.ul}, Nom,
Age, Ville, Etablissement).

Langage SQL
===========

SQL est un langage déclaratif qui permet d'interroger une base de
données par l'intermédiaire d'un SGBD sans se soucier de la
représentation interne (physique) des données, de leur localisation, des
chemins d'accès ou des algorithmes nécessaires. À ce titre, il s'adresse
à une large communauté d'utilisateurs potentiels, pas seulement aux
informaticiens. On peut l'utiliser de manière interactive, mais
également en association avec des interfaces graphiques, ou des langages
de programmation (comme Python).

Le langage SQL est composé de différents sous-ensembles :

LMD

:   Langage de Manipulation des données (DML, Data Manipulation
    Language).

    Il permet la *manipulation* et la *mise à jour des tables*, et est
    composé de quatre ordres fondamentaux : , , , .

LDD

:   Langage de Définition des Données (DDL, Data Definition Language).

    Il permet la *définition* et la *mise à jour du schéma relationnel*
    de la base de données (mode administration). Il est composé des
    ordres suivants : , , , , , , .

LCD

:   Langage de Contrôle des Données (DCL, Data Control Language).

    Il permet de définir les contraintes d'intégrité, de gérer les accès
    et les autorisations (administration). Il est composé des ordres : ,
    , .

Le programme cette année se limite au langage de manipulation des
données et plus particulièrement à l'ordre .

Opérations de l'algèbre relationnelle et traductions en langage SQL
===================================================================

La manipulation de données dans le modèle relationnel se fait à l'aide
d'opérations formelles reposant sur des concepts mathématiques issus de
la théorie des ensembles : c'est **l'algèbre relationnelle**.

::: {.definition}
**Definition 10**. *L'**algèbre relationnelle** consiste en un petit
nombre d'opérations de base qui, **appliquées à des relations,
produisent de nouvelles relations**. Ces opérations peuvent être
composées pour construire des expressions algébriques de plus en plus
complexes.*
:::

Opérations relationnelles de base
---------------------------------

### Projection

::: {.definition}
**Definition 11**. *La **projection** consiste à filtrer certains
attributs de la relation, ce qui donne au résultat une relation de
**degré** inférieur à celui de la relation de départ.*

*Pour $I$ une relation de schéma relationnel $I [A_{1 }, \ldots
  , A_n]$, si $1 \leqslant i < j \leqslant n$,
$$\pi_{A_i, \ldots, A_j} (I) = \{ (A_i : t (A_i), \ldots , A_j : t
     (A_j)) | t \epsilon I \}$$*
:::

    **Nom**    **Ville**
  ----------- -----------
     Henri       Paris
   Stanislas     Paris
   Henriette     Lyon
   Dominique     Nancy
   Isabelle      Nancy
    Olivier    Marseille
     Henri       Paris
    Jérôme       Nancy
   Laurence    Bordeaux
   Christian     Paris
    Antoine    Marseille
   Laurence      Paris

  : *Projection* *$\pi_{\text{Nom,Ville}}
    (\text{lecteur})$*

En langage SQL

:   `SELECT``\ `{=latex}`Nom,Ville``\ `{=latex}`FROM``\ `{=latex}`lecteur``\ `{=latex}`;`

### Sélection (ou restriction)

::: {.definition}
**Definition 12**. *La **sélection** consiste à filtrer des
enregistrements de la relation en fonction d'une **condition**. Le
résultat d'une sélection est une relation de **même degré** mais de
**cardinalité différente**.*

*Pour $I$ une relation de schéma relationnel $I [A_{1 }, \ldots
  , A_n]$ et $a \epsilon \ensuremath{\operatorname{dom}} (A_i)$,
$$\sigma_{A_i = a} (I) = \{ t \epsilon I | t (A_i) = a \}$$*
:::

   **Numero_carte**   **Nom**    **Age**   **Ville**      **Etablissement**
  ------------------ ---------- --------- ----------- --------------------------
          5           Isabelle     56        Nancy               INPL
          6           Olivier      51      Marseille   Université Saint Charles
          7            Henri       98        Paris       Université Sorbonne

  : *Selection $\sigma_{\text{Age} > 50} (\text{lecteur})$*

   **Numero_carte**   **Nom**   **Age**   **Ville**    **Etablissement**
  ------------------ --------- --------- ----------- ---------------------
          1            Henri      10        Paris     Université Sorbonne
          7            Henri      98        Paris     Université Sorbonne

  : *Selection $\sigma_{\text{Nom} = \text{''Henri''}}
    (\text{lecteur})$*

Intuitivement, dans une représentation de type table, une sélection
conserve uniquement les enregistrements vérifiant la condition.

En langage SQL

:   `SELECT``\ `{=latex}`*``\ `{=latex}`FROM``\ `{=latex}`lecteur``\ `{=latex}`WHERE``\ `{=latex}`Age``\ `{=latex}`>``\ `{=latex}`50``\ `{=latex}`;`

#### Affichage de tous les enregistrements d'une relation :

#### Composition d'une sélection et d'une projection :

Une sélection sur une relation formant une nouvelle relation, il est
possible de « passer » cette dernière en argument d'une opération de
projection. La composition se note :
$$\pi_{\text{champs}}  (\sigma_{\text{contrainte}}  (\text{relation}))$$

   **Nom**    **Ville**
  ---------- -----------
   Isabelle     Nancy
   Olivier    Marseille
    Henri       Paris

  : *Combinaison d'une sélection et d'une projection
  $\pi_{\text{Nom}, \text{Ville}} (\sigma_{\text{Age} > 50}
    (\text{lecteur}))$*

En langage SQL

:   `SELECT``\ `{=latex}`Nom,Ville``\ `{=latex}`FROM``\ `{=latex}`lecteur``\ `{=latex}`WHERE``\ `{=latex}`Age>50``\ `{=latex}`;`

#### Opérateurs de comparaison et connecteurs logiques de SQL

Ci-dessous sont présentés quelques opérateurs et connecteurs qui
apparaissent très fréquemment dans les requêtes SQL. Pour une liste plus
exhaustive et davantage d'exemples, consulter <http://sql.sh>.

   **Opérateur**   **Signification**
  --------------- -------------------
        $=$              Égal
       $< >$           Différent
        \<             Inférieur
        $>$            Supérieur
       $< =$       Inférieur ou égal
       $> =$       Supérieur ou égal

     **Signification**
  -- ---------------------------------------
     Appartient à un intervalle
     Appartient à un ensemble
     Teste si le champ contient une donnée
     Compare des chaînes de caractères

      **Nom**        **Instrument**
  ---------------- ------------------
   Jaco Pastorius   Basse électrique
     Bill Evans          Piano

     Appareil      Couleur        Nom            Instrument
  --------------- --------- ---------------- ------------------
   Réfrigérateur    rouge    Jaco Pastorius   Basse électrique
   Réfrigérateur    rouge      Bill Evans          Piano
       Robot        mauve    Jaco Pastorius   Basse électrique
       Robot        mauve      Bill Evans          Piano
    Cuisinière      jaune    Jaco Pastorius   Basse électrique
    Cuisinière      jaune      Bill Evans          Piano

  : *$\text{ma\_cuisine} \times \text{musicien}$*

L'exemple précédent a été choisi de façon à illustrer que le résultat
d'un produit cartésien peut n'avoir aucun sens dans la réalité.

En langage SQL

:   il n'est pas nécessaire d'utiliser un quelconque mot clé ; il faut
    requérir toutes les colonnes depuis les deux tables.

### Division Cartésienne

La division cartésienne est le pendant du produit cartésien, tout comme
la division euclidienne est le pendant du produit sur des entiers : si
on note $A$ et $B$ deux relations (ou tables), alors $A \div B$ est la
« plus grande » relation (au sens de l'inclusion) telle que le produit
cartésien avec $B$ redonne (presque) $A$. Formellement, c'est la plus
grande relation telle qu'il existe une relation $C$ vérifiant :
$$[(A \div B) \times B] \cup C = A \text{ \ \ \ \ et \ \ \ \ } [(A \div B)
   \times B] \cap C = \varnothing$$ Il n'existe pas en langage SQL
d'opérateur permettant d'implémenter directement la division
cartésienne.

Création d'un alias, renommage
------------------------------

Il peut être pénible d'utiliser, dans les requêtes, des noms de champs
définis de manière complexe, ou, tout simplement, nommés de façon pas
très parlante. On peut alors définir un *alias* pour renommer
*temporairement* un champ (et même une table).

::: {.definition}
**Definition 13**. *Un renommage pour un ensemble fini d'attributs U est
une fonction injective de U dans l'ensemble att que l'on notera
$A_1 \rightarrow B_1, ..., A_n
  \rightarrow B_n$.*

*L'opération de renommage
$\rho_{A_1 \rightarrow B_1, ..., A_n \rightarrow
  B_n}$ transforme une relation $I$ sur $A_1, ..., A_n$ en une relation
sur $B_1, ..., B_n$ de de telle sorte que :
$$\rho_{A_1 \rightarrow B_1, ..., A_n \rightarrow B_n} (I) = \left\{ v
     \text{sur} B_1, \ldots, B_n  | \exists u \epsilon I, v (B_i \right) = u
     (A_i)  \text{pour tout } i \epsilon [1 , n]  \}$$*
:::

La création d'un alias permet de faciliter grandement la lecture d'une
requête. Cette opération se note :

   **Badge**   **Nom**    **Ville**
  ----------- ---------- -----------
       7        Henri       Paris
       6       Olivier    Marseille
       5       Isabelle     Nancy

  : *$\rho_{\text{Numero\_carte} \rightarrow \text{Badge}} 
    (\pi_{\text{Numero\_carte}, \text{Nom}, \text{Ville}} (\sigma_{\text{Age} >
    50} (\text{lecteur})))$*

En langage SQL

:   on utilise le mot clé , immédiatement après le nom du champ, pour
    introduire l'alias.

Dans l'exemple précédent, on a illustré l'utilisation de la clause «  »
qui permet de trier les résultats suivant l'ordre (*par défaut
ascendant*) défini par certains champs (ici le mot clé indique que c'est
l'ordre descendant qui a été choisi).

Jointure
--------

*La **jointure** est l'opération fondamentale de l'algèbre relationnelle
qui permet d'exprimer le sens du lien entre les relations, dans le monde
réel*. Conformément au programme, on ne présente ici que l'opération de
***jointure symétrique***.

::: {.definition}
**Definition 14**. *Une **jointure** permet d'associer plusieurs
relations dans une même requête. Le résultat de cette requête est une
relation de **degré supérieur** aux degrés de chacune des relations de
départ. L'opération de jointure est **symétrique** et **associative**.*

*La liaison entre les relations s'effectue par le contenu commun d'un
champ (**champs de jointure**).*

*La jointure des relations et selon une certaine contrainte se note :
$$\text{table1} \vartriangleright \hspace{-0.5em}
     \vartriangleleft_{\text{contrainte}} \text{table2}  \text{ \ \ \ ou \ \ \
     }  \text{table1} [\ensuremath{\operatorname{contrainte}}]  \text{table2}$$*
:::

Il est bien évidemment possible d'*associer une jointure à une
projection et une sélection*. *Ces associations doivent être prises en
compte lors de la détermination du **degré** et de la **cardinalité** de
la relation finale*.

::: {#tab:jointure}
   **Numero_carte**    **Nom**    **Num_Etablissement**
  ------------------ ----------- -----------------------
          1             Henri               1
          2           Stanislas             2
          3           Henriette             1

  : *Relation Lecteur_bis($\underline{\text{Numero\_carte}}$, Nom,
  Numero_Etablissement)*[\[tab:jointure\]]{#tab:jointure
  label="tab:jointure"}
:::

   **Num_Etablissement**   **Ville**   **Nom_Etablissement**
  ----------------------- ----------- -----------------------
             1               Paris      Université Jussieu
             2               Lyon            CHU Bron
             3               Nancy      Université Poincaré
             4               Paris      Université Sorbonne

  : *Relation Etablissement($\underline{\text{Num\_Etablissement}}$,
  Ville, Nom_Etablissement)*

Même si l'on ne dispose pas du modèle conceptuel associé, on constate
que l'on peut relier les deux relations par le champ «  ». Les
informations concernant l'établissement de la relation «  » sont
stockées dans la relation «  » dont la clé est le champ «  »*. Pour
obtenir la liste des lecteurs ainsi que les informations concernant leur
établissement, on effectue une jointure entre ces relations sur le champ
«  ».*

Schéma de la base de données prenant en compte la jointure : Dans la
relation l'attribut est une *clé étrangère*.

   **Numero_carte**    **Nom**    **Num_Etablissement**   **Num_Etablissement**   **Ville**   **Nom_Etablissement**
  ------------------ ----------- ----------------------- ----------------------- ----------- -----------------------
          1             Henri               1                       1               Paris      Université Jussieu
          2           Stanislas             2                       2               Lyon            CHU Bron
          3           Henriette             1                       1               Paris      Université Jussieu

  : $\text{Lecteur\_bis} \vartriangleright \hspace{-0.5em}
    \vartriangleleft_{\text{Num\_Etablissement} = \text{Num\_Etablissement}} 
    \text{Etablissement}$

Le champ «  » figure deux fois dans la relation résultat de la jointure
car la première occurrence provient de la relation «  » alors que la
seconde provient de la relation «  ».

Afin de ne conserver qu'*une occurrence des **champs de jointure***, on
peut réaliser une ***projection*** :

   **Numero_carte**    **Nom**    **Num_Etablissement**   **Ville**   **Nom_Etablissement**
  ------------------ ----------- ----------------------- ----------- -----------------------
          1             Henri               1               Paris      Université Jussieu
          2           Stanislas             2               Lyon            CHU Bron
          3           Henriette             1               Paris      Université Jussieu

  :  $\pi_{\text{Numero\_carte}, \text{Nom}, \text{Num\_Etablissement},
    \text{Ville}, \text{Nom\_Etablissement}}  \left( \text{Lecteur\_bis}
    \vartriangleright \hspace{-0.5em}
    \vartriangleleft_{\text{Num\_Etablissement} = \text{Num\_Etablissement}} 
    \text{Etablissement} \right)$

Cette opération, $\text{jointure} + \text{projection}$, est parfois
appelée *jointure naturelle*.

Les champs de jointure ne doivent pas nécessairement être nommés à
l'identique. Nous verrons comment les différentier dans la partie « En
langage SQL », page .

*On peut considérer l'opération de jointure comme une sélection sur le
produit cartésien des deux relations.* On ne conserve que les lignes
dont le contenu du champ sur lequel s'effectue la jointure est égal.

   **Numero_carte**    **Nom**    **Num_Etablissement**   **Num_Etablissement**   **Ville**   **Nom_Etablissement**
  ------------------ ----------- ----------------------- ----------------------- ----------- -----------------------
          1             Henri               1                       1               Paris      Université Jussieu
          1             Henri               1                       2               Lyon            CHU Bron
          1             Henri               1                       3               Nancy      Université Poincaré
          1             Henri               1                       4               Paris      Université Sorbonne
          2           Stanislas             2                       1               Paris      Université Jussieu
          2           Stanislas             2                       2               Lyon            CHU Bron
          2           Stanislas             2                       3               Nancy      Université Poincaré
          2           Stanislas             2                       4               Paris      Université Sorbonne
          3           Henriette             1                       1               Paris      Université Jussieu
          3           Henriette             1                       2               Lyon            CHU Bron
          3           Henriette             1                       3               Nancy      Université Poincaré
          3           Henriette             1                       4               Paris      Université Sorbonne

  : *$\text{Lecteur\_bis} \vartriangleright \hspace{-0.5em}
    \vartriangleleft_{\text{Num\_Etablissement} = \text{Num\_Etablissement}} 
    \text{Etablissement}$* *Les lignes grisées sont celles qui sont
  sélectionnées lors d'une jointure.*

En langage SQL

:   il existe deux façons de réaliser une opération de jointure en SQL :

    -   la première est basée sur l'idée qu'*une opération de jointure
        peut être considérée comme une sélection sur le produit
        cartésien des deux relations* :

        *Avec une projection :*

        Le traitement de la requête n'est cependant pas, dans ce cas,
        optimal au niveau du SGBD.

    -   la seconde méthode utilise l'opérateur de jointure  :

        *Avec une projection :*

    On remarque qu'*un champ est défini de façon unique grâce à la
    concaténation du nom de la relation et de celui du champ* :
    .[\[champ-nom-unique\]]{#champ-nom-unique label="champ-nom-unique"}

    Si les champs portent des noms différents, il n'est pas nécessaire
    de préciser de quelle relation ils sont issus.

Fonctions de calculs et d'agrégation
------------------------------------

Une règle, dans le domaine des bases de données, est que tout ce qui
peut se calculer ne doit pas être stocké dans la base. *On évite ainsi
la perte de place et l'incohérence qui peut découler du stockage
d'informations redondantes*.

### Fonctions de calculs

Le langage SQL ne possède pas d'instruction d'itération ; il possède
cependant des *fonctions simples de traitement des données d'une
colonne* (les calculs plus complexes doivent être effectués à l'aide
d'un langage de programmation comme Python).

   **Fonction**  **Opération**
  -------------- --------------------------------------------------
                 Comptage du nombre d'enregistrements de la table
                 Maximum des éléments d'une colonne
                 Minimum des éléments d'une colonne
                 Moyenne des éléments d'une colonne
                 Somme des éléments d'une colonne

  : *Fonctions statistiques de SQL*

Détermination de l'age moyen des lecteurs

:   

Comptage du nombre de lecteurs

:   Dans le cas de la fonction , il n'est pas nécessaire de préciser le
    champ puisque cette fonction s'applique à la relation toute entière.

### Agrégats ou groupage

::: {.definition}
**Definition 15**. *Les opérations d'« agrégation » (ou de groupage)
regroupent les enregistrements d'une relation par valeurs contenues dans
une colonne.*

*On applique généralement des opérations de calcul sur les
« sous-tables » ainsi créées.*
:::

   **NumVoit**   **Marque**   **Type**   **Couleur**
  ------------- ------------ ---------- -------------
        1         Peugeot       404         Rouge
        2         Citroen        SM         Noire
        3           Opel         GT        Blanche
        4         Peugeot       403        Blanche
        5         Renault      Alpine       Rose
        6         Renault     Floride       Bleue
        7         Peugeot       806        Blanche

  : *Relation Voiture(NumVoit,Marque,Type,Couleur)*

Affichage des différentes marques

:   Pour réaliser cette opération avec SQL, on utilise le mot clé suivi
    du nom de la colonne sur laquelle s'effectue l'agrégat.

    `SELECT``\ `{=latex}`Marque``\ `{=latex}`FROM``\ `{=latex}`Voiture``\ `{=latex}`GROUP``\ `{=latex}`BY``\ `{=latex}`Marque;`

   **Marque**
  ------------
    Peugeot
    Citroen
      Opel
    Renault

  : *Différentes marques de voitures*

Affichage du nombre de voitures des différentes marques

:   Lors de cette opération, la fonction est appliquée à chaque
    « sous-tables » créée.

    `SELECT``\ `{=latex}`Marque,``\ `{=latex}`COUNT(*)``\ `{=latex}`AS``\ `{=latex}`Compte``\ `{=latex}`FROM``\ `{=latex}`Voiture``\ `{=latex}`GROUP``\ `{=latex}`BY``\ `{=latex}`Marque``\ `{=latex}`;`

   **Marque**   **Compte**
  ------------ ------------
    Peugeot         3
    Citroen         1
      Opel          1
    Renault         2

  : *Comptage du nombre de voitures, pour chaque marque*

Affichage de l'age moyen des lecteurs, par université de la relation 

:   

### Restriction sur le résultat d'une requête agrégative

Le résultat de l'opération de groupage peut lui-même être filtré : on
effectue une sélection des lignes par rapport au contenu des colonnes
obtenues dans la table résultat de la recherche groupée.

Calcul du nombre de voitures par marque dont le nombre est supérieur à 1

:   `SELECT``\ `{=latex}`Marque,``\ `{=latex}`COUNT(*)``\ `{=latex}`AS``\ `{=latex}`Compte`\
    `FROM``\ `{=latex}`Voiture`\
    `GROUP``\ `{=latex}`BY``\ `{=latex}`Marque`\
    `HAVING``\ `{=latex}`Compte``\ `{=latex}`>``\ `{=latex}`1``\ `{=latex}`;`

   **Marque**   **Compte**
  ------------ ------------
    Peugeot         3
    Renault         2

  : *Comptage du nombre de voitures, pour chaque marque, si le nombre
  est supérieur à 1*

*Le mot clé permet d'effectuer une sélection sur le résultat de
l'opération de groupage. Le mot clé opère une sélection sur les
enregistrements de la table avant l'opération de groupage.*

Calcul du nombre de voitures, par marque, dont la couleur n'est pas « Rouge »

:   `SELECT``\ `{=latex}`Marque,``\ `{=latex}`COUNT(*)``\ `{=latex}`AS``\ `{=latex}`Compte`\
    `FROM``\ `{=latex}`Voiture`\
    `WHERE``\ `{=latex}`NOT``\ `{=latex}`(Couleur``\ `{=latex}`=``\ `{=latex}`’Rouge’)`\
    `GROUP``\ `{=latex}`BY``\ `{=latex}`Marque`

 

[^1]: *Misc:* *Chapitre S2,07*

[^2]: Un tuple est aussi désigné par les termes ***n-uplets*** ou
    ***enregistrement***.
