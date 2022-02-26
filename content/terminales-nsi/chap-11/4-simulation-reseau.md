---
title: "Simulation de réseaux"
subtitle: "Chapitre 10,4"
author: ""
type: ""
date: 2020-12-06T04:35:41+04:00
draft: false
toc: true
tags: ["Réseaux", "IP", "Adressage", "TCP", "Ethernet", "Routage"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de cette séance est de mettre en pratique les concepts rappelés lors des séances précédentes et d'introduire la notion de routage.

{{% note normal %}}
- Télécharger le logiciel {{< remote "Filius" "https://www.lernsoftware-filius.de/Herunterladen" >}}
- Choisir le paquet « Zip » pour OSX ou Linux (hors Ubuntu). Pour Windows, on peut choisir « Windows » ou « Zip ».
{{% /note %}}

## Construction d'un réseau local

1. En `mode conception`, créer le réseau local suivant :
<img src="/terminales-nsi/chap-11/chap-11-4-1.png" alt="" width="" />

1. Configurer chaque ordinateur : `Mode conception` $\longrightarrow$ `Clic droit` sur l'ordinateur $\longrightarrow$ `Configurer`.

1. Sélectionner « Utiliser l'adresse IP comme nom ».

1. Ralentir les animations de façon à pouvoir visualiser le chemin des segments : ramener le curseur placé juste à droite du bouton `Simulation` à 10 ou 0&nbsp;%.

1. Sur l'ordinateur portable installer les outils en ligne de commande : `Clic gauche` $\longrightarrow$ `Installation des logiciels` $\longrightarrow$ `Ligne de commande` $\longrightarrow$ `Appliquer les modifications`.

1. À quoi correspond la table `arp` ? 
{{% solution "Réponse" %}}
La table `arp` donne la correspondance entre les adresses MAC, seules utilisées sur un réseau local, et les adresses IP, définies par les administrateurs réseau.
{{% /solution %}}

7. Lancer la commande `arp -a` et examiner son retour. Que nous apprend-elle ?
{{% solution "Réponse" %}}
<center>

| Adresse IP | Adresse MAC |
|:----:|:----:|
| 255.255.255.255 | FF:FF:FF:FF:FF:FF |

</center>
Par défaut, on a juste l'adresse de diffusion.
{{% /solution %}}

8. Lancer la commande `ping 192.168.0.11`. Que permet de visualiser cette commande ?
{{% solution "Réponse" %}}
La commande `ping` permet de tester si une liaison réseau vers une machine que l'on sait allumée et fonctionnelle existe ou pas. Des paquets sont envoyés vers cette dernière ; elle les retourne alors tels quels (echo).
{{% /solution %}}

9. Décrire la circulation des segments observable lors de la simulation.
{{% solution "Réponse" %}}
- Dans un premier temps tous les cables s'allument, ce qui témoigne d'un mécanisme de **diffusion**.
- Par la suite, seuls les cables reliant les deux machines qui dialoguent au switch s'allument. **Le switch (commutateur) permet un dialogue direct entre ces machines**.
{{% /solution %}}

9. Lancer à nouveau la commande `arp -a`. Quelle information supplémentaire la table `arp` contient-elle ?
{{% solution "Réponse" %}}
<center>

| Adresse IP | Adresse MAC |
|:----:|:----:|
| 255.255.255.255 | FF:FF:FF:FF:FF:FF |
| 192.168.0.11 | 0C:84:62:DD:1B:C4 |
</center>
La table `arp` contient désormais une entrée pour l'ordinateur d'adresse IP 192.168.0.11.

Remarque.
: Vous n'obtiendrez pas forcément les mêmes entrées lors de votre simulation.
{{% /solution %}}

10. Visualiser l'historique du traffic : `Clic droit` sur l'ordinateur $\longrightarrow$ `Afficher les échanges de données`. 

11. Pourquoi voit-on, dans certains messages, une adresse MAC valant FF:FF:FF:FF:FF:FF  ?
{{% solution "Réponse" %}}
Il s'agit de l'adresse de diffusion.
{{% /solution %}}

12. À quel niveau du modèle OSI le protocole `arp` intervient-il ?
{{% solution "Réponse" %}}
Niveau 2, couche de liaison.
{{% /solution %}}

13. À quel niveau du modèle OSI intervient la commande `ping` ?
{{% solution "Réponse" %}}
Le protocole ICMP intervient au niveau 3, couche réseau.
{{% /solution %}}

14. Examiner la table SAT du switch : `Clic gauche` sur le switch.    
Que nous apprend cette table ?
{{% solution "Réponse" %}}
Cette table indique sur quel port se trouve chaque ordinateur (repéré par son adresse MAC).
{{% /solution %}}

15. Expliquer pourquoi on dit qu'« **un commutateur (switch) limite le domaine de collision mais pas le domaine de diffusion** ».
{{% solution "Réponse" %}}
{{% note tip %}}
- Au niveau de la couche 2 du modèle OSI, aucune notion de connexion entre deux machines n'existe ; les segments sont diffusés sur tout le réseau et sont reçus aussi bien par la machine destinataire (qui traite alors l'information) que par celles qui ne le sont pas.
- Le processus de découverte de l'adresse MAC de la machine destinataire se fait forcément par diffusion. Un commutateur doit permettre ce mécanisme.
- Par la suite, le switch s'assure que les segments destinés à une machine soient directement dirigés vers le port qui conduit à la machine destinataire ; il évite donc une diffusion à tout le réseau et les éventuelles collisions entre segments qui pourraient intervenir.
{{% / note %}}
{{% /solution %}}

