import glob
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#import statsmodels.api as sm
import matplotlib

#zakres wierszy: 2929 - 20471 (2016.01.01 - 2017.12.31)
start_row = 2929
end_row = 20472

initial_df = pd.read_csv("../data/raw/odczyty_archh_urzadz_5004.csv",
                         sep=";",
                         usecols=["Data czas", "Energia", "T zewn.", "V wiatr",
                                  "Wilg.", "Zachm", "Dlug. dnia", "Typ dnia", "Pora roku"],
                         skiprows=lambda x: x in [1, 2],
                         dtype={
                             "V wiatr": "int32",
                             "Wilg.": "int32",
                             "Zachm": "int32",
                             "Typ dnia": "int32",
                             "Pora roku": "int32"
                         },
                         decimal=",").iloc[start_row:end_row]

initial_df["Energia"] = 0

all_files = glob.glob('../data/raw/*.csv')
for filename in all_files:
    file = pd.read_csv(filename,
                       sep=';',
                       usecols=["Energia"],
                       skiprows=lambda x: x in [1, 2],
                       decimal=",").iloc[start_row:end_row]

    initial_df["Energia"] += file["Energia"]

initial_df.index = np.arange(1, len(initial_df)+1)

print(initial_df.head())
initial_df.to_csv("../data/preprocessed/data.csv", index=False)