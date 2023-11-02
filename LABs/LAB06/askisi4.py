#Askisi 4
#Christodoulos Stylianides
#!/bin/python3

import numpy as np
datafile=open("datafile.txt")#to file afto exei mesa ta data apo tin ekfonisi tis askisis 4
f=[]
a=[]
da=[]
c=14

for line in datafile:
    freq,ampl,err=np.loadtxt(datafile,usecols=(0,1,2),unpack=True,skiprows=2)
    f+=[(freq)]
    a+=[(ampl)]
    da+=[(err)]
    
datafile.close()

f=np.array(f)
a=np.array(a)
da=np.array(da)
f=f.reshape((c,1))
a=a.reshape((c,1))
da=da.reshape((c,1))
filetowrite=open('lab06_prob04.txt','w')
filetowrite.write("Data: 2020 - 09 - 25\nData taken by Ioanna and Xristakis\n\tfrequency (Hz)  amplitute (mm)   amp error (mm)\n")
for i in range(c):
    filetowrite.write("\t{0:12.4f}\t{1:12.2f}\t{2:12.2f}\n".format(float(f[i]),float(a[i]),float(da[i])))
    print("\t{0:12.4f}\t{1:12.2f}\t{2:12.2f}".format(float(f[i]),float(a[i]),float(da[i])))

exit()
