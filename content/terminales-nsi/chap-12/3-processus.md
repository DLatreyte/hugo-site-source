---
title: "Gestion des processus et des ressources"
subtitle: "Chapitre 11,3"
author: ""
type: ""
date: 2021-01-10T05:10:07+04:00
draft: false
toc: true
tags: []
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de ce document est d'essayer de faire comprendre les idées mises en œuvre lors de l'écriture des système d'exploitation afin qu'**un nombre de programmes plus important que le nombre de processeurs puisse fonctionner « simultanément »**. 

## L'ordonnanceur

### Rappel sur l'exécution d'un programme

{{% note tip %}}

- Un programme est un fichier contenant une suite d'instructions écrites en langage machine. C'est une suite d'octets que le processeur que le processeur est capable de décoder et d'exécuter.

- Actions du système d'exploitation au lancement d'un programme :
    - Le contenu du fichier contenant le programme est copié dans la mémoire vive (RAM), à une certaine adresse $a$.
    - Le système d'exploitation écrit l'adresse $a$ dans le registre IP (instruction pointer).

- Au cycle d'horloge du processeur suivant, ce dernier lit l'instruction qui se trouve dans le registre IP et l'exécute. Par la suite, il exécute la deuxième instruction puis les suivantes.

Remarque
: L'exécution d'une instruction par le processeur se décompose en en plusieurs sous-étapes : le **chargement** (*récupération de l'instruction en mémoire*), le **décodage** (*quelle action est codée par la suite d'octets*) et l'**exécution**.
{{% /note %}}

### Interruptions

La description précédente est correcte mais incomplète : elle laisse penser qu'une fois un programme lancé le processeur se focalise sur son exécution, au détriment de l'exécution de tout autre programme.

{{% note tip %}}
Une **interruption** est *un signal envoyé au processeur lorsqu'un évènement se produit*.
{{% /note %}}

Il existe plusieurs types d'interruptions :

- les *interruptions générées par le matériel* (un disque dur signale qu'il a fini d'écrire un octet, une carte réseau signale qu'une trame vient d'arriver, ...)

- les *interruptions d'horloges* générées par le processeur (historiquement toutes les $\pu{55 ms}$, toutes les $\pu{100 ns}$ de nos jours).

Lorsqu'un processeur reçoit une interruption il interrompt son exécution à la fin de l'instruction courante et exécute un programme se trouvant à une adresse prédéfinie.\
Ce programme, le **gestionnaire d'interruption**, reçoit une copie des valeurs courante des registres, ainsi qu'un code numérique lui permettant de savoir quel est le type de l'interruption qui a stoppé le processeur.


{{% note normal %}}
On utilise les interruptions, principalement dans deux buts :

- *permettre des **communications non bloquantes** avec des périphériques externes ;*

- *commuter entre les tâches dans un **ordonnanceur**.*

**Les interruptions constituent le fondement de l'exécution concurrente des programmes.**
{{% /note %}}

### Vocabulaire

{{% note tip %}}
Exécutable
: Fichier binaire contenant des instructions en langage machine directement exécutables par le processeur de la machine.

Processus
: **Instance du programme en cours d'exécution**. *Un système d'exploitation identifie généralement les processus par un numéro unique*.\
Un processus est décrit par :

- L'**ensemble de la mémoire allouée** par le système d'exploitation pour l'exécution du programme (instructions codées et données manipulées, qu'elles soient contenues dans la pile ou sur le tas) ;

- L'**ensemble des ressources utilisées** par le programme (fichiers ouverts, connexions réseau, etc.) ;

- Les **valeurs stockées dans tous les registres du processeur**.

Thread ou tâche
: **Éxécution d'une suite d'instructions démarrée par un processus**. *Deux processus sont l'exécution de deux programmes différents (traitement de texte et navigateur web, par exemple). Deux threads sont l'exécution concurrente de deux suites d'instructions d'un même processus* (téléchargement d'une page web et affichage d'une page web).

Exécution concurrente
: Deux processus ou threads s'exécutent de manière concurrente s'**ils se partagent l'accès à un processeur**. Ils ne s'exécutent donc pas au même moment.

