import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
cases=np.array([607,576,638,615,655,536,358,539,432,460,445,428,448,367,470,401])
x=np.array(range(1,len(cases)+1))
y=np.zeros(len(x))
for i in range(0,len(y)):
    y[i]=cases[0]
    for j in range(0,i):
        y[i]=y[i]+cases[j]
a0=np.array([5.5,.4])
steps=4
for i in range(0,steps):
#plotting the model
    xsmall=np.linspace(1,5,10)
    plt.scatter(x[0:5],y[0:5])
    plt.plot(xsmall,np.exp(a0[0]+a0[1]*xsmall),label=i)
    A=np.zeros([len(y),2])
    W=np.zeros([len(y),len(y)])
    for i in range(0,len(y)):
        A[i,0]=1
        A[i,1]=x[i]
        W[i,i]=np.exp(a0[0]+a0[1]*x[i])
    gradients=np.transpose(A).dot(y)-np.transpose(A).dot(np.exp(A.dot(a0)))
    H=np.transpose(A).dot(W).dot(A)
    a0=a0-np.linalg.inv(H).dot(gradients)
plt.legend()
plt.show()
