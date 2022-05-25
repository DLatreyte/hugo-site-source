"""
Mouvement d'une balle contenue dans une boite à deux dimensions.
"""
import turtle
from time import sleep
import random


def trace_rectangle(tortue: "Turtle", x: int, y: int,
                    longueur: int, largeur: int) -> None:
    """
    Déplace la souris à la position (x, y) puis trace un rectangle de
    longueur et largeur passées en argument.
    (x, y) est le coin inférieur gauche du rectangle.
    """
    tortue.penup()
    tortue.goto(x, y)
    tortue.pendown()
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)


def lancement_jeu(fenetre: "Screen", tortue: "Turtle", t: int, t_max: int,
                  largeur: int, hauteur: int, x: int, y: int, vx:int,
                  vy: int, rayon: int) -> None:
    """
    Déplace à l'écran une balle en la conservant dans les limites du
    plateau.
    """
    while t <= t_max:
        if y > (hauteur / 2 - rayon):
            vy = -vy
        elif y < (-hauteur / 2 + rayon):
            vy = -vy
        elif x > (largeur / 2 - rayon):
            vx = -vx
        elif x < (-largeur / 2 + rayon):
            vx = -vx
        x = x + vx
        y = y + vy
        
        rouge = random.randint(0, 255)
        vert = random.randint(0, 255)
        bleu = random.randint(0, 255)
        
        tortue.clear()
        tortue.penup()
        tortue.goto(x, y)
        tortue.pendown()
        tortue.pencolor(rouge, vert, bleu)
        tortue.dot(rayon)
        fenetre.update()
        
        sleep(0.1)

        t = t + 1


def main():
    """ Fonction principale. """
    
    # Paramètres de l'animation
    largeur = 400
    hauteur = 400
    rayon = 30
    x, y = 0, 0
    vx, vy = 20, 15
    date_debut, date_fin = 1, 500
    
    # Création de la fenêtre
    fenetre = turtle.Screen()
    fenetre.setup(largeur + 50, hauteur + 50)
    fenetre.bgcolor("black")
    fenetre.tracer(0)
    
    # Création de la tortue qui trace les limites de l'aire de jeu
    tortue1 = turtle.Turtle()
    tortue1.speed(0)
    tortue1.color("white")
    tortue1.hideturtle()
    turtle.colormode(255)
    
    # Tracé des limites
    trace_rectangle(tortue1, -largeur // 2, -hauteur // 2, largeur, hauteur)

    # Création de la tortue du jeu
    tortue = turtle.Turtle()
    tortue.speed(0)
    tortue.color("yellow")
    tortue.hideturtle()
    tortue.dot(rayon)
    
    # Lancement du jeu
    lancement_jeu(fenetre, tortue, date_debut, date_fin, largeur, hauteur,
                  x, y, vx, vy, rayon)
    
main()
