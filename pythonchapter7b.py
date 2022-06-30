import pip
import pandas as pd
import numpy as np
import random
import matplotlib.pyplot as plt
#choose a training set, this will include 20 calls, at least 4 samples from sri lanka jungle fowl
indices=[]
n=10
for i in range (0,16):
  indices=np.append(indices,random.randint(0, n))
  
# the data in birdcalls.zip are from audio calls, we will be looking at discrete fourier transforms of these calls.
Temp = np.zeros([2,60])
elist = []
for i in range(0,100000 - 60):
  Temp[0] = Take[s2list, {1 + i, 60 + i}];
  Temp[1] = Take[s3list, {1 + i, 60 + i}];
  S = Temp . Transpose[Temp]/60;
  w,v=np.linalg.eig(S)
  elist = np.append(elist, np.max(v));

