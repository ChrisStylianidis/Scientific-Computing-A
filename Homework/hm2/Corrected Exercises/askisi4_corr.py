#Askisi4 Christodoulos Stylianides
#!/bin/python3

d=input("Give number:")
d=int(d)
number=d
digits=0
while d>0:#me afto to while vrisko arithmo psifiwn
    digits+=1
    d//=10
end=digits
ans=0

for i in range(end):
    n=number%10#kathe fora pernw to telefteo psifio
    poow=1
    if n==1:
        for j in range(i):#to function pow se for
            poow*=2
        ans+=poow
    number//=10#miwnno ton arithmo 

print(ans)
exit()
#10/10