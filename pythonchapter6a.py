import pip
import pandas as pd
import numpy as np
data = pd.read_csv('stockreturn.csv')
mat=np.array(data)

returnAAL=[]
returndAL=[]
returnUAL=[]
returnABBV=[]
returnCBG=[]
returnEQR=[]

for i in range(1,600000):
    if mat[i, 6] == "AAL":
        returnAAL=np.append(returnAAL, mat[i, 4])
    if mat[i, 6] == "ABBV":
        returnABBV=np.append(returnABBV, mat[i, 4])
    if mat[i, 6] == "DAL":
        returndAL=np.append(returndAL, mat[i, 4])
    if mat[i, 6] == "UAL":
        returnUAL=np.append(returnUAL, mat[i, 4])
    if mat[i, 6] == "CBG":
        returnCBG=np.append(returnCBG, mat[i, 4])
    if mat[i, 6] == "EQR":
        returnEQR=np.append(returnEQR, mat[i, 4])
x=np.arange(0,len(returnAAL))
plt.scatter(x,returnAAL)

A=np.zeros((6,len(returnAAL)-1))
for i in range(1,len(returnAAL)-1):
  A[0, i]=np.log(returnAAL[i + 1]/returnAAL[i])
  A[1, i]=np.log(returnABBV[i + 1]/returnABBV[i])
  A[2, i]=np.log(returnCBG[i + 1]/returnCBG[i])
  A[3, i]=np.log(returndAL[i + 1]/returndAL[i])
    
plt.hist(flist)

#average 7 day

avg1=[]
avg2=[]
temp=np.zeros(30)
temp1=np.zeros(30)
for time in range(0,1090):
    for i in range(0,30):
        temp[i]=avg[i - 1 + time]
        temp1[i]=mlist[i - 1 + time]
        avg1=np.append(avg1,np.mean(temp))
        avg2=np.append(avg2,np.mean(temp1))
       
  A[4, i]=np.log(returnEQR[i + 1]/returnEQR[i])
  A[5, i]=np.log(returnUAL[i + 1]/returnUAL[i])

elist =[]
mlist = []
flist = []
avg = []
for time in range(0,1200):
    Temp=np.zeros((6,6))
    for i in range(0,6):
        for j in range(0,6):
            Temp[i,j]=A[i,j+time-1]
    W=Temp.dot(np.transpose(Temp))/np.sqrt(2*6)
    Stime=np.transpose(Temp).dot(Temp)/np.sqrt(2*6)
    H1=(W + np.transpose(W))/6
    w,v=np.linalg.eig(H1)
    elist=np.append(elist, np.mean(v))
    w,v=np.linalg.eig(Stime)
    mlist=np.append(mlist, np.max(v))
    w,v=np.linalg.eig(W)
    flist=np.append(flist, np.mean(v))
    avg = np.append(avg, np.mean(Stime[1]))
