import pip
import pandas as pd
import numpy as np
import statistics
import matplotlib.pyplot as plt

def newton_poly(coef, x_data, x):
#    evaluate the newton polynomial  at x
    n = len(x_data) - 1 
    p = coef[n]
    for k in range(1,n+1):
        p = coef[n-k] + (x -x_data[n-k])*p
    return p
def lu(A):
    
    # Return an error if matrix is not square
    if not A.shape[0]==A.shape[1]:
        raise ValueError("Input matrix must be square")

    n = A.shape[0] 

    L = np.zeros((n,n),dtype='float64') 
    U = np.zeros((n,n),dtype='float64') 
    U[:] = A 
    np.fill_diagonal(L,1) # fill the diagonal of L with 1

    for i in range(n-1):
        for j in range(i+1,n):
            L[j,i] = U[j,i]/U[i,i]
            U[j,i:] = U[j,i:]-L[j,i]*U[i,i:]
            U[j,i] = 0
    return (L,U)

A=np.array([[1,37.5,57.21,9.5],[1,6.83,36.33,5.7],[1,11.25,38.32,4.8],[1,28.21,41.86,72.6]])
b=np.array([30.7,15.3,12.16,23.75])
coef=np.linalg.inv(np.transpose(A).dot(A)).dot(np.transpose(A)).dot(b)
print(coef)

x_data = np.array([6.6, 12, 15, 58.5])
y_data = np.array([45.6, 105.5, 69.7, 53.5])
Vstar=np.vander(x_data,4,increasing=True)
L=lu(Vstar)[0]
U=lu(Vstar)[1]
dd=np.zeros([len(Vstar)])
for i in range(0,len(Vstar)):
    dd[i]=(np.linalg.inv(L).dot(y_data))[i]*(np.linalg.inv(U))[i,i]
y_new=newton_poly(dd,x_data,x_data)
plt.scatter(x_data,y_data,color="purple")
plt.plot(x_data, y_new)
plt.show()

A=np.array([[1.,69883.,0.269484],[1.,25802.,0.130347],[1.,17332.,0.296852],[1.,22108.,0.171374],
[1,49248.,0.151853],[1,52136.,0.265944],[1.,22492.,0.403457],[1.,65090.,0.143834],[1.,27680.,0.447641],
[1.,28604.,0.235673],[1.,71200.,0.314642],[1.,35636.,0.253052]])
b=np.array([0.8, 0.634, 0.725, 0.741, 0.743, 0.192, 0.5314, 0.848, 0.7986,0.7105, 0.9422, 0.8818])
coef=np.linalg.inv(np.transpose(A).dot(A)).dot(np.transpose(A)).dot(b)
print(coef)
div = np.zeros([A.shape[0], A.shape[1]])
for i in range(0,A.shape[0]):
    for j in range(0,A.shape[1]):
        if j < A.shape[1]-1:
            div[i][j]=(A[i,j+1]-statistics.mean(A[:,j+1]))/statistics.stdev(A[:,j+1])
        else:
            div[i][j]=(b[i]-statistics.mean(b))/statistics.stdev(b)
u,s,vt=np.linalg.svd(div)
label =['Carnegie', 'Clemson', 'James Madison', 'HPU', 'New England', 'Old Dominion',
'Providence', 'Rutgers', 'UConn','Penn','William&Mary']
xcoord=u[:,0]
ycoord=u[:,1]
plt.figure(figsize=(10,10))
plt.scatter(u[:,0],u[:,1])
plt.xlabel('pc1')
plt.ylabel('pc2')
for i, label in enumerate (label):
    plt.text(xcoord[i], ycoord[i], label)