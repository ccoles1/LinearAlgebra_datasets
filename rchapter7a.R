install.packages('matrixcalc')
library('matrixcalc')
data<-read.csv(file="words.csv",sep = ",")
mat<-as.matrix(data)
m<-mat
ncol<-ncol(m)
temp<-list()
for (i in 1:length(m)){
    if (nchar(m[i])==5){
        temp<-append(temp,m[i])
        }
}

# There are 496918 words in this list, 15902 of which are with 5 letters
#guess='tares'
#guess='saree'
guess='zesty'
matches<-list()
index <-matrix(c(0,1,2,3,4,5))
countmatch<-matrix(0,6,6)
for (i in 1:6){
    for (j in 1:6){
        matches<-append(matches,c(i,j))
        }
    }
for (i in 1:length(temp)){
    check1<-0
    check2<-0
    for (j in 1:5){
        if ((unlist(gregexpr(substr(guess,j,j), temp[i]))[1] >= 0) && (unlist(gregexpr(substr(guess,j,j), temp[i]))[1] != j)){
            check1 <- check1 + 1
            }
        if (unlist(gregexpr(substr(guess,j,j), temp[i]))[1] == j){
            check2<-check2+1
            }
        }
    countmatch[check2,check1]<-countmatch[check2,check1]+1
}
