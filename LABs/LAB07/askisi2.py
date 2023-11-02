#Askisi 2 Christodoulos Stylianides
#!/bin/python3
import numpy as np
def sinc(x):
    if x==0.0:
        return 1.0
    return np.sin(x)/x
x=np.linspace(-5.0,5.0,101)
values=list(map(sinc,x))#ola ta x pernoun apo tin sinartisi
values=np.array(values)
for i in range(101):
    print("{0:5.1f}\t\t{1:15.10f}".format(x[i],values[i]))
exit()
