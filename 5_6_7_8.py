import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

df=pd.read_csv("Lipstick.csv")
print(df)
le_age=LabelEncoder()
le_income=LabelEncoder()
le_gender=LabelEncoder()
le_ms=LabelEncoder()
le_buys=LabelEncoder()

df["Age"]=le_age.fit_transform(df["Age"])
df["Income"]=le_income.fit_transform(df["Income"])
df["Gender"]=le_gender.fit_transform(df["Gender"])
df["Ms"]=le_ms.fit_transform(df["Ms"])
df["Buys"]=le_buys.fit_transform(df["Buys"])

model=DecisionTreeClassifier(criterion="entropy")
X=df[["Age","Income","Gender","Ms"]]
Y=df["Buys"]

X_train, X_test, Y_train, Y_test=train_test_split(X, Y,)
model.fit(X_train,Y_train)

X_test=pd.DataFrame([{
    "Age":"<21",
    "Income":"Low",
    "Gender":"Female",
    "Ms":"Married"
}])


X_test["Age"]=le_age.fit_transform(X_test["Age"])
X_test["Income"]=le_income.fit_transform(X_test["Income"])
X_test["Gender"]=le_gender.fit_transform(X_test["Gender"])
X_test["Ms"]=le_ms.fit_transform(X_test["Ms"])

X_test2=pd.DataFrame([{
    "Age":">35",
    "Income":"Medium",
    "Gender":"Female",
    "Ms":"Married"
}])

X_test2["Age"]=le_age.fit_transform(X_test2["Age"])
X_test2["Income"]=le_age.fit_transform(X_test2["Income"])
X_test2["Gender"]=le_gender.fit_transform(X_test2["Gender"])
X_test2["Ms"]=le_ms.fit_transform(X_test2["Ms"])


prediction=model.predict(X_test)[0]
pre_label=le_buys.inverse_transform([prediction])[0]
print("\n",pre_label)

prediction2=model.predict(X_test2)[0]
pre_label2=le_buys.inverse_transform([prediction2])[0]
print("\n",pre_label2)