---
title: "Modélisation des réseaux"
subtitle: ""
author: ""
type: ""
date: 2020-11-26T06:13:06+04:00
draft: false
toc: true
tags: ["Réseaux", "IP", "Adressage", "TCP", "Ethernet"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---


## Vocabulaire

{{% note normal %}}

- **Réseau :** ensemble d’équipements interconnectés (liaisons mais aussi protocoles).

- **Un internet :** réseau informatique dont le protocole de routage/adressage est IP (Internet Protocol).

- **L’Internet :** réseau des réseaux —plus grand réseau internet

  - Tous les réseaux internet ne font pas partie de l’Internet.
  - Le WEB (World Wide Web) est seulement une composante de l’Internet.

{{% /note %}}

## Structure d'un internet

Pour transmettre des données d’un équipement vers un autre, il faut envoyer un signal sur un support de communication. Il est cependant  **impossible de relier directement entre eux tous les équipements** qui souhaiteraient interagir, surtout dans le cadre d’un réseau mondialisé. *Le nombre de liaisons serait trop important et les liaisons seraient trop longues (affaiblissement physique du signal)*.

<img src="/terminales-nsi/chap-11/chap-11-1/reseau1.png" alt="" width="90%" />

L’idée retenue consiste à faire communiquer des systèmes terminaux en les connectant à une infrastructure spécifique constituée de liens de communication (câbles, paires torsadées, câbles électriques, fibres optiques ou encore l’air pour des liaisons sans fil) et des équipements spécifiques pour relayer les données (*points d’accès*, *modem*, *antennes relais*, *routeurs*, *commutateurs*, etc.). **Ces équipements interconnectés les uns aux autres permettent ainsi de diminuer le nombre de liaisons et leur distance et d’interconnecter tous les systèmes terminaux (ou hôtes)**.  
Chaque type de lien de communication a des caractéristiques propres en termes de **débit**, **bande passante**, **résistance aux interférences électromagnétiques**, **facilité d’installation**, **coût**, etc.

<img src="/terminales-nsi/chap-11/chap-11-1/reseau2.png" alt="" width="100%" />

## Commutation de paquets

{{% note normal %}}

La communication entre ordinateurs est basée sur la **commutation de paquets** :

- Les messages sont découpés en paquets de taille limitée ;
- Chaque paquet est envoyé indépendamment des autres.

{{% /note %}}

**Remarque :** Nous reviendrons sur la commutation de paquets plus tard.

## Les composants des réseaux

L’architecture réseau définit les éléments dans un réseau, c’est-à-dire les types de nœuds dans le réseau.

- Un **réseau internet** est composé :
  - De **concentrateurs** (network hub) (*matériel obsolète*) ;
  - De **points d'accès** (Wifi) ;
  - De **commutateurs** (network switch) ;
  - De **routeurs** ;
  - De media de transport des signaux (câbles de cuivre, fibres optiques, air, )
  - De machines utilisateurs (stations, serveurs, téléphones, etc.).

## Protocole de communication

### Qu’est-ce qu’un protocole ?

Imaginons que nous souhaitions envoyer une lettre à un ami. Quelles sont les différentes étapes pour pouvoir faire parvenir une lettre par courrier postal ?

### Un protocole de communication est un accord entre deux parties sur la manière de communiquer

{{% note normal %}}

Un **protocole de communication** définit :

- Le format des messages échangés ;
- Comment les messages sont échangés.

{{% /note %}}

### Qu’est-ce que cela implique pour les réseaux de communications ?

Il est nécessaire de définir :

- dans quel sens la communication s'effectue ;
- comment on s'assure de sa fiabilité ;
- comment le séquencement des messages doit être effectué ;
- comment le contrôle des erreurs peut être effectué ;
- quelle doit être la longueur du message ;
- quelle est la vitesse de transmission ;
- etc.

## Architecture logique en couches

{{% note normal %}}

L'échange d'informations entre deux ordinateurs est un processus complexe. **On décompose la tâche de transmission des données en plusieurs sous-tâches indépendantes**.

{{% /note %}}

**Remarque :** chaque sous-tâche correspond à une couche dans l'architecture en couches.

### Hiérarchie des protocoles

<img src="/terminales-nsi/chap-11/chap-11-1/reseau3.png" alt="" width="70%" />

### Modèle OSI

<img src="/terminales-nsi/chap-11/chap-11-1/reseau4.png" alt="" width="110%" />

### Rôle des couches dans le modèle OSI

{{% note normal %}}

#### Couche « Physique »

Transmission des **bits** sur le support physique (spécification des connecteurs, détermination des caractéristiques électriques des circuits, etc.).

#### Couche « Liaison de données »

Transmission fiable de **trames** sur une connexion physique entre deux nœuds qui partagent un **même support physique**.

#### Couche « Réseau »

Transmission des **paquets/datagrammes** d'une source vers une destination en passant par plusieurs nœuds intermédiaires (**adressage**, **routage**, **contrôle de congestion**).

#### Couche « Transport »

Transmission de *bout-en-bout* des **segments**, avec fiabilité et efficacité (contrôle de flux, reprise sur erreur, optimisation).

{{% /note %}}

### Encapsulation des protocoles

<img src="/terminales-nsi/chap-11/chap-11-1/reseau5.png" alt="" width="110%" />
