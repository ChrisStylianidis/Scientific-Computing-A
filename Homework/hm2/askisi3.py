#Askisi 3 Christodoulos Stylianides
#!/bin/python3

a=input("Give number:")
a=float(a)

c=-1#ksekiname apo dekadika
ans2=0.0
boool=0
de=a-int(a)
while (de-int(de))!=0:
    boool=1#vazo mia metavliti bool gia to if amesos meta to while
    de*=2
    if de>1.0:
        de=de-int(de)
        ans2+=(10**c)
    c-=1
if boool==1:#tha mpei sto if MONO an mpike esto kai mia fora sto while.
    c+=1#tis dio aftes entoles tis xriazomai giati, 
    ans2+=(10**c)# vgenontas apo to while prpei oi entoles na epanalifthoun.
#o logos pou prostheto +1 sto c einai gia tin thesi tou psifiou ston arithmo.

a//=1# fevgo ta dekadika
ans1=0
d=0#d einai i thesi tou psifiou
while a>0:
    if a%2==1:
        ans1+=(10**d)   
    a//=2
    d+=1
ans=ans1+ans2
print(ans)
exit()
