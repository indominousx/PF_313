# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# import math
# rows = [
#     ("Young",  "High",   "No",  "Fair", "No"),
#     ("Young",  "High",   "No",  "Good", "No"),
#     ("Middle", "High",   "No",  "Fair", "Yes"),
#     ("Old",    "Medium", "No",  "Fair", "Yes"),
#     ("Old",    "Low",    "Yes", "Fair", "Yes"),
#     ("Old",    "Low",    "Yes", "Good", "No"),
#     ("Middle", "Low",    "Yes", "Good", "Yes"),
#     ("Young",  "Medium", "No",  "Fair", "No"),
#     ("Young",  "Low",    "Yes", "Fair", "Yes"),
#     ("Old",    "Medium", "No",  "Fair", "Yes"),
#     ("Young",  "Medium", "Yes", "Good", "Yes"),
#     ("Middle", "Medium", "No",  "Good", "Yes"),
#     ("Middle", "High",   "Yes", "Fair", "Yes"),
#     ("Old",    "Medium", "No",  "Good", "No"),
# ]
# 
# df = pd.DataFrame(rows, columns=["Age","Income","Married","Health","Class"])
# print(df)
# 
# def entropy(cmain):
#     c_ounts=cmain.value_counts()
#     total=c_ounts.sum()
#     ent=0.0
#     for c in c_ounts:
#         p=c/total
#         if p>0:
#             ent-=p*math.log(p,2)
#     return ent
# entropymain=entropy(df["Class"])
# 
# X=["Age","Income","Married","Health"]
# prev_entropy=1.0
# for c in X:
#     groups = df.groupby(df[c])
#     wei_entropy = 0.0
#     for name,grp in groups:
#         e=entropy(grp["Class"])
#         w=len(grp)/len(df)
#         wei_entropy+=w*e
#     print(wei_entropy, f"{c}")
#     if wei_entropy<prev_entropy:
#         prev_entropy=wei_entropy
# 
# info_gain=entropymain-prev_entropy
# print(info_gain)
# 


import pandas as pd
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 
import math

rows = [
    ("Young",  "High",   "No",  "Fair", "No"),
    ("Young",  "High",   "No",  "Good", "No"),
    ("Middle", "High",   "No",  "Fair", "Yes"),
    ("Old",    "Medium", "No",  "Fair", "Yes"),
    ("Old",    "Low",    "Yes", "Fair", "Yes"),
    ("Old",    "Low",    "Yes", "Good", "No"),
    ("Middle", "Low",    "Yes", "Good", "Yes"),
    ("Young",  "Medium", "No",  "Fair", "No"),
    ("Young",  "Low",    "Yes", "Fair", "Yes"),
    ("Old",    "Medium", "No",  "Fair", "Yes"),
    ("Young",  "Medium", "Yes", "Good", "Yes"),
    ("Middle", "Medium", "No",  "Good", "Yes"),
    ("Middle", "High",   "Yes", "Fair", "Yes"),
    ("Old",    "Medium", "No",  "Good", "No"),
]

df=pd.DataFrame(rows,columns=["Age","Income","Married","Health","Class"])

def entropy(cmain):
    ent=0.0
    counts=cmain.value_counts()
    total=counts.sum()
    for c in counts:
        p=c/total
        if p>0:
            ent-=p*math.log(p,2)
    return ent     

entropygain=entropy(df["Class"])

X=["Age","Income","Married","Health"]
prev_ent=1.0
for c in X:
    groups=df.groupby(df[c])
    wei_entro=0.0
    for name,grp in groups:
        e=entropy(grp["Class"])
        w=len(grp)/len(df)
        wei_entro+=w*e
    print(wei_entro,f"{c}")
    if wei_entro<prev_ent:
        prev_ent=wei_entro

infogain=entropygain-prev_ent
print(infogain)





