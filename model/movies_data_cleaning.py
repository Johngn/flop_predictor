#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 11:48:29 2020

@author: johngillan
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

all_movies = pd.read_csv('./data/IMDbmovies.csv')

all_movies[['budget_currency','budget']] = all_movies.budget.str.split(expand=True)
all_movies[['income_currency','boxoffice']] = all_movies.worlwide_gross_income.str.split(expand=True)

all_movies.budget = pd.to_numeric(all_movies['budget'])
all_movies.boxoffice = pd.to_numeric(all_movies['boxoffice'])

movies = all_movies[all_movies.budget_currency == "$"]

movies = movies.drop(['imdb_title_id','year','budget_currency','title','income_currency','votes','reviews_from_critics','description','country','usa_gross_income','worlwide_gross_income','reviews_from_users','language','reviews_from_users','original_title','usa_gross_income','date_published','writer','production_company','imdb_title_id'], axis='columns')
movies = movies.dropna()

# %%
all_actors_lists = []
all_actors = []
for i in movies.actors:
    all_actors_lists.append(i.split(', '))
    for j in i.split(', '):
        all_actors.append(j)
        
all_actors_valuecounts = pd.DataFrame(all_actors)[0].value_counts()
# print(np.count_nonzero(all_actors_valuecounts < 10))

unpopular_actors = all_actors_valuecounts[all_actors_valuecounts < 10]
unpopular_actors_names = np.array(unpopular_actors.keys())
# remove actors who have appeared in less than 10 films
for x in unpopular_actors_names:
    for i in all_actors_lists:
        if x in i:
            i.remove(x)
            
movies.actors = all_actors_lists

''' actor encoding - takes some time because so many need to be removed '''
movies = movies.drop('actors', 1).join(movies.actors.str.join('|').str.get_dummies())

# %%
all_directors_lists = []
all_directors = []
for i in movies.director:
    all_directors_lists.append(i.split(', '))
    
    for j in i.split(', '):
        all_directors.append(j + " D")
        
for i in all_directors_lists:
    i[0] = i[0] + ' D'
    if len(i) > 1:
        i[1] = i[1] + ' D'
        
all_directors_valuecounts = pd.DataFrame(all_directors)[0].value_counts()
# print(np.count_nonzero(all_directors_valuecounts < 3))

unpopular_directors = all_directors_valuecounts[all_directors_valuecounts < 3]
unpopular_directors_names = np.array(unpopular_directors.keys())
# remove directors who have directed less than 3 films
for x in unpopular_directors_names:
    for i in all_directors_lists:
        if x in i:
            i.remove(x)
            
movies.director = all_directors_lists

''' director encoding '''
movies = movies.drop('director', 1).join(movies.director.str.join('|').str.get_dummies())

# %%
# convert each value in genre column to list
movies.genre = movies.genre.apply(lambda x: x.split(', '))
# one-hot encoding for genres
movies = movies.drop('genre', 1).join(movies.genre.str.join('|').str.get_dummies())

# %%
movies.to_csv('./data/movies_clean.csv', index=False)





















