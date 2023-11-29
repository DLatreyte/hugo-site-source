---
title: "Simulation de réseaux"
subtitle: ""
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

- Télécharger le logiciel {{< remote "Filius" "<https://www.lernsoftware-filius.de/Herunterladen>" >}}
- **Attention :** Choisir la langue lors de la première ouverture du logiciel. En cas d’erreur, supprimer le dossier `.filius` contenant les paramètres de langues se trouvant dans `C:\Users\nom d’utilisateur sur le réseau\AppData\Local\.filius` (sous windows).
{{% /note %}}

## Construction d'un réseau local

1. En `mode conception`, créer le réseau local suivant :
<img src="/terminales-nsi/chap-11/chap-11-4-1.png" alt="" width="" />

1. Configurer chaque ordinateur : `Mode conception` $\longrightarrow$ `Clic droit` sur l'ordinateur $\longrightarrow$ `Configurer`.  
*Remarque :* le masque de sous-réseau doit être `255.255.255.0`.

1. Sélectionner « Utiliser l'adresse IP comme nom ».

1. Ralentir les animations de façon à pouvoir visualiser le chemin des trames : ramener le curseur placé juste à droite du bouton `Simulation` à 1&nbsp;%.

1. Sur l'ordinateur portable installer les outils en ligne de commande : `Mode simulation` $\longrightarrow$ `Clic gauche` $\longrightarrow$ `Installation des logiciels` $\longrightarrow$ `Ligne de commande` $\longrightarrow$ `Appliquer les modifications`.

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
Par défaut, on a juste l'adresse MAC de diffusion (broadcast).
{{% /solution %}}

8. Lancer la commande `ping 192.168.0.11`. À quoi sert cette commande ?
{{% solution "Réponse" %}}
La commande `ping` permet de tester si une liaison réseau vers une machine que l'on sait allumée et fonctionnelle existe ou pas. Des paquets sont envoyés vers cette dernière ; elle les retourne alors tels quels (echo).
{{% /solution %}}

9. Décrire la circulation des trames observables lors de la simulation.
{{% solution "Réponse" %}}

- Dans un premier temps tous les cables s'allument, ce qui témoigne d'un mécanisme de **diffusion**.
- Par la suite, seuls les cables reliant les deux machines qui dialoguent au switch s'allument. **Le switch (commutateur) permet un dialogue direct entre ces machines**.
{{% /solution %}}

10. Lancer à nouveau la commande `arp -a`. Quelle information supplémentaire la table `arp` contient-elle ?
{{% solution "Réponse" %}}

<center>

| Adresse IP | Adresse MAC |
|:----:|:----:|
| 255.255.255.255 | FF:FF:FF:FF:FF:FF |
| 192.168.0.11 | 0C:84:62:DD:1B:C4 |
</center>
La table `arp` contient désormais une entrée pour l'ordinateur d'adresse IP 192.168.0.11.

Remarque.
: Vous n'obtiendrez pas forcément les mêmes adresses MAC lors de votre simulation.
{{% /solution %}}

11. Visualiser l'historique du traffic : `Clic droit` sur l'ordinateur $\longrightarrow$ `Afficher les échanges de données`.  
Décrire avec précision la méthode utilisée pour découvrir quel est l'ordinateur d'adresse IP 192.168.0.11 sur le réseau.
{{% solution "Réponse" %}}

- L'ordinateur portable forme et envoie une trame *diffusée sur tout le réseau local (broadcast)* qui contient :
  - Pour la couche de liaison (niveau 2) :
    - Adresse MAC source : son adresse MAC
    - Adresse MAC destination : adresse MAC de diffusion (l'adresse MAC de l'ordinateur distant est encore inconnue à ce stade)
  - Pour la couche réseau (niveau 3) :
    - IP source : son adresse IP
    - IP destination  : l'adresse IP de l'ordinateur distant
    - Protocole : ARP
    - Commentaire : Qui a pour adresse IP 192.168.0.11 ?
