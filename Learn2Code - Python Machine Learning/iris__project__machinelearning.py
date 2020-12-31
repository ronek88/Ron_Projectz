import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


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

y = IRIS_only_numbers['species_encoded'].values
x = IRIS_only_numbers[['petal_length', 'petal_width']].values

x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)

sc = StandardScaler()
x_train_featured = sc.fit_transform(x_train)
x_test_featured = sc.fit_transform(x_test)






print('x')