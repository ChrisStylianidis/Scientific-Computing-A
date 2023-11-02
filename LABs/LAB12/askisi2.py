#Christodoulos Stylianides askisi 2
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
x=[]
y1=[]
y2=[]
for i in range(25):
    xv = (i-1)*0.1
    x.append(xv)
    y1.append(4*np.exp(-2*xv))
    y2.append(0.5*xv*xv)
legd=['y1(x)=4e^(-2x)','$y2(x)=0.5x^2$']
comm=['r-','b-']
plt.plot(x,y1,comm[0],label=legd[0])
plt.plot(x,y2,comm[1],label=legd[1])


#
def func(xv):
    return 4*np.exp(-2*xv)-0.5*xv*xv
#
a =-10 #float(input("Give the low limit "))
b =10 #float(input("Give the upper limit "))
eps = 1E-5      # epithymiti akribeia tis lusis
#
fa = func(a)
fb = func(b)
#
if fa*fb > 0:
    print('The interval does not contain the solution',fa,fb)
    exit()
#
while (b-a) > eps:
    c = (a+b)/2.0
    fc = func(c)
    if fc == 0:
        exit()
    if fc * fa > 0:     
        a = c           
        fa = fc
    else:
        b = c          
        fc = fc         
        
#
yvalue=0.5*c*c#vazo to c dld x aksonas gia simio tomis se mia apo tis eksioseis
print('f(x={:.5f})={:.5f}'.format(c,yvalue))
ans=[c,yvalue]
np.savetxt("askisi2.dat",ans)
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')
plt.legend()
plt.savefig("askisi2.pdf")

exit()
