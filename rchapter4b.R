install.packages('devtools')
library('devtools')
library('matlib')
require('rSymPy')
library('factoextra')
# Table 4.6 Data
A<-matrix(c(1,37.5,57.21,9.5, 1,6.83,36.33,5.7, 1,11.25,38.32,4.8, 1,28.21,41.86,72.6),nrow
           =4,byrow=TRUE)
b<-matrix(c(30.7,15.3,12.16,23.75),nrow=4,byrow=TRUE)
print((t(A)%*%A)%*%t(A)%*%b)

# Table 4.7 Data
x<- c(6.6, 12, 15, 58.5)
n<- length(x)
q<-matrix(0, n, n)
q[,1]<- c(45.6, 105.5, 69.7, 53.5)
f<- as.character(round(q[1,1], 4))
fi<- ''
for (i in 2:n) {
  for (j in i:n) {
    q[j,i]<- (q[j,i-1] - q[j-1,i-1]) / (x[j] - x[j-i+1])
  }
  fi<- paste(fi, '*(x - ', x[i-1], ')', sep = '', collapse = '')
  f<- paste(f, '+', round(q[i,i], 4), fi, sep = '', collapse = '')
}
print(f)

# Table 4.8 Data
A<-matrix(c(1.,69883.,0.269484,1.,25802.,0.130347,1.,17332.,0.296852,1.,22108.,0.171374,
             1.,49248.,0.151853,1.,52136.,0.265944,1.,22492.,0.403457,1.,65090.,0.143834,1.,27680.,0.447641,
             1.,28604.,0.235673,1.,71200.,0.314642,1.,35636.,0.253052),nrow=12,byrow=TRUE)
b<-matrix(c(0.8, 0.634, 0.725, 0.741, 0.743, 0.192, 0.5314, 0.848, 0.7986,0.7105, 0.9422, 0.8818),nrow=12,byrow=TRUE)
print((t(A)%*%A)%*%t(A)%*%b)
div<-matrix(0,nrow(A),ncol(A))
for(i in 1:nrow(div)){
  for(j in 1:ncol(div)){
    if(j!=ncol(div)){
      div[[i,j]]=(A[[i,j+1]]-mean(A[,j+1]))/sd(A[,j+1])
    }
    else{div[[i,j]]=(b[[i]]-mean(b))/sd(b)}
  }
}
div.pca<- prcomp(div,scale = TRUE)
fviz_pca_ind(div.pca)
