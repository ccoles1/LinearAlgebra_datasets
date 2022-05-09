require(matrixcalc)#install this package
require(MASS)
library(factoextra)#install this package
data<-read.csv(file="faces.csv",header = FALSE,sep = ",")
mat <- as.matrix(data)#make sure your data is a matrix
#we will a matrix without the titles
faces<-matrix(0,nrow(mat)-2,ncol(mat)-2)
for(i in 1:nrow(faces)){
  for(j in 1:ncol(faces)){
    faces[i,j]<-as.numeric(mat[i+1,j+1])
  }}
S=t(faces)%*%faces
S.eigen<-eigen(S)
pc1<-matrix(0,1,nrow(faces))
pc2<-matrix(0,1,nrow(faces))
pc1<-(S.eigen$vectors)[,1]
pc2<-(S.eigen$vectors)[,2]
names<-mat[1:nrow(mat),1]
PC <- data.frame(t = names, pc1, pc2)
ggplot(PC, aes(pc1, pc2)) + 
  geom_text(aes(label = tribes), size = 3) +
  xlab("First Principal Component") + 
  ylab("Second Principal Component") + 
  ggtitle("First Two Principal Components of Faces Data")
#lda
Class1<-faces[,1:5]
Class2<-faces[,6:10]
Class1.pca<-princomp(t(Class1), cor = FALSE, scores = TRUE)
Class2.pca<-princomp(Class2, cor = FALSE, scores = TRUE)
# Eigenvectors (limited to top to principal components)
Class1.svd<-svd(t(Class1)%*%Class1, 5, 2, LINPACK = FALSE)
Class1.eigen<-Class1.svd$v
Class2.svd<-svd(t(Class2)%*%Class2, 5, 2, LINPACK = FALSE)
Class2.eigen<-Class2.svd$v
Class1.mean<-colMeans (Class1.eigen )
Class2.mean<-colMeans (Class2.eigen )
betweenmeans<-Class1.mean-Class2.mean
Sw<-t(Class1.eigen)%*%Class1.eigen+t(Class2.eigen)%*%Class2.eigen
V<-ginv(Sw)%*%betweenmeans
Class1.LDA<-Class1.eigen%*%V/norm(V) 
Class2.LDA<-Class2.eigen%*%V/norm(V) 
projectedfaces<-matrix(0,ncol(faces),2)
for(i in 1:ncol(faces)){
  if(i< 6){
    projectedfaces[i,1]<-(Class1.LDA[i]*V)[1]
    projectedfaces[i,2]<-(Class1.LDA[i]*V)[1]
  }    
  if(i> 6){
    projectedfaces[i,1]<-(Class2.LDA[i-5]*V)[1]
    projectedfaces[i,2]<-(Class2.LDA[i-5]*V)[1]
  }    
}

# Plot of active individuals
p <- fviz_pca_ind(Class1.pca, repel = TRUE)
x<-projectedfaces[,1]
y<-projectedfaces[,2]
names<- c(1,2,3,4,5,6,7,8,9,10)
d<-data.frame(names,x,y)
ggplot(d, aes(x, y)) + 
  geom_text(aes(label = names), size = 3)
