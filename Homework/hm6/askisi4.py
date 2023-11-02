#Christodoulos Stylianides Askisi4
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
def lineFit(x,y):
    xavg = x.mean()
    slope = (y * (x-xavg)).sum()/(x * (x-xavg)).sum()
    yint = y.mean() - slope * xavg
    return slope, yint

def LineFitWt(x,y,dy):
    dy2 = dy**2
    norm = (1./dy2).sum()
    xhat = (x/dy2).sum() / norm
    yhat = (y/dy2).sum() / norm
    slope = ((x-xhat)*y/dy2).sum()/((x-xhat)*x/dy2).sum()
    yint = yhat - slope*xhat
    dy2_slope = 1./((x-xhat)*x/dy2).sum()
    dy2_yint = dy2_slope * (x*x/dy2).sum()/norm
    return slope, yint, np.sqrt(dy2_slope), np.sqrt(dy2_yint)

file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/Homeworks/Data2Fit.dat")

x, y, dy = np.loadtxt(file, skiprows=2, unpack=True)

klisi1,yinters1,sigmaa,sigmab=LineFitWt(x,y,dy)

print("The error of the slope is ",sigmaa)
print("The error of the y intersect is",sigmab)

klisi2,yinters2=lineFit(x,y)
plt.errorbar(x,y, fmt='oC1', label='data',xerr=0, yerr=dy, ecolor='black')
xaks=np.linspace(0,25.0,10000)
yaks1=klisi1*xaks+yinters1
yaks2=klisi2*xaks+yinters2
plt.plot(xaks,yaks1,label='lineFitWt',color='g')
plt.plot(xaks,yaks2,label='lineFit',color='darkblue')
ax=plt.gca()
ax.set_xlim([-0.1,24.])
plt.axvline(x=0,color='k')
plt.axhline(y=0,color='k')

plt.legend()
plt.savefig("Askisi4.pdf")
#plt.show()
exit()
