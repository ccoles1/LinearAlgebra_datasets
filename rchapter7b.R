install.packages('matrixcalc')
library('matrixcalc')

data<-read.csv(file="birdcalls1.csv",header = FALSE,sep = ",")
#birdcalls.csv is located in birdcallsupdated.zip
mat<-as.matrix(data)
X<-matrix(0,nrow(mat)-2,ncol(mat)-2)
for(i in 1:nrow(X)){
  for(j in 1:ncol(X)){
    X[i,j]<-as.numeric(mat[i+1,j+2])
  }}

sort_index<-function(x){
    s<-sort(x, index.return=TRUE)$ix
    return(s)
}

decision<-list()

n<-10
jfn<-4

# 2n is the number of non Sri Lankan Jungle fowl in the training set, jfn is the number of Sri Lankan Jungle fowl in the training set. This can be changed.
#Sri Lankan Jungle fowl bird calls are between col1 and col2, in the dataset Sri Lankan Jungle fowl are in columns 17 to 31

col1<-3
col2<-7
for (run in 1:5){
    indices<-list()
    jfindices<-list()
    xpeaks<-list()
    ypeaks<-list()
    xconstraints<-list()
    yconstraints<-list()
    indices1<-sample(1:col1, n, replace=T)
    indices2<-sample(col2:ncol(mat),n,replace=T)
    indices<-c(indices1,indices2)
    jfindices<-sample(col1:col2,jfn,replace=T)

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

#now a test case from the jungle fowl data
    birdcall=mat[,sample(col1:col2,1,replace=F)]
    f=abs(fft(birdcall))
    x=sort_index(f)[1]/1000
    y=(sort_index(f)[2]-sort_index(f)[1])/sort_index(f)[1]
    if ((x > xconstraints[1]) & (x < xconstraints[2]) & (y > yconstraints[1]) & (y < yconstraints[2])){
        decision<-append(decision,1)
        } else {
        decision<-append(decision,0)
    }
}

if (sum(decision == 1) >= sum(decision == 0)){
    print("Bird is a Sri Lankan Jungle Fowl")
}else{
    print("Bird is not a Sri Lankan Jungle Fowl")
}

# if at any point you wish to see a scatterplot
plot(xpeaks,ypeaks)
points(jfxpeaks,jfypeaks,col='red')
