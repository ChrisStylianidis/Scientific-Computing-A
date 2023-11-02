#Christodoulos Stylianides Askisi 2
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
akrivia1=1000
akrivia2=10000
Periodos=2*np.pi
dt=Periodos/akrivia1
t=[]
unow,xnow,tnow=0,1,0
xpos1,ypos1=[],[]
E1,E2,E3=[],[],[]
e1,e2,e3=0,0.5,0.5#energies kinitiki dinamiki oliki
while(tnow<=Periodos):
    xpos1.append(xnow)
    ypos1.append(unow)
    E1.append(e1)
    E2.append(e2)
    E3.append(e3)
    t.append(tnow)
    unow+=-xnow*dt
    xnow+=unow*dt
    e1=0.5*(unow**2)
    e2=0.5*(xnow**2)
    e3=e2+e1
    tnow+=dt

dt=2*np.pi/akrivia2
t1=[]
unow,xnow,tnow=0,1,0
xpos2,ypos2=[],[]
E11,E21,E31=[],[],[]
e1,e2,e3=0,0.5,0.5#energies kinitiki dinamiki oliki
while(tnow<=Periodos):
    xpos2.append(xnow)
    ypos2.append(unow)
    E11.append(e1)
    E21.append(e2)
    E31.append(e3)
    t1.append(tnow)
    unow-=xnow*dt
    xnow+=unow*dt
    e1=0.5*(unow**2)
    e2=0.5*(xnow**2)
    e3=e2+e1
    tnow+=dt

plt.figure()#Acc Speed And position in one plot different graphs
plt.suptitle("Euler for Harmonic Motion")
plt.subplot(221)
plt.title("Kinetic: Green, Potential: Blue, Total: Black")
plt.plot(t,E1,'g',t,E2,'b',t,E3,'k')#kinitiki green, dinamiki blue, oliki black 
plt.xlabel("Time t(s)")
plt.ylabel("Energy J(Joules)")

plt.subplot(222)

#plt.title("Kinetic: Green, Potential: Blue, Total: Black")
plt.plot(t1,E11,'g',t1,E21,'b',t1,E31,'k')#kinitiki green, dinamiki blue, oliki black 
plt.xlabel("Time t(s)")
plt.ylabel("Energy J(Joules)")

plt.subplot(223)
plt.title("Errors")
yy,yyy=np.zeros(len(E3)),np.zeros(len(E31))
for i in range(len(E3)):
    yy[i]=(0.5-E3[i])#to 0.5 einai to theoritiko
plt.plot(t,yy,'k')
plt.subplot(224)
plt.title("Errors")
for i in range(len(E31)):
    yyy[i]=(0.5-E31[i])
plt.plot(t1,yyy,'k')
plt.savefig("Harmonic Motion Energy.pdf")



plt.figure()#u x


tth=np.linspace(0,Periodos,10000)#time theory
xth=np.cos(tth)
uth=-np.sin(tth)
plt.plot(xth,uth,'r--')#to theoritiko einai diakekomeno




plt.title("Phase Space")
plt.ylabel("Speed u(m/s)")
plt.xlabel("Position x(m)")
plt.plot(xpos1,ypos1,'b',xpos2,ypos2,'k')
plt.savefig("Phase Space.pdf")

plt.show()
exit()
