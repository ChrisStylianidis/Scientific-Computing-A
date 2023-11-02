#Askisi 6 Christodoulos Stylianides
#!/bin/python3

import numpy as np


print("Give 5 degrees in fahrenheit")
F=np.zeros(5)
C=F
for i in range(5):#gemisma pinaka
    a=input()
    a=int(a)
    F[i]=a

for i in range(5):#mporousa na paralipso to deftero for
    C[i]=(F[i]-32)*5/9

print(C)
exit()
