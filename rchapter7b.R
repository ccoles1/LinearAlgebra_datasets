install.packages('matrixcalc')
library('matrixcalc')

data<-read.csv(file="birdcalls1.csv",header = FALSE,sep = ",")
mat<-as.matrix(data)
X<-matrix(0,nrow(mat)-2,ncol(mat)-2)
for(i in 1:nrow(X)){
  for(j in 1:ncol(X)){
    X[i,j]<-as.numeric(mat[i+1,j+2])
  }}

decision<-list()

sort_index<-function(lst){
    s<-sort(x, index.return=TRUE)
    return(s)
}

n<-10
jfn<-4

#Sri Lankan Jungle fowl bird calls are between col1 and col2
col1<-3
col2<-7
indices<-list()
jfindices<-list()
xpeaks<-list()
ypeaks<-list()
jfxpeaks<-list()
jfypeaks<-list()
xconstraints<-list()
yconstraints<-list()
indices1<-sample(1:col1, n, replace=F)
indices2<-sample(col2:ncol(mat),n,replace=F)
indices<-c(indices1,indices2)
jfindices=sample(col1:col2,jfn,replace=F)
