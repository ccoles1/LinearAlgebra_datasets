require(matrixcalc)#install this package
data<-read.csv(file="project1sports.csv",header = FALSE,sep = ",")
mat <- as.matrix(data)#make sure your data is a matrix
#mat tells the scores of each game
#we will create sec to show score differential
sec<-matrix(0,nrow(mat)-1,ncol(mat)-1)
for(i in 1:nrow(sec)){
  for(j in 1:ncol(sec)){sec[i,j]<-as.numeric(mat[i+1,j+1])
  }}
diff<-sec
wins<-c()
for(i in 1:nrow(sec))
{
  wini<-0
  for(j in 1:ncol(sec))
  {
    diff[i,j]<-(as.numeric(mat[i+1,j+1])-as.numeric(mat[j+1,i+1]))
    if(diff[i,j]>0){wini<-wini+1}
    if(as.numeric(mat[i+1,j+1])!=0)
    {
    sec[i,j]<-1
    sec[j,i]<-1
    }
  }
  wins<-append(wins,wini)
}

#using powers of a matrix to rank teams
gamecounter<-c()
for(i in 1:nrow(sec))#nrow() gives the number of rows in a matrix
{
  counter<-0
  for(j in 1:ncol(sec))#ncol()gives the number of columns in a matrix
{
    if(sec[i,j]==0)
      {counter=counter+1}
  }#this nested loop will determine how many nonzero scores a 
  #stores it in gamecounter

  gamecounter<-append(gamecounter,ncol(sec)-counter)
}
netscore<-c()
for(i in 1:nrow(sec))
{netscore<-append(netscore,sum(diff[i,])/gamecounter[i])}
#the above loop creates a netscore vector based on the scores
#note that if a team loses a game then the entry will be neg

newmatrix<-sec+diag(nrow(sec))
ranking1<-netscore+newmatrix%*%netscore+matrix.power(newmatrix,2)%*%netscore
rankorder1<-order(ranking1)
rankingmatrix1<-matrix(0,length(ranking1),2)
for(i in 1:length(ranking1))
{ rankingmatrix1[i,1]<-mat[rankorder1[i]+1,1]
rankingmatrix1[i,2]<-ranking1[rankorder1[i]]}
#using eigenvalues to rank teams
newmatrix2<-matrix(0,nrow(mat)-1,ncol(mat)-1)
for(i in 1:nrow(newmatrix2)){
  for(j in 1:ncol(newmatrix2)){newmatrix2[i,j]<-as.numeric(mat[i+1,j+1])
  }}
for(i in 1:nrow(newmatrix2))
{
  for(j in 1:ncol(newmatrix2))
  {
    if(newmatrix2[i,j]!=0)
    {newmatrix2[i,j]<-newmatrix2[i,j]/(as.numeric(mat[i+1,j+1])+as.numeric(mat[j+1,i+1]))}
  }
}
evv.newmatrix2<-eigen(newmatrix2)
k <- which(abs(evv.newmatrix2$values)==max(abs(evv.newmatrix2$values)))
#finds the maximum eigenvalue
maxvector<-round(abs(evv.newmatrix2$vectors[,k]),digits=3)
maxvector<-maxvector/norm(maxvector)
#Re takes the real part of an entry, eliminate if you
#expect complex eigenvalues and eigenvectors
#find the eigenvector associated with the max eigenvector
ranking2<-maxvector
rankorder2<-order(ranking2)
rankingmatrix2<-matrix(0,length(ranking2),2)
for(i in 1:length(ranking2))
{ rankingmatrix2[i,1]<-mat[rankorder2[i]+1,1]
rankingmatrix2[i,2]<-ranking2[rankorder2[i]]}

#Colley matrix ranking 
Colley<--sec
#creating a zero matrix
for(i in 1:nrow(sec))
{
  for(j in 1:ncol(sec))
  {
    if(i==j)
      {
      Colley[i,j]<-2+sum(sec[i,])
    }
  }}
b<-matrix(0,nrow(sec),1)
for(i in 1:length(wins))
{
  b[i]<-1+.5*(wins[i]-(gamecounter[i]-wins[i]))
}
r<-round(solve(Colley,b),digits=3)
rankorder3<-order(r)
rankingmatrix3<-matrix(0,length(rankorder3),2)
for(i in 1:length(rankorder3))
{ rankingmatrix3[i,1]<-mat[rankorder3[i]+1,1]
rankingmatrix3[i,2]<-r[rankorder3[i]]}
