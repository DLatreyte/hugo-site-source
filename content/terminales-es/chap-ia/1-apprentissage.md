---
title: "Teachable Machine : reconnaître une position"
subtitle: ""
author: ""
type: ""
date: 2023-03-01T22:35:36+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de cette séance est de montrer comment on peut apprendre à un **modèle d'apprentissage** à reconnaître une position. Le logiciel utilisé est Teachable Machine et **l'apprentissage aura pour objectif de faire en sorte que le logiciel puisse déterminer si on se tient droit, ou si on est incliné vers la gauche ou vers la droite**.

## Préparation

1. Accéder au <a href="https://teachablemachine.withgoogle.com" target="_blank">logiciel en ligne</a>

2. Cliquer sur « Commencer ».

3. Choisir « Projet posture ».

## Entraînement

Trois postures doivent être définies :
    - « Sans inclinaison »,
    - « Inclinaison à gauche »,
    - « Inclinaison à droite ».

4. Renommer la classe d'apprentissage « Class 1 » en « Sans inclinaison » et la classe d'apprentissage « Class 2 » en « Inclinaison à gauche ».

5. Ajouter une classe d'apprentissage et la renommer en « Inclinaison à droite ».

6. Sélectionner la webcam de la classe « Sans inclinaison ».  
Se rendre dans la partie « configuration » (icône en forme de roue dentellée) et désactiver « Maintenir pour enregistrer ».  
Enregistrer les paramètres.

7. Assis sur sa chaise, se tenir droit et lancer l'enregistrement.  
Il est possible d'un petit peu bouger pendant l'enregistrement.

8. Sélectionner la webcam de la classe « Inclinaison à gauche ».  
Lancer l'enregistrement et effectuer des petits mouvement en se penchant vers la gauche, en restant assis sur sa chaise.  
*Attention à toujours rester dans le champ de la caméra.*

9. Sélectionner la webcam de la classe « Inclinaison à droite ».  
Lancer l'enregistrement et effectuer des petits mouvement en se penchant vers la droite, en restant assis sur sa chaise.  
*Attention à toujours rester dans le champ de la caméra.*

10. Dans la partie « Entraînement », cliquer sur « Entraîner le modèle » et attendre que l'apprentissage se termine.

11. Tester le modèle. Ce modèle fonctionne-t-il correctement ?

12. Se lever et reculer, tout en restant dans le champ de la caméra. Effectuer de nouveaux tests. Le modèle fonctionne-t-il toujours correctement ?

13. Comment faire en sorte que le modèle fonctionne aussi si on est debout ?

14. Effectuer les modifications dans l'entraînement du modèle et le tester à nouveau.

15. Se faire remplacer par une autre personne. Le modèle fonctionne-t-il toujours aussi bien ?

## Ouverture

16. Expliquer comment on pourrait utiliser ce logiciel pour lui apprendre à déterminer si une banane est trop verte pour être mangée, est mûre ou est sur le point de ne plus être comestible. Donner en particulier les classes d'apprentissage qu'il faudrait utiliser.
