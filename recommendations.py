#Import Libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


#Read dataset file
dataset3=pd.read_csv("D:/Xampp/htdocs/Sports Centre/Sport Centre.csv")

#Cleaning dataset

#Split court from a Series to multiple columns
dataset3['COURT1'] = dataset3['COURT']
dataset3[['COURT1','COURT2','COURT3','COURT4']] = dataset3['COURT1'].str.split(',',expand=True)
dataset3.fillna('', inplace=True)


#Manipulating data duplicates
dataset3['COURT1'] = dataset3.loc[dataset3.duplicated('COURT1', keep='first'), 'COURT1'] + ' Duplicate'
dataset3['COURT1'].loc[0] = "Badminton"
dataset3['COURT1'].loc[2] = "Futsal"
dataset3['COURT1'].loc[8] = "Squash"
dataset3['COURT1'].loc[21] = "Tennis Duplicate"
dataset3['COURT1'].loc[213] = "Tennis"
dataset3['COURT2'].loc[1] = "Volleyball"

#Declaring vector for TFIDF
vector=TfidfVectorizer(stop_words="english")

#Using COURT Series for vectorization
vecs=vector.fit_transform(dataset3["COURT"].apply(lambda x: np.str_(x)))

#Make Cosine Similarity
sim=cosine_similarity(vecs)

#Recommendation process of Sports Centre based on Court search by user
def recommend(title):
    
    if title == "Badminton":

        indices = pd.Series(dataset3.index, index = dataset3['COURT1'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:216]

        sim_index = [i[0] for i in sorted_scores]

        name = dataset3['NAME'].iloc[sim_index]
        location = dataset3['LOCATION'].iloc[sim_index]
        court= dataset3['COURT'].iloc[sim_index]

        recommendationCourt_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationCourt_data['NAME'] = name
        recommendationCourt_data['LOCATION'] = location
        recommendationCourt_data['COURT'] = court
        
    elif title == "Futsal":

        indices = pd.Series(dataset3.index, index = dataset3['COURT1'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:160]

        sim_index = [i[0] for i in sorted_scores]

        name = dataset3['NAME'].iloc[sim_index]
        location = dataset3['LOCATION'].iloc[sim_index]
        address= dataset3['ADDRESS'].iloc[sim_index]
        court= dataset3['COURT'].iloc[sim_index]

        recommendationCourt_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationCourt_data['NAME'] = name
        recommendationCourt_data['LOCATION'] = location
        recommendationCourt_data['COURT'] = court

    elif title == "Squash":

        indices = pd.Series(dataset3.index, index = dataset3['COURT1'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:6]

        sim_index = [i[0] for i in sorted_scores]
        
        name = dataset3['NAME'].iloc[sim_index]
        location = dataset3['LOCATION'].iloc[sim_index]
        address= dataset3['ADDRESS'].iloc[sim_index]
        court= dataset3['COURT'].iloc[sim_index]

        recommendationCourt_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationCourt_data['NAME'] = name
        recommendationCourt_data['LOCATION'] = location
        recommendationCourt_data['COURT'] = court

    elif title == "Tennis":

        dataset3['COURT'].loc[21] = "Tennis"
        indices = pd.Series(dataset3.index, index = dataset3['COURT1'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:12]

        sim_index = [i[0] for i in sorted_scores]

        name = dataset3['NAME'].iloc[sim_index]
        location = dataset3['LOCATION'].iloc[sim_index]
        court= dataset3['COURT'].iloc[sim_index]

        recommendationCourt_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationCourt_data['NAME'] = name
        recommendationCourt_data['LOCATION'] = location
        recommendationCourt_data['COURT'] = court

    elif title == "Volleyball":

        indices = pd.Series(dataset3.index, index = dataset3['COURT2'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:11] 

        sim_index = [i[0] for i in sorted_scores]

        name = dataset3['NAME'].iloc[sim_index]
        location = dataset3['LOCATION'].iloc[sim_index]
        court= dataset3['COURT'].iloc[sim_index]

        recommendationCourt_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationCourt_data['NAME'] = name
        recommendationCourt_data['LOCATION'] = location
        recommendationCourt_data['COURT'] = court

    return recommendationCourt_data
