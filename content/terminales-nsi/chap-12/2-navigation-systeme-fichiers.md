---
title: "Système de fichiers"
subtitle: "Chapitre 11,02"
author: ""
type: ""
date: 2020-12-09T16:15:48+04:00
draft: false
toc: true
tags: ["Système de fichiers", "Arborescence", "Fichier logique", "Shell", "Fichier physique", "Commandes", "Attributs de fichier", "Permission d'accès aux fichiers", "Ligne de commande"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

{{% note normal %}}
#### Linux est un logiciel libre

Un logiciel est dit libre si son code est couvert par une licence autorisant :
- l'utilisation du logiciel ;
- l'accès public au code source ;
- la modification et la redistribution publique de ces modifications.
{{% /note %}}


## Introduction

Il est possible de commander les systèmes d'exploitation de la famille UniX et leurs dérivés (tels OS X et Linux) grâce à un logiciel appelé **shell**, en *ligne de commandes*. À l'ère de l'interface graphique et des écrans tactiles, on peut se demander pourquoi continuer à taper des commandes, processus qui semble *beaucoup plus long* et *nécessite un apprentissage préalable*. En fait, une fois les commandes maîtrisées, *utiliser la ligne de commande s'avère beaucoup plus efficace pour réaliser des tâches non élémentaires*.

#### Exemple de tâche.
Se rendre dans un répertoire contenant une multitude d'images dans différents formats, compter le nombre de celles qui sont au format `jpeg` et stocker le résultat dans un fichier.

```shell
cd /chemin/vers/repertoire; ls -l | grep jpeg | wc -l > nbre_jpg.txt
```

*Essayez de faire le même enchaînement d'opérations depuis une interface graphique, cela prendra sûrement plus de temps.*

## Invite de commande, commandes et paramètres des commandes


### Invite de commande

> On appelle **Invite de commande** le message qui « invite » à entrer une commande dans la console/terminal :

```bash
mats@serveur-ubuntu:~$
````


Ici, il faut comprendre que l'utilisateur `mats` est connecté à la machine de nom `serveur-ubuntu` et qu'il se situe, dans l'**arborescence des fichiers**, dans son *dossier personnel* (représenté par le symbole `~`).

{{% note warning %}}
Le symbole dollar `$` final signifie que l'utilisateur *mats* n'est pas l'administrateur de la machine. Lorsqu'on utilise la machine en tant qu'*administrateur*, appelé **root** sous UniX, le symbole terminal est `#`.
{{% /note %}}

### Commandes

> L'invite de commande permet d'entrer des commandes. Le comportement de chacune de ces commandes peut être modifié ou précisé à l'aide d'*options**. 

> Le **résultat** de la commande, la **liste de ses options**, leur emploi, etc. font l'objet d'une entrée dans la **documentation** déjà installée sur le système.

```bash
man ls   # lecture de la page de documentation de la commande ls
```

```bash
date                # Retourne la date du jour

date +%Y-%m-%d      # Retourne la date du jour dans le format Année-Mois-Jour

ls                  # Liste tous les fichiers et dossiers du dossier courant

ls -l -a -R         # Liste tous les fichiers et dossiers du dossier courant 
                    # avec des options supplémentaires : affichage long de tous les
                    # fichiers (cachés ou pas) récursif
``` 

#### Remarque.
Lorsque plusieurs options sont utilisées, il est possible de condenser l'écriture de la commande. Par exemple, la commande `ls -l -a -R` peut s'écrire : `ls -laR`. *L'ordre de ces options n'a aucune importance*.


De nombreuses aide à la saisie existent :
- **Rappel des dernières commandes entrées :** utiliser la touche <kbd>↑</kbd> du clavier.

- **Autocomplétion des commandes :** 
    - *entrer les premiers caractères d'une commande et taper la touche* <kbd>⇥</kbd> *deux foix :* la liste des commandes commençant par ces caractères apparaît.
    - *entrer les premiers caractères d'une commande, si cette chaîne est suffisante pour que le système puisse identifier de façon certaine la commande*, un appui sur <kbd>⇥</kbd> complète la commande.

- **Sélection multiple de fichiers :** le caractère <kbd>*</kbd>, appelé **joker** est très utilisé.
```bash
ls -l *.jpeg     # liste tous les fichiers dont l'extension est .jpeg    
```

- **Quelques raccourcis clavier utiles :**
    - <kbd>CTR + L</kbd> : efface le contenu du terminal
    - <kbd>CTRL + A</kbd> : ramène le curseur au début de la commande
    - <kbd>CTRL + E</kbd> : ramène le curseur à la fin de la ligne de commandes
    - <kbd>CTRL + U</kbd> : supprime tout ce qui est à gauche du curseur
    - <kbd>CTRL + K</kbd> : supprime tout ce qui est à droite du curseur
    - <kbd>CTRL + W</kbd> : supprimer le premier mot situé à gauche du curseur
    - <kbd>CTRL + Y</kbd> : si du texte a été supprimé à l'aide d'une des commandes précédentes, ce texte est copié à l'endroit où se trouve le curseur.    

## Les fichiers 

### Qu'est-ce qu'un fichier ?

{{% note tip %}}
Les **fichiers** servent à **stocker des informations de manière permanente**, entre deux exécutions d'un programme.
{{% /note %}}

#### Rappel.
Le contenu des variables disparaît à chaque fin d'exécution d'un programme (ou du bloc d'instructions dans lequel la variable est définie). Les fichiers sont stockés sur des **périphériques à mémoire de masse** (disquette, disque dur, CD Rom, clé USB, etc.).

{{% note tip %}}
En informatique, on utilise le terme **fichier** pour décrire trois notions bien distinctes :
- Le **fichier physique**, *succession de 0 et de 1 sur un support physique* (disque dur, disque optique, etc.).
  
- Le **fichier logique**, *objet informatique que nous présente le système d'exploitation*. **Cet objet est une image du fichier physique**. Les fichiers logiques sont organisés sous forme d'**une arborescence** qui *dépend du système d'exploitation utilisé*, et sont repérés par **un nom** auquel on accole **une extension** (<kbd>.py</kbd> pour un fichier source Python, <kbd>.jpeg</kbd> pour une image au format JPEG (acronyme de *Joint Photographic Experts Group*), <kbd>.exe</kbd> pour un fichier
exécutable, etc.).     
Généralement, un fichier logique possède des **attributs** gérés par le système d'exploitation (*qui a le droit de le lire*, *de le modifier*, *de le détruire*, etc.).

- L'objet qui, dans un langage de programmation, est associé au fichier logique. Nous avons tel objet en Python.
{{% /note %}}

### Fichier physique

{{% note tip %}}
Un **périphérique à mémoire de masse** stocke simplement des **informations binaires** (**bits**). *À ce niveau, aucune distinction entre une image, un texte, un son, etc. n'existe* : un **fichier physique** est  un regroupement de 0 et de 1, stockés sur ce périphérique. 
{{% /note %}}

{{% note normal %}}
Un **système d'exploitation** (Windows, Linux, OS X, FreeBSD, etc.) sait quels blocs physiques il faut réunir pour former un **fichier logique** (fichier image, fichier texte, fichier son, etc.).
{{% /note %}}

Le nombre de bits qu'un périphérique de masse peut stocker est appelé sa **capacité**. Un disque d'un téraoctet (symbole To) peut stocker $2^{40}$ mots de 8 bits.

### Organisation des fichiers logiques en une arborescence

> Les fichiers logiques sont organisés sous forme d'une **arborescence** :

{{< mermaid >}}
graph TD
A(".") --> B("bin")
A --> C("boot")
A --> D("dev")
A --> E("etc")
A --> F("home")
A --> G("lib")
A --> H("media")
A --> I("root")
A --> J("sbin")
A --> K("tmp")
A --> L("usr")
A --> M("var")
F --> FA("user1")
F --> FB("LLM")
FB --> FBA("student1")
FB --> FBB("student2")
FB --> FBC("student3")
FBB --> FBBA("Documents")
FBB --> FBBB("Images")
FBB --> FBBC("Musique")
FBB --> FBBD("Bureau")
FBB --> FBBE("Téléchargements")
FBB --> FBBF("Vidéos")
FBBA --> FBBAA("NSI")
FBBA --> FBBAB("PC")
{{< /mermaid >}}

{{% note tip %}}
#### Chemin d'un fichier

Repérer un fichier logique dans l'arborescence consiste à donner son chemin dans cette arborescence :

Chemin absolu d'un fichier.
: Dans une **arborescence**, le **chemin (absolu) d'un fichier** est la *liste des noms des nœuds de la branche qui va de la **racine** de l'arborescence jusqu'au fichier en question*.
```bash
/home/LLM/student2/Images/chaton.jpeg
```

Chemin relatif d'un fichier.
: Lorsque le chemin qui conduit au fichier ne débute pas au niveau de la racine mais depuis l'endroit dans lequel on se trouve dans l'arborescence, le chemin est dit relatif.
```bash
./Images/chaton.jpeg
```
{{% /note %}}

{{% note normal %}}
Dans un chemin relatif <kbd>.</kbd> signifie « dossier (ou nœud) courant », <kbd>..</kbd> signifie « dossier (ou nœud) parent », <kbd>~</kbd> signifie « dossier personnel ».
{{% /note %}}

{{% note warning %}}
#### Peut-on parler du chemin d'un dossier ?

Sous Unix, **tout n'est que fichier** : en particulier, *un dossier est un fichier qui contient la liste des fichiers placés plus bas que lui dans l'arborescence.* On exprime donc le chemin d'un dossier de la même façon que celle d'un fichier. 
{{% /note %}}

## Quelques commandes de déplacement dans l'arborescence des fichiers et de manipulation des fichiers

- `pwd` (**print working directory**) : affiche le chemin absolu de l'endroit où l'on se trouve dans l'arborescence du système de fichiers.

- `which nom_commande` : affiche le chemin absolu de l'emplacement de la commande `nom_commande` dans le système de fichiers.

- `ls` : liste le contenu du dossier courant.
    - *Options utiles :*
        - `a` (**all**) : les fichiers cachés sont inclus dans l'affichage ;
        - `l` (**long**) : affiche toutes les informations (droits, types, etc.) ;
        - `F`: ajoute un `/` à la fin des noms des dossiers afin de les mettre en évidence ;
        - `h` (**human readable**) : utilisé avec l'option `l` exprime les tailles en multiples d'octets ;
        - `S` : trie le résultat final par taille des fichiers décroissante ;
        - `t` : trie les fichiers par date de dernière modification ;
        - `r` : renverse l'ordre de tri des deux paramètres précédents ;
        - `R` (**recursive**) : affiche le contenu des sous-dossiers.

- `cd` (**change directory**) : permet de se déplacer dans l'arborescence. *Le chemin passé en argument peut être absolu ou relatif*.

- `du` (**disk usage**) : donne la taille occupée par les répertoires situés plus bas dans l'arborescence que le point d'où est lancée la commande. 
    - *Options utiles :*
        - `h` (**human readable**) : les tailles sont affichées en multiples d'octets ;
        - `a` : les dossiers et les fichiers sont pris en compte ;
        - `s` : seul le résultat final est affiché.

- `cat` : affiche le contenu d'un fichier texte à l'écran.

- `less` : affiche le contenu d'un fichier texte à l'écran, page par page. Taper sur la touche <kbd>Espace</kbd> pour passer à la page suivante, la touche <kbd>b</kbd> pour passer à la page précédente et la touche <kbd>q</kbd> pour quitter.

- `touch` : permet de créer un fichier vide (ou de mettre à jour la date de modification).

- `mkdir` (**make directory**) : crée le dossier dont le nom est passé en argument. 
    - *Option utile :*
        - `p` : créé un sous-dossier et tous les sous-dossiers intermédiaires si nécessaire.

- `cp` (**copy**) : copie un fichier ailleurs dans l'arborescence.  
    - *Option utile :*
        - `r` : permet de copier un dossier et les fichiers contenus dans ce dernier.

- `mv` (**move**) : déplace un fichier ou un dossier dans l'arborescence.

- `mv` : renomme un fichier ou un dossier.

- `rm` (**remove**) : supprime un fichier.
    - *Options utiles :*
        - `i` : demande confirmation avant toute action ;
        - `f` (**force**) : la suppression est effectuée quoi qu'il arrive ;
        - `v` (**verbose**) : affiche toutes les informations ;
        - `r` (**recursive**) : supprime un dossier et tout son contenu.

- `rmdir` (**remove directory**) : supprime un dossier vide.

## Méta-données d'un fichier logique

La commande `ls -l` permet d'obtenir un certain nombre d'informations sur les fichiers (ou dossiers) :

```bash
ubuntu@serveur-ubuntu:~/Images$ ls -lh t2png-2.gif
-rw-rw-r-- 1 ubuntu ubuntu 74K Dec  9 18:40 t2png-2.gif
```

```bash 
ubuntu@serveur-ubuntu:~$ ls -lh
total 4.0K
drwxrwxr-x 2 ubuntu ubuntu 4.0K Dec  9 18:41 Images
```

On peut décomposer cette sortie de la sorte :

|||||||||||
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
|`-`|`rw-`|`rw-`|`r--`| `1` | ubuntu | ubuntu | 74K | Dec 9 18:40 | t2png-2.gif |
|1|<span style="margin-left: 0.5em;">2</span>|<span style="margin-left: 0.5em;">3</span>|<span style="margin-left: 0.5em;">8</span>|4|<span style="margin-left: 1.5em;">6</span>|<span style="margin-left: 1.5em;">7</span>|<span style="margin-left: 0.5em;">8</span>|<span style="margin-left: 2em;">9</span>|<span style="margin-left: 2em;">10</span>|

{{% note tip %}}
1. **Type de fichier** : `-` ordinaire, `d` répertoire, `l` lien symbolique.
2. **Droits** de l'**utilisateur propriétaire** (généralement le créateur du fichier) : `rwx` droits de lecture (**read**), d'écriture (**write**) et d'exécution (**execute**) si programme.
3. **Droits** du **groupe propriétaire** (généralement celui du créateur du fichier) : `rwx` droits de lecture (**read**), d'écriture (**write**) et d'exécution (**execute**) si programme.
4. **Droits** de **tous les utilisateurs** de l'ordinateur : `rwx` droits de lecture (**read**), d'écriture (**write**) et d'exécution (**execute**) si programme.
5. Nombre de **liens « durs »**. C'est le nombre de noms de fichiers qui référencent ce fichier.
6. **Identifiant** du **propriétaire du fichier**.
7. **Identifiant** du **groupe propriétaire du fichier**.
8. **Taille du fichier** en octets.
9. **Date de dernière modification** du fichier.
10. **Nom du fichier**.
{{% /note %}}


## Travail

### Notions de base

1. Soit l'invite de commande suivante :
```bash 
toto@einstein:~/Documents/Photos    
```
Quelles informations nous fournit cette invite de commande&nbsp;?

2. Comment rappeler la dernière commande saisie au clavier&nbsp;?

3. Un programme exécutable est-il un fichier spécial&nbsp;?

4. Les extensions des fichiers ont-elles une signification particulière sous Linux&nbsp;?

5. Dans la liste suivante, indiquer les chemins absolus :
```bash
~/Documents
/usr/local/bin
/home/LLM/hpotter
./Bureau/Classes/Terminale/hpotter
../01_Travail 
```

6. Où que l'on se situe dans le système de fichiers, quel est l'effet de la commande :
```bash
cd ~    
```

7. Pour lister de manière récursive tous les fichiers --- sans exception --- présents dans `/usr`, quelle commande faut-il taper&nbsp;?

8. Dans un répertoire contenant une multitude de fichiers, comment afficher la liste détaillée des fichiers, les derniers modifiés apparaissant en dernier dans cette liste (en bas de l'écran)&nbsp;?

9. Pour créer le plus simplement possible, dans son dossier personnel, des sous-dossiers formant le chemin suivant : `programmes/python/backup`, il faut taper : 
```bash
mkdir programmes/python/backup
mkdir -p programmes/python/backup
mkdir programmes; cd programmes; mkdir python; cd python; mkdir backup
mkdir -p programmes python backup
```

10. Une fois les sous-dossiers de la question précédente créés, la commande qui suit supprime-t-elle le sous-dossier `python`.
```python
cd programmes; rmdir python    
```

11. Pour déplacer un répertoire et son contenu dans un sous-répertoire, quelle commande taper&nbsp;?
```bash
mv repertoire_a_deplacer sous-repertoire/
cp -r repertoire_a_deplacer sous-repertoire/
```

12. Quel est l'effet de la commande `rm -rf /` exécutée en tant que simple utilisateur&nbsp;?
    1. Tout le système de fichier est détruit.
    2. Aucun effet car l'utilisateur n'a pas le droit de supprimer la racine du système de fichiers.
    3. Une erreur est retournée car seul l'administrateur a le droit d'utiliser cette commande.
    4. Tous les fichiers et répertoires de l'utilisateur sont supprimés.


### Manipulations de base dans le système de fichiers

Depuis votre dossier personnel, créez un dossier `NSI` et entrez dans ce dossier.
1. Affichez votre position dans le système de fichiers.
2. Créez la structure suivante en deux commandes :
```bash
|-----dossier1
|        |-----dossier3
|-----dossier2
|        |-----dossier4
         |-----dossier5
```

3. Déplacez-vous dans le répertoire `dossier1` *en utilisant un chemin absolu* et créez-y le fichier vide `fichier1`.
4. Copiez le fichier `fichier1` dans le répertoire `dossier3` *en utilisant un chemin relatif*.
5. Déplacez-vous dans le dossier `dossier2` *en utilisant un chemin relatif*.
6. Copiez le fichier `fichier1` dans le répertoire `dossier5` en le renommant `fichier2`.
7. Déplacez le fichier `fichier2` dans le répertoire `dossier4` en le renommant `fichier3`.
8. Supprimez le fichier `fichier1` du répertoire `dossier3`.
9. Retournez dans votre dossier personnel et supprimez tous les fichiers et dossiers qui viennent d'être créés.


### À la recherche du texte perdu

Le répertoire `MetaCaracteres` vous est fourni. Avec la commande `ls MetaCaracteres`, vous constaterez alors que ce répertoire contient de très nombreux fichiers. *Les méta-caractères permettent de définir des motifs à partir desquels une sélection des éléments affichés peut être effectuée.*

{{% note normal %}}

#### Motifs possibles :

- `*` : *représente n’importe quelle suite de caractères (vide ou non)* ;

- `?` : *représente n’importe quel caractère (exactement un)* ;

- `[liste de caractères]` : *représente n’importe quel caractère de la liste (exactement un)*. La liste peut-être un intervalle (`a-z` par exemple), le code ASCII des caractères est pris en considération pour définir les caractères appartenant à l’intervalle ;

- `[^liste de caractères]` : *représente n’importe quel caractère qui n'est pas dans la liste (exactement un)*.

{{% /note %}}

#### Exemples
```bash
ls img*.jpg       # liste tous les noms de fichiers qui commencent par img et se terminent par .jpg avec 0 ou plusieurs caractères entre les deux motifs.
ls img?.jpg       # liste tous les noms de fichiers qui commencent par img et se terminent par .jpg avec exactement un caractère entre les deux motifs.
ls img[1234].jpg  # liste img1.jpg, img2.jpg, img3.jpg, img4.jpg s'ils existent.
ls [^abc]*        # liste tous les noms de fichiers qui ne commencent ni par a, ni par b, ni par c.
ls [^A-Z]*        # liste tous les noms de fichiers qui ne commencent pas par une majuscule.
ls img?*[23].jpg  # liste tous les noms de fichiers qui commencent par img, se terminent par .jpg avec entre un ou plusieurs caractères suivis d'un 2 ou d'un 3.
``` 

{{% note exercise %}}
Donner la signification de chacun des motifs suivants :

1. `*.jpg`
1. `[0-9]*[a-z]` 
1. `*.???` 
1. `*[^A-Z]*` 
1. `?????`
1. `?*?`
1. `*[^.]???` 

Tester les réponses dans un terminal. Pour ce faire, créer dans un dossier un certain nombre de fichiers vides à l'aide de la commande `touch nom_fichier` (utiliser tous les noms possibles et imaginables). 
{{% /note %}}

{{% solution "Réponses" %}}
1. Tous les noms qui se terminent par `.jpg`.
1. Tous les noms qui commencent par un chiffre et se terminent par une lettre en minuscule.
1. Tous les noms qui possèdent une extension (après le `.`) composée de trois caractères exactement.
1. Tous les noms qui en contiennent aucune lettre en majuscule.
1. Tous les noms formés de cinq caractères.
1. Tous les noms formés d'au moins deux caractères.
1. Tous les noms formés d'au moins quatre caractères et dont le quatrième caractère en partant de la droite n'est pas un point.
{{% /solution %}}

----

{{< remote "Dossier compressé à télécharger" "/terminales-nsi/chap-12/MetaCaracteres.zip" >}}

----

1. Déterminez les éléments du répertoire `MetaCaracteres` dont le nom correspond à chacun des motifs suivants et expliquez brièvement les caractéristiques des éléments affichés.
```bash
Prompt$ ls * 
Prompt$ ls ? 
Prompt$ ls [a-c]?
Prompt% ls [ac]?
Prompt% ls [a-c]*
Prompt% ls *.txt
```

2. L’énoncé de cette question se trouve dans le fichier `MetaCaracteres/questionTP1`. La commande cat suivie d’un nom de fichier vous permettra d’afficher le contenu du fichier, et donc de pouvoir le lire et de suivre les indications que vous y trouverez.