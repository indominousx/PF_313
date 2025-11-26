import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import math

df=pd.read_csv("Lipstick.csv")
print(df.head())

def entropy(cmain):
    ent=0.0
    counts=cmain.value_counts()
    total=counts.sum()
    for c in counts:
        p=c/total
        if p>0:
            ent-=p*math.log(p,2)
    return ent

entropygain=entropy(df["Buys"])

X=["Age","Income","Gender","Ms"]
prev_ent=1.0
for c in X:
    wei_ent=0.0
    groups=df.groupby(df[c])
    for name,grp in groups:
        e=entropy(grp["Buys"])
        w=len(grp)/len(df)
        wei_ent+=w*e
    print(wei_ent,f"{c}")

    if wei_ent<prev_ent:
        prev_ent=wei_ent

info_gain= entropygain-prev_ent
print(info_gain)
