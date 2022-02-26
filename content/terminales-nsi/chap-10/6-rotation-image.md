---
title: "Rotation d'une image bitmap d'un quart de tour"
subtitle: "Chapitre 13,5"
author: ""
type: ""
date: 2020-11-18T17:12:52+04:00
draft: false
toc: true
tags: ["Diviser pour régner", "Récursivité", "Traitement images"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

L'objectif de cette activité est l'écriture d'une fonction qui effectue la rotation d'une image bitmap de 90 degrés en utilisant le principe « Diviser pour régner ».

On peut manipuler des images en Python à l'aide du **module PIL (Python Image Library)**. Une première partie de l'activité est consacrée à la prise en main de ce module. Dans un second temps, la fonction de manipulation des bits est développée.

## Images numériques

### Définition

{{% note normal %}}
#### L'image matricielle
Une **image matricielle**, ou « carte de points » (de l'anglais « bitmap »), est une image constituée d'une *matrice de points colorés*, c'est-à-dire, constituée d'*un tableau, d'une grille, où chaque case possède une couleur qui lui est propre et est considérée comme un point*. Il s'agit donc d'une juxtaposition de points de couleurs formant, dans leur ensemble, une image.
<div style="text-align: right;">
<a href="https://fr.wikipedia.org/wiki/Image_matricielle">Wikipedia</a>
</div>
{{% /note %}}

<img src="/terminales-nsi/chap-10/chap-10-2-1.jpg" alt="" width="80%" />

### Caractéristiques

{{% note normal %}}
#### Numérisation
Le codage ou la représentation informatique d'une image implique sa **numérisation**. Cette numérisation se fait dans deux espaces :

- l'**espace spatial** dans lequel *l'image est numérisée suivant l'axe des abscisses et l'axe des ordonnées* : on parle d'**échantillonnage**. Les échantillons dans cet espace sont nommés **pixels** (« *picture element* ») et leur nombre va constituer la **définition de l'image**.

- l'**espace des couleurs** dans lequel *les différentes valeurs de luminosité que peut prendre un pixel sont numérisées pour représenter sa couleur et son intensité* ; on parle de **quantification**. La précision dans cet espace dépend du nombre de bits sur lesquels on code la luminosité et est appelée **profondeur de l'image**.
{{% /note %}}

{{% note tip %}}
#### À retenir
La qualité d'une image matricielle est déterminée par *le nombre total de pixels* et *la quantité d’information contenue dans chaque pixel* (souvent appelée profondeur de numérisation des couleurs).
{{% /note %}}

{{% note normal %}}
#### Définition d'une image
On appelle **définition** le nombre de points (pixels) constituant une image: *c'est le nombre de colonnes de l'image que multiplie son nombre de lignes.*

La **définition** d'une image indique donc le niveau de détails qui seront visibles dans l'image. *Pour une taille donnée, plus il y aura de pixels, plus il y aura de détails fins visibles*.

**Exemple.** Une image numérisée avec une définition de $640 \times 480$ pixels (donc contenant 307 200 pixels) apparaîtra très approximative et sous forme d’un pavage de petits carrés de couleur, par comparaison à une image de $1280 \times  1024$ pixels (soit 1 310 720 pixels).
{{% /note %}}

{{% note normal %}}
#### Résolution d'une image
On appelle **résolution** le nombre de points (pixels) contenus dans une longueur donnée, le pouce (un pouce mesure $\pu{2,54 cm}$, c'est une unité de mesure britannique). Elle est exprimée en « *points par pouce* » (**PPP**) en français et « *Dots Per Inch* » (**DPI**) en anglais. 

La résolution permet ainsi d'établir le rapport entre la **définition** d'une image et la **dimension** réelle de sa représentation sur un support physique (écran, papier, etc.)
{{% /note %}}


<img src="/terminales-nsi/chap-10/chap-10-2-2.png" alt="" width="" />
> Source : {{< remote "http://www.raphaelisdant.fr/paris8/" "http://www.raphaelisdant.fr/paris8/" >}}

{{% note normal %}}
#### Codage des couleurs
En plus de sa définition, une image numérique utilise plus ou moins de mémoire selon le *codage des informations de couleur* qu'elle possède. C'est ce que l'on nomme le **codage de couleurs** ou **profondeur des couleurs**, exprimé en bits par pixel (bpp) : 1, 4, 8, 16, 24, ... bits.

Le **codage des informations de couleur** est donc *le nombre de bits utilisés pour coder une couleur*.
{{% /note %}}

#### Remarque.
Les écrans utilisent la **synthèse additive** pour restituer les couleurs : *chaque pixel est composé de trois sous-éléments munis respectivement d'un filtre : rouge, vert, bleu*.

{{% note normal %}}
#### Quelques modes de représentation des couleurs
- **Mode bitmap (noir et blanc) :** Avec ce mode, il est possible d'afficher uniquement des images en deux couleurs: noir et blanc. Il présente une profondeur de 1 bpp.
- **Mode  niveau de gris :** Avec ce mode, il est possible d'afficher  des images utilisant 254 ou 65534 nuances de gris entre le blanc et le noir.      
*Le niveau de gris représente la luminosité d'un pixel, lorsque les valeurs de ses composantes de couleur sont identiques.*       
Pour convertir une image couleur en niveau de gris il faut remplacer, pour chaque pixel les trois valeurs représentant les niveaux de rouge, de vert et de bleu, en une seule valeur représentant la luminosité.       
Il présente une profondeur de 8 bpp ou 16 bpp.
- **Mode RVB :** Dans ce mode, la couleur de chaque pixel de l'image est codée à l'aide d'un triplet de valeurs pour le rouge, le vert et le bleu. Chaque canal peut être codé sur 8 bits (le plus fréquent) ou 16 bits (appareils de photo modernes).
{{% /note %}}

### Exploitation des documents

1. Déterminer la résolution d'une image de $300 \times 300$ pixels mesurant 2 pouces par coté.
2. Quelle serait la définition en pixels d'une feuille scannée d'une largeur de 8,5 pouces sur une hauteur de 11 pouces en 300 dpi ?
3. Quel est le poids, en octets, d'une image d'une définition de $640 \times  480$, codée sur 1 bit (image en « noir et blanc ») ? codée sur 8 bits (« niveau de gris ») ? codée sur 24 bits (« RVB ») ?
4. Pourquoi le mode « niveau de gris » divise-t-il par trois le nombre d'octets nécessaire au codage ?
5. Quelle particularité doivent présenter les sous-éléments de chaque pixel lors de l'affichage d'une image en « niveau de gris » ?
6. Déterminer le nombre de couleurs que l'on peut coder en mode RVB (8 bpp).

### Manipulation d'une image en niveaux de gris avec Python

7. Étudier le code suivant, essayer de déterminer quel traitement effectue la fonction `mystere` et le tester.

```python
import PIL.Image as pi


def mystere(im):
    """
    Cette fonction réalise un traitement qu'il faut deviner, sur
    l'image dont l'objet qui la représente est passé en argument.

    Paramètre
    ---------
    im: PIL.Image.Image
        Objet image

    Retour
    ------
    None
    """
    (largeur, hauteur) = (im.width, im.height)

    for y in range(hauteur):
        for x in range(largeur):
            niveau = im.getpixel((x, y))
            niveau = 255 - niveau
            im.putpixel((x, y), niveau)

def main():
    """ Fonction principale """

    # Chemin de l'image
    image = "tigrenb.png"
    # Création de l'objet image
    im_nb = pi.open(image)
    # Visualisation du fichier
    im_nb.show()

    # Modification du fichier
    mystere(im_nb)
    # Visualisation des modifications
    im_nb.show()

main()
```

- {{< remote "Fichier image tigrenb.png" "/terminales-nsi/chap-10/tigrenb.png" >}}

8. À partir de la fonction précédente, écrire une fonction nommée `noir_et_blanc` qui, en fonction d’un seuil `s`, transforme tous les pixels de valeur inférieure à `s` en 0 (noir) et tous les autres en 255 (blanc).

9. En modifiant les couleurs des pixels, il est possible de « dessiner » dans une image. Par exemple, on peut tracer une ligne horizontale blanche dans l'image.     
Écrire la fonction `ligne_blanche` qui trace une ligne blanche horizontale au niveau de l’ordonnée $y$ de l’image et le tester.

10. Écrire la fonction `ligne`, évolution de la fonction précédente, qui permet de tracer une ligne horizontale d’une « couleur », *codée en niveau de gris*, dont le niveau est passé en argument.

11. On veut maintenant pouvoir assombrir ou éclaircir des images. Pour assombrir une image, on *décide* de diviser par 2 le niveau de tous les pixels. À l’opposé, pour éclaircir une image, on *décide* de multiplier par 2 le niveau de tous les pixels, en prenant soin de ne pas dépasser la valeur maximale de 255 (on limite donc les valeurs supérieures à 255).
Écrire la fonction `traitement` qui réalise ces opérations (la fonction doit être capable d'éclaircir ou d'assombrir l'image).

12. Écrire la fonction `grille` qui trace une grille à l’écran. Cette fonction doit recevoir en argument le pas de la grille, la couleur des traits horizontaux et verticaux (en niveaux de gris) et l’objet image.

### Manipulation d'une image en couleur avec Python

13. Étudier le code suivant. 
```python
from PIL import Image


def recuperation_niveaux(im: Image, pt: tuple) -> None:
    """
    Récupère la couleur du pixel pt.
    """
    # On vérifie que le point est dans l'image
    (largeur, hauteur) = (im.width, im.height)
    if pt[0] > (largeur - 1) or pt[0] < 0 or pt[1] < 0 or pt[1] > (hauteur - 1):
        raise Exception("Le point indiqué n'est pas dans l'image.")

    # Récupération des niveaux de couleur
    triplet = im.getpixel(pt)

    return triplet


def modification_couleur(im: Image, pt: tuple, triplet: tuple) -> None:
    """ 
    Attribue la couleur (triplet) au pixel pt.
    """

    # On vérifie que le point est dans l'image
    (largeur, hauteur) = (im.width, im.height)
    if pt[0] > (largeur - 1) or pt[0] < 0 or pt[1] < 0 or pt[1] > (hauteur - 1):
        raise Exception("Le point indiqué n'est pas dans l'image.")

    # Modification de la couleur
    im.putpixel(pt, triplet)


def grille(im: Image, pas: int, triplet: tuple) -> None:
    """
    Trace une grille à l'écran, de pas 'pas' dont la couleur 
    est donnée par le triplet triplet.
    """
    pass


def augmentation_contraste(im: Image, offset: int) -> None:
    """
    Augmente le contraste de l'image d'une valeur offset.
    """
    pass


def teinte_plus_chaude(im: Image, offset: int) -> None:
    pass


def main():
    """ Fonction principale. """
    nom_image = "tigre.jpg"

    # Création de l'objet image
    im = Image.open(nom_image)
    im.show()

    # Récupération des niveaux de couleur
    pt = (600, 250)
    (rouge, vert, bleu) = recuperation_niveaux(im, pt)

    # Affichage du résultat
    print("Au point {} : R : {}, V : {}, B : {}".format(pt, rouge, vert, bleu))


main()
```
- {{< remote "Fichier image tigre.jpg" "/terminales-nsi/chap-10/tigre.jpg" >}}

14. Quelle est la couleur du pixel de coordonnées $(600, 250)$ ?

15. Adapter la fonction `grille` de la partie précédente de façon à ce qu'on puisse choisir la couleur de la grille.

16. Écrire le corps de la fonction `augmentation_contraste`.

16. Écrire le corps de la fonction `teinte_plus_chaude`.

## Rotation d'une image d'un quart de tour

Dans la suite de cette activité on suppose que l'image est carrée et que sa dimension est une puissance de 2, par exemple $256 \times 256$. 

Une solution se trouve à {{< remote "cette adresse" "https://repl.it/@dlatreyte/rotation-image" >}}

{{% note normal %}}
L'idée de l'algorithme consiste à découper l'image en quatre, à effectuer la rotation de 90 degrés de chacun des quatre morceaux, puis de les déplacer vers leur position finale. 
{{% /note %}}

<img src="/terminales-nsi/chap-10/chap-10-2-3.png" alt="" width="60%" />

- {{< remote "Fichier image 1 : A-8x8.png" "/terminales-nsi/chap-10/A-8x8.png" >}}

- {{< remote "Fichier image 1 : A-80x80.png" "/terminales-nsi/chap-10/A-80x80.png" >}}

- {{< remote "Fichier image 1 : A-800x800.png" "/terminales-nsi/chap-10/A-80x80.png" >}}

- {{< remote "Fichier image 1 : hokusai_512x512.png" "/terminales-nsi/chap-10/hokusai_512x512.png" >}}

Afin de pouvoir procéder récursivement, définir la fonction (et sa spécification !) `rotation_aux(px, x, y, t)` qui effectue la rotation de la portion carrée de l'image comprise entre les pixels $(x,y)$ et $(x+t, y+t)$. Cette fonction ne renvoie rien, elle modifie le tableau `px` pour effectuer la rotation de cette portion de l'image, au même endroit. On suppose que `t` est une puissance de 2.       
Le code de cette fonction est :
```python
def rotation_aux(im, x: int, y: int, t: int) -> None:
    if t == 1:
        return

    t = t // 2
    rotation_aux(im, x, y, t)
    rotation_aux(im, x + t, y, t)
    rotation_aux(im, x, y + t, t)
    rotation_aux(im, x + t, y + t, t)

    for i in range(x, x + t):
        for j in range(y, y + t):
            #print(x, y)
            t_1 = im.getpixel((i, j))
            t_2 = im.getpixel((i, j + t))
            t_3 = im.getpixel((i + t, j + t))
            t_4 = im.getpixel((i + t, j))

            im.putpixel((i, j), t_4)
            im.putpixel((i + t, j), t_3)
            im.putpixel((i + t, j + t), t_2)
            im.putpixel((i, j + t), t_1)
```

17. Étudier ce code afin de bien le comprendre. En particulier, faire fonctionner à la main la fonction pour une image de définition $8 \times 8$.

18. En déduire la fonction `rotation(px)` qui effectue une rotation de l'image toute entière, sa dimension étant donnée par le paramètre `taille`.     
Une fois la rotation effectuée, on pourra sauvegarder le résultat dans un autre fichier avec l'instruction `im.save("Apres_rotation.png")`. 







