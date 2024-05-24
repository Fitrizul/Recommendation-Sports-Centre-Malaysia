##Import Libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

#Read dataset
dataset2=pd.read_csv("D:/Xampp/htdocs/Sports Centre/Sport Centre.csv")

#Copy dataset
def important_features(dataset2):
    data2=dataset2.copy()
    return data2

data2=important_features(dataset2)

#Remove duplicate
data2["LocationTest"] = data2["LOCATION"]

#Remove duplicate
data2["LocationTest"].loc[1:24] = "Pulau Pinang duplicate"
data2["LocationTest"].loc[26:48] = "Kedah duplicate"
data2["LocationTest"].loc[50:53] = "Perlis duplicate"
data2["LocationTest"].loc[55:79] = "Perak duplicate"
data2["LocationTest"].loc[80:94] =  "Negeri Sembilan duplicate"
data2["LocationTest"].loc[96:110] = "Melaka duplicate"
data2["LocationTest"].loc[113:142] = "Johor duplicate"
data2["LocationTest"].loc[144:168] =  "Pahang duplicate"
data2["LocationTest"].loc[170:192] =  "Kelantan duplicate"
data2["LocationTest"].loc[194:210] = "Terengganu duplicate"
data2["LocationTest"].loc[212:240] = "Kuala Lumpur duplicate"
data2["LocationTest"].loc[242:271] = "Selangor duplicate"
data2["LocationTest"].loc[273:285] = "Sarawak duplicate"
data2["LocationTest"].loc[287:299] = "Sabah duplicate"

#Declaring vector for TFIDF
vector=TfidfVectorizer(stop_words="english")

#Using LOCATION Series for vectorization
vecs=vector.fit_transform(data2["LOCATION"].apply(lambda x: np.str_(x)))

#Make cosine similarity comparison between vector
sim=cosine_similarity(vecs) 

#Process of recommendation based on location search by user
def recommend(title):

    if title == "Perlis":

        indices = pd.Series(data2.index, index = data2['LocationTest'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)
        sorted_scores= sorted_scores[0:5]
   
        sim_index = [i[0] for i in sorted_scores]

        name = data2['NAME'].iloc[sim_index]
        location = data2['LOCATION'].iloc[sim_index]
        address= data2['ADDRESS'].iloc[sim_index]
        court= data2['COURT'].iloc[sim_index]
    
        recommendationLocation_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationLocation_data['NAME'] = name
        recommendationLocation_data['LOCATION'] = location
        recommendationLocation_data['COURT'] = court
    else:  
        indices = pd.Series(data2.index, index = data2['LocationTest'])
        idx = indices[title]

        scores= list(enumerate(sim[idx]))
        sorted_scores= sorted(scores,key=lambda x:x[1], reverse=True)

        if title == "Pulau Pinang":  
            sorted_scores= sorted_scores[0:25]  
        elif title == "Kedah":
            sorted_scores= sorted_scores[0:24]
        elif title == "Perak":
            sorted_scores= sorted_scores[0:26]
        elif title == "Kuala Lumpur":
            sorted_scores= sorted_scores[0:30]
        elif title == "Selangor": 
            sorted_scores= sorted_scores[0:31]
        elif title == "Negeri Sembilan": 
            sorted_scores= sorted_scores[0:16]
        elif title == "Melaka": 
            sorted_scores= sorted_scores[0:16]
        elif title == "Johor":
            sorted_scores= sorted_scores[0:31]
        elif title == "Pahang":
            sorted_scores= sorted_scores[0:26]
        elif title == "Terengganu":
            sorted_scores= sorted_scores[0:17]
        elif title == "Kelantan":
            sorted_scores= sorted_scores[0:23]
        elif title == "Sarawak":
            sorted_scores= sorted_scores[0:14]
        elif title == "Sabah":
            sorted_scores= sorted_scores[0:14]

        sim_index = [i[0] for i in sorted_scores]

        name = data2['NAME'].iloc[sim_index]
        location = data2['LOCATION'].iloc[sim_index]
        address= data2['ADDRESS'].iloc[sim_index]
        court= data2['COURT'].iloc[sim_index]
    
        recommendationLocation_data = pd.DataFrame(columns=['NAME','LOCATION','COURT'])

        recommendationLocation_data['NAME'] = name
        recommendationLocation_data['LOCATION'] = location
        recommendationLocation_data['COURT'] = court

    return recommendationLocation_data