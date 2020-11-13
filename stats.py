# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 16:58:32 2020

@author: simon
"""

import pandas as pd

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