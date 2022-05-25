"""
Tracés de cercles de différentes tailles.
"""

import turtle
import random

def draw_circles(tortue: "Turtle", r: int,
                 r_min: int, dr: int) -> None:
    """
    Dessine à l'écran une série de cercles dont les rayons sont
    de plus en plus petits.
    Le processus itératif cesse dès que le rayon du cercle à tracer
    est inférieur au rayon minimal choisi.
    """
    while not(r < r_min):
        rouge = random.randint(0, 255)
        vert = random.randint(0, 255)
        bleu = random.randint(0, 155)
        tortue.penup()
        tortue.goto(0, -r)
        tortue.pendown()
        tortue.pencolor(rouge, vert, bleu)
        tortue.circle(r)
        
        r -= dr


def main():
    """
    Fonction principale, appelle toutes les autres fonctions.
    """
    width = 700
    height = 600
    
    radius = 200
    radius_min = 15
    delta_r = 15

    window = turtle.Screen()
    window.setup(width, height)
    window.bgcolor("black")
    window.colormode(255)  # gestion de la couleur de la tortue

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.color("red")
    pen.speed(0)
    pen.pensize("3")
    
    draw_circles(pen, radius, radius_min, delta_r)

    window.exitonclick()

main()

