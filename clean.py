from rake_nltk import Rake
import string
import gather
from gather import movies

miscellaneous = ['name', 'id', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
punctuation = ['[', ']', '{', '}', '"', ':', '(', ')', '\'\'']
repeatable_punctuation = [', ,', '\'', ', ', ',,']

#clean words for random punctuation, parentheses and replace commas with spaces
def clean (column):
    count = 0
    while count < len(movies.index):

        if(column == 'keywords' or column == 'genres'):
            for word in miscellaneous:
                movies[column][count] = movies[column][count].replace(word, '', -1)
        
        for punct in punctuation:
            movies[column][count] = movies[column][count].replace(punct, '', -1)

        for repeat in repeatable_punctuation:
            while movies[column][count].find(repeat) != -1:
                movies[column][count] = movies[column][count].replace(repeat, ' ', -1)
            
        if(column == 'important_words'):
            movies[column][count] = movies[column][count].replace(',', ' ', -1)
        
        movies[column][count] = str(movies[column][count])

        count = count + 1
    return

#extracts the keywords from the column and separates them with spaces
#if test = true it is because the column is the genre or keyword column with 
def extract_keywords(column):
    count = 0
    while count < len(movies.index):
        # instantiating Rake, by default it uses english stopwords from NLTK
        # and discards all puntuation characters as well
        r = Rake()

        # extracting the words by passing the text
        r.extract_keywords_from_text(str(movies[column][count]))

        # getting the dictionary whith key words as keys and their scores as values
        key_words_dict_scores = r.get_word_degrees()
        
        # assigning the key words to the new column for the corresponding movie

        movies[column][count] = str(list(key_words_dict_scores.keys()))
        
        count = count + 1
        
    return

#puts the words from the column given into the important words column
#and drops the old column
#also replaces commas with spaces
def put_in_important_words(from_column):
    count = 0
    while count < len(movies[from_column]):
        holder = str(movies[from_column][count])
        if(from_column == 'title'):
            holder = holder.replace(' ', '', -1)
        movies['important_words'][count] = movies['important_words'][count] + holder + ' '
        count = count + 1
    if(from_column != 'title'):
        movies.drop(columns = [from_column], inplace = True)
    
    return

#####################################################################################

#clean each column
clean('title')
clean('genres')
clean('keywords')

#extract the keywords from each column
extract_keywords('genres')
extract_keywords('keywords')

#round 2 of cleaning because extract_keywords makes it into a list
clean('genres')
clean('keywords')

#put the words from each column into important_words and delete the old column
put_in_important_words('title')
put_in_important_words('genres')
put_in_important_words('keywords')

#clean the important_words column for random parentheses, brackets, and punctuation
clean('important_words')