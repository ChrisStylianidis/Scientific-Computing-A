#Christodoulos Stylianides askisi 3
#!/bin/python3
import numpy as np

def f(x):
    return np.exp(-x**4)
def g(x):
    return 3*x*x*np.exp(x**3)

def trapezium(n,down,up):
    dx=(up-down)/n
    s=f(up)+f(down)
    for i in range(1,n-1):
        s+=f(down+i*dx)+f(down+(i+1)*dx)
    s/=2
    s*=dx
    print("Trapezium rule with {0:d} intervals is: {1:.8f}".format(int(n),float(s)))

def averagemeanrule(n,down,up):
    dx=(up-down)/n
    s=g(up)+g(down)
    for i in range(1,n-1):
        s+=g(down+(i+0.5)*dx)
    s*=dx
    print("Average mean rule with {0:d} intervals is: {1:.5f}".format(int(n),float(s)))
for k in range(13):
    trapezium(2**k+1,-2,2)
for k in range(13):
    averagemeanrule(2**k+1,0,1)


exit()
#==================
#10
#==================