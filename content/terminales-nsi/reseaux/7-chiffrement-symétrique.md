---
title: "Réalisation d'un chiffrement symétrique"
subtitle: ""
author: ""
type: ""
date: 2022-04-15T06:36:15+04:00
draft: false
toc: true
tags: []
categories: []
image: ""
solution_est_visible: true
auto_numbering: true
---

> L'objectif de ce document est d'illustrer un exemple de chiffrement symétrique, basique mais très utilisé dans les débuts de l'informatique car son implémentation est très simple..

## Principe de la méthode

1. Rechercher le codage binaire du mot `mon papa`. C'est le message à chiffrer.
{{% solution "Réponse" %}}

`01101101 01101111 01101110 00100000 01110000 01100001 01110000 01100001`

{{% /solution %}}

**Remarque :** utiliser le site [https://www.rapidtables.com/convert/number/ascii-to-binary.html](https://www.rapidtables.com/convert/number/ascii-to-binary.html) pour obtenir les codes des caractères.

{{% note tip %}}

#### Rappel

Pour déterminer le codage binaire d'un caractère il faut :

- Rechercher son code sous forme décimale ;
- Déterminer l'écriture binaire du code décimal.

{{% /note %}}

2. On choisit le mot `bar` comme clé de chiffrement. Rechercher le codage binaire de ce mot.
{{% solution "Réponse" %}}

`01100010 01100001 01110010`

{{% /solution %}}

3. Le chiffrement est effectué à l'aide d'une opération logique : on effectue un **XOR bit à bit** entre les bits du message à chiffrer et ceux de la clé.
Rappeler la table de vérité du XOR (OU exclusif).
{{% solution "Réponse" %}}

<center>

| B1 | B2 | B1 XOR B2 |
| :---: | :---: | :---: |
| True | True | False |
| True | False | True |
| False | True | True |
| False | False | False |

</center>

{{% /solution %}}

4. La clé est plus courte que le message. La dupliquer autant de fois que nécessaire (si la taille du message n'est pas un multiple entier de celle de la clé, ne prendre que quelques bits de cette dernière, en commençant par la gauche).
{{% solution "Réponse" %}}

`01100010 01100001 01110010 01100010 01100001 01110010 01100010 01100001`

{{% /solution %}}

5. Réaliser l'opération `message XOR clé`.
{{% solution "Réponse" %}}

| | |
| :----: | :----: |
|  | 01101101 01101111 01101110 00100000 01110000 01100001 01110000 01100001 |
| XOR | |
|  | 01100010 01100001 01110010 01100010 01100001 01110010 01100010 01100001 |
| | |
|  | 00001111 00001110 00011100 01000010 00010001 00010011 00010010 00000000 |

{{% /solution %}}

6. Afin de déchiffrer le message, on applique la même opération au message chiffré. Vérifier que l'on obtient bien le codage du message initial.
{{% solution "Réponse" %}}

| | |
| :----: | :----: |
|  | 00001111 00001110 00011100 01000010 00010001 00010011 00010010 00000000 |
| XOR | |
|  | 01100010 01100001 01110010 01100010 01100001 01110010 01100010 01100001 |
| | |
|  | 01101101 01101111 01101110 00100000 01110000 01100001 01110000 01100001 |

On obtient bien le même codage.
{{% /solution %}}

## Implémentation en Python

7. Définir la fonction `codage` dont la spécification est

```python
def codage(a: int) -> str:
    """
    Détermine l'écriture binaire de l'entier
    a passé en argument et la retourne sous
    forme d'une chaîne de 8 caractères 0 ou 1.

    Hypothèse : les caractères sont codés sur un octet.
    """
```

{{% solution "Réponse" %}}

```python
def codage(a: int) -> str:
    """
    Détermine l'écriture binaire de l'entier
    a passé en argument et la retourne sous
    forme d'une chaîne de 8 caractères 0 ou 1.

    Hypothèse : les caractères sont codés sur un octet.
    """
    inv_chaine_bin = ""  # Chaîne binaire inversée

    while a != 0:
        inv_chaine_bin += str(a % 2)
        a = a // 2

    octet = 8  # Formation d'octets
    if len(inv_chaine_bin) < octet:
        inv_chaine_bin += "0" * (octet - len(inv_chaine_bin))

    chaine_bin = ""  # Inversion de la chaîne
    for i in range(len(inv_chaine_bin) - 1, -1, -1):
        chaine_bin += inv_chaine_bin[i]

    return chaine_bin
```

{{% /solution %}}

8. Définir la fonction `codage_chaine` dont la spécification est

```python
def codage_chaine(texte: str) -> str:
    """
    Convertit la chaîne de caractères passée
    en argument en une chaîne de caractères
    formés de 0 et de 1.
    Les 0 et 1 constitue le codage binaire 
    de chacun des caractères de la chaîne
    initiale.

    Hypothèse : les caractères sont codés sur un octet.
    """
```

La fonction `codage_chaine` utilise les fonctions `codage` et `ord`.

{{% solution "Réponse" %}}

```python
def codage_chaine(texte: str) -> str:
    """
    Convertit la chaîne de caractères passée
    en argument en une chaîne de caractères
    formés de 0 et de 1.
    Les 0 et 1 constitue le codage binaire 
    de chacun des caractères de la chaîne
    initiale.

    Hypothèse : les caractères sont codés sur un octet.
    """
    rep = ""

    for car in texte:
        valeur = ord(car)  # Valeur décimale
        chaine_bin = codage(valeur)
        rep += chaine_bin

    return rep
```

{{% /solution %}}

9. Vérifier que la fonction `codage_chaine` retourne bien le même codage que celui établi à la question 1. dans la partie principale du programme.

10. Obtenir le code de la clé utilisée à la question 2.
{{% solution "Réponses aux deux questions précédentes" %}}

```python
if __name__ == "__main__":
    #texte_a_chiffrer = input("Texte à chiffrer : ")
    texte_a_chiffrer = "papa"
    texte_code = codage_chaine(texte_a_chiffrer)
    print(f"Code du texte :\n{texte_code}")

    #cle = input("Clé de chiffrement : ")
    cle = "bar"
    cle_code = codage_chaine(cle)
    print(f"Code de la clé :\n{cle_code}")
```

{{% /solution %}}

11. Définir la fonction `ajustement_cle` dont la spécification est

```python
def ajustement_cle(code_cle: str, longueur_chaine: int) -> str:
    """
    Ajuste la longueur du code de la clé à celle du
    code de la chaîne à chiffrer, de longueur 
    longueur_chaine.
    """
```

{{% solution "Réponse" %}}

```python
def ajustement_cle(code_cle: str, longueur_chaine: int) -> str:
    """
    Ajuste la longueur du code de la clé à celle du
    code de la chaîne à chiffrer, de longueur 
    longueur_chaine.
    """
    if len(code_cle) >= longueur_chaine:
        rep = code_cle[:longueur_chaine]
    else:
        rapport = longueur_chaine // len(code_cle)
        rep = code_cle * rapport
        rep += code_cle[:longueur_chaine - len(rep)]

    return rep
```

{{% /solution %}}

12. Définir la fonction `chiffrement` dont la spécification est

```python
def chiffrement(chaine: str, cle: str) -> str:
    """
    Réalise la chiffrement de chaine à l'aide de
    la clé.
    Méthode : chaine xor cle
    """
```

La fonction `chiffrement` utilise la fonction `ajustement_cle`.

**Remarque :** l'opérateur, en Python, permettant de réaliser le `xor` est `^` *à la condition que les opérandes soient des entiers*.

{{% solution "Réponse" %}}

```python
def chiffrement(chaine: str, cle: str) -> str:
    """
    Réalise la chiffrement de chaine à l'aide de
    clé.
    Méthode : chaine xor cle
    """
    cle = ajustement_cle(cle, len(chaine))

    code_texte_chiffre = ""
    for i in range(len(chaine)):
        valeur = int(chaine[i]) ^ int(cle[i])
        code_texte_chiffre += str(valeur)
    return code_texte_chiffre
```

{{% /solution %}}

13. Définir la fonction `decodage` dont la spécification est

```python
def decodage(car_code: str) -> str:
    """
    Décode le caractère dont le code est passé en
    argument.

    Hypothèse : les caractères sont codés sur un octet
    """
```

{{% solution "Réponse" %}}

```python
def decodage(car_code: str) -> str:
    """
    Décode le caractère dont le code est passé en
    argument.

    Hypothèse : les caractères sont codés sur un octet
    """
    valeur_code = 0
    octet = 8

    for i in range(len(car_code)):
        valeur_code += int(car_code[i]) * 2**(octet - (i + 1))

    return chr(valeur_code)
```

{{% /solution %}}

14. Définir la fonction `decodage_chaine` dont la spécification est

```python
def decodage_chaine(chaine_code: str) -> str:
    """
    Décode la chaine dont le code est passé
    en argument.

    Hypothèse : les caractères sont codés sur un octet
    """
```

15. Définir la fonction `dechiffrement` dont la spécification est

```python
def dechiffrement(code_chaine_chiffree: str, cle: str) -> str:
    """
    Réalise la déchiffrement de chaine (codée) à l'aide de
    la clé.
    Méthode : chaine xor cle
    """
```
