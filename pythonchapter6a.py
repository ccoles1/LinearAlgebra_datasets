data<-read.csv(file="stockreturn.csv",sep = ",")
mat<-as.matrix(data)
t1<-matrix(0,nrow(mat)-2)
for(i in 1:nrow(X)){
  for(j in 1:ncol(X)){
    t1[i,j]<-as.numeric(mat[i+1,j+2])
  }}

returnAAL<-list()
returndAL<-list()
returnUAL <-list()
returnABBV<-list()
returnCBG <-list()
returnEQR<-list()
for i in range (0,600000):
    if t1[i, 6] == "AAL":
        returnAAL<-np.append(returnAAL, t1[i, 4])
    if t1[i, 6] == "ABBV":
        returnABBV<-np.append(returnABBV, t1[i, 4])
    if t1[i, 6] == "DAL":
        returnDAL<-np.append(returnDAL, t1[i, 4])
    if t1[i, 6] == "UAL":
        returnUAL<-np.append(returnUAL, t1[i, 4])
    if t1[i, 6] == "CBG":
        returnCBG<-np.append(returnCBG, t1[i, 4])
    if t1[i, 6] == "EQR":
        returnEQR<-np.append(returnEQR, t1[i, 4])
