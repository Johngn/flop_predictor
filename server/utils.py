import json
import pickle
import numpy as np

__model = None
__data_columns = None
__directors = None
__actors = None
__genres = None

def get_estimated_boxoffice(duration, avg_vote, budget, actor, director, genre):        
    x = np.zeros(len(__data_columns))

    try:
        actor_index = __data_columns.index(actor.lower())
    except:
        actor_index = -1
        
    try:
        director_index = __data_columns.index(director.lower())
    except:
        director_index = -1
        
    try:
        genre_index = __data_columns.index(genre.lower())
    except:
        genre_index = -1
    
    x[0] = duration
    x[1] = avg_vote
    x[2] = budget
    x[actor_index] = 1
    x[director_index] = 1
    x[genre_index] = 1
    
    return round(__model.predict([x])[0], 2)

def load_saved_assets():    
    global __data_columns
    global __directors
    global __actors
    global __genres
    global __model
    
    with open("./columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __directors = __data_columns[23:414]
        __actors = __data_columns[414:]
        __genres = __data_columns[3:23]
        
    with open("./flop_predictor.pickle", 'rb') as f:
        __model = pickle.load(f)
        
    
def get_director_names():
    return __directors

def get_actor_names():
    return __actors

def get_genre_names():
    return __genres


if __name__ == '__main__':
    load_saved_assets()
