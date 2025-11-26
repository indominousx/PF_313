import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=sns.load_dataset("titanic")
print(df)

print(df.sample(10))
print(len(df[df["sex"]=="male"]))

print(df.shape[0])

df1=df[(df["sex"]=="male") & (df["alive"]=="yes")]
print(len(df1))

print(df.describe())
print(df.dtypes)


df2=pd.read_csv("Telecom Churn.csv")
print(df2.head())
print(df2.columns)

print(df2.mean(numeric_only=True))
print(df2.count(numeric_only=True))
print(df2.std(numeric_only=True))
num_only=df2.select_dtypes(include="number")
print(num_only.quantile(0.25,numeric_only=True))
print(num_only.quantile(0.50,numeric_only=True))
print(num_only.quantile(0.75,numeric_only=True))




