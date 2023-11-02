#Christodoulos Stylianides askisi 2
#!/bin/python3
from random import random
import numpy as np
import matplotlib.pyplot as plt
import urllib.request


file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/Homeworks/pillowforce.dat")
x=[]#metatopisi
y=[]#dinami stromatos
m=80
g=9.8
h=int(input("Give h:"))

for line in (file):
    t,p=np.loadtxt(file,usecols=(0,1),unpack=True)
    x.append(t)
    y.append(p)
plt.figure()
plt.plot(x[0],y[0],'k')
plt.xlabel("Distance (m)")
plt.ylabel("Force (N)")
plt.savefig("ForceDistance2A.pdf")

def f(value):
    for i in range(2000):#to size tou list mou
        if(x[0][i]>value):
            return y[0][i]
def montecarlo(ntries,Low,Up):#monte carlo mesi timi
    value=0
    for i in range(ntries):
        rnd=Low+(Up-Low)*random()
        rvs=f(rnd)
        value+=rvs
    expect=(Up-Low)*(value/ntries)
    return expect


W1=-m*g*h
W2=0
xast=0
while(W2>W1 and xast>-10):
    xast-=0.1
    W2=montecarlo(10000,xast,0)-m*g*xast#x asteraki
exit()
#apologoume se opoion tin diorthosei...
#=================
#hahaha cute, alla ta exeis kanei swsta 
#10
#=================
