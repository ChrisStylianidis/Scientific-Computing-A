#Christodoulos Stylianides Askisi 1
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
dx=0.05#step
n=500#akrivia se np.linspace
x=0#x aksonas per one value
xa=[]#x aksonas gia list (xrisi se graph)
y=0#ipologizo y
yt=0
y1=[]#y aksonas gia list(xrisi se graph)
plt.figure()
plt.xlabel("x Values")
plt.ylabel("y Values")
plt.title(" $ \frac{dy}{dx} = y^2+1 $")
for i in range(4):
    while(x<1):
        xa.append(x)
        y1.append(y)
        yt=(y**2)+1
        y+=yt*dx
        x+=dx
    plt.plot(xa,y1,'--')
    y1=[]
    xa=[]
    dx+=0.05
    x=0
    y=0
xa=np.linspace(0,1,n)
y=np.tan(xa)
plt.plot(xa,y,'k')
plt.savefig("lab09_prob1.pdf")
plt.show()
exit()
