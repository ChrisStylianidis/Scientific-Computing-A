#Askisi 5 Christodoulos Stylianides
#!/bin/python3

value=input("Give the number:")
a=int(value)
psifia=0
while(a>0):
    psifia+=1
    a//=10

print(psifia)

exit()
