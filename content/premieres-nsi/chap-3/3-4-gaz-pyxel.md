---
title: "Simuler un gaz avec Pyxel"
subtitle: "Doc. 3,4"
date: 2026-11-16T12:00:00+04:00
draft: false
toc: true
tags: ["Pyxel", "simulation", "gaz parfait", "particule", "tuple", "déballage", "fonction qui renvoie un tuple", "liste de tuples", "liste passée en paramètre", "lambda", "liste en compréhension", "parcours par indice", "boucles imbriquées", "rebond", "collision"]
categories: ["Informatique", "1ère Spé NSI"]
solution_est_visible: false
auto_numbering: true
weight: 40
---
- {{< remote "Énoncé au format pdf" "/premieres-nsi/chap-3/3-4/3-4-enonce.pdf" >}}

{{< note goal >}}
Construire pas à pas avec Pyxel la simulation d'un gaz : chaque particule est un tuple, le gaz est une liste de tuples passée en paramètre aux fonctions.
{{< /note >}}

{{< question >}}
Sur un billard, une bille frappe la bande de droite. Le schéma montre sa vitesse juste avant le choc.

![Bille juste avant le choc](/premieres-nsi/chap-3/3-4/rebond-1.svg?width=35%)

Dessiner la flèche de sa vitesse juste après le choc. Lequel des deux mouvements, horizontal ou vertical, est modifié par le choc ?
{{< /question >}}

{{< solution "Réponse" >}}
![Bille juste avant et juste après le choc](/premieres-nsi/chap-3/3-4/rebond-2.svg?width=35%)

Seul le mouvement horizontal change : la bille allait vers la droite, elle repart vers la gauche. Elle continue de monter comme avant.
{{< /solution >}}

Dans un gaz, les particules avancent en ligne droite et rebondissent sur les parois comme la bille sur la bande. Le programme de départ est fourni dans Capytale. Quand une question commence par « Sans exécuter le programme », on écrit sa réponse avant de vérifier.

## Une particule décrite par un tuple

Une particule est décrite par cinq entiers, rangés dans un tuple, toujours dans le même ordre :

| **indice** | 0 | 1 | 2 | 3 | 4 |
|:---|:---|:---|:---|:---|:---|
| **élément** | `x` | `y` | `vx` | `vy` | `couleur` |

`x` et `y` sont les coordonnées du centre, en pixels. `vx` et `vy` sont les nombres de pixels parcourus horizontalement et verticalement à chaque image. Un écran n'a pas de demi-pixel : toutes ces valeurs sont des entiers.

```python
import pyxel

# Constantes
LARGEUR = 160    # largeur de la fenêtre, en pixels
HAUTEUR = 120    # hauteur de la fenêtre, en pixels
RAYON = 3        # rayon d'une particule, en pixels

# Type d'une particule : (x, y, vx, vy, couleur)
Particule = tuple[int, int, int, int, int]

def dessiner_particule(p: Particule) -> None:
    """Dessine la particule p = (x, y, vx, vy, couleur)."""
    x, y, couleur = p[0], p[1], p[4]
    pyxel.circ(x, y, RAYON, couleur)

def update(gaz: list[Particule]) -> None:
    """Fait avancer le gaz d'une image."""
    pass

def draw(gaz: list[Particule]) -> None:
    """Dessine les particules du gaz."""
    pyxel.cls(0)
    dessiner_particule(gaz[0])

# Programme principal
pyxel.init(LARGEUR, HAUTEUR, title="Gaz parfait")
particules = [(36, 60, 2, -1, 8)]     # le gaz : une seule particule pour l'instant
pyxel.run(lambda: update(particules), lambda: draw(particules))
```

La ligne `Particule = tuple[...]` donne un nom au type d'une particule, que l'on utilise dans les annotations des fonctions.

`pyxel.run` attend deux fonctions sans paramètre. `lambda: update(particules)` est justement une fonction sans paramètre, écrite sur une ligne : à chaque image, elle appelle `update` en lui passant la liste `particules`.

{{< note success "Règle de ce programme" >}}
Une fonction peut lire les **constantes**, écrites en majuscules (`LARGEUR`, `RAYON`...), car leur valeur ne change jamais. Elle ne lit aucune autre variable du programme principal : la liste des particules lui est toujours passée en paramètre.
{{< /note >}}

