import pandas as pd
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score
import collections
import numpy as np, matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn.model_selection import GridSearchCV
import re
from sklearn.preprocessing import Binarizer


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


#prepare data for x and y axis where we are using only species encoded, petal length and petal width
y = IRIS_only_numbers['species_encoded'].values
x = IRIS_only_numbers[['petal_length', 'petal_width']].values


#avoid overfitting by splitting data to test and train, 80 percent train and 20 percent test
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.2)


#use scaling for data to not have too big differences in the values, simply normalize values
sc = StandardScaler()
x_train_featured = sc.fit_transform(x_train)
x_test_featured = sc.fit_transform(x_test)


#use KNeihbor algorithm to train data according to algorith KNeighbors
knn = KNeighborsClassifier(n_neighbors=9, metric='euclidean', weights='uniform')
knn.fit(x_train, y_train)
print(knn)


#test prediction for new values new x_new count new y predict
x_new = sc.transform([[1.4,0.2]])
new_prediction = knn.predict(x_new)
print('\n')
print('Prediction for new petal values is: {}'.format(new_prediction))


#Test set predicition for x values in dataset
y_pred = knn.predict(x_test)
print('Test set - predictions: {}'.format(y_pred))
count_predics = collections.Counter(y_pred)
print(count_predics)
print('\n')


#check correctness/accuracy of created model and predicted data
cm = confusion_matrix(y_test,y_pred)
print(cm)
score = accuracy_score(y_test, y_pred)
print('Accuracy of our model is: {}'.format(score))
print('\n')


#display visually accuracy of our model and predicted data
x_set, y_set = x_test, y_test
x1, x2 = np.meshgrid(np.arange(start=x_set[:, 0].min()-1, stop=x_set[:, 0].max() + 1, step=0.01),
                     np.arange(start=x_set[:, 1].min()-1, stop=x_set[:, 1].max() + 1, step=0.01))
plt.contourf(x1, x2, knn.predict(np.array([x1.ravel(), x2.ravel()]).T).reshape(x1.shape),
                                 alpha=0.50, cmap=ListedColormap(('red', 'green', 'blue')))
plt.xlim(x1.min(), x1.max())
plt.ylim(x2.min(), x2.max())

for i,j in enumerate(np.unique(y_set)):
    plt.scatter(x_set[y_set == j, 0], x_set[y_set == j, 1],
                color=ListedColormap(('red', 'green', 'blue'))(i), label = j)
plt.title('K-NN (Test set)')
plt.xlabel('Petal length')
plt.ylabel('Petal width')
plt.legend()
plt.show()


#hyperparameters tuning of our model to decrease errorness
#check row for knn definition especially n_neighbours, weights, metric
#and use technic cross validation to check our best settings of parameters for used algorith
select_params = {'n_neighbors': range(1,12),
                 'weights': ['uniform', 'distance'],
                 'metric': ['euclidean', 'manhattan', 'chebyshev', 'minkowski']}

grid_knn = GridSearchCV(knn, select_params, cv=5)
grid_knn.fit(x_train, y_train)
print('Best params for our model are: {}'.format(grid_knn.best_params_))
print('Best average score on training set is: {}'.format(grid_knn.best_score_))


#feature engineering, we are adding new data into dataset by our knowledge and skills
IRIS['petal_area'] = IRIS['petal_width'] * IRIS['petal_length']
IRIS['sepal_area'] = IRIS['sepal_width'] * IRIS['sepal_length']
print('\n\n')
print(IRIS.head(5))

text = 'teplota je 29.6 C'
pattern = '\d+.\d+'
extract = re.findall(pattern, text)
print('\n')
print(extract)

nakupy = [[6], [2], [4]]
binarizer = Binarizer(threshold=5)
vip = binarizer.fit_transform(nakupy)
print('\n')
print(vip)












print('\n\n\n\n\n\n\n\n\nx')