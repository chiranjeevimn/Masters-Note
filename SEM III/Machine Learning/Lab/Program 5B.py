# KNN Algorithm for another dataset

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# print(sns.get_dataset_names())

data = sns.load_dataset("iris")
# print(data.head())
# print(data.info())
# print(data.isnull().sum())
# print(data['species'].value_counts())

# features
x = np.array(data.iloc[:, 0:4])
# print(x)
# print(x.shape)
y = np.array(data.iloc[:, 4])
# print(y)
# print(y.shape)

from sklearn.model_selection import train_test_split

xtrain, xtest, ytrain, ytest = train_test_split(x, y, train_size=.80, random_state=3)
# print(xtest.shape)

from sklearn.neighbors import KNeighborsClassifier

model = KNeighborsClassifier(n_neighbors=4, p=2)
model.fit(xtrain, ytrain)

ypred = model.predict(xtest)
# print(ypred)
# print(ytest)

print(ytest[1] == ypred[1])
count = 0
for i in range(len(ytest)):
    if ypred[i] == ytest[i]:
        count = count + 1
print(count)
print(len(ytest))

# Accuracy
print(count / len(ytest) * 100)

# Another way to find accuracy
from sklearn.metrics import accuracy_score

a = accuracy_score(ytest, ypred)
print(a * 100)

import joblib

joblib.dump(model, "iris.pkl")
                                                                               
mymod = joblib.load("C:/Users/MCA/Chiru/iris.pkl")
print(mymod.predict([[4.7, 3.2, 1.3, 0.2]]))
