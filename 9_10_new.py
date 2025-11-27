import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

rows=[("P1",0.1,0.6),
      ("P2",0.15,0.71),
      ("P3",0.08,0.9),
      ("P4",0.16,0.85),
      ("P5",0.2,0.3),
      ("P6",0.25,0.5),
      ("P7",0.24,0.1),
      ("P8",0.3,0.2)
      ]
df=pd.DataFrame(rows,columns=["Points","X","Y"])
print(df)

X=["X","Y"]
m1=df[df["Points"]=="P1"][X].values
m2=df[df["Points"]=="P8"][X].values

points=df[X].values
df["d1"]=np.linalg.norm(points-m1,axis=1)
df["d2"]=np.linalg.norm(points-m2,axis=1)
df["Cluster"]=df[["d1","d2"]].idxmin(axis=1)
df["Cluster"]=df["Cluster"].map({"d1":1,"d2":2})


#Answer the Questions
print(df[df["Points"]=="P6"]["Cluster"].values[0])

print(len(df[df["Cluster"]==2]))


m1new=df[df["Cluster"]==1][X].mean().values
m2new=df[df["Cluster"]==2][X].mean().values

print(m1new,m2new)
