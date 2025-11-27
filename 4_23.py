import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
import math

df=pd.read_csv("Lipstick.csv")
print(df)

def entropy(cmain):
    counts=cmain.value_counts()
    total=counts.sum()
    ent=0.0
    for c in counts:
        p=c/total
        if p>0:
            ent-=p*math.log(p,2)
    return ent

entropygain=entropy(df["Buys"])

X=["Age","Income","Gender","Ms"]
prev_entropy=1.0
for x in X:
    groups=df.groupby(df[x])
    wei_entropy=0.0
    for name,grp in groups:
        e=entropy(grp["Buys"])
        w=len(grp)/len(df)
        wei_entropy+=w*e
    print(wei_entropy,f"{x}")
    if wei_entropy<prev_entropy:
        prev_entropy=wei_entropy

information_gain = entropygain-prev_entropy
print(information_gain)

