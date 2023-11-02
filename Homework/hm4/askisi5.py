#Christodoulos Stylianides Askisi 5
#!/bin/python3
from random import random
import numpy as np

def f(x):
    return 6*(x**3)


tries=100000
xmin=5
xmax=8
ymin=0
ymax=f(xmax)

itsin=0#it is in, sampling method euler.
for i in range(tries):
    x=xmin+(xmax-xmin)*random()
    y=ymax*random()
    if(f(x)>=y):
        itsin+=1#epitixies
Atr=(xmax-xmin)*(ymax-ymin)#area orthogoniou
Area=itsin*Atr/tries#Area == degmatolipsia

def montecarlo(ntries,Low,Up):#monte carlo mesi timi
    value=0
    for i in range(ntries):
        rnd=Low+(Up-Low)*random()
        rvs=f(rnd)
        value+=rvs
    expect=(Up-Low)*(value/ntries)
    return expect
Integral=montecarlo(tries,xmin,xmax)


x=5#euler method
area=0#area me mikro 'a'  einai tou euler
dx=0.15
while(x<=8):
    xderiv=f(x)
    area+=xderiv*dx
    x+=dx


print("The area according to Eulers Method is: {:.2f}".format(float(area)))
print("The area according to Monte Carlo's Average price is: {:.2f}".format(float(Integral)))
print("The area according to Monte Carlo's Sampling Method is: {:.2f}".format(Area))
print("The area according to Integration is: 5206.50")


exit()
