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
    print('loading saved assets...start')
    
    global __data_columns
    global __directors
    global __actors
    global __genres
    global __model
    
    with open("../model/columns.json", 'r') as f:
        __data_columns = json.load(f)['data_columns']
        __directors = __data_columns[23:414]
        __actors = __data_columns[414:]
        __genres = __data_columns[3:23]
        
    with open("../model/flop_predictor.pickle", 'rb') as f:
        __model = pickle.load(f)
        
    
    print('loading saved assets...done')
        
    
def get_director_names():
    return __directors    
def get_actor_names():
    return __actors    
def get_genre_names():
    return __genres


if __name__ == '__main__':
    load_saved_assets()
    
    
    print(get_estimated_boxoffice(180, 8.8, 1e6, 'tom cruise', 'steven Spielberg d', 'sport'))
    print(get_estimated_boxoffice(100, 2.8, 1e8, 'meg ryan', 'steven Spielberg d', 'action'))
    print(get_estimated_boxoffice(190, 6.8, 5e9, 'bill murray', 'david lynch d', 'sport'))
    print(get_estimated_boxoffice(180, 8.8, 1e6, 'Ted Danson', 'woody allen d', 'Western'))
    
    
    
    
    
    
    
    
    