#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('bigram.csv')
#use data from bigram.csv posted on github for jane austen data
m=np.array(data)

num_rows, num_cols=m.shape
wordlist=["miss","anne","poor","marianne","when","replied","with","felt","jane","appeared","cried","but"]
T=np.zeros((len(wordlist),len(wordlist)))

for i in range(0,num_rows):
    if m[i][1] in wordlist and m[i][2] in wordlist:
        T[wordlist.index(m[i][2])][wordlist.index(m[i][1])]=m[i][3]
num_rows,num_cols=T.shape
for i in range(0,num_rows):
    if sum(T[i])!=0:
        T[i]=T[i]/sum(T[i])
initialword="marianne"
sentence=initialword
initial=np.zeros(len(wordlist))
initial[wordlist.index(initialword)]=1
for i in range(0,3):
    ranking=np.linalg.matrix_power(T,i+1).dot(initial)
    sentence=sentence.__add__(" ")
    sentence=sentence.__add__(wordlist[ranking.argmax()])
print(sentence)
#autocorrect part of case study
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
 

 
 
#Initialise HMM
observations=('A','E','R')
V=np.array((0,1,3))
states = ('A', 'E','L','R')
hiddenstates=" "
transition_prob = np.array(((.1,.29,.33,.21),(.17,.18,.40,.36),(.28,.21,.27,.29),(.45,.32,0,.14)))
emission_prob=transition_prob
start_prob=np.array((3/4,1/8,0,1/16))
alpha = forward(V, np.transpose(transition_prob), np.transpose(emission_prob), start_prob)
print("alpha")
print(alpha)
beta = backward(V, np.transpose(transition_prob), np.transpose(emission_prob))
print("beta")
print(beta)
print("gamma")
gamma=alpha[0]*beta[0]/alpha[0].dot(beta[0])
print(gamma)
hiddenstates=hiddenstates.__add__(states[gamma.argmax()])

for i in range(1,3):
    index=gamma.argmax()
    gamma=alpha[i]*beta[i]/alpha[i].dot(beta[i])
    print(gamma)
    p=(np.transpose(emission_prob)[index]*gamma)
    hiddenstates=hiddenstates.__add__(states[p.argmax()])
print("hiddenstates ",hiddenstates)


        
