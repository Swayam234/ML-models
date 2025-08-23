import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("C:\git demo\ML projects\Mall_Customers (2).csv")
df
df.info()
x=df.iloc[:,3:]
x

# Initial data visualization
plt.title("Unclustered data")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.scatter(x["Annual Income (k$)"],x["Spending Score (1-100)"])

from sklearn.cluster import KMeans
km=KMeans(n_clusters=6)
x.shape
km.fit_predict(x)

km.inertia_  #sum squared errors affect the value of inertia
SSE=[]
for i in range(1,16):
  km=KMeans(n_clusters=i)
  km.fit_predict(x)
  SSE.append(km.inertia_)
SSE

#Elbow Method
plt.title("Elbow Method")
plt.xlabel("Number of Clusters")
plt.ylabel("SSE")
plt.grid()
plt.xticks(range(1,16))
plt.plot(range(1,16),SSE,marker=".",color="red")
km=KMeans(n_clusters=5,random_state=2)
label=km.fit_predict(x)
km.fit

# Data Visualization without centroids
plt.figure(figsize=(10,6))
plt.title("Clustered Data")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.scatter(x["Annual Income (k$)"],x["Spending Score (1-100)"],c=label)
km.cluster_centers_
cent=km.cluster_centers_

# Data visualization with centroids
plt.figure(figsize=(16,9))
plt.title("Clustered data")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.scatter(x["Annual Income (k$)"],x["Spending Score (1-100)"],c=label)
plt.scatter(cent[:,0],cent[:,1],color="red")