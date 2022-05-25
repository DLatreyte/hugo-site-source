import turtle
import random

def trace_carre(tortue: "Turtle", largeur: int) -> None:
    """
    Trace un carré de largeur donnée dont l'orientation dépend
    de l'orientation de la tortue.
    À l'issue du tracé, la tortue retrouve sa direction intiale.
    """
    for i in range(4):
        tortue.forward(largeur)
        tortue.left(90)
        
def main():
    """ Fonction principale. """
    tortue = turtle.Turtle()
    tortue.speed(0)
    
    nbre_carres = 200
    
    largeur_min = 5
    largeur_max = 25
    
    angle_min = 0
    angle_max = 360
    
    x_min = -200
    x_max = 200
    y_min = -200
    y_max = 200

    for i in range(nbre_carres):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        largeur = random.randint(largeur_min, largeur_max)
        angle = random.randint(angle_min, angle_max)
        
        tortue.penup()
        tortue.setposition(x, y)
        tortue.setheading(angle)
        tortue.pendown()
        trace_carre(tortue, largeur)
        
    turtle.exitonclick()


main()