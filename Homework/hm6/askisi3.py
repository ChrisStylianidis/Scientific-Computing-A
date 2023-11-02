#Askisi 3 Christodoulos Stylianides
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

def Bessel(x,n):
    y=np.zeros(len(x))
    if(n==0):
        for i in range(len(x)):
            if x[i]==0:
                y[i]=1
            else:
                y[i]=np.sin(x[i])/x[i]
    if(n==1):
        for i in range(len(x)):
            if x[i]==0:
                y[i]=0
            else:
                y[i]=np.sin(x[i])/(x[i]**2)-np.cos(x[i])/x[i]
    if(n==2):
        for i in range(len(x)):
            if x[i]==0:
                y[i]=0
            else:
                y[i]=(3/(x[i]**2)-1)*np.sin(x[i])/(x[i])-3*np.cos(x[i])/(x[i]**2)
    return y

x=np.linspace(0,20.,10000)
#N=int(input("Give the grade of n:"))
plt.plot(x,Bessel(x,0),'k',label="$J_0(x)$")
plt.plot(x,Bessel(x,1),'b--',label="$J_1(x)$")
plt.plot(x,Bessel(x,2),'r',linestyle=(0,(1,1)),label="$J_2(x)$")
plt.legend()
plt.axhline(y=0,color='k')
ax=plt.gca()
ax.set_xlim([0.,20.])
plt.savefig("Askisi3.pdf")
#plt.show()
exit()
    
            
