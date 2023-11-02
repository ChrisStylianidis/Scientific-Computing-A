#Christodoulos Stylianides askisi 5
#!/bin/python3
from random import random
times=10000000#times you throw the dice
c=0#counter how many times the number is 6
for i in range(times):
    if random()<1/6:
        c+=1
p=c/times
print(p)
exit()
