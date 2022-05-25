import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv('athlete_events.csv', delimiter=';')  
data.head()



# 1. Quelle a ete l'evoltion du nombre d'athletes dans les jeux olympics d'ete depuis leur creation?
#Sur le meme graphique quelle a ete l'evolution du nombre d'athlete dans les jeux olympics d'hiver depuis leur creation? 

df1 = data.groupby('Year')['Season'].value_counts().unstack()
#unstack= il y a plusieurs indexs, on veut donc y acceder un par un donc on les 'unstacks'.
years = df1.index.tolist()
#tolist()= Retourne une liste de valeur.
athletes = np.transpose(np.asarray(df1))
#Pour utiliser les listes de valeurs de la colonnes de dataframe on doit
#utiliser array a la place de pandas series(np.asarray) et puis cree une rangee de la colonne (np.transpose)
fig = plt.figure(figsize=(18, 16))
#Change les dimension de la figure
p1 = plt.bar(years,athletes[0])
#faire un plot de bar = plt.bar(x(position abscisse), hauteur)
p2 = plt.bar(years,athletes[1])
#faire un plot de bar = plt.bar(x(position abscisse), hauteur)
plt.ylabel('Number of atheletes')
# Nommer l'axe des ordonnees
plt.xticks(years, years, rotation=90)
# afficher la Valeurs des bars en abscisse et faire les bars verticale
plt.title('The evolution of the number of athletes at the Summer Olympic Games since their creation')
#Ajoute un titre au graphique
plt.legend((p1[0], p2[0]), ('Summer', 'Winter'))
#Modifie la legende du graphique
plt.show()


# 2.  Comment le nombre de femme dans les jeux olympics d'ete a changer depuis leur creation?

df2 = data.groupby(['Year', 'Season', 'Sex']).size()
#size()= Nombre de chaque rangee dans chaque group
df2 = df2.reset_index()
#creation de dataframe avec plusieur indice donc pour avoir acces aux indices par leur noms on reset l'indice
#et on obtient des dataframes avec des noms de colonne qui correspond aux indices
df2 = df2.loc[df2['Season']=='Summer'].loc[df2['Sex']=='F']
#Cela retourne des rangees ou colonnes de df, on cherchait a ce que les rangee contiennent 'Season' == 'Summer'
years = np.asarray(df2['Year'])
#Pour utiliser les listes de valeurs de la colonnes de dataframe on doit
#utiliser array a la place de pandas series(np.asarray)
athletes = np.asarray(df2[0])
#Pour utiliser les listes de valeurs de la coloumn de dataframe on doit
#utiliser array a la place de pandas series(np.asarray)
fig = plt.figure(figsize=(18, 16))
#Change les dimension de la figure
p1 = plt.bar(years,athletes)
#faire un plot de bar = plt.bar(x(position abscisse), hauteur)
plt.ylabel('Number of women')
# Nommer l'axe des ordonnees
plt.xticks(years, years, rotation=90)
# afficher la Valeurs des bars en abscisse et faire les bars verticale
plt.title('The evolution of number of women at the Summer Olympics changed since their creation')
#Ajoute un titre au graphique
plt.show()


# Comment le nombre de discipline dans les jeux olympic d'ete a changer depuis leur creation?

df3 = data.loc[data['Season']=='Summer']
#Cela retourne des rangees ou colonnes de df, on cherchait a ce que les rangee contiennent 'Season' == 'Summer'
df3 = df3.groupby(['Year', 'Season', 'Sport']).Sport.nunique()
#Serie.nunique() = Retourne le nombre d'elements unique, Na non comptee (elements repetee 1 fois)
df3 = df3.groupby(['Year', 'Season']).size()
#size()= Nombre de chaque rangee dans chaque group
df3 = df3.reset_index()
#creation de dataframe avec plusieur indice donc pour avoir acces aux indices par leur noms on reset l'indice
#et on obtient des dataframes avec des noms de colonne qui correspond aux indices
years = np.asarray(df3['Year'])
#Pour utiliser les listes de valeurs de la colonne de dataframe on doit
#utiliser array a la place de pandas series(np.asarray)
disciplines = np.asarray(df3['Sport'])
#Pour utiliser les listes de valeurs de la colonne de dataframe on doit
#utiliser array a la place de pandas series(np.asarray)
fig = plt.figure(figsize=(18, 16))
#Change les dimension de la figure
p1 = plt.bar(years,disciplines)
#faire un plot de bar = plt.bar(x(position abscisse), hauteur)
plt.ylabel('Number of disciplines')
# Nommer l'axe des ordonnees
plt.xticks(years, years, rotation=90)
# afficher la Valeurs des bars en abscisse et faire les bars verticale
plt.title('The evolution of number of disciplines at the Summer Olympics changed since their creation')
#Ajoute un titre au graphique
plt.show()

