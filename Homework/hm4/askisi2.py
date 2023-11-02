#Christodoulos Stylianides askisi 2
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
from random import random
#Transformation Method
def f(x):
    return np.log(x)
ntries = 1000000

xmin=1
xmax=2

y = []
for i in range(ntries):
    x=xmin+(xmax-xmin)*random()
    y.append(f(x))
cont,binv,intr=plt.hist(y,bins=100,color='k')
plt.show()
exit()
