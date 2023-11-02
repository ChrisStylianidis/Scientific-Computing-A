#Christodoulos Stylianides askisi 4
#!/bin/python3
from random import random, seed 
import numpy as np
import matplotlib.pyplot as plt
seed(3141592653)
def distance(x,y):
    return np.sqrt(x**2+y**2)
yaks=[]
xaks=[]
tries=10000
myfile=open('Askisi4A.txt','w')
myfile.write("Seconds Given:\t\taverage distance:\n")
for stoptime in range(100):
    d=0
    for i in range(tries):
        time=0
        x=0
        y=0
        while(time<=stoptime):
            chance=random()
            if chance<0.25:
                y+=1#panw
            elif chance>=0.25 and chance<0.5:
                y-=1#katw
            elif chance>=0.5 and chance<0.75:
                x+=1#deksia
            else:
                x-=1#aristera
            time+=1
        d+=distance(x,y)
    yaks.append(d/tries)
    xaks.append(stoptime)
    myfile.write("{0:d}\t\t\t{1:5.3f}\n".format(int(stoptime+1),float(d/tries)))
plt.plot(xaks,yaks,'k')
plt.xlabel("Seconds allowed")
plt.ylabel("Average Distance")

plt.savefig("Askisi4B.pdf")

exit()
#======================
#10
#======================