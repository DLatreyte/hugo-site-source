---
title: "Emprunt de livres dans un CDI"
subtitle: "Chapitre 12.8"
author: ""
type: ""
date: 2022-01-19T04:45:20+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}

Le fichier de travail se trouve à cette <a href="https://replit.com/@dlatreyte/CDI-eleves#main.sql" target="_blank">adresse</a>.

{{% /note %}}
La base de données correspond à la modélisation d’emprunt de livres dans un CDI&nbsp;:

- Chaque élève d’un lycée peut emprunter des livres au CDI, les données concernants ces livres et les emprunts en cours sont stockés dans une base de données.

- Les auteurs ainsi que les éditeurs figurent également dans cette base.

## Travail préalable

0. Déterminer la structure de la base de données et indiquer son schéma relationnel.

## Requêtes simples

Donner le code SQL de chacune des requêtes suivantes.

1. Afficher tous les noms des auteurs.
{{% solution "Réponse" %}}

```sql
SELECT nom 
FROM auteurs;
```

{{% /solution %}}

2. Afficher le titre de tous les livres.
{{% solution "Réponse" %}}

```sql 
SELECT titre FROM livres;
```

{{% /solution %}}

3. Afficher les noms des classes du lycée sans doublon.
{{% solution "Réponse" %}}

```sql
SELECT classe FROM eleves;
```

{{% /solution %}}

4. Afficher les titres des livres et les annees d’édition classé selon l’année.
{{% solution "Réponse" %}}

```sql
SELECT titre, annee
FROM livres
ORDER BY annee ASC;
```

{{% /solution %}} 

5. Quels sont les livres dont le titre contient le mot Astérix&nbsp;?
{{% solution "Réponse" %}}

```sql

``` 

{{% /solution %}}

## Expressions et fonctions

Donner le code SQL de chacune des requêtes suivantes.

6. Afficher les noms et prénoms des élèves de la classe 1-G1.
{{% solution "Réponse" %}}

```sql
SELECT nom, prenom
FROM eleves
WHERE classe = '1-G1';
```

{{% /solution %}}

7. Afficher les titres des livres publiés après 2000.
{{% solution "Réponse" %}}

```sql
SELECT titre
FROM livres
WHERE annee > 2000;
```

{{% /solution %}}

8. Afficher les isbn des livres dont la date retour est déjà passée (au 25 octobre 2020).
{{% solution "Réponse" %}}

```sql
SELECT isbn
FROM emprunt
WHERE date_ret > 2020-10-25;
```

{{% /solution %}}

9. Combien d’auteurs sont présents dans la base de données&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT COUNT(*)
FROM auteurs;
```

{{% /solution %}}

10. Quelle est l’annee d’édition du ou des livre(s) le(s) plus ancien(s)&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT MIN(annee)
FROM livres;
```

{{% /solution %}}

## Requêtes imbriquées

Donner le code SQL de chacune des requêtes suivantes.

11. Afficher les titres des livres empruntés.
{{% solution "Réponse" %}}

```sql
SELECT titre
FROM livres
WHERE isbn IN (SELECT isbn
    FROM emprunt);
```

{{% /solution %}}

12. Afficher, sans doublon, le nom et prénom des élèves qui ont emprunté au moins un livre.
{{% solution "Réponse" %}}

```sql
SELECT DISTINCT nom, prenom
FROM eleves
WHERE num_etu IN (SELECT num_etu
    FROM emprunt);
```

{{% /solution %}}

13. Afficher, sans doublon, le nom et prénom des élèves qui ont emprunté au moins un livre avec une date retour dépassée (au 25 octobre 2020).
{{% solution "Réponse" %}}

```sql
SELECT DISTINCT nom, prenom
FROM eleves
WHERE num_etu IN (SELECT num_etu
    FROM emprunt
    WHERE date_ret > '2020-10-25');
```

{{% /solution %}}

14. Quels sont les editeurs à avoir édité un livre contenant Astérix dans le titre&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT nom 
FROM editeurs
WHERE siret IN (SELECT siret
    FROM livres
    WHERE titre LIKE "%Astérix%");
```

{{% /solution %}}

15. Quel est le titre du ou des livre(s) le(s) plus ancien(s)&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT titre 
FROM livres
WHERE annee IN (SELECT min(annee)
    FROM livres);
```

{{% /solution %}}

## Jointures

Donner le code SQL de chacune des requêtes suivantes en utilisant la clause `JOIN`.

16. Afficher les titres des livres empruntés.
{{% solution "Réponse" %}}

```sql
SELECT titre
FROM livres 
JOIN emprunt
ON livres.isbn = emprunt.isbn;
```

{{% /solution %}}

17. Afficher, sans doublon, le nom et prénom des élèves qui ont emprunté au moins un livre.
{{% solution "Réponse" %}}

```sql
SELECT DISTINCT nom, prenom
FROM eleves 
JOIN emprunt 
ON eleves.num_etu = emprunt.num_etu;
```

{{% /solution %}}

18. Afficher, sans doublon, le nom et prénom des élèves qui ont emprunté au moins un livre avec une date retour dépassée (au 25 octobre 2020).
{{% solution "Réponse" %}}

```sql
SELECT nom, prenom
FROM eleves
JOIN emprunt ON eleves.num_etu = emprunt.num_etu
WHERE date_ret > '2020-10-25';
```

{{% /solution %}}

19. Qui est l’auteur du livre 1984&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT nom 
FROM auteurs
JOIN ecrire ON auteurs.a_id = ecrire.a_id
JOIN livres ON ecrire.isbn = livres.isbn
WHERE livres.titre = "1984";
```

{{% /solution %}}

20. Afficher les titres des livres écrit par Pierre Boulle.
{{% solution "Réponse" %}}

```sql
SELECT titre 
FROM livres
JOIN ecrire ON livres.isbn = ecrire.isbn
JOIN auteurs ON ecrire.a_id = auteurs.a_id
WHERE auteurs.nom = 'Pierre Boulle';
```

{{% /solution %}}

21. Combien de livres ont été écrit par Isaac Asimov&nbsp;?
{{% solution "Réponse" %}}

```sql
SELECT COUNT(livres.isbn)
FROM livres 
JOIN ecrire ON livres.isbn = ecrire.isbn
JOIN auteurs ON ecrire.a_id = auteurs.a_id
WHERE auteurs.nom = "Isaac Asimov";
``` 

ou, meilleurs,

```sql 
SELECT COUNT(isbn)
FROM ecrire
JOIN auteurs on ecrire.a_id = auteurs.a_id
WHERE auteurs.nom = "Isaac Asimov";
```

{{% /solution %}}

22. Afficher les noms des editeurs ayant édité un écrit par Barjavel.
{{% solution "Réponse" %}}

```sql
SELECT DISTINCT editeurs.nom 
FROM editeurs
JOIN livres ON editeurs.siret = livres.siret
JOIN ecrire ON livres.isbn = ecrire.isbn
JOIN auteurs ON ecrire.a_id = auteurs.a_id
WHERE auteurs.nom like '%Barjavel%';
```

{{% /solution %}}
