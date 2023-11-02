#Christodoulos Stylianides
#Askisi 4
#!/bin/python

def prpar(N):#akrivos to idio function me tin askisi 3
    list=[]
    for i in range(2,N//2+1):
        if N%i==0:
            list+=[i]
    list+=[N]
    return list

primes=[]
for i in range(2,10000):
    if prpar(i)[0]==i:
        primes+=[i]
print(primes)
exit()
