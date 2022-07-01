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

sort_index<-function(x){
    s<-sort(x, index.return=TRUE)$ix
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

xconstraints<-list()
yconstraints<-list()
indices1<-sample(1:col1, n, replace=F)
indices2<-sample(col2:ncol(mat),n,replace=F)
indices<-c(indices1,indices2)
jfindices=sample(col1:col2,jfn,replace=F)

for (i in 1:length(indices)){
    birdcall<-mat[,indices[i]]
    f<-abs(fft(birdcall))
    xpeaks<-append(xpeaks,sort_index(f)[1]/1000)
    ypeaks<-append(ypeaks,(sort_index(f)[2]-sort_index(f)[1])/sort_index(f)[1])
}

jfxpeaks<-matrix(0,length(jfindices))
jfypeaks<-matrix(0,length(jfindices))
for (i in 1:length(jfindices)){
    birdcall<-mat[,jfindices[i]]
    f<-abs(fft(birdcall))
    jfxpeaks[i]<-sort_index(f)[1]/1000
    jfypeaks[i]<-(sort_index(f)[2]-sort_index(f)[1])/sort_index(f)[1]
    xconstraints<-append(xconstraints,min(jfxpeaks))
    xconstraints<-append(xconstraints,max(jfxpeaks))
    yconstraints<-append(yconstraints,min(jfypeaks))
    yconstraints<-append(yconstraints,max(jfypeaks))
}
