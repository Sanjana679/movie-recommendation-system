import pandas as pd 
import numpy as np 
from rake_nltk import Rake
import string

# Cleans the string for random punctuation, numbers, and quotations
# test = true when it is the genre column 
def clean_1 (string, test):
    string = string.replace('[', '', -1)
    string = string.replace(']', '', -1)
    string = string.replace('{', '', -1)
    string = string.replace('}', '', -1)
    string = string.replace('"', '', -1)

    if(test == True):
        string = string.replace('name', '', -1)
        string = string.replace('id', '', -1)
        string = string.replace('1', '', -1)
        string = string.replace('2', '', -1)
        string = string.replace('3', '', -1)
        string = string.replace('4', '', -1)
        string = string.replace('5', '', -1)
        string = string.replace('6', '', -1)
        string = string.replace('7', '', -1)
        string = string.replace('8', '', -1)
        string = string.replace('9', '', -1)
        string = string.replace('0', '', -1)
    string = string.replace(':', '', -1)
    string = string.replace('(', '', -1)
    string = string.replace(')', '', -1)
    string = string.replace('\'\'', ', ', -1)

    while string.find(', ,') != -1:
        string = string.replace(', ,', ',', -1)

    while string.find('\'') != -1:
        string = string.replace('\'', '', -1)

    while string.find(', ') != -1:
        string = string.replace(', ', ',', -1)

    while string.find(',,') != -1:
        string = string.replace(',,', ',', -1)
    
    string = string.replace(' ', '', -1)
    return string

#extracts the keywords from the from_column, and puts it in the to_column
def extract_keywords(from_column, to_column, test):
    for index, row in movies.iterrows():
        holder = str(row[from_column])

        # instantiating Rake, by default it uses english stopwords from NLTK
        # and discards all puntuation characters as well
        r = Rake()

        # extracting the words by passing the text
        r.extract_keywords_from_text(holder)

        # getting the dictionary whith key words as keys and their scores as values
        key_words_dict_scores = r.get_word_degrees()
        
        # assigning the key words to the new column for the corresponding movie

        if(test == True):
            movies[to_column][index] = movies[to_column][index] + clean_1(str(list(key_words_dict_scores.keys())), True) + ' '
        else:   
            movies[to_column][index] = movies[to_column][index] + clean_1(str(list(key_words_dict_scores.keys())), False) + ' '
    return

def put_in_important_words(from_column):
    for index, row in movies.iterrows():
        holder = str(row[from_column])
        holder = holder.replace(' ', '', -1)
        movies['important_words'][index] = movies['important_words'][index]+ holder + ' '
    return
#########################################################################

movies = pd.read_csv("tmdb_5000_movies.csv")

movies = movies[['title', 'genres', 'overview', 'vote_average']]
movies['important_words'] = ''

#extract the keywords from each column and put the keywords in the important_words column 
put_in_important_words('title')
extract_keywords('overview', 'important_words', False)
extract_keywords('genres', 'important_words', True)
put_in_important_words('title')

#after extracting the keywords, remove the columns except for important_words and vote_average
movies.drop(columns = ['overview'], inplace = True)
movies.drop(columns = ['genres'], inplace = True)


#replace the commas in the strings with spaces 
count = 0
while count < len(movies['important_words']):
    movies['important_words'][count] = movies['important_words'][count].replace(',',' ', -1)
    count = count + 1

#print(movies['important_words'][61])
def getMovies():
    return movies
