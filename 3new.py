import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("House Data.csv")
print(df.sample(10))

print(df.info())

df["NetSquareMeters"]=pd.to_numeric(df["NetSquareMeters"].str.replace(r"[^0-9]","",regex=True),errors="coerce")
df["NetSquareMeters"]=df["NetSquareMeters"]/10
df["NetSquareMeters"].astype(int)

print(df.info())

print(df.describe())

num_cols = df.describe().columns
print(num_cols)
for x in num_cols:
    plt.figure(figsize=(10,5))
    sns.histplot(df[x],bins=50,kde=True)
    plt.xlabel(f"Histogram of {x} ")
    plt.ylabel("Frequency")
    plt.show()




