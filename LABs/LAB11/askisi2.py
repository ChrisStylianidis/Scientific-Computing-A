#Christodoulos Stylianides askisi 2
#!/bin/python3
import numpy as np
def f(x):
    return 3*x*x*np.exp(x**3)

def averagemeanrule(n,down,up):
    dx=(up-down)/n
    s=f(up)+f(down)
    for i in range(1,n-1):
        s+=f(down+(i+0.5)*dx)
    s*=dx
    print("Average mean rule with step {0:d} is: {1:.5f}".format(int(n),float(s)))
    exit()
ntries=int(input("Give tries:"))
d=0#down
u=1#up
averagemeanrule(ntries,d,u)
exit()
