---
title: "SQL Murder Mystery"
subtitle: "Chapitre 12,7"
author: ""
type: ""
date: 2021-02-07T07:00:01+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}
- Les fichiers de travail se trouvent à cette adresse : {{< remote "https://replit.com/@dlatreyte/Murder-Mystery#main.sql" "https://replit.com/@dlatreyte/Murder-Mystery" >}}

- Les documents de référence se trouvent à cette adresse : {{< remote "https://github.com/NUKnightLab/sql-mysteries" "https://github.com/NUKnightLab/sql-mysteries" >}}
{{% /note %}}

## Task

A crime has taken place and the detective needs your help. The detective gave you the crime scene report, but you somehow lost it. You vaguely remember that the crime was a ​murder​ that occurred sometime on ​Jan.15, 2018​ and that it took place in ​SQL City​. All the clues to this mystery are buried in a huge database, and you need to use SQL to navigate through this vast network of information. Your first step to solving the mystery is to retrieve the corresponding crime scene report from the police department’s database. Take a look at the SQL reference to learn how to do this! From there, you can use your SQL skills to find the murderer.

- If you just want to solve the mystery, go to {{< remote "mystery.knightlab.com" "http://mystery.knightlab.com" >}} 
- If you're new to SQL, you may want to start at our {{< remote "walkthrough" "http://mystery.knightlab.com/walkthrough.html" >}}. It won't teach you everything about SQL, but it should teach you all that you need to solve the mystery.


## Entity Relationship Diagram of the database

<img src="/terminales-nsi/chap-13/chap-13-5/schema.png" alt="" width="" />

## Checking the Solution

Write the following queries in your SQL environment to check whether you've found the right murderer:
```SQL
INSERT INTO solution VALUES (1, "Insert the name of the person you found here");
SELECT value FROM solution;
```