- L'ordinateur distant forme et envoie une trame **potentiellement** *diffusée sur tout le réseau local (broadcast)* qui contient :
  - Pour la couche de liaison (niveau 2) :
    - Adresse MAC source : son adresse MAC
    - Adresse MAC destination : adresse MAC de l'ordinateur portable
  - Pour la couche réseau (niveau 3) :
    - IP source : son adresse IP
    - IP destination  : l'adresse IP de l'ordinateur portable
    - Protocole : ARP
    - Commentaire : C'est moi et mon adresse MAC est ...

À ce stade de la communication, la découverte est terminée et on passe à un autre protocole.
{{% /solution %}}

12. Pourquoi voit-on, dans certains messages, une adresse MAC valant FF:FF:FF:FF:FF:FF  ?
{{% solution "Réponse" %}}
Il s'agit de l'adresse MAC de diffusion (broadcast).
{{% /solution %}}

13. À quel niveau du modèle OSI le protocole `arp` intervient-il ?
{{% solution "Réponse" %}}
Niveau 3, couche réseau. Ce protocole fait cependant le lien entre les informations de la couche 2 et celles de la couche 3. On dit parfois que ce protocole appartient à la couche $2\\, 1/2$.
{{% /solution %}}

14. À quel niveau du modèle OSI intervient la commande `ping` ?
{{% solution "Réponse" %}}
Le protocole ICMP intervient au niveau 3, couche réseau.
{{% /solution %}}

15. Examiner la table SAT du switch : `Clic gauche` sur le switch.
Que nous apprend cette table ?
{{% solution "Réponse" %}}
Cette table indique quel port il faut emprunter pour accéder aux ordinateurs dont l'adresse MAC a été repérée.
{{% /solution %}}

16. Expliquer pourquoi on dit qu'« **un commutateur (switch) limite le domaine de collision mais pas le domaine de diffusion** ».
{{% solution "Réponse" %}}
{{% note tip %}}

- Au niveau de la couche 2 du modèle OSI, aucune notion de connexion entre deux machines n'existe ; les segments sont diffusés sur tout le réseau et sont reçus aussi bien par la machine destinataire (qui traite alors l'information) que par celles qui ne le sont pas.
- Le processus de découverte de l'adresse MAC de la machine destinataire se fait forcément par diffusion. Un commutateur doit permettre ce mécanisme.
- Par la suite, le switch s'assure que les segments destinés à une machine soient directement dirigés vers le port qui conduit à la machine destinataire ; il évite donc une diffusion à tout le réseau et les éventuelles collisions entre segments qui pourraient intervenir.
{{% / note %}}
{{% /solution %}}

17. Reprendre les manipulations précédentes en utilisant encore la commande `ping` vers une nouvelle machine. Vérifier le remplissage des tables `arp` et `SAT`.

## Communication entre deux réseaux

18. Créer le réseau local suivant :
<img src="/terminales-nsi/chap-11/chap-11-4-2.png" alt="" width="" />

Les masques de sous-réseau sont :  

- `255.255.255.0` pour le sous-réseau connecté au switch A ;
- `255.255.0.0` pour le sous-réseau connecté au switch B.

{{% note tip %}}

- Pour pouvoir communiquer sur un même réseau, deux hôtes doivent avoir la même adresse réseau (IP).
- Pour pouvoir communiquer entre deux réseaux différents, il faut passer par une routeur (ou passerelle), qui lui, possède plusieurs cartes réseau, et donc plusieurs adresses IP.
{{% /note %}}

19. Lancer la commande `ping` depuis un ordinateur du sous-réseau A vers un ordinateur du sous-réseau B. Observer et justifier le résultat.
{{% solution "Réponse" %}}
Il est impossible d'atteindre un ordinateur du sous-réseau B depuis un ordinateur du sous-réseau A car ils n'appartiennent pas au même réseau et parce que le routeur n'a pas encore été configuré.
{{% /solution %}}

