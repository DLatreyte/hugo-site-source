# Chap. 13 — Cryptanalyse : analyse fréquentielle

[TOC]

**Bibliographie.** *« Divertissements mathématiques et informatiques »*, Laurent Signac

------

## Introduction

L'**analyse fréquentielle** est une technique de cryptanalyse qui utilise le fait que, dans les langues basées sur des lettres, celles-ci n'apparaissent pas au hasard : certaines lettres, ainsi que certaines suites de lettres, apparaissent plus souvent que d'autres.

Ces fréquences d'apparition dépendent de la langue. En français, la lettre la plus fréquente est le E. Dans un texte, environ une lettre sur six est un E. Les lettres les moins fréquentes sont le K et le W. Il faut plus de 2000 lettres pour avoir de bonnes chances de trouver un W.

Puisqu'une substitution monoalphabétique, comme le chiffrement de César, transforme une lettre de manière toujours identique, il suffit de repérer dans le texte crypté la lettre qui revient le plus souvent. Il y a de bonnes chances pour qu'elle corresponde au E. Les autres lettres fréquentes sont A, N, S, T et I. Chaque nouvelle lettre découverte en utilisant la méthode des fréquences nous fait progresser dans la voie du déchiffrement.

**Remarque.** En plus des fréquences des lettres seules, il est possible d'utiliser les fréquences des bigrammes (deux lettres consécutives) ou des trigrammes. Le bigramme le plus fréquent en français est ES.

L'analyse fréquentielle ne peut être utile que si l'on dispose d'une quantité suffisante de données. Nous allons donc être amenés à manipuler de longues chaînes de caractères qu'il est hors de question de « retaper »· Par exemple, le texte qui servira de base à nos statistiques comporte un demi-million de caractères.

Puis, après avoir construit notre propre table de fréquences, basée sur le roman de Jules Verne *La Jangada*, nous l'utiliserons pour analyser un texte chiffré d'environ 450 caractères et déduirons de cette analyse la totalité du texte en clair et la quasi-totalité de la clé de chiffrement.

## Manipulation de fichiers texte avec Python

### Deux types de fichiers logiques

