import pip
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
x=np.array([1,2,3,4,5,6,7,8,9])
y=np.array([659.96,624.43,601.68,625.68,552.13,459.89,477.64,560.08,567.51])
# Lagrange interpolant
plt.plot(x,y,'ro')
poly = lagrange(x, y)
xi = np.linspace(1,9, 200)
plt.plot(xi,poly(xi))
print(poly)
#Chebyshev interpolant
xnodes=np.zeros([8])
unodes=xnodes
for k in range(0,8):
    xnodes[k]=np.cos((2*k+1)*np.pi/16)
x=xnodes
u=4*x+5
c=np.zeros([8])
sum=0;
for i in range(0,8):
    t=[0]*i
    t.append(1)
    cheb = np.polynomial.chebyshev.Chebyshev(t)
    if i==0:
        c[i]=np.dot(poly(u),cheb(x))/8
    else:
        c[i]=2*np.dot(poly(u),cheb(x))/8
coef=np.zeros([7])
for i in range(0,7):
    t=[0]*i
    t.append(1)
    cheb = np.polynomial.chebyshev.Chebyshev(t)
    for j in range(len(np.polynomial.chebyshev.cheb2poly(cheb.coef))):
        coef[j] = np.polynomial.chebyshev.cheb2poly(cheb.coef)[j]
    sum=sum+c[i]*coef

sum=np.flip(sum)
chebpoly=np.poly1d(sum)
print(chebpoly)
plt.plot(xi,chebpoly((xi-5)/4))
