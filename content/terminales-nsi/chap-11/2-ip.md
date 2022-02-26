---
title: "Adressage IP"
subtitle: "Chapitre 10,2"
author: ""
type: ""
date: 2020-11-26T06:16:49+04:00
draft: false
toc: true
tags: ["Réseaux", "IP", "Adressage"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

1. L'adresse IPv4 d'un réseau est 192.168.56.0/24. Combien de bits sont-ils 
dédiés à la partie réseau ? Combien de machines peut-on incorporer à ce 
réseau ?
{{% solution "Réponse" %}}
24 bits sont réservés au réseau dans l'adresse. Une adresse IPv4 étant 
composée de 32 bits, il reste 8 bits pour l'adressage des machines dans ce 
réseau. Avec ces 8 bits on peut créer $2^8 = 256$ adresses différentes, pour 
$2^8 - 2 = 254$ ordinateurs.

**Remarque :** L'adresse avec tous les bits de la partie host positionnés à 0 est l'adresse du réseau et l'adresse avec tous les bits de la partie host positionnés à 1 
est l'adresse de diffusion (broadcast).
{{% /solution %}}

2. Quel est le masque de réseau de l'adresse de la question 1 ?
{{% solution "Réponse" %}}
Masque : 255.255.255.0, traduction décimale de 
`11111111.11111111.11111111.00000000`
{{% /solution %}}

3. Quelle est la première adresse utilisable sur le réseau de la question 1 ?
La dernière ?
{{% solution "Réponse" %}}
- Première adresse (pour machine) : 192.168.56.1
- Dernière adresse (pour machine) : 192.168.56.254.
{{% /solution %}}

4. Écrire l'adresse IPv4 222.1.1.20, de masque 255.255.255.192 en notation CIDR.
{{% solution "Réponse" %}}
$192 = (11000000)\_{2}$, donc le masque s'écrit 
`11111111.11111111.11111111.11000000`. 26 bits sont utilisés pour la partie 
réseau. L'adresse s'écrit donc 222.1.1.20/26.
{{% /solution %}}

5. Écrire l'adresse IPv4 135.1.1.25, de masque 255.255.248.0 en notation CIDR.
{{% solution "Réponse" %}}
$248 = \left( 1111 \\; 1000 \right)\_{2}$, donc le masque s'écrit 
11111111.11111111.11111000.00000000. 21 bits sont utilisés pour la partie 
réseau. L'adresse s'écrit donc 135.1.1.25/21.
{{% /solution %}}

6. Un fournisseur d'accès a alloué l'adresse réseau de classe C : 211.1.1.0 à 
une compagnie. Cette dernière utilisant le masque réseau de la classe C : 
255.255.255.0, combien d'ordinateurs peut-elle connecter au réseau ?
{{% solution "Réponse" %}}
Il reste 8 bits pour la partie hôte, donc $2^8 - 2 = 254$ ordinateurs peuvent 
être connectés au réseau.
{{% /solution %}}

7. Sur un ordinateur dont le système d'exploitation est `Linux`, la commande 
`ifconfig` retourne l'adresse IPv4 172.16.20.234 et le masque 255.255.0.0.     
Quelle est l'adresse réseau du réseau auquel cet ordinateur appartient ?
{{% solution "Réponse" %}}
Méthode pour déterminer l'adresse réseau :
<center>

| | | |
| ----: | ---- | ---- |
| |Adresse : |`10101100.00010000.00010100.11101010` |
| &|  |   |
|   | Masque : | `11111111.11111111.00000000.00000000` |
| | | |
|  | Réseau : | `10101100.00010000.00000000.00000000` |

</center>
soit 172.16.0.0.
{{% /solution %}}

8. Combien d'ordinateurs peut-on incorporer au réseau de la question 
précédente ?
{{% solution "Réponse" %}}
16 bits sont réservés à la partie host. On peut donc incorporer $2^{16} - 2 
= \pu{65 534}$ ordinateurs à ce réseau.
{{% /solution %}}

9. L'adresse IPv4 d'un ordinateur est 172.16.20.234/22. Combien d'ordinateurs 
peut-on incorporer à ce réseau ?
{{% solution "Réponse" %}}
Il reste 10 bits pour la partie host, soit $2^{10} = 1024$ adresses. On peut 
donc construire 1022 adresses utilisables pour des ordinateurs.
{{% /solution %}}

10. Quelle est la première adresse utilisable sur le réseau de la question 
précédente ? La dernière ?
{{% solution "Réponse" %}}
La réponse à cette question nécessite tout d'abord de déterminer l'adresse 
réseau :
<center>

| | | |
| ----: | ---- | ---- |
| |Adresse : |`10101100.00010000.00010100.11101010` |
| &|  |   |
|   | Masque : | `11111111.11111111.11111100.00000000` |
| | | |
|  | Réseau : | `10101100.00010000.00010100.00000000` |

</center>

soit 172.16.20.0.         
- La première adresse utilisable est donc : `10101100.00010000.00010100.00000001`, soit 172.16.20.01.
- La dernière est : `10101100.00010000.00010111.11111110`, soit 172.16.23.254.
{{% /solution %}}

11. Un fournisseur d'accès a alloué l'adresse réseau de classe A : 29.0.0.0 à 
une compagnie. Cette dernière doit posséder au moins 20 sous-réseaux 
comportant chacun au maximum 160 machines. Le responsable informatique hésite 
entre les deux masques de réseau suivants pour l'adressage des sous-réseaux : 
255.255.0.0 et 255.255.255.0. Ces masques conviennent-ils tous les deux ?

{{% solution "Réponse" %}}
**Rappel :**  dans un réseau de classe A 8 bits sont réservés à la partie 
réseau, le masque est donc 255.0.0.0.

- Si le masque 255.255.0.0 est utilisé pour créer les sous-réseaux, les 8 bits réseau supplémentaires, par rapport au masque fourni par le fournisseur d'accès, permettent de créer $2^8 = 256$ sous-réseaux et les 16 bits restants permettent d'intégrer $2^{16} - 2 = 65 \\; 534$ machines.
- Si le masque 255.255.255.0 est utilisé pour créer les sous-réseaux, les 16 bits réseau supplémentaires permettent de créer $2^{16} = 65 \\; 536$ sous-réseaux et les 8 bits restants permettent d'intégrer $2^8 - 2 = 254$ machines.

Les deux solutions envisagées conviennent donc.
{{% /solution %}}

12. Un fournisseur d'accès a alloué l'adresse réseau de classe B : 135.1.0.0 à 
une compagnie. Cette dernière doit posséder 4 sous-réseaux comportant chacun 
environ 200 machines. Déterminer le masque de réseau le plus simple 
permettant de réaliser l'adressage attendu.

{{% solution "Réponse" %}}
**Rappel :**  dans un réseau de classe B 16 bits sont réservés à la partie 
réseau, le masque est donc 255.255.0.0.

- Puisqu'il faut réserver environ 200 adresses pour les machines, 8 bits doivent être utilisés. Cela donne comme masque réseau 255.255.255.0.
- À partir du masque précédent, on constate que 8 bits supplémentaire sont utilisés, par rapport au masque fourni par le fournisseur d'accès, pour les sous-réseaux. Comme $2^8 = 256 > 4$, on peut donc bien créer les 4 sous-réseaux attendus. Le plus simple est 
donc de choisir le masque : 255.255.255.0.
{{% /solution %}}

13. Un fournisseur d'accès a alloué l'adresse réseau de classe C : 205.11.2.0 
à une compagnie qui doit créer 30 sous-réseaux. Quel masque de sous-réseau 
permet de maximiser le nombre d'ordinateurs sur chaque sous-réseaux ?

{{% solution "Réponse" %}}
Le masque du réseau est : 255.255.255.0 puisqu'il s'agit d'un réseau de 
classe C.       
$2^4 = 16$ et $2^5 = 32$. Il faut donc réserver 5 bits supplémentaires, pour la création des sous-réseaux. En réserver davantage diminuerait le nombre d'ordinateurs dans chacun des sous-réseaux. Le masque de sous-réseau à utiliser est donc 255.255.255.248 (les 5 bits de poids le plus importants sont positionnés à 1 : `11111111.11111111.11111111.11111000`).
{{% /solution %}}

14. Combien d'ordinateurs pourront être connectés à chacun des sous-réseaux de 
la question précédente ?

{{% solution "Réponse" %}}
Il reste 3 bits pour la partie hôte, donc $2^3 - 2 = 6$ adresses pour des 
ordinateurs.
{{% /solution %}}

15. Quelle sera l'adresse du troisième ordinateur du second 
sous-réseau ?

{{% solution "Réponse" %}}
On applique le masque `11111111.11111111.11111111.11111000` à l'adresse de réseau ` 11001101.00001011.00000010.00000000`.

- Le premier sous-réseau a donc pour adresse `11001101.00001011.00000010.00001000` et celle du second sous réseau `11001101.00001011.00000010.00010000` soit 205.11.2.16.
- L'adresse du troisième ordinateur est `11001101.00001011.00000010.00010011` soit 205.11.2.19.
{{% /solution %}}