**Référence :** [http://pise.info/algo/fichiers.htm](http://pise.info/algo/fichiers.htm)

La manipulation d'un fichier dépend de son type :

- **Fichiers texte :** un fichier texte est organisé sous forme de lignes successives. Chacune de ces lignes est appelée un   **enregistrement**. 
  En fait, entre chaque enregistrement, sont stockés les octets correspondants aux caractères `CR`(code ASCII 13) et `LF`(code ASCII 10), signifiant un retour au début de la ligne suivante.

  > *Le traitement de tels fichiers revient à celui de **chaînes de caractères**.*

  Ce type de fichier est couramment utilisé dès lors que l'on doit stocker des informations pouvant être assimilées à une base de données (sans le besoin de performances des « Serveurs de Bases de Données »).

- Fichiers binaires : ces fichiers ne possèdent pas de structure de ligne, les octets sont écrits les uns à la suite des autres. *Le traitement de tels fichiers est forcément spécifique aux données qui y sont stockées, il n'existe pas de méthode générique.*

> Dans un fichier texte, *toutes les données sont écrites sous forme de texte* (chaînes de caractères). Cela veut dire que les nombres y sont représentés sous forme de suites de « caractères-chiffres ». *Ces nombres doivent donc être convertis en chaînes de caractères lors de   l'**écriture** dans le fichier. Inversement, lors de la **lecture** du fichier, on devra convertir ces chaînes en nombres si l'on veut pouvoir les utiliser dans des calculs*.

### Création d'un objet de type fichier avec Python

En python, on crée un objet fichier grâce à la fonction `open` :

```python
f = open("fichier.txt",'r')
```

La fonction `open` prend, comme arguments, deux chaînes de caractères. La première est le **chemin du fichier** à ouvrir (absolu ou relatif), la seconde précise dans quel **mode** il doit l'être (*lecture*, *écriture*, etc.). Il est aussi possible, de manière optionnelle, d'indiquer **l'encodage** du texte dans le fichier à lire.

**Remarque.** Il faut toujours faire attention à l'encodage utilisé lors de l'édition d'un texte dans un éditeur. Par défaut, en Python 3, les chaînes de caractères sont encodées en utf-8. C'est le réglage par défaut des systèmes d'exploitation modernes. *Tout texte non encodé en utf-8 n'est pas détecté comme tel par Python 3 mais comme une séquence d'octets (texte binaire donc) !*

**Création d'un objet fichier en lecture seule en précisant l'encodage**

```python
f = open("fichier.txt", encoding='iso-8859-15', mode='r')
```

### Modes d'ouverture des fichiers

- `r` : **mode lecture seule**. Le pointeur de fichier est au début du fichier.
- `rb` : **mode lecture seule au format binaire**.  Très pratique lorsqu'on ouvre un fichier qui n'est pas un fichier texte (image, son, etc.) ou que l'on souhaite avoir une vision plus détaillée des  fichiers texte.
- `r+` : **mode lecture et écriture**. Le pointeur de fichier est au début du fichier.
- `rb+` : idem au format binaire.
- `w` : **écriture seule**. Le fichier est créé à l'appel de la fonction `open` s'il n'existe pas déjà, **écrasé sinon** !
- `wb`: idem mais au format binaire.
- `w+` : **écriture et lecture**. Si le fichier existe déjà, il est écrasé à l'appel de la fonction `open`.
- `wb+` : idem mais au format binaire.
- `a` : **ouvre un fichier en ajout**. Le pointeur de fichier est en fin de fichier si celui-ci existe. Le fichier est créé dans le cas contraire.
- `ab` : idem mais au format binaire.
- `a+` : **ajout et lecture**. Le pointeur de fichier est en fin de fichier si celui-ci existe. Le fichier est créé dans le cas       contraire.
- `ab+` : identique mais au format binaire.

### Opérations courantes sur les fichiers

- `open()` : création ou ouverture d'un fichier.
- `close()` : fermeture d'un fichier.
- `readline()` : retourne la ligne courante sous forme d'une chaîne de caractères. Permet de ne pas avoir à « charger » tout le fichier en mémoire, pratique donc lorsqu'on manipule de très grandes quantités de données.
- `readlines()` : retourne une liste formée de toutes les lignes du fichier. Chaque élément de cette liste est une chaîne de caractères. Tout le fichier est donc « chargé » en mémoire. Attention aux fichiers trop volumineux !
- `read()` : retourne une chaîne de caractères contenant tous les caractères présents dans le fichier. Attention aux fichiers trop volumineux !
- `seek()` : déplace le pointeur de fichier (curseur) du *nombre d'octets* spécifié en arguments.
- `write()` : écrit une chaîne de caractères dans le fichier à partir de la position courante du curseur. *Le passage à la ligne doit être géré manuellement*.
- `writelines()` : écrit les chaînes de caractères contenues dans une liste. Le passage à la ligne est géré automatiquement.

### Exemples

#### Affichage du contenu d'un fichier, ligne par ligne

```python
f = open("fichier.txt", 'r')
      
for ligne in f.readline():
    print(ligne)
```

#### Affichage du contenu d'un fichier, ligne par ligne

```python
f = open("fichier.txt", 'r')
      
for ligne in f:    # car en fait, f est un itérateur
    print(ligne)
```

#### Affichage du contenu d'un fichier après l'avoir chargé entièrement en mémoire dans une liste dont les éléments sont les lignes

```python
f = open("fichier.txt", 'r')
      
lignes = f.readlines()
for ligne in lignes:
    print(ligne)
```

#### Affichage du contenu d'un fichier après l'avoir chargé entièrement en mémoire dans une seule chaîne de caractères

```python
f = open("fichier.txt", 'r')
      
chaine = f.read()
```



#### La manipulation des fichiers impose *la transformation de chaînes de caractères*

Il est nécessaire de savoir très rapidement : *découper une chaîne de caractères en sous-chaînes*, *construire une chaîne de caractères*, etc. Les exemples ci-dessous sont donc généralement  utilisés lorsqu'on manipule des fichiers contenant du texte :

```python
>>> a = "1;2;3;4;5;6"
>>> a.split(";")
['1', '2', '3', '4', '5', '6']
>>> l = a.split(";")
>>> b = "!".join(l)
>>> print(b)
"1!2!3!4!5!6"
>>> type(a), type(b), type(l)
(<type 'str'>, <type 'str'>, <type 'list'>)
>>> c = "\nabcde\n"
>>> d = c.strip()
>>> print(d)
"abcde"
```

##### Séparateurs de lignes et autres différences entre systèmes d'exploitation

Sur les systèmes POSIX (famille des Unix, Linux ou OS X) le séparateur de ligne est le caractère **Nouvelle ligne** (`Newline` ou `\n`). Pour les versions antérieures de Mac OS, c'était le **Retour à la ligne** (`Return` ou `\r`), tandis que les systèmes DOS et Windows utilisent la combinaison des deux (`\r\n`).

Parmi les autres différences entre systèmes, on trouve le séparateur de répertoires dans les chemins d'accès (POSIX utilise `/` alors que DOS et Windows utilisent `\`. Les modules `os` et `os.path` permettent de ne pas avoir à se soucier de toutes ces différences.

## Travail à réaliser

### Extraction de tous les caractères du roman

1. Télécharger le texte contenant le roman de Jules Verne : [La jangada](./la-jangada.txt).
   **Remarque.** Ce texte a été récupéré sur le site du [projet Gutenberg](https://www.gutenberg.org).

2. Définir la fonction dont la spécification est :

   ```python
   def extraction_caracteres(nom_fichier: str) -> List[str]:
       """
       Ouvre le fichier nom_fichier, extrait l'ensemble des caractères
       sous forme d'une unique chaîne de caractères puis crée une liste 
       dont chaque élément est un caractère présent dans le texte initial.
       """
   ```

   **Remarque :** Ne pas oublier d'importer le module `typing` dans les premières lignes.

   ```python
   from typing import List, Dict, Sequence
   ```

3. Définir et appeler la fonction `main` suivante :

   ```python
   def main():
       """ Fonction principale qui appelle toutes les autres. """
       roman = "la-jangada.txt"
       liste_caracteres = extraction_caracteres(roman)
       print(liste_caracteres)
   ```

### Nettoyage des caractères

La liste `liste_caractères` contient des caractères n'appartenant pas à l'alphabet (blancs, ponctuations, etc.). Il est nécessaire de les éliminer.

1. Importer le module `string` au début du fichier.

2. Compléter le code de la fonction `suppression_ponctuation` suivante :

   ```python
   def suppression_ponctuation(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères de ponctuation dans la liste.
       """
       ponctuations = string.punctuation + "«»°"
       ...
       ...
           ...
               ...
               ...
           ...
       return liste_car
   ```

3. Sur le même modèle, compléter le code de la fonction `suppression_blancs` suivante :

   ```python
   def suppression_blancs(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères invisibles dans la liste.
       """
       ...
       ...
           if liste_car[i] in string.whitespace:
               ...
               ...
           ...
       return liste_car
   ```

4. Sur le même modèle, compléter le code de la fonction `suppression_chiffres` suivante :

   ```python
   def suppression_chiffres(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères invisibles dans la liste.
       """
       ...
       ...
           if liste_car[i] in string.digits:
               ...
               ...
           ...
       return liste_car
   ```

5. Définir une fonction appelée `nettoyage` qui réalise en un seul appel les trois actions réalisées par les trois fonctions précédentes.

6. Appeler la fonction nettoyage depuis la fonction `main` :

   ```python
   def main():
       """ Fonction principale qui appelle toutes les autres. """
       roman = "la-jangada.txt"
       liste_caracteres = extraction_caracteres(roman)
       liste_caracteres = nettoyage(liste_caracteres)
       print(liste_caracteres)
   ```

### Transformation des caractères accentués

Dans cette partie nous allons transformer tous les caractères accentués en leur équivalent sans accent.

1. Définir la fonction `trouve_indice` dont la spécification est :

   ```python
   def trouve_indice(car: str, seq: Sequence) -> int:
       """
       Détermine le premier indice du caractère car dans liste.
       On suppose que car appartient à la liste.
       
       Ainsi trouve_indice('a', "jkhdsalkj") retourne 5.
       """
   ```

2. Définir la fonction `transformation_accents` dont une partie du code est :

   ```python
   def transformation_accents(liste_car: List[str]) -> List[str]:
       """
       Transforme chaque caractère accentué en son équivalent sans accent.
       """
       accents = "âãàéèêëïîôôùüûÂÁÀÃÉÈËÊÎÏÔOÕõÙÜÛçÇÑñń"
       equivalents = "aaaeeeeiioouuuAAAAEEEEIIOOOOUUUcCNnn"
   
       ...
           ...
               ...
               ...
               ...
       ...
   ```

   Cette fonction doit utiliser la fonction `trouve_indice`.

3. Appeler la fonction `nettoyage` depuis la fonction `main` :

   ```python
   def main():
       """ Fonction principale qui appelle toutes les autres. """
       roman = "la-jangada.txt"
       liste_caracteres = extraction_caracteres(roman)
       liste_caracteres = nettoyage(liste_caracteres)
       liste_caracteres = transformation_accents(liste_caracteres)
       print(liste_caracteres)
   ```

   ### Transformation des minuscules en majuscules

   1. Définir la fonction `transformation_minuscules` dont la spécification est :

      ```python
      def transformation_minuscules(liste_car: List[str]) -> List[str]:
          """
          Transforme toutes les minuscules de la liste liste_car en majuscules.
          """
      ```

      Utiliser les méthodes sur les chaînes de caractères introduites au chapitre 10.

   2. Appeler la fonction `transformation_minuscules` depuis la fonction `main` :

      ```python
      def main():
          """ Fonction principale qui appelle toutes les autres. """
          roman = "la-jangada.txt"
          liste_caracteres = extraction_caracteres(roman)
          liste_caracteres = nettoyage(liste_caracteres)
          liste_caracteres = transformation_accents(liste_caracteres)
          liste_caracteres = transformation_minuscules(liste_caracteres)
          print(liste_caracteres)
      ```

   ### Création des dictionnaires

   L'objet de cette partie est la création d'un dictionnaire dont les clés sont les caractères et les valeurs leur fréquence d'apparition.

   1. Définir la fonction `creation_dict_car` dont la spécification est :

      ```python
      def creation_dict_car(liste_car: List[str]) -> Dict[str, int]:
          """
          Création d'un dictionnaire dont les clés sont les caratères présents dans
          la liste liste_car et dont les valeurs sont les nombres de fois que ces
          caractères sont présents.
          """
      ```

   2. Définir la fonction dont la spécification est :

      ```python
      def analyse_dict_car(dict_car: Dict[str, int]) -> Dict[str, float]:
          """
          Création d'un dictionnaire des caractères présents, comme clés, dans le
          dictionnaire dict_car et dont les valeurs représentent les fréquences
          d'apparition de ces caractères (en pourcentages).
          """
      ```

   3. Appeler les deux fonctions précédentes depuis la fonction `main` :

      ```python
      def main():
          """ Fonction principale qui appelle toutes les autres. """
          roman = "la-jangada.txt"
          liste_caracteres = extraction_caracteres(roman)
          liste_caracteres = nettoyage(liste_caracteres)
          liste_caracteres = transformation_accents(liste_caracteres)
          liste_caracteres = transformation_minuscules(liste_caracteres)
          dict_car = creation_dict_car(liste_caracteres)
          print(dict_car)
          dict_car = analyse_dict_car(dict_car)
          print(dict_car)
      ```

   4. Définir la fonction `affichage` suivante :

      ```python
      def affichage_dict(dic_car: Dict[str, float]) -> None:
          """
          Affichage du contenu d'un dictionnaire classé en fonction des valeurs,
          de la plus grande à la plus petite.
          """
          liste_couples = []
          for cle in dic_car.keys():
              liste_couples.append((cle, dic_car[cle]))
          for couple in sorted(liste_couples, key=lambda c: c[1], reverse=True):
              print("{} : {}".format(couple[0], couple[1]))
      ```

   5. Appeler la fonction `affichage` depuis la fonction `main` :

      ```python
      def main():
          """ Fonction principale qui appelle toutes les autres. """
          roman = "la-jangada.txt"
          liste_caracteres = extraction_caracteres(roman)
          liste_caracteres = nettoyage(liste_caracteres)
          liste_caracteres = transformation_accents(liste_caracteres)
          liste_caracteres = transformation_minuscules(liste_caracteres)
          dict_car = creation_dict_car(liste_caracteres)
          dict_car = analyse_dict_car(dict_car)
          affichage_dict(dict_car)
      ```

      Le résultat devrait être :

      ```shell
      E : 16.632918585196244
      A : 9.091462562178396
      S : 7.618122043284734
      I : 7.475838929201186
      T : 7.3603889222110475
      N : 7.062518884644699
      R : 6.763972382193641
      U : 6.239937584839971
      O : 5.488159609634664
      L : 5.407434800059529
      D : 3.845702869564041
      C : 3.051533094917043
      M : 2.804397923703781
      P : 2.7110457696140995
      V : 1.6641036163812735
      Q : 1.2776166789181973
      F : 1.2045584713697512
      G : 1.0210109993190255
      B : 0.9781682232875292
      H : 0.7709444802720291
      J : 0.6358769916253647
      X : 0.376790940782264
      Y : 0.2611154454972242
      Z : 0.24352735849482052
      K : 0.01127441474513058
      W : 0.0015784180643182812
      ```

   
---
   
   ##### Solution
   
   ```python
   from typing import List, Dict, Sequence
   import string
   
   
   def affichage_dict(dic_car: Dict[str, float]) -> None:
       """
       Affichage du contenu d'un dictionnaire classé en fonction des valeurs,
       de la plus grande à la plus petite.
       """
       liste_couples = []
       for cle in dic_car.keys():
           liste_couples.append((cle, dic_car[cle]))
       for couple in sorted(liste_couples, key=lambda c: c[1], reverse=True):
           print("{} : {}".format(couple[0], couple[1]))
   
   
   def analyse_dict_car(dict_car: Dict[str, int]) -> Dict[str, float]:
       """
       Création d'un dictionnaire des caractères présents, comme clés, dans le
       dictionnaire dict_car et dont les valeurs représentent les fréquences
       d'apparition de ces caractères.
       """
       dict_frequences = {}
   
       nbre_car = 0
       for nbre in dict_car.values():
           nbre_car += nbre
   
       for cle in dict_car.keys():
           dict_frequences[cle] = dict_car[cle] / nbre_car * 100
   
       return dict_frequences
   
   
   def creation_dict_car(liste_car: List[str]) -> Dict[str, str]:
       """
       Création d'un dictionnaire dont les clés sont les caratères présents dans
       la liste liste_car et dont les valeurs sont les nombres de fois que ces
       caractères sont présents.
       """
       dict_car = {}
       for car in liste_car:
           if car in dict_car.keys():
               dict_car[car] += 1
           else:
               dict_car[car] = 1
       return dict_car
   
   
   def transformation_minuscules(liste_car: List[str]) -> List[str]:
       """
       Transforme toutes les minuscules de la liste liste_car en majuscules.
       """
       for i in range(len(liste_car)):
           if liste_car[i].islower():
               liste_car[i] = liste_car[i].upper()
       return liste_car
   
   
   def trouve_indice(car: str, seq: Sequence) -> int:
       """
       Détermine le premier indice du caractère car dans liste.
       On suppose que car appartient à la liste.
       
       Ainsi trouve_indice('a', "jkhdsalkj") retourne 5.
       """
       indice = 0
       for elt in seq:
           if car == elt:
               return indice
           indice += 1
   
   
   def transformation_accents(liste_car: List[str]) -> List[str]:
       """
       Transforme chaque caractère accentué en son équivalent sans accent.
       """
       accents = "âãàéèêëïîôôùüûÂÁÀÃÉÈËÊÎÏÔOÕõÙÜÛçÇÑñń"
       equivalents = "aaaeeeeiioouuuAAAAEEEEIIOOOOUUUcCNnn"
   
       for i in range(len(liste_car)):
           if liste_car[i] in accents:
               indice_car = trouve_indice(liste_car[i], accents)
               nouveau_car = equivalents[indice_car]
               liste_car[i] = nouveau_car
       return liste_car
   
   
   def suppression_chiffres(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères invisibles dans la liste.
       """
       i = 0
       while i < len(liste_car):
           if liste_car[i] in string.digits:
               del liste_car[i]
               continue
           i += 1
       return liste_car
   
   
   def suppression_blancs(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères invisibles dans la liste.
       """
       i = 0
       while i < len(liste_car):
           if liste_car[i] in string.whitespace:
               del liste_car[i]
               continue
           i += 1
       return liste_car
   
   
   def suppression_ponctuation(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères de ponctuation dans la liste.
       """
       ponctuations = string.punctuation + "«»°"
       i = 0
       while i < len(liste_car):
           if liste_car[i] in ponctuations:
               del liste_car[i]
               continue
           i += 1
       return liste_car
   
   
   def nettoyage(liste_car: List[str]) -> List[str]:
       """
       Supprime tous les caractères de ponctuation, les blancs et les chiffres
       dans la liste.
       """
       a_supprimer = string.punctuation + "«»°" + string.whitespace + string.digits
       i = 0
       while i < len(liste_car):
           if liste_car[i] in a_supprimer:
               del liste_car[i]
               continue
           i += 1
       return liste_car
   
   
   def extraction_caracteres(nom_fichier: str) -> List[str]:
       """
       Ouvre le fichier nom_fichier, extrait l'ensemble des caractères
       sous forme d'une unique chaîne de caractères puis crée une liste 
       dont chaque élément est un caractère présent dans le texte initial.
       """
       with open(nom_fichier, 'r', encoding='utf-8-sig') as f:
           chaine_contenu = f.read()
       return list(chaine_contenu)
   
   
   def main():
       """ Fonction principale qui appelle toutes les autres. """
       
       # Création du dictionnaire de référence
       roman = "la-jangada.txt"
       liste_caracteres_ref = extraction_caracteres(roman)
       liste_caracteres_ref = nettoyage(liste_caracteres_ref)
       liste_caracteres_ref = transformation_accents(liste_caracteres_ref)
       liste_caracteres_ref = transformation_minuscules(liste_caracteres_ref)
   
       dict_car_ref = creation_dict_car(liste_caracteres_ref)
       dict_car_ref = analyse_dict_car(dict_car_ref)
   #     print(dict_car_ref)
       
       affichage_dict(dict_car_ref)
   
       # Analyse du texte chiffré
       texte = "texte-chiffre.txt"
       liste_caracteres_chif = extraction_caracteres(texte)
       liste_caracteres_chif = nettoyage(liste_caracteres_chif)
       
       dict_car_chif = creation_dict_car(liste_caracteres_chif)
       dict_car_chif = analyse_dict_car(dict_car_chif)
   #    print(dict_car_chif)
       print("----------------------------------------")
       affichage_dict(dict_car_chif)
   
   
   main()
   ```
   
   