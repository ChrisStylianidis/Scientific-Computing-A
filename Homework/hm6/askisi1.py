#Askisi 1 Christodoulos Stylianides
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from random import random
r=np.linspace(2,10,1000)
eps=0.0103
sig=3.3
A=4*eps*(sig**12)
B=4*eps*(sig**6)
y=A/(r**12)-B/(r**6)
def f(x):
    return A/(x**12)-B/(x**6)
plt.plot(r,y,label="VLJ(r)")
ax=plt.gca()
ax.set_ylim([-0.010,0.020])
ax.set_xlim([3.5,8.])
plt.legend(loc='best')
plt.savefig("Askisi1A.pdf")
minn=0#ipo alles sinthikes to min einai enas
#megalos arithmos alla afou i sinartisi exei y upo to miden
#theto to min ws 0
r0=0
for i in range(10000):
    x=3.5+random()*(8-3.5)
    y=f(x)
    if(minn>y):
        minn=y
        r0=x
print("The minimum value of Vlj:")
print("Vlj(r0={0:0.5f})= {1:0.5f}".format(r0,minn))
dx=0.05
x=3.5
xa,fa=[],[]#o aksonas x kai i dinami F
fcurr=-12*A/(x**13)+6*B/(x**7)
while(x<8):
    xa.append(x)
    fa.append(fcurr)
    deriv=-f(x)
    fcurr+=deriv*dx
    x+=dx
plt.figure()
plt.plot(xa,fa,'k',label="F")
plt.legend(loc='best')
plt.savefig("Askisi1C.pdf")
exit()
