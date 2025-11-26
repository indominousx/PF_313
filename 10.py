import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
rows=[("P1",2,10),
      ("P2",2,5),
      ("P3",8,4),
      ("P4",5,8),
      ("P5",7,5),
      ("P6",6,4),
      ("P7",1,2),
      ("P8",4,9)]

df=pd.DataFrame(rows,columns=["Points","X","Y"])
print(df)

cols=["X","Y"]

m1=df[df["Points"]=="P1"][cols].values
m2=df[df["Points"]=="P4"][cols].values
m3=df[df["Points"]=="P7"][cols].values


pts=df[cols].values
df["d1"]=np.linalg.norm(pts-m1,axis=1)
df["d2"]=np.linalg.norm(pts-m2,axis=1)
df["d3"]=np.linalg.norm(pts-m3,axis=1)

df["Cluster"]=df[["d1","d2","d3"]].idxmin(axis=1)
df["Cluster"]=df["Cluster"].map({"d1":1,"d2":2,"d3":3})


