import pandas as pd

df = pd.read_csv("data.csv", sep=",")

col_names = df.columns.names
coordinates = df[['X_COORD', 'Y_COORD']].values


#%%
import matplotlib.pyplot as plt

plt.scatter(coordinates[:,0], coordinates[:,1], s=1)
plt.show()

#%%
