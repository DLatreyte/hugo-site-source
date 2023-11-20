---
title: "Le codage d'Huffman"
subtitle: ""
author: ""
type: ""
date: 2020-11-16T16:11:14+04:00
draft: false
toc: true
tags: ["Arbre binaire", "Compression"]
categories: ["Terminales Spé NSI", "Informatique"]
image: ""
solution_est_visible: true
auto_numbering: true
---

> Cette séance a pour objet l'étude d'une méthode de compression de données inventée par David Albert Huffman en 1952. Cette méthode permet de réduire la longueur du codage d’un alphabet et repose sur la création d’un arbre binaire.

## Différents types de codages

{{% note normal %}}
*On appelle **alphabet** l’ensemble des symboles (caractères) composant la donnée de départ à compresser.*
{{% /note %}}

Dans la suite, nous utiliserons un alphabet composé seulement des 8 lettres A, B, C, D, E, F, G et H.

On cherche à coder chaque lettre de cet alphabet par une séquence de chiffres binaires.

1. Combien de bits sont nécessaires pour coder chacune des 8 lettres de l’alphabet&nbsp;?
{{% solution "Réponse" %}}

Il faut coder 8 caractères, on a donc besoin de 3 bits, puisque $2^3 = 8$.

{{% /solution %}}

2. Quelle est la longueur en octets d’un message de 1 000 caractères construit sur cet alphabet&nbsp;?
{{% solution "Réponse" %}}

- $1000 \times 3 = 3000$ bits sont nécessaires.
- $\dfrac{3000}{8} = 375$ octets sont nécessaires.

{{% /solution %}}

3. Proposer un code de taille fixe pour chaque caractère de l’alphabet de 8 lettres.
{{% solution "Réponse" %}}

A&nbsp;: 000&nbsp;; B&nbsp;: 001&nbsp;; C&nbsp;: 010&nbsp;; D&nbsp;: 011&nbsp;; E&nbsp;: 100&nbsp;; F&nbsp;: 101&nbsp;; G&nbsp;: 110 et H&nbsp;: 111.

{{% /solution %}}

On considère maintenant le codage suivant, la longueur du code de chaque caractère étant variable.

<center>

| **Lettre** | A | B | C | D | E | F | G | H |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| **Code** | 10 | 001 | 000 | 1100 | 01 | 1101 | 1110 | 1111 |

</center>

{{% note normal %}}
Ce type de code est dit **préfixe**, ce qui signifie qu’*aucun code n’est le préfixe d’un autre* (le code de A est 10 et aucun autre code ne commence par 10, le code de B est 001 et aucun autre code ne commence par 001). Cette propriété permet de séparer les caractères de manière non ambiguë.
{{% /note %}}

4. En utilisant la table précédente, donner le code du message : CACHE.
{{% solution "Réponse" %}}

CACHE&nbsp;: 00010000111101

{{% /solution %}}

5. Quel est le message correspondant au code 001101100111001.
{{% solution "Réponse" %}}

001101100111001 : BADGE

{{% /solution %}}

Dans un texte, chacun des 8 caractères a un nombre d’apparitions différent. Cela est résumé dans le tableau suivant, construit à partir d’un texte de 1 &nbsp;000 caractères.

<center>

| **Lettre** | A | B | C | D | E | F | G | H |
| :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: | :----: |
| **Nombre** | 240 | 140 | 160 | 51 | 280 | 49 | 45 | 35 |

</center>

7. En utilisant le code de taille fixe proposé à la question 3., quelle est la longueur en bits du message contenant les 1 000 caractères énumérés dans le tableau précédent&nbsp;?
{{% solution "Réponse" %}}

Si on utilise 3 bits pour chaque caractère, il faut $1000 \times 3 = 3000$ bits pour coder le message.

{{% /solution %}}

8. En utilisant le code de la question 4., quelle est la longueur du même message en bits&nbsp;?
{{% solution "Réponse" %}}

