from sklearn import datasets
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

IRIS = pd.read_csv('datasetss\IRIS.csv')
print('\n')
print(IRIS)

#encode objects to binaries numbers for species
label_encoding = preprocessing.LabelEncoder()
IRIS['species_encoded'] = label_encoding.fit_transform(IRIS['species'])
# print('\n')
# print(IRIS)

IRIS_only_numbers = IRIS.drop('species', axis=1)
print(IRIS_only_numbers)


#--------HOLDDOUT DATA -----------
#prepare holdout data, 80percent training data and 20 percent test data to avoid overfitting
data = [1,2,3,4,5]
train1, test = train_test_split(data, test_size=0.2)
print('\n')
print(train1)
print(test)

#traing 60, validation 20, test 20 percent
train2, validation = train_test_split(train1, test_size=0.25)
print('\n')
print(train2)
print(test)
#-----------------END------------------



