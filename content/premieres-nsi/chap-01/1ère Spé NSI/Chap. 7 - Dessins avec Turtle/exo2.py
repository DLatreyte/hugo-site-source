import turtle

def trace_rectangle(tortue: "Turtle", longueur: int, largeur: int) -> None:
    """
    Dessine à l'écran à l'aide de la tortue passée en argument
    un rectangle de longueur et largeurs passées en argument.
    Le dessin est effectué à partir de la position de la tortue
    lorsque la fonction est appelée.
    """
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)


def main():
    """ Fonction principale qui appelle toutes les autres. """
    tortue_1 = turtle.Turtle()
    tortue_1.shape("turtle")
    tortue_1.color("aquamarine4")
    longueur = 200
    largeur = 200
    nbre_carres = 3
    angle_entre_carres = 15
    for i in range(nbre_carres):
        trace_rectangle(tortue_1, longueur, largeur)
        tortue_1.left(angle_entre_carres * (i + 1))

    turtle.exitonclick()  # Empêche la fenêtre de se fermer automatiquement à la fin du tracé

main()
