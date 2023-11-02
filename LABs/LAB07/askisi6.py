#Askisi 6 Christodoulos Stylianides
#!/bin/python3
import numpy as np
import urllib.request
myfile=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/LAB07/orbit.csv")
def tipikiapoklisi(x,xm,N):#to function tis tipikisapoklisis
    sum=0
    x=np.array(x)
    for i in range(N):
        sum+=((x[i]-xm)**2)
    c=np.sqrt(sum/N)
    return c
N=0#to plithos ton stixiwn sto file
for line in myfile:
    N+=1
    time,posx,posy,posz=np.loadtxt(myfile,delimiter=',',unpack=True)
t=time.mean()#mesos oros tou kathe array antistixa
x=posx.mean()
y=posy.mean()
z=posz.mean()

tta=tipikiapoklisi(time,t,N)#orizo metavlites TimeTipikiApoklisi
xta=tipikiapoklisi(posx,x,N)#posXTipikiApoklisi
yta=tipikiapoklisi(posy,y,N)#posYTipikiApoklisi
zta=tipikiapoklisi(posz,z,N)
final_list=[tta,xta,yta,zta]#ta vazo se lista
final_list=np.array(final_list)#tin kano array gia to for meta

my_file=open('storedata.dat','w')#anigo to file sto opio tha grapso
my_file.write("Standard deviation for\ntime:\t\tposx:\t\tposy:\t\tposz:\n")
for i in range(4):
    my_file.write("{0:.10f}\t".format(final_list[i]))#grafo ta aparetita stixia
my_file.write("\nMean for\ntime:\t\t\t posx:\t\t  posy:\t\t posz:\n")
my_file.write("{0:10.8f}\t {1:10.8f}\t {2:10.8}\t {3:10.8}\n".format(t,x,y,z))

myfile.close()#web file
my_file.close()#to file sto opio egrapsa ta data
exit()
