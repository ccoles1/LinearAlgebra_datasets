require(matrixcalc)#install this package
library(factoextra)#install this package
data<-read.csv(file="starhusbandbook.csv",header = FALSE,sep = ",")
mat <- as.matrix(data)#make sure your data is a matrix
#we will a matrix without the titles
starhusband<-matrix(0,nrow(mat)-2,ncol(mat)-2)
for(i in 1:nrow(starhusband)){
  for(j in 1:ncol(starhusband)){
    starhusband[i,j]<-as.numeric(mat[i+1,j+2])
  }}
S=starhusband%*%t(starhusband)
starhusband.eigen<-eigen(S)
pc1<-matrix(0,1,nrow(starhusband))
pc2<-matrix(0,1,nrow(starhusband))
pc1<-(starhusband.eigen$vectors)[,1]
pc2<-(starhusband.eigen$vectors)[,2]
tribes<-mat[3:nrow(mat),2]
PC <- data.frame(t = tribes, pc1, pc2)
ggplot(PC, aes(pc1, pc2)) + 
  geom_text(aes(label = tribes), size = 3) +
  xlab("First Principal Component") + 
  ylab("Second Principal Component") + 
  ggtitle("First Two Principal Components of Starhusband Data")