$N = f(A)\cdot l(A) + f(B)\cdot l(B) + f(C)\cdot l(C) + f(D)\cdot l(D) + f(E)\cdot l(E) + f(F)\cdot l(F) + f(G)\cdot l(G) + f(H)\cdot l(H)$ où $f(x_i)$ est la fréquence du caractère $x_i$ et $l(x_i)$ la longueur (en bits) du codage du caractère $x_i$.
**A.N.** $N = 240 \times 2 + 140 \times 3 + 160 \times 3 + 51 \times 4 + 280 \times 2 + 49 \times 4 + 45 \times 4 + 35 \times 4 = 2660$

{{% /solution %}}

{{% note normal %}}
Ce type de codage réserve le codage le plus court aux caractères les plus fréquents.
{{% /note %}}

## Codage de Huffman

L’objectif du codage de Huffman est de trouver le codage proposé à la question 4.

{{% note normal %}}
*Le codage de Huffman minimise la taille en nombre de bits du message codé en se basant sur le nombre d’apparition de chaque caractère (un caractère qui apparaît souvent aura un code plutôt court).*

- Pour déterminer le code optimal, on considère 8 arbres, chacun réduit à une racine, contenant le symbole et son nombre d’apparitions.
{{% /note %}}
{{< mermaid >}}
graph TD
    A("A | 240")
    B("B | 140")
    C("C | 160")
    D("D | 51")
    E("E | 280")
    F("F | 49")
    G("G | 45")
    H("H | 35")
{{< /mermaid >}}
{{% note normal %}}
- On fusionne ensuite les deux arbres contenant les plus petits nombres d’apparitions (valeur inscrite sur la racine), et on affecte à ce nouvel arbre la somme des nombres d’apparitions de ses deux sous-arbres. Lors de la fusion des deux arbres, le choix de mettre l’un ou l’autre à gauche n’a pas d’importance. Nous choisissons ici de mettre le plus fréquent à gauche (s’il y a un cas d’égalité, nous faisons un choix arbitraire).
{{% /note %}}
{{< mermaid >}}
graph TD
    A("A | 240")
    B("B | 140")
    C("C | 160")
    D("D | 51")
    E("E | 280")
    F("F | 49")
    I("80") --> G
    I("80") --> H
    G("G | 45")
    H("H | 35")
{{< /mermaid >}}
{{% note normal %}}
- On recommence jusqu’à ce qu’il n’y ait plus qu’un seul arbre.
{{% /note %}}

9. Combien d’étapes (combien de fusions d’arbres) sont nécessaires pour que cet algorithme se termine&nbsp;?

10. En suivant l’algorithme précédent, construire l’arbre de Huffman.

{{% note normal %}}
Le code à affecter à chaque lettre est déterminé par sa position dans l’arbre. Précisément, le code d’un symbole de l’alphabet décrit le chemin de la racine à la feuille qui le contient : *un 0 indique qu’on descend par le fils gauche et un 1 indique qu’on descend par le fils droit*.
{{% /note %}}

{{< mermaid >}}
graph TD
    A(" ") --> B(" ")
    B --> X("X")
    B --> Y("Y")
    A --> Z("Z")
{{< /mermaid >}}

Dans le cas de l’arbre ci-dessus le code de X est 00 (deux fois à gauche), le code de Y est 01, et celui de Z est 1.

11. Sur chaque arête de l’arbre construit à la question 10., inscrire 0 ou 1 selon que l’arête joint un fils gauche ou un fils droit.

12. Quel est le code de F&nbsp;?

Le code suivant permet, à partir d’un fichier nommé texte.txt, de construire l’arbre de Huffman puis un dictionnaire qui associe à chaque caractère du fichier d’entrée son code sous forme d’une séquence de bits (liste de 0 et de 1).

## Implémentation en Python de l'algorithme

