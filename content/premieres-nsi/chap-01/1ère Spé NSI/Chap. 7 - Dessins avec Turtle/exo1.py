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
    """ Fonction principale qui initialise toutes les
    variables et appelle toutes les autres. """
    tortue_1 = turtle.Turtle()
    tortue_2 = turtle.Turtle()
    longueur = 300
    largeur = 200
    trace_rectangle(tortue_1, longueur, largeur)
    trace_rectangle(tortue_2, longueur // 3, largeur // 3)

    turtle.exitonclick()  # Empêche la fenêtre de se fermer automatiquement à la fin du tracé

main()