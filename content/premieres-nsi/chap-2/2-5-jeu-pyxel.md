---
title: "Un premier jeu avec Pyxel"
subtitle: "Doc. 2,5"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["Pyxel", "fonction", "paramètre", "argument", "valeur renvoyée", "if", "for", "range", "while", "constante", "variable locale", "variable globale", "global", "booléen"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: false
auto_numbering: true
weight: 50
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-2/2-5/2-5-enonce.pdf" >}}

{{< note goal >}}
En construisant pas à pas un petit jeu avec la bibliothèque Pyxel, vous allez réinvestir les fonctions, les instructions conditionnelles et les boucles dans un vrai programme, et découvrir la différence entre variables locales et variables globales.
{{< /note >}}

Dans le jeu final, le joueur est un carré vert posé sur un sol. Il se déplace avec les flèches du clavier et doit attraper des cibles jaunes qui apparaissent au hasard. Chaque cible attrapée rapporte un point ; la partie est gagnée à 10 points.

Le programme de départ est fourni dans l'activité Capytale. Lorsqu'une question commence par « Sans exécuter le programme », il faut écrire sa réponse avant de lancer le programme, puis vérifier.

## Découverte de Pyxel

Voici le programme de départ :

```python
import pyxel

LARGEUR = 160
HAUTEUR = 120

def update():
    pass

def draw():
    pyxel.cls(0)
    pyxel.text(50, 60, "Bonjour NSI !", 7)

pyxel.init(LARGEUR, HAUTEUR, title="Mon premier jeu")
pyxel.run(update, draw)
```

Un programme Pyxel contient deux fonctions particulières. La fonction `update()` fait évoluer l'état du jeu (position des personnages, score…) ; la fonction `draw()` dessine cet état à l'écran. L'instruction `pyxel.run(update, draw)` lance le jeu : à partir de ce moment, Pyxel appelle `update()` puis `draw()` à chaque nouvelle image, jusqu'à la fermeture de la fenêtre.

{{< question >}}
Lancer le programme, puis modifier successivement les trois nombres de l'instruction `pyxel.text(50, 60, "Bonjour NSI !", 7)`.

1. Que représente chacun de ces nombres ?
1. Où se trouve l'origine du repère ? Dans quel sens augmentent les coordonnées $x$ et $y$ ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `50` et `60` sont les coordonnées $x$ et $y$, en pixels, du coin supérieur gauche du texte. `7` est le numéro de la couleur dans la palette de Pyxel (16 couleurs numérotées de 0 à 15 ; la couleur 7 est le blanc).
1. L'origine est le coin supérieur gauche de la fenêtre. $x$ augmente vers la droite et $y$ augmente vers le bas, contrairement au repère utilisé en mathématiques.
{{< /solution >}}

{{< question >}}
Chaque caractère occupe 4 pixels de large et 6 pixels de haut. Calculer les coordonnées à donner à `pyxel.text` pour que le message « Bonjour NSI ! » apparaisse dans le coin inférieur droit de la fenêtre, puis vérifier.
{{< /question >}}

{{< solution "Réponse" >}}
Le message compte 13 caractères (espaces et point d'exclamation compris), soit $13 \times 4 = 52$ pixels de large. Il faut donc $x = 160 - 52 = 108$ et $y = 120 - 6 = 114$.
{{< /solution >}}

{{< question >}}
Le programme définit les fonctions `update` et `draw`, mais on ne trouve nulle part l'instruction `draw()`. Pourtant le texte s'affiche.

1. Qui appelle la fonction `draw` ?
1. Pourquoi écrit-on `pyxel.run(update, draw)` et non `pyxel.run(update(), draw())` ?
{{< /question >}}

{{< solution "Réponse" >}}
1. C'est la fonction `pyxel.run` qui appelle `draw`, à chaque image.
1. Sans parenthèses, on transmet à `pyxel.run` les fonctions elles-mêmes, que Pyxel pourra appeler quand il le faudra. Avec les parenthèses, Python appellerait `update` et `draw` une seule fois, avant de lancer le jeu, et transmettrait leurs valeurs renvoyées (`None`) : Pyxel n'aurait plus de fonctions à appeler.
{{< /solution >}}

{{< question >}}
Remplacer l'instruction `pyxel.text(...)` par `pyxel.text(50, 60, str(pyxel.frame_count), 7)`. La variable `pyxel.frame_count` contient le nombre d'images affichées depuis le lancement du programme.

À l'aide d'un chronomètre, estimer le nombre de fois où la fonction `draw` est appelée en une seconde.
{{< /question >}}

{{< solution "Réponse" >}}
Environ 30 fois par seconde. Par défaut, Pyxel affiche 30 images par seconde ; cette valeur peut être modifiée avec le paramètre `fps` de `pyxel.init`.
{{< /solution >}}

{{< question >}}
Sans exécuter le programme, prévoir ce qui se passe si l'on supprime l'instruction `pyxel.cls(0)`. Vérifier, puis expliquer le rôle de `pyxel.cls`.
{{< /question >}}

{{< solution "Réponse" >}}
Pyxel n'efface pas l'écran de lui-même : chaque nombre est écrit par-dessus les précédents, et on obtient rapidement une tache illisible. `pyxel.cls(col)` remplit tout l'écran avec la couleur `col`, ce qui efface l'image précédente avant de dessiner la nouvelle.
{{< /solution >}}

{{< qcm >}}
- question: 'Dans la fenêtre Pyxel, où se trouve l''origine du repère, et dans quel sens augmente $y$ ?'
  reponses:
    - 'En bas à gauche ; $y$ augmente vers le haut.'
    - 'En haut à gauche ; $y$ augmente vers le bas.'
    - 'Au centre de la fenêtre ; $y$ augmente vers le haut.'
  bonne: 2
  explication: 'Comme pour la plupart des écrans, l''origine est le coin supérieur gauche : $x$ augmente vers la droite et $y$ vers le bas.'
- question: 'Pourquoi écrit-on `pyxel.run(update, draw)` et non `pyxel.run(update(), draw())` ?'
  reponses:
    - 'Les deux écritures sont équivalentes.'
    - 'On transmet les fonctions elles-mêmes, que Pyxel appellera à chaque image ; avec des parenthèses, on les appellerait une seule fois et on transmettrait leur résultat.'
    - 'Les parenthèses sont interdites dans les arguments d''une fonction.'
  bonne: 2
  explication: 'Écrire `draw` désigne la fonction ; écrire `draw()` l''appelle. C''est Pyxel qui appelle `update` et `draw`, environ 30 fois par seconde.'
- question: 'Quel est le rôle de `pyxel.cls(0)` au début de `draw()` ?'
  reponses:
    - 'Fermer la fenêtre.'
    - 'Effacer l''écran en le remplissant avec la couleur 0, avant de redessiner l''image.'
    - 'Remettre le compteur d''images à zéro.'
  bonne: 2
  explication: 'Sans effacement, chaque nouvelle image se superposerait aux précédentes : un objet qui se déplace laisserait une trace.'
{{< /qcm >}}

## Le joueur

Pour que le programme reste lisible et facile à modifier, les valeurs numériques ne sont pas écrites directement dans les instructions. Elles sont rangées au début du programme dans des variables au nom explicite. Ajouter, sous `HAUTEUR` :

```python
TAILLE_JOUEUR = 8
COULEUR_JOUEUR = 11

x_joueur = 76
y_joueur = 100
```

L'instruction `pyxel.rect(x, y, l, h, col)` dessine un rectangle plein de largeur `l`, de hauteur `h` et de couleur `col`, dont le coin supérieur gauche a pour coordonnées `(x, y)`.

{{< question >}}
Écrire une fonction `dessiner_joueur()`, sans paramètre, qui dessine le joueur : un carré de côté `TAILLE_JOUEUR`, de couleur `COULEUR_JOUEUR`, dont le coin supérieur gauche a pour coordonnées `(x_joueur, y_joueur)`. Remplacer ensuite, dans `draw()`, l'affichage du texte par un appel à cette fonction.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def dessiner_joueur():
    pyxel.rect(x_joueur, y_joueur, TAILLE_JOUEUR, TAILLE_JOUEUR, COULEUR_JOUEUR)

def draw():
    pyxel.cls(0)
    dessiner_joueur()
```
{{< /solution >}}

{{< question >}}
La valeur 76 place le joueur au milieu de l'écran, dans le sens horizontal.

1. Pourquoi n'a-t-on pas choisi 80, qui est la moitié de 160 ?
1. Remplacer 76 par une expression qui utilise `LARGEUR` et `TAILLE_JOUEUR`.
1. Pourquoi utiliser l'opérateur `//` plutôt que `/` dans cette expression ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `x_joueur` est l'abscisse du bord gauche du carré. Avec 80, le bord gauche serait au milieu et le carré serait décalé vers la droite. Pour que le centre du carré soit au milieu, il faut reculer d'une demi-taille : $80 - 4 = 76$.
1. `x_joueur = (LARGEUR - TAILLE_JOUEUR) // 2`.
1. `/` donne toujours un flottant (`76.0`), alors qu'une coordonnée de pixel est un nombre entier. `//` donne un entier (`76`).
{{< /solution >}}

{{< question >}}
Remplacer `LARGEUR = 160` par `LARGEUR = 200` et relancer le programme.

1. Qu'est-ce qui a changé sans qu'il soit nécessaire de modifier une autre ligne ?
1. Que faudrait-il faire si le nombre 160 avait été écrit partout dans le programme ?
{{< /question >}}

{{< solution "Réponse" >}}
1. La fenêtre est plus large et le joueur est toujours au milieu, car sa position de départ est calculée à partir de `LARGEUR`.
1. Il faudrait retrouver et modifier chaque 160 à la main, avec le risque d'en oublier un, ou de modifier un 160 qui n'a rien à voir avec la largeur.
{{< /solution >}}

{{< note success "Constantes" >}}
Une variable dont la valeur ne change pas pendant l'exécution du programme est appelée une **constante**. Par convention, en Python, son nom s'écrit en majuscules (`LARGEUR`, `TAILLE_JOUEUR`). Python n'interdit pas de la modifier : c'est une convention entre programmeurs. Regrouper les constantes au début du programme permet de changer une valeur en un seul endroit.
{{< /note >}}

{{< question >}}
Dans `draw()`, remplacer `dessiner_joueur()` par `dessiner_joueur`, sans les parenthèses. Que se passe-t-il ? Faire le lien avec l'instruction `pyxel.run(update, draw)` et formuler la différence entre **désigner** une fonction et **appeler** une fonction.
{{< /question >}}

{{< solution "Réponse" >}}
Aucune erreur n'apparaît, mais le joueur n'est plus dessiné. Sans parenthèses, Python désigne la fonction par son nom sans l'exécuter, comme dans `pyxel.run(update, draw)`. Avec les parenthèses, la fonction est appelée : les instructions de son corps sont exécutées.
{{< /solution >}}

{{< qcm >}}
- question: 'Que désigne, par convention, un nom écrit en majuscules comme `LARGEUR` ?'
  reponses:
    - 'Une constante : une variable dont la valeur ne change pas pendant l''exécution.'
    - 'Une variable que Python interdit de modifier.'
    - 'Une fonction de Pyxel.'
  bonne: 1
  explication: 'C''est une convention entre programmeurs : Python n''empêche pas de la modifier. Regrouper les constantes au début du programme permet de changer une valeur en un seul endroit.'
- question: 'Avec `LARGEUR = 160` et `TAILLE_JOUEUR = 8`, quelle expression centre horizontalement le joueur ?'
  reponses:
    - '`LARGEUR // 2`'
    - '`(LARGEUR - TAILLE_JOUEUR) // 2`'
    - '`LARGEUR / 2 - TAILLE_JOUEUR`'
  bonne: 2
  explication: 'L''abscisse est celle du coin supérieur gauche : on retire la taille du joueur avant de diviser par 2, ce qui donne 76. L''opérateur `//` garantit un résultat entier.'
- question: 'Dans `draw()`, on écrit `dessiner_joueur` au lieu de `dessiner_joueur()`. Que se passe-t-il ?'
  reponses:
    - 'Le joueur est dessiné normalement.'
    - 'Rien n''est dessiné : on désigne la fonction sans l''appeler.'
    - 'Python affiche une erreur de syntaxe.'
  bonne: 2
  explication: 'Sans parenthèses, on désigne la fonction mais on ne l''exécute pas. Seul l''appel, avec parenthèses, exécute son corps.'
{{< /qcm >}}

## Déplacer le joueur : variables locales et globales

L'instruction `pyxel.btn(touche)` renvoie `True` tant que la touche est enfoncée, `False` sinon. Les flèches du clavier sont désignées par `pyxel.KEY_LEFT`, `pyxel.KEY_RIGHT`, `pyxel.KEY_UP` et `pyxel.KEY_DOWN`.

Ajouter la constante `VITESSE = 2` ainsi que la fonction suivante, qui contient volontairement une erreur, puis appeler cette fonction dans `update()` (à la place de `pass`).

```python
def deplacer_joueur():
    if pyxel.btn(pyxel.KEY_LEFT):
        x_joueur = x_joueur - VITESSE
```

{{< question >}}
Lancer le programme, attendre quelques secondes, puis appuyer sur <kbd>←</kbd>.

1. Quel message d'erreur obtient-on ? Quelle ligne est en cause ?
1. Pourquoi l'erreur n'apparaît-elle pas dès le lancement du programme ?
{{< /question >}}

{{< solution "Réponse" >}}
1. On obtient une erreur `UnboundLocalError`, avec un message du type « cannot access local variable 'x_joueur' where it is not associated with a value » (le texte exact dépend de la version de Python). La ligne en cause est `x_joueur = x_joueur - VITESSE`.
1. Cette ligne n'est exécutée que si la condition est vraie, c'est-à-dire lorsque la touche <kbd>←</kbd> est enfoncée.
{{< /solution >}}

Dans une fonction, une variable qui reçoit une valeur par une affectation est considérée par Python comme une variable **locale** : elle n'existe que pendant l'exécution de la fonction et n'a aucun lien avec la variable de même nom définie au début du programme. Ici, pour calculer `x_joueur - VITESSE`, Python cherche la variable locale `x_joueur`, qui n'a encore reçu aucune valeur : d'où l'erreur.

Pour modifier une variable définie au début du programme, appelée variable **globale**, il faut l'annoncer au début de la fonction avec le mot-clé `global`.

{{< note success "Variables locales et variables globales" >}}
- Une variable définie en dehors de toute fonction est une variable **globale**. Toute fonction peut lire sa valeur.
- Une variable qui reçoit une valeur à l'intérieur d'une fonction est une variable **locale** à cette fonction.
- Pour qu'une fonction puisse modifier une variable globale, il faut écrire `global nom_de_la_variable` au début du corps de la fonction.
{{< /note >}}

{{< question >}}
Ajouter la ligne `global x_joueur, y_joueur` au début de `deplacer_joueur()`, puis compléter cette fonction pour que le joueur se déplace dans les quatre directions.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def deplacer_joueur():
    global x_joueur, y_joueur

    if pyxel.btn(pyxel.KEY_LEFT):
        x_joueur = x_joueur - VITESSE

    if pyxel.btn(pyxel.KEY_RIGHT):
        x_joueur = x_joueur + VITESSE

    if pyxel.btn(pyxel.KEY_UP):
        y_joueur = y_joueur - VITESSE

    if pyxel.btn(pyxel.KEY_DOWN):
        y_joueur = y_joueur + VITESSE
```
{{< /solution >}}

{{< question >}}
La fonction `dessiner_joueur()` utilise `x_joueur` et `y_joueur`, et la fonction `deplacer_joueur()` utilise `VITESSE`, sans aucune déclaration `global`. Pourquoi cela ne provoque-t-il pas d'erreur ?
{{< /question >}}

{{< solution "Réponse" >}}
Ces fonctions ne font que lire la valeur de ces variables, sans leur affecter de nouvelle valeur. Une fonction peut toujours lire une variable globale ; `global` n'est nécessaire que pour la modifier.
{{< /solution >}}

{{< question >}}
1. Maintenir les touches <kbd>→</kbd> et <kbd>↑</kbd> enfoncées en même temps. Qu'observe-t-on ?
1. Un élève propose de remplacer les quatre `if` par une structure `if … elif … elif … elif …`. Sans exécuter le programme, prévoir ce qui se passerait avec les mêmes touches, puis vérifier.
{{< /question >}}

{{< solution "Réponse" >}}
1. Le joueur se déplace en diagonale : les deux conditions sont vraies, donc les deux coordonnées sont modifiées.
1. Avec `elif`, seul le bloc de la première condition vraie est exécuté. Le joueur ne se déplacerait que vers la droite (la condition sur <kbd>→</kbd> est testée avant celle sur <kbd>↑</kbd>) : le déplacement en diagonale deviendrait impossible.
{{< /solution >}}

{{< question >}}
Sans exécuter le programme, calculer le nombre de pixels parcourus en une seconde lorsque la touche <kbd>→</kbd> reste enfoncée, puis le temps nécessaire pour traverser l'écran de gauche à droite. Vérifier avec un chronomètre.
{{< /question >}}

{{< solution "Réponse" >}}
`update()` est appelée 30 fois par seconde et le joueur avance de 2 pixels à chaque appel : $2 \times 30 = 60$ pixels par seconde. Pour aller du bord gauche ($x = 0$) au bord droit ($x = 152$), il faut environ $152 / 60 \approx$ 2,5 secondes.
{{< /solution >}}

{{< question >}}
Pourquoi l'appel à `deplacer_joueur()` est-il placé dans `update()` et non dans `draw()` ?
{{< /question >}}

{{< solution "Réponse" >}}
Déplacer le joueur modifie l'état du jeu, ce qui est le rôle de `update()`. La fonction `draw()` doit seulement dessiner l'état du jeu, sans le modifier.
{{< /solution >}}

{{< qcm >}}
- question: 'Une fonction contient `x_joueur = x_joueur - VITESSE` sans déclaration `global`. Que se passe-t-il à l''appel ?'
  reponses:
    - 'La variable globale `x_joueur` est modifiée.'
    - 'Une erreur : Python considère `x_joueur` comme une variable locale, utilisée avant d''avoir reçu une valeur.'
    - 'Rien : l''instruction est ignorée.'
  bonne: 2
  explication: 'Une variable qui reçoit une valeur dans une fonction est locale à cette fonction. Pour modifier la variable globale, il faut écrire `global x_joueur` au début du corps de la fonction.'
- question: 'La fonction `dessiner_joueur()` lit `x_joueur` sans déclaration `global`. Est-ce une erreur ?'
  reponses:
    - 'Oui : `global` est nécessaire pour toute utilisation.'
    - 'Non : toute fonction peut lire une variable globale ; `global` n''est nécessaire que pour la modifier.'
  bonne: 2
  explication: 'Lire une variable globale est toujours possible. La déclaration `global` ne sert qu''aux fonctions qui lui affectent une nouvelle valeur.'
- question: 'Pourquoi l''appel à `deplacer_joueur()` est-il placé dans `update()` et non dans `draw()` ?'
  reponses:
    - '`update()` fait évoluer l''état du jeu ; `draw()` ne fait que dessiner cet état.'
    - '`draw()` n''est jamais appelée.'
    - 'C''est indifférent.'
  bonne: 1
  explication: 'On sépare la logique du jeu (`update`) de son affichage (`draw`) : chaque fonction a une seule tâche.'
{{< /qcm >}}

## Rester dans l'écran

Déplacer le joueur jusqu'au bord de l'écran : il peut en sortir. Il faut donc n'autoriser un déplacement que si le joueur reste entièrement visible.

{{< question >}}
Compléter les conditions suivantes, en n'utilisant que des variables (aucun nombre sauf 0) :

```python
if pyxel.btn(pyxel.KEY_LEFT) and ................:
if pyxel.btn(pyxel.KEY_RIGHT) and ................:
if pyxel.btn(pyxel.KEY_UP) and ................:
if pyxel.btn(pyxel.KEY_DOWN) and ................:
```

Expliquer pourquoi la condition sur le bord droit doit tenir compte de la taille du joueur, alors que celle sur le bord gauche n'en tient pas compte.
{{< /question >}}

{{< solution "Réponse" >}}
```python
if pyxel.btn(pyxel.KEY_LEFT) and x_joueur > 0:
if pyxel.btn(pyxel.KEY_RIGHT) and x_joueur < LARGEUR - TAILLE_JOUEUR:
if pyxel.btn(pyxel.KEY_UP) and y_joueur > 0:
if pyxel.btn(pyxel.KEY_DOWN) and y_joueur < HAUTEUR - TAILLE_JOUEUR:
```
`x_joueur` repère le bord gauche du carré : il suffit qu'il ne devienne pas négatif. Le bord droit du carré se trouve `TAILLE_JOUEUR` pixels plus loin ; pour qu'il reste dans l'écran, `x_joueur` ne doit pas dépasser `LARGEUR - TAILLE_JOUEUR`, soit 152.
{{< /solution >}}

{{< question >}}
Remplacer `VITESSE = 2` par `VITESSE = 3`.

1. Sans exécuter le programme, écrire les valeurs successives de `x_joueur` lorsque le joueur part de 76 et que la touche <kbd>←</kbd> reste enfoncée. Le joueur reste-t-il dans l'écran ?
1. Modifier les quatre conditions pour que le joueur ne sorte jamais de l'écran, quelle que soit la valeur de `VITESSE`. Revenir ensuite à `VITESSE = 2`.
{{< /question >}}

{{< solution "Réponse" >}}
1. 76, 73, 70, …, 7, 4, 1, puis $-2$. Lorsque `x_joueur` vaut 1, la condition `x_joueur > 0` est vraie : le joueur recule de 3 pixels et sort de l'écran de 2 pixels. Avec une vitesse de 2, le problème n'apparaissait pas, car 76 est pair : le joueur tombait exactement sur 0.
1. Il faut tester la position **après** le déplacement :
   ```python
   if pyxel.btn(pyxel.KEY_LEFT) and x_joueur - VITESSE >= 0:
   if pyxel.btn(pyxel.KEY_RIGHT) and x_joueur + VITESSE <= LARGEUR - TAILLE_JOUEUR:
   if pyxel.btn(pyxel.KEY_UP) and y_joueur - VITESSE >= 0:
   if pyxel.btn(pyxel.KEY_DOWN) and y_joueur + VITESSE <= HAUTEUR - TAILLE_JOUEUR:
   ```
{{< /solution >}}

{{< qcm >}}
- question: 'Le joueur va vers la gauche avec la touche ←. Quelle condition l''empêche de sortir de l''écran ?'
  reponses:
    - '`if pyxel.btn(pyxel.KEY_LEFT) and x_joueur > 0:`'
    - '`if pyxel.btn(pyxel.KEY_LEFT) or x_joueur > 0:`'
    - '`if pyxel.btn(pyxel.KEY_LEFT) and x_joueur < LARGEUR:`'
  bonne: 1
  explication: 'On ne recule que si la touche est enfoncée **et** que le joueur n''est pas déjà au bord gauche (abscisse 0).'
- question: 'Avec `VITESSE = 3`, le joueur part de `x_joueur = 76` vers la gauche. La condition `x_joueur > 0` suffit-elle à le garder dans l''écran ?'
  reponses:
    - 'Oui, toujours.'
    - 'Non : de 1, il passe à $-2$ ; il faut tester `x_joueur - VITESSE >= 0`.'
  bonne: 2
  explication: '76, 73, …, 4, 1, puis $-2$ : la condition `1 > 0` est vraie, et le déplacement fait sortir le joueur. Il faut tester la position après le déplacement.'
{{< /qcm >}}

## La cible : une fonction avec des paramètres

L'instruction `pyxel.circ(x, y, r, col)` dessine un disque de centre `(x, y)`, de rayon `r` et de couleur `col`. Ajouter les constantes et les variables suivantes :

```python
RAYON_CIBLE = 4
COULEUR_CIBLE = 10

x_cible = 80
y_cible = 30
```

puis la fonction ci-dessous, et l'instruction `dessiner_cible(x_cible, y_cible)` dans `draw()`.

```python
def dessiner_cible(x, y):
    pyxel.circ(x, y, RAYON_CIBLE, COULEUR_CIBLE)
```

{{< question >}}
Dans la définition `def dessiner_cible(x, y):` et dans l'appel `dessiner_cible(x_cible, y_cible)` :

1. identifier les paramètres et les arguments ;
1. indiquer la valeur de `x` et celle de `y` pendant l'exécution de cet appel.
{{< /question >}}

{{< solution "Réponse" >}}
1. `x` et `y` sont les **paramètres** : ce sont des variables locales à la fonction. `x_cible` et `y_cible` sont les **arguments** : leurs valeurs sont transmises aux paramètres au moment de l'appel.
1. `x` vaut 80 et `y` vaut 30.
{{< /solution >}}

{{< question >}}
Sans exécuter le programme, prévoir le résultat de chacun des appels suivants, placés dans `draw()`, puis vérifier.

1. `dessiner_cible(20, 20)` suivi de `dessiner_cible(140, 90)` ;
1. `dessiner_cible(y_cible, x_cible)` ;
1. `dessiner_cible(20)`.
{{< /question >}}

{{< solution "Réponse" >}}
1. Deux cibles sont dessinées, en $(20, 20)$ et en $(140, 90)$ : la même fonction est réutilisée avec d'autres arguments.
1. La cible est dessinée en $(30, 80)$ : le premier argument est toujours transmis au premier paramètre, quel que soit son nom.
1. Erreur `TypeError: dessiner_cible() missing 1 required positional argument: 'y'` : il manque une valeur pour le paramètre `y`.
{{< /solution >}}

{{< question >}}
Ajouter à la fonction `dessiner_cible` un troisième paramètre `couleur`, puis modifier l'appel dans `draw()` pour que la cible soit toujours dessinée avec la couleur `COULEUR_CIBLE`. Vérifier en affichant une deuxième cible d'une autre couleur, puis la supprimer.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def dessiner_cible(x, y, couleur):
    pyxel.circ(x, y, RAYON_CIBLE, couleur)
```
Dans `draw()` : `dessiner_cible(x_cible, y_cible, COULEUR_CIBLE)`.
{{< /solution >}}

{{< qcm >}}
- question: 'Pour la définition `def dessiner_cible(x, y):` et l''appel `dessiner_cible(x_cible, y_cible)`, quels sont les paramètres ?'
  reponses:
    - '`x_cible` et `y_cible`'
    - '`x` et `y`'
    - '`dessiner_cible`'
  bonne: 2
  explication: 'Les paramètres sont les noms de la définition ; `x_cible` et `y_cible` sont les arguments. Pendant l''appel, `x` reçoit la valeur de `x_cible` et `y` celle de `y_cible`.'
- question: 'Que se passe-t-il avec l''appel `dessiner_cible(20)` ?'
  reponses:
    - 'La cible est dessinée en $(20, 0)$.'
    - 'Une erreur : il manque un argument.'
    - 'La cible est dessinée en $(20, 20)$.'
  bonne: 2
  explication: 'Une fonction attend autant d''arguments qu''elle a de paramètres : ici deux.'
- question: 'Que dessine l''appel `dessiner_cible(y_cible, x_cible)` ?'
  reponses:
    - 'La même cible, l''ordre des arguments n''a pas d''importance.'
    - 'Une cible dont l''abscisse et l''ordonnée sont échangées.'
  bonne: 2
  explication: 'Les arguments sont associés aux paramètres dans l''ordre : `x` reçoit ici la valeur de `y_cible`.'
{{< /qcm >}}

## Le sol : une boucle for

Ajouter les constantes et la fonction suivantes, puis appeler `dessiner_sol()` dans `draw()`.

```python
Y_SOL = HAUTEUR - 4
EPAISSEUR_SOL = 2
LARGEUR_DALLE = 6
PAS_DALLES = 8
COULEUR_SOL = 3

def dessiner_sol():
    for x in range(0, LARGEUR, PAS_DALLES):
        pyxel.rect(x, Y_SOL, LARGEUR_DALLE, EPAISSEUR_SOL, COULEUR_SOL)
```

{{< question >}}
Sans exécuter le programme :

1. combien de dalles sont dessinées ?
1. quelles sont les abscisses de la première et de la dernière dalle ?
1. quelle est la largeur de l'espace entre deux dalles voisines ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `x` prend les valeurs 0, 8, 16, …, 152 : il y a $160 / 8 = 20$ dalles.
1. 0 et 152 (160 est exclu).
1. Deux dalles voisines commencent à 8 pixels d'écart et mesurent 6 pixels : l'espace vaut $8 - 6 = 2$ pixels.
{{< /solution >}}

{{< question >}}
Sans exécuter le programme, prévoir l'aspect du sol dans chacun des cas suivants, puis vérifier :

1. `LARGEUR_DALLE = 8` ;
1. `LARGEUR_DALLE = 6` et `PAS_DALLES = 4`.
{{< /question >}}

{{< solution "Réponse" >}}
1. Les dalles se touchent : le sol forme une ligne continue.
1. Il y a 40 dalles, qui se chevauchent (chacune mesure 6 pixels, mais elles commencent tous les 4 pixels) : le sol forme aussi une ligne continue.
{{< /solution >}}

{{< question >}}
Réécrire la fonction `dessiner_sol()` avec une boucle `while` (voir Doc. 2,4). Laquelle des deux versions est la plus adaptée ? Pourquoi ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
def dessiner_sol():
    x = 0
    while x < LARGEUR:
        pyxel.rect(x, Y_SOL, LARGEUR_DALLE, EPAISSEUR_SOL, COULEUR_SOL)
        x = x + PAS_DALLES
```
La boucle `for` est plus adaptée : le nombre de répétitions est connu à l'avance, et elle évite d'écrire soi-même l'initialisation et la mise à jour de `x` (dont l'oubli provoquerait une boucle infinie).
{{< /solution >}}

{{< question >}}
Dans `draw()`, placer l'appel à `dessiner_sol()` avant `pyxel.cls(0)`. Qu'observe-t-on ? Pourquoi ?
{{< /question >}}

{{< solution "Réponse" >}}
Le sol n'apparaît plus : il est dessiné, puis immédiatement effacé par `pyxel.cls(0)`. Dans `draw()`, l'ordre des instructions est l'ordre dans lequel les éléments sont superposés à l'écran.
{{< /solution >}}

{{< question >}}
Le joueur peut descendre dans le sol. Modifier la condition sur la touche <kbd>↓</kbd> pour qu'il s'arrête au-dessus du sol, et la position de départ `y_joueur` pour qu'il soit posé sur le sol au lancement du jeu.
{{< /question >}}

{{< solution "Réponse" >}}
```python
if pyxel.btn(pyxel.KEY_DOWN) and y_joueur + VITESSE <= Y_SOL - TAILLE_JOUEUR:
```
et `y_joueur = Y_SOL - TAILLE_JOUEUR` (soit 108).
{{< /solution >}}

{{< qcm >}}
- question: 'Avec `LARGEUR = 160` et `PAS_DALLES = 8`, combien de dalles dessine la boucle `for x in range(0, LARGEUR, PAS_DALLES):` ?'
  reponses:
    - '20'
    - '21'
    - '19'
  bonne: 1
  explication: '`x` prend les valeurs 0, 8, 16, …, 152 : 160 est exclu, soit $160 / 8 = 20$ valeurs, donc 20 dalles.'
- question: 'Pour dessiner les dalles du sol, quelle boucle est la plus adaptée ?'
  reponses:
    - 'Une boucle `for`, car le nombre de dalles est connu à l''avance.'
    - 'Une boucle `while`, car on ne sait pas quand s''arrêter.'
  bonne: 1
  explication: 'Le nombre de répétitions est connu avant de commencer : la boucle `for` avec `range` est plus simple et ne risque pas d''être infinie.'
- question: 'Dans `draw()`, on appelle `dessiner_sol()` avant `pyxel.cls(0)`. Qu''observe-t-on ?'
  reponses:
    - 'Le sol est dessiné normalement.'
    - 'Le sol n''apparaît pas : il est effacé aussitôt dessiné.'
  bonne: 2
  explication: 'L''ordre des instructions compte : `pyxel.cls` efface tout ce qui a été dessiné avant lui.'
{{< /qcm >}}

## Distance entre deux points : une fonction qui renvoie une valeur

Pour savoir si le joueur attrape la cible, il faut mesurer la distance qui les sépare. La distance entre les points de coordonnées $(x_1, y_1)$ et $(x_2, y_2)$ vaut :

$$d = \sqrt{(x_2 - x_1)^2 + (y_2 - y_1)^2}$$

La racine carrée s'obtient avec la fonction `sqrt` du module `math`, à importer au début du programme : `from math import sqrt`.

{{< question >}}
Écrire une fonction `distance(x1, y1, x2, y2)` qui renvoie la distance entre les points $(x_1, y_1)$ et $(x_2, y_2)$.

Sans exécuter le programme, prévoir la valeur de `distance(0, 0, 3, 4)` et son type. Vérifier en ajoutant temporairement `print(distance(0, 0, 3, 4))` juste après la définition de la fonction.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def distance(x1, y1, x2, y2):
    d = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d
```
D'après le théorème de Pythagore, $\sqrt{3^2 + 4^2} = \sqrt{25} = 5$. Python affiche `5.0` : `sqrt` renvoie toujours un flottant.
{{< /solution >}}

{{< question >}}
Un élève a écrit une fonction qui affiche la distance au lieu de la renvoyer :

```python
def distance_affichee(x1, y1, x2, y2):
    print(sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
```

1. Sans exécuter le programme, prévoir le résultat de `print(distance_affichee(0, 0, 3, 4) + 1)`, puis vérifier.
1. Pourquoi cette fonction ne peut-elle pas servir dans le jeu ?
{{< /question >}}

{{< solution "Réponse" >}}
1. Python affiche d'abord `5.0` pendant l'appel de la fonction, puis s'arrête sur l'erreur `TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'`. Une fonction sans `return` renvoie `None`, qu'on ne peut pas additionner à un entier.
1. Le jeu a besoin de la valeur de la distance pour la comparer à un seuil. Une valeur affichée à l'écran ne peut pas être réutilisée par le programme ; seule une valeur renvoyée le peut.
{{< /solution >}}

{{< qcm >}}
- question: 'Que renvoie `distance(0, 0, 3, 4)` ?'
  reponses:
    - '`5.0`'
    - '`7`'
    - '`25`'
  bonne: 1
  explication: '$\sqrt{3^2 + 4^2} = \sqrt{25} = 5$. La fonction `sqrt` renvoie toujours un `float` : `5.0`.'
- question: 'Une fonction `distance_affichee` contient `print(...)` mais pas de `return`. Que vaut `distance_affichee(0, 0, 3, 4)` ?'
  reponses:
    - '`5.0`'
    - '`None`'
    - 'Une erreur.'
  bonne: 2
  explication: 'La fonction affiche 5.0, mais ne renvoie rien : sa valeur est `None`. On ne peut donc pas réutiliser le résultat dans un calcul ou une comparaison.'
{{< /qcm >}}

## La cible est-elle attrapée ? Une fonction qui renvoie un booléen

On considère la fonction suivante :

```python
def cible_attrapee():
    d = distance(x_joueur + 4, y_joueur + 4, x_cible, y_cible)
    return d < 8
```

{{< question >}}
1. Pourquoi ajoute-t-on 4 aux coordonnées du joueur ?
1. Justifier la valeur 8, en s'appuyant sur un schéma.
1. Réécrire la fonction en remplaçant les nombres 4 et 8 par des expressions qui utilisent les constantes `TAILLE_JOUEUR` et `RAYON_CIBLE`.
{{< /question >}}

{{< solution "Réponse" >}}
1. `(x_joueur, y_joueur)` est le coin supérieur gauche du carré. En ajoutant la moitié du côté, soit 4, on obtient son centre. On compare ainsi le centre du joueur au centre de la cible.
1. Le carré et la cible se touchent lorsque la distance entre leurs centres vaut la demi-taille du carré plus le rayon de la cible : $4 + 4 = 8$. Ce calcul est exact lorsque la cible arrive par un côté du carré, et approché lorsqu'elle arrive par un coin.
1. ```python
   def cible_attrapee():
       demi_taille = TAILLE_JOUEUR // 2
       d = distance(x_joueur + demi_taille, y_joueur + demi_taille, x_cible, y_cible)
       return d < demi_taille + RAYON_CIBLE
   ```
{{< /solution >}}

{{< question >}}
1. Quelles valeurs la fonction `cible_attrapee()` peut-elle renvoyer ?
1. Un élève a écrit la fin de la fonction ainsi :
   ```python
   if d < 8:
       return True
   else:
       return False
   ```
   Les deux versions sont-elles équivalentes ? Laquelle préférer ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `True` ou `False` : `d < 8` est une expression booléenne.
1. Elles sont équivalentes. La version `return d < 8` est préférable : l'expression `d < 8` est déjà un booléen, il suffit de renvoyer sa valeur.
{{< /solution >}}

{{< question >}}
Dans `draw()`, afficher le texte « Touché ! » en haut de l'écran lorsque le joueur touche la cible. Tester.
{{< /question >}}

{{< solution "Réponse" >}}
```python
if cible_attrapee():
    pyxel.text(5, 5, "Touché !", 7)
```
Une fonction qui renvoie un booléen s'utilise directement comme condition d'un `if`.
{{< /solution >}}

{{< qcm >}}
- question: 'La fonction se termine par `return d < 8`. Que renvoie-t-elle ?'
  reponses:
    - 'Un nombre.'
    - 'Un booléen : `True` ou `False`.'
    - 'Rien.'
  bonne: 2
  explication: '`d < 8` est une expression booléenne : son évaluation donne directement `True` ou `False`.'
- question: 'Les écritures `return d < 8` et `if d < 8: return True` / `else: return False` sont-elles équivalentes ?'
  reponses:
    - 'Oui, mais la première est plus simple : la comparaison est déjà un booléen.'
    - 'Non, la première renvoie toujours `True`.'
  bonne: 1
  explication: 'Inutile d''écrire un `if` pour renvoyer `True` ou `False` : on renvoie directement la valeur de la condition.'
{{< /qcm >}}

## Faire apparaître une nouvelle cible

L'instruction `pyxel.rndi(a, b)` renvoie un entier choisi au hasard entre `a` et `b`, bornes comprises. Un disque de centre `(x, y)` et de rayon `r` occupe les pixels d'abscisse `x - r` à `x + r` ; les pixels de l'écran ont des abscisses comprises entre 0 et `LARGEUR - 1`.

{{< question >}}
1. Déterminer les valeurs minimale et maximale de `x_cible` pour que la cible soit entièrement visible. Faire de même pour `y_cible`, en imposant que la cible reste au-dessus du sol.
1. Écrire une fonction `nouvelle_cible()` qui donne à la cible une position choisie au hasard, entièrement visible.
1. Dans `update()`, appeler `nouvelle_cible()` lorsque la cible est attrapée. Tester.
{{< /question >}}

{{< solution "Réponse" >}}
1. `x_cible` doit vérifier `x_cible - RAYON_CIBLE >= 0` et `x_cible + RAYON_CIBLE <= LARGEUR - 1`, donc être compris entre `RAYON_CIBLE` et `LARGEUR - 1 - RAYON_CIBLE` (de 4 à 155). De même, `y_cible` est compris entre `RAYON_CIBLE` et `Y_SOL - 1 - RAYON_CIBLE` (de 4 à 111).
1. ```python
   def nouvelle_cible():
       global x_cible, y_cible

       x_cible = pyxel.rndi(RAYON_CIBLE, LARGEUR - 1 - RAYON_CIBLE)
       y_cible = pyxel.rndi(RAYON_CIBLE, Y_SOL - 1 - RAYON_CIBLE)
   ```
   `global` est nécessaire, car la fonction modifie `x_cible` et `y_cible`.
1. ```python
   def update():
       deplacer_joueur()
       if cible_attrapee():
           nouvelle_cible()
   ```
{{< /solution >}}

{{< question >}}
Il peut arriver que la nouvelle cible apparaisse directement sur le joueur.

1. Que se passe-t-il dans ce cas ?
1. Pour l'éviter, il faut tirer une nouvelle position tant que la cible touche le joueur. Quelle boucle faut-il utiliser ? Pourquoi ?
1. Renommer la fonction de la question précédente en `tirer_position_cible()`, puis écrire une nouvelle fonction `nouvelle_cible()` qui l'utilise.
{{< /question >}}

{{< solution "Réponse" >}}
1. La cible est attrapée aussitôt, sans que le joueur ait bougé.
1. Une boucle `while` : on ne sait pas à l'avance combien de tirages seront nécessaires.
1. ```python
   def nouvelle_cible():
       tirer_position_cible()
       while cible_attrapee():
           tirer_position_cible()
   ```
{{< /solution >}}

{{< qcm >}}
- question: 'On tire une nouvelle position de cible **tant que** la cible touche le joueur. Quelle boucle utiliser ?'
  reponses:
    - '`for`, car on connaît le nombre de tirages.'
    - '`while`, car on ne sait pas à l''avance combien de tirages seront nécessaires.'
  bonne: 2
  explication: 'Le nombre de tirages dépend du hasard : c''est une boucle non déterministe.'
- question: 'Quelle instruction Pyxel donne un entier aléatoire entre `a` et `b`, bornes comprises ?'
  reponses:
    - '`pyxel.rndi(a, b)`'
    - '`range(a, b)`'
    - '`pyxel.rnd(a)`'
  bonne: 1
  explication: '`pyxel.rndi(a, b)` renvoie un entier aléatoire entre `a` et `b`, les deux bornes étant incluses (comme `random.randint`). `range(a, b)` ne tire rien au hasard.'
{{< /qcm >}}

## Le score

Ajouter la variable `score = 0` au début du programme.

{{< question >}}
1. Pourquoi le nom `score` est-il écrit en minuscules, alors que `LARGEUR` est écrit en majuscules ?
1. Modifier `update()` pour que le score augmente de 1 à chaque cible attrapée. Que faut-il ajouter au début de la fonction ?
{{< /question >}}

{{< solution "Réponse" >}}
1. La valeur de `score` change pendant la partie : ce n'est pas une constante.
1. ```python
   def update():
       global score

       deplacer_joueur()
       if cible_attrapee():
           score = score + 1
           nouvelle_cible()
   ```
   `global score` est nécessaire, car `update()` modifie la variable globale `score`.
{{< /solution >}}

{{< question >}}
Remplacer l'affichage de « Touché ! » par celui du score, à l'aide de l'instruction `pyxel.text(5, 5, "Score : " + str(score), 7)`.

1. Pourquoi faut-il écrire `str(score)` ?
1. Réécrire cette instruction à l'aide d'une f-string (voir Doc. 2,2).
1. Faut-il ajouter `global score` dans `draw()` ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `score` est un entier. L'opérateur `+` ne peut pas concaténer une chaîne et un entier (`TypeError: can only concatenate str (not "int") to str`) : `str(score)` convertit l'entier en chaîne.
1. `pyxel.text(5, 5, f"Score : {score}", 7)`.
1. Non : `draw()` lit la valeur de `score` sans la modifier.
{{< /solution >}}

{{< qcm >}}
- question: 'Pourquoi `score` s''écrit-il en minuscules, alors que `LARGEUR` est en majuscules ?'
  reponses:
    - 'Parce que `score` change pendant la partie : ce n''est pas une constante.'
    - 'Parce que Python l''exige pour les nombres.'
    - 'C''est un hasard.'
  bonne: 1
  explication: 'Les majuscules signalent une constante. `score` est une variable globale modifiée au cours du jeu.'
- question: 'Dans `update()`, l''instruction `score += 1` provoque une erreur. Que faut-il ajouter au début de la fonction ?'
  reponses:
    - '`global score`'
    - '`score = 0`'
    - '`return score`'
  bonne: 1
  explication: 'Pour modifier une variable globale dans une fonction, il faut la déclarer avec `global`. Écrire `score = 0` remettrait le score à zéro à chaque image.'
- question: 'Pourquoi écrit-on `"Score : " + str(score)` ?'
  reponses:
    - 'Parce qu''on ne peut pas concaténer une chaîne et un entier.'
    - 'Pour arrondir le score.'
  bonne: 1
  explication: '`+` entre chaînes exige deux `str`. Une f-string fait la conversion automatiquement : `f"Score : {score}"`.'
{{< /qcm >}}

## Gagner la partie

Ajouter la constante `SCORE_GAGNANT = 10` et modifier `update()` pour que le joueur ne puisse plus bouger une fois la partie gagnée :

```python
def update():
    global score

    if score < SCORE_GAGNANT:
        deplacer_joueur()
        if cible_attrapee():
            score = score + 1
            nouvelle_cible()
```

{{< question >}}
Pour tester rapidement la fin de partie, quelle ligne suffit-il de modifier ?
{{< /question >}}

{{< solution "Réponse" >}}
Il suffit de donner une petite valeur à la constante, par exemple `SCORE_GAGNANT = 2`, puis de revenir à 10 une fois les tests terminés.
{{< /solution >}}

{{< question >}}
Un élève a écrit la fonction `draw()` suivante pour afficher « BRAVO ! » au centre de l'écran en fin de partie :

```python
def draw():
    if score < SCORE_GAGNANT:
        pyxel.cls(0)
        dessiner_sol()
        dessiner_cible(x_cible, y_cible, COULEUR_CIBLE)
        dessiner_joueur()
        pyxel.text(5, 5, f"Score : {score}", 7)
    else:
        pyxel.text(LARGEUR // 2, HAUTEUR // 2, "BRAVO !", 7)
```

1. Sans exécuter le programme, prévoir les deux défauts de l'affichage en fin de partie. Vérifier.
1. Corriger la fonction. Pour centrer le texte, utiliser les constantes `pyxel.FONT_WIDTH` et `pyxel.FONT_HEIGHT`, qui valent la largeur (4) et la hauteur (6) d'un caractère, ainsi que la fonction `len`.
{{< /question >}}

{{< solution "Réponse" >}}
1. Premier défaut : l'écran n'est plus effacé en fin de partie (`pyxel.cls(0)` n'est appelée que pendant le jeu), donc « BRAVO ! » s'écrit par-dessus la dernière image du jeu. Second défaut : le texte n'est pas centré, car `(LARGEUR // 2, HAUTEUR // 2)` est la position de son coin supérieur gauche.
1. ```python
   def draw():
       pyxel.cls(0)
       if score < SCORE_GAGNANT:
           dessiner_sol()
           dessiner_cible(x_cible, y_cible, COULEUR_CIBLE)
           dessiner_joueur()
           pyxel.text(5, 5, f"Score : {score}", 7)
       else:
           message = "BRAVO !"
           x = (LARGEUR - len(message) * pyxel.FONT_WIDTH) // 2
           y = (HAUTEUR - pyxel.FONT_HEIGHT) // 2
           pyxel.text(x, y, message, 7)
   ```
   Le message mesure $7 \times 4 = 28$ pixels de large : il est affiché en $(66, 57)$.
{{< /solution >}}

{{< qcm >}}
- question: 'Pour tester rapidement la fin de partie, que suffit-il de modifier ?'
  reponses:
    - 'La valeur de la constante `SCORE_GAGNANT` (par exemple 2).'
    - 'Toutes les conditions du programme.'
    - 'La fonction `draw()`.'
  bonne: 1
  explication: 'C''est tout l''intérêt d''une constante : une seule ligne à modifier.'
- question: 'Une fois la partie gagnée, où doit-on empêcher le joueur de bouger ?'
  reponses:
    - 'Dans `update()`, qui fait évoluer l''état du jeu.'
    - 'Dans `draw()`, en ne dessinant plus le joueur.'
  bonne: 1
  explication: '`update()` gère l''état du jeu ; `draw()` ne fait que l''afficher.'
{{< /qcm >}}

## Quitter et rejouer

L'instruction `pyxel.btnp(touche)` renvoie `True` uniquement au moment où la touche vient d'être enfoncée, et non pendant tout le temps où elle reste enfoncée comme `pyxel.btn`. L'instruction `pyxel.quit()` ferme le jeu.

{{< question >}}
1. Pourquoi utilise-t-on `pyxel.btn` pour déplacer le joueur, et non `pyxel.btnp` ?
1. Modifier `update()` pour que la touche <kbd>Q</kbd> ferme le jeu à tout moment, y compris après la victoire.
{{< /question >}}

{{< solution "Réponse" >}}
1. Avec `pyxel.btnp`, le joueur n'avancerait que d'un pas à chaque appui : il faudrait appuyer à nouveau pour chaque déplacement de 2 pixels.
1. Au début de `update()`, en dehors du bloc `if score < SCORE_GAGNANT:` :
   ```python
   if pyxel.btnp(pyxel.KEY_Q):
       pyxel.quit()
   ```
   Par défaut, la touche <kbd>Échap</kbd> ferme aussi le jeu.
{{< /solution >}}

{{< question >}}
Une fois la partie gagnée, un appui sur <kbd>R</kbd> doit lancer une nouvelle partie : le joueur revient à sa position de départ, le score revient à 0 et une nouvelle cible apparaît.

1. Pour ne pas écrire deux fois la position de départ, créer deux constantes `X_DEPART` et `Y_DEPART`, et les utiliser pour initialiser `x_joueur` et `y_joueur`.
1. Écrire une fonction `nouvelle_partie()`. Quelles variables doivent être déclarées `global` ?
1. Appeler cette fonction dans `update()` au bon endroit.
{{< /question >}}

{{< solution "Réponse" >}}
1. ```python
   X_DEPART = (LARGEUR - TAILLE_JOUEUR) // 2
   Y_DEPART = Y_SOL - TAILLE_JOUEUR

   x_joueur = X_DEPART
   y_joueur = Y_DEPART
   ```
1. ```python
   def nouvelle_partie():
       global x_joueur, y_joueur, score

       x_joueur = X_DEPART
       y_joueur = Y_DEPART
       score = 0
       nouvelle_cible()
   ```
   `x_cible` et `y_cible` n'ont pas à être déclarées ici : elles sont modifiées dans `tirer_position_cible()`, qui les déclare déjà.
1. ```python
   if score < SCORE_GAGNANT:
       ...
   elif pyxel.btnp(pyxel.KEY_R):
       nouvelle_partie()
   ```
{{< /solution >}}

{{< qcm >}}
- question: 'Quelle est la différence entre `pyxel.btn` et `pyxel.btnp` ?'
  reponses:
    - '`btn` est vrai tant que la touche est enfoncée ; `btnp` n''est vrai qu''au moment où elle vient d''être pressée.'
    - 'Il n''y en a aucune.'
    - '`btnp` est réservé à la souris.'
  bonne: 1
  explication: 'Pour un déplacement continu, on utilise `btn`. Pour une action unique (quitter, rejouer), `btnp` évite de répéter l''action à chaque image.'
- question: 'Pour rejouer, le joueur doit revenir à sa position de départ. Comment éviter d''écrire deux fois cette position ?'
  reponses:
    - 'En la stockant dans des constantes (par exemple `X_DEPART`, `Y_DEPART`) utilisées au lancement et au redémarrage.'
    - 'En copiant les nombres aux deux endroits.'
  bonne: 1
  explication: 'Une valeur écrite à un seul endroit ne peut pas devenir incohérente : on la modifie une fois, et tout le programme suit.'
{{< /qcm >}}

## Le programme obtenu

Le programme complet est organisé ainsi :

<div class="etapes">
<div class="etape">constantes, puis variables décrivant l'état du jeu</div>
<div class="etape-fleche">↓</div>
<div class="etape">fonctions réalisant chacune une tâche précise<br>
<code>dessiner_joueur()</code>, <code>dessiner_cible(...)</code>, <code>dessiner_sol()</code>, <code>distance(...)</code>, <code>cible_attrapee()</code>, <code>deplacer_joueur()</code>, <code>tirer_position_cible()</code>, <code>nouvelle_cible()</code>, <code>nouvelle_partie()</code></div>
<div class="etape-fleche">↓</div>
<div class="etape"><code>update()</code> : fait évoluer l'état du jeu</div>
<div class="etape-fleche">↓</div>
<div class="etape"><code>draw()</code> : dessine l'état du jeu</div>
<div class="etape-fleche">↓</div>
<div class="etape"><code>pyxel.init(...)</code> puis <code>pyxel.run(update, draw)</code></div>
</div>

{{< question >}}
Dans votre programme, trouver un exemple de chacune des notions suivantes et le recopier.

| **Notion** | **Exemple dans votre programme** |
|:---|:---|
| Constante |  |
| Définition d'une fonction |  |
| Appel d'une fonction |  |
| Fonction avec paramètres |  |
| Fonction renvoyant une valeur |  |
| Fonction renvoyant un booléen |  |
| Instruction conditionnelle |  |
| Boucle `for` |  |
| Boucle `while` |  |
| Fonction qui modifie une variable globale |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **Notion** | **Exemple** |
|:---|:---|
| Constante | `TAILLE_JOUEUR = 8` |
| Définition d'une fonction | `def dessiner_joueur():` |
| Appel d'une fonction | `dessiner_joueur()` dans `draw()` |
| Fonction avec paramètres | `def dessiner_cible(x, y, couleur):` |
| Fonction renvoyant une valeur | `distance(...)` |
| Fonction renvoyant un booléen | `cible_attrapee()` |
| Instruction conditionnelle | `if cible_attrapee():` |
| Boucle `for` | `for x in range(0, LARGEUR, PAS_DALLES):` |
| Boucle `while` | `while cible_attrapee():` |
| Fonction qui modifie une variable globale | `deplacer_joueur()`, `nouvelle_partie()`… |
{{< /solution >}}

## Défis

Les défis sont classés par difficulté croissante.

{{< question >}}
**Défi A : cible multicolore.** La couleur de la cible change à chaque point marqué.
{{< /question >}}

{{< solution "Réponse" >}}
Dans `draw()` : `dessiner_cible(x_cible, y_cible, 8 + score % 8)`. La couleur varie de 8 à 15 ; on évite ainsi la couleur 0, noire, invisible sur le fond noir.
{{< /solution >}}

{{< question >}}
**Défi B : difficulté croissante.** À partir de 5 points, le joueur se déplace plus vite. `VITESSE` peut-elle rester une constante ?
{{< /question >}}

{{< solution "Réponse" >}}
Non : sa valeur change pendant la partie. On la remplace par une variable `vitesse`, en minuscules, qui vaut 2 au départ. Dans `update()`, lorsque `score >= 5`, on lui donne la valeur 4 (déclarer `global vitesse`). Dans `nouvelle_partie()`, il faut la remettre à 2. Grâce aux conditions écrites dans la partie « Rester dans l'écran », le joueur ne sort pas de l'écran.
{{< /solution >}}

{{< question >}}
**Défi C : temps limité.** La partie dure 30 secondes. Le temps restant est affiché à l'écran ; lorsqu'il atteint 0, la partie est perdue.
{{< /question >}}

{{< solution "Réponse" >}}
À 30 images par seconde, 30 secondes correspondent à 900 images. On mémorise dans une variable globale `debut`, initialisée à 0, la valeur de `pyxel.frame_count` au début de chaque partie (dans `nouvelle_partie()`). Le temps restant, en secondes, vaut `30 - (pyxel.frame_count - debut) // 30`. Le jeu continue tant que ce temps est positif et que le score est inférieur à `SCORE_GAGNANT` ; sinon, on affiche un message de défaite.
{{< /solution >}}

{{< question >}}
**Défi D : deux cibles.** Une deuxième cible, d'une autre couleur, rapporte 3 points.
{{< /question >}}

{{< solution "Réponse" >}}
Il faut deux autres variables `x_cible2` et `y_cible2`. Pour ne pas écrire deux fois les mêmes fonctions, on donne des paramètres à `cible_attrapee(xc, yc)`. Pour les nouvelles positions, `tirer_position_cible()` peut être remplacée par deux fonctions qui renvoient une abscisse et une ordonnée tirées au hasard. Attention : avec des gains de 1 et 3 points, le score peut dépasser `SCORE_GAGNANT` sans lui être égal ; la condition `score < SCORE_GAGNANT` reste correcte.
{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- distinguer la définition d'une fonction de son appel, et désigner une fonction sans l'appeler ;
- utiliser des constantes plutôt que des valeurs numériques écrites dans les instructions ;
- expliquer quand une variable est locale ou globale, et utiliser `global` à bon escient ;
- écrire une condition qui tient compte des dimensions d'un objet ;
- distinguer paramètres et arguments ;
- choisir entre une boucle `for` et une boucle `while` ;
- distinguer une fonction qui renvoie une valeur d'une fonction qui l'affiche ;
- écrire une fonction qui renvoie un booléen et l'utiliser comme condition ;
- utiliser quelques instructions de Pyxel (`text`, `rect`, `circ`, `btn`, `btnp`, `rndi`).
{{< /note >}}