Exécution parallèle
: Deux processus ou threads s'exécutent en parallèle s'**ils s'exécutent au même instant**. *Plusieurs processeurs dans l'ordinateur sont donc nécessaires à une exécution parallèle*.
{{% /note %}}

{{% note warning %}}
**Les processus sont isolés par le système d'exploitation, ils ne partagent pas la même zone de la mémoire alors que les threads issus d'un même processus peuvent accéder aux variables globales du programme et occupent le même espace mémoire.**
{{% /note %}}

|Nom|Description|
|:----|:----|
|**PID**|Process ID, l'identifiant numérique du processus|
|**État**|L'état dans lequel se trouve le processus|
|**Registres**|La valeur des registres lors de la dernière interruption|
|**Mémoire**|Zone mémoire (plage d'adresses) allouée par le processus lors de son exécution|
|**Ressources**| Liste des fichiers ouverts, connexions réseau en cours d'utilisation, etc.|

> Informations pour la description d'un **Processus**.

### Ordonnanceur du système d'exploitation

{{% note tip %}}
Le système d'exploitation utilise des interruptions pour « reprendre la main » et décider quel programme en cours d'exécution doit avoir accès au processeur.
{{% /note %}}

#### Exemple

1. Le processus « traitement de texte » a accès au processeur. Il est en cours d'exécution.

2. Une interruption d'horloge se déclenche.

3. Le code du gestionnaire d'interruption est appelé. Il reçoit comme arguments les valeurs de tous les registres avant le déclenchement de l'interruption (donc tout ce qui concerne le processus ayant accès au processeur).

4. Le gestionnaire d'interruption sauvegarde ces valeurs à un endroit particulier de la mémoire.

5. Le gestionnaire d'interruption choisit dans la liste des processus un processus en attente, par exemple celui correspondant à un navigateur web.

6. Il restaure les valeurs des registres qu'il avait sauvegardés lors de la dernière interruption du navigateur web.\
Parmi ces registres, il y a en particulier IP, le pointeur d'instruction, qui contient l'adresse de la prochaine instruction à exécuter.

7. Le gestionnaire d'interruption a fini son travail et « rend la main ». Le processeur exécute le code du processus lié au navigateur web jusqu'à la prochaine interruption.

{{% note normal %}}
On appelle **commutation de contexte** l'action d'interrompre un processus et de sauvegarder son état. C'est l'**ordonnanceur** qui est en charge de cette tâche.\
Afin de pouvoir décider à quel processus donner la main, l'ordonnanceur utilise une structure de données telle qu'une **file** pour stocker la liste des processus et ainsi partager les tâches.
{{% /note %}}


### États d'un processus

{{% note normal %}}
Les interruptions ne se limitent pas aux interruptions d'horologes, un processus peut être en attente d'une action d'un utilisateur, de la réception d'une trame, du résultat de la recherche d'une information sur un disque dur, etc. Un processus peut donc être interrompu et mis en attente par le système d'exploitation qui favorise alors d'autres processus.
{{% /note %}}

{{% note tip %}}
La plupart des systèmes d'exploitation définissent différents états pour les processus :

Nouveau
: État d'un processus en cours de création. Le système d'exploitation vient de copier le code exécutable en mémoire.

Prêt
: Le processus est dans la file des processus à exécuter et attend d'être choisi par l'ordonnanceur.

En exécution
: Le processus est en train d'être exécuté.

En attente
: Le processus est en interrompu et en attente d'un évènement externe (entrée/sortie, allocation mémoire, etc).

Terminé
: Le processus est terminé. Le système d'exploitation est en train de désallouer les ressources que le processus utilisait.
{{% /note %}}

<img src="/terminales-nsi/chap-12/chap-12-3/chap-12-3-1.png" alt="" widht="" />
> Cycle de vie d'un processus

{{% note normal %}}
Les états **Nouveau** et **Terminé** sont temporaires. Normalement l'état d'un processus varie entre **Prêt**, **En attente** et **En exécution**.
{{% /note %}}

### L'ordonnancement

Plusieurs processus peuvent donc être dans l’état prêt : *comment choisir celui qui sera élu&nbsp;?* 
{{% note tip %}}
L’**ordonnanceur** (**scheduler**) classe les processus prêts dans une file et le **répartiteur** (**dispatcher**) alloue quant à lui un processeur à l’élu dans le cas d’une architecture multiprocesseur.
{{% /note %}}

{{% note normal %}}
Il existe plusieurs **politiques d’ordonnancement** dont le choix va dépendre des objectifs du système.\
Quelques exemples :

- **Premier arrivé, premier servi :** simple, mais peu adapté à la plupart des situations.

- **Plus court d’abord :** très efficace, mais il est la plupart du temps impossible de connaître à l’avance le temps d’exécution d’un processus.

- **Priorité :** le système alloue un niveau de priorité aux processus (SCHED_FIFO sur Linux). Cependant des processus de faible priorité peuvent ne jamais être élus.

- **Tourniquet :** un quantum de temps est alloué à chaque processus (SCHED_RRsous Linux). Si le processus n’est pas terminé au bout de ce temps, il est mis en bout de file en état prêt.

- **Un système hybride entre tourniquet et priorité** qu’on retrouve dans les systèmes Unix.
{{% /note %}}

## Commandes Unix de gestion des processus

{{% note normal %}}
`ps` (*process status*) est la commande de base pour lister tous les processus en cours. Options utiles :
    - `a`: tous les processus ;
    - `u` : nom des utilisateurs qui ont lancé le processus ;
    - `x` : fait aussi apparaître les processus qui n'ont pas été lancés depuis la ligne de commande.
{{% /note %}}

```bash
ubuntu@serveur-ubuntu:~$ ps aux
USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
root           1  1.0  0.6 169776 13280 ?        Ss   06:56   0:07 /sbin/init
root           2  0.0  0.0      0     0 ?        S    06:56   0:00 [kthreadd]
root           3  0.0  0.0      0     0 ?        I<   06:56   0:00 [rcu_gp]
root           4  0.0  0.0      0     0 ?        I<   06:56   0:00 [rcu_par_gp]
root           6  0.0  0.0      0     0 ?        I<   06:56   0:00 [kworker/0:0H-kblockd]
root           9  0.0  0.0      0     0 ?        I<   06:56   0:00 [mm_percpu_wq]
.............................................
.............................................
ubuntu      8421  0.0  0.1  11476  3284 pts/0    R+   07:08   0:00 ps aux
```

La colonne `STAT` l'état du processus :

- `R` (*Running* ou *Runnable*) : le processus est dans l'état **Prêt** ou **En exécution**.
- `S`(*Sleeping*) : le processus est **En attente**.

{{% note normal %}}
`top` permet en temps réel les processus en cours.
{{% /note %}}

```bash
ubuntu@serveur-ubuntu:~$ top

top - 07:12:34 up 15 min,  1 user,  load average: 0.00, 0.05, 0.14
Tasks: 113 total,   1 running, 111 sleeping,   1 stopped,   0 zombie
%Cpu(s):  0.0 us,  0.2 sy,  0.0 ni, 99.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   1983.9 total,    678.0 free,    142.0 used,   1163.9 buff/cache
MiB Swap:      0.0 total,      0.0 free,      0.0 used.   1648.7 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                    
    935 ubuntu    20   0   14808   6048   4564 S   0.3   0.3   0:00.18 sshd                       
   8441 ubuntu    20   0   11864   4088   3424 R   0.3   0.2   0:00.03 top                        
      1 root      20   0  169776  13280   8796 S   0.0   0.7   0:07.13 systemd                    
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.01 kthreadd                   
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                     
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                 
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-kblockd       
      9 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq    
```
Le processus qui monopolise le plus le processeur apparaît dans la première ligne.

{{% note tip %}}
Un système d'exploitation en fonctionnement est *constitué par un ensemble de processus*. Au démarrage de la machine, un processus père est lancé (historiquement c'est le processus `init` ou `systemd` sur Linux). *Son rôle est par la suite de démarrer tous les autres processus*.
{{% /note %}}

