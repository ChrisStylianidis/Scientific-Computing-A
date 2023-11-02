#Askisi 2 Christodoulos Stylianides
#!/bin/python3

import numpy as np
a=np.random.rand(3,3)
for i in range(3):
    for j in range(3):
        a[i,j]*=8
        a[i,j]+=2

print(a)
exit()
