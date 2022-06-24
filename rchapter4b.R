library(matlib)
require(rSymPy)
library(factoextra)
# Table 4.6 Data
A<-matrix(c(1,37.5,57.21,9.5, 1,6.83,36.33,5.7, 1,11.25,38.32,4.8, 1,28.21,41.86,72.6),nrow
           =4,byrow=TRUE)
b<-matrix(c(30.7,15.3,12.16,23.75),nrow=4,byrow=TRUE)
print((t(A)%*%A)%*%t(A)%*%b)

# Table 4.7 Data
x<- c(6.6, 12, 15, 58.5)
n<- length(x)
q<-matrix(0, n, n)
q[,1]<- c(45.6, 105.5, 69.7, 53.5)
