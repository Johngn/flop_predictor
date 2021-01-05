#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 14:46:47 2021

@author: johngillan
"""

import pickle
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
# %%
movies = pd.read_csv('./data/movies_clean.csv')

X = movies.drop(['year','new_box_office'], axis='columns')
y = movies.new_box_office

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=10)
# %%
model = LinearRegression()
model.fit(X_train, y_train)

print("Model score is: " + str(np.round(model.score(X_test, y_test), 2)))

predicted_boxoffice = model.predict(X)
mean_absolute_error(y, predicted_boxoffice)

def predict_boxoffice(duration, avg_vote, budget, genre, director, actor):
    x = np.zeros(len(X.columns))
    
    if genre in X.columns:
        genre_index = np.where(X.columns == genre)[0][0]    
        x[genre_index] = 1
    
    if director in X.columns:
        director_index = np.where(X.columns == director)[0][0]    
        x[director_index] = 1
    
    if actor in X.columns:
        actor_index = np.where(X.columns == actor)[0][0]    
        x[actor_index] = 1
        
    x[0] = duration
    x[1] = avg_vote
    x[2] = budget
    
    return model.predict([x])[0]

print(predict_boxoffice(80, 9.9, 1e7, 'Sport', 'James Cameron D', 'Meg Ryan')/1e6)
# %%
cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)

score = cross_val_score(LinearRegression(), X, y, cv=cv)
# %%
def find_best_model_using_gridsearchcv(X, y):
    algos = {
        'linear_regression' : {
            'model': LinearRegression(),
            'params': {
                'normalize': [True, False]
                }
            },
        'lasso' : {
            'model': Lasso(),
            'params': {                
                'alpha': [1, 2],
                'selection': ['random', 'cyclic']
                }
            },
        'decision_tree' : {
            'model': DecisionTreeRegressor(),
            'params': {                
                'criterion': ['mse', 'friedman_mso'],
                'splitter': ['best', 'random']
                }
            },
        }
    
    scores = []
    
    cv = ShuffleSplit(n_splits=5, test_size=0.2, random_state=0)
    
    for algo_name, config in algos.items():
        gs = GridSearchCV(config['model'], config['params'], cv=cv, return_train_score=False)
        gs.fit(X, y)
        
        scores.append({
            'model': algo_name,
            'best_score': gs.best_score_,
            'best_params': gs.best_params_
        })
        
    return pd.DataFrame(scores, columns=['model', 'best_score', 'best_params'])
    
test = find_best_model_using_gridsearchcv(X, y)
''' Seems that DecisionTreeRegressor with criterion: mse and splitter: best gives the best score '''
# %%
def predict_boxoffice(duration, avg_vote, metascore, budget, director, actor, genre):
    x = np.zeros(len(X.columns))
    
    if director in X.columns:
        director_index = np.where(X.columns == director)[0][0]    
        x[director_index] = 1
    
    
    if actor in X.columns:
        actor_index = np.where(X.columns == actor)[0][0]    
        x[actor_index] = 1
    
    
    if genre in X.columns:
        genre_index = np.where(X.columns == genre)[0][0]    
        x[genre_index] = 1
        
    x[0] = duration
    x[1] = avg_vote
    x[2] = metascore
    x[3] = budget
    print(x)
    return model.predict([x])[0]

print(predict_boxoffice(150, 9.9, 80, 3e8, 'Clint Eastwood', 'Tom', 'Horror')/1e6)
# %%
with open('./model/flop_predictor.pickle', 'wb') as f:
    pickle.dump(model, f)
    
import json
columns = {
    'data_columns': [col.lower() for col in X.columns]
    }
with open('./model/columns.json', 'w') as f:
    f.write(json.dumps(columns))
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    