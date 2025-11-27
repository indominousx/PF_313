import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

df=sns.load_dataset("iris")
print(df)

k=3
iter=10

X=df.drop("species",axis=1).columns.tolist()
print(X)

index=np.random.choice(len(df),size=3,replace=False)
m1=df.iloc[index[0]][X].values.astype(float)
m2=df.iloc[index[1]][X].values.astype(float)
m3=df.iloc[index[2]][X].values.astype(float)

for i in range(10):
    points=df[X].values.astype(float)
    df["d1"]=np.linalg.norm(points-m1,axis=1)
    df["d2"]=np.linalg.norm(points-m2,axis=1)
    df["d3"]=np.linalg.norm(points-m3,axis=1)

    df["Cluster"]=df[["d1","d2","d3"]].idxmin(axis=1)
    df["Cluster"]=df["Cluster"].map({"d1":1,"d2":2,"d3":3})

    m1=df[df["Cluster"]==1][X].mean().values.astype(float)
    m2=df[df["Cluster"]==2][X].mean().values.astype(float)
    m3=df[df["Cluster"]==3][X].mean().values.astype(float)

print(m1,m2,m3)



