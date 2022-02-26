---
title: "Modéliser les notes des élèves"
subtitle: "Chapitre 6,3"
author: ""
type: ""
date: 2020-10-13T05:06:51+04:00
draft: false
toc: true
tags: ["Dictionnaire", "Liste"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

## Partie 1 : Modélisation simpliste

On modélise les notes d'une élève de la faon suivante :
```python
notes_de_lea = [12, 14, 3, 16, 17, 2, 13, 19]
``` 
1. Quel est le type de `notes_de_lea`&nbsp;?
    - un `int`
    - une liste
    - un tuple
    - un dictionnaire
    - autre chose
{{% solution "Réponse" %}}

Type : `int`.

{{% /solution %}}

2. Que vaut l'expression `notes_de_lea[2]`&nbsp;?
    - 3
    - 14
    - 6
    - 5
    - autre chose
{{% solution "Réponse" %}}

`notes_de_lea[2]` vaut 3.

{{% /solution %}}

3. Quelle instruction permet d'ajouter une note de 15 à cette structure de données&nbsp;?
    - `notes_de_lea.append(15)` 
    - `notes_de_lea[8] = 15` 
    - `notes_de_lea.append([15])` 
    - `notes_de_lea = notes_de_lea + 15`     
{{% solution "Réponse" %}}

Ajout à la fin d'une liste : `notes_de_lea.append(15)`.

{{% /solution %}}

4. On propose le code suivant :
{{< highlight py3 "linenos=table" >}}
def fonction(liste_de_notes):
    """
    'liste_de_notes' est une liste de nombres qui modélise
    les notes d’un élève.
    Cette fonction renvoie ???
    """
    compteur1 = 0
    compteur2 = 0
    for note in liste_de_notes:
        if note >= 10:
            compteur1 = compteur1 + 1
        else:
            compteur2 = compteur2 + 1
    return (compteur1, compteur2)
    
notes_de_lea = [12, 14, 3, 16, 17, 2, 13, 19]
assert fonction(notes_de_lea) == ???
{{< / highlight >}}

- Quel est le type de retour de cette fonction&nbsp;?
- Recopier et compléter la ligne 17 de ce code.
- Recopier et compléter la ligne 5 de ce code. On demande ici d'expliquer en quelques mots ce que fait cette fonction.

{{% solution "Réponses" %}}

- Type de la valeur de retour : `tuple`
- `assert fonction(notes_de_lea) == (6, 2)`
- Cette fonction renvoie le nombre de notes supérieures ou égales à 10 et le nombre de notes inférieures à 10.

{{% /solution %}}

## Partie 2 : Modélisation avec une structure de données imbriquées

La modélisation précédente n'est pas satisfaisante si l'on veut conserver les notes de plusieurs élèves dans une même structure de données.    
On propose, dans cette partie, de modéliser les notes des élèves de la façon suivante :
```python
notes_de_la_classe = [('Enzo', 3), ('Emma', 16), ('Lucas', 14), ('Manon', 13)]
```    

1. Quel est le type de `notes_de_la_classe`&nbsp;?
    - un `int` 
    - une liste
    - un tuple
    - un dictionnaire
    - autre chose
{{% solution "Réponse" %}}

Type : liste.

{{% /solution %}}

2. Que vaut l'expression `notes_de_la_classe[2]`&nbsp;?
    - `14`
    - `'Lucas'`
    - `('Lucas', 14)` 
    - `'Emma'` 
    - `16` 
    - autre chose
{{% solution "Réponse" %}}

`notes_de_la_classe[2]` vaut `('Lucas', 14)`.

{{% /solution %}}

3. Quelle instruction permet d'ajouter à cette structure de données une note de 15 obtenue par Farid&nbsp;?
{{% solution "Réponse" %}}

`notes_de_la_classe.append(('Farid', 15))`

{{% /solution %}}

4. On veut écrire une fonction `nom_du_genie` qui prend une telle structure de données en paramètre et qui renvoie le nom de l'élève qui a eu la meilleure note.
    - Proposer un test pour cette fonction.
    - On donne le code mélangé de cette fonction. À vous de le remettre dans l'ordre !
```python
        note_max = note
    note_max = None
def nom_du_genie(les_notes):
    return genie
        genie = nom
    genie = None
        if note_max == None or note > note_max:
    for (nom, note) in les_notes:
```    
{{% solution "Réponses" %}}

```python
def nom_du_genie(les_notes):
    note_max = None
    genie = None
    for (nom, note) in les_notes:
        if note_max == None or note > note_max:
            genie = nom
            note_max = note
    return genie
```

{{% /solution %}}     

5. Que vaut l'expression `nom_du_genie([])`&nbsp;?
    - `None`
    - `''` 
    - `0` 
    - `()` 
    - rien : cette expression génère une erreur
{{% solution "Réponse" %}}

L'expression retourne `None` 

{{% /solution %}}

## Partie 3 : Une modélisation plus complète

Dans cette partie, on souhaite modéliser dans une même structure de données les notes des élèves d'une classe en précisant le nom de la matière concernée par la note. On propose la modélisation suivante :
```python
notes = {'Enzo' : ('Math', 3), 'Emma' : ('Math', 16),
        'Lucas' : ('NSI', 14), 'Manon' : ('Math', 3)}
```

1. Quel est le type de `notes`&nbsp;?
    - un `int` 
    - une liste
    - un tuple
    - un dictionnaire
    - autre chose
{{% solution "Réponse" %}}

Type : dictionnaire.

{{% /solution %}}

2. Que vaut l'expression `notes[2]`&nbsp;?
    - `14`
    - `'Lucas'` 
    - `('NSI', 14)` 
    - `3`
    - cette expression génère une erreur
{{% solution "Réponse" %}}

`notes[2]` génère une erreur.

{{% /solution %}}

3. Quelle instruction permet d'ajouter la note de 15 obtenue par Farid en NSI&nbsp;?
{{% solution "Réponse" %}}

`notes['Farid'] = ('NSI', 15)`

{{% /solution %}}

4. Quel est l'affichage généré par l'exécution du code suivant&nbsp;?
```python
for (nom, (matiere, note)) in notes.items():
    if note < 15:
        print(nom)
``` 
{{% solution "Réponse" %}}

Le code affiche les noms des élèves qui ont une note inférieure à 15.

{{% /solution %}}

5. On veut écrire une fonction qui prend une telle structure de données en paramètre et qui renvoie le nom de l'élève qui a eu la moins bonne note, toutes matières confondues.
    - Proposer une test pour cette fonction.
    - Écrire le code de cette fonction.
{{% solution "Réponses" %}}

```python
def moins_bon(notes: Dict[str, Tuple[str, int]]) -> List[str]:
    note_moins_bonne = 20
    rep = []

    for (nom, t_matiere) in notes.items():
        note = t_matiere[1]

        if note < note_moins_bonne:
            rep = [nom]
            note_moins_bonne = note
        elif note == note_moins_bonne:
            rep.append(nom)

    return rep

if __name__ == "__main__":
    notes = {'Enzo' : ('Math', 3), 'Emma' : ('Math', 16), 'Lucas' : ('NSI', 14), 'Manon' : ('Math', 3)}
    
    moins_bon(notes) == ['Enzo', 'Manon']
```

{{% /solution %}}

6. On veut écrire une fonction `tri_par_matiere` qui prend une telle structure de données en paramètre et qui renvoie un dictionnaire dont les clés sont les noms des matières, et les valeurs la liste des notes obtenues par les élèves dans chaque matière.

**Exemple :**
```python
>>> notes = {'Enzo' : ('Math', 3), 'Emma' : ('Math', 16),
        'Lucas' : ('NSI', 14), 'Manon' : ('Math', 3)}
>>> tri_par_matiere(notes)
{'Math': [3, 3, 16], 'NSI': [14]}
``` 
Écrire le code de cette fonction.

{{% solution "Réponse" %}}

```python
def tri_par_matiere(notes: Dict[str, Tuple[str, int]]) -> Dict[str, List[int]]:
    rep = {}

    for nom, t_matiere in notes.items():
        matiere = t_matiere[0]
        note = t_matiere[1]

        if matiere not in rep.keys():
            rep[matiere] = [note]
        else:
            rep[matiere].append(note)

    return rep
```

{{% /solution %}}