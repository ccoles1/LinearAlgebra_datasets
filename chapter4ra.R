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