{{< question >}}
Lancer le programme. Avec `particules = [(36, 60, 2, -1, 8)]` :

1. que vaut `particules[0][2]` ? Quelle grandeur représente-t-il ?
1. que faut-il écrire pour obtenir la couleur de la particule ?
1. la particule va-t-elle monter ou descendre quand elle bougera ? Justifier à l'aide du repère de Pyxel (Doc. 2,5).
{{< /question >}}

{{< solution "Réponse" >}}
1. `particules[0]` est le tuple de la particule, et `particules[0][2]` son élément d'indice 2 : `2`, c'est `vx`.
1. `particules[0][4]`, qui vaut `8`.
1. Dans Pyxel, $y$ augmente vers le bas. Avec `vy = -1`, $y$ diminue à chaque image : la particule monte.
{{< /solution >}}

{{< question >}}
Modifier `particules` pour obtenir une particule verte (couleur 11), au centre de l'écran, qui se déplacera vers la gauche de 1 pixel par image. Vérifier, puis revenir à la valeur de départ.
{{< /question >}}

{{< solution "Réponse" >}}
`particules = [(80, 60, -1, 0, 11)]`. Le centre est en $(\dfrac{160}{2}, \dfrac{120}{2}) = (80, 60)$. Aller vers la gauche, c'est diminuer $x$ : `vx = -1`.
{{< /solution >}}

{{< qcm >}}
- question: 'Une particule est décrite par le tuple `(x, y, vx, vy, couleur)`. Avec `particules = [(36, 60, 2, -1, 8)]`, que vaut `particules[0][1]` ?'
  reponses:
    - '`60`'
    - '`36`'
    - '`(36, 60, 2, -1, 8)`'
  bonne: 1
  explication: '`particules[0]` est le tuple de la particule, et son élément d''indice 1 est l''ordonnée `y`.'
- question: 'Dans Pyxel, une particule a `vy = -1`. Comment se déplace-t-elle verticalement ?'
  reponses:
    - 'Elle monte.'
    - 'Elle descend.'
  bonne: 1
  explication: 'Dans Pyxel, $y$ augmente vers le bas : diminuer $y$ fait monter la particule.'
- question: 'D''après la règle du programme, quelles variables une fonction peut-elle lire sans les recevoir en paramètre ?'
  reponses:
    - 'Les constantes écrites en majuscules, comme `LARGEUR` ou `RAYON`.'
    - 'Toutes les variables du programme principal.'
    - 'La liste `particules`.'
  bonne: 1
  explication: 'La valeur des constantes ne change jamais ; la liste des particules, elle, est toujours passée en paramètre.'
{{< /qcm >}}

## Faire avancer la particule

Pyxel affiche 30 images par seconde et appelle `update(particules)` avant chaque image. À chaque appel, on ajoute `vx` à `x` et `vy` à `y`.

{{< question >}}
**Sans exécuter le programme.** La particule part de $x = 36$ avec `vx = 2`. Elle touche le bord droit quand son centre atteint $x = 159 - 3 = 156$. Au bout de combien de temps ?
{{< /question >}}

{{< solution "Réponse" >}}
**A.N.** $v_x =$ 2 px/image $\times$ 30 image/s $=$ 60 px/s.

Il reste $156 - 36 = 120$ pixels : **A.N.** $t = \dfrac{\pu{120 px}}{\pu{60 px/s}} = \pu{2 s}$.
{{< /solution >}}

Un élève propose :

```python
def deplacer(p: Particule) -> None:
    p[0] = p[0] + p[2]
    p[1] = p[1] + p[3]
```

{{< question >}}
**Sans exécuter le programme**, prévoir ce qui se passe si on appelle `deplacer(particules[0])`. Expliquer.
{{< /question >}}

{{< solution "Réponse" >}}
Erreur `TypeError: 'tuple' object does not support item assignment` : un tuple n'est pas mutable (Doc. 3,1).
{{< /solution >}}

La fonction doit donc fabriquer un nouveau tuple et le retourner. Pour récupérer d'un coup les cinq éléments de `p`, on le **déballe** :

```python
x, y, vx, vy, couleur = p      # x reçoit p[0], y reçoit p[1], etc.
```

Il faut autant de noms à gauche que d'éléments dans le tuple.

{{< question >}}
Écrire la fonction `deplacer` :

