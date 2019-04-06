import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
import statsmodels.api as sm
import matplotlib

matplotlib.rcParams['axes.labelsize'] = 14
matplotlib.rcParams['xtick.labelsize'] = 12
matplotlib.rcParams['ytick.labelsize'] = 12
matplotlib.rcParams['text.color'] = 'k'


df = pd.read_csv("data/preprocessed/dataNoWeather.csv", index_col=0)

df.index = pd.to_datetime(df.index)
#print(df.head())
y = df["Energia"].resample('1d').mean()

#y.plot(figsize=(15, 6))
#plt.show()

decomposition = sm.tsa.seasonal_decompose(y, model='additive')
print(decomposition.seasonal)
fig = decomposition.plot()
plt.show()
