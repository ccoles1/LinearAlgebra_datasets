#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
#%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt


#np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('faces.csv') #save datafile in the same file as your .py file
m=np.array(data)

faces=np.array(np.transpose(np.delete(np.transpose(m),[0,1],0)))

num_rows, num_cols = faces.shape

S=np.array(np.transpose(faces).dot(faces)

values,vectors=np.linalg.eig(faces)
pos1=np.argsort(values)[0]
pos2=np.argsort(values)[1]
pc1=np.real(vectors[pos1])
pc2=np.real(vectors[pos2])
names=np.transpose(m)[1]

# Plot
plt.scatter(pc1, pc2)
tick=names
for i,tick in enumerate(tick):
    x = pc1[i]
    y = pc2[i]
    plt.scatter(x, y)
    plt.text(x, y, tick, fontsize=11)
plt.show()

