#Christodoulos Stylianides
#Askisi 2 kai 3
#!/bin/python3

import numpy as np
import urllib.request
file=urllib.request.urlopen("http://www2.ucy.ac.cy/~fotis/phy140/LAB06/mydata.txt")#me ton tropo tis dialeksis 9 perno to .txt

point_data=[]
time_data=[]
height_data=[]
uncert_data=[]#arxikopiw tis listes mou

for line in file:
    p,t,h,u=np.loadtxt(file,usecols=(0,1,2,3),unpack=True,skiprows=2)
    #perno tis times p t h u apo to file agnoontas tis protes 3 grammes (0,1,2) 
    point_data+=[(p)]#prostheto ws tuple tin kathe metavliti 
    time_data+=[(t)]#stin antistixi lista
    height_data+=[(h)]
    uncert_data+=[(u)]

point=np.array(point_data)#kathe list to kanw array
time=np.array(time_data)
height=np.array(height_data)
uncert=np.array(uncert_data)

print("Number of each measurement:",point)#tipono me minimata ta arrays mou
print("Time of each flight:",time)
print("Height of each falling mass",height)
print("Uncertainty in each measurement:", uncert)
file.close()#klino to file

#Askisi 3

file_towrite=open('mydatawritten.txt','w')
point=np.reshape(point,(13,1))#o logos pou to metatrepo se pinaka 13 grammon einai
time=np.reshape(time,(13,1))#epd den katafera na to dimiourgiso se zip file me ta lists pou exoun tuples
height=np.reshape(height,(13,1))
uncert=np.reshape(uncert,(13,1))
file_towrite.write("Data for falling mass experiment\nDate: 16-Sep-2020\nData taken by Andria and Marios\n\n")#den katafera na xrisimopiiso tin sinartisi header
file_towrite.write("\t\tdata point  time(sec)\t height (mm) uncertainty (mm)\n")
for i in range(13):
    file_towrite.write("\t{0:12.1f}\t{1:12.1f}\t{2:12.1f}\t{3:12.1f}\n".format(float(point[i]),float(time[i]),float(height[i]),float(uncert[i])))
    

exit()
#10/10