20. Configurer le routeur afin qu'il route les paquets entre les deux sous-réseaux et tenter à nouveau l'expérience de la question 18. La communication est-elle bien établie ?
**Remarque :** Choisir l'adresse `192.168.0.254` pour l'interface qui est dans le sous-réseau de gauche et `172.16.255.254` pour celle qui est dans le sous-réseau de droite.
{{% solution "Réponse" %}}
La communication est toujours impossible.
{{% /solution %}}

21. Afin de comprendre pourquoi la communication entre les machines des deux sous-réseaux est toujours impossible, sur l'ordinateur du sous-réseau A, lancer la commande `route`. Examiner le résultat et identifier le problème.
{{% solution "Réponse" %}}

<center>

| Destination | Masque | Passerelle | Interface |
| :---: | :---: | :---: | :---: |
| 192.168.0.10 | 255.255.255.255 | 127.0.0.1 | 127.0.0.1 |
| 192.168.0.0 | 255.255.255.0 | 192.168.0.10 | 192.168.0.10 |
| 127.0.0.1 | 255.0.0.0 | 127.0.0.1 | 127.0.0.1 |

</center>

L'ordinateur ne connaît pas la route vers le sous-réseau B.
{{% /solution %}}

22. Configurer l'ordinateur afin que la communication avec l'autre sous-réseau soit possible.
{{% solution "Réponse" %}}
Il faut ajouter à la main une nouvelle route (ce qui sera fait un peu plus tard) ou définir la « passerelle par défaut », c'est à dire la passerelle qui sera utilisée chaque fois que l'ordinateur ne saura pas quoi faire.
{{% /solution %}}

23. Lancer à nouveau la commande `ping` et examiner le résultat.
{{% solution "Réponse" %}}

La communication n'a toujours pas lieu.

{{% /solution %}}

24. Que faut-il faire pour que la communication entre les deux ordinateurs puisse enfin s'établir ?
{{% solution "Réponse" %}}
L'ordinateur du sous-réseau B doit lui aussi avoir une passerelle définie.
{{% /solution %}}

25. Examiner la table `arp` de l'ordinateur du sous-réseau A qui vient de communiquer avec l'ordinateur du sous-réseau B. Existe-t-il une entrée pour l'ordinateur du sous-réseau B ? Quelle est l'entrée qui existe ?
{{% solution "Réponse" %}}
Il n'existe aucune entrée pour l'ordinateur du sous-réseau B mais une entrée pour l'interface du routeur appartenant au sous-réseau A.
{{% note tip %}}
La couche de liaison ne définit **aucune connexion directe entre deux ordinateurs**. Les ordinateurs envoient toujours des **segments** (niveau 2) sur le réseau local. Lorsque l'ordinateur destinataire ne se trouve pas sur le réseau local, c'est au routeur d'acheminer correctement les **paquets** (niveau 3).
{{% /note %}}
{{% /solution %}}

26. Lancer la commande `traceroute` vers l'ordinateur du sous-réseau B. À quoi correspond le retour de cette commande ?
{{% solution "Réponse" %}}
`traceroute` donne le chemin suivi par les paquets.
{{% /solution %}}

## Réseaux étendus

{{% note normal %}}
Télécharger le fichier de configuration du {{< remote "réseau étendu" "/terminales-nsi/chap-11/chap-11-4-3.fls" >}}
{{% /note %}}

27. Lancer la commande `traceroute` depuis l'ordinateur M14 vers l'ordinateur M9. Noter la route empruntée par les paquets.

28. Afin de simuler une panne, supprimer le câble réseau qui relie le routeur F au routeur E et lancer à nouveau la commande `traceroute`. Les paquets issus de M14 parviennent-ils toujours en M9 ?

Remarque.
: Cela peut ne pas fonctionner du premier coup, car la mise à jour des tables de routage n’est pas immédiate. Pour remédier à cela, faire un `ping` entre M14 et M9, si cela ne fonctionne pas (timeout), attendre quelques secondes et recommencer.

29. Ouvrir les tables de routage de tous les routeurs qui sont intervenus dans la communication et expliquer le fonctionnement de ces tables.
