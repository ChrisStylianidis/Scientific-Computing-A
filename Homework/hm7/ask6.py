#Christodoulos Stylianides Askisi 6

#!/bin/python3
from random import random,seed
import numpy as np
seed(3141592653)

M=int(input("How many balls do you want to take each time?"))

while(M<=1 or M>=100):
    M=int(input("Please insert a valid number for balls (1<M<100)"))


ntries=int(input("How many attempts each time?"))
box=np.ones(101)#to kouti mou exei mesa 101 mpales tin proti tha tin agnoo
p=0#pithanotita
for j in range(ntries):
    box=np.ones(101)#kathe fora vazo oles tis mpales mesa
    sum=0
    for i in range(M):
        x=int(1+random()*100)#to x einai apo to 1 mexri to 100 
                              #(den einai pote 101)
        while(box[x]==0):
            x=int(1+random()*100)#an tixei kai parei ena arithmo pou idi iparxei
                           #vgennontas apo to while afto tha exei mia 
                            #mpala pou den vgike
        box[x]=0#vgazo tin mpala
        sum+=x#prostheto tin mpala
    if(sum>500):
        p+=1
print("The possibility of the sum of {0:d} Balls to be more than 500 is: {1:0.4f}".format(M,p/ntries))

exit()
