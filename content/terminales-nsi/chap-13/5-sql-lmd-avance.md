---
title: "Le langage SQL : Le langage de manipulation de données (LMD), Compléments"
subtitle: "Chapitre 12,5"
author: ""
type: ""
date: 2021-02-09T08:37:37+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Notion de clé d'une relation et dépendance fonctionnelle

Lorsqu'on utilise une base de données, il est nécessaire d'accéder à un
enregistrement par le contenu d'un ou de plusieurs champs. On nomme
***clé*** d'une relation un champ, ou un ensemble de champs, qui permet
d'*identifier précisément un enregistrement.* Une relation peut
comprendre plusieurs clés possibles ; ce sont les *clés candidates*.

{{% note tip %}}
*On appelle **clé primaire** d'une relation la clé
minimale parmi toutes les clés candidates de la relation. Une clés
primaire doit toujours contenir une valeur et celle-ci doit être unique
pour chacun des enregistrements de la relation*
{{% /note %}}

Pour désigner une clé (primaire), il faut donc prendre en compte le «
sens » des données contenues dans la relation. **Si aucun champ ne peut
constituer une clé, il est nécessaire d'introduire un champ formel, tel
qu'un identifiant numérique.**

{{% note tip %}}
*Une **dépendance fonctionnelle** existe entre deux
ensembles de champs si les valeurs contenues dans l'un des ensembles de
champs permettent de déterminer les valeurs contenues dans l'autre
ensemble.*
{{% /note %}}

Les dépendances fonctionnelles expriment la relation de hiérarchie qui
existe entre les champs.

<center>

| Numero_carte | Nom | Age | Ville | Etablissement |
| :--: | :--: | :--: | :--: | :--: |
| 1 | Henri | 10 | Paris | Université Sorbonne |
| 2 | Stanislas | 34 | Paris | Université Jussieu |
| 3 | Henriette | 44 | Lyon | CHU Bron |
| 4 | Dominique | 19 | Nancy | Université Poincaré |
| 5 | Isabelle | 56 | Nancy | INPL |
| 6 | Olivier | 51 | Marseille | Université Saint Charles |
| 7 | Henri | 98 | Paris | Université Sorbonne |
| 8 | Jérôme | 23 | Nancy | INPL |
| 9 | Laurence | 34 | Bordeaux | Université Victor Segalen |
| 10 | Christian | 41 | Paris | ENS |
| 11 | Antoine | 16 | Marseille | Université Saint Charles |
| 12 | Laurence | 34 | Paris | Université Jussieu |

> *Relation lecteur(Numero_carte, Nom, Age, Ville,
  Etablissement)*

</center>

Si l'on examine les données de la relation, on remarque :

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

{{% note tip %}}
*On indique la clé primaire d'un schéma relationnel en soulignant le
champ, dans le schéma relationnel* : *Relation lecteur(<ins>Numero_carte</ins>, Nom, Age, Ville,
  Etablissement)*
{{% /note %}}


## Jointure de deux relations

### Qu'est-ce qu'une jointure ?

{{% note tip %}}
*La **jointure** est l'opération fondamentale de l'algèbre relationnelle
qui permet d'exprimer le sens du lien entre les relations, dans le monde
réel*. Conformément au programme, on ne présente ici que l'opération de
***jointure symétrique***.
{{% /note %}}

{{% note tip %}}
*Une **jointure** permet d'associer plusieurs
relations dans une même requête. Le résultat de cette requête est une
relation de **degré supérieur** aux degrés de chacune des relations de
départ. L'opération de jointure est **symétrique** et **associative**.*

*La liaison entre les relations s'effectue par le contenu commun d'un
champ (**champs de jointure**).*
{{% /note %}}

{{% note normal %}}
Il est bien évidemment possible d'*associer une jointure à une
projection et une sélection*. *Ces associations doivent être prises en
compte lors de la détermination du **degré** et de la **cardinalité** de
la relation finale*.
{{% /note %}}

<center>

| Numero_carte | Nom | Num_Etablissement |
| :--: | :--: | :--: |
| 1 | Henri | 1 |
| 2 | Stanislas | 2 |
| 3 | Henriette  | 1 |


> *Relation Lecteur_bis(<ins>Numero_carte</ins>, Nom,
  Numero_Etablissement)*

</center>

<center>

| Num_Etablissement | Ville | Nom_Etablissement |
| :--: | :--: | :--: |
| 1 | Paris | Université Jussieu |
| 2 | Lyon | CHU Bron |
| 3 | Nancy | Université Poincaré |
| 4 | Paris | Université Sorbonne |

> *Relation Etablissement(<ins>Num_Etablissement</ins> Ville, Nom_Etablissement)*

</center>

