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

<img src="/terminales-nsi/chap-11/chap-11-1/empilement_protocoles.png" alt="" width="90%" />
<div style="text-align: right;">
<a href="http://projet.eu.org/pedago/sin/ISN/">http://projet.eu.org/pedago/sin/ISN/</a>
</div>

<!--
<img src="/terminales-nsi/chap-11/chap-11-1/reseau3.png" alt="" width="70%" />
-->

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

{{% note normal %}}

L'encapsulation, en informatique et spécifiquement pour les réseaux informatiques, est un procédé consistant À inclure les données d'un protocole dans un autre protocole.

{{% /note %}}

{{% note normal %}}

Lors d’une transmission, les données traversent chacune des couches au niveau de la machine émettrice. À chaque couche, une information est ajoutée au paquet de données, il s’agit d’un en-tête, ensemble d’informations qui garanti la transmission. Au niveau de la machine réceptrice, lors du passage dans chaque couche, l’en-tête est lu, puis supprimé. Ainsi À la réception, le message est dans son état originel.

À chaque niveau, le paquet de données change d’aspect, car on lui ajoute un en-tête, ainsi les appellations changent suivant les couches :

- le *paquet de données* est appelé **message** au niveau de la **couche application** ;
- le **message** est ensuite encapsulé sous forme de **segment** dans la **couche transport** ;
- le **segment**, une fois encapsulé, prend le nom de **paquet** dans la **couche réseau** ;
- enfin on parle de **trame** au niveau de la **couche liaison** ;
- et de **signal** au niveau de la **couche physique**.

{{% /note %}}

<img src="/terminales-nsi/chap-11/chap-11-1/reseau5.png" alt="" width="110%" />

## Adressage IP

Lorsque l'on veut établir une communication, il est indispensable de posséder trois informations :

1. Le nom de la machine distante,
2. son adresse,
3. la route à suivre pour y parvenir.
Le nom dit « qui » est l'hôte distant, l'adresse nous dit « où » il se trouve et la route « comment » on y parvient.

{{% note normal %}}

Les adresses IP (version 4) sont standardisées sous forme d'un **nombre de 32 bits** (**représenté sous forme de quatre entiers de huit bits, séparés par des points**) qui permet à la fois l'identification de chaque hôte et du réseau auquel il appartient. Le choix des nombres composants une adresse IP n'est pas laissé au hasard, au contraire il fait l'objet d'une attention particulière notamment pour faciliter les **opérations de routage**.  
Chaque adresse IP contient donc deux informations, une **adresse de réseau** et une **adresse d'hôte**. *La combinaison des deux désigne de manière **unique** une machine et une seule sur l'Internet*.

{{% /note %}}

**Remarque :** la version IPv4 du protocole IP ne permet plus de définir un nombre d'adresses utilisables suffisant. Cette version est progressivement remplacée par la version IPv6 qui ne sera pas abordée ici.

### Deux types d'adressage

#### Par classes

C'est l'adressage historique, il est toujours utilisé sur les réseaux privés mais a disparu dans les réseaux public car il engendre la perte d'un grand nombre d'adresses.

| Classe | Nbre bits du masque de sous réseau | Nbre bits de l'adresse hôte | Adresses réseau |
| :---: | :---: | :---: | :---: |
| A | 8 bits commençant obligatoirement par le bit 0 | 24 bits | 1.0.0.0 à 126.0.0.0 |
| B | 16 bits commençant obligatoirement par les bits 10 | 16 bits | 128.0.0.0 à 191.255.0.0 |
| C | 24 bits commençant obligatoirement par les bits 110 | 8 bits | 192.0.0.0 à 223.255.255.0 |
| D | Non défini | Non défini | 224.0.0.0 à 239.255.255.0 |
| E | Non défini | Non défini | 240.0.0.0 à 255.255.255.0 |

#### Remarques

- L'adresse réseau 0.0.0.0 n’existe pas ;
- Le NetID « 127 » est réservée pour les communications en boucle locale (loopback) ;
- La classe D est prévue pour faire du « multicast » ou multipoint.
- La classe E est une classe expérimentale.
- Deux adresses hôtes ne sont pas attribuables :
  - *tous les bits de la partie hôte à 1 : c'est l'**adresse de diffusion** ;*
  - *tous les bits de la partie hôte à 0 : c'est l'**adresse du réseau**.*

1. Calculer le nombre de réseaux différents que l'on peut définir en fonction des classes.
{{% solution "Réponse" %}}

- Classe A : $2^7 = 128$. Le premier bit est fixé 0, on ne peut donc modifier que les sept bits suivants.
- Classe B : $2^{14} = 16384$. Les deux premiers bits sont fixés à 10, on ne peut donc modifier que les 14 bits suivants.
- Classe C : $2^{21} = 209752$. Les trois premiers bits sont fixés à 110, on ne peut donc modifier que les 21 bits suivants.

{{% /solution %}}

2. Calculer le nombre d'hôtes pour chaque réseau.
{{% solution "Réponse" %}}

**Rappel :** Deux configurations sont impossibles pour la partie hôte : tous les bits à 0 (adresse réseau) et tous les bits à 1 (adresse de diffusion).

- Classe A : $2^{24} -2 = 16277214$
- Classe B : $2^{16} -2 = 65534$
- Classe C : $2^{8} -2 = 254$

{{% /solution %}}

### Sans classe (CIDR : classless interdomain routing)

{{% note normal %}}

- Le nombre de bits utilisés pour la partie réseau est accolé à l'adresse IP : $$192.168.0.0/24$$

{{% /note %}}

### Comment différentier les bits utilisés pour la partie réseaux de ceux utilisés pour la partie hôte ?

{{% note normal %}}

Un **masque de sous-réseau** est un masque distinguant les bits d'une adresse IPv4 utilisés pour identifier le sous-réseau de ceux utilisés pour identifier l'hôte.

- *L'adresse du sous-réseau est obtenue en appliquant l'opérateur ET binaire entre l'adresse IPv4 et le masque de sous-réseau*.
- *L'adresse de l'hôte à l'intérieur du sous-réseau est quant à elle obtenue en appliquant l'opérateur ET entre l'adresse IPv4 et le complément à un du masque*.

*On utilise en pratique des masques constitués (sous leur forme binaire) d'une suite de 1 suivis d'une suite de 0 (il y a donc 32 masques réseau possibles).*
{{% /note %}}

3. Déterminer les adresses réseau et hôte à partir de l'adresse 192.168.1.2/24.
{{% solution "Réponse" %}}

- **Adresse réseau :** il faut réaliser l'opération : 192.168.1.2 & 255.255.255.0

$$
\def\arraystretch{1.5}
\begin{array}{cc}
    & 11000000.10101000.00000001.00000010 \\\\
   \text{ET} & 11111111.11111111.11111111.00000000 \\\\ \hline
   \text{=} & 11000000.10101000.00000001.00000000
\end{array}
$$
soit 192.168.1.0

- **Adresse hôte :** soit on effectue un & logique avec le complément à 1 du masque, doit on cherche le nombre formé par les bits non retenus par la partie réseau.

$$
\def\arraystretch{1.5}
\begin{array}{cc}
    & 11000000.10101000.00000001.00000010 \\\\
   \text{ET} & 00000000.00000000.00000000.11111111 \\\\ \hline
   \text{=} & 00000000.00000000.00000000.00000010
\end{array}
$$
soit 0.0.0.2

{{% /solution %}}
