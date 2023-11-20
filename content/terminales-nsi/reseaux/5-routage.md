---
title: "Le routage entre réseaux IP"
subtitle: "Chapitre 10,5"
author: ""
type: ""
date: 2021-01-02T15:51:33+04:00
draft: false
toc: true
tags: ["Réseaux", "IP", "Adressage", "TCP", "Ethernet", "Routage"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Routeurs et objectif du routage ?

{{% note normal %}}
La responsabilité d’un **protocole de routage** est de *fournir l’information nécessaire pour effectuer un routage*, c’est-à-dire la détermination d’un chemin entre une **machine émettrice** et **une machine réceptrice**, toutes deux identifiées par leur **adresse IP** sur des **sous-réseaux différents**.
{{% /note %}}

{{% note tip %}}
Un **routeur** est un ordinateur possédant **au moins deux interfaces réseaux** situées sur des sous-réseaux IP différents.
{{% /note %}}

{{% note warning %}}
Il faut être capable de distinguer une **carte réseau** d'une **interface réseau**.\
Une **carte réseau** est un *objet physique possédant une adresse MAC*. *On peut «&nbsp;attacher&nbsp;» à une **carte réseau** une ou plusieurs **interfaces réseaux**, objets virtuels, possédant toutes des adresses IP différentes*.\
La plupart du temps, cependant, on n'attache qu'une seule interface à chaque carte réseau.
{{% /note %}}

- Tous les systèmes d'exploitation, pour des raisons de fonctionnement interne qui ne seront pas développées ici, définissent une interface dite de bouclage (**loopback**) dont l'adresse est `127.0.0.1`.

{{% note exercise %}}
1. Lancer un terminal.
2. Entrer la commande `ipconfig /all` sous Windows ou `ifconfig` sous Linux ou OSX. Vérifier que l'interface de loopback est bien définie.
3. Tapper la commande `ping 127.0.0.1` et vérifier que l'interface est bien active.
{{% /note %}}

- Dans les faits, pour des raisons de performances, *dire qu'un routeur possède plusieurs interfaces réseaux est équivalent à dire que le routeur possèdent plusieurs cartes réseaux*.

- **Dans les tables de routage, il n'est jamais fait allusion aux cartes réseaux mais aux interfaces réseaux**.

### Tables de routage

{{% note normal %}}
#### Les routeurs ne sont pas les seuls ordinateurs à posséder une table de routage

Chaque ordinateur sur un réseau doit décider à qui transmettre les trames lorsqu'il doit dialoguer avec un autre ordinateur.
{{% /note %}}


À l'aide du logiciel Filius, on se connecte à une machine d'adresse IP `172.12.0.2` et on clique sur «&nbsp;Afficher le bureau&nbsp;».

On utilise la commande `route` dans le terminal et on obtient le résultat suivant :
<img src="/terminales-nsi/chap-11/chap-11-5/chap-11-5-2.png" alt="" width="" />

1. Décrire le plus précisément possible cet affichage.

{{% solution "Réponse" %}}

Ligne 1 
: La machine a pour adresse IP `172.12.0.2` (on le sait grâce au masque de sous-réseau `255.255.255.255` qui est le masque d'un hôte). Tout paquet destiné à cet ordinateur émis depuis cet ordinateur doit passer par l'interface de loopback.

Ligne 2
: Tout paquet à destination du sous-réseau `172.12.0.0`, sous-réseau auquel appartient l'ordinateur doit transiter par l'interface attachée à cet ordinateur d'adresse `172.12.0.2`.\
**Rappel :** Un ordinateur n'a pas besoin d'un routeur pour dialoguer avec un autre ordinateur appartenant au même réseau. **Les routeurs ne sont obligatoires que lorsqu'il s'agit de faire dialoguer des ordinateurs appartenant à des réseaux différents.

Ligne 3
: Tout paquet à destination du réseau de loopback doit transiter par l'adresse de loopback.

Ligne 4
: (**Route par défaut**) Tout paquet destiné à un ordinateur pour lequel aucune des décisions de routage précédentes ne convient (donc tous les paquets qui ne sont destinés ni à l'ordinateur, ni au sous-réseau auquel l'ordinateur appartient) doit transiter par l'interface d'adresse `172.12.0.2` et être adressé à l'ordinateur d'adresse `172.12.255.254` ; c'est le **routeur**.

{{% /solution %}}

2. Quelle est l'adresse du routeur avec lequel cet ordinateur peut directement dialoguer ?

{{% solution "Réponse" %}}
Le routeur de ce sous-réseau a donc pour adresse `172.12.255.254`.
{{% /solution %}}

On simule le réseau suivant ({{< remote "Fichier simulation à télécharger" "/terminales-nsi/chap-11/chap-11-5/chap-11-5-3.fls" >}}) :
<img src="/terminales-nsi/chap-11/chap-11-5/chap-11-5-4.png" alt="" width="" />

Remarque
: Tous les routeurs utilisent un routage automatique. Leur action n'est pas étudiée dans l'exercice qui suit.

3. À l'aide du logiciel Filius, se connecter à la machine d'adresse IP `192.168.0.10` et cliquer sur «&nbsp;Afficher le bureau&nbsp;».

4. Cette machine est-elle capable d'envoyer un paquet vers la machine d'adresse `192.168.3.11` ? Justifier la réponse à partir de l'étude de la table de routage.
{{% solution "Réponse" %}}
L'ordinateur peut tout à fait envoyer un paquet vers l'ordinateur d'adresse `192.168.3.11` puisqu'il possède une route par défaut qui passe par le routeur R2, route qui mène au sous-réseau d'adresse `192.168.3.0`.
{{% /solution %}}

5. Même question pour l'envoi d'un paquet vers la machine d'adresse `192.168.1.10`.
{{% solution "Réponse" %}}
Lorsqu'on affiche la table de routage de cet ordinateur on constate qu'aucune entrée ne lui permet d'envoyer un paquet vers le réseau d'adresse `192.168.1.0/24` puisque ce réseau n'est pas le sien et que le routeur R2, passerelle par défaut pour cet ordinateur, n'a aucune connaissance de ce réseau.
{{% /solution %}}

6. Se connecter l'ordinateur d'adresse IP `192.168.0.11`. Est-il capable d'envoyer un paquet vers la machine d'adresse IP `192.168.3.11` ? Justifier la réponse à partir de l'étude de la table de routage.
{{% solution "Réponse" %}}
Lorsqu'on affiche la table de routage de cet ordinateur on constate qu'aucune entrée ne lui permet d'envoyer un paquet hors de son réseau (ou de son adresse loopback). Il ne sait donc pas comment envoyer un message à l'ordinateur d'adresse `192.168.3.11`.
{{% /solution %}}

7. Corriger la configuration réseau de l'ordinateur d'adresse IP `192.168.0.11` de façon à ce qu'il puisse envoyer un paquet à l'ordinateur d'adresse `192.168.3.11`.
{{% solution "Réponse" %}}
Il faut configurer la passerelle par défaut en lui attribuant l'adresse du routeur : `192.168.1.253`.
{{% /solution %}}

8. L'ordinateur d'adresse `192.168.3.11` peut-il répondre à l'ordinateur d'adresse `192.168.0.10` ? Justifier la réponse à partir de l'étude de la table de routage.
{{% solution "Réponse" %}}
La route par défaut, dans la table de routage passe par le routeur R4 qui, sauf configuration particulière non prise en compte dans cette partie, ne sait pas comment atteindre le réseau `192.168.0.0`. L'ordinateur d'adresse `192.168.3.11` ne peut donc pas répondre à l'ordinateur d'adresse `192.168.0.10`.
{{% /solution %}}

9. Utiliser la commande `ping` pour confirmer l'étude menée jusqu'à présent.

10. Quelle entrée devrait posséder la table de routage de la machine d'adresse `192.168.0.10` pour pouvoir communiquer avec la machine d'adresse `192.168.1.10` ?

<center>

| Destination | Masque | Passerelle | Interface |
| :---------: | :----: | :--------: | :-------: |
|             |        |            |           |

</center>

{{% solution "Réponse" %}}
<center>

| Destination | Masque        | Passerelle    | Interface    |
| :---------: | :-----------: | :-----------: | :----------: |
| 192.168.1.0 | 255.255.255.0 | 192.168.0.254 | 192.168.0.10 |

</center>
{{% /solution %}}


### Comment une décision de routage est-elle prise par un routeur ?

{{% note tip %}}
#### Algorithme de prise de décision

- Un signal électrique (ou lumineux ou hertzien) parvient à l'une des cartes réseau du routeur.\
Le routeur *reconstruit la trame* contenant toutes les informations que transporte ce signal.

- Le routeur *lit l'adresse MAC du destinataire dans l'entête de la trame*.\
Si cette adresse MAC n'est pas celle du routeur, la trame est rejetée. Si l'adresse MAC est bien celle du routeur, le routeur analyse l'adresse *IP du destinataire final*, présente dans l'entête du paquet contenu dans la trame.

- Si l'*adresse IP du destinataire final appartient à un réseau auquel le routeur est directement connecté*, le routeur envoie directement l'information sur le bon réseau.

- Si l'*adresse IP du destinataire final appartient à un réseau qui apparaît dans la table de routage*, le routeur envoie l'information à la passerelle définie.

- Si l'*adresse IP du destinataire final n'appartient à aucun des réseaux présents dans la table de routage*, le routeur envoie l'information à la passerelle par défaut.
{{% /note %}}

11. Quelle couche du modèle OSI est concernée par l'émission ou la réception de signaux physiques ?
{{% solution "Réponse" %}}
L'émission ou la réception des signaux physiques sont définies par des protocoles de la **couche physique** (ou couche 1).
{{% /solution %}}

12. À quelle couche appartiennent les protocoles qui définissent la structure d'une trame et qui se basent sur les adresses MAC ?
{{% solution "Réponse" %}}
La structure d'une trame est définie au niveau de la **couche de liaison** (couche 2).
{{% /solution %}}

13. Au niveau de quelle couche parle-t-on de paquets et d'adresses IP ?
{{% solution "Réponse" %}}
Les structure des paquets est définie au niveau de la **courche réseau** (couche 3).
{{% /solution %}}

14. Combien de sauts retourne la commande `traceroute 192.168.3.11` lancée depuis la machine d'adresse `192.168.0.10` ?
{{% solution "Réponse" %}}
Le signal parvient à l'ordinateur d'adresse `192.168.3.11` en 3 sauts : `192.168.0.253`, `192.168.2.2`, `192.168.3.11`.\
Ce sont toutes les interfaces d'entrées des différentes trames.
{{% /solution %}}

15. Combien de sauts retourne la commande `traceroute 192.168.0.10` lancée depuis la machine d'adresse `192.168.3.11` ? Expliquer l'origine de la différence.
{{% solution "Réponse" %}}
Le signal parvient à l'ordinateur d'adresse `192.168.0.10` en 4 sauts : `192.168.3.254`, `192.168.3.253`, `192.168.2.1`, `192.168.0.10`.\
Ce sont toutes les interfaces d'entrées des différentes trames.\
On compte dans ce sens un saut de plus car l'ordinateur d'adresse `192.168.3.11` ne sait pas s'adresser directement au routeur `192.168.3.253`.
{{% /solution %}}

16. Compléter la table de routage du routeur R3 de façon à ce que n'importe quel ordinateur puisse communiquer avec n'importe quel autre ordinateur.
Ajouter aussi la passerelle par défaut, R4
<center>

| Destination   | Masque          | Passerelle    | Interface     |
| :-----------: | :-------------: | :-----------: | :-----------: |
| 192.168.3.253 | 255.255.255.255 | 127.0.0.1     | 127.0.0.1     |
| 192.168.2.2   | 255.255.255.255 | 127.0.0.1     | 127.0.0.1     |
| 192.168.3.0   | 255.255.255.0   | 192.168.3.253 | 192.168.3.253 |
| 192.168.2.0   | 255.255.255.0   | 192.168.2.2   | 192.168.2.2   |
| 127.0.0.1     | 255.0.0.0       | 127.0.0.1     | 127.0.0.1     |

</center>
{{% solution "Réponse" %}}
<center>

| Destination | Masque        | Passerelle    | Interface     |
| :---------: | :-----------: | :-----------: | :-----------: |
| 192.168.0.0 | 255.255.255.0 | 192.168.2.1   | 192.168.2.2   |
| 192.168.1.0 | 255.255.255.0 | 192.168.2.1   | 192.168.2.2   |
| 0.0.0.0     | 0.0.0.0       | 192.168.3.254 | 192.168.3.253 |

</center>
{{% /solution %}}

17. On donne ci-dessous la table de routage de base du routeur R1. Cette table doit-elle être complétée de façon à ce que tous les ordinateurs puissent communiquer avec tous les ordinateurs sur le réseau ?

<center>

| Destination   | Masque          | Passerelle    | Interface     |
| :-----------: | :-------------: | :-----------: | :-----------: |
| 192.168.1.254 | 255.255.255.255 | 127.0.0.1     | 127.0.0.1     |
| 192.168.0.254 | 255.255.255.255 | 127.0.0.1     | 127.0.0.1     |
| 192.168.1.0   | 255.255.255.0   | 192.168.1.254 | 192.168.1.254 |
| 192.168.0.0   | 255.255.255.0   | 192.168.0.254 | 192.168.0.254 |
| 127.0.0.1     | 255.0.0.0       | 127.0.0.1     | 127.0.0.1     |
| 0.0.0.0       | 0.0.0.0         | 192.168.0.253 | 192.168.0.254 |

</center>

{{% solution "Réponse" %}}
Cette table de routage est complète, il n'est pas nécessaire d'ajouter quoi que ce soit. Tout paquet destiné à un réseau non présent dans cette table est envoyé à la passerelle par défaut qui s'occupe de le router au-delà du périmètre d'influence de R1.
{{% /solution %}}


## Types de routage

Si le réseau n'est pas trop étendu, il est possible de créer manuellement les tables de routage de chaque routeur (**routage statique**). Cependant, cette méthode n'est pas applicable sur des grands réseaux&nbsp;: les routeurs doivent alors mettre en œuvre des protocoles leurs permettant de construire et de partager automatiquement les tables de routage&nbsp;; on parle de **routage dynamique**.


### Intérêt d'un routage automatique

{{% note tip %}}

- Les protocoles de routage établissent des règles d’**échange entre routeurs pour mettre à jour leurs tables selon des critères de coût** comme, par exemple, la **distance**, l’**état de la liaison**, le **débit**. *Ils améliorent ainsi l’efficacité du routage*.

- Les protocoles de routage ont pour objectif d'éviter les **boucles de routage** (le message peut «&nbsp;tourner en rond&nbsp;» dans le réseau et ne jamais atteindre son destinataire).

- Les protocoles de routage doivent permettre de **compenser les pannes dans le réseau** : une fois une panne détectée, il faut transmettre l’information sur l’événement le plus rapidement possible pour que les différents routeurs recalculent par où faire passer leurs messages en contournant la liaison en panne.
{{% /note %}}

On laisse donc les routeurs mettre eux-mêmes à jour leur table de routage grâce à la mise en œuvre de *protocoles de routage*. 

{{% note normal %}}
Initialement, les informations dont dispose un routeur sont celles sur ces voisins immédiats ainsi que les sous-réseaux auxquels il est connecté. En envoyant régulièrement des messages à ses voisins, et en évaluant le temps de réponse, il peut déterminer si un routeur fonctionne ou pas et en déduire si une liaison existe toujours ou est rompue. Il peut ensuite propager cette information à ses voisins qui peuvent eux-mêmes les transmettre à leurs voisins. *Ainsi, **de proche en proche**, tous les routeurs finissent par partager les mêmes connaissances sur la topologie du réseau*.
{{% /note %}}


### Routing Information Protocol (RIP) : algorithme à vecteur de distances

- RIP est historiquement le premier algorithme de routage. 

{{% note tip %}}
RIP recherche **le plus court chemin** selon un *critère de coût simple* : **le nombre de routeurs à traverser (hop)**.\
Cela revient à affecter un **coût unitaire à la traversée de chaque routeur**.\
RIP appartient à la famille des **protocoles à vecteurs de distance**, *puisque les informations contenues dans la table de routage sont du type **(adresse, distance)**.*
$$ \text{adresse} + \text{distance} = \text{vecteur} $$
{{% /note %}}

#### Algorithme général de RIP

- Lors de l'**initialisation du routeur**, celui-ci détermine l'adresse réseau de ses interfaces puis *envoie sur chacune une demande d'informations (table RIP complète) aux routeurs voisins*.

- Lors de la **réception d'une demande**, un *routeur envoie sa table complète ou partielle* suivant la nature de cette demande. 

- Lors de la **réception d'une réponse**, il met à jour sa table si besoin. Trois cas peuvent se présenter :
	- pour une **nouvelle route**, il *incrémente la distance*, *vérifie que celle-ci est strictement inférieure à 15* et diffuse immédiatement le vecteur de distance correspondant ;
	- pour une **route existante, mais avec une distance plus faible**, la table est mise à jour. La nouvelle distance et, éventuellement, l'adresse du routeur si elle diffère sont intégrées à la table ;
	- pour une **route existante, mais avec une distance plus importante**, la table est mise à jour si la nouvelle distance est émise par le même routeur voisin que précédemment.

	Bien sûr, si l'*appareil reçoit une route dont la distance est supérieure à celle déjà connue d'un autre voisin, RIP l'ignore*. 
	
- À intervalles réguliers (toutes les 30 secondes), la *table RIP est diffusée qu'il y ait ou non des modifications.*

- Des routes doivent être retirées de la table gérée par RIP dans deux situations :

	- en premier lieu, si un **réseau immédiatement connecté devient inaccessible** (panne de l'interface, de la ligne, modification de la topologie par l'administrateur, etc.), les routeurs RIP reliés à ce réseau affectent dans leur table une *distance «&nbsp;infinie&nbsp;»* (16 comme indiqué plus haut) à cette route. Elle est conservée pendant la durée d'un temporisateur de «&nbsp;maintien&nbsp;» (garbage collect) de 120 secondes puis est supprimée. Immédiatement après, le vecteur avec une distance «&nbsp;infinie&nbsp;» est diffusé. Un routeur qui reçoit un vecteur avec une distance de 16 comprend : «&nbsp;il faut que tu retires cette route de ta table, car elle est devenue invalide !&nbsp;» De proche en proche, cette information se propage ;
	- en second lieu, **un routeur du réseau tombe en panne**. Cela veut peut-être dire que les réseaux situés derrière cet appareil sont devenus inaccessibles. Mais comment savoir si un routeur est en panne ? RIP considère qu'un routeur qui *n'a pas donné de nouvelles depuis trois minutes* est hors service. Pour gérer cette situation, il attribue à toutes les routes dynamiques un temporisateur initialisé à 180 secondes par défaut. À chaque réception d'un vecteur de distance déjà présent dans la table, le compteur est réinitialisé. Mais si jamais ce compteur atteint zéro, la route est considérée comme invalide. On se retrouve alors dans la situation précédente (distance infinie, temporisateur de maintien, diffusion de l'information puis suppression de la route). Maintenant, si un autre routeur connaît une route menant vers un des réseaux que l'on vient de retirer, c'est parfait ! Notre routeur intègrera cette nouvelle route dans sa table. De cette façon, RIP permet la tolérance aux pannes.

<div style="text-align: right;">
<a href="https://inetdoc.developpez.com/tutoriels/routage-dynamique-protocole-rip/#L3-1" target="_blank"> https://inetdoc.developpez.com/tutoriels/routage-dynamique-protocole-rip/#L3-1 </a>
</div>

{{% note normal %}}
Un routeur garde donc en mémoire, pour chaque réseau IP connu, l'adresse du routeur voisin dont la distance (on dit aussi **métrique**) est la plus petite.
{{% /note %}}

{{% note tip %}}
Les trois caractéristiques principales qui distinguent l’algorithme RIP de l’algorithme OSPF sont :

- *La distance est mesurée en nombre de routeurs à traverser*. 

- *Aucun routeur n'a une vision globale du réseau*. Les routes sont connues de proche en proche.

- Le protocole est *limité aux réseaux dont le plus long chemin implique quinze routeurs au maximum car la convergence des informations est très lente*. 
{{% /note %}}

Remarque
: Les situations où les routes doivent être choisies en fonction de paramètres mesurés en temps réel comme un **délai**, une **fiabilité** ou une **charge**, se prêtent donc mal à ce type de traitement.

Remarque
: Pour déterminer quelle est la meilleure route, le protocole RIP s'appuie sur l'algorithme de Bellman et Ford qui sera étudié un peu plus tard dans l'année.


{{% note exercise %}}
<img src="/terminales-nsi/chap-11/chap-11-5/chap-11-5-5.png" alt="" width="" />

1. Pour chaque sous-réseau situé entre deux routeurs, donner la première adresse utilisable pour adresser une machine et la dernière.

2. Attribuer aux différentes interfaces des routeurs des adresses.

3. Donner la table de routage du routeur $R_1$ à son initialisation. Ajouter une colonne distance.

<center>

| Destination | Masque | Passerelle | Interface | Distance |
| :---------: | :----: | :--------: | :-------: | :------: |
|             |        |            |           |          |

</center>

**Remarque :** Pour simplifier la lecture, ne rien écrire dans la colonne Passerelle si celle-ci est le routeur lui-même. De plus, ne pas prendre en compte l'adresse de loopback et la route par défaut.

4. Même question pour le routeur $R_3$ et le routeur $R_2$.

5. Donner la table de routage du routeur $R_1$ si on imagine qu'il a d'abord échangé une demande RIP avec le routeur $R_3$.

6. Donner la table de routage du routeur $R_1$ si on imagine qu'il a ensuite échangé une demande RIP avec le routeur $R_2$.

7. Quelle est la table de routage finale pour le routeur $R_1$.

8. Quel chemin vont suivre les paquets entre PC1 et PC2 ?

{{% /note %}}

{{% solution "Réponses" %}}
1. 
   - `10.0.0.0/8`: adresses de `10.0.0.1` à `10.255.255.254` (même chose pour tous les réseaux en `x.0.0.0/8`) ;
   - `192.168.1.0/24`: adresses de `192.168.1.1` à `192.168.1.254` ;
   - `192.168.2.0/24`: adresses de `192.168.2.1` à `192.168.2.254` ;
2. 
   - $R_1$ : `192.168.1.254`, `10.0.0.1`, `20.0.0.1` ;
   - $R_2$ : `20.0.0.2`, `30.0.0.2`, `40.0.0.2` ;
   - $R_3$ : `30.0.0.1`, `50.0.0.1`, `70.0.0.2`, `10.0.0.2` ;
   - $R_4$ : `40.0.0.1`, `50.0.0.2`, `60.0.0.2` ;
   - $R_5$ : `192.168.2.254`, `60.0.0.1`, `70.0.0.1`.

3. Table de routage de $R_1$ après initialisation :
<center>

| Destination   | Masque          | Passerelle | Interface       | Distance |
| :-----------: | :-------------: | :--------: | :-------------: | :------: |
| `192.168.1.0` | `255.255.255.0` |            | `192.168.1.254` | 1        |
| `10.0.0.0`    | `255.0.0.0`     |            | `10.0.0.1`      | 1        |
| `20.0.0.0`    | `255.0.0.0`     |            | `20.0.0.1`      | 1        |

</center>

4. 
- Table de routage de $R_2$ après initialisation : 
<center>

| Destination | Masque      | Passerelle | Interface  | Distance |
| :---------: | :---------: | :--------: | :--------: | :------: |
| `40.0.0.0`  | `255.0.0.0` |            | `40.0.0.2` | 1        |
| `30.0.0.0`  | `255.0.0.0` |            | `30.0.0.2` | 1        |
| `20.0.0.0`  | `255.0.0.0` |            | `20.0.0.2` | 1        |

</center>

- Table de routage de $R_3$ après initialisation :
<center>

| Destination | Masque      | Passerelle | Interface  | Distance |
| :---------: | :---------: | :--------: | :--------: | :------: |
| `50.0.0.0`  | `255.0.0.0` |            | `50.0.0.1` | 1        |
| `30.0.0.0`  | `255.0.0.0` |            | `30.0.0.1` | 1        |
| `70.0.0.0`  | `255.0.0.0` |            | `70.0.0.2` | 1        |
| `10.0.0.0`  | `255.0.0.0` |            | `10.0.0.2` | 1        |

</center>

5. Après échange RIP entre $R_1$ et $R_3$, table de routage de $R_1$ :
<center>

| Destination   | Masque          | Passerelle | Interface       | Distance |
| :-----------: | :-------------: | :--------: | :-------------: | :------: |
| `192.168.1.0` | `255.255.255.0` |            | `192.168.1.254` | 1        |
| `10.0.0.0`    | `255.0.0.0`     |            | `10.0.0.1`      | 1        |
| `20.0.0.0`    | `255.0.0.0`     |            | `20.0.0.1`      | 1        |
| `50.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `30.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `70.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |

</center>

6. Après échange RIP entre $R_1$ et $R_2$, table de routage de $R_1$ :
<center>

| Destination   | Masque          | Passerelle | Interface       | Distance |
| :-----------: | :-------------: | :--------: | :-------------: | :------: |
| `192.168.1.0` | `255.255.255.0` |            | `192.168.1.254` | 1        |
| `10.0.0.0`    | `255.0.0.0`     |            | `10.0.0.1`      | 1        |
| `20.0.0.0`    | `255.0.0.0`     |            | `20.0.0.1`      | 1        |
| `50.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `30.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `70.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `40.0.0.0`    | `255.0.0.0`     | `20.0.0.2` | `20.0.0.1`      | 2        |

</center>

7. Table de routage finale de $R_1$ :
<center>

| Destination   | Masque          | Passerelle | Interface       | Distance |
| :-----------: | :-------------: | :--------: | :-------------: | :------: |
| `192.168.1.0` | `255.255.255.0` |            | `192.168.1.254` | 1        |
| `10.0.0.0`    | `255.0.0.0`     |            | `10.0.0.1`      | 1        |
| `20.0.0.0`    | `255.0.0.0`     |            | `20.0.0.1`      | 1        |
| `50.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `30.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `70.0.0.0`    | `255.0.0.0`     | `10.0.0.2` | `10.0.0.1`      | 2        |
| `40.0.0.0`    | `255.0.0.0`     | `20.0.0.2` | `20.0.0.1`      | 2        |
| `60.0.0.0`    | `255.0.0.0`     | `20.0.0.2` | `20.0.0.1`      | 3        |
| `192.168.2.0` | `255.255.255.0` | `10.0.0.2` | `10.0.0.1`      | 3        |

</center>

8. Les paquets vont traverser les routeurs $R_1$, $R_3$ et $R_5$.
{{% /solution %}}

### Open Shortest Path First (OSPF) : algorithme à état de liaison

{{% note tip %}}

- L’algorithme SPF (Shortest Path First) *calcule le plus court chemin* vers toutes les destinations de la zone ou du système autonome, en partant du routeur où s’effectue le calcul (à partir de sa base de données topologiques). *Il calcule le plus court chemin, selon un critère de coût où interviennent de **multiples paramètres** : l’**état des liens**, l’**encombrement du réseau** et des **mémoires des routeurs intermédiaires**.*

- Le calcul du plus court chemin est effectué de manière indépendante par tous les routeurs qui possèdent donc la même information : une **vision globale de tout le réseau**.

- *Chaque réseau peut être schématisé par un **graphe** dans lequel les routeurs et les switchs sont les **sommets**, leurs liaisons sont les **arêtes**, les étiquettes des arêtes sont les **coûts**.*

- Le protocole OSPF définit les règles et les formats de messages entre routeurs.
{{% /note %}}

Remarque
: L'algorithme utilisé par le protocole SPF est l’**algorithme de Dijkstra** (cet algorithme sera étudié un peu plus tard dans l'année) pour obtenir les routes les moins coûteuses et sans cycle. *Chaque routeur devient alors la racine d’un arbre qui contient les meilleures routes*.

