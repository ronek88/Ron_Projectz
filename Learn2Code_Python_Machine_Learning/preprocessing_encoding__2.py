from sklearn import datasets
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing


IRIS = pd.read_csv('datasetss\IRIS.csv')
print(IRIS.info())
print('\n')
print(IRIS)




#Why encoding? because data set can contains not float and in values and
#lot of alghorithms are working with only numbers so we have to encode this object
#values to binary numbers
encoded_dataset_getdummies = pd.get_dummies(IRIS, prefix=['species'])
print('\n')
print(encoded_dataset_getdummies)


label_encoding = preprocessing.LabelEncoder()
IRIS['species_encoded'] = label_encoding.fit_transform(IRIS['species'])
print('\n')
print(IRIS)




