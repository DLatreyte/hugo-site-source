---
title: "Les réseaux"
subtitle: ""
author: ""
type: ""
date: 2020-11-26T06:04:09+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
layout: "single"
---

## Protocoles de routage

Dans un réseau, les routeurs jouent un rôle essentiel dans la transmission des paquets sur internet : les paquets sont routés individuellement par des algorithmes. Les pertes logiques peuvent être compensées par des protocoles reposant sur des accusés de réception ou des demandes de renvoi, comme TCP.

### Au programme

| Contenus | Capacités attendues | Commentaire |
|:----:|:----:|:----:|
| Protocoles de routage. | Identifier, suivant le protocole de routage utilisé, la route empruntée par un paquet. | <br />- En mode débranché, les tables de routage étant données, on se réfère au nombre de sauts (protocole RIP) ou au coût des routes (protocole OSPF).<br />- Le lien avec les algorithmes de recherche de chemin sur un graphe est mis en évidence.

### Documents

- **Doc.** [*Modélisation des réseaux*](1-modelisation-reseaux)

- **Doc.** [*Adressage IP*](2-ip)

- **Doc.** [*Analyse du protocole de transport TCP*](3-analyse-tcp)

- **Doc.** [*Simulation de réseaux*](4-simulation-reseau)

- **Doc.** [*Le routage entre réseaux IP*](5-routage)

## Sécurisation des communications

La protection des données sensibles échangées est au cœur d’internet. Les notions de chiffrement et de déchiffrement de paquets pour les communications sécurisées sont explicitées.

### Au programme

| Contenus | Capacités attendues | Commentaire |
| ---- | ---- | ---- |
| - Sécurisation des communications. | - Décrire les principes de chiffrement symétrique (clef partagée) et asymétrique (avec clef privée/clef publique).<br />- Décrire l’échange d’une clef symétrique en utilisant un protocole asymétrique pour sécuriser une communication HTTPS. |- Les protocoles symétriques et asymétriques peuvent être illustrés en mode débranché, éventuellement avec description d’un chiffrement particulier.<br />- La négociation de la méthode chiffrement du protocole SSL (Secure Sockets Layer) n’est pas abordée. |

### Documents

- **Doc.** [*Cours*](https://www.remnote.com/a/25022023/63fc4b5d35d23643c0cbda0c)

- **Doc.** [*Réalisation d'un chiffrement symétrique*](7-chiffrement-symétrique)
