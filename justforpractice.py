import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df=sns.load_dataset("iris")
cols=df.drop("species",axis=1).columns.tolist()
print(cols)