{{% note exercise %}}
Reprendre l'exercice précédent en prenant en compte que les débits des liaisons éthernet sont très supérieurs aux débits des liaisons séries. Le protocole OSPF conduit-il selon vous à la même conclusion que le protocole RIP quant au chemin le plus court pour se déplacer de PC1 à PC2 ?
{{% /note %}}

{{% solution "Réponse" %}}
Les débits de transmission sur les liaisons séries sont bien plus petits que ceux sur les liaisons éthernet. Si le protocole OSPF est utilisé la meilleure route annoncée sera donc $R_1 \longrightarrow R_2 \longrightarrow R_3 \longrightarrow R_4 \longrightarrow R_5$.

<center>

| Technologie          | BP descendante                      | BP montante                         |
| :------------------: | :---------------------------------: | :---------------------------------: |
| Modem                | $\pu{56 kbit/s}$                    | $\pu{48 kbit/s}$                    |
| Bluetooth            | $\pu{3 Mbit/s}$                     | $\pu{3 Mbit/s}$                     |
| Ethernet             | $\pu{10 Mbit/s}$                    | $\pu{10 Mbit/s}$                    |
| Wi-Fi                | $\pu{11 Mbit/s}$ à $\pu{10 Gbit/s}$ | $\pu{11 Mbit/s}$ à $\pu{10 Gbit/s}$ |
| ADSL                 | $\pu{13 Mbit/s}$                    | $\pu{1 Mbit/s}$                     |
| 4G                   | $\pu{100 Mbit/s}$                   | $\pu{50 Mbit/s}$                    |
| Satellite            | $\pu{50 Mbit/s}$                    | $\pu{1 Mbit/s}$                     |
| FastEthernet         | $\pu{100 Mbit/s}$                   | $\pu{100 Mbit/s}$                   |
| FFTH (fibre optique) | $\pu{10 Gbit/s}$                    | $\pu{10 Gbit/s}$                    |

