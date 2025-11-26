# import numpy as np
# import pandas as pd
# import seaborn as sns
#
# # Load Iris dataset from seaborn
# df = sns.load_dataset("iris")
#
# # Keep only numeric columns (drop 'species')
# cols = ["sepal_length","sepal_width","petal_length","petal_width"]
# X = df[cols].values
#
# # Randomly choose 3 initial centroids
# np.random.seed(0)
# idx = np.random.choice(len(df), 3, replace=False)
# m1 = df.iloc[idx[0]][cols].values
# m2 = df.iloc[idx[1]][cols].values
# m3 = df.iloc[idx[2]][cols].values
#
# print("Initial centroids:")
# print("m1:", m1)
# print("m2:", m2)
# print("m3:", m3)
#
# # ------------------------------
# # K-Means Loop for 10 iterations
# # ------------------------------
# for i in range(10):
#
#     pts = df[cols].values
#
#     # compute Euclidean distances
#     df["d1"] = np.linalg.norm(pts - m1, axis=1)
#     df["d2"] = np.linalg.norm(pts - m2, axis=1)
#     df["d3"] = np.linalg.norm(pts - m3, axis=1)
#
#     # assign clusters
#     df["cluster"] = df[["d1","d2","d3"]].idxmin(axis=1)
#     df["cluster"] = df["cluster"].map({"d1":1, "d2":2, "d3":3})
#
#     # compute new centroids
#     c1 = df[df.cluster==1][cols].mean().values
#     c2 = df[df.cluster==2][cols].mean().values
#     c3 = df[df.cluster==3][cols].mean().values
#
#     # update if cluster not empty
#     if not np.isnan(c1).any(): m1 = c1
#     if not np.isnan(c2).any(): m2 = c2
#     if not np.isnan(c3).any(): m3 = c3
#
#     print(f"\nIteration {i+1}")
#     print("m1:", m1)
#     print("m2:", m2)
#     print("m3:", m3)
#
# print("\nFINAL CENTROIDS:")
# print("m1:", m1)
# print("m2:", m2)
# print("m3:", m3)



import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
print(df.columns)
cols=df.drop("species",axis=1).columns.tolist()
k=3
iter=10

index=np.random.choice(len(df),size=3,replace=False)
m1=df.iloc[index[0]][cols].values.astype(float)
m2=df.iloc[index[1]][cols].values.astype(float)
m3=df.iloc[index[2]][cols].values.astype(float)



for i in range(10):
    points=df[cols].values.astype(float)
    df["d1"]=np.linalg.norm(points-m1,axis=1)
    df["d2"]=np.linalg.norm(points-m2,axis=1)
    df["d3"]=np.linalg.norm(points-m3,axis=1)

    df["Cluster"]=df[["d1","d2","d3"]].idxmin(axis=1)
    df["Cluster"]=df["Cluster"].map({"d1":1,"d2":2,"d3":3})

    m1=df[df["Cluster"]==1][cols].mean().values
    m2=df[df["Cluster"]==2][cols].mean().values
    m3=df[df["Cluster"]==3][cols].mean().values

print(m1)
print(m2)
print(m3)



