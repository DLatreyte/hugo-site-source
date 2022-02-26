---
title: "Le langage SQL : Le langage de manipulation de données (LMD)"
subtitle: "Chapitre 12,4"
author: ""
type: ""
date: 2021-02-04T04:29:53+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

## Introduction

{{% note normal %}}
Le langage SQL est composé de différents sous-ensembles :

LMD : Langage de Manipulation des données (DML, Data Manipulation Language)
:   *Permet la manipulation et la mise à jour des tables*, composé de quatre ordres fondamentaux : `SELECT`, `UPDATE`, `INSERT`, `DELETE`.

LDD : Langage de Définition des Données (DDL, Data Definition Language)
:   *Permet la définition et la mise à jour du schéma relationnel de la base de données* (mode administration). Composé des ordres suivants : `CREATE TABLE`, `CREATE INDEX`, `CREATE VIEW`, `DROP TABLE`, `DROP INDEX`, `DROP VIEW`, `ALTER TABLE`.

LCD : Langage de Contrôle des Données (DCL, Data Control Language)
:   *Permet de définir les contraintes d’intégrité, de gérer les accès et les autorisations* (administration). Composé des ordres : `GRANT`, `REVOKE`, `LOCK`. Recouvre les déclencheurs (triggers), procédures cataloguées.
{{% /note %}}

Le programme se limite au sous-ensemble **LMD**. Nous serons tout de même obligés d'utiliser l'ordre de création de table `CREATE TABLE`.

## SQLite 

Dans ce cours nous utiliserons SQLite depuis l'interface de {{< remote "Repl.it" "https://repl.it/" >}}. 

