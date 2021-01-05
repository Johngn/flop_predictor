import json
import pickle
import numpy as np

__model = None
__data_columns = None
__directors = None
__actors = None
__genres = None

def get_estimated_boxoffice(duration, avg_vote, budget, actor, director, genre):
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
        
    x = np.zeros(len(__data_columns))
    
    x[0] = duration
    x[1] = avg_vote
    x[2] = metascore
    x[3] = budget
    
    return round(__model.predict([x])[0], 2)

def load_saved_assets():
    print('loading saved assets...start')
    
    global __data_columns
    global __directors
    global __actors
    global __genres
    global __model
    
    with open("../model/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __directors = __data_columns[1451:-21]
        __actors = __data_columns[4:1450]
        __genres = __data_columns[-21:]
        
    with open("../model/flop_predictor.pickle", 'rb') as f:
        __model = pickle.load(f)
        
    
    print('loading saved assets...done')
        
    

def get_director_names():
    return __directors


if __name__ == '__main__':
    load_saved_assets()
    
    
    print(get_estimated_boxoffice(180, 8.8, 100, 1e7, 'actor', 'director', 'genre'))
    print(get_estimated_boxoffice(100, 2.8, 50, 1e8, 'actor', 'director', 'genre'))
    print(get_estimated_boxoffice(150, 6.8, 3, 5e7, 'actor', 'director', 'genre'))
    print(get_estimated_boxoffice(180, 8.8, 69, 1e6, 'actor', 'director', 'genre'))
    
    
    
    
    
    
    
    
    