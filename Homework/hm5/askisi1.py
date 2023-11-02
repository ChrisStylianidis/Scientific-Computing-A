#Christodoulos Stylianides Askisi 1
#!/bin/python3
from random import random
import numpy as np
def f(x):
    return np.sin(x)
def montecarlo(ntries,Low,Up):#monte carlo mesi timi
    value=0
    valuesqrt=0
    for i in range(ntries):
        rnd=Low+(Up-Low)*random()
        rvssqrt=f(rnd)*f(rnd)
        rvs=f(rnd)
        valuesqrt+=rvssqrt
        value+=rvs
    expectsqrt=(Up-Low)*(valuesqrt/ntries)
    expect=(Up-Low)*(value/ntries)
    error=(Up-Low)*np.sqrt(abs((expectsqrt)-(expect)**2)/ntries)
    return expect,error


myfile=open('integral.dat','w')
myfile.write("Tries:\tIntegral: errors:\n")

xmin=0
xmax=np.pi
for i in range(17):
    tries=2**(i+1)
    Integral,error=montecarlo(tries,xmin,xmax)
    #print(Integral,error)
    myfile.write("{:d}\t{:.5f}\t  {:.5f}\n".format(tries,Integral,error))
myfile.close()
exit()
