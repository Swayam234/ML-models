import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
data=pd.read_csv("C:/ML-models/ML projects/temperatures (4).csv")
data.head()
data.tail()
data.shape
column=data
count=column[column==0].count()
print(count)
data.isnull().sum()
data.isnull().head()
data.info()
data.head()
x=data[["YEAR"]]
y=data["ANNUAL"]
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
plt.title("Temperature Plot of India")
plt.xlabel("Year")
plt.ylabel("Temperature")
plt.scatter(x,y)
x_train.shape
x_test.shape
model=LinearRegression()
model.coef_
model.intercept_
model.score(x_test,y_test)
model.predict(np.array([[2018]]))
