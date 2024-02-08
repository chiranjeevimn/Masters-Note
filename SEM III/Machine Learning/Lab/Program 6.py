# Naive Bayesian Program
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
from sklearn.naive_bayes import GaussianNB

df = pd.read_csv("C:/Users/MCA/Desktop/ML Lab Dataset/placement.csv")
# print(df)
# print(df.info())
# print(df.isnull().sum())
# print(df.shape)

# sns.countplot(x="status", data=df)
# plt.show()
# sns.countplot(x="status", hue="gender", data=df)
# plt.show()
df.drop(['sl_no', 'gender', 'ssc_b', 'hsc_b', 'hsc_s', 'degree_t', 'specialisation'], axis=1, inplace=True)
# print(df.info())

enc = LabelEncoder()
df['workex'] = enc.fit_transform(df['workex'])

# feature and Target
x = df.drop('status', axis=1)
y = df['status']
# print(x.shape, y.shape)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=3)


model = GaussianNB()
model.fit(x_train, y_train)

y_pred = model.predict(x_test)
df1 = pd.DataFrame({'Actual Status': y_test, 'Predicted Status': y_pred})
# print(df1)

print(classification_report(y_test, y_pred))
print(confusion_matrix(y_test, y_pred))

print(accuracy_score(y_test, y_pred) * 100)

import joblib

# joblib.dump(model, "naivebayes.pkl")

mymodel = joblib.load("C:/Users/MCA/Chiru/naivebayes.pkl")
print(df)
print(mymodel.predict([[67.00, 92.00, 76.08, 0, 56.0, 59.80]]))
