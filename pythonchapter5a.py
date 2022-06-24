# Start coding h# Import necessary modules
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import math
from math import exp
# Load the digits dataset: digits
digits = datasets.load_digits()
X = digits.data
y = digits.target
data = np.zeros([64,1])
for i in range(0,64):
    data[i]=X[226][i]
subscriptlist=np.array([0,1,2,3,4,20,21,22,23,24,209,210,214,213,215])


# pick a sample to plot

w=np.zeros([15,1])
for i in range(0,15):
    w[i]=1/15
train=np.zeros([len(subscriptlist),64])
for j in range(0,len(subscriptlist)):
        train[j]=X[subscriptlist[j]]
train=np.transpose(train)

def phi(x):
#sigmoid activation function
    return 1/(1+math.exp(-x))
# hyperbolic tan activation function
#    return np.tanh(x)

def phiprime(x):
#derivative of sigmoid activation function
    return math.exp(-x)/((1+math.exp(-x))*(1+math.exp(-x)))
# derivative hyperbolic tan activation function
#    return 1/np.cosh(x)*1/np.cosh(x)

def softmax(x):
    return np.exp(x)/np.sum(np.exp(x))

def cross_entropy(actual, predicted):
    loss=-np.sum(actual*np.log(predicted))
    return loss

phimatrix=np.zeros([64,1])
phiprimematrix=np.zeros([64,1])
diff=np.zeros([64,1])
yhat=np.array([64,1])
yhat=train.dot(w)
check=train.dot(w)
partials=np.zeros([subscriptlist.shape[0]+1])
softpartial=np.zeros([subscriptlist.shape[0]+1])   
r=.03
for k in range(0,64):
    actual=np.zeros([64,1])
    actual[k]=1
    for steps in range(0,1):
#        for i in range(0,64):
#            phimatrix[i]=phi(train.dot(w)[i])
#            phiprimematrix[i]=phiprime(train.dot(w)[i])
 
 #   for i in range(0,64):
 #       diff[i]= (data[i]-phimatrix[i])[0]
        diff=data-softmax(train.dot(w))
 #   partial derivatives when cost function is SSE
 #   partial derivatives when cost function is cross-entropy, cpartials
        partials=np.transpose(train).dot(softmax(train.dot(w))-data)
#    partials=np.transpose(train).dot(np.multiply(phiprimematrix,diff))
        cpartials=partials
        
        for i in range(0,15):
#        w[i] = w[i] -(2*r * partials)[i]
             w[i] = w[i] -(r * cpartials)[i]
# if you want w to be a percentage weight vector, let w=w/sum(w)
        w=w/sum(w)
        yhat=softmax(train.dot(w))
 #   SSE=(np.transpose(phimatrix-data)).dot(phimatrix-data)
        cerror=cross_entropy(actual, yhat)
  print(w)
