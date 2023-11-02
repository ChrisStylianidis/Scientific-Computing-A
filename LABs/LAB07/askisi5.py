#Askisi 5 Christodoulos Stylianides
#o tropos epilisis tis askisis mou einai o eksis, arxika zitao ola ta simia toso tou orthogoniou oso kai tou simiou tou opiou psaxno
#elegxo to simio a me b to opio einai to pano aristera kai to pano deksia an to simio pou elegxo einai kato apo tin efthia afti
#meta apo to simio b c pali an einai kato apo tin efthia tous (to simio c einai to kato deksia)
#meta elegxo ta simia d c kai oxi c d giati to x tou simiou d einai mikrotero apo tou c ara an elegxa c d i klisi tha eixe lathos prosimo
#metaksi twn simiwn d c elegxo panw apo tin efthia kathos gia na anikei sto orthogonio prpei na einai panw apo tin efthia c d
#telos elegxo ta simia a d kai gia afta elegxo panw apo tin efthia pou dimiourgoun
#trexo to function tou elegxou tis efthias me mia metavliti pou onomasa case, i metavliti afti dilonei an tha elegxo panw i kato apo
#tin efthia pou tha dimiourgisoun ta 2 simia
#lastly, se periptosi pou i klisi einai apiro, diladi i efthia parallili me ton aksona y elegxo antistixa ortha me to case deksia kai aristera
#se kathe periptosi apo to x
#!/bin/python3
print()
print("Give your points in a clockwise rotation with the first being the farthest left")
print("Give values for point A:")
ax=float(input("X:"))
ay=float(input("Y:"))
print("Give values for point B:")
bx=float(input("X:"))
by=float(input("Y:"))
print("Give values for point C:")
cx=float(input("X:"))
cy=float(input("Y:"))
print("Give values for point D:")
dx=float(input("X:"))
dy=float(input("Y:"))
print("Give values for point to check:")
x=float(input("X:"))
y=float(input("Y:"))
if ax==dx:#se periptosi pou dothoun simia ta opia vriskontai stin idia efthia x=ax=dx
    tempx=dx#gia na trexei ortha to programma prepei na allaksoun oi onomasies tou kathe
    tempy=dy#simiou.
    dx=cx
    dy=cy
    cx=bx
    cy=by
    bx=ax
    by=ay
    ax=tempx
    ay=tempy 
def equation(x1,y1,x2,y2,x,y,case):
    if x1!=x2:
        m= (y2-y1)/(x2-x1)
        if (y<(x-x1)*m+y1)and(case==1):#case 1 psaxnei kato apo tin
            return 1                   #efthia
        if(y>(x-x1)*m+y1)and(case==2):#case 2 psaxnei panw
            return 1
    if x1==x2:#se periptosi pou i efthia exei apiri klisi
        if (x>x1)and(case==1):#elegxo deksia 
            return 1
        if (x<x1) and (case==2):#elegxo aristera
            return 1
    return 0
d=0
d+=equation(ax,ay,bx,by,x,y,1)
d+=equation(bx,by,cx,cy,x,y,1)
d+=equation(dx,dy,cx,cy,x,y,2)
d+=equation(ax,ay,dx,dy,x,y,2)
if(d==4):#an kai oi 4 efthies einai orthes tote to simio einai metaksi ton oriwn
    print("You are in! Coordinates:",x,y)
else:
    print("You are outside the rectangle shape!")
exit()
