# Linear Regression
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("C:/Users/MCA/Desktop/ML Lab Dataset/salary_data.csv")
# print(data.head())
# print(data.info())

# x = data['YearsExperience']
# print(x)

# x = np.array(data.iloc[:, 0])
# print(x)
# print(x.shape)

X = np.array(data.iloc[:][['YearsExperience']])
# print(X.shape)

y = np.array(data.iloc[:, 1])
# print(y.shape)

# import scikit-learn
from sklearn.model_selection import train_test_split
#
# # random state is the seed value that can take 1 to 2 to power 32-1
xtrain, xtest, ytrain, ytest = train_test_split(X, y, train_size=.80, random_state=4697)
# # print(xtrain ,ytrain)
#
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(xtrain, ytrain)
#
# # Prediction
ypred = model.predict(xtest)
# # print(ypred)
# # print(ytest)

from sklearn.metrics import r2_score
r2 = r2_score(ytest, ypred)
print(r2)

# # plot the training samples - x and y
# plt.figure(figsize=(8,5))
# plt.scatter(xtrain, ytrain, color='red', s=100, label='ActualPoints')
# plt.scatter(xtrain,model.predict(xtrain), color='green', s=100, label='PredictedPoints')
#
# # line of regression
# plt.plot(xtrain, model.predict(xtrain), linestyle="dotted", color='yellow')
# plt.show()

# For testing dataset
plt.figure(figsize=(8,5))
plt.scatter(xtest, ytest, color='red', s=100, label='ActualPoints')
plt.scatter(xtest,model.predict(xtest), color='green', s=100, label='PredictedPoints')

# line of regression
plt.plot(xtest, model.predict(xtest), linestyle="dotted", color='yellow')
plt.show()

# scores=[]
# for i in range(5000):
#     xtrain1, xtest1, ytrain1, ytest1=  train_test_split(X, y, train_size=.80, random_state=i)
#     model1 = LinearRegression()
#     model1.fit(xtrain1, ytrain1)
#     ypred1 = model1.predict(xtest1)
#     scores.append(r2_score(ytest1, ypred1))
# print(scores)
# print(np.max(scores))
# print(np.argmax(scores))


