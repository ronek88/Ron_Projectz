from sklearn import datasets
import os
import numpy as np
import pandas as pd


IRIS = pd.read_csv('datasetss\IRIS.csv')
print(IRIS.info())
print('\n')
print(IRIS.head(6))


#Check of missing values in dataset
print('\nNumber of missing values in IRIS data set is: {}'.format(IRIS.isnull().sum()))
print('\n')


#Prepare dataset with the missing value
ukazka = {'meno':['Tomas', 'Patrik'], 'vek':[10,np.nan], 'vaha': [20,30]}
df = pd.DataFrame(data=ukazka)
print(df)
print('\n')
print(df.isnull().sum())


#one possibility is to remove the whole columns with the method drop
#or fill missing values with average of values in the column
print('\n')
df_remove_missing_columns = df.drop('vek', axis=1)
print(df_remove_missing_columns)

print('\n')
df_fill_missing_values = df.fillna(df.mean())
print(df_fill_missing_values)