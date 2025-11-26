import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv("IRIS.csv")
print(df.describe())
print(df.dtypes)

df.hist(figsize=(10,10),bins=15)
plt.suptitle("Feature Showcase")
plt.show()


plt.figure(figsize=(10,10))
df.boxplot()
plt.show()


import matplotlib.pyplot as plt

for col in df.select_dtypes(include='number').columns:
    plt.figure()
    plt.boxplot(df[col])
    plt.title(f"Boxplot of {col}")
    plt.show()

sns.boxplot(x="sepal_width",data=df)
plt.title("Boxplot")

plt.show()