
require(matrixcalc)#install this package
data<-read.csv(file="C:/Users/ccoles/Dropbox/linear_databook/gerrymandering/project1c.csv", 
             header = FALSE,sep = ",")
mat <- as.matrix(data)#make sure your data is a matrix
datamatrix<-mat[,2:ncol(mat)]
datamatrix<-datamatrix[2:nrow(mat),]
diagmatrix<-matrix(0,nrow(datamatrix),ncol(datamatrix))
for(i in 1:nrow(datamatrix))
{diagmatrix[i,i]<-datamatrix[i,i]}
AE<-datamatrix-diagmatrix
#netscore represents the percentage of the boundary shared
netscore<-matrix(0,nrow(AE),1)
for(i in 1:nrow(AE))
{netscore[i]<-sum(AE[i,])}
#ranking1
AEstar<-AE+t(AE)+diag(nrow(AE))
ranking1<-netscore+AEstar%*%netscore
#this adds in the census block numbers and sorts
rankorder1<-order(ranking1)
rankingmatrix1<-matrix(0,length(ranking1),2)
for(i in 1:length(ranking1))
{ rankingmatrix1[i,1]<-mat[rankorder1[i]+1,1]
  rankingmatrix1[i,2]<-ranking1[rankorder1[i]]}
#ranking 2
adjmatrix<-matrix(0,nrow(AE),ncol(AE))
for(i in 1:nrow(AE))
{
  for(j in i:ncol(AE))
  {
    if(AE[i,j]!=0){adjmatrix[i,j]<-1}
  }
}
adjmatrix<-adjmatrix+t(adjmatrix)
Laplacian<--adjmatrix
for(i in 1:nrow(adjmatrix))
{Laplacian[i,i]<-sum(adjmatrix[i,])}
ev <- eigen(Laplacian)
values<-ev$values
vectors<-ev$vectors
fiedlervalue<-values[length(values)-1]
fiedlervector<-vectors[,length(values)-1]
rankorder2<-order(fiedlervector)
rankingmatrix2<-matrix(0,length(fiedlervector),2)
for(i in 1:length(fiedlervector))
{ rankingmatrix2[i,1]<-mat[rankorder2[i]+1,1]
rankingmatrix2[i,2]<-fiedlervector[rankorder2[i]]}

#script to create two subgraphs and apply the Fiedler ranking again
g1<-c()
g2<-c()
for(i in 1:nrow(rankingmatrix2))
{
if(rankingmatrix2[i,2] < 0)
{
g1<-append(g1,rankorder2[i])
}
  else
{
g2<-append(g2,rankorder2[i])
}}
g1adj=matrix(0,length(g1),length(g1))
g2adj=matrix(0,length(g2),length(g2))
for(i in 1:length(g1))
{for(j in 1:length(g1))
{g1adj[i,j]<-adjmatrix[g1[i],g1[j]]
}}
for(i in 1:length(g2))
{for(j in 1:length(g2))
{g2adj[i,j]<-adjmatrix[g2[i],g2[j]]
}}
Laplaciang2<--g2adj
for(i in 1:nrow(g2adj))
{Laplaciang2[i,i]<-sum(g2adj[i,])}
evg2 <- eigen(Laplaciang2)
valuesg2<-evg2$values
vectorsg2<-evg2$vectors
fiedlervalueg2<-valuesg2[length(valuesg2)-1]
fiedlervectorg2<-vectorsg2[,length(valuesg2)-1]
rankorder<-order(fiedlervectorg2)

rankingmatrix3<-matrix(0,length(fiedlervectorg2),2)
for(i in 1:length(fiedlervectorg2))
{ rankingmatrix3[i,1]<-mat[g2[rankorder[i]]+1,1]
rankingmatrix3[i,2]<-fiedlervectorg2[rankorder[i]]}