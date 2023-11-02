#Christodoulos Stylianides askisi 1
#!/bin/python3
import numpy as np
def f(x):
    return np.exp(-x**4)

def trapezium(n,down,up):
    dx=(up-down)/n
    s=f(up)+f(down)
    for i in range(1,n-1):
        s+=f(down+i*dx)+f(down+(i+1)*dx)
    s/=2
    s*=dx
    print("Trapezium rule for step {0:1d} is: {1:.5f}".format(int(n),float(s)))

ntries=int(input("Give tries:"))
d=-2#down
u=2#up
trapezium(ntries,d,u)


exit()

