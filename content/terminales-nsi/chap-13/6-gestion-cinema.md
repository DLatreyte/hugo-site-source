---
title: "Gestion d'une salle de cinéma"
subtitle: "Chapitre 12,6"
author: ""
type: ""
date: 2021-02-09T05:50:34+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: false
auto_numbering: true
---

> L'objectif de cette séance est de mettre en œuvre tous les concepts du chapitre.

La base de donnée accessible à {{< remote "cette adresse" "https://repl.it/@dlatreyte/Cinema" >}} simule de façon simplifiée la gestion d'un cinéma.

1. Étudier la structure de chacune des relations de la base et établir son schéma relationnel.\
En particulier, faire apparaître les clés primaires et les clés étrangères.
{{% solution "Réponse" %}}
- Quelles sont les tables de la base ?
```SQL
.tables
```

- Quelle est la structure de chacune de ces relations ?
```SQL
pragma table_info('film');
pragma table_info('projection');
pragma table_info('categorie');
```

**Rappel :** ces commandes sont spécifiques à SQLite et ne sont pas au programme. Il est cependant utile de les connaître.
{{% /solution %}}

2. Afficher le contenu de chacune des relations.
{{% solution "Réponse" %}}
```SQL
SELECT *
FROM film;

SELECT *
FROM projection;

SELECT *
FROM categorie;
```
{{% /solution %}}

3. Quelles sont les différentes catégories de film ?
{{% solution "Réponse" %}}
```SQL 
SELECT codecat, libcat
FROM categorie;
```
{{% /solution %}}

4. Quelles sont les noms des salles du cinéma triés dans l'ordre alphabétique ?
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT salle
FROM projection
ORDER BY salle;
```
{{% /solution %}}

5. Quels sont les films (numéro, titre, durée) projetés au cinéma ?
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT film.numfilm, titre, duree
FROM film, projection
WHERE film.numfilm = projection.numfilm;
```
ou
```SQL
SELECT DISTINCT f.numfilm, titre, duree
FROM film f, projection p
WHERE f.numfilm = p.numfilm;
``` 
ou
```SQL

```
{{% /solution %}}

6. Quels sont les salles qui ont des séances à 11h00 ?
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT salle
FROM projection
WHERE seance = '11h00';
```
{{% /solution %}}

7. Quelle est le titre et la durée du film numéro 20 ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre, duree
FROM film
WHERE numfilm = '20';
```
{{% /solution %}}

8. Quelle est le titre et la durée (en heure) du film numéro 20 ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre, (duree/60)
FROM film
WHERE numfilm = '20';
```
{{% /solution %}}

9. Quels sont les noms des films diffusés en salle nord qui durent entre 60 et 120 minutes ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre
FROM film, projection
WHERE film.numfilm = projection.numfilm
AND salle = 'Nord'
AND duree BETWEEN '60' AND '120';
```
{{% /solution %}}

10. Combien il y a-t-il de films dans la base (dans une colonne nommée : Total films) ?
{{% solution "Réponse" %}}
```SQL 
SELECT COUNT(*) AS 'Total films'
FROM film;
```
{{% /solution %}}

11. Combien il y a-t-il de films produits par Universal dans la base ?
{{% solution "Réponse" %}}
```SQL 
SELECT production, COUNT(numfilm) AS 'Nbre films'
FROM film
WHERE production = (SELECT production 
                    FROM film 
                    WHERE production = "Universal");
```
{{% /solution %}}

12. Combien il y a-t-il de films dans la catégorie documentaire (libellé catégorie, nombre de films) ?
{{% solution "Réponse" %}}
```SQL 
SELECT libcat, COUNT(numfilm) AS 'Nbre films'
FROM film f, categorie c
WHERE f.codecat = c.codecat
AND c.libcat = (SELECT libcat 
                FROM categorie
                WHERE libcat = "documentaire");
```
{{% /solution %}}

13. Quels sont les titres des films de 140 minutes et produits par UGC ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre
FROM film
WHERE duree = '140'
AND production = 'UGC';
```
{{% /solution %}}

14. Quels sont les titres des films commençant par C et L (triés par ordre alphabétique) ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre
FROM film
WHERE titre LIKE 'C%'
OR titre LIKE 'L%'
ORDER BY titre;
```
{{% /solution %}}

15. Quels sont les titres des films qui ne commencent pas par la lettre U (triés alphabétiquement) ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre
FROM film
WHERE titre NOT LIKE 'U%'
ORDER BY titre;
```
{{% /solution %}}

16. Quels sont les titres et la durée des films qui ne sont pas diffusés en salle nord ?
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT titre, duree
FROM film, projection
WHERE film.numfilm=projection.numfilm
AND salle != 'Nord';
```
{{% /solution %}}

17. Quels sont les titres des films diffusés à 11h dans les salles Nord ou Centrale ? 
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT titre
FROM film, projection
WHERE film.numfilm=projection.numfilm
AND seance LIKE '11h%'
AND salle IN ('Nord','Centrale');
```
{{% /solution %}}

18. Quelle est la durée moyenne des films de la base ?
{{% solution "Réponse" %}}
```SQL 
SELECT AVG(duree)
FROM film ;
```
{{% /solution %}}

19. Quelle est la séance du film diffusé le plus tôt dans la journée du 18/11 ?
{{% solution "Réponse" %}}
```SQL 
SELECT MIN(seance)
FROM projection
WHERE date='2005/11/18';
```
{{% /solution %}}

20. Quel est le numéro et le titre des films qui ont la même durée que le film numéro 71 ?\
Utiliser deux requêtes imbriquées.
{{% solution "Réponse" %}}
```SQL 
SELECT numfilm, titre
FROM film
WHERE duree = (SELECT duree
               FROM film
               WHERE numfilm='71');
