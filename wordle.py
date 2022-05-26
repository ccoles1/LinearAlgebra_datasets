{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "c7f1bd7a-3f00-4cca-b764-5ee5dba0af8c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pip\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "from scipy.linalg import svd\n",
    "import matplotlib.pyplot as plt\n",
    "from itertools import combinations"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "657a3600-fef1-4596-bccb-6fac38a55e89",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = pd.read_csv('words.csv')\n",
    "m=np.array(data)\n",
    "ncol=m.shape[0]\n",
    "m=m[:,0:ncol]\n",
    "temp=list()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "3f690d71-e256-42e2-bd4c-9baa2b6e1d45",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(0,209453):\n",
    "    if len(m[i,0])==5:\n",
    "        temp.append(m[i,0])\n",
    "for i in range(209455,len(m)):\n",
    "    if len(m[i,0])==5:\n",
    "        temp.append(m[i,0])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b4a0108a-e048-4baf-b52b-75bc14bcfd49",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "15902\n"
     ]
    }
   ],
   "source": [
    "print(len(temp))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6a2e5fc7-d6ed-4878-8fbb-3301364c9048",
   "metadata": {},
   "source": [
    "There are 496918 words in this list, 15902 of which are with 5 letters"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "e1952555-e557-4747-bad4-900f54f926f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "#guess='tares'\n",
    "#guess='saree'\n",
    "guess='zesty'\n",
    "index = [0,1,2,3,4,5]\n",
    "countmatch=np.zeros([6,6])\n",
    "matches=list()\n",
    "for i in range(0,6):\n",
    "    for j in range(0,6):\n",
    "        matches.append([i,j])\n",
    "for i in range(0,len(temp)):\n",
    "    check1=0\n",
    "    check2=0\n",
    "    for j in range(0,5):\n",
    "        if temp[i].find(guess[j]) >= 0 and temp[i].find(guess[j]) is not j :\n",
    "            check1 = check1 + 1\n",
    "        if temp[i].find(guess[j]) == j:\n",
    "            check2 =check2+1\n",
    "    countmatch[check2,check1]=countmatch[check2,check1]+1\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "ce8781bb-be0f-4f5c-94a1-1c79be2311cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "listmatch=\" \".join(str(e) for e in matches)\n",
    "\n",
    "prob=countmatch/len(temp)\n",
    "plist=np.concatenate(prob)\n",
    "sorted=np.sort(plist)\n",
    "fig = plt.figure()\n",
    "plt.bar(np.arange(len(plist)),sorted[::-1],color='gray')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "79692ff7-feb8-4df0-8b5d-f1309b0a7e63",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "zesty   2.6015651589419333\n"
     ]
    }
   ],
   "source": [
    "entropy=0\n",
    "for k in range(0,len(plist)):\n",
    "    if plist[k]>0:\n",
    "        entropy=entropy-plist[k]*np.log2(plist[k])\n",
    "print(guess,\" \",entropy)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1e5e6ec5-001d-4f7a-bad1-2381062b6fe9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
