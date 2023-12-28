# Data Pre-Processing
import numpy as np
import pandas as pd

df = pd.read_csv("C:/Users/MCA/Chiru/CHIRU/ML Lab Dataset/movies.csv")

# print(type(df))
# print(df.head())
# print(df.tail())

# print(df.sample(random_state=2))

# print(df.info())

# print(df.isnull().sum())

# Missing Values
# Dropping all attribute null
# df_1 = df.dropna(axis=0, how='all')
# print(len(df_1))
# print(len(df))
#
# # Dropping any attribute null
# df_2 = df.dropna(axis=0, how='any')
# print(len(df_2))
#
# # Dropping particular attribute null
df_3 = df.dropna(axis=0, how='all',subset=["GENRE"])
# print(len(df_3))


df = df.drop(["Gross"], axis=1)
# print(df.isnull().sum())

# print(df["VOTES"])

df["VOTES"] = df["VOTES"].fillna("0")
# print(df.isnull().sum())

# print(df["RunTime"])

MeanR = df["RunTime"].mean()
# print(MeanR)
meanRT=round(MeanR,1)
# print(meanRT)
df['RunTime']=df['RunTime'].fillna(meanRT)
# print(df['RunTime'])
# print(df.isnull().sum())


meanRating=df['RATING'].mean()
# print(meanRating)
meanRating=round(meanRating,1)
# print(meanRating)
df['RATING']=df['RATING'].fillna(meanRating)
# print(df['RATING'])
# print(df.isnull().sum())


# print(df['GENRE'])

df['GENRE']=df['GENRE'].fillna("Comedy")
# print(df.isnull().sum())

# print(df['YEAR'])

df['YEAR']=df['YEAR'].fillna(1999)
print(df.isnull().sum())

print(df.info())