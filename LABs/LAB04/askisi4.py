#Askisi 4 Christodoulos Stylianides
#!/bin/python3

import numpy as np

Arr=np.zeros(5)
print("Give 5 numbers:")
for i in range(5):
    a=input()
    a=int(a)
    Arr[i]=a

Rev=np.zeros(len(Arr))
j=len(Arr)-1

for i in range(len(Arr)):
    Rev[i]=Arr[j]
    j-=1

print(Rev)
exit()

    
    
