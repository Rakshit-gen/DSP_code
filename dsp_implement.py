import numpy as np
import scipy as sy
from matplotlib import pyplot as plt
import math

def solver():
    l=int(input('Enter 1 for convolution and 2 for dft:'))
    if l==1:
        xn=list(map(float,input('X[n]: ').split()))
        hn=list(map(float,input('H[n]: ').split()))
        n1=len(xn)
        n2=len(hn)
        N=n1+n2-1
        Y=np.zeros(N)
        m=N-n1
        n=N-n2
        xn=np.pad(xn,(0,m),'constant')
        hn=np.pad(hn,(0,n),'constant')
        for i in range(N):
            for j in range(N):
                if i>=j:
                    Y[i]=Y[i]+xn[i-j]*hn[j]
        print(Y)
        for j in Y:
            print(j)
    if l==2:
        xn=list(map(float,input('X[n]: ').split()))
        N=int(input('How many point DFT:'))
        dftval=np.fft.fft(xn,n=N)
        print(dftval)
        for i in dftval:
            print(i)
while True:
    try:
        solver()
    except Exception:
        print('Invalid')
    