16. Reprendre les manipulations précédentes en effectuant la commande `ping` vers une nouvelle machine et en examinant le remplissage des tables `arp` et `SAT`.

## Communication entre deux réseaux

17. Créer le réseau local suivant :
<img src="/terminales-nsi/chap-11/chap-11-4-2.png" alt="" width="" />
Les masques de sous-réseau sont : 
    - 255.255.255.0 pour le sous-réseau connecté au switch A ;
    - 255.255.0.0 pour le sous-réseau connecté au switch B.

{{% note tip %}}
- Pour pouvoir communiquer sur un même réseau, deux hôtes doivent avoir la même adresse réseau (IP). 
- Pour pouvoir communiquer entre deux réseaux différents, il faut passer par une passerelle, qui elle possède plusieurs cartes réseau, et donc plusieurs adresses IP.
{{% /note %}}

18. Lancer la commande `ping` depuis un ordinateur du sous-réseau A vers un ordinateur du sous-réseau B. Observer et justifier le résultat.
{{% solution "Réponse" %}}
Il est impossible d'atteindre un ordinateur du sous-réseau B depuis un ordinateur du sous-réseau A car ils n'appartiennent pas au même réseau et parce que le routeur n'a pas encore été configuré.
{{% /solution %}}

19. Configurer le routeur afin qu'il route les paquets entre les deux sous-réseaux et tenter à nouveau l'expérience de la question 18. La communication est-elle bien établie ?
{{% solution "Réponse" %}}
La communication est toujours impossible. 
{{% /solution %}}

20. Afin de comprendre pourquoi la communication entre les machines des deux sous-réseaux est toujours impossible, sur l'ordinateur du sous-réseau A, lancer la commande `route`. Examiner le résultat et identifier le problème.
{{% solution "Réponse" %}}
L'ordinateur ne connaît pas la route vers le sous-réseau B.
{{% /solution %}}

21. Configurer les ordinateurs afin que la communication entre les sous-réseaux soit possible.
{{% solution "Réponse" %}}
Définir la passerelle par défaut.
{{% /solution %}}

22. Lancer à nouveau la commande `ping` et examiner le résultat.

23. Examiner la table `arp` de l'ordinateur du sous-réseau A qui vient de communiquer avec l'ordinateur du sous-réseau B. Existe-t-il une entrée pour l'ordinateur du sous-réseau B ? Quelle est l'entrée qui existe ?
{{% solution "Réponse" %}}
Il n'existe aucune entrée pour l'ordinateur du sous-réseau B mais une entrée pour l'interface du routeur appartenant au sous-réseau A.
{{% note tip %}}
La couche de liaison ne définit **aucune connexion directe entre deux ordinateurs**. Les ordinateurs envoient toujours des **segments** (niveau 2) sur le réseau local. Lorsque l'ordinateur destinataire ne se trouve pas sur le réseau local, c'est au routeur d'acheminer correctement les **paquets** (niveau 3).
{{% /note %}}
{{% /solution %}}

24. Lancer la commande `traceroute` vers l'ordinateur du sous-réseau B. À quoi correspond le retour de cette commande ?
{{% solution "Réponse" %}}
`traceroute` donne le chemin suivi par les paquets.
{{% /solution %}}


## Réseaux étendus

{{% note normal %}}
Télécharger le fichier de configuration du {{< remote "réseau étendu" "/terminales-nsi/chap-11/chap-11-4-3.fls" >}}
{{% /note %}}

25. Lancer la commande `traceroute` depuis l'ordinateur M14 vers l'ordinateur M9. Noter la route empruntée par les paquets.

26. Afin de simuler une panne, supprimer le câble réseau qui relie le routeur F au routeur E et lancer à nouveau la commande `traceroute`. Les paquets issus de M14 parviennent-ils toujours en M9 ?

Remarque.
: Cela peut ne pas fonctionner du premier coup, car la mise à jour des tables de routage n’est pas immédiate. Pour remédier à cela, faire un `ping` entre M14 et M9, si cela ne fonctionne pas (timeout), attendre quelques secondes et recommencer.

27. Ouvrir les tables de routage de tous les routeurs qui sont intervenus dans la communication et expliquer le fonctionnement de ces tables.




