import numpy as np
import pandas as pd

data = pd.read_csv('lab1.csv')
features = np.array(data)[:, :-1]
target = np.array(data)[:, -1]

specific_h = features[0].copy()
general_h = [["?" for _ in range(len(specific_h))] for _ in range(len(specific_h))]

for i, h in enumerate(features):
    if target[i] == "yes":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                specific_h[x] = '?'
                general_h[x][x] = '?'
    elif target[i] == "no":
        for x in range(len(specific_h)):
            if h[x] != specific_h[x]:
                general_h[x][x] = specific_h[x]
            else:
                general_h[x][x] = '?'

general_h = [g for g in general_h if g != ['?' for _ in range(len(specific_h))]]

print("\nFinal specific_h:\n", specific_h)
print("Final general_h:\n", general_h)
