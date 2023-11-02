#Askisi 7 Christodoulos Stylianides
#!/bin/python3

a=input("Give A:")
a=int(a)
b=input("Give B:")
b=int(b)

for i in range(a,b+1):# simperilamvano to a kai b
    c=0#counter pou mou dixnei tous dieretes tou i extos to 1 kai to i
    for j in range(2,i):
        if i%j==0:
            c+=1
    if c==0:
        print(i,' is a prime')

exit()
