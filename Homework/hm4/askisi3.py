#Christodoulos Stylianides askisi 3
#!/bin/python3
from random import random
import numpy as np

def f(x):
    return x*x*np.exp(-x)

tries=10000
value=0#to mikrotero value,theoro oti einai to 0

for i in range(tries):
    x=4*random()
    y=random()#to y max den einai megalitero apo 1
    if(f(x)>=y and value<y):
        value=y

print("Max value of f(x):",value)
#end of part 1

def g(x,y):
    return y-x-2*x*x-2*x*y-y*y
xmin=-2
xmax=2
ymin=1
ymax=3#oria gia x kai y

value=ymin
for i in range(tries):
    x=xmin+(xmax-xmin)*random()
    y=ymin+(ymax-ymin)*random()
    if(g(x,y)>=y and value<y):
        value=y

print("Max value of f(x,y) is:",value)


    
    
   
exit()
