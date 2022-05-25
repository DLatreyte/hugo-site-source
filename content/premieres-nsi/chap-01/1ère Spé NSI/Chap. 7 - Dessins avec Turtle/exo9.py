import turtle


def rectangle(tortue: "Turtle", longueur: int, largeur: int) -> None:
    """
    Trace un rectangle de longueur et largeur passées en argument grâce à la
    tortue (elle-même passée en argument).
    Les position et direction de la tortue ne sont pas modifiées.
    À l'issue du tracé la tortue se retrouve au point de départ, avec
    la même direction.
    """
    for i in range(2):
        tortue.forward(longueur)
        tortue.left(90)
        tortue.forward(largeur)
        tortue.left(90)
        

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
    rectangle(tortue, longueur, largeur)
        
        
def main():
    """
    Fonction principale. Initialisation des variables et appel des
    autres fonctions.
    """
    # Paramètres de l'animation
    largeur_aire_jeu = 800
    longueur_aire_jeu = 800
    largeur_carre = 100
    x_rect = -(longueur_aire_jeu - largeur_carre)
    y_rect = -largeur_carre //2
    pas = 10  # de combien augment l'abscisse entre deux animations
    
    # Création de la fenetre pour l'animation
    fenetre = turtle.Screen()
    fenetre.setup(longueur_aire_jeu + 50, largeur_aire_jeu + 50)
    fenetre.bgcolor("black")
    
    # Création de la tortue pour tracer les limites de l'animation
    tortue1 = turtle.Turtle()
    tortue1.speed(0)
    tortue1.color("white")
    tortue1.hideturtle()
    
    # Tracé des limites
    trace_rectangle(tortue1, -longueur_aire_jeu // 2,
                    -largeur_aire_jeu // 2, longueur_aire_jeu,
                    largeur_aire_jeu)
    
    # Création de la tortue pour l'animation
    tortue2 = turtle.Turtle()
    tortue2.speed(0)
    tortue2.color("white")
    tortue2.hideturtle()
    
    # On prend en main le rafraichissement
#     fenetre.tracer(0)
    
    # Animation
    while x_rect <= longueur_aire_jeu // 2:
        tortue2.clear()
        trace_rectangle(tortue2, x_rect, y_rect, largeur_carre, largeur_carre)
#         fenetre.update()  # affichage()
        x_rect += pas
        
        
    # Ferme la fenêtre avec un click sur l'espace de jeu
    turtle.exitonclick()
    
main()
    
        
