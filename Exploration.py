import pandas as pd 
import numpy as np
import GatherAndCleanData
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

movies = GatherAndCleanData.getMovies()

count = CountVectorizer()

count_matrix = count.fit_transform(movies['important_words'])


cosine_sim = cosine_similarity(count_matrix, count_matrix)
