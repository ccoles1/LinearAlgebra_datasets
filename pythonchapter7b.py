import pip
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
data = pd.read_csv('birdcalls1.csv')
mat=np.array(data)

#this function helps find indices of the largest peaks in the discrete fourier transform of the calls
def sort_index(lst, rev=True):
    index = range(len(lst))
    s = sorted(index, reverse=rev, key=lambda i: lst[i])
    return s
  
#choose a training set, this will include 20 calls, at least 4 samples from sri lanka jungle fowl
indices=[]
xpeaks=[]
ypeaks=[]
n=10
jfn=4

#Sri Lankan Jungle fowl bird calls are between col1 and col2
col1=3
col2=7
for i in range (0,n):
  indices=np.append(indices,random.randint(0, col1-1))
for i in range (0,n):
  indices=np.append(indices,random.randint(col2+1,mat.shape[1]-1))
for i in range (0,jfn):
  jfindices=np.append(jfindices,random.randint(col1, col2))
  
# the data in birdcalls.zip are from audio calls, we will be looking at discrete fourier transforms of these calls.
for i in range(0,len(indices)):
    birdcall=mat[:,int(indices[i])]
    f=np.abs(fft(birdcall))
    xpeaks=np.append(xpeaks,sort_index(f)[0])
    ypeaks=np.append(ypeaks,sort_index(f)[1])
for i in range(0,len(jfindices)):
    birdcall=mat[:,int(jfindices[i])]
    f=np.abs(fft(birdcall))
    jfxpeaks=np.append(jfxpeaks,sort_index(f)[0]/1000)
    jfypeaks=np.append(jfypeaks,(sort_index(f)[1]-sort_index(f)[0])/sort_index(f)[0])

plt.scatter(xpeaks,ypeaks)
plt.scatter(jfxpeaks,jfypeaks,color='r')

xconstraints=[]
xconstraints=np.append(xconstraints,[np.min(jfxpeaks),np.max(jfxpeaks)])
yconstraints=[]
yconstraints=np.append(yconstraints,[np.min(jfypeaks),np.max(jfypeaks)])

#now a test case from the jungle fowl data
