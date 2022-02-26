---
title: "Simulation du fonctionnement d'une banque"
subtitle: "Chapitre 4,2"
author: ""
type: ""
date: 2020-09-26T20:06:58+04:00
draft: false
toc: true
tags: ["Objet", "Classe", "Attribut", "Méthode", "Instance", "Encapsulation"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

L'objectif de ce document est de simuler (sommairement bien sûr) le fonctionnement d'une banque. Le programme doit permettre : 
- La création d'une banque ;
- La création de comptes bancaires ;
- La création de personnes propriétaires de ces comptes bancaires.

Une correction se trouve à cette adresse : {{< remote "https://repl.it/@dlatreyte/banque" "https://repl.it/@dlatreyte/banque" >}}

## Classe Personne

Dans un module nommé `personne`, créer la classe `Personne` dont la spécification est la suivante :
```python
class Personne():
    """
    Modélisation d'une personne.

    Attributs
    ---------
    - nom : str
        Renseigné à la création de l'objet
    - Prenom : str
        Renseigné à la création de l'objet
    - email : str
        Email. Initialisé à ""
    - telephone : str
        Numéro de téléphone. Initialisé à ""
    - date_naissance : str
        Chaîne de caractères au format jour/mois/année (4 chiffres). Initialisé à ""
    - jour_naissance : int
        Déterminé à partir de la date de naissance. Initialisée à -1
    - mois_naissance : int
        Déterminé à partir de la date de naissance. Initialisée à -1
    - annee_naissance : int
        Déterminé à partir de la date de naissance. Initialisée à -1
    """
```

Les spécifications des méthodes sont les suivantes :
```python
def __init__(self, nom: str, prenom: str) -> None:
    """
    Initialisation des attributs.
    """
```

```python
def modifier_nom(self, nom: str) -> None:
        """
        Permet de modifier le nom de la personne.
        """
```

```python
def obtenir_nom(self) -> str:
        """
        Retourne le nom de la personne.
        """
```

```Python
def modifier_prenom(self, prenom: str) -> None:
        """
        Permet de modifier le prénom de la personne.
        """
```

```python
def obtenir_prenom(self) -> str:
        """
        Retourne le prénom de la personne.
        """
```

```python
def obtenir_email(self) -> str:
        """
        Retourne l'email de la personne.
        """
```

```python
def renseigner_email(self, email: str) -> None:
        """
        Renseigne l'attribut email de la personne.
        """
```

```python
def obtenir_telephone(self) -> str:
        """
        Retourne le numéro de téléphone de la personne.
        """
```

```python
def renseigner_telephone(self, telephone: str) -> None:
        """
        Renseigne l'attribut telephone de la personne.
        """
``` 

```python
def renseigner_date_naissance(self, date: str) -> None:
        """
        Récupère la date de naissance sous la forme jour/mois/année.
        Renseigne l'attribut date_naissance et, après un traitement, les attributs
        jour_naissance, mois_naissance, annee_naissance.
        
        Lève une exception de type ValueError si l'année ne possède pas le bon format.
        """
```

```python
def obtenir_date_naissance(self) -> str:
        """
        Retourne la date de naissance.
        """
```

```python
def obtenir_age(self, annee_en_cours: int) -> int:
        """
        Retourne l'age de la personne à partir de l'année en cours.

        Lève une exception de type Exception si la date de naissance n'a pas été renseignée au préalable.
        """
```

La méthode `infos` suivante doit aussi faire parti de cette classe :
```python
def infos(self) -> str:
        """
        Retourne toutes les informations relatives à la personne.
        """

        chaine = """
        Prénom : {}
        Nom : {}
        Date de naissance : {}
        Email : {}
        Téléphone : {}
        """.format(self.obtenir_prenom(), self.obtenir_nom(),
                   self.obtenir_date_naissance(), self.obtenir_email(),
                   self.obtenir_telephone())

        return chaine
```

{{% note warning %}}
Tester la classe en instanciant au moins un objet de type `Personne` et en utilisant toutes les méthodes.
{{% /note %}}

## Classe Compte_bancaire

Dans un module nommé `compte_bancaire` créer la classe `Compte_bancaire` dont la spécification est la suivante :
```python
class Compte_bancaire():
    """
    Définition d'un compte bancaire.

    Attributs
    ---------
    - proprietaire : Personne
        Personne propriétaire du compte. Initialisé à la création de l'objet.
    - identifiant : int
        Identifiant unique du compte. Initialisé à la création de l'objet par un calcul réalisé par une méthode statique.
    - solde : float
        Solde du compte. Initialisé à la création de l'objet.
```
Les spécifications des méthodes sont les suivantes :

{{% note warning %}}
Ne pas oublier d'importer la classe `Personne` du module `personne` au début du fichier.
{{% /note %}}

```python 
def __init__(self, proprietaire: Personne, montant_initial: float) -> None:
    """
    Initialisation des attributs.
    """
```

```python
@staticmethod
def determine_id(proprietaire: Personne) -> int:
    """
    Détermine l'identifiant du compte aléatoirement à partir du
    nom et du prénom du propriétaire.

    Méthode statique
    """
```

```python
def obtenir_solde(self) -> float:
    """
    Retourne le solde du compte.
    """
``` 

```python
def depot(self, montant: float) -> None:
    """
    Ajoute montant au solde
    """
```

```python
def retrait(self, montant: float) -> None:
    """
    Retire le montant montant du solde à la condition qu'il y ait suffisamment d'argent.
    Une exception de type ValueError est levée si le montant est trop important
    """
```

La méthode `infos` suivante fait aussi partie de la classe :
```python
def infos(self) -> str:
    """
    Informations sur le compte.
    """
    chaine = """
    Compte numéro : {}
    Solde : {}
    """.format(self.identifiant, self.solde)

    chaine = chaine + self.proprietaire.infos()

    return chaine
```

{{% note warning %}}
Tester la classe en instanciant au moins un objet de type `Compte_bancaire` et en utilisant toutes les méthodes.
{{% /note %}}

## Classe Banque

Cette classe est de loin la moins développée du document, vous pourrez ajouter des méthodes selon vos idées.

Dans un module nommé `banque`, créer la classe `Banque` dont la spécification est la suivante :
```python
class Banque():
    """
    Modélisation d'une banque.

    Attributs
    ---------
    - nom : str
        Nom de la banque. Initialisé lors de la création de l'objet.
    - comptes : Liste[Compte_bancaire]
        Liste des comptes bancaires au sein de la banque.
    """
```

{{% note warning %}}
- Ne pas oublier d'importer la classe `Personne` du module `personne` au début du fichier.
- Ne pas oublier d'importer la classe `Compte_bancaire` du module `compte_bancaire` au début du fichier.
{{% /note %}}

Les spécifications des méthodes sont les suivantes :

```python
def __init__(self, nom: str) -> None:
    """
    Initialisation de l'objet
    """
```
Incorporer les méthodes suivantes dans la classe :
```python
def creation_compte(self) -> None:
    """
    Prend en charge l'ouverture d'un compte au sein de la banque.
    """
    print("Procédure de création du compte :")
    print("---------------------------------")

    nom = input("Nom du propriétaire du compte : ")
    prenom = input("Prenom du propriétaire du compte : ")
    montant_initial = float(input("Montant du dépôt initial : "))

    p = Personne(nom, prenom)
    c = Compte_bancaire(p, montant_initial)

    self.comptes.append(c)

def infos(self) -> str:
    """
    Informations sur la banque
    """
    chaine = """
    -----------
    """

    for compte in self.comptes:
        chaine = chaine + compte.infos()
        chaine = """
        -----------
        
        """
    
    return chaine
``` 

## Programme principal

Dans le fichier nommé `main`, instancier un objet de type `Banque` et créer quelques comptes bancaires.


