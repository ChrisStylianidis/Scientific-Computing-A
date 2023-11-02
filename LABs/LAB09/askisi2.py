#Christodoulos Stylianides Askisi 2
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

R=1000
C=1E-6
V0=12
t=0
dt=1E-5
Q=C*V0
xa,ya=[],[]
t,V=0,12
while(t<0.001):
    xa.append(t)
    ya.append(V)
    Vt=V/R#Vt einai to V tonoumeno (derivative)
    Q-=Vt*dt
    V=Q/C
    t+=dt
xth=np.linspace(0,0.001,1000)
yth=V0*np.exp((-xth)/(R*C))
plt.plot(xth,yth,'k',xa,ya,'r--')
plt.xlabel("Time (s)")
plt.ylabel("Volts (V)")
plt.title("Apofortisi Piknoti")
plt.show()
exit()
