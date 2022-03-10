#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt


#np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('starhusbandbook.csv') #save datafile in the same file as your .py file
m=np.array(data)

starhusband=np.array(np.transpose(np.delete(np.transpose(m),[0,1],0)))

num_rows, num_cols = starhusband.shape

S=np.array(starhusband.dot(np.transpose(starhusband)))
gramian=np.zeros((num_rows,num_rows))
for i in range(num_rows):
    for j in range(num_rows):
        gramian[i][j]=S[i][j]
    
values,vectors=np.linalg.eig(gramian)
pos1=np.argsort(values)[0]
pos2=np.argsort(values)[1]
pc1=np.real(vectors[pos1])
pc2=np.real(vectors[pos2])
tribes=np.transpose(m)[1]

# Plot
plt.scatter(pc1, pc2)
tick=tribes
for i,tick in enumerate(tick):
    x = pc1[i]
    y = pc2[i]
    plt.scatter(x, y)
    plt.text(x, y, tick, fontsize=11)
plt.show()