```python
def deplacer(p: Particule) -> Particule:
    """Retourne la particule p après une image de déplacement."""
```

Tester dans la console : `deplacer((36, 60, 2, -1, 8))` doit retourner `(38, 59, 2, -1, 8)`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def deplacer(p: Particule) -> Particule:
    """Retourne la particule p après une image de déplacement."""
    x, y, vx, vy, couleur = p
    return (x + vx, y + vy, vx, vy, couleur)
```
{{< /solution >}}

{{< question >}}
Dans `update`, remplacer `pass` par `gaz[0] = deplacer(gaz[0])`. **Sans exécuter le programme**, prévoir ce qui se passera au bout de 2 secondes, puis vérifier.
{{< /question >}}

{{< solution "Réponse" >}}
La particule traverse le bord droit et disparaît : rien ne lui dit de rebondir.
{{< /solution >}}

{{< question >}}
Un autre élève écrit dans `update` : `gaz = [deplacer(gaz[0])]`. Il n'obtient aucune erreur, mais la particule reste immobile. Expliquer, en s'aidant des fonctions `reinitialiser_1` et `reinitialiser_2` du Doc. 3,2.
{{< /question >}}

{{< solution "Réponse" >}}
À l'appel, le paramètre `gaz` référence la même liste que `particules`. `gaz = [...]` fait référencer une nouvelle liste par la variable locale `gaz` : la liste `particules` n'est pas touchée, comme dans `reinitialiser_1`. `gaz[0] = ...` remplace un élément de la liste partagée, comme dans `reinitialiser_2`.
{{< /solution >}}

{{< qcm >}}
- question: 'Que produit `deplacer(particules[0])` si la fonction contient l''instruction `p[0] = p[0] + p[2]` ?'
  reponses:
    - 'Une erreur `TypeError` : un tuple n''est pas mutable.'
    - 'La particule avance de `vx` pixels.'
  bonne: 1
  explication: 'On ne peut pas modifier un élément d''un tuple : la fonction doit fabriquer et retourner un nouveau tuple.'
- question: 'Que retourne `deplacer((36, 60, 2, -1, 8))` ?'
  reponses:
    - '`(38, 59, 2, -1, 8)`'
    - '`(38, 61, 2, -1, 8)`'
    - '`(36, 60, 2, -1, 8)`'
  bonne: 1
  explication: 'On ajoute `vx` à `x` et `vy` à `y` : $36 + 2 = 38$ et $60 - 1 = 59$. La vitesse et la couleur sont inchangées.'
- question: 'Dans `update(gaz)`, laquelle de ces instructions fait réellement avancer la particule de la liste `particules` ?'
  reponses:
    - '`gaz[0] = deplacer(gaz[0])`'
    - '`gaz = [deplacer(gaz[0])]`'
  bonne: 1
  explication: '`gaz[0] = ...` modifie un élément de la liste partagée avec le programme principal. `gaz = [...]` fait seulement référencer une nouvelle liste par la variable locale `gaz`.'
- question: 'À 30 images par seconde, une particule avance de 2 pixels par image. Combien de temps met-elle à parcourir 120 pixels ?'
  reponses:
    - '2 s'
    - '60 s'
    - '4 s'
  bonne: 1
  explication: 'Sa vitesse vaut $2 \times 30 = 60$ px/s, d''où $t = \dfrac{120}{60} = 2$ s.'
{{< /qcm >}}

## Rebondir contre les murs

Comme sur le billard, quand la particule touche le mur de droite, `vx` devient `-vx`. On complète `deplacer` : elle change d'abord la vitesse si un mur est touché, puis fait avancer la particule. Première version, qui ne traite que le mur de droite :

```python
def deplacer(p: Particule) -> Particule:
    """Retourne la particule p après une image : sa vitesse change
    si elle touche un mur, puis elle avance."""
    x, y, vx, vy, couleur = p
    if x + RAYON >= LARGEUR - 1:      # le bord droit du disque touche le mur
        vx = -vx
    return (x + vx, y + vy, vx, vy, couleur)
