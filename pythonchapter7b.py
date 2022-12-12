import pip
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import matplotlib.mlab as mlab
f = open('GSE13598.txt','r')
lines = []
with open('GSE13598.txt') as f:
    lines = f.readlines()
    lines=[]
with open('GSE13598.txt') as f:
    for line in f:
        lines=[line.rstrip() for line in f]
        newline=[]
for i in range(0,len(lines)):
    line=lines[i]
    loc=line.find('Type')
    word1=line[0:loc].split()[0]
    word2=line[0:loc].split()[1]
    if (word1 not in newline) and ('/' not in word1):
        newline=np.append(newline,word1)
    if (word2 not in newline) and ('/' not in word2):
        newline=np.append(newline,word2)
M=np.zeros([len(newline),len(newline)])
for i in range(0,len(lines)):
    line=lines[i]
    loc=line.find('Type')
    word1=line[0:loc].split()[0]
    word2=line[0:loc].split()[1]
    if ('/' not in word1) and ('/' not in word2):
        idx1=list(newline).index(word1)
        idx2=list(newline).index(word2)
        M[idx1,idx2]=1
M=M+np.transpose(M)

for i in range(0,M.shape[0]):
    for j in range(0,M.shape[1]):
        if M[i,j]>1:
            M[i,j]=1
            
#creating an output txt file
f = open("outfile.txt","w")
for row in M:
    for el in row:
        f.write("%.4f" %el + ' ')
    f.write('\n')
f.close()

#drawing an adjacency graph
labeldict = {}
import networkx as nx 
G = nx.DiGraph() 
for i in range(1100,1120): 
    labeldict[i]=newline[i]
    for j in range(1100,1120): 
        if M[i][j] == 1: 
            G.add_edge(i,j) 
nx.draw_circular(G,labels=labeldict,font_size=8,node_size=1400,node_color='lightgray') 
plt.savefig('genegraph.eps') 

#average spacing over n consecutive eigenvalues
w,v=np.linalg.eig(M)
sorted=np.sort(np.abs(w))
n=30
avgspacing=[]
for j in range(0,6*n):
    spacing=np.zeros(n)
    for i in range(0,n):
        spacing[i]=sorted[i+1+(n-1)*j]-sorted[i+(n-1)*j]
    avg=np.sum(spacing)/n
    avgspacing=np.append(avgspacing,avg)
    
fig = plt.figure()
ax = fig.add_subplot(111)
ax.hist(avgspacing, bins=7,color='lightgray',edgecolor='black', weights=np.ones_like(avgspacing)*100 / len(avgspacing))
ax.yaxis.set_major_formatter(PercentFormatter())
plt.xlabel('Eigenvalue Average Spacing')
plt.ylabel('Frequency')
