#Christodoulos Stylianides Askisi 7
#!/bin/python3
import numpy as np
import urllib.request
from random import random
file_towrite=open("randomized_pinakas.dat","w")
file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/Homeworks/pinakas.dat")
'''
kata tin anagnosi tou file me afto 
ton tropo xanete i proti timi
'''


h,u=np.loadtxt(file,unpack=True)
for i in range(len(h)):
    newpos=int(len(h)*random())
    k=u[i]
    u[i]=u[newpos]
    u[newpos]=k
    k=h[i]
    h[i]=h[newpos]
    h[newpos]=k 
    
for i in range(len(h)):
    file_towrite.write("{0:12.5f}\t{1:12.5f}\n".format(h[i],u[i]))
