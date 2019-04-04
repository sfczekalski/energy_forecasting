import pandas as pd

file = pd.read_csv('../data/raw/odczyty_archh_urzadz_5004.csv',
                   sep=';',
                   usecols=["Data czas", "Energia", "T zewn.", "V wiatr",
                            "Wilg.", "Zachm", "Dlug. dnia", "Typ dnia", "Pora roku"],
                   skiprows=lambda x: x in [1, 2],
                   decimal=",")

print(file.head())