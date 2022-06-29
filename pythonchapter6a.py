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
