require('matrixcalc')#install this package
#require(MASS)
#install.packages('gtools')
#install.packages('HMM')
library(gtools)
library(factoextra)#install this package
data<-read.csv(file="s_n_p_data1920.csv",header = FALSE,sep = ",")
mat <- as.matrix(data)#make sure your data is a matrix
binarymarket<-matrix(0,nrow(mat)-2,3)
for(i in 1:nrow(binarymarket)){
  for(j in 1:ncol(binarymarket)){
    if(as.numeric(mat[i+1,5])>as.numeric(mat[i+1,2]))
    {binarymarket[i,1]<-1}
    if(as.numeric(mat[i+1,3])>as.numeric(mat[i+1,2]))
    {binarymarket[i,2]<-1}
    if(as.numeric(mat[i+1,2])>as.numeric(mat[i+1,4]))
    {binarymarket[i,3]<-1}
  }}
patterns<-permutations(2,3,v=c(0,1),repeats.allowed=TRUE)
patterndata<-matrix(0,nrow(binarymarket))
countpatterns<-matrix(0,nrow(patterns))
for (i in 1:nrow(binarymarket))
{for (j in 1:nrow(patterns))
{
  if(isTRUE(all.equal(binarymarket[i,],patterns[j,],convert=TRUE)))
  {
    patterndata[i]=j
    countpatterns[j]=countpatterns[j]+1
  }}}
p<-countpatterns/sum(countpatterns)
T<-matrix(0,8,8)
for (i in 1:nrow(patterndata)-1)
{T[patterndata[i+1],patterndata[i]]=T[patterndata[i+1],patterndata[i]]+1}
T<-T/sum(T)
#forward
P=cbind(patterns,T%*%T%*%p)
#webscrapping for data
#install.packages('selectr')
#install.packages('xml2')
#install.packages('rvest')
library(xml2)
library(rvest)
library(stringr)
library(tidyr)
f<-read.csv(file="tweets.csv",header = FALSE,sep = ",")

#install.packages('HMM')
library(HMM)
# Initial HMM

# Sequence of observation
a = sample(c(rep("Bull",100),rep("Bear",300)))
b = sample(c(rep("Bull",300),rep("Bear",100)))
observation = c(a,b)
# Initialise HMM
transProbs<-matrix(c(1/3,3/4,2/3,1/4),2)
emissionProbs<-matrix(c(1,4/5,0,1/5),2)
hmm<-initHMM(c("U","D"), c("Bull","Bear"), startProbs=c(1/2,1/2),transProbs,emissionProbs)
print(hmm)
# Sequence of observations
observations = c("Bull","Bear","Bull")
# Calculate Viterbi path
viterbi = viterbi(hmm,observations)
print(viterbi)
# Baum-Welch
bw = baumWelch(hmm,observation,10)
print(bw$hmm)
