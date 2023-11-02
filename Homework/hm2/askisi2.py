#Askisi2 Christodoulos Stylianides
#!/bin/python3

e=1

for i in range(1,11):
    fac=1#arxikopio to factorial epd meta tha pernei tipes 10!*9! ktlp
    for j in range(i,0,-1):
        fac*=j
    e+=(1/fac)
print(e)
exit()
