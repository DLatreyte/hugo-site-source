import turtle


def main():
    nbre_cercles = 30
    angle_entre_cercles = int(360 / nbre_cercles)
    rayon_cercles = 100
    
    tortue = turtle.Turtle()
    tortue.speed(0)
    
    for i in range(0, nbre_cercles):
        turtle.circle(rayon_cercles)
        turtle.setheading(angle_entre_cercles * (i + 1))


main()
    