```

{{< question >}}
Compléter `deplacer` pour les murs de gauche, du haut et du bas, puis tester.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def deplacer(p: Particule) -> Particule:
    """..."""
    x, y, vx, vy, couleur = p
    if x + RAYON >= LARGEUR - 1:
        vx = -vx
    if x - RAYON <= 0:
        vx = -vx
    if y + RAYON >= HAUTEUR - 1:
        vy = -vy
    if y - RAYON <= 0:
        vy = -vy
    return (x + vx, y + vy, vx, vy, couleur)
```
Quatre `if` indépendants : dans un coin, la particule touche deux murs à la fois. Avec `elif`, un seul serait traité.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. Pour les murs du haut et du bas, quelle composante de la vitesse change de signe ?
1. Le mur du haut est la ligne $y = 0$. Quel point du disque l'atteint en premier ?
{{< /note >}}

{{< question >}}
**Sans ordinateur.** On part de `particules = [(158, 60, 1, 0, 8)]`. Compléter le tableau avec les valeurs de `x` et `vx` après chaque appel de `update`. Que fait la particule ? Vérifier à l'écran.

| **image** | départ | 1 | 2 | 3 | 4 |
|:---|:---|:---|:---|:---|:---|
| `x` | 158 |  |  |  |  |
| `vx` | 1 |  |  |  |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **image** | départ | 1 | 2 | 3 | 4 |
|:---|:---|:---|:---|:---|:---|
| `x` | 158 | 157 | 158 | 157 | 158 |
| `vx` | 1 | $-1$ | 1 | $-1$ | 1 |

À l'image 2, $157 + 3 \geq  159$ : la particule touche encore le mur alors qu'elle s'en éloigne, et `vx` change à nouveau de signe. Elle reste coincée et tremble.
{{< /solution >}}

{{< question >}}
Modifier les quatre conditions pour qu'une particule ne rebondisse que si elle se dirige vers le mur qu'elle touche. Refaire le tableau sans ordinateur, puis vérifier.
{{< /question >}}

{{< solution "Réponse" >}}
```python
if x + RAYON >= LARGEUR - 1 and vx > 0:
    vx = -vx
if x - RAYON <= 0 and vx < 0:
    vx = -vx
if y + RAYON >= HAUTEUR - 1 and vy > 0:
    vy = -vy
if y - RAYON <= 0 and vy < 0:
    vy = -vy
```
Les valeurs de `x` deviennent 157, 156, 155, 154 et `vx` reste $-1$ : la particule se dégage.
{{< /solution >}}

{{< note success "À retenir" >}}
Un tuple n'est pas mutable : une fonction qui « modifie » une particule fabrique et retourne un nouveau tuple. Le déballage `x, y, vx, vy, couleur = p` donne un nom à chaque élément.

Lors d'un rebond sur une paroi, la composante de la vitesse perpendiculaire à la paroi change de signe.

Une fonction qui reçoit une liste en paramètre peut modifier ses éléments (`gaz[0] = ...`). Si elle affecte une nouvelle valeur au paramètre (`gaz = ...`), la liste d'origine ne change pas.
{{< /note >}}

{{< qcm >}}
- question: 'Une particule touche le mur du haut. Quelle composante de sa vitesse change de signe ?'
  reponses:
    - '`vy`'
    - '`vx`'
    - 'Les deux.'
  bonne: 1
  explication: 'Lors d''un rebond, la composante de la vitesse perpendiculaire à la paroi change de signe. Le mur du haut est horizontal.'
- question: 'Le disque a un rayon `RAYON`. Quelle condition indique qu''il touche le mur de gauche, d''abscisse 0 ?'
  reponses:
    - '`x - RAYON <= 0`'
    - '`x <= 0`'
    - '`x + RAYON <= 0`'
  bonne: 1
  explication: 'Le point du disque le plus à gauche a pour abscisse `x - RAYON` : c''est lui qui atteint le mur en premier.'
- question: 'Pourquoi ajoute-t-on la condition `vx > 0` au test du mur de droite ?'
  reponses:
    - 'Pour ne faire rebondir que les particules qui se dirigent vers ce mur.'
    - 'Pour accélérer la particule.'
    - 'Pour éviter une erreur `IndexError`.'
  bonne: 1
  explication: 'Sans elle, une particule qui vient de rebondir et touche encore le mur voit sa vitesse inversée une seconde fois : elle reste coincée contre la paroi.'
{{< /qcm >}}

## Un gaz : une liste de particules

On veut maintenant 30 particules, tirées au hasard. `pyxel.rndi(a, b)` retourne un entier au hasard entre `a` et `b`, bornes comprises. Ajouter ces constantes au début du programme (8, 11 et 12 sont le rouge, le vert et le bleu) :

