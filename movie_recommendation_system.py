# -*- coding: utf-8 -*-
"""Movie recommendation system

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rV_cAvOnmE7MrCtPl1fTwjKNHTj9LkzW

# **Movie Recommendation System**

# **Objective :**

To develop a personalized Movie Recommendation System that leverages machine learning algorithms and user preferences to suggest movies tailored to individual tastes. The primary goal is to enhance user engagement and satisfaction by providing relevant movie recommendations based on historical viewing behavior and movie attributes. The system will strive to achieve a high level of accuracy and user-friendliness, making it a valuable tool for movie enthusiasts seeking personalized movie suggestions.

# **Data Source :**

This Data source is taken from github of ybi repositories. It's an a csv file.

# **Import Library :**
"""

import pandas as pd
import numpy as np

"""# **Import DataSet :**"""

df = pd.read_csv(r"https://raw.githubusercontent.com/Naveen1131/MovieRecommendation/main/Movies%20Recommendation.csv")

df.head()

df.info()

df.shape

df.columns

"""# **Feature Selection :**"""

df_features = df[['Movie_Title','Movie_Budget','Movie_Production_Country','Movie_Cast','Movie_Director']].fillna('')

"""Selected five existing features from recommended movies. It can vary for each movie."""

df_features.shape

df_features

import numpy as np

# Assuming df_features contains your data
X = np.array(df_features[['Movie_Title', 'Movie_Budget', 'Movie_Production_Country', 'Movie_Cast', 'Movie_Director']])
shape = X.shape
print(shape)

X.shape

"""# **Get Feature Text Conversion to Tokens**"""

from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Sample text data
df = pd.read_csv(r"https://raw.githubusercontent.com/Naveen1131/MovieRecommendation/main/Movies%20Recommendation.csv")

# Create a DataFrame from the sample data
df = pd.DataFrame(df)

# Combine the text data from multiple columns into a single Series
combined_text = str(df['Movie_Title']) + ' ' + str(df['Movie_Budget']) + ' ' + str(df['Movie_Production_Country']) + ' ' + str(df['Movie_Cast']) + ' ' + str(df['Movie_Director'])

# Create and fit the TF-IDF vectorizer
tfidf = TfidfVectorizer()
X_tfidf = tfidf.fit_transform(df['Movie_Title'])

# Now, X_tfidf contains the TF-IDF vectorized representation of the combined text data
# You can use X_tfidf for further machine learning tasks

X_tfidf.shape

print(X_tfidf)

"""# **Get Similarity Score using Cosine Similarity**

Cosine similarity is a metric used to measure the similarity between two non-zero vectors in an inner product space. In the context of text data or document similarity, cosine similarity is often used to determine how similar two documents are based on the angle between their vector representations in a multi-dimensional space.
"""

from sklearn.metrics.pairwise import cosine_similarity

Similarity_Score = cosine_similarity(X_tfidf)

Similarity_Score

Similarity_Score.shape

"""# **Get Movie as Input from user and validate for closest spelling**"""

Favourite_Movie_Name = input('Enter your favourite movie name : ')

All_Movies_Title_List = df['Movie_Title'].tolist()

import difflib

Movie_Recommendation = difflib.get_close_matches(Favourite_Movie_Name,All_Movies_Title_List)
print(Movie_Recommendation)

Close_Match = Movie_Recommendation[0]
print(Close_Match)

Index_of_Close_Match_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
print(Index_of_Close_Match_Movie)

Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Close_Match_Movie]))
print(Recommendation_Score)

len(Recommendation_Score)

"""# **Get All Movies Sort Based on Recommendation Score Wrt Favourite Movie**"""

Sorted_Similar_Movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)
print(Sorted_Similar_Movies)

print('Top 30 Movies Suggested for you : \n')

i = 1

for movie in Sorted_Similar_Movies:
  index = movie[0]
  title_from_index = df[df.index==index]['Movie_Title'].values[0]
  if(i<31):
    print(i, '.',title_from_index)
    i+=1

"""# **Top 10 Movie Recommendation System**"""

Movie_Name = input('Enter your favourite movie name : ')
list_of_all_titles = df['Movie_Title'].tolist()
Find_Close_Match = difflib.get_close_matches(Movie_Name,list_of_all_titles)
Close_Match = Find_Close_Match[0]
Index_of_Movie = df[df.Movie_Title == Close_Match]['Movie_ID'].values[0]
Recommendation_Score = list(enumerate(Similarity_Score[Index_of_Movie]))
sorted_similar_movies = sorted(Recommendation_Score, key = lambda x:x[1], reverse = True)

print('Top 10 Movies Suggested for you : \n')

i = 1

for movie in sorted_similar_movies:
  index = movie[0]
  title_from_index = df[df.Movie_ID==index]['Movie_Title'].values
  if(i<11):
    print(i, '.',title_from_index)
    i+=1