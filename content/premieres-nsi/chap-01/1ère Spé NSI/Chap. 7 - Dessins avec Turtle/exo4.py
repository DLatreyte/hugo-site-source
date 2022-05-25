import turtle
import random

def main():
    """ Fonction principale du programme. """
    nbre_points = 200
    
    rayon_min = 5
    rayon_max = 25
    
    x_min = -200
    x_max = 200
    y_min = -200
    y_max = 200
    
    window = turtle.Screen()
    window.setup(2 * x_max + 50, 2 * y_max + 50)
    window.bgcolor("white")
    window.colormode(255)  # gestion de la couleur de la tortue
    
    tortue = turtle.Turtle()
    tortue.speed(0)
    
    for i in range(nbre_points):
        x = random.randint(x_min, x_max)
        y = random.randint(y_min, y_max)
        rayon = random.randint(rayon_min, rayon_max)
        rouge = random.randint(0, 255)
        vert = random.randint(0, 255)
        bleu = random.randint(0, 255)
        
        tortue.penup()
        tortue.setposition(x, y)
        tortue.pendown()
        tortue.pencolor(rouge, vert, bleu)
        tortue.dot(rayon)
        
    window.exitonclick()

main()
        