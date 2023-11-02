#Christodoulos Stylianides Askisi 3
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
pi=3.1415926535897932384626433832795028841971693993751058209749445

def myfun(t):
    return np.exp(-t)*np.cos(2*pi*t)

x1=np.arange(0.0,5.1,0.1)
x2=np.arange(0.0,5.02,0.02)

plt.figure()
plt.suptitle("Askisi 3")
plt.subplot(211)
plt.plot(x1,myfun(x1),'o',color="b")
plt.xlabel("Myfunction")
plt.ylabel("Values")

plt.plot(x2,myfun(x2),'k')
plt.subplot(212)

x=x2
y=np.cos(2*pi*x)
plt.plot(x,y,'r--')
plt.ylabel("Values")
plt.xlabel("cos(2*pi*x)")

plt.show()
exit()
#======================
#10
#======================