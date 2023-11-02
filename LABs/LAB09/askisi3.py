#Christodoulos Stylianides Askisi 3
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
R=1000
C=1E-6
V0=12#V pigis
t,V=0,0
dt=1E-5
xa,ya=[],[]
xth,yth=[],[]
Q=0
while(t<1E-3):
    xa.append(t)
    ya.append(V)
    Vt=(V0-V)/R
    Q+=Vt*dt
    V=Q/C    
    yth.append(V0*(1-np.exp((-t)/(R*C))))
    xth.append(t)
    t+=dt
plt.plot(xa,ya,'r--',xth,yth,'k')
plt.xlabel("Time (s)")
plt.ylabel("Volts (V)")
plt.title("Fortisi Piknoti")
plt.show()
exit()