{{% note normal %}}
La hiérarchie des processus peut être visualisée grâce à la commande `pstree`.
{{% /note %}}

```bash
ubuntu@serveur-ubuntu:~$ pstree -h
systemd─┬─accounts-daemon───2*[{accounts-daemon}]
        ├─2*[agetty]
        ├─atd
        ├─cron
        ├─dbus-daemon
        ├─irqbalance───{irqbalance}
        ├─multipathd───6*[{multipathd}]
        ├─networkd-dispat
        ├─polkitd───2*[{polkitd}]
        ├─rsyslogd───3*[{rsyslogd}]
        ├─snapd───13*[{snapd}]
        ├─sshd───sshd───sshd───bash─┬─pstree
        │                           └─top
        ├─systemd───(sd-pam)
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-network
        ├─systemd-resolve
        ├─systemd-timesyn───{systemd-timesyn}
        ├─systemd-udevd
        └─unattended-upgr───{unattended-upgr}
```
L'exemple précédent montre que l'utilisateur **ubuntu** a accédé au serveur **ubuntu** par ssh et a lancé depuis le terminal (en ligne de commande donc) deux commandes qui s'exécutent en parallèle `pstree` et `top`. Les processus ont été créés par le processus `bash`.

{{% note normal %}}
`kill` envoie un signal de terminaison aux processus dont le PID est passé en argument.
{{% /note %}}