```python
NB_PARTICULES = 30          # nombre de particules du gaz
VITESSE_MAX = 2             # valeur maximale d'une composante de la vitesse
COULEURS = (8, 11, 12)      # couleurs possibles
```

{{< question >}}
Écrire la fonction `nouvelle_particule`, puis la tester plusieurs fois dans la console :

```python
def nouvelle_particule() -> Particule:
    """Retourne une particule entièrement visible, tirée au hasard.
    Chaque composante de la vitesse est comprise entre -VITESSE_MAX
    et VITESSE_MAX. La couleur est l'un des éléments de COULEURS."""
```
{{< /question >}}

{{< solution "Réponse" >}}
```python
def nouvelle_particule() -> Particule:
    """..."""
    x = pyxel.rndi(RAYON, LARGEUR - 1 - RAYON)
    y = pyxel.rndi(RAYON, HAUTEUR - 1 - RAYON)
    vx = pyxel.rndi(-VITESSE_MAX, VITESSE_MAX)
    vy = pyxel.rndi(-VITESSE_MAX, VITESSE_MAX)
    couleur = COULEURS[pyxel.rndi(0, len(COULEURS) - 1)]
    return (x, y, vx, vy, couleur)
```
On tire un indice valide de `COULEURS`, pas directement une couleur. La fonction ne lit que des constantes, la règle est respectée. Une particule peut tirer `vx = 0` et `vy = 0` : elle reste immobile.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. Un disque est entièrement visible si son centre est à au moins `RAYON` pixels de chaque bord (Doc. 2,5).
1. Pour la couleur, tirer au hasard l'**indice** d'un élément de `COULEURS`.
{{< /note >}}

{{< question >}}
Dans le programme principal, remplacer `particules = [(36, 60, 2, -1, 8)]` par une liste de `NB_PARTICULES` particules construite **en compréhension** (Doc. 3,2). Pourquoi cette ligne doit-elle se trouver après la définition de `nouvelle_particule` ?
{{< /question >}}

{{< solution "Réponse" >}}
```python
particules = [nouvelle_particule() for i in range(NB_PARTICULES)]
```
Python exécute le programme de haut en bas : la fonction doit être définie avant d'être appelée, sinon `NameError`.
{{< /solution >}}

{{< question >}}
Modifier `draw` pour dessiner toutes les particules de `gaz`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def draw(gaz: list[Particule]) -> None:
    """Dessine les particules du gaz."""
    pyxel.cls(0)
    for p in gaz:
        dessiner_particule(p)
```
On ne fait que lire la liste : le parcours par éléments suffit.
{{< /solution >}}

Pour faire bouger toutes les particules, un élève écrit :

```python
def update(gaz: list[Particule]) -> None:
    for p in gaz:
        p = deplacer(p)
```

{{< question >}}
**Sans exécuter le programme**, prévoir ce qu'on observe. Expliquer, puis corriger.
{{< /question >}}

{{< solution "Réponse" >}}
Les particules restent immobiles. `p = ...` fait référencer un nouveau tuple par la variable `p`, mais rien n'est rangé dans la liste (même piège que `for n in notes: n += 1`, Doc. 3,2). Il faut passer par les indices :

```python
def update(gaz: list[Particule]) -> None:
    for i in range(len(gaz)):
        gaz[i] = deplacer(gaz[i])
