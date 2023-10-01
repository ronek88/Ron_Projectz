#Python Libraries
#jupyter.org
libs = ['Pandas', 'Numpy', 'Sklearn', 'Seaborn']
print('Important libraries we will use in machine learning: {}'.format(','.join(libs)))




#try to import numpy with Conda environment 3.8
import numpy as np

random_numbers_1_10 = np.random.randint(1, 10)
print('\nGenerate by numpy random number from 1 to 10: ' + str(random_numbers_1_10))
print('\n')



#play with sklearn and boston dataset
from sklearn import datasets
import os
import pandas as pd

# first_dataset = datasets.load_boston()
# print('\n')
# print(first_dataset.DESCR)

IRIS = pd.read_csv('datasetss\IRIS.csv')
print(IRIS.info())
print('\n')
print(IRIS.head(6))