```bash
ubuntu@serveur-ubuntu:~$ kill 8419
```

## Programmation concurrente

### Processus concurrents

**Remarque :** cette partie nécessite une bonne compréhension des sections 1.4, 1.5 et 1.6 de ce document.


1. Écrire le programme Python suivant : 
```python
from os import getpid

pid = str(getpid())
with open("test.txt", "w") as fichier:
    for i in range(1000):
        fichier.write("{} : {}\n".format(pid, i))
        fichier.flush()
```

2. À quoi sert la fonction `getpid` ?
{{% solution "Réponse" %}}
La fonction `getpid` retourne le PID du processus qui la lance.
{{% /solution %}}

3. À quoi sert la fonction `flush()` ?
{{% solution "Réponse" %}}
La fonction `flush` donne un ordre d'écriture immédiate des caractères dans le fichier.
{{% /solution %}}

4. Prévoir ce que doit contenir le fichier. \
Lancer le programme et vérifier la correction de la prédiction.
{{% solution "Réponse" %}}
Le fichier est constitué de 1000 lignes de la forme `PID : i`.\
La première ligne est par exemple `418 : 0`\
La dernière ligne du même fichier est alors `418 : 999`.
{{% /solution %}}

5. Depuis la console (shell), lancer trois fois le programme en une commande, en plaçant l'exécution de ces programmes en arrière plan (c'est le rôle de l'esperluette `&`).
```bash
python nom_prog.py & python nom_prog.py & python nom_prog.py &
```
Relever les PID des processus.

6. Examiner le contenu du fichier `test.txt` et recommencer plusieurs fois l'opération. Quelles remarques peut-on faire ? Essayer de justifier ce comportement.
{{% solution "Réponse" %}}

- On a l'impression que certaines lignes n'ont été écrites que par certains des processus et le choix du processus qui a écrit la ligne en question semble être aléatoire. Ils semblent s'être réparti les travaux d'écriture alors qu'ils fonctionnent indépendamment les uns des autres !!!

- **Justification.** Chaque processus, lors de l'ouverture du fichier, enregistre la position du curseur d'écriture. À chaque écriture de caractères, ce curseur est avancé du nombre de caractères (octets en fait) correspondant.\
Chaque fois qu'un processus est interrompu par l'ordonnanceur, il conserve en mémoire son état, en particulier la position du curseur au moment de l'interruption. Lorsqu'il est à nouveau appelé par la suite il reprend donc depuis cette position... et peut donc écraser les entrées des autres processus si ces derniers étaient plus avancés.
{{% /solution %}}

{{% note tip %}}
Le fonctionnement multitâches d'un système d'exploitation est un avantage la plupart du temps mais **soulève des problèmes lorsque des processus partagent des ressources** *car un processus ne sait pas qu'il est interrompu et reprend son travail dans l'état même dans son état au moment de l'interruption* sans prendre en compte ce l'action des autres processus sur la ressource partagée.
{{% /note %}}

### Interblocage

{{% note exercise %}}
#### Exemple 1

Trois élèves doivent réaliser lors d'un cours de math un travail à l'aide d'une règle et d'une équerre. Le premier élève n'a apporté qu'une règle, le deuxième qu'une équerre et le troisième a oublié toutes ses affaires.