Même si l'on ne dispose pas du modèle conceptuel associé, on constate
que l'on peut relier les deux relations par le champ `Numero_Etablissement`. Les
informations concernant l'établissement de la relation `Lecteur_bis` sont
stockées dans la relation `Etablissement` dont la clé est le champ `Num_Etablissement`*. Pour
obtenir la liste des lecteurs ainsi que les informations concernant leur
établissement, on effectue une jointure entre ces relations sur le champ
`Numero_Etablissement`.*

Schéma de la base de données prenant en compte la jointure : Dans la
relation l'attribut est une *clé étrangère*.

<center>

| Numero_carte | Nom | Num_Etablissement | Num_Etablissement | Ville | Nom_Etablissement |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 1 | Henri | 1 | 1 | Paris | Université Jussieu |
| 2 | Stanislas | 2 | 2 | Lyon | CHU Bron |
| 3 | Henriette | 1 | 1 | Paris | Université Jussieu |

> Résultat de la jointure des relations `Lecteur_bis` et `Etablissement`.

</center>

Le champ `Num_Etablissement` figure deux fois dans la relation résultat de la jointure
car la première occurrence provient de la relation `Lecteur_bis` alors que la
seconde provient de la relation `Etablissement`.

Afin de ne conserver qu'*une occurrence des **champs de jointure***, on
peut réaliser une ***projection*** :

<center>

| Numero_carte | Nom | Num_Etablissement | Ville | Nom_Etablissement |
| :---: | :---: | :---: | :---: | :---: |
| 1 | Henri | 1 | Paris | Université Jussieu |
| 2 | Stanislas | 2 | Lyon | CHU Bron |
| 3 | Henriette | 1 | Paris | Université Jussieu |

> Résultat de la jointure des relations `Lecteur_bis` et `Etablissement` après projection.

</center>

Cette opération, $\text{jointure} + \text{projection}$, est parfois
appelée *jointure naturelle*.

Les champs de jointure ne doivent pas nécessairement être nommés à
l'identique.


### Comment effectuer une jointure en langage SQL ?

Il existe deux façons de réaliser une opération de jointure en SQL :

- la première est basée sur l'idée qu'*une opération de jointure
        peut être considérée comme une sélection sur le produit
        cartésien des deux relations* :
```SQL
SELECT * 
FROM Lecteur_bis, Etablissement
WHERE Lecteur_bis.Num_Etablissement = Etablissement.Num_Etablissement ;
```
*Avec une projection :*
```SQL
SELECT Lecteur_bis.Numero_carte,Lecteur_bis.Nom,Etablissement.Ville, Etablissement.Nom_Etablissement
FROM Lecteur_bis,Etablissement
WHERE Lecteur_bis.Num_Etablissement = Etablissement.Num_Etablissement ;
```

- la seconde méthode utilise l'opérateur de jointure  :
```SQL
SELECT * FROM Lecteur_bis 
JOIN Etablissement ON Lecteur_bis.Num_Etablissement = Etablissement.Num_Etablissement ;
```
*Avec une projection :*
```SQL
SELECT Lecteur_bis.Numero_carte, Lecteur_bis.Nom, Etablissement.Ville, Etablissement.Nom_Etablissement
FROM Lecteur_bis 
JOIN Etablissement ON Lecteur_bis.Num_Etablissement = Etablissement.Num_Etablissement ;
``` 

{{% note warning %}}
On remarque qu'*un champ est défini de façon unique grâce à la concaténation du nom de la relation et de celui du champ*. Si les champs portent des noms différents, il n'est pas nécessaire de préciser de quelle relation ils sont issus.
{{% /note %}}


## Fonctions de calculs

Une règle, dans le domaine des bases de données, est que tout ce qui
peut se calculer ne doit pas être stocké dans la base. *On évite ainsi
la perte de place et l'incohérence qui peut découler du stockage
d'informations redondantes*.

Le langage SQL ne possède pas d'instruction d'itération ; il possède
cependant des *fonctions simples de traitement des données d'une
colonne* (les calculs plus complexes doivent être effectués à l'aide
d'un langage de programmation comme Python).

<center>


| Fonction | Opération |
|:----:|:----:|
| `COUNT` | Comptage du nombre d'enregistrements de la table |
| `MAX` | Maximum des éléments d'une colonne |
| `MIN` | Minimum des éléments d'une colonne |
| `AVG` | Moyenne des éléments d'une colonne |
| `SUM` | Somme des éléments d'une colonne |


</center>

#### Exemples

- Détermination de l'age moyen des lecteurs
```SQL
 SELECT AVG(Age) AS Age_Moyen FROM lecteur ;
 ```
  
- Comptage du nombre de lecteurs
```SQL
SELECT COUNT(*) AS Nombre_Lecteurs FROM lecteur ;
```

Dans le cas de la fonction , il n'est pas nécessaire de préciser le champ puisque cette fonction s'applique à la relation toute entière.
