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
