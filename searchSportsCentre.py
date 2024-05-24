import pandas as pd

from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Read dataset
dataset1=pd.read_csv("D:/Xampp/htdocs/Sports Centre/Sport Centre.csv")

#Cleaning address and court Series
dataset1["ADDRESSTEST"] = dataset1["ADDRESS"]
dataset1["ADDRESSTEST"] = dataset1["ADDRESSTEST"].replace(',','', regex=True)
dataset1["COURTTEST"] = dataset1["COURT"]
dataset1["COURTTEST"] = dataset1["COURTTEST"].replace(',','', regex=True)

#Copy dataset
def important_features(dataset):
    data=dataset1.copy()

    data["Recommend1"]=data["NAME"]+ data["LOCATION"]
    return data

data=important_features(dataset1)

from sklearn.feature_extraction.text import TfidfVectorizer

#Declaring a vector object for TFIDF
vector=TfidfVectorizer(stop_words="english")

#Learn the vocabulary of recommendation column that have merge the features
#Return the term-document matrix
vecs=vector.fit_transform(data["Recommend1"].apply(lambda x: np.str_(x)))


#Make cosine similarity comparison between vectors
sim=cosine_similarity(vecs) 


#Process of recommendation based on user last booking
def recommend(title):

    #Create indices index from title
    indices = pd.Series(data.index, index = data['NAME'])
    idx = indices[title]

    #Make similarity based on the name of sports centre from indices
    #Make a list based on cosine similarity scores
    scores= list(enumerate(sim[idx]))

    #Sort the scores in descending order
    sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
    sorted_scores= sorted_scores[0:1]
   
    #Create a variable index to access the recommendation list
    sim_index = [i[0] for i in sorted_scores]

    #Assign new variables to access the recommendation list Series
    name = data['NAME'].iloc[sim_index]
    location = data['LOCATION'].iloc[sim_index]
    address= data['ADDRESS'].iloc[sim_index]
    court= data['COURT'].iloc[sim_index]

    #Create a recommendation DataFrame
    recommendationBooking_data = pd.DataFrame(columns=['NAME','ADDRESS','LOCATION','COURT'])

    #Assign the DataFrame value from the recommendation list Series
    recommendationBooking_data['NAME'] = name
    recommendationBooking_data['ADDRESS'] = address
    recommendationBooking_data['LOCATION'] = location
    recommendationBooking_data['COURT'] = court
    
    #Return DataFrame
    return recommendationBooking_data