```
{{% /solution %}}

21. Quel le numéro et le titre des films de la même catégorie que Super Mondet XII ?\
Utiliser deux requêtes imbriquées.
{{% solution "Réponse" %}}
```SQL 
SELECT numfilm, titre
FROM film
WHERE codecat = (SELECT codecat
                 FROM film
                 WHERE titre = 'Super Mondet XII');
```
{{% /solution %}}

22. Quels sont les titres des films diffusés aux horaires suivants : 11h00, 13h10 et 14h50 ?
{{% solution "Réponse" %}}
```SQL 
SELECT titre
FROM film f, projection p
WHERE f.numfilm = p.numfilm
AND seance IN ('11h00','13h10','14h50');
```
{{% /solution %}}

23. Quels sont les films (numéro et titre) plus longs que la moyenne ?\
Utiliser deux requêtes imbriquées.
{{% solution "Réponse" %}}
```SQL 
SELECT numfilm, titre
FROM film
WHERE duree > (SELECT AVG(duree)
               FROM film);
```
{{% /solution %}}

24. Quels films (numéro, titre, salle et séance) sont programmés aux mêmes horaires ?\
Utiliser une autojointure.
{{% solution "Réponse" %}}
```SQL 
SELECT DISTINCT p1.numfilm, p1.salle, p1.seance
FROM projection p1, projection p2
WHERE p1.seance = p2.seance
AND p1.numfilm! = p2.numfilm;
```
{{% /solution %}}

25. Quelle est le titre, la salle, la séance et la durée (en heure) des films projeté. En utilisant la fonction ROUND(<champ ou formule>,<nb décimales>) ?{{% solution "Réponse" %}}
```SQL 
SELECT titre, salle, seance, ROUND(duree/60,1) AS 'duree'
FROM film f, projection p
WHERE f.numfilm = p.numfilm;
```
{{% /solution %}}

26. Quels sont les films (numéro et titre) qui n’ont pas été diffusés ?
{{% solution "Réponse" %}}
```SQL 

```
{{% /solution %}}

27. Quels sont les trois films qui sont les plus diffusés ? cc) Quel est le film le plus diffusé ?
{{% solution "Réponse" %}}
```SQL 

```
{{% /solution %}}

On souhaite maintenant ajouter l'attribut `tarif` à la relation `projection`. Exécuter la commande suivante :
```SQL
ALTER TABLE projection ADD tarif float;
``` 

28. Vérifier que la structure de la relation `projection` a bien été modifiée.

On fait la supposition que le tarif des films dépend du film, de la salle, de la séance et de la date de projection. Le tarif exprime le tarif de base.

29. Mettre à jour la table projection en fixant un tarif de base à 5 € pour la salle nord, 8 € pour la salle centrale, 6.5 € pour la salle sud.
{{% solution "Réponse" %}}
```SQL 
UPDATE projection
SET tarif = '5.00'
WHERE sale = 'nord';

UPDATE projection
SET tarif = '8.00'
WHERE sale = 'centrale';

UPDATE projection
SET tarif = '6.50'
WHERE sale = 'sud';
```
{{% /solution %}}

30. Une erreur s’est glissée dans la table projection : l’horaire de 13h10 est à remplacé par 19h30 pour la salle sud.
{{% solution "Réponse" %}}
```SQL 
UPDATE projection
SET seance = '19h30'
WHERE seance = '13h10';
```
{{% /solution %}}

31. Mettre à jour la table projection en majorant de 1 € les films dont les séances sont à 14h50 ; de 2 € pour les séances à 19h30.
{{% solution "Réponse" %}}
```SQL 
UPDATE projection
SET tarif = tarif+1
WHERE seance = '14h50';

UPDATE projection
SET tarif = tarif+2
WHERE seance = '19h30';
```
{{% /solution %}}

32. Mettre à jour la table projection en majorant le 10% les films en projection le 18/11.
{{% solution "Réponse" %}}
```SQL 
UPDATE projection
SET tarif = tarif * 1.1
WHERE date = '2005/11/18';
```
{{% /solution %}}

33. Mettre à jour la table projection en majorant de 25% les films n°10 et n°50.
{{% solution "Réponse" %}}
```SQL 
UPDATE projection
SET tarif = tarif * 1.25
WHERE numfilm = '10'
OR numfilm = '50';
```
{{% /solution %}}

34. Mettre à jour la table film en ajoutant les films suivants :
    - 89, Les fourmis de l’espace (documentaire), produit par UGC, 130 minutes.
    - 90, Jet Set (comédie), produit par Paramounth, 100 minutes.
{{% solution "Réponse" %}}
```SQL 
INSERT INTO film
VALUES ('89','Les fourmis de l’espace','130','UGC','DOCU');
INSERT INTO film
VALUES ('90','Jet Set','100','Paramounth','COMD');
```
{{% /solution %}}

35. Effacer les enregistrements en date du 17-11-2005.
{{% solution "Réponse" %}}
```SQL 
DELETE FROM projection
WHERE date = '2005/11/17';
```
{{% /solution %}}

 