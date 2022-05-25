import numpy as np
import matplotlib.pyplot as plt


def affichage(x, y, labels):
    """
    Affichage des courbes.
    
    Paramètres
    ----------
    x : array
        Tableau des abscisses
    y : tuple(arrays)
        Différentes ordonnées
    labels: tuple
        Liste des étiquettes
    
    Retour
    ------
    res : None
    """
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_title("Différentes compléxités")
    ax.grid()
    for i in range(len(y)):
        ax.plot(x, y[i], label=labels[i])
    ax.legend()
    fig.savefig("complexites_sans_exponentielle.png")
    fig.show()

x = np.linspace(1, 10, 100)
y1 = x                 # O(N)
y2 = np.log2(x)        # O(log N)

y3 = np.zeros(len(x))  # O(N log N)
for i in range(len(x)):
    y3[i] = y1[i] * y2[i]
    
y4 = y1 * y1           # O(N^2)
y5 = np.exp(y1)        # O(e^^N)

affichage(x,
          (y1, y2, y3, y4),
          ("O(N)", "O(log N)", "O(N log N)", "O(N^2)"))
