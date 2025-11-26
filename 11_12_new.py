import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("IRIS.csv")
print(df.head())
#
# num_cols=df.describe().columns
# for x in num_cols:
#     plt.figure(figsize=(10,5))
#     sns.histplot(df[x],bins=20,kde=True)
#     plt.xlabel(f"Histogram with respect to {x}")
#     plt.ylabel("Values")
#     plt.show()
#


#12th Question
sns.boxplot(x="sepal_width",y="petal_width",data=df)
plt.show()

sns.boxplot(x="sepal_width",data=df)
plt.show()

for col in df.select_dtypes(include="number").columns:
    plt.figure()
    plt.boxplot(df[col])
    plt.show()