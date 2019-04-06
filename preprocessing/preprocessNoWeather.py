import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#import statsmodels.api as sm
import matplotlib


initial_df = pd.read_csv("../data/raw/odczyty_archh_urzadz_5004.csv",
                         sep=";",
                         usecols=["Data czas", "Energia", "Dlug. dnia", "Typ dnia", "Pora roku"],
                         skiprows=lambda x: x in [1, 2],
                         dtype={
                             "Typ dnia": "int32",
                             "Pora roku": "int32"
                         },
                         decimal=",")

initial_df["Energia"] = 0

all_files = glob.glob('../data/raw/*.csv')
for filename in all_files:
    file = pd.read_csv(filename,
                       sep=';',
                       usecols=["Energia"],
                       skiprows=lambda x: x in [1, 2],
                       decimal=",")

    initial_df["Energia"] += file["Energia"]

initial_df.index = np.arange(1, len(initial_df)+1)

print(initial_df.head())
initial_df.to_csv("../data/preprocessed/dataNoWeather.csv", index=False)