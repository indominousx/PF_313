import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=sns.load_dataset("titanic")
print(df.select_dtypes(include="number").columns)
sns.countplot(x="sex",hue="survived",data=df)
plt.show()

sns.countplot(x="class",hue="survived",data=df)
plt.title("Aisa Hi Timepass")
plt.show()


sns.boxplot(x="class",y="fare",data=df)
plt.show()

#16--------------------------------------------------------------
plt.figure(figsize=(10,10))
sns.histplot(x="fare",bins=30,kde=True,data=df)
plt.xlabel("Fare")
plt.ylabel("Frequency")
plt.show()