1. Que devront-ils faire pour réaliser le travail demandé par le professeur ?

2. Des processus peuvent-ils procéder de la sorte (s'il n'ont pas été programmés pour) ?
{{% /note %}}
{{% solution "Réponses" %}}

1. Les élèves doivent discuter et se mettre d'accord sur une stratégie d'utilisation du matériel.

2. Un processus d'enregistrement du son qui utilise une carte fonctionne de façon indépendante d'un processus qui diffuse du son à travers cette même carte réseau. Aucun dialogue n'existe entre les deux.
{{% /solution %}}

{{% note exercise %}}
#### Exemple 2

Sur une route à deux sens, des travaux occupent la moitié de la route. Des véhicules roulant dans les deux sens se sont engagés simultanément et se retrouvent face à face. Plusieurs véhicules les ont suivis ; plus personne ne peut reculer. Le véhicule venant de la gauche occupe la partie de la route dont l'accès serait nécessaire au véhicule venant de la droite et inversement.
{{% /note %}}

{{% note exercise %}}
#### Exercice 3

Le même blocage peut intervenir dans un rond-point lorsque le traffic est dense si personne ne souhaite sortir à la première sortie mais plutôt à la sortie en face de l'entrée.
{{% /note %}}

{{% note tip %}}
*On appelle **interblocage** (**deadlock**) la situation dans laquelle deux processus se bloquent mutuellement : le premier attend l'accès à une ressource mobilisée par le second qui lui-même attend l'accès à une ressource mobilisée par le premier*. \
L'origine de l'interblocage est l'accès exclusif à certaines ressources. 
{{% /note %}}


{{% note normal %}}
#### Exemple d'interblocage

- Un processus $p\_1$ possède un accès exclusif à la ressource $R\_1$ alors qu'un processus $p\_2$ possède un accès exclusif à une ressource $R\_2$. 

- Le processus $p\_1$ a alors besoin d'un accès à la ressource $R\_2$ avant de pouvoir libérer $R\_1$. Comme la ressource $R\_2$ est occupée, ce processus est placé dans l'état **En attente**.

- Le processus $p\_2$ passe dans l'état **En exécution** et essaie d'accéder à la ressource $R\_1$, sans avoir encore libéré $R\_2$. Comme $R\_1$ n'a pas encore été libéré par $p\_1$, la ressource n'est pas accessible et $p\_2$ est placé **En attente**.

- Le processus $p\_1$ passe dans l'état **En exécution** et essaie d'accéder à la ressource $R\_2$. cette dernière n'est pas accessible et $p\_1$ est placé **En attente**.

- Le processus $p\_2$ passe dans l'état **En exécution** et essaie d'accéder à la ressource $R\_2$. cette dernière n'est pas accessible et $p\_2$ est placé **En attente**.

- ....
{{% /note %}}

### Illustration d'une situation d'interblocage en Python

1. Écrire le programme suivant :
```python
import threading

def hello(n):
    for i in range(5):
        print("Je suis le thread {} et ma valeur est {}".format(n, i))
    print("Fin du Thread {}".format(n))

for n in range(4):
    t = threading.Thread(target=hello, args=[n])
    t.start()
```

2. Étudier le programme. Expliquer le rôle des deux dernières lignes.
{{% solution "Réponse" %}}
Ce programme utilise des threads pour réaliser l'exécution en parallèle de la fonction `hello`.
{{% /solution %}}

3. Exécuter le programme. L'affichage est-il surprenant ?
{{% solution "Réponse" %}}
Comme pour les processus, les threads alternent leur exécution en fonction des commutations de contexte. L'ordre dans lequel sont démarrés les threads ne donne aucune indication sur l'ordre dans lequel ils peuvent se terminer.
{{% /solution %}}

4. Écrire le programme suivant :
```python
import threading
COMPTEUR = 0

def incr():
    global COMPTEUR
    for c in range(100000):
        v = COMPTEUR
        COMPTEUR = v + 1

th = []
for n in range(4):
    t = threading.Thread(target=incr, args=[])
    t.start()
    th.append(t)

for t in th:
    t.join()
print("Valeur finale : {}".format(COMPTEUR))
``` 