SQLite est un **moteur de base de données relationnelle** (sous-ensemble d'un **SGBD**) accessible par le langage SQL. Contrairement aux serveurs de bases de données traditionnels, comme MySQL ou PostgreSQL, sa particularité est de ne pas reproduire le *schéma habituel client-serveur* mais de *fonctionner sans serveur* (on parle de *base de données « standalone » ou « embarquée »*). L'intégralité de la base de données (déclarations, tables, index et données) est stockée dans un fichier indépendant de la plateforme.

Remarque
:   On peut accéder à SQLite depuis de nombreux langages de programmation. Nous utiliserons dans un premier temps une *interface en ligne de commande (CLI)* et par la suite *Python*. 

SQLite est le moteur de base de données le plus utilisé au monde.

{{% note warning %}}
Chaque SGBD possède, en plus du SQL, des commandes propres : {{< remote "section 3 de la documentation officielle" "https://sqlite.org/cli.html" >}} Ces dernières **commencent toujours par un point** en SQLite et **ne devront pas être apprises !**
{{% /note %}}

## Création d'une première base de données

On possède un fichier tableur contenant des informations sur quelques acteurs, parmi les plus célèbres.

<center>

| Nom | Prénom | Sexe | Pays | Age |
|:---:|:---:|:---:|:---:|:---:|
| Hanks | Tom | Homme | USA | 64 |
| Holland | Tom | Homme | Angleterre | 24 |
| Johansson | Scarlett | Femme | USA | 36 |
| Johnson | Dwayne | Homme | USA | 48 |
| Robbie | Margot | Femme | Australie | 30 |
| Cotillard | Marion | Femme | France | 45 |
| Gadot | Gal | Femme | Israël | 35 |
| Cruise | Tom | Homme | USA | 58 |

</center>


On souhaite transformer ce fichier en une base de données contenant, pour l'instant, *une seule relation*.

1. Réaliser une copie de l'{{< remote "environnement de travail sur repl.it" "https://repl.it/@dlatreyte/Celebrites" >}}

L'instruction de création de la table (relation) est 
```SQL
CREATE TABLE  IF NOT EXISTS "Celebrites" (
    Nom varchar(40),
    Prenom varchar(40),
    Sexe varchar(6),
    Pays varchar(15),
    Age int
);
```

2. Indiquer la signification de chaque ligne de la commande.

3. Incorporer la commande au fichier `celebrites.sql` et l'exécuter.

4. Afin de vérifier que la commande a bien créé une table dans **la base de données qui réside pour l'instant dans la RAM**, ajouter la commande suivante au fichier `main.sql` 
```SQL
-- Énumérations des tables
.tables
```
Relancer l'exécution des commandes et observer le résultat dans la console.

5. Afin d'examiner la structure de la table `Celebrites`, ajouter l'une des commandes suivantes au fichier `main.sql`.
```SQL
-- Structure de la table Celebrites
.schema 'Celebrites'
```
ou
```SQL
-- Structure de la table Celebrites
pragma table_info('Celebrites');
```

La commande permettant d'intégrer le tuple `("Hanks", "Tom", "Homme", "USA", 64)` à la relation `Celebrites` est :
```SQL
INSERT INTO Celebrites VALUES ("Hanks", "Tom", "Homme", "USA", 64);
```

{{% note warning %}}
La commande, telle qu'elle est donnée ici, impose le respect de l'ordre des informations dans le tuple.
{{% /note %}}

6. Intégrer la commande précédente au fichier `celebrites.sql`. Exécuter cette commande. La sortie fait-elle apparaître le résultat de cette commande ?

7. Afin de vérifier que les informations ont bien été ajoutées à la base de données, ajouter la commande suivante dans le fichier `main.sql` 
```SQL
SELECT * FROM Celebrites;
```
Exécuter cette commande.

8. Ajouter maintenant au fichier `celebrites.sql` toutes les commandes permettant de peupler la base de données.\
Exécuter ces commandes.

9. La base de données réside toujours en mémoire et n'a, pour l'instant, pas été sauvegardée dans un fichier. Ajouter la commande suivante à la fin du fichier `celebrites.sql`
```SQL
.save "cinema.sqlite"
```
Vérifier que le fichier `cinema.sqlite` a bien été créé.

{{% note normal %}}
Désormais, à la prochaine utilisation de la base de données il ne sera plus nécessaire de relancer toute la création de la base de données (ce qui pourrait être très très long dans le cas d'une base conséquente) mais seulement la commande 
```SQL
.open "cinema.sqlite"
```
au début du fichier `main.sql` (qui ne devra alors plus lire le fichier `celebrites.sql`).
{{% /note %}}

## Premières requêtes : Projection

{{% note warning %}}
Toutes les commandes à venir devront être entrées dans le fichier `main.sql` après la commande de lecture du fichier `celebrites.sql` (ou après la commande de lecture du fichier `cinema.sqlite`).
{{% /note %}}

10. La commande `SELECT * FROM Celebrites;` est une requête. Que signifie le caractère `*` dans cette commande ?
{{% solution "Réponse" %}}
Le caractère `*` indique que l'on souhaite que la relation retournée par la commande `SELECT` contienne tous les attributs (champs).
{{% /solution %}}

{{% note tip %}}
*Une **projection** consiste à filtrer certains
attributs d'une relation. Le résultat d'une projection est une relation de
**degré** inférieur à celui de la relation de départ.*
{{% /note %}}

11. Adapter la commande précédente de façon à obtenir tous les noms des acteurs présents dans la base de données.
{{% solution "Réponse" %}}
```SQL
SELECT Nom 
FROM Celebrites;
``` 
{{% /solution %}}

12. Adapter la commande précédente de façon à obtenir tous les noms et sexes des acteurs présents dans la base de données.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Sexe 
FROM Celebrites;
```
{{% /solution %}}

## Premières requêtes : Sélection

### Sélections simples

{{% note tip %}}
*La **sélection** consiste à filtrer des
enregistrements d'une relation en fonction d'une **condition**. Le
résultat d'une sélection est une relation de **même degré** mais de
**cardinalité différente**.*

Une sélection s'effectue en langage SQL à l'aide de la clause `WHERE`.
{{% /note %}}

13. Écrire la commande qui retourne toutes les informations relatives aux femmes présentes dans la base de données.
{{% solution "Réponse" %}}
```SQL
SELECT * 
FROM Celebrites
WHERE Sexe = "Femme";
```
{{% /solution %}}

14. Adapter la commande précédente de façon à obtenir tous les noms et prénoms des femmes présentes dans la base de données.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, prenom 
FROM Celebrites
WHERE Sexe = "Femme";
```
{{% /solution %}}

### Opérateurs de comparaison

15. Quels sont les noms de tous les acteurs (sans distinction de sexe) qui n'ont pas pour pays d'origine les USA.
{{% solution "Réponse" %}}
```SQL
SELECT Nom
FROM Celebrites
WHERE Pays != "USA";
```
{{% /solution %}}

16. Quels sont les noms des acteurs (sans distinction de sexe) qui ont plus de 40 ans ?
{{% solution "Réponse" %}}
```SQL
SELECT Nom
FROM Celebrites
WHERE Age > 40;
```
{{% /solution %}}

17. Quels sont les noms et prénoms des acteurs (sans distinction de sexe) qui ont plus de 40 ans ?
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Age > 40;
```
{{% /solution %}}

18. Quels sont les noms des acteurs (sans distinction de sexe) qui ont au plus 36 ans ?
{{% solution "Réponse" %}}
```SQL
SELECT Nom
FROM Celebrites
WHERE Age <= 36;
```
{{% /solution %}}

19. Quels sont les noms des actrices françaises ?
{{% solution "Réponse" %}}
```SQL
SELECT Nom
FROM Celebrites
WHERE Sexe = "Femme" AND Pays = "France";
```
{{% /solution %}}

20. Quels sont les ages des acteurs américains hommes dont le prénom est Tom ?
{{% solution "Réponse" %}}
```SQL
SELECT Age
FROM Celebrites
WHERE Sexe = "Homme" AND Prenom = "Tom" AND Pays = "USA";
```
{{% /solution %}}

21. Quels sont les prénoms des acteurs (sans distinction de sexe) australiens ou de plus de 40 ans ?
{{% solution "Réponse" %}}
```SQL
SELECT Prenom
FROM Celebrites
WHERE Age > 40 OR Pays = "Australie";
```
{{% /solution %}}

## Exercices d'application

### Les sportifs stars

Écrire toutes les commandes correspondant au requêtes ci-dessous pour la base de donnée se trouvant à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Sportifs-Stars" >}}

1. Donner le schéma relationnel de la base de données.
2. Afficher les noms de tous les sportifs.
3. Afficher les noms et prénoms de tous les sportifs.
4. Afficher les noms, prénoms et sports de tous les sportifs.
5. Afficher le nom des sportifs nés au mois de décembre.
6. Afficher les noms et prénoms des sportifs nés en juin.
7. Afficher les noms et prénoms des sportifs nés en 1981.
8. Afficher les noms et prénoms des sportifs pratiquant le football. 

### Instagram

Écrire toutes les commandes correspondant au requêtes ci-dessous pour la base de donnée se trouvant à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Instagram" >}}

1. Donner le schéma relationnel de la base de données.
2. Afficher toutes les informations relatives aux utilisateurs qui ne sont pas des footballeurs.
3. Afficher toutes les informations relatives aux utilisateurs qui ont plus de 200 million followers.
4. Afficher toutes les informations relatives des utilisateurs qui ont au plus 200 million followers.
5. Afficher toutes les informations relatives des utilisateurs qui ont au moins 200 million followers.
6. Afficher les prénoms, noms et « Instagram handle » des comptes qui ont au maximum 155 millions de followers.
7. Afficher toutes les informations pour les comptes qui correspondent à des chanteurs et qui ont plus de 200 millions de followers.
8. Afficher toutes les informations pour les comptes qui correspondent à des footballeurs ou qui ont moins de 150 millions de followers.

## Première requêtes : Ordres SQL

{{% note normal %}}

On reprend, dans cette partie, l'étude de la relation `Celebrites`.

{{% /note %}}

{{% note tip %}}
L'opérateur `ORDER BY` est utilisé pour *trier le résultat d'une projection*. Par défaut ce tri s'effectue par *ordre croissant* (lexicographique ou numérique). Pour trier par ordre décroissant, il faut ajouter le mot clé `DESC`, pour trier par ordre croissant on utilise `ASC`. 
{{% /note %}}

22. Rechercher toutes les informations sur les acteurs, triées par age croissant.
{{% solution "Réponse" %}}
```SQL
SELECT *
FROM Celebrites
ORDER BY Age;
```
{{% /solution %}}

23. Rechercher toutes les informations sur les acteurs, triées par pays d'origine (par ordre décroissant).
{{% solution "Réponse" %}}
```SQL
SELECT *
FROM Celebrites
ORDER BY Pays DESC;
```
{{% /solution %}}

24. Rechercher les noms et prénoms des acteurs triés par age et nom croissants.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prénom
FROM Celebrites
ORDER BY Age, Nom;
```
{{% /solution %}}

25. Rechercher les noms et prénoms des acteurs triés par age décroissant et nom croissant.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prénom
FROM Celebrites
ORDER BY Age DESC, Nom ASC;
```
{{% /solution %}}

26. Rechercher les ages et sexes des acteurs, triés par age croissant.
{{% solution "Réponse" %}}
```SQL
SELECT Age, Sexe
FROM Celebrites
ORDER BY Age;
```
{{% /solution %}}


{{% note tip %}}
L'opérateur `BETWEEN` est utilisé pour *sélectionner une valeur numérique dans un intervalle*. 
{{% /note %}}

27. Écrire une requête qui affiche toutes les informations sur les artistes dont les ages sont compris entre 30 et 60 ans.
{{% solution "Réponse" %}}
```SQL
SELECT Age, Sexe
FROM Celebrites
WHERE Age BETWEEN 30 AND 60;
```
{{% /solution %}}

## Première requêtes : recherche de motifs lors d'une sélection

{{% note normal %}}

On reprend, dans cette partie, l'étude de la relation `Celebrites`.

{{% /note %}}

{{% note tip %}}
L'opérateur `LIKE` permet de rechercher un motif lors d'une sélection.
{{% /note %}}

27. Rechercher les prénoms des acteurs dont le nom commence par la lettre `j`.
{{% solution "Réponse" %}}
```SQL
SELECT Prenom
FROM Celebrites
WHERE Nom LIKE 'J%';
```
{{% /solution %}}

28. Rechercher les noms et prénoms des acteurs dont le sexe commence par la lettre `h`, trié par nom croissant.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Sexe LIKE 'h%'
ORDER BY Nom;
```
{{% /solution %}}

29. Rechercher les noms et prénoms des acteurs dont le prénom se termine par la lettre `t`.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Prenom LIKE '%t';
```
{{% /solution %}}

30. Rechercher les noms et prénoms des acteurs dont le prénom contient la lettre `a`.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Prenom LIKE '%a%';
```
{{% /solution %}}

31. Rechercher les noms et prénoms des acteurs dont le pays d'origine commence par un `a`.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Pays LIKE 'a%';
```
{{% /solution %}}

32. Rechercher les noms et prénoms des acteurs dont le pays d'origine se termine par un `l`.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Pays LIKE '%l';
```
{{% /solution %}}

33. Rechercher les noms et prénoms des acteurs dont le pays d'origine comporte un `a`.
{{% solution "Réponse" %}}
```SQL
SELECT Nom, Prenom
FROM Celebrites
WHERE Pays LIKE '%a%';
```
{{% /solution %}}

#### Exercice d'application

Écrire toutes les commandes correspondant au requêtes ci-dessous pour la base de donnée se trouvant à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Animaux" >}}

1. Rechercher toutes les informations sur les animaux dont le nom commence par la lettre `p`.

2. Rechercher toutes les informations sur les animaux dont le nom se termine par la lettre `e` et qui sont En danger.

3. Rechercher toutes les informations sur les animaux dont le nom comporte la lettre `a` et qui sont Vulnérable. Le résultat doit être trié par nom (ascendant).

4. Afficher le nom de tous les animaux et leur état de préservation.

5. Afficher le nom de tous les animaux vulnérables par ordre décroissant de la vitesse de déplacement.

6. Afficher le nom et la durée de vie moyenne des animaux dont le nom comporte un `e`. L'affichage doit être effectué par durée de vie moyenne croissante.

7. Afficher les nom, durée de vie moyenne et vitesse de déplacement des animaux dont le nom comporte un `o`, par vitesse de déplacement décroissante.

## Modification des entrées d'une base de données

{{% note normal %}}

On reprend, dans cette partie, l'étude de la relation `Celebrites`.

{{% /note %}}

{{% note tip %}}
L'ordre `UPDATE` permet de modifier un enregistrement dans une table. La clause `WHERE` est utilisée pour sélectionner l'enregistrement.
{{% /note %}}

34. Faire en sorte que l'age de l'actrice Margot Robbie soit égal à 29 ans.
{{% solution "Réponse" %}}
```SQL
UPDATE Celebrites
SET Age = 29
WHERE Nom = "Robbie";
```
{{% /solution %}}
Vérifier que la modification a bien été effectuée.

35. Modifier le fichier contenant la base de données de façon à ce que la modification, uniquement effectuée en mémoire vive pour l'instant, soit enregistrée de façon permanente.

36. Le vrai nom de Tom Cruise est Thomas Cruise Mapother IV. Modifier l'entrée dans la base de données.
{{% solution "Réponse" %}}
```SQL
UPDATE Celebrites
SET Nom = "Cruise Mapother IV", prenom = "Thomas"
WHERE Nom = "Cruise";
```
{{% /solution %}}

{{% note tip %}}
L'ordre `DELETE` permet de supprimer un enregistrement d'une table. Si aucune clause `WHERE` n'est utilisée, *tous les enregistrements de la table sont supprimés*.
{{% /note %}}

37. Supprimer l'acteur Tom Holland de la table Celebrites.
{{% solution "Réponse" %}}
```SQL
DELETE FROM Celebrites
WHERE Nom = "Holland";
```
{{% /solution %}}

#### Exercice d'application

Écrire toutes les commandes correspondant au requêtes ci-dessous pour la base de donnée se trouvant à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Superheroes-and-Villains" >}}

1. Écrire une requête qui affiche tous les enregistrements de la table « Superheroes and Villains ».

2. Écrire une requête qui affiche la structure de la table « Superheroes and Villains ».

3. Écrire une requête qui affiche les noms des superheroes femmes.

4. Écrire une requête qui affiche les noms et types (gentil ou méchant) des films X-Men ou Guardians of the Galaxy.

5. Écrire une requête qui affiche tous les noms des personnages par ordre alphabétique.

6. Écrire une requête qui affiche les types des personnages et leurs noms par ordre alphabétique croissant pour les types mais ordre alphabétique décroissant pour les noms.

7. Écrire une requête qui affiche les noms des personnages commençant par la lettre `M`.

8. Écrire une requête qui affiche les noms des personnages se terminant par la lettre `N`.

9. Écrire une requête qui affiche les noms des personnages contenant la lettre `I`.

10. Écrire une requête qui modifie le nom du personnage Groot. Le nouveau nom est Baby Groot. Afficher le résultat de cette requête.

11. Écrire une requête qui supprime l'enregistrement dont le nom est Queen of Hearts. Afficher la table pour vérifier le résultat de la requête.


## Exercice d'application à partir de données réelles et conséquentes

{{% note normal %}}
Le document de travail se trouve à cette adresse : {{< remote "https://repl.it/@dlatreyte/Indicateurs-lycees-en-France" "https://repl.it/@dlatreyte/Indicateurs-lycees-en-France" >}}
{{% /note %}}

La base de donnée contient tous les indicateurs des lycées français présentés sur le site de l’éducation nationale et dont les données sont en accès “libre” sur {{< remote "data.gouv.fr" "https://www.data.gouv.fr/fr/" >}}. La notice descriptive est fournie.

- Écrire 10 requêtes qui vous semblerons utiliser au mieux cette base de données.