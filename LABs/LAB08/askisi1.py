#Christodoulos Stylianides Askisi 1
#!/bin/python3
import numpy as np
import matplotlib.pyplot as plt

i=np.arange(0,5)
mynumbers=2*i-1

plt.figure()
#plt.subtitle("My first plot")
plt.subplot(121)
plt.plot(i,mynumbers,'k')#mavri efthia
plt.xlabel("xvalues")
plt.ylabel("yvalues")
plt.subplot(122)
plt.plot(i,mynumbers,'o',color='red')
plt.xlabel("xvalues")
plt.ylabel("yvalues")
plt.suptitle("Many Graphs")
plt.savefig("myFirstPlots.pdf")

plt.show()
exit()
