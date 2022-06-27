cases <- matrix(c(607,576,638,615,655,536,358,539,432,460,445,428,448,367,470,401))
x<-matrix(0, length(cases))
y<-matrix(0, length(x))
for (i in 1:length(y)){
    y[i]<-cases[1]
    for (j in 1:i){
        x[i]<-i
        y[i]<-y[i]+cases[j]
    }
}
a0<-matrix(c(5.5,.4))
