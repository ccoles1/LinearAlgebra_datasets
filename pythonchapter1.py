#!C:\Python37\python.exe
import pip
import pandas as pd
import numpy as np
np.set_printoptions(suppress=True)#suppresses scinotation
data = pd.read_csv('project1sports.csv') #save datafile in the same file as your .py file
m=np.array(data)
sec=np.transpose(np.delete(np.transpose(m),0,0))
diff=-sec
wins=[]
num_rows, num_cols = sec.shape
#ranking1
diagmatrix=np.zeros( (num_rows, num_cols) )
for i in range(0,num_rows):
    wini=0
    for j in range(0,num_cols):
        diff[i][j]=m[i][j+1]-m[j][i+1]
        if diff[i][j]>0:
            wini=wini+1
        if sec[i][j]!=0:
            sec[i][j]=1
            sec[j][i]=1
    wins=np.append(wins,wini)

#using powers of a matrix to rank teams
gamecounter=[]
for i in range(num_rows):
    counter=0
    for j in range(num_cols):
        if sec[i][j]==0:
            counter=counter+1
    gamecounter=np.append(gamecounter,num_cols-counter)
#this nested loop will determine how many nonzero scores a
#team has and stores it in gamecounter

#this for loop creates a netscore vector based on the scores
#note that if a team loses a game then the entry will be neg

netscore=np.zeros((num_rows))
for i in range(num_rows):
    netscore[i]=sum(diff[i])/gamecounter[i]
newmatrix=sec+np.eye(num_rows, dtype=int)
ranking1=netscore+newmatrix.dot(netscore)+np.linalg.matrix_power(newmatrix,2).dot(netscore)
rankingmatrix1=[]
for i in range(num_rows):
    rankingmatrix1=np.append(rankingmatrix1,[m[np.argsort(ranking1)[i]][0],ranking1[np.argsort(ranking1)[i]]])
print(rankingmatrix1)
#ranking2, using eigenvalues to rank teams
newmatrix2=np.zeros((num_rows,num_cols))
num_rows, num_cols=newmatrix2.shape
for i in range(num_rows):
    for j in range(num_cols):
        if sec[i][j]!=0:
            newmatrix2[i][j]=m[i][j+1]/(m[i][j+1]+m[j][i+1])
values,vectors=np.linalg.eig(newmatrix2)
maxpos=0
#finds the maximum eigenvalue
for i in range(num_rows):
    if np.argsort(np.abs(values))[i]==num_rows-1:
        maxpos=i
maxvector=np.abs(np.transpose(np.transpose(vectors)[maxpos]))
maxvector=np.round(maxvector/np.linalg.norm(maxvector),3)
#Re takes the real part of an entry, eliminate if you
#expect complex eigenvalues and eigenvectors
#find the eigenvector associated with the max eigenvector
ranking2=maxvector
rankingmatrix2=[]
for i in range(num_rows):
    rankingmatrix2=np.append(rankingmatrix2,[m[np.argsort(ranking2)[i]][0],ranking2[np.argsort(ranking2)[i]]])
print(rankingmatrix2)

#ranking3,Colley matrix ranking
Colley=np.zeros((num_rows,num_cols))
for i in range(num_rows):
    for j in range(num_cols):
        if i!=j:
            Colley[i][j]=-sec[i][j]
        if i==j:
            Colley[i][j]=2+sum(sec[i])

b=np.zeros((num_rows,1))
for i in range(len(wins)):
    b[i]=1+.5*(wins[i]-(gamecounter[i]-wins[i]))
ranking3=np.zeros((1,num_rows))
for i in range(num_rows):
    ranking3[0][i]=np.transpose(np.round(np.linalg.solve(Colley,b),3))[0][i]
rankingmatrix3=[]
for i in range(num_rows):
    rankingmatrix3=np.append(rankingmatrix3,[m[np.argsort(ranking3)[0][i]][0],ranking3[0][np.argsort(ranking3)[0][i]]])
print(rankingmatrix3)
