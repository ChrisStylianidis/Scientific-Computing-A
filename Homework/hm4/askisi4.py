#Christodoulos Stylianides askisi 4
#!/bin/python3
from random import random
import numpy as np

L=10
step=1

def imin(x):#sinartisi gia sinthiki while
    if x>L or x<-L:#molis vgei apo ta oria 
        return False#tha vgei kai apo to while
    return True

tries=int(input("How many drunken walks do you want to try?"))
countsteps=0
for i in range(tries):
    pos=0#position
    
    while(imin(pos)):
        if random()>=0.5:
            pos+=step
        else:
            pos-=step
        countsteps+=1
average=countsteps/tries
print("Average steps per walk:",average)
exit()
