#Askisi 6 Christodoulos Stylianides
#!/bin/python3


def fac(n):
    m=1
    while(n>0):
        m*=n
        n-=1
    return m
def binomial(n,k):#(a)
    if k==0:
        return 1
    c=(fac(n))/(fac(k)*fac(n-k))
    return int(c)
for i in range(1,20):#(b)
    for j in range(i+1):
        print(binomial(i,j), end=' ')
    print()

exit()
#10/10