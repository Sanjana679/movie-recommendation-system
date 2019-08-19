import pandas as pd 
import numpy as np
import clean
from clean import movies
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

count = CountVectorizer()

count_matrix = count.fit_transform(movies['important_words'])

cosine_sim = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(movies.index)
indices[:5]

# function that takes in movie title as input and returns the top 10 recommended movies
def recommendations(title):
    
    recommended_movies = []
    
    # gettin the index of the movie that matches the title
    selected_movie_index = -1
    count = 0
    while count < len(movies['title']):
        if movies['title'][count] == title:
            selected_movie_index = count
        count = count + 1

    if selected_movie_index == -1:
        return "Not a valid movie"
      
    # creating a Series with the similarity scores in descending order
    score_series = pd.Series(cosine_sim[selected_movie_index]).sort_values(ascending = False)
    
    # getting the indexes of the 10 most similar movies
    top_10_indexes = list(score_series.iloc[1:11].index)
    
    # populating the list with the titles of the best 10 matching movies
    for i in top_10_indexes:
        recommended_movies.append(movies['title'][i])
        
    return recommended_movies


print(recommendations((input("What is a movie that you have watched recently? : "))))