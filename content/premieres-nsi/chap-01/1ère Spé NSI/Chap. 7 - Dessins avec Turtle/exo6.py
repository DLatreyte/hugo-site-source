import turtle

def main():
    nbre_colonnes = 15
    nbre_rangees = 15
    rayon = 10
    dx = 30  # espacement horizontal entre points
    dy = 30  # espacement vertical entre points
    
    tortue = turtle.Turtle()
    tortue.speed(0)
    
    for i in range(nbre_rangees):
        for j in range(nbre_colonnes):
            tortue.penup()
            tortue.setposition(i * dx - (nbre_rangees * dx) // 2,
                               j * dy - (nbre_colonnes * dy) // 2)
            tortue.pendown()
            tortue.dot(rayon)
    
    turtle.exitonclick()
    
main()

            