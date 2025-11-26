import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv('House Data.csv')
print(df.columns)
print(df.describe())