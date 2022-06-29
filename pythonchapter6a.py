data<-read.csv(file="stockreturn.csv",sep = ",")
mat<-as.matrix(data)

returnAAL<-list()
returndAL<-list()
returnUAL <-list()
returnABBV<-list()
returnCBG <-list()
returnEQR<-list()
for (i in 2:600000){
    if (mat[i, 7] == "AAL"){
        returnAAL<-append(returnAAL, mat[i, 5])
        }
    if (mat[i, 7] == "ABBV"){
        returnABBV<-append(returnABBV, mat[i, 5])
        }
    if (mat[i, 7] == "DAL"){
        returndAL<-append(returndAL, mat[i, 5])
        }
    if (mat[i, 7] == "UAL"){
        returnUAL<-append(returnUAL, mat[i, 5])
        }
    if (mat[i, 7] == "CBG"){
        returnCBG<-append(returnCBG, t1[i, 5])
        }
    if (mat[i, 7] == "EQR"){
        returnEQR<-append(returnEQR, mat[i, 5])
        }
    }
x<-1:length(returnAAL)
plot(x,returnAAL)

A<-matrix(0,6,length(returnAAL)-1)
for (i in 1:length(returnAAL)-1){
  A[1, i]<-log(as.numeric(returnAAL[i + 1])/as.numeric(returnAAL[i]))
  A[2, i]<-log(as.numeric(returnABBV[i + 1])/as.numeric(returnABBV[i]))
  A[3, i]<-log(as.numeric(returnCBG[i + 1])/as.numeric(returnCBG[i]))
  A[4, i]<-log(as.numeric(returndAL[i + 1])/as.numeric(returndAL[i]))
  A[5, i]<-log(as.numeric(returnEQR[i + 1])/as.numeric(returnEQR[i]))
  A[6, i]<-log(as.numeric(returnUAL[i + 1])/as.numeric(returnUAL[i]))
}

elist =list()
mlist = list()
flist = list()
avg = list()

for (time in 1:1200){
    Temp<-matrix(0,6,6)
    for (i in 1:6){
        for (j in 1:6){
            Temp[i,j]<-A[i,j+time-1]
            }
        }
    W<-Temp%*%t(Temp)/sqrt(2*6)
    Stime<-t(Temp)%*%Temp/sqrt(2*6)
    H1<-(S + t(S))/6;
    ev <-eigen(H1)
    elist<-append(elist, mean((values <- ev$values)))
    ev<-eigen(Stime)
    mlist<-append(mlist, max(mean((values <- ev$values))))
    ev<-eigen(W)
    flist<-append(flist, mean((values <- ev$values)))
    avg = append(avg, mean(Stime[1,]))
}
hist(unlist(flist),main="eigenvalues of correlation matrix")

#average 7 day

avg1<-list()
avg2<-list()
temp<-matrix(0,30)
temp1<-matrix(0,30)
for (time in 1:1090){
    for (i in 1:30){
      temp[i]<-avg[i - 1 + time]
      temp1[i]<-mlist[i - 1 + time]
        }
  avg1<-append(avg1,mean(unlist(temp)))
  avg2<-append(avg2,mean(unlist(temp1)))
}

x<-1:length(avg1)
y<-10*unlist(avg1)
plot(x,y,col="blue",xlab='time',ylab='eigenvalues of covariance matrix')
plot(x,avg2,col="red",xlab='time',ylab='maximum eigenvalues')
