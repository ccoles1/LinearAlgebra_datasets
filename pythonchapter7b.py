#choose a training set, this will include 20 calls, at least 4 samples from sri lanka jungle fowl
indices=[]
for i in range (0,16):
  indices=np.append(indices,random.randint(0, n))
Temp = Table[0, {i, 1, 2}, {j, 1, 60}];
elist = {};
For[i = 1, i <= 100000 - 60,
  Temp[[1]] = Take[s2list, {1 + i, 60 + i}];
  Temp[[2]] = Take[s3list, {1 + i, 60 + i}];
  S = Temp . Transpose[Temp]/60;
  elist = Append[elist, Max[N[Eigenvalues[S]]]];
  i = i + 1];
