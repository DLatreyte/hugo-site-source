---
title: "Programmation Objet"
subtitle: "Chapitre 4,1"
author: ""
type: ""
date: 2020-09-23T21:07:12+04:00
draft: false
toc: true
tags: ["Objet", "Classe", "Attribut", "Méthode", "Instance", "Encapsulation"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Programmation orientée objet

{{% note tip %}}

*Un objet est une instance d'une classe.*

{{% /note %}}

L'un des objectifs principaux de la notion d'objet est d'organiser des programmes complexes grâce aux notions :
- d'**encapsulation** ; 
- d'**abstraction** ; 
- d'**héritage** ; 
- de **polymorphisme** ; 

**Remarque :** Seules les deux premières notions apparaissent dans le programme de NSI.

{{% note tip %}}
#### Encapsulation

Le principe de l'encapsulation est de *regrouper dans le même objet, les données (attributs) et les traitements (méthodes)* qui lui sont spécifiques. Ainsi un objet est défini par ses attributs et ses méthodes.

**Les objets partagent tous les mêmes méthodes mais les attributs leurs sont propres.**
{{% /note %}}

{{% note tip %}}
#### Abstraction

L'intérêt de la POO est qu'elle permet de créer des objets possédant un certain degré d'abstraction.
Ce processus d'abstraction consiste à identifier des caractéristiques et des mécanismes communs pour un ensemble d'éléments.

Attributs
: Ce sont les données de l'objets, ses **caractéristiques**.

Méthodes
: Ce sont les **comportements** de l'objet.
{{% /note %}}

{{% note tip %}}
#### Héritage

Le concept d'**héritage** permet de créer des **sous-classes plus spécialisées** à partir de classes plus générales (appelées super-classe).

- La **super-classe** (classe mère) déclare des méthodes et des attributs communs.
- La **sous-classe** hérite des attributs, des méthodes et du type de la super-classe et peut les redéfinir (cf. *polymorphisme*).
{{% /note %}}

{{% note tip %}}
#### Polymorphisme

Le **polymorphisme** est la faculté pour une **méthode** *portant le même nom mais appartenant à des classes distinctes héritées d'effectuer un travail différent*. 
Cette propriété est acquise par la technique de la **surcharge**.
{{% /note %}}

## Compte bancaire

{{% note normal %}}

Toute cette partie doit être réalisée en utilisant le logiciel [Python Tutor](https://pythontutor.com).   
Sélectionner [Start visualizing your code now](https://pythontutor.com/visualize.html#mode=edit) puis [Live Programming mode](https://pythontutor.com/live.html#code=&cumulative=false&heapPrimitives=nevernest&mode=edit&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false).

{{% /note %}}

Dans ce premier exemple, on considère une classe qui modélise un compte bancaire.

### Une classe est un nouveau type et un objet est une instance de classe

1. Taper et exécuter le code suivant :
```python
class Compte:
    """
    Modélisation d'un compte bancaire.
    """
    pass
``` 

{{% note normal %}}

- Un nom de classe commence toujours (c'est une convention) par une lettre capitale ;
-  `pass` est l'instruction Python qui indique de ne rien faire.

{{% /note %}}

Quelles actions a déclenché le code précédent ?
{{% solution "Réponse" %}}

- Création d'un objet `Classe Compte` ;
- Création d'une variable `Compte` dans l'espace de nom global. Cette variable référence l'objet `Classe Compte`

{{% /solution %}}

2. À la suite, taper et exécuter le code suivant :
```python
compte_1 = Compte()
```

Quelle action a déclenché le code précédent ?
{{% solution "Réponse" %}}

- Création d'un **objet (ou instance)** de la classe `Compte` ;
- Création d'une variable `compte_1` dans l'espace de nom global. Cette variable référence l'objet.

{{% /solution %}}

3. Afin d'en découvrir davantage sur `compte_1`, taper et exécuter l'instruction suivante :
```python
print(compte_1)
``` 

Que nous apprend l'affichage à l'écran ?
{{% solution "Réponse" %}}
```bash
<__main__.Compte object at 0x7f7cc89bec88>
```
`compte_1` appartient à l'espace de nom global et référence un objet de type `Compte` situé à l'adresse 0x7f7cc89bec88.
{{% /solution %}}

4. *«&nbsp;Définir une classe est équivalent à définir un nouveau type.&nbsp;»*   
Quelle instruction Python pourrait démontrer cette affirmation ? 
{{% solution "Réponse" %}}

```python
print(type(compte_1))
```

{{% /solution %}}

### Un objet possède des attributs dont les valeurs lui sont propres

5. Un compte bancaire possède généralement un propriétaire et un solde. Taper et exécuter les lignes de code suivantes :
```python
compte_1.proprietaire = "Pascal"
compte_1.solde = 1000
```

Les attributs (ou variable) `proprietaire` et `solde` appartiennent-ils à l'espace de nom global&nbsp;?
{{% solution "Réponse" %}}

{{% note tip %}}

Les attributs sont des **variables locales à l'objet**.

{{% /note %}}


{{% /solution %}}

6. Taper et exécuter les instructions qui permettent de créer un objet `compte_2` dont le propriétaire se nomme «&nbsp;Natacha&nbsp;» et dont le solde est de 2000.
{{% solution "Réponse" %}}

```python
compte_2 = Compte()
compte_2.proprietaire = "Natacha"
compte_2.solde = 2000
``` 

{{% /solution %}}

7. Les objets `compte_1` et `compte_2` partagent-ils les valeurs des attributs&nbsp;?
{{% solution "Réponse" %}}

Les attributs sont des variables locales à l'objet.

<img src="/terminales-nsi/chap-4/chap-4-1/objet_2.png" alt="" width="60%" />

{{% note tip %}}

Deux instances d'une même classe ne partagent pas leurs attributs.

{{% /note %}}

{{% /solution %}}

### Un objet possède un comportement

8. Modifier le code de définition de la classe de façon à ce qu'il soit :
```python
class Compte:
    """
    Modélisation d'un compte bancaire.
    """
    def retrait(self, valeur: float) -> None:
        """
        Retire valeur au solde.
        """
        self.solde = self.solde - valeur
``` 

La fonction `retrait` est appelée **méthode**. Quelle est sa particularité ?
{{% solution "Réponse" %}}

La fonction `retrait` est locale à la classe ; c'est la raison pour laquelle on parle de **méthode**.

{{% /solution %}}

9. La méthode `retrait` est-elle locale à chaque objet ?
{{% solution "Réponse" %}}

<img src="/terminales-nsi/chap-4/chap-4-1/objet_3.png" alt="" width="60%" />

{{% note tip %}}

Les objets instances d'une même classe **partagent les méthodes**.

{{% /note %}}

{{% /solution %}}

10. Natacha vient de retirer 50. Le code qui permet de prendre en compte ce retrait dans le programme est 
```python
compte_2.retrait(50)
```
- Observer l'effet de l'instruction.
- N'y a-t-il rien de surprenant dans l'appel de la méthode `retrait`&nbsp;?

{{% solution "Réponse" %}}

La définition de la méthode `retrait` fait apparaître deux paramètres : `self` et `valeur` alors que lors de l'appel de la fonction on ne fournit qu'un seul argument qui semble être `valeur`.

{{% /solution %}}

11. À quoi peut bien servir le paramètre `self` dans la définition d'une méthode&nbsp;?
{{% solution "Réponse" %}}

{{% note info %}}

Les méthodes étant partagées par les différentes instances (objets) d'une classe, elle ne peuvent à priori pas savoir sur quel objet elle doivent agir.  
L'information sur cet objet est donc passée automatiquement par Python à la méthode. Pour être plus clair, l'instruction
```python
compte_2.retrait(50)
```
est équivalente à
```python
Compte.retrait(compte_2, 50)
```

{{% /note %}}

{{% note tip %}}

Lorsqu'on définit une méthode, le premier paramètre doit toujours être nommé `self` (c'est une convention). Il représente l'objet sur lequel la méthode doit agir.

{{% /note %}}

{{% /solution %}}

12. Créer l'objet `compte_3` et lui retrirer le montant 100. Quel est le problème&nbsp;?
{{% solution "Réponse" %}}

```python
compte_3 = Compte()
compte_3.retrait(100)
```

On obtient l'erreur suivante :

```bash
AttributeError: 'Compte' object has no attribute 'solde'
```

C'est tout à fait normal car l'objet `compte_3` ne possède par d'attribut `solde`.
{{% /solution %}}

### Les attributs d'un objet doivent être initialisés à la création de cet objet

13. Modifier le code de la classe `Compte` :
```python
class Compte:
    """
    Modélisation d'un compte bancaire.
    """
    def __init__(self, proprietaire: str = "", solde: float = 0) -> None:
        self.proprietaire = proprietaire
        self.solde = solde
        
    def retrait(self, valeur: float) -> None:
        """
        Retire valeur au solde.
        """
        self.solde = self.solde - valeur
```

- Est-ce que l'erreur apparue à la question 12. est toujours présente&nbsp;?

14. Afin de bien comprendre le rôle de la méthode `__init__`, créer le compte `compte_4`. À quoi sert cette méthode ?
{{% solution "Réponse" %}}

La méthode permet d'initialiser l'objet : ses attributs sont automatiquement créés, des valeurs par défaut peuvent même leur être affectées.

{{% /solution %}}

### Toutes les variables ne sont pas des attributs

15. Essayer d'imaginer comment déterminer simplement le nombre de comptes créés.
{{% solution "Réponse" %}}

L'idéal serait qu'un compteur compte soit incrémenté chaque fois qu'un compte est créé.

{{% /solution %}}

16. Modifier le code de la classe `Compte` :
```python
class Compte:
    """
    Modélisation d'un compte bancaire.
    """
    nbre_comptes = 0
    
    def __init__(self, proprietaire: str = "", solde: float = 0) -> None:
        self.proprietaire = proprietaire
        self.solde = solde
        
    def retrait(self, valeur: float) -> None:
        """
        Retire valeur au solde.
        """
        self.solde = self.solde - valeur
```

La variable `nbre_comptes` est-elle locale aux objets ? Est-elle locale à la classe ?
{{% solution "Réponse" %}}

La variable `nbre_comptes` est locale à la classe&nbsp;: **c'est une variable de classe**.

{{% note tip %}}

Les variables de classe sont partagées par tous les objets.

{{% /note %}}

{{% /solution %}}

17. Modifier le code de la classe `Compte` :
```python
class Compte:
    """
    Modélisation d'un compte bancaire.
    """
    nbre_comptes = 0
    
    def __init__(self, proprietaire: str = "", solde: float = 0) -> None:
        Compte.nbre_comptes = Compte.nbre_comptes + 1
        self.proprietaire = proprietaire
        self.solde = solde
        
    def retrait(self, valeur: float) -> None:
        """
        Retire valeur au solde.
        """
        self.solde = self.solde - valeur
``` 
- Comment manipule-t-on une variable de classe ?

{{% solution "Réponse" %}}

{{% note tip %}}

Pour manipuler une variable de classe, il faut précéder son nom du nom de la classe.

{{% /note %}}

{{% /solution %}}