import pandas as pd

movies = pd.read_csv("tmdb_5000_movies.csv")

movies = movies[['title', 'keywords', 'genres', 'vote_average']]
movies['important_words'] = ''
