import pip
import pandas as pd
import numpy as np
from scipy.linalg import svd
import matplotlib.pyplot as plt
from itertools import combinations
data = pd.read_csv('words.csv')
m=np.array(data)
ncol=m.shape[0]
m=m[:,0:ncol]
temp=list()
for i in range(0,209453):
    if len(m[i,0])==5:
        temp.append(m[i,0])
for i in range(209455,len(m)):
    if len(m[i,0])==5:
        temp.append(m[i,0])
# There are 496918 words in this list, 15902 of which are with 5 letters
#guess='tares'
#guess='saree'
guess='zesty'
index = [0,1,2,3,4,5]
countmatch=np.zeros([6,6])
matches=list()
for i in range(0,6):
    for j in range(0,6):
        matches.append([i,j])
for i in range(0,len(temp)):
    check1=0
    check2=0
    for j in range(0,5):
        if temp[i].find(guess[j]) >= 0 and temp[i].find(guess[j]) is not j :
            check1 = check1 + 1
        if temp[i].find(guess[j]) == j:
            check2 =check2+1
    countmatch[check2,check1]=countmatch[check2,check1]+1
# showing the probability distribution of outcomes for the given guess
listmatch=" ".join(str(e) for e in matches)

prob=countmatch/len(temp)
plist=np.concatenate(prob)
sorted=np.sort(plist)
fig = plt.figure()
plt.bar(np.arange(len(plist)),sorted[::-1],color='gray')
plt.show()

# determining the entropy based on the probability distribution of the outcomes
entropy=0
for k in range(0,len(plist)):
    if plist[k]>0:
        entropy=entropy-plist[k]*np.log2(plist[k])
print(guess," ",entropy)
