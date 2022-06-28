install.packages('matrixcalc')
library('matrixcalc')
data<-read.csv(file="digits.csv",header = FALSE,sep = ",")
mat<-as.matrix(data)
X<-matrix(0,nrow(mat)-2,ncol(mat)-2)
for(i in 1:nrow(X)){
  for(j in 1:ncol(X)){
    X[i,j]<-as.numeric(mat[i+1,j+2])
  }}
subscriptlist=matrix(c(0,1,2,3,4,20,21,22,23,24,209,210,214,213,215))

# pick a sample to plot
w<-matrix(0, 15)
for (i in 1:15){
    w[i]=1/15
}
train<-matrix(0,length(subscriptlist),63)
for (j in 1:length(subscriptlist)){
        row<-subscriptlist[j]+1
        for (i in 1:ncol(X)){
            train[j,i]=X[row,i]
        }
 }
train<-t(train)

phi <- function(x){
#sigmoid activation function
      return(1/(1+exp(-x)))
# hyperbolic tan activation function
#    return(tanh(x))
}
phiprime<-function(x){
#derivative of sigmoid activation function
    return(exp(-x)/((1+exp(-x))*(1+exp(-x))))
# derivative hyperbolic tan activation function
# return(1/cosh(x)*1/cosh(x))
}
softmax<-function(x){
    return(exp(x)/sum(exp(x)))
}
cross_entropy<-function(actual, predicted){
    loss<-sum(actual*log(predicted))
    return(loss)
}
