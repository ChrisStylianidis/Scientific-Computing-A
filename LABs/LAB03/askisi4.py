#Askisi 4 Christodoulos Stylianides
#!/bin/python3

MyList=[12,15,55,60,73,75,80,122,130,150,180]

for i in range(11):
    if MyList[i]>150:
        break
    if MyList[i]%5==0:
        print(MyList[i])

exit()
