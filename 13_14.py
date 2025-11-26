import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("Covid Vaccine Statewise.csv")
print(df)
print(df.columns.tolist())
print(df.sample(10))
print(df.describe())
print(df.info())


firstdose=df.groupby("State")["First Dose Administered"].sum().astype(int).sort_values(ascending=False)
print(firstdose)

seconddose=df.groupby("State")["Second Dose Administered"].sum().astype(int).sort_values(ascending=False)
print(seconddose)


#14-------------------------------------------------------------
# df["Male(Individuals Vaccinated)"]=df["Male(Individuals Vaccinated)"].fillna(0)
print(df["Male(Individuals Vaccinated)"].fillna(0).sum().astype(int))

print(df["Female(Individuals Vaccinated)"].fillna(0).sum().astype(int))

