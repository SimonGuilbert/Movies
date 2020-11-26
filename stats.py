# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:58:32 2020

@author: simon
"""

import pandas as pd
import matplotlib.pyplot as plt

ratings = pd.read_csv("ratings.csv")
series = {}

effectifs = ratings["movieId"].value_counts()

#On ne prend que les films qui ont plus de 199 notes
selection = effectifs[effectifs.values>199]

merged = pd.merge(ratings, selection, left_on='movieId', right_on=selection.index)

for movieId in selection.index:
    series[movieId] = merged[merged["movieId"] == movieId]["rating"].values
    # Si jamais il faut que toutes les séries aient le même nombre de valeurs :
    # series[movieId] = merged[merged["movieId"] == movieId]["rating"].head(200).values
    
print(series[1198])

def moyenne_mobile(L, n):
    S=[0]
    moy=[]
    for i, x in enumerate(L,1):
        S.append(S[i-1] + x)
        if i>=n:
            m= (S[i]-S[i-n])/n
            moy.append(m)
    return moy

#Partie affichage des moyennes mobiles pour un film
avis=series[1198]
moyennes_mobiles=moyenne_mobile(series[1198],10)
plt.plot(avis, color='blue')
plt.plot(moyennes_mobiles, color='red')
plt.legend(['avis','moyennes mobiles'])
plt.grid()
plt.title("movieId 1198")
plt.show()
