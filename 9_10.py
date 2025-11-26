import pandas as pd
import numpy as np
import seaborn as sns

# #
# # points = {
# #     'P1': [0.1, 0.6],
# #     'P2': [0.15, 0.71],
# #     'P3': [0.08, 0.9],
# #     'P4': [0.16, 0.85],
# #     'P5': [0.2, 0.3],
# #     'P6': [0.25, 0.5],
# #     'P7': [0.24, 0.1],
# #     'P8': [0.3, 0.2],
# # }
# points={
#     'P1':[0.1,0.6],
#     'P2':[0.15,0.71],
#     'P3':[0.08,0.9],
#     'P4':[0.16,0.85],
#     'P5':[0.2,0.3],
#     'P6':[0.25,0.5],
#     'P7':[0.24,0.1],
#     'P8':[0.3,0.2]
# }
#
# df=pd.DataFrame.from_dict(points,orient='index',columns=["X","Y"]).reset_index().rename(columns={'index':'Points'})
#
# m1=np.array(points["P1"])
# m2=np.array(points["P8"])
#
# pts=df[["X","Y"]].values
# df['d1']=np.linalg.norm(pts-m1,axis=1)
# df['d2']=np.linalg.norm(pts-m2,axis=1)
# df["Cluster"]=np.where(df['d1'] <= df['d2'],1,2)
#
# print(df)
#
# print(df[df["Points"]=="P6"]["Cluster"].values[0])
#
# m2clus=df[df["Cluster"]==2]
# print(len(m2clus))
#
# m1new=df[df["Cluster"]==1][["X","Y"]].mean().values
# m2new=df[df["Cluster"]==2][["X","Y"]].mean().values
#
# print("\n",m1new,"\n",m2new)
#
#
#
#
#
import pandas as pd

rows=[("P1",0.1,0.6),
      ("P2",0.15,0.71),
      ("P3",0.08,0.9),
      ("P4",0.16,0.85),
      ("P5",0.2,0.3),
      ("P6",0.25,0.5),
      ("P7",0.24,0.1),
      ("P8",0.3,0.2),
]

df=pd.DataFrame(rows,columns=["Points","X","Y"])
print(df)

m1=df[df["Points"]=="P1"][["X","Y"]].values[0]
m2=df[df["Points"]=="P8"][["X","Y"]].values[0]

pts=df[["X","Y"]].values
df["d1"]=np.linalg.norm(pts-m1,axis=1)
df["d2"]=np.linalg.norm(pts-m2,axis=1)
df["Cluster"]=np.where(df["d1"]<=df["d2"],1,2)

print(df)

print(df[df["Points"]=="P6"]["Cluster"].values[0])

m2clus=df[df["Cluster"]==2]
print(len(m2clus))

m1new=df[df["Cluster"]==1][["X","Y"]].mean().values
m2new=df[df["Cluster"]==2][["X","Y"]].mean().values
print(m1new)
print(m2new)