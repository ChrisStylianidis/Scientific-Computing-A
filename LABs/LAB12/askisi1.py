#Christodoulos Stylianides askisi 1
#!/bin/python3
import numpy as np
from random import random
def f(x):
    return -(x)**np.pi+np.pi*(x)
#
def func(x):
    return -np.pi*(x**(np.pi-1))+np.pi
#
def deriv(x):
    return -np.pi*(np.pi-1)*(x**(np.pi-2))
#
def newton(x0,f,df,eps,istepmx):
    istep = 0
    flag = 0
    condition = True
    #
    while condition:
        if df(x0) == 0:
            flag = 2
            break
#
        error=f(x0)/df(x0)
        x1 = x0 - error    # The new solution 
        x0 = x1            # The new solution becomes the old solution for the
        istep = istep+1
        if np.abs(error) < eps:
            condition = False
#            
        if istep > istepmx:
            flag = 1
            break
#
    return x0,flag,istep

# Main 
xinit = float(input("Give a value (non zero positive):"))#the value cannot be zero
#because f''(0)=0 and you cannot devide by zero
eps =0.0001 #float(input("Give the accuracy "))
itermx =100# int(input("Give the max numbers of iterations for convergence "))
#
xsolution,flag,iter = newton(xinit,func,deriv,eps,itermx)
#
ymax=f(xsolution)
if flag == 1:
    print('No solution was reached because no convergence')
    print('{:.2d} iteration were used of max {:.2d}'.format(iter,iterx))
else:
    xmax=1.72
    itsin=0
    tries=1000000
    for j in range(tries):
        x=xmax*random()
        y=ymax*random()
        if(f(x)>=y):
            itsin+=1#epitixies
    Atr=(xmax)*(ymax)#area orthogoniou
    Area=itsin*Atr/tries#Area == olokliroma me methodo digmatolipsias
    print("The Sample Method Value for {0:d} tries is: {1:.5f}".format(int(tries),float(Area)))

exit()
    
