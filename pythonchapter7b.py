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
for i in range (0,16):
  indices=np.append(indices,random.randint(0, n))
  
# the data in birdcalls.zip are from audio calls, we will be looking at discrete fourier transforms of these calls.
for i in range(0,len(indices)):
    birdcall=birdcall=mat[:,i]
    f=np.abs(fft(birdcall))
    xpeaks=np.append(xpeaks,sort_index(f)[0])
    ypeaks=np.append(ypeaks,sort_index(f)[1])

plt.scatter(xpeaks,ypeaks)

