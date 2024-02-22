import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
import pandas as pd

df = pd.read_csv("C:/Users/MCA/Desktop/ML Lab Dataset/driver-data.csv")
# print(df)
# print(df.info())
x1 = df['mean_dist_day'].values
x2 = df['mean_over_speed_perc'].values
# print(x1, x2)

y = np.array(list(zip(x1, x2))).reshape(len(x1), 2)
# print(y)
print(y.shape)

plt.plot()
plt.xlim([0, 250])
plt.ylim([0, 100])
plt.title('Dataset')
plt.scatter(x1, x2)
plt.show()

import matplotlib.pyplot as plt1

kmeans = KMeans(n_clusters=3)
kmeans.fit(y)
print(kmeans.cluster_centers_)
plt.title("KMEANS")
plt1.scatter(y[:, 0], y[:, 1], c=kmeans.labels_, cmap='rainbow')
plt1.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], color="black")
plt1.show()
