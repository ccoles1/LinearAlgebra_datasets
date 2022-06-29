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