```
{{< /solution >}}

{{< note success "À retenir" >}}
Le gaz est une **liste de tuples**, construite en compréhension. Pour lire ses éléments, on la parcourt par éléments. Pour les remplacer, on la parcourt par indices : `gaz[i] = ...`.
{{< /note >}}

{{< qcm >}}
- question: 'Quelle instruction construit une liste de `NB_PARTICULES` particules tirées au hasard ?'
  reponses:
    - '`[nouvelle_particule() for i in range(NB_PARTICULES)]`'
    - '`[nouvelle_particule()] * NB_PARTICULES`'
    - '`nouvelle_particule() * NB_PARTICULES`'
  bonne: 1
  explication: 'La compréhension appelle la fonction à chaque tour. La deuxième écriture répète `NB_PARTICULES` fois la **même** particule ; la troisième répète les éléments d''un seul tuple.'
- question: 'Que se passe-t-il avec la boucle `for p in gaz: p = deplacer(p)` ?'
  reponses:
    - 'Les particules restent immobiles.'
    - 'Toutes les particules avancent.'
    - 'Une erreur `TypeError`.'
  bonne: 1
  explication: '`p = ...` fait référencer un nouveau tuple par la variable `p`, mais rien n''est rangé dans la liste. Il faut parcourir les indices : `gaz[i] = deplacer(gaz[i])`.'
- question: 'Pour dessiner toutes les particules dans `draw`, quel parcours suffit ?'
  reponses:
    - 'Le parcours par éléments, `for p in gaz:`, car on ne fait que lire la liste.'
    - 'Le parcours par indices est obligatoire.'
  bonne: 1
  explication: 'On ne modifie pas la liste : lire ses éléments un par un suffit.'
{{< /qcm >}}

## Pour aller plus loin : des collisions entre particules

Dans un gaz réel, les particules se heurtent aussi entre elles. Deux particules se touchent si la distance entre leurs centres est inférieure ou égale à `2 * RAYON`.

{{< question >}}
Ajouter `from math import sqrt` au début du programme, puis écrire :

```python
def distance(p1: Particule, p2: Particule) -> float:
    """Retourne la distance entre les centres de p1 et p2."""

def se_touchent(p1: Particule, p2: Particule) -> bool:
    """Retourne True si p1 et p2 se touchent, False sinon."""
```

Tester : `distance((0, 0, 1, 1, 8), (3, 4, 0, 0, 12))` doit retourner `5.0`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def distance(p1: Particule, p2: Particule) -> float:
    """Retourne la distance entre les centres de p1 et p2."""
    return sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)

def se_touchent(p1: Particule, p2: Particule) -> bool:
    """Retourne True si p1 et p2 se touchent, False sinon."""
    return distance(p1, p2) <= 2 * RAYON
```
La distance n'est en général pas entière : elle est de type `float`, même si les positions sont des entiers.
{{< /solution >}}

Deux particules de même masse qui se heurtent de face **échangent leurs vitesses**. On adopte ce modèle pour toutes les collisions.

{{< question >}}
Écrire la fonction `choc` :

```python
def choc(p1: Particule, p2: Particule) -> tuple[Particule, Particule]:
    """Retourne les particules p1 et p2 après leur collision :
    elles ont échangé leurs vitesses."""
```

Tester : `choc((50, 60, 1, 0, 8), (55, 60, -1, 0, 12))` doit retourner `((50, 60, -1, 0, 8), (55, 60, 1, 0, 12))`.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def choc(p1: Particule, p2: Particule) -> tuple[Particule, Particule]:
    """..."""
    x1, y1, vx1, vy1, c1 = p1
    x2, y2, vx2, vy2, c2 = p2
    return (x1, y1, vx2, vy2, c1), (x2, y2, vx1, vy1, c2)
```
La fonction retourne un tuple de deux tuples.
{{< /solution >}}

Voici la fonction qui teste toutes les paires de particules de la liste `gaz`. Sa dernière ligne déballe le tuple retourné par `choc`, comme `a, b = b, a` (Doc. 3,1).

```python
def gerer_chocs(gaz: list[Particule]) -> None:
    """Fait échanger leurs vitesses aux particules de gaz qui se touchent."""
    for i in range(len(gaz)):
        for j in range(i + 1, len(gaz)):
            p1 = gaz[i]
            p2 = gaz[j]
            if se_touchent(p1, p2):
                gaz[i], gaz[j] = choc(p1, p2)
```

{{< question >}}
1. Avec 3 particules, écrire tous les couples `(i, j)` testés.
1. Pourquoi la boucle intérieure commence-t-elle à `i + 1` et non à `0` ?
{{< /question >}}

{{< solution "Réponse" >}}
1. `(0, 1)`, `(0, 2)` et `(1, 2)`.
1. En partant de 0, chaque paire serait testée deux fois, par exemple `(0, 1)` puis `(1, 0)` : le second échange de vitesses annulerait le premier.
{{< /solution >}}

{{< question >}}
Ajouter l'appel `gerer_chocs(gaz)` à la fin de `update`. Observer longuement : certaines particules restent collées. Pourquoi ? Corriger, en s'inspirant de la correction des rebonds sur les murs.
{{< /question >}}

{{< solution "Réponse" >}}
Après l'échange, les deux particules se touchent encore à l'image suivante : elles échangent à nouveau leurs vitesses et repartent l'une vers l'autre. On n'autorise la collision que si elles se rapprochent :

```python
def se_rapprochent(p1: Particule, p2: Particule) -> bool:
    """Retourne True si la distance entre p1 et p2 diminue
    pendant l'image suivante, False sinon."""
    return distance(deplacer(p1), deplacer(p2)) < distance(p1, p2)
