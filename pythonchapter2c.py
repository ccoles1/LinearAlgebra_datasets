#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
import csv
import re
#import nltk #natural language toolkit


np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('tweets.csv')
market=pd.read_csv('s_n_p_data_1920.csv')
m=np.array(data)
mydata=np.zeros(9)
#extracting the date from tweet
with open('tweets.csv', newline='') as f:
  for j in range(0,m.shape[0]):
        datemarker1=''
        reader = csv.reader(f)
        row1 = next(reader)
        word_list = str(row1).split()
        datepiece=word_list[-2]
        datemarker1=datemarker1.__add__(datepiece[-10:-8])
        datemarker1=datemarker1.__add__("/")
        datemarker1=datemarker1.__add__(datepiece[-7:-5])
        datemarker1=datemarker1.__add__("/")
        if datepiece[-1]=='0':
            datemarker1=datemarker1.__add__('2020')
        if datepiece[-1]=='9':
            datemarker1=datemarker1.__add__('2019')
        print(datemarker1)
        #matching the tweet date to the market data
        with open('marketdata1920.csv', newline='') as g:
          for i in range(1,232):
              reader = csv.reader(g)
              row1 = next(reader)
              word_list = str(row1).split()
              datepiece=word_list[0]
              if datepiece[3]=='/':
                  datemarker2='0'
                  datemarker2=datemarker2.__add__(datepiece[2:11])
              else:
                  datemarker2=datepiece[2:12]
              if datemarker1 ==datemarker2:
                  mydata=np.append(mydata,[datemarker2,row1[1],row1[2],row1[3],row1[4], row1[5],row1[6],row1[7],'Bull'])

#for row in reader:
#    print(row)
   # word_list = str(row).split()
   # datepiece=word_list[-2]
   # print(datepiece[-10:-1])

#forward backward algorithm
def forward(V, a, b, initial_distribution):
    alpha = np.zeros((V.shape[0], a.shape[0]))
    alpha[0, :] = initial_distribution * b[:, V[0]]
 
    for t in range(1, V.shape[0]):
        for j in range(a.shape[0]):
            alpha[t, j] = alpha[t - 1].dot(a[:, j]) * b[j, V[t]]
 
    return alpha

def backward(V, a, b):
    beta = np.zeros((V.shape[0], a.shape[0]))

    beta[V.shape[0] - 1] = np.ones((a.shape[0]))
    for t in range(V.shape[0] - 2, -1, -1):
        for j in range(a.shape[0]):
            beta[t, j] = (beta[t + 1] * b[:, V[t + 1]]).dot(a[j, :])
 
    return beta

 #baum-welch algorithm
def baumwelch(V, a, b, initial_distribution, n_iter):
    M = a.shape[0]
    T = len(V)
 
    for n in range(n_iter):
        alpha = forward(V, a, b, initial_distribution)
        beta = backward(V, a, b)
 
        xi = np.zeros((M, M, T - 1))
        for t in range(T - 1):
            denominator = np.dot(np.dot(alpha[t, :].T, a) * b[:, V[t + 1]].T, beta[t + 1, :])
            for i in range(M):
                numerator = alpha[t, i] * a[i, :] * b[:, V[t + 1]].T * beta[t + 1, :].T
                xi[i, :, t] = numerator / denominator
 
        gamma = np.sum(xi, axis=1)
    
        a = np.sum(xi, 2) / np.sum(gamma, axis=1).reshape((-1, 1))

        gamma = np.hstack((gamma, np.sum(xi[:, :, T - 2], axis=0).reshape((-1, 1))))
 
        K = b.shape[1]
        denominator = np.sum(gamma, axis=1)
        for l in range(K):
            b[:, l] = np.sum(gamma[:, V == l], axis=1)
 
        b = np.divide(b, denominator.reshape((-1, 1)))
 
    return {"T":np.transpose(a), "E":np.transpose(b)}

#Initialise HMM
observations=('Bull','Bull','Bull')
V=np.array((0,0,0))
states = ('U','D')
hiddenstates=" "
transition_prob = np.array(((1/3,3/4),(2/3,1/4)))
emission_prob=np.array(((1,4/5),(0,1/5)))
start_prob=np.array((.5,.5))
alpha = forward(V, np.transpose(transition_prob), np.transpose(emission_prob), start_prob)
print("alpha")
print(alpha)
beta = backward(V, np.transpose(transition_prob), np.transpose(emission_prob))
print("beta")
print(beta)
print("gamma")
gamma=alpha[0]*beta[0]/alpha[0].dot(beta[0])
print(gamma)
pi=gamma
hiddenstates=hiddenstates.__add__(states[gamma.argmax()])

for i in range(1,3):
    index=gamma.argmax()
    gamma=alpha[i]*beta[i]/alpha[i].dot(beta[i])
    print(gamma)
    p=(np.transpose(emission_prob)[index]*gamma)
    hiddenstates=hiddenstates.__add__(states[p.argmax()])
print("hiddenstates ",hiddenstates)

#baum-welch
new=baumwelch(V, np.transpose(transition_prob), np.transpose(emission_prob),start_prob,1)
print(new)
