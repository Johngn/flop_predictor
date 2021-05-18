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

movies = movies[movies['year'] >= 1980]

cpi = pd.read_csv('./cpi.csv')

cols = cpi.columns[cpi.columns.isin(['Year', 'Avg'])]
cpi = cpi[cols]
cpi = cpi[cpi['Year'] >= 1980]

cpi_2020 = 260.2
factors = [np.round(cpi_2020/item, 3) for i, item in enumerate(cpi.Avg)]
cpi['factors'] = factors


movie_factors = np.zeros(len(movies))
movie_year = movies.year
movie_budget = movies.budget

for i, valuei in enumerate(movie_year):
    for j, valuej in cpi.Year.items():
        if valuei == valuej:
            movie_factors[i] = cpi.factors[j]
            
new_budget = movies.budget*movie_factors
movies['budget'] = new_budget
new_box_office = movies.boxoffice*movie_factors
movies['boxoffice'] = new_box_office

movies = movies.drop(['imdb_title_id','budget_currency','title','income_currency','votes','reviews_from_critics','description','country','usa_gross_income','worlwide_gross_income','reviews_from_users','language','reviews_from_users','original_title','usa_gross_income','date_published','writer','production_company','imdb_title_id'], axis='columns')
movies = movies.dropna()
# %%
# convert each value in genre column to list
movies.genre = movies.genre.apply(lambda x: x.split(', '))

# one-hot encoding for genres
movies = movies.drop('genre', 1).join(movies.genre.str.join('|').str.get_dummies())

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
    
for i, item in enumerate(all_actors_lists):
    if len(item) == 0:
        all_actors_lists[i] = np.nan
        
movies['actors'] = all_actors_lists
movies = movies.dropna()


all_directors_lists = []
all_directors = []
for i in movies.director:
    all_directors_lists.append(i.split(', '))
    
    for j in i.split(', '):
        all_directors.append(j + " ")   # add space to distinguish directors who also act
        
for i in all_directors_lists:
    i[0] = i[0] + ' '                   # add space to distinguish directors who also act
    if len(i) > 1:
        i[1] = i[1] + ' '               # add space to distinguish directors who also act
        
all_directors_valuecounts = pd.DataFrame(all_directors)[0].value_counts()
# print(np.count_nonzero(all_directors_valuecounts < 3))

unpopular_directors = all_directors_valuecounts[all_directors_valuecounts < 5]
unpopular_directors_names = np.array(unpopular_directors.keys())
# remove directors who have directed less than 3 films
for x in unpopular_directors_names:
    for i in all_directors_lists:
        if x in i:
            i.remove(x)

for i, item in enumerate(all_directors_lists):
    if len(item) == 0:
        all_directors_lists[i] = np.nan
        
movies['director'] = all_directors_lists

movies = movies.dropna()
# %%

''' actor encoding - takes some time because so many need to be removed '''
movies = movies.drop('actors', 1).join(movies.actors.str.join('|').str.get_dummies())
''' director encoding '''
movies = movies.drop('director', 1).join(movies.director.str.join('|').str.get_dummies())

# %%
genre_boxoffice = []
genre_score = []
for i in unique_genres:
    genre_boxoffice.append(np.mean(movies[movies[i] == 1].new_budget))
    genre_score.append(np.mean(movies[movies[i] == 1].avg_vote))

genre_boxoffice = np.array(genre_boxoffice)

data = {'genre':  unique_genres,
        'mean': genre_score}

genre_boxoffice_data = pd.DataFrame(data, columns=['genre','mean'])
genre_score_data = pd.DataFrame(data, columns=['genre','mean'])

fig, ax = plt.subplots(figsize=(14,6), nrows=1, ncols=1)
sns.barplot(x="mean",
            y="genre",
            data=genre_data,
            order=genre_data.sort_values('mean', ascending = False).genre
            )
plt.ylabel('')
plt.xlabel('Mean box office')


# %%
# make list of all unique genres
all_actors = []
for i in movies.actors:
    for j in i:
        all_actors.append(j)
actors = np.array(all_actors)
unique_actors = np.unique(actors)

# make list of all unique genres
all_directors = []
for i in movies.director:
    for j in i:
        all_directors.append(j)
directors = np.array(all_directors)
unique_directors = np.unique(directors)

# make list of all unique genres
all_genres = []
for i in movies.genre:
    for j in i:
        all_genres.append(j)
genres = np.array(all_genres)
unique_genres = np.unique(genres)


# %%
movies.to_csv('./data/movies_clean_new.csv', index=False)





















