from sklearn import datasets
import os
import numpy as np
import pandas as pd
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

IRIS = pd.read_csv('datasetss\IRIS.csv')
print(IRIS.info())
print('\n')
print(IRIS)

# encoded_dataset_getdummies = pd.get_dummies(IRIS, prefix=['species'])
# print('\n')
# print(encoded_dataset_getdummies)

#encode objects to binaries numbers for species
label_encoding = preprocessing.LabelEncoder()
IRIS['species_encoded'] = label_encoding.fit_transform(IRIS['species'])
print('\n')
print(IRIS)

print('\n')
print(IRIS.describe())


#scaling, normalization of datas to not have so big differences in the numbers,
#system is using STD and average,, STD (smerodajna odchylka)
custom_dataset = pd.DataFrame({'vek': [20,30,40], 'zostatok': [3000,4500,200]})
print('\n')
print(custom_dataset, '\n')

print('\n')
print('Priemer je: \n{}\n'.format(np.mean(custom_dataset)))

print('\n')
print('Smerodajna odchylka STD je: \n{}\n'.format(np.std(custom_dataset)))

scaler = StandardScaler()
norm = scaler.fit_transform(custom_dataset)
print('\n')
print(norm)