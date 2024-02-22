import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import svm
from sklearn import metrics

digits = datasets.load_digits()
clf = svm.SVC(gamma=0.00001, C=100)
x, y = digits.data[:-10], digits.target[:-10]
clf.fit(x, y)

print(clf.predict(digits.data[:-10]))
plt.imshow(digits.images[6], interpolation='nearest')
plt.show()
