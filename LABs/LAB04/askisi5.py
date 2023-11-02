#Askisi 5 Christodoulos Stylianides
#!/bin/python3

import numpy as np

r=input("Give rows:")
r=int(r)
c=input("Give columns:")
c=int(c)
V=np.zeros((r,c))
for i in range(c):
    V[0,i]=1
    V[r-1,i]=1
for i in range(r):
    V[i,0]=1
    V[i,c-1]=1
print(V)
exit()
