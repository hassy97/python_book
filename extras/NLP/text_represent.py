import numpy as np
from sklearn.feature_extraction.text import CountVectorizer 

''' how to structure the textful data into the 
    rows colum for the future machine learning
    models predictions'''

# corpus 
corpus =['my name is hassy']

# make an object for the CountVectorizer
vec = CountVectorizer()
# for structuring the text data we use fit_tranform ()

Structure_data = vec.fit_transform(corpus)
print()
# print(Structure_data)

# convert the text data  into the frequency based representation for future use in ml predictions
print(Structure_data.toarray())

# get the features unique words  from the corpus 
vec.get_feature_names()

vec.vocabulary_

#print(vec.vocabulary_)

print(len(vec.get_feature_names()))
