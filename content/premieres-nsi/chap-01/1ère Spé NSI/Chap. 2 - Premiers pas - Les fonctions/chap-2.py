def conversion_franc_euro(francs: float) -> str:
    """
    Conversion d'une somme en francs en euros. Le message retourné
    donne les deux valeurs.
    """
    change = 6.55957
    euros = francs / change
    return "{} francs correspondent à {} euros.".format(francs, euros)


def salutation(nom: str, prenom: str, naissance: int) -> str:
    """
    À partir des nom, prénom et date de naissance, retourne un message
    d'accueil indiquant l'âge.
    
    >>> salutation("Dupond", "Patrick", 1961)
    'Bonjour Patrick Dupond, vous avez 58 ans.'
    """
    annee_en_cours = 2019
    message = "Bonjour {0} {1}, vous avez {2} ans.".format(prenom,
                                                           nom,
                                                           annee_en_cours - naissance)
    return message


import random
def age_aleatoire(age_min: int, age_max: int) -> str:
    """
    À partir de deux ages limites, retourne un message contenant
    un age déterminé aléatoirement.
    
    >>> age_aleatoire(20, 100)
    'Votre age est : 85 ans !'
    """
    age = random.randint(age_min, age_max)
    return "Votre age est : {} ans !".format(age)