13. Écrire le code (et la spécification !) de la classe `Noeud`, nœud d'un arbre binaire.
Par rapport à l'implémentation réalisée lors des TP précédenrs, ajouter le champ `lettre` initialisé à la chaîne de caractères vide et la méthode suivante :

```python
def __lt__(self, n: Noeud):
        """
        Comparaison de deux noeuds = comparaison des valeurs
        """
        return self.valeur < n.valeur
```

{{% solution "Réponse" %}}

```python
class Noeud:
    def __init__(self: Noeud, val: int, let: str = "") -> None:
        """
        Initialisation de l'objet.
        """
        self.valeur = val
        self.lettre = let
        self.gauche = None
        self.droit = None

    def __lt__(self: Noeud, n: Noeud) -> bool:
        """
        Comparaison de deux noeuds = comparaison des valeurs
        """
        return self.valeur < n.valeur
```

{{% /solution %}}

14. Écrire les codes (et la spécification !) des fonctions `est_vide`, `est_feuille`, `parcours_prefixe` qui, respectivement  teste si un nœud est vide, teste si un nœud est une feuille et finalement affiche l'arbre.

{{% solution "Réponse" %}}

```python
def est_vide(n: Noeud) -> bool:
    """
    Détermine si l'arbre est vide.
    """
    return n is None


def est_feuille(n: Noeud) -> bool:
    """
    Détermine si le noeud est une feuille.
    """
    return (n.gauche is None) and (n.droit is None)


def parcours(n: Noeud) -> str:
    """
    Parcours en profondeur préfixe de l'arbre.
    """
    if n is None:
        return ""
    else:
        chaine = str(n.valeur)
        chaine += parcours(n.gauche)
        chaine += parcours(n.droit)
        return chaine
```

{{% /solution %}}
15. Écrire le code de la fonction `creation_table_frequences` dont la spécification est

```python
def creation_table_frequences(message: str) -> dict[str, int]:
    """
    Établit la table des fréquences des caractères dans message.
    """
```

Tester la fonction avec l'instruction :

```python
assert creation_table_frequences("ABRACADABRA") == {'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}
```

{{% solution "Réponse" %}}

```python
def creation_table_frequences(message: str) -> dict[str, int]:
    """
    Établit la table des fréquences des caractères dans message.
    """
    dic = {}
    for car in message:
        if car in dic.keys():
            dic[car] += 1
        else:
            dic[car] = 1
    return dic
```

{{% /solution %}}

