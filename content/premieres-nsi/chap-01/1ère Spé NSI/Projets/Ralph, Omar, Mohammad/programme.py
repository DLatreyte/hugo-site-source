import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#Fichier d'études des Jeux Olympiques dans le binks.

olymp = pd.read_csv("athlete_events.csv", sep = ";") #Charge le fichier sous le nom olympics.


"""
#1ère question: Quelle a été l'évolution du nombre d'athlètes aux JO d'été depuis leur création ?
"""

olymp_name_total = olymp.loc[olymp["Season"]!="NA",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_name_total) #Vérification

#Sur le même graphique: quelle a été l'évolution du nombre d'athlètes aux JO d'hiver depuis leur création ?

olymp_name_winter = olymp.loc[olymp["Season"]=="Winter",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_name_winter) #Vérification
#Affichage du graphique.
dataframe = pd.concat([olymp_name_total, olymp_name_winter], axis=1)
dataframe = dataframe.plot()
plt.show()





"""
#2ème question: Quelle a été l'évolution du nombre de femmes aux JO d'été depuis leur création ?
"""
olymp_femme_total = olymp.loc[olymp["Sex"]=="F",["Name", "Year"]].pivot_table(index="Year", aggfunc=len).fillna(0)
print(olymp_femme_total) #Vérification

olymp_femme_total.plot()
plt.show()





"""
#3ème question: Quelle a été l'évolution du nombre de disciplines aux JO d'été depuis leur création ?
"""
olymp_discipline_total = olymp.loc[olymp["Season"]=="Summer",["Year", "Sport"]].pivot_table(index="Year", aggfunc="nunique").fillna(0)
olymp_discipline_total = olymp_discipline_total.drop(columns="Year") #Suppression de la colonne "Year" qui est une constante.
print(olymp_discipline_total) #Vérification
olymp_discipline_total.plot(style="bo", markersize="3")
plt.show()





"""
#4ème question: Quelle est le nombre de médailles gagnées par chaque pays au total des années ?
"""
olymp_medal = olymp.loc[olymp["Year"]!="NA",["Team", "Medal"]].pivot_table(index="Team", columns="Medal", aggfunc=len).fillna(0)
olymp_medal = olymp_medal.sort_values(by=["Gold"], ascending=False)
print(olymp_medal)


#annee 2012 (avec un ratio):
olymp_medal = olymp.loc[olymp["Year"]==2012,["Team", "Medal"]].pivot_table(index="Team", columns="Medal", aggfunc=len).fillna(0)
olymp_medal = olymp_medal.sort_values(by=["Gold"], ascending=False)
olymp_name = olymp.loc[olymp["Year"]==2012,["Team", "Name"]].pivot_table(index="Team", aggfunc="nunique").fillna(0).loc[:,["Name"]]
olymp_name = olymp_name.sort_values(by=["Name"], ascending=True)
dataframe = pd.concat([olymp_medal, olymp_name], axis=1).fillna(0)
dataframe = dataframe.div(dataframe["Name"], axis=0).fillna(0).sort_values(by="Gold") 
print(dataframe)




