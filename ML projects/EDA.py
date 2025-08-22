from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
df=pd.read_csv("C:/git demo/ML projects/Heart (1).csv")
df.head()
df.shape
df.isnull().sum()
df.count()
df==0
(df==0).sum()
df['Age'].mean()
df.columns
data=df[['Age','Sex','ChestPain','RestBP','Chol']]
train,test=train_test_split(data,test_size=0.25,random_state=0)
train.shape
test.shape
actual=list(np.ones(45))+list(np.zeros(55))
np.array(actual)
predicted=np.concatenate((np.ones(40),np.zeros(52),np.ones(8)))
predicted
from sklearn.metrics import ConfusionMatrixDisplay
ConfusionMatrixDisplay.from_predictions(actual,predicted)
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
print(classification_report(actual,predicted))
accuracy_score(actual,predicted)