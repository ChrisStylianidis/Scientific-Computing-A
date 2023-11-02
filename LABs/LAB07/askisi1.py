#Askisi 1 Christodoulos Stylianides
#!/bin/python3
import numpy as np

x=np.linspace(-5.0,5.0,101)
def sinc(num):
    if num==0:
        return 1.0
    y=np.sin(num)/num
    return y
for i in range(101):
    print("{0:.1f}\t\t{1:15.10f}".format(float(x[i]),float(sinc(x[i]))))
exit()
