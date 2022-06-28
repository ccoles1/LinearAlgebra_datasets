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
train<-matrix(0,length(subscriptlist),64])
for (j in 1:length(subscriptlist)){
        train[j]=X[subscriptlist[j]]
 }
train<-t(train)

def phi(x):
#sigmoid activation function
    return 1/(1+math.exp(-x))
# hyperbolic tan activation function
#    return np.tanh(x)
