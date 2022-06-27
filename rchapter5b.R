install.packages('matrixcalc')
install.packages('matlib')
library('matrixcalc')
library('matlib')
cases <- matrix(c(607,576,638,615,655,536,358,539,432,460,445,428,448,367,470,401))
x<-matrix(0, length(cases))
y<-matrix(0, length(x))
for (i in 1:length(y)){
    y[i]<-cases[1]
    for (j in 1:i){
        x[i]<-i
        y[i]<-y[i]+cases[j]
    }
}
a0<-matrix(c(5.5,.4))
A<-matrix(0,length(y),2)
W<-matrix(0,length(y),length(y))
for (i in 1:length(y)){
    A[i,1]<-1
    A[i,2]<-x[i]
    W[i,i]<-exp(a0[1]+a0[2]*x[i])
}
gradients<-t(A)%*%y-t(A)%*%(exp(A%*%a0))
H<-t(A)%*%W%*%A
a0<-a0-inv(H)%*%gradients

#plotting the model
xsmall <- seq(1, 5, by=0.1)
plots<-matrix(0,length(xsmall),4)
plot(x,y)
data<-matrix(c(exp(a0[1]+a0[2]*xsmall)))
for (i in 1:length(data)){
    plots[i,1]<-data[i]
}
plot(xsmall,exp(a0[1]+a0[2]*xsmall),xlab = "Time",
   ylab = "Cumulative Covid Cases",typ="l",col="green")