```
et la condition devient `if se_touchent(p1, p2) and se_rapprochent(p1, p2):`.
{{< /solution >}}

{{< note tip "Coups de pouce" >}}
1. Que fait `gerer_chocs` à l'image qui suit un échange de vitesses ?
1. Sur le mur, on n'a fait rebondir que les particules qui s'en approchaient. Comment savoir si deux particules se rapprochent ? On peut utiliser `deplacer` et `distance`.
{{< /note >}}

Il reste un défaut : des particules rapides se traversent parfois.

{{< question >}}
**Sans ordinateur.** Deux particules arrivent de face, en diagonale : `(50, 50, 2, 2, 8)` et `(56, 56, -2, -2, 12)`. À chaque image, `update` les déplace, puis appelle `gerer_chocs`. Compléter le tableau (distances arrondies au dixième), puis expliquer pourquoi les particules se traversent.

| **image** | départ | 1 | 2 | 3 |
|:---|:---|:---|:---|:---|
| particule 1 | (50, 50) |  |  |  |
| particule 2 | (56, 56) |  |  |  |
| distance | 8,5 |  |  |  |
| `se_touchent` | non |  |  |  |
| `se_rapprochent` | oui |  |  |  |
{{< /question >}}

{{< solution "Réponse" >}}
| **image** | départ | 1 | 2 | 3 |
|:---|:---|:---|:---|:---|
| particule 1 | (50, 50) | (52, 52) | (54, 54) | (56, 56) |
| particule 2 | (56, 56) | (54, 54) | (52, 52) | (50, 50) |
| distance | 8,5 | 2,8 | 2,8 | 8,5 |
| `se_touchent` | non | oui | oui | non |
| `se_rapprochent` | oui | non | non | non |

**A.N.** À l'image 1 : $d = \sqrt{(54 - 52)^2 + (54 - 52)^2} = \sqrt{8} \approx \pu{2,8 px}$.

Quand le contact est enfin détecté, les particules se chevauchent déjà largement. À l'image suivante, leurs centres se sont croisés : la distance ne diminue pas, `se_rapprochent` retourne `False` et aucun choc n'a lieu.
{{< /solution >}}

Pour éviter ce chevauchement, il faut anticiper : **avant** de déplacer les particules, on regarde si elles vont se toucher à l'image suivante.

{{< question >}}
Modifier la condition de `gerer_chocs` pour tester si les particules se toucheront après leur déplacement, puis placer l'appel `gerer_chocs(gaz)` au début de `update`. Refaire le tableau précédent, puis vérifier à l'écran que les particules ne se traversent presque plus.
{{< /question >}}

{{< solution "Réponse" >}}
```python
if se_touchent(deplacer(p1), deplacer(p2)) and se_rapprochent(p1, p2):
```
```python
def update(gaz: list[Particule]) -> None:
    """Fait avancer le gaz d'une image : d'abord les chocs, puis le déplacement."""
    gerer_chocs(gaz)
    for i in range(len(gaz)):
        gaz[i] = deplacer(gaz[i])
