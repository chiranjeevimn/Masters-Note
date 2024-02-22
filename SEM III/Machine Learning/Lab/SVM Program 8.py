# SVM Algorithm

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics

# loading the dataset
df = datasets.load_breast_cancer()
# print(df)
# print(df['target'])

x_train, x_test, y_train, y_test = train_test_split(df.data, df.target, test_size=0.4, random_state=209)

cls = svm.SVC(kernel="linear")
cls.fit(x_train, y_train)
pred = cls.predict(x_test)

print("Accuracy:", metrics.accuracy_score(y_test, y_pred=pred)*100)
print("Precision Score:", metrics.precision_score(y_test, y_pred=pred))
print("Recall:", metrics.recall_score(y_test, y_pred=pred))
print(metrics.classification_report(y_test, y_pred=pred))