16. Lire le document sur [les files de priorité](http://pascal.ortiz.free.fr/contents/python/structures_de_donnees/les_files_de_priorite.html).  
Écrire le code de la fonction `construction_arbre_huffman` dont la spécification est

```python
def construction_arbre_huffman(dic_frequences: dict[str, int]) -> Noeud:
    """
    Construction de l'arbre de Huffman.
    """
```

et l'algorithme (cf. Cormen, *Algorithmes*)
<img src="/terminales-nsi/chap-9/chap-9-4-1.png" alt="" width="70%" />

{{% note warning %}}
Cet algorithme est un exemple d'**algorithme glouton** dans lequel on prend la décision qui semble la meilleure à un instant donné.
{{% /note %}}

{{% solution "Réponse" %}}

```python
def construction_arbre_huffman(dic_frequences: dict[str, int]) -> Noeud:
    """
    Construction de l'arbre de Huffman.
    """
    file = []

    # Création de tous les noeuds et insertion dans la file
    for lettre, frequence in dic_frequences.items():
        noeud = Noeud(frequence, lettre)
        heappush(file, noeud)

    # Construction de l'arbre
    for i in range(len(dic_frequences) - 1):
        noeud_droit = heappop(file)
        noeud_gauche = heappop(file)
        # Nouvel arbre
        nouvelle_valeur = noeud_droit.valeur + noeud_gauche.valeur
        noeud = Noeud(nouvelle_valeur)
        noeud.droit = noeud_droit
        noeud.gauche = noeud_gauche
        # Intégration à la file
        heappush(file, noeud)

    # Retour de l'arbre
    return heappop(file)
```

{{% /solution %}}

17. Écrire une fonction nommée `codes_huffman_parcours` dont la spécification est :

```python
def codes_huffman_parcours(a: Noeud, dic: dict[str, str], code: str) -> None:
    """
    Parcours de l'arbre et construction des codes et du dictionnaire passé en argument.
    Les lettres constituent les clés et les codes les valeurs.

    Algorithme récursif.
    """
```

{{% solution "Réponse" %}}

```python
def codes_huffman_parcours(a: Noeud, dic: dict[str, str], code: str) -> None:
    """
    Parcours de l'arbre et construction des codes et du dictionnaire passé en argument.
    Les lettres constituent les clés et les codes les valeurs.

    Algorithme récursif.
    """
    if est_feuille(a):
        # Cas de base : on modifie le dictionnaire
        dic[a.lettre] = code
        return None
    else:
        codes_huffman_parcours(a.gauche, dic, code + "0")
        codes_huffman_parcours(a.droit, dic, code + "1")
```

{{% /solution %}}

18. Écrire une fonction nommée `encodage` dont la spécification est :

```python
def encodage(message: str, codes: dict[str, str]) -> str:
    """
    Retourne la chaîne de bits produite par le codage de Huffman pour la chaîne message.
    """
```

{{% solution "Réponse" %}}

```python
def encodage(message: str, codes: dict[str, str]) -> str:
    """
    Retourne la chaîne de bits produite par le codage de Huffman pour la chaîne message.
    """
    message_code = ""
    for car in message:
        message_code += codes[car]
    return message_code
```

{{% note warning %}}

Il est impératif de savoir écrire le code de cette fonction !

{{% /note %}}

{{% /solution %}}

19. Écrire une fonction nommée `decodage` dont la spécification est :

```python
def decodage(message_compresse: str, codes: dict[str, str]) -> str:
    """
    Retourne le message non compressé à partir du codage de Huffman. 
    """
```

{{% solution "Réponse" %}}

```python
def decodage(message_compresse: str, codes: dict[str, str]) -> str:
    """
    Retourne le message non compressé à partir du codage de Huffman. 

    Étape intermédiaire : passer d'un dictionnaire 'A': '001' à
    '001' : 'A'
    """
    # Inversion clés - valeurs
    dic_inverse = {}
    for cle, valeur in codes.items():
        dic_inverse[valeur] = cle

    # Décodage
    resultat = ""
    code = ""
    for car in message_compresse:
        code += car
        if code in dic_inverse.keys():
            resultat += dic_inverse[code]
            code = ""
    return resultat
```

{{% /solution %}}

{{% note warning %}}

Il est impératif de savoir écrire le code de cette fonction !

{{% /note %}}

### Appels de toutes les fonctions dans la partie principale du programme

```python
if __name__ == "__main__":
    arb = Noeud(12, 'A')
    arb.gauche = Noeud(23, 'B')
    arb.droit = Noeud(48, 'C')
    arb.gauche.gauche = Noeud(49, 'K')
    arb.droit.gauche = Noeud(9, 'H')
    arb.droit.droit = Noeud(78, 'X')

    print(parcours(arb))
    print(arb < Noeud(67, 'E'))

    assert creation_table_frequences("ABRACADABRA") == {
        'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}

    message = "ABRACADABRA"

    # nom_fichier = "livre.txt"
    # with open(nom_fichier, 'r') as f:
    #    message = f.read()

    table_frequences = creation_table_frequences(message)
    arbre = construction_arbre_huffman(table_frequences)
    print(parcours(arbre))

    dic_codes = {}
    codes_huffman_parcours(arbre, dic_codes, '')
    print(dic_codes)

    message_code = encodage(message, dic_codes)
    print(message_code)
    message_decode = decodage(message_code, dic_codes)
    print(message_decode)
```