</center>
{{% /solution %}}

{{% note tip %}}
#### Notion de coût d'une liaison

La notion de coût est directement liée au **débit des liaisons** entre les routeurs. Le **débit** correspond au *nombre de bits de données qu'il est possible de faire passer dans un réseau par seconde*. Le débit est donc donné en bits par seconde (bps) ou dans l'une des unités multiples.\
Connaissant le débit d'une liaison, il est possible de calculer le coût d'une liaison à l'aide de la formule suivante :
$$
   \text{Coût} = \dfrac{10^8}{\text{Débit}}
$$
avec le débit en bits par seconde.
{{% /note %}}

Remarque
: Pour obtenir la métrique d'une route, il suffit d'additionner les coûts de chaque liaison.

## Exercice

Soit le réseau dont la topologie est la suivante :
<img src="/terminales-nsi/chap-11/chap-11-5/chap-11-5-6.png" alt="" width="" />

Les adresses IP des routeurs sont les suivantes :

- $A$ : 
   - eth0 : `172.18.255.254`
   - eth1 : `192.168.1.1`
   - eth2 : `192.168.2.1`
- $B$ :
   - eth0 : `192.168.1.2`
   - eth1 : `192.168.3.1`
   - eth2 : `172.16.255.254`
- $C$ :
   - eth0 : `192.168.2.2`
   - eth1 : `192.168.3.2`
   - eth2 : `172.17.255.254`


