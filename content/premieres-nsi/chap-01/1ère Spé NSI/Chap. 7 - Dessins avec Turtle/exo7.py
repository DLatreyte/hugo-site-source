"""
Tracés de carrés concentriques.
"""

import turtle
import math as m
    
def trace_carres(tortue: "Turtle", largeur: int,
                 largeur_min: int, dl: int) -> None:
    """
    Dessine à l'écran une série de carrés dont les largeurs
    sont de plus en plus petites.
    Le processus itératif cesse dès que la largeur à tracer est 
    inférieure à la largeurw minimale choisie.
    Tous les carrés sont espacés de la longueur dl.
    """
    while not(largeur < largeur_min):
        tortue.penup()
        tortue.home()
        tortue.goto(-largeur // 2, -largeur // 2)  # Coin inférieur gauche
        tortue.pendown()
        trace_carre(tortue, largeur)
        
        largeur -= dl
        
def trace_carre(tortue: "Turtle", largeur: int) -> None:
    """
    Dessine un carré de côté de largeur donnée.
    """
    for i in range(4):
        tortue.forward(largeur)
        tortue.left(90)
    
    
def main():
    """
    Fonction principale, appelle toutes les autres fonctions.
    """
    width = 700
    height = 600
    
    largeur = 300
    largeur_min = 10
    delta = 15

    fenetre = turtle.Screen()
    fenetre.setup(width, height)
    fenetre.bgcolor("black")

    tortue = turtle.Turtle()
    tortue.hideturtle()
    tortue.color("yellow")
    tortue.speed(0)
    tortue.pensize("3")
    
    trace_carres(tortue, largeur, largeur_min, delta)

    window.exitonclick()

main()

