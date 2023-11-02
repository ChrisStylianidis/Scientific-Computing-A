#Christodoulos Stylianides Askisi 3
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
m=0.01
b=0.1
dt=0.001
t=0
u=0
g=9.8
U,T=[],[]
eu=0
EU=[]
while(t<0.1):
    EU.append(eu)
    T.append(t)
    U.append(u)
    eu+=(-b*u/m+g)*dt
              #i methodos euler
              # kai euler cromer einai i idia   
    ut=-b*u/m+g#giati psaxnoume taxitita-xrono
    u+=ut*dt
    t+=dt
t,u,eu=0,0,0
dt=0.01
U1,T1,EU1=[],[],[]
while(t<0.1):
    T1.append(t)
    U1.append(u)
    EU1.append(eu)
    eu+=(-b*u/m+g)*dt
    ut=-b*u/m+g
    u+=ut*dt
    t+=dt

#to x kai y einai ta theoritika 
x=np.linspace(0,0.1,1000)
y=(m*g/b)*(1-np.exp(-b*x/m))#i praksi afti ipologistike sto xarti

plt.xlabel("Time t(s)")
plt.ylabel("Speed u(m/s)")
plt.title("Method Euler-Cromer")
plt.plot(x,y,'r--')#theoritiko einai red diakekomeni
plt.plot(T,U,'k',T1,U1,'b')#mikro vima black line, megalitero vima blue line
plt.savefig("SpeedEuler-Cromer.pdf")
plt.figure()
plt.xlabel("Time t(s)")
plt.ylabel("Speed u(m/s)")
plt.plot(x,y,'r--')
plt.plot(T,EU,'k',T1,EU1,'b')
plt.title("Method Euler")
plt.savefig("SpeedEuler.pdf")

#i diafora metaksi theoritikis kai arithmitikis timis 
#mionete otan to vima dt einai mikrotero, opws fenete sto sxima 
#i mavri grami i opia exei pio mikro vima einai mia pio kali anaparastasi
#tis theoritikis



plt.show()
exit()
