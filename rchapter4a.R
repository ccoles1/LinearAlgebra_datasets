require(matrixcalc)#install this package
require(matlib)#install this package
library(matrixcalc)
library(mpoly)
require(mpoly)#install this package
M <- matrix(c(20,9,1,5,20,8,19,20,19,20),nrow = 2, ncol = 5, byrow = TRUE)
A <- matrix(c(1,2,3,4),nrow = 2, ncol = 2, byrow = TRUE)
print(A)
encryption<-A%*%M%%29
print(encryption)
decryption<-inv(A)%*%encryption%%29
print(decryption)

# Public Key Encryption using Chebyshev Polynomials
x<-.065
s<-2731#Rahasa knows s but Siri only knows Ts(x)
Ts<- cos(s*acos(x))
r<-1951#Siri knows r but Rahasa only knows Tr(x)
Tr<-cos(r*acos(x))
Trs<-cos(r*acos(Ts))
soln1a<-acos(Ts)/acos(x)
soln1b<-1/acos(x)
soln2a<-acos(Trs)/acos(Tr)
soln2b<-1/acos(Tr)
for (i in 1:3000){
  pn1<-round(soln1a+i*2*pi*soln1b)
  pn2<- -soln2a+0.44747421259888365*(2.105633366676259 +
                                       4.1727931936289355*i)*2*pi*soln2b
  if((sum(pn1/1:pn1==pn1%/%1:pn1)==2)&&(pn1==pn2)){
    print(pn1)
  }}
# Decryption cheby< −chebyshev(5)
cheb<-c(-51167940,-3,0,-4,0,16)
polyroot(cheb)