1. Établir la table de routage du routeur $A$ si on suppose que le protocole RIP est utilisé.\
Utiliser le nom des interfaces (eth0, eth1, eth2) à la place des adresses IP dans la table de routage.

{{% solution "Réponse" %}}
<center>

| Destination   | Masque          | Passerelle    | Interface | Distance |
| :-----------: | :-------------: | :-----------: | :-------: | :------: |
| `172.18.0.0`  | `255.255.0.0`   |               | eth0      | 1        |
| `192.168.1.0` | `255.255.255.0` |               | eth1      | 1        |
| `192.168.2.0` | `255.255.255.0` |               | eth2      | 1        |
| `172.17.0.0`  | `255.255.0.0`   | `192.168.2.2` | eth2      | 2        |
| `192.168.3.0` | `255.255.255.0` | `192.168.1.2` | eth1      | 2        |
| `172.16.0.0`  | `255.255.0.0`   | `192.168.1.2` | eth1      | 2        |

</center>
{{% /solution %}}


2. Quel est, d'après la table de routage ci-dessus, le chemin qui sera emprunté par un paquet pour aller d'une machine ayant pour adresse IP `172.18.1.1/16` à une machine ayant pour adresse IP `172.16.5.3/16` ?
{{% solution "Réponse" %}}
La route que suivront les paquets est : $A \longrightarrow B$.
{{% /solution %}}

