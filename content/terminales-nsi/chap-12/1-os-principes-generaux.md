---
title: "Système d'exploitation : Principes généraux"
subtitle: "Chapitre 11,1"
author: ""
type: ""
date: 2021-01-06T16:24:21+04:00
draft: false
toc: true
tags: ["Système d'exploitation", "Ordonnanceur", "Gestionnaire de mémoire", "pile réseau", "gestionnaire de périphériques", "gestionnaire du système de fichiers"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Introduction

1. À l'aide d'un éditeur de texte, écrire le programme Python suivant :
```python
from os.path import getsize
from tkinter.filedialog import askopenfilename

fichier = askopenfilename()
if fichier:
    print("Fichier a pour taille {} octets".format(str(getsize(fichier))))
```
2. Exécuter le programme.

3. À l'aide de la fonction `help` préciser le rôle des fonctions `getsize` du module `os` et `askopenfilename` du module `tkinter.filedialog`.

{{% solution "Réponse" %}}
- `askopenfilename` du module `tkinter.filedialog` crée une boite de dialogue permettant de sélectionner un fichier.\
Plus précisément, cette fonction retourne une chaîne de caractères contenant le chemin du fichier à ouvrir.\
La chaîne de caractères est vide si aucun fichier n'est sélectionné.
- `getsize` du module `os` retourne la taille en octets du fichier passé en argument.
{{% /solution %}}

Ce petit programme permet d'illustrer les différentes *fonctionnalités* d'un **système d'exploitation**. Nous allons les découvrir à travers quelques questions.

4. L'éxécution de ce programme empêche-t-elle d'utiliser en même temps d'autres programmes ?

5. Le comportement précédent est-il du à un effort particulier du programmeur (vous donc) ?

6. Le programme précédent est-il toujours utilisable si le fichier se trouve sur une clé USB ? Sur une autre partition du disque dur ?

7. La durée de réponse du programme dépend-elle de la taille du fichier sélectionné ?

8. Le fonctionnement du programme dépend-il de la taille de l'écran, du fait d'utiliser une souris ou un pavé tactile ?

9. Actuellement, sur votre ordinateur, le nombre de programmes en cours d'exécution est :
    1. Plus grand que le nombre de processeurs ;
    2. Égal au nombre de processeurs ;
    3. Inférieur au nombre de processeurs.

10. Essayer de résumer les quelques fonctionnalités que les questions précédentes ont essayé de faire émerger.
{{% solution "Réponse" %}}

{{% note normal %}}

- Pendant l'exécution du programme, le système continu de fonctionner, **un mécanisme semble donc permettre à plusieurs programmes de s'exécuter en parallèle**.

- Le *nombre de programmes qui s'exécute à un instant donné est supérieur au nombre de processeurs présents sur la machine*.

- **Tous les composants matériels (stockage, affichage, entrées) sont accessibles** sans que le programmeur du programme ait à se préoccuper de quoi que ce soit.

- **Des informations (*méta-données*) semblent accompagner les fichiers**. L'accès à leur taille, par exemple, est indépendant de leur contenu.

{{% /note %}}
{{% /solution %}}

## Système d'exploitation

{{% note tip %}}
Un **système d'exploitation** est *un programme ou un ensemble de programmes dont la fonction est la gestion des ressources matérielles et logicielles d'un ordinateur*.\
Un système d'exploitation permet :
- l'exécution de **processus** ;
- la lecture et l'écriture d'informations ;
- la manipulation de fichiers ;
- à plusieurs usagers et **processus** de se partager les ressources de l'ordinateur « simultanément » ;
- la communication entre ordinateurs ;
- ...
{{% /note %}}

<img src="/terminales-nsi/chap-12/chap-12-1/chap-12-1-1.png" alt="" width="70%" />

{{% note tip %}}
Parmi les différents composants logiciels que l'on trouve dans un système d'exploitation, on identifie :

- L'**ordonnanceur**, qui « décide » quel processus est exécuté à un instant donné par un processeur.

- Le **gestionnaire de mémoire**, qui répartit la mémoire vive entre les différents processus en cours d'exécution.

- Le **gestionnaire du système de fichiers**, qui définit comment sont organiser les informations sur les supports physiques.

- La **pile réseau** qui implémente, entre autres, les protocoles tels que Ethernet, IP, TCP, ...

- Le **gestionnaire de périphériques** qui gère les accès au matériel (carte graphique, disques durs, clavier, souris, écran, imprimante, ...)
{{% /note %}}

{{% note warning %}}
{{< remote "Système d'exploitation sur Wikipedia" "https://fr.wikipedia.org/wiki/Système_d%27exploitation" >}}
{{% /note %}}