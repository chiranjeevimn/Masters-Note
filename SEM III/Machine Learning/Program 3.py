import pandas as pd
import numpy as np

df = pd.read_csv("C:/Users/MCA/Desktop/ML Lab Dataset/Poison.csv")
# print(df)

concepts = np.array(df)[:, :-1]
# print(concepts)

target = np.array(df)[:, -1]


# print(target)

def train(con, tar):
    for i, val in enumerate(tar):
        if val == "yes":
            spe_h = con[i].copy()
            break
    for i, val in enumerate(con):
        if tar[i] == "yes":
            for x in range(len(spe_h)):
                if val[x] != spe_h[x]:
                    spe_h[x] = "?"
                else:
                    pass
    return spe_h


print(train(concepts, target))
