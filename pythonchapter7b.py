import pip
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.fft import fft, ifft
data = pd.read_csv('birdcalls.csv')
mat=np.array(data)

decision=[]

def sort_index(lst, rev=True):
    index = range(len(lst))
    s = sorted(index, reverse=rev, key=lambda i: lst[i])
    return s

# 2n is the number of non Sri Lankan Jungle fowl in the training set, jfn is the number of Sri Lankan Jungle fowl in the training set. This can be changed.
n=10
jfn=4

#Sri Lankan Jungle fowl bird calls are between col1 and col2, in the dataset Sri Lankan Jungle fowl are in columns 17 to 31
col1=17
col2=31
# 5 decision tree runs are made but more can be done.
for run in range(0,5):
    indices=[]
    jfindices=[]
    xpeaks=[]
    ypeaks=[]
    jfxpeaks=[]
    jfypeaks=[]
    xconstraints=[]
    yconstraints=[]
    for i in range (0,n):
      indices=np.append(indices,random.randint(0, col1-1))
    for i in range (0,n):
      indices=np.append(indices,random.randint(col2+1,mat.shape[1]-1))
    for i in range (0,jfn):
      jfindices=np.append(jfindices,random.randint(col1, col2))

    for i in range(0,len(indices)):
        birdcall=mat[:,int(indices[i])]
        f=np.abs(fft(birdcall))
        xpeaks=np.append(xpeaks,sort_index(f)[0]/1000)
        ypeaks=np.append(ypeaks,(sort_index(f)[1]-sort_index(f)[0])/sort_index(f)[0])
    for i in range(0,len(jfindices)):
        birdcall=mat[:,int(jfindices[i])]
        f=np.abs(fft(birdcall))
        jfxpeaks=np.append(jfxpeaks,sort_index(f)[0]/1000)
        jfypeaks=np.append(jfypeaks,(sort_index(f)[1]-sort_index(f)[0])/sort_index(f)[0])
    xconstraints=np.append(xconstraints,[np.min(jfxpeaks),np.max(jfxpeaks)])
    yconstraints=np.append(yconstraints,[np.min(jfypeaks),np.max(jfypeaks)])

#now a test case from the jungle fowl data
    birdcall=mat[:,int(random.randint(col1, col2))]
    f=np.abs(fft(birdcall))
    x=sort_index(f)[0]/1000
    y=(sort_index(f)[1]-sort_index(f)[0])/sort_index(f)[0]
    if x > xconstraints[0] and x < xconstraints[1] and y > yconstraints[0] and y < yconstraints[1]:
        decision=np.append(decision,True)
    else:
        decision=np.append(decision,False)
    
if np.count_nonzero(decision ==1) >= np.count_nonzero(decision ==0):
    print("Bird is a Sri Lankan Jungle Fowl")
else:
    print("Bird is not a Sri Lankan Jungle Fowl")

# if at any point you wish to see a scatterplot
plt.scatter(xpeaks,ypeaks)
plt.scatter(jfxpeaks,jfypeaks,color='r')
