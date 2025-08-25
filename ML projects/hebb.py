import numpy as np

#Bipolar input for AND gate
inputs = np.array([
                 [-1,-1],
                 [-1,1],
                 [1,-1],
                 [1,1]
])

#Bipolar target values
targets=np.array([-1,-1,-1,1])

#Weights and bias initialization
weights = np.zeros(2)
bias = 0
print("Initial weights",weights)
print("Initial bais",bias)

#Hebbian learning rule
for i in range(len(inputs)):
  x=inputs[i]
  y=targets[i]
  weights+=x*y
  bias+=y
  print("\n Trained weights",weights)
  print("\n Trained bias",bias)
  
def predict(x):
  net=np.dot(x,weights)+bias
  if net>0:
    return 1
  else:
    return -1

#Testing model
print("\n Testing Hebbian Model with AND truth table")
for i in range(len(inputs)):
  pred=predict(inputs[i])
  print(pred)