```
Au départ, les particules se toucheront en $(52, 52)$ et $(54, 54)$, et elles se rapprochent : elles échangent leurs vitesses, puis avancent en $(48, 48)$ et $(58, 58)$. Elles rebondissent sans se chevaucher. Il reste de rares traversées, lors de contacts très rasants ou quand trois particules se touchent en même temps.
{{< /solution >}}

{{< qcm >}}
- question: 'Avec 4 particules, combien de couples `(i, j)` la double boucle `for i in range(n): for j in range(i + 1, n):` teste-t-elle ?'
  reponses:
    - '6'
    - '12'
    - '16'
  bonne: 1
  explication: '`(0, 1)`, `(0, 2)`, `(0, 3)`, `(1, 2)`, `(1, 3)` et `(2, 3)` : chaque paire n''est testée qu''une fois.'
- question: 'Pourquoi la boucle intérieure commence-t-elle à `i + 1` et non à `0` ?'
  reponses:
    - 'Sinon chaque paire serait testée deux fois, et le second échange de vitesses annulerait le premier.'
    - 'Pour aller plus vite, sans changer le résultat.'
    - 'Pour éviter une erreur `IndexError`.'
  bonne: 1
  explication: 'En partant de 0, on testerait `(0, 1)` puis `(1, 0)`. Il faut aussi éviter de tester une particule avec elle-même.'
- question: 'Que retourne `choc((50, 60, 1, 0, 8), (55, 60, -1, 0, 12))` ?'
  reponses:
    - '`((50, 60, -1, 0, 8), (55, 60, 1, 0, 12))`'
    - '`((55, 60, 1, 0, 8), (50, 60, -1, 0, 12))`'
    - '`((50, 60, -1, 0, 12), (55, 60, 1, 0, 8))`'
  bonne: 1
  explication: 'Les particules échangent leurs vitesses ; elles gardent leur position et leur couleur.'
{{< /qcm >}}

## Défis

{{< question >}}
**Défi A : le mélange de deux gaz.** Au départ, les particules rouges sont dans la moitié gauche de la boîte, les bleues dans la moitié droite. Donner à `nouvelle_particule` les paramètres `couleur`, `x_min` et `x_max`, puis construire la liste. Comparer la vitesse du mélange avec et sans collisions.
{{< /question >}}

{{< solution "Réponse" >}}
```python
def nouvelle_particule(couleur: int, x_min: int, x_max: int) -> Particule:
    """Retourne une particule de la couleur donnée, d'abscisse
    comprise entre x_min et x_max."""
    x = pyxel.rndi(x_min, x_max)
    y = pyxel.rndi(RAYON, HAUTEUR - 1 - RAYON)
    vx = pyxel.rndi(-VITESSE_MAX, VITESSE_MAX)
    vy = pyxel.rndi(-VITESSE_MAX, VITESSE_MAX)
    return (x, y, vx, vy, couleur)
```
Dans le programme principal :
```python
milieu = LARGEUR // 2
rouges = [nouvelle_particule(8, RAYON, milieu - 1 - RAYON)
          for i in range(NB_PARTICULES // 2)]
bleues = [nouvelle_particule(12, milieu + RAYON, LARGEUR - 1 - RAYON)
          for i in range(NB_PARTICULES // 2)]
particules = rouges + bleues
```
L'opérateur `+` concatène les deux listes. Avec les collisions, le mélange est plus lent : chaque particule est sans cesse déviée par ses voisines. C'est la **diffusion**.
{{< /solution >}}

{{< question >}}
**Défi B : chauffer le gaz.** Chaque appui sur la touche <kbd>↑</kbd> double les deux composantes de la vitesse de toutes les particules. Que se passe-t-il après plusieurs appuis ?
{{< /question >}}

{{< solution "Réponse" >}}
Dans `update` :
```python
if pyxel.btnp(pyxel.KEY_UP):
    for i in range(len(gaz)):
        x, y, vx, vy, couleur = gaz[i]
        gaz[i] = (x, y, 2 * vx, 2 * vy, couleur)
```
Les particules vont plus vite. Après plusieurs appuis, une particule avance de plus de `2 * RAYON` pixels par image : elle peut en traverser une autre sans que la simulation détecte le contact, ou s'enfoncer de plusieurs pixels dans un mur.
{{< /solution >}}

## Bilan

{{< note success "À l'issue de cette activité, je sais…" >}}
- représenter un objet par un tuple et lire un élément par son indice ;
- expliquer pourquoi on ne peut pas modifier un élément d'un tuple, et écrire une fonction qui retourne un nouveau tuple ;
- déballer un tuple pour nommer ses éléments ;
- construire une liste de tuples en compréhension ;
- choisir entre un parcours par éléments, pour lire une liste, et un parcours par indices, pour la modifier ;
- passer une liste en paramètre à une fonction, et expliquer pourquoi la fonction peut modifier ses éléments mais pas la remplacer ;
- parcourir toutes les paires d'éléments d'une liste avec deux boucles imbriquées ;
- faire tourner un programme à la main pour trouver l'origine d'un comportement inattendu.
{{< /note >}}
