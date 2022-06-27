install.packages('matrixcalc')
library('matrixcalc')
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
n<-4
plots<-matrix(0,length(xsmall),n)
for (steps in 1:n){
# for plotting the model
    xsmall <- seq(1, 5, by=0.1)
    data<-matrix(c(exp(a0[1]+a0[2]*xsmall)))
    for (i in 1:length(data)){
        plots[i,steps]<-data[i]
    }
    A<-matrix(0,length(y),2)
    W<-matrix(0,length(y),length(y))
    for (i in 1:length(y)){
        A[i,1]<-1
        A[i,2]<-x[i]
        W[i,i]<-exp(a0[1]+a0[2]*x[i])
    }
    gradients<-t(A)%*%y-t(A)%*%(exp(A%*%a0))
    H<-t(A)%*%W%*%A
    a0<-a0-matrix.inverse(H)%*%gradients
}

#plotting the model
plot(x[1:5],y[1:5],xlab = "Time",
       ylab = "Cumulative Covid Cases",ylim=c(300, 3700))
for (steps in 1:n){
    lines(xsmall,plots[,steps],col=steps)
}   
legend("topleft", legend = c(1:n),
       lwd = 3, lty = c(2, 1, 1), col = c(1:n))
