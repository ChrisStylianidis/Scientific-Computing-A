#Christodoulos Stylianides Askisi 1
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
#erotima (a)
Ts=30
T0=90
dt1=0.005
dt2=0.05
t=5*60
n1=t*200+1#n1 kai n2 einai akrivia gia evresi,
n2=(t*20)#tis theoritikis timis.

T1,T2=[],[]#lists gia ta plots temperature
t1,t2=[],[]#lists gia ta plots time

tcur1,tcur2=0,0#xronos currently
Tcur1,Tcur2=90,90#thermokrasia currently

while(tcur1<t):
    T1.append(Tcur1)
    t1.append(tcur1)
    tt1=-(1/60)*(Tcur1-Ts)#tt1 simenei T tonoumeno dld i paragogos ws pros xrono
    Tcur1+=tt1*dt1#methodos euler vima gia thermokrasia
    tcur1+=dt1#auksano xrono
while(tcur2<t):#idia diadikasia gia vima 0.05
    T2.append(Tcur2)
    t2.append(tcur2) 
    tt2=-(1/60)*(Tcur2-Ts)
    Tcur2+=tt2*dt2
    tcur2+=dt2
x=np.linspace(0,300,n1)
y=Ts-(Ts-T0)*np.exp(-x/60)#theoritiki timi

plt.figure()
plt.title("How the coffee cools")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.plot(t1,T1,'k')#to mikro vima einai black line
plt.plot(t2,T2,'b')#to megalitero vima einai blue line
plt.plot(x,y,'r--')#to piramatiko einai red diakekomeno
plt.savefig("EulerCoffee.pdf")

#erotima (b)

x2=np.linspace(0,300,n2)
y2=Ts-(Ts-T0)*np.exp(-x2/60)
T1er=T1-y
T2er=T2-y2

plt.figure()
plt.title("Errors")
plt.xlabel("Time (s)")
plt.ylabel("Temperature (°C)")
plt.plot(t1,T1er,'k',t2,T2er,'b')
plt.savefig("EulerCoffeeErrors.pdf")

plt.show()
exit()
