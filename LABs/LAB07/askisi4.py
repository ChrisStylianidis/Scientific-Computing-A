#Askisi 4 Christodoulos Stylianides
#!/bin/python3
import numpy as np
myfile=open("test.txt")
temp=[]
for line in myfile:
    x=line#to x mou einai to string tis grammis
    y=""#arxikopio to y ws adio string
    for j in range(5):
        y+=x[j]#perno tus protous 5 xaraktires tou x xoris to \n sto telos
    temp+=[(str(y))]#ta vazo se list
myfile.close()
data=np.array(temp)# kanw to list array
file_to_write=open('newtest.txt','w')
i=0
while i<7:
    if i==4:#otan ftasei sto data5 dld gia i==4
        i+=1#afou i arithmisi ksekina apo to 0
    file_to_write.write("{}\n".format(data[i]))
    i+=1
exit()
