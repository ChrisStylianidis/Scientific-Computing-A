#Christodoulos Stylianides askisi 1
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from random import random
#Rejection Method
def f(x):
    return np.exp(-(x**2))
ntries = 10000

xmin=-10
xmax=10
ymin=0
ymax=1

x = []
for i in range(ntries):
    xran=xmin+(xmax-xmin)*random()
    yran=ymin+(ymax-ymin)*random()
    if(f(xran)>=yran):
        x.append(xran)
        
freq,binv,intr=plt.hist(x,bins=100,color='k')
plt.show()
exit()
