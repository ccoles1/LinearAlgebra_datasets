import pip
import pandas as pd
import numpy as np
from sympy import Matrix
M=Matrix(2,5,[20,9,1,5,20,8,19,20,19,20])
A=Matrix(2,2,[1,2,3,4])
encryption=A%29
print(encryption)
decryption=A.inv_mod(29)*encryption%29
print(decryption)
# Public Key Encryption using Chebyshev Polynomials
x=.065
s=2731 #Rahasa knows $s$ but Siri only knows T_s(x)
Ts=np.cos(s*np.arccos(x))
r=1951 # Siri knows r but Rahasa only knows T_r(x)
Tr=np.cos(r*np.arccos(x))
Trs=np.cos(r*np.arccos(Ts))
soln1a=np.arccos(Ts)/np.arccos(x)
soln1b=1/np.arccos(x)
soln2a=np.arccos(Trs)/np.arccos(Tr)
soln2b=1/np.arccos(Tr)
for i in range(3000):
    pn1=round(soln1a+i*2*math.pi*soln1b,0)
    pn2=round(-soln2a+0.44747421259888365*(2.105633366676259 +4.1727931936289355*i)*2*math.pi*soln2b,0)
    isPrime=True
if float(pn1).is_integer()==True:
    pn1=int(float(pn1))
    for j in range(2,pn1-1):
        if pn1%j == 0:
            isPrime= False
        if isPrime==True and pn1==int(float(pn2)):
            print(pn1)
# Decryption
cheb = np.polynomial.chebyshev.Chebyshev((0,0,0,0,0,1))
coef = np.polynomial.chebyshev.cheb2poly(cheb.coef)
coef-np.array([51167940,0,0,0,0,0])