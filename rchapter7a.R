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

index <-matrix(c(0,1,2,3,4,5))
countmatch<-matrix(0,6,6)

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

# showing the probability distribution of outcomes for the given guess
prob<-countmatch/length(temp)
sorted<-sort(as.vector(prob),decreasing=TRUE)
barplot(sorted)

# determining the entropy based on the probability distribution of the outcomes
entropy<-0
for (k in 1:length(sorted)){
    if (sorted[k]>0){
        entropy<-entropy-sorted[k]*log2(sorted[k])
        }
    }
print(entropy)
