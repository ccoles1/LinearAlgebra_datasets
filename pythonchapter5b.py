import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
#y=np.array([607,576,638,615,655,536,358,539,432,460,445,428,448,367,470,401])
#x=np.array(range(0,len(y)))
y=np.array([607,576,638,61,655])
x=np.array(range(0,len(y)))
a0=np.array([5.5,.4])
steps=3
for i in range(0,steps):
    #plotting the model
    plt.scatter(x,y)
    plt.plot(x,np.exp(a0[0]+a0[1]*x))
    A=np.zeros([len(y),2])
    W=np.zeros([len(y),len(y)])
    for i in range(0,len(y)):
        A[i,0]=1
        A[i,1]=x[i]
        W[i,i]=np.exp(a0[0]+a0[1]*x[i])
    gradients=np.transpose(A).dot(y)-np.transpose(A).dot(np.exp(A.dot(a0)))
    H=np.transpose(A).dot(W).dot(A)
    a0=a0-np.linalg.inv(H).dot(gradients)
plt.show()
