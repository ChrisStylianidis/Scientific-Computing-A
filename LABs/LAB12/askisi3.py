#Christodoulos Stylianides askisi 3
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

#gia na sxediaso tin ellipsi tha xriasto tous parametrikous tipous
theta=np.linspace(0,2*np.pi,1000)
x=5*np.cos(theta)
y=4*np.sin(theta)
comm='k-'
legd='Ellipse'
plt.plot(x,y,comm,label=legd)



def f(x,a):
    return a*x+8*a-1
def check(a):
    found=0
    xlocal=-5
    while(xlocal<5):
        ye=f(xlocal,a)#y efthias
        y1ell=-np.sqrt(16-16*xlocal*xlocal*0.04)#y ellipsis katw apo to y=0
        y2ell=np.sqrt(16-16*xlocal*xlocal*0.04)#y ellipsis pano apo to y=0
        if(abs(ye-y1ell)<0.001):
            found+=1
        if(abs(ye-y2ell)<0.001):
            found+=1
        xlocal+=0.001
    return found




a=0.5
found=2
while((found!=0) and a<3):
    x,y=[],[]
    x0=-10
    for j in range(150):
        x.append(x0)
        y0=f(x0,a)
        y.append(y0)
        x0+=0.1
    found=check(a)
    #print(found,a)
    if (found==0):
        break
    a+=0.01
plt.plot(x,y)
'''

i methodos pou xrisimopoiisa itan na psaxno
tis efthies, metavallontas tin klisi etsi oste na perna
apo to (-8,-1) kai na psaxno poses fores vriskei simio stin ellipsi
epd omws den tha vrethei pote i timi isi me tis ellipsis psaxno me akrivia
0.00001, vgenontas apo to while i efthia den vriskei kanena simio,
dld exei vgei apo tin ellipsi
meta, psaxno tin elaxisti timi gia f(x)=yefthias-yellipisis=0
'''
L=a#L einai i klisi tis efthias
def func(xv,L):
    return f(xv,L)-np.sqrt(16-16*xv*xv*0.04)
#
a =-4 #to x<0 
b =-1
eps = 1E-5    # epithymiti akribeia tis lusis
#
newx=np.linspace(a,b,1000)
newy=func(newx,L)
mini=newy[0]
for i in range(1,1000):
    if newy[i]<mini:
        mini=newy[i]
        xm=newx[i]
#plt.plot(newx,newy)
print("x0=",xm)

print("y0=",(np.sqrt(16-16*xm*xm*0.04)))
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.savefig("lab12_ask03_plot.pdf")
plt.show()
exit()
