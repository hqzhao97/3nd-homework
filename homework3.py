import numpy as np
import pylab as pl
number=[]
totaltime=[]
N=[]
N0=1000
N.append(N0)
a=10
b=0.01
timestep=1
totaltime.append(0)
for i in range (10000):
	t=totaltime[i]+timestep
	number=N[i]+a*N[i]-b*N[i]*N[i]
	N.append(number)
	totaltime.append(t)
pl.plot(totaltime,N,'r')
pl.show