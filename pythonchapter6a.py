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
  A[4, i]=np.log(returnEQR[i + 1]/returnEQR[i])
  A[5, i]=np.log(returnUAL[i + 1]/returnUAL[i])
