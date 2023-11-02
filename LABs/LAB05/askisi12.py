#Christodoulos Stylianides
#!/bin/python3

import numpy as np

x=np.arange(10,51,5)
y=2*x-15
myfile=open('pinakes.csv','w')    
myfile.write("\tx:---\ty:---\n") 
print("\tx:---\ty:--- \n")
for i in range(9):
    print("\t{0:6.3f}\t{1:6.3f} \n".format(x[i],y[i]))
    myfile.write("\t{0:6.3f}\t{1:6.3f} \n".format(x[i],y[i]))
np.savetxt("x_values.dat",x)
np.savetxt("y_values.dat",y)

myfile.close()

exit()
