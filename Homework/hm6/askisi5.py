#!/usr/root/python3

import numpy as np
import matplotlib.pyplot as plt
from random import random

def athr(n):
    sum=0
    for i in range(n):
        x=6*random()
        if(x<=1):
            sum+=1
        if(x>1 and x<=2):
            sum+=2
        if(x>2 and x<=3):
            sum+=3
        if(x>3 and x<=4):
            sum+=4
        if(x>4 and x<=5):
            sum+=5
        if(x>5 and x<=6):
            sum+=6
    return sum
ntries=10000

plt.figure()
zaria=2
x=np.zeros(ntries)
for i in range(ntries):
    x[i]=athr(zaria)
cont,binv,intr=plt.hist(x,bins=zaria*10+1,color='k',range=(float(zaria),float(zaria)*6),density=True,histtype='step')
plt.grid(True)
plt.title("Throwing {0:d} dice".format(zaria))
plt.savefig("Askisi5B.pdf")

plt.figure()
zaria=3
x=np.zeros(ntries)
for i in range(ntries):
    x[i]=athr(zaria)
cont,binv,intr=plt.hist(x,bins=zaria*10+1,color='k',range=(float(zaria),float(zaria)*6),density=True,histtype='step')
plt.grid(True)
plt.title("Throwing {0:d} dice".format(zaria))
plt.savefig("Askisi5C.pdf")
#plt.show()
exit()
