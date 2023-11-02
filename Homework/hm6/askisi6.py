#Askisi 6 Christodoulos Stylianides
#!/bin/python3
import numpy as np

def sort(A):
    for i in range(len(A)):
        temp=A[i]
        j=i-1
        while(j>=0 and A[j]>temp):
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp

def meseatimi(A):
    sort(A)
    mid=int(len(A)/2)
    if(len(A)%2==0):
        return (A[mid-1]+A[mid])/2.0
    return A[mid]
n=int(input("Give size of array:"))
a=np.zeros(n)
print("Give %d values:" %n)
for i in range(n):
    a[i]=int(input(""))
print("I mesea timi einai = ",meseatimi(a))
