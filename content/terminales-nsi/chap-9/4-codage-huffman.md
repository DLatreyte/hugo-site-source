---
title: "Le codage d'Huffman"
subtitle: "Chapitre 9,4"
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

14. Écrire les codes (et la spécification !) des fonctions `est_vide`, `est_feuille`, `parcours_prefixe` qui, respectivement  teste si un nœud est vide, teste si un nœud est une feuille et finalement affiche l'arbre. 

15. Écrire le code de la fonction `creation_table_frequences` dont la spécification est 
```python
def creation_table_frequences(message: str) -> Dict[str, int]:
    """
    Établit la table des fréquences des caractères dans message.
    """
``` 
Tester la fonction avec l'instruction : 
```python
assert creation_table_frequences("ABRACADABRA") == {'A': 5, 'B': 2, 'R': 2, 'C': 1, 'D': 1}
``` 

16. Lire le document sur {{< remote "les files de priorité" "http://pascal.ortiz.free.fr/contents/python/structures_de_donnees/les_files_de_priorite.html" >}}   
Écrire le code de la fonction `construction_arbre_huffman` dont la spécification est 
```python
def construction_arbre_huffman(dic_frequences: Dict[str, int]) -> Noeud:
    """
    Construction de l'arbre de Huffman.
    """
```
et l'algorithme (cf. Cormen, *Algorithmes*)
<img src="/terminales-nsi/chap-9/chap-9-4-1.png" alt="" width="70%" />

{{% note warning %}}
Cet algorithm est un exemple d'**algorithme glouton** dans lequel on prend la décision qui semble la meilleure à un instant donné.
{{% /note %}}

17. Écrire une fonction nommée `codes_huffman_parcours` dont la spécification est :
```python
def codes_huffman_parcours(a: Noeud, dic: Dict[str, str], code: str) -> None:
    """
    Parcours de l'arbre et construction des codes et du dictionnaire passé en argument. Les lettres constituent les valeurs et les codes les clés.

    Algorithme récursif.
    """
```

18. Écrire une fonction nommée `encodage` dont la spécification est :
```python
def encodage(message: str, codes: Dict[str, str]) -> str:
    """
    Retourne la chaîne de bits produite par le codage de Huffman pour la chaîne message.
    """
```

19. Écrire une fonction nommée `decodage` dont la spécification est :
```python
def decodage(message_compresse: str, codes: Dict[str, str]) -> str:
    """
    Retourne le message non compressé à partir du codage de Huffman. 
    """
```

{{% solution "Corrigé" %}}
{{% remote "Code Python" "https://repl.it/@dlatreyte/huffman" %}}
{{% /solution %}}