3. Établir la table de routage du routeur $A$ si on suppose que le protocole OSPF est utilisé.\
   On donne les débits suivants :
      - Liaison routeur $A$ - routeur $B$ : 1 Mbps ;
      - Liaison routeur $A$ - routeur $C$ : 10 Mbps ;
      - Liaison routeur $C$ - routeur $B$ : 10 Mbps ;
      - Liaisons routeurs - switch : 10 Mbps.

{{% solution "Réponse" %}}
<center>

| Destination   | Masque          | Passerelle    | Interface | Distance |
| :-----------: | :-------------: | :-----------: | :-------: | :------: |
| `172.18.0.0`  | `255.255.0.0`   |               | eth0      | 10       |
| `192.168.1.0` | `255.255.255.0` |               | eth1      | 100      |
| `192.168.2.0` | `255.255.255.0` |               | eth2      | 10       |
| `172.17.0.0`  | `255.255.0.0`   | `192.168.2.2` | eth2      | 20       |
| `192.168.3.0` | `255.255.255.0` | `192.168.2.2` | eth2      | 20       |
| `172.16.0.0`  | `255.255.0.0`   | `192.168.2.2` | eth2      | 30       |

</center>
{{% /solution %}}

4. Quel est, d'après la table de routage ci-dessus, le chemin qui sera emprunté par un paquet pour aller d'une machine ayant pour adresse IP `172.18.1.1/16` à une machine ayant pour adresse IP `172.16.5.3/16` ?
{{% solution "Réponse" %}}
La route que suivront les paquets est : $A \longrightarrow C \longrightarrow B$.
{{% /solution %}}