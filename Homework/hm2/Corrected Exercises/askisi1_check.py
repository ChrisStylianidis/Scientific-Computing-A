#Askisi 1 Christodoulos Stylianides
#!/bin/python3

ans=1
for i in range(1,11):
    ans*=i#vgenontas apo to for to ans einai to 10!

for i in range(10,0,-1):
    print(i,'! is',ans)
    ans//=i

exit()

## grade : 10/10
