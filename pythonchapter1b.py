#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('project1c.csv') #save datafile in the same file as your .py file
m=np.array(data)

datamatrix=np.transpose(np.delete(np.transpose(m),0,0))

num_rows, num_cols = datamatrix.shape
#ranking1
diagmatrix=np.zeros( (num_rows, num_cols) )
for i in range(0,num_rows):
    diagmatrix[i][i]=datamatrix[i][i]
AE=np.array(datamatrix-diagmatrix)
#netscore represents the percentage of the boundary shared
netscore=np.zeros((num_rows))
for i in range(num_rows):
    netscore[i]=sum(AE[i])
AEstar=AE+np.transpose(AE)+np.eye(num_rows, dtype=int)
ranking1=netscore+AEstar.dot(netscore)
#this adds in the census block numbers and sorts
rankingmatrix1=np.zeros((num_rows,2))
for i in range(num_rows):
    rankingmatrix1[i][0]=m[np.argsort(ranking1)[i]][0]
    rankingmatrix1[i][1]=ranking1[np.argsort(ranking1)[i]]
print(rankingmatrix1)

#ranking 2
adjmatrix=np.zeros((num_rows,num_cols))
for i in range(num_rows):
    for j in range(num_cols):
        if AE[i][j]!=0:
            adjmatrix[i][j]=1
Laplacian=-adjmatrix
for i in range(num_rows):
    Laplacian[i][i]=sum(adjmatrix[i])
values,vectors=np.linalg.eig(Laplacian)
posfiedler=np.argsort(values)[1]
fiedlervector=np.transpose(vectors)[posfiedler]
ranking2=np.sort(fiedlervector)
rankingmatrix2=np.zeros((num_rows,2))
for i in range(num_rows):
    rankingmatrix2[i][0]=m[np.argsort(fiedlervector)[i]][0]
    rankingmatrix2[i][1]=round(ranking2[i],2)
print(rankingmatrix2)

#script to create two subgraphs and apply the Fiedler ranking again
#with the larger of the two lists
g1=[]
g2=[]
temp=[]
for i in range(num_rows):
    if rankingmatrix2[i][1]<0:
        g1=np.append(g1,np.argsort(fiedlervector)[i])
    else:
        g2=np.append(g2,np.argsort(fiedlervector)[i])
if len(g1)>len(g2):
    temp=g1
else:
        temp=g2

tempadj=np.zeros((len(temp),len(temp)))
for i in range(len(temp)):
    for j in range(len(temp)):
        tempadj[i][j]=adjmatrix[int(temp[i])][int(temp[j])]
        
Laplacian2=-tempadj
for i in range(len(temp)):
    Laplacian2[i][i]=sum(tempadj[i])
values2,vectors2=np.linalg.eig(Laplacian2)
posfiedler2=np.argsort(values2)[1]
    
fiedlervector2=np.transpose(vectors2)[posfiedler2]
ranking3=np.sort(fiedlervector2)
rankingmatrix3=np.zeros((len(temp),2))
for i in range(len(temp)):
    rankingmatrix3[i][0]=int(m[int(temp[np.argsort(fiedlervector2)[i]])][0])
    rankingmatrix3[i][1]=round(ranking3[i],2)
print(rankingmatrix3)
