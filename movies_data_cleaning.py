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

all_movies = pd.read_csv('IMDbmovies.csv')

all_movies[['budget_currency','budget_amount']] = all_movies.budget.str.split(expand=True)
all_movies[['income_currency','income_amount']] = all_movies.worlwide_gross_income.str.split(expand=True)

all_movies.budget_amount = pd.to_numeric(all_movies['budget_amount'])
all_movies.income_amount = pd.to_numeric(all_movies['income_amount'])

movies = all_movies[all_movies.budget_currency == "$"]

movies = movies.dropna()

modern_movies = movies[movies.year > 2000]
# %%
all_genres = []
for i in movies.genre.values:
    split_genres = i.split(',')
    split_genres_stripped = [x.strip() for x in split_genres]
    all_genres += split_genres_stripped
    # print(genres)
    
all_genres = pd.DataFrame(all_genres)

unique_genres = all_genres[0].unique()