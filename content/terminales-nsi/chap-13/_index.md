---
title: "Bases de données"
subtitle: "Chapitre 12"
author: ""
type: ""
date: 2021-01-18T17:54:59+04:00
draft: false
toc: true
tags: []
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
layout: "single"
---

Le développement des traitements informatiques nécessite la manipulation de données de plus en plus nombreuses. Leur organisation et leur stockage constituent un enjeu essentiel de performance. Le recours aux bases de données relationnelles est aujourd’hui une solution très répandue. Ces bases de données permettent d’organiser, de stocker, de mettre à jour et d’interroger des données structurées volumineuses utilisées simultanément par différents programmes ou différents utilisateurs. Cela est impossible avec les représentations tabulaires étudiées en classe de première.

Des systèmes de gestion de bases de données (SGBD) de très grande taille (de l’ordre du pétaoctet) sont au centre de nombreux dispositifs de collecte, de stockage et de production d’informations. L’accès aux données d’une base de données relationnelle s’effectue grâce à des requêtes d’interrogation et de mise à jour qui peuvent par exemple être rédigées dans le langage SQL (Structured Query Language). Les traitements peuvent conjuguer le recours au langage SQL et à un langage de programmation.

Il convient de sensibiliser les élèves à un usage critique et responsable des données.

## Au programme

| Contenus | Capacités attendues | Commentaire |
|:---- |:---- |:---- |
| - Modèle relationnel : relation, attribut, domaine, clef primaire, clef étrangère, schéma relationnel. | - Identifier les concepts définissant le modèle relationnel. | - Ces concepts permettent d’exprimer les contraintes d’intégrité (domaine, relation et référence).|
| - Base de données relationnelle. | - Savoir distinguer la structure d’une base de données de son contenu. Repérer des anomalies dans le schéma d’une base de données. | - La structure est un ensemble de schémas relationnels qui respecte les contraintes du modèle relationnel.<br />- Les anomalies peuvent être des redondances de données ou des anomalies d’insertion, de suppression, de mise à jour.<br />- On privilégie la manipulation de données nombreuses et réalistes.|
| - Système de gestion de bases de données relationnelles. | - Identifier les services rendus par un système de gestion de bases de données relationnelles : persistance des données, gestion des accès concurrents, efficacité de traitement des requêtes, sécurisation des accès. | - Il s’agit de comprendre le rôle et les enjeux des différents services sans en détailler le fonctionnement. |
| - Langage SQL : requêtes d’interrogation et de mise à jour d’une base de données. | - Identifier les composants d’une requête.<br />- Construire des requêtes d’interrogation à l’aide des clauses du langage SQL : SELECT, FROM, WHERE, JOIN.<br />- Construire des requêtes d'insertion et de mise à jour à l'aide de : UPDATE, INSERT, DELETE. | - On peut utiliser DISTINCT, ORDER BY ou les fonctions d’agrégation sans utiliser les clauses GROUP BY et HAVING. |

## Documents

- **Chap. 12,1 :** [*Introduction aux bases de données*](1-introduction-bases-de-donnees)

- **Chap. 12,2 :** [*Le modèle Entité/Association*](2-entite-association)

- **Chap. 12,3 :** [*Du schéma entités/associations au schéma relationnel*](3-vers-modele-relationnel)

- **Chap. 12,4 :** [*Le langage SQL : Le langage de manipulation de données (LMD)*](4-sql-lmd)

- **Chap. 12,5 :** [*Le langage SQL : Le langage de manipulation de données (LMD), Compléments*](5-sql-lmd-avance)

- **Chap. 12,6 :** [*Gestion d'une salle de cinéma*](6-gestion-cinema)

- **Chap. 12,7 :** [*SQL Murder Mystery*](7-murder-mystery)

- **Chap. 12,8 :** [*Emprunt de livres dans un CDI*](8-cdi)


