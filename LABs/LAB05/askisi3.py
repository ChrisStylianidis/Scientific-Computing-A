#Christodoulos Stylianides
#Askisi 3 kai 4
#!/bin/python

def prpar(N):#protoi paragontes
    list=[]
    for i in range(2,N//2+1): #den xriazete na elegkso times panw apo tin mesi
        if N%i==0:          #tou arithmou kathos den mporoun na einai dieretes
            list+=[i]
    list+=[N]#simperilamvano to N
    return list
#Main program
a=int(input("Give a number:"))
print(prpar(a))



exit()
