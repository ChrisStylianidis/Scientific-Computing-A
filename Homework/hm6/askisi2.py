#Christodoulos Stylianides askisi 4
#!/bin/python3
import numpy as np
from random import random

def det22(A):
    return A[0][0]*A[1][1]-A[1][0]*A[0][1]

def orizousa(A):
    sum=0
    if(len(A)==2):
        return det22(A)
    for i in range(len(A)):
        B=np.zeros((len(A)-1,len(A)-1))
        r=0

        for j in range(1,len(A)):
            c=0
            for k in range(len(A)):
                if(k!=i):
                    B[r][c]=A[j][k]
                    c+=1
            r+=1
        if((i)%2==0):
            sum+=A[0][i]*orizousa(B)
        else:
            sum-=A[0][i]*orizousa(B)
    return sum
H=np.zeros((5,5))
S=np.zeros(5)
for i in range(5):
    for j in range(5):
        H[i][j]=1/(i+j+1)#anti na valw -1 vazo +1 epd to i j ksekinoun apo 0
    S[i]=i+1
x=np.linalg.solve(H,S)
solutions=np.dot(H,x)
for i in range(5):
    print("Solution x{}: {:0.0f}".format(i+1,x[i]))
print("Orizousa apo vivliothiki np=",np.linalg.det(H))
print("Orizousa tis sinartisis mou=",orizousa(H))
