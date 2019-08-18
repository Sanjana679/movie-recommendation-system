import pandas as pd 
import numpy as np
import GatherAndCleanData
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies = GatherAndCleanData.getMovies()

count = CountVectorizer()

count_matrix = count.fit_transform(movies['important_words'])


cosine_sim = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(GatherAndCleanData.getMovies().index)
indices[:5]

# function that takes in movie title as input and returns the top 10 recommended movies
def recommendations(title, cosine_sim = cosine_sim):
    
    recommended_movies = []
    
    # gettin the index of the movie that matches the title
    count = 0
    while count < len(movies['title']):
        selected_movie_index = 0

        if movies['title'][count] == title:
            selected_movie_index = count
        count = count + 1

    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[selected_movie_index]).sort_values(ascending = False)

    # getting the indexes of the 10 most similar movies
    top_10_indexes = list()
    
    for i in range(10):
        top_10_indexes.append(i)

    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(movies['title'][i])
        
    return recommended_movies


print(recommendations('The Lone Ranger'))
