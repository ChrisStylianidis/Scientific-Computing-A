#Christodoulos Stylianides askisi 3
#!/bin/python3
from random import random, seed
import numpy as np
seed(65432176)
def f(x1,x2,x3,x4,x5,x6):
    return (x1+x2+x3+x4+x5+x6)**2

Low=0
Up=1
def montecarlo(ntries):#monte carlo mesi timi
    value=0
    for i in range(ntries):
        rnd1=random()
        rnd2=random()
        rnd3=random()
        rnd4=random()
        rnd5=random()
        rnd6=random()
        rvs=f(rnd1,rnd2,rnd3,rnd4,rnd5,rnd6)
        value+=rvs
    expect=(value/ntries)#den pollaplasiazo me (b-a)(d-c)afou einai ola ena
    return expect


myfile=open('askisi3.dat','w')
myfile.write("   Tries:\tIntegral: \n")

for i in range(21):
    tries=2**(i+1)
    myfile.write("{:9d} {:15.10f}\n".format(tries,montecarlo(tries)))