5. Expliquer le rôle de l'instruction `global COMPTEUR`.
{{% solution "Réponse" %}}
`COMPTEUR` est une variable globale, accessible depuis une fonction mais non modifiable.\
Pour outrepasser ce comportement, il faut utiliser le mot clé `globla`. On peut alors modifier la valeur de la variable depuis la fonction.
{{% /solution %}}

6. Expliquer le rôle de l'instruction `t.join()`.
{{% solution "Réponse" %}}
Attend que le fil d'exécution se termine. Ceci bloque le fil appelant jusqu'à ce que le fil dont la méthode `join` est appelée se termine – soit normalement, soit par une exception non gérée – ou jusqu'à ce que le délai optionnel timeout soit atteint.
{{% /solution %}}

7. Exécuter le programme. L'affichage est-il surprenant ?
{{% solution "Réponse" %}}
Comme on a démarré 4 threads et que chacun d'eux effectue 100 000 tours de boucles, on pouvait s'attendre à ce que la valeur finale soit égale à 400 000. Ce n'est pas le cas.
{{% /solution %}}

8. Expliquer la valeur finale obtenue.
{{% solution "Réponse" %}}
**Lorsqu'un thread est interrompu par la commutation de contexte, son état est conservé**. Lorsque ce thread reprend son travail, il utilise la valeur de `COMPTEUR` lors de son arrêt et ne prend pas en compte les incrémentations réalisées par les autres threads alors qu'il était dans l'état **En attente**.
{{% /solution %}}

{{% note normal %}}
Un **verrou** est un objet que l'on peut essayer d'acquérir. Si on est le premier à faire cette demande, on acquiert le verrou. On peut le rendre à tout moment. Si en revanche quelqu'un d'autre détient le verrou, on est bloqué jusqu'à ce que ce verrou soit libéré.
{{% /note %}}

9. Écrire le programme suivant :
```python
import threading
verrou = threading.Lock()
COMPTEUR = 0

def incr():
    global COMPTEUR
    for c in range(100000):
        verrou.acquire()
        v = COMPTEUR
        COMPTEUR = v + 1
        verrou.release()

th = []
for n in range(4):
    t = threading.Thread(target=incr, args=[])
    t.start()
    th.append(t)

for t in th:
    t.join()
print("Valeur finale : {}".format(COMPTEUR))
```

10. Expliquer pourquoi on obtient bien maintenant la valeur 400000.

11. Écrire le programme suivant :
```python
import threading

verrou1 = threading.Lock()
verrou2 = threading.Lock()

def f1():
    verrou1.acquire()
    print("Section critique 1.1")
    verrou2.acquire()
    print("Section critique 1.2")
    verrou2.release()
    verrou1.release()

def f2():
    verrou2.acquire()
    print("Section critique 2.1")
    verrou1.acquire()
    print("Section critique 2.2")
    verrou1.release()
    verrou2.release()

t1 = threading.Thread(target=f1, args=[])
t2 = threading.Thread(target=f2, args=[])
t1.start()
t2.start()
```

12. Quelle situation essaie-t-il d'illustrer ? Justifier la réponse.

13. Exécuter le programme plusieurs fois. La situation prévue à la question précédente intervient-elle vraiment ? Pourquoi ?

14. Ajouter les lignes 
```python
for i in range(100000):
    continue
``` 
au dessous de l'instruction `print("Section critique 1.1")`. \
Expliquer pourquoi le comportement du programme a été modifié.



## À retenir

{{% note tip %}}
Les systèmes d'exploitation multitâches sont la norme. Ils permettent d'exécuter de façon **concurrente** plusieurs programmes. L'exécution d'un programme s'appelle un **processus**. C'est le système d'exploitation, et en particulier l'**ordonnanceur**, qui determine quel processus s'exécute à un instant donné. Le fait pour un processus d'être interrompu s'appelle une **commutation de contexte**. Plusieurs processus s'exécutant de façon concurrente peuvent s'**interbloquer** s'ils attendent un accès à une même ensemble de **ressources en accès exclusif**. Les **threads** ou **processus légers** sont des « sous-processus » s'exécutant de manière concurrente. L'accès à des ressources par plusieurs threads peut être protégé par des **verrous**.
{{% /note %}}