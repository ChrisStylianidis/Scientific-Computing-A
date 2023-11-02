#Christodoulos Stylianides askisi 6
#!/bin/python3
from random import random
import numpy as np
def point(x,ar):
    for i in range(ar):
        if x>=i and x<i+1:
            return i
'''
mporoun na dothei o arithmos gia tis portes
i akomi kai gia ton arithmo pexnidion pu tha ginei
'''

tries=10000
ar=3#number of doors in monty hall's problem
win=0
for i in range(tries):
    car=np.zeros(ar)
    x=ar*random()
    car[point(x,ar)]+=1#vazo to aftokinito se mia tixea thesi
    y=ar*random()
    car[point(y,ar)]+=1#vazo ton pexti na dialeksei
    #print(car)
    c=0#o pinakas mou einai gematos apo miden assous i 2
    for j in range(ar):#an iparxei arithmos tote den mporoume na to anniksoume
       if car[j]==0:
           c+=1
    if c==ar-1:#an to vrike apo tin proti tote kerdizei
        win+=1#+1 niki gia kathe fora pou to vriskei tin proti fora
#an allaksei pithanotita tha kerdisi(an to doro den einai stin arxiki epilogi)
playerstays=win/tries#i pithanotita na kerdisei an minei stin epilogi
playerchanges=1-playerstays#pithanotita na kerdisei an allaksei
print("If he doesnt change his choice:{:.2f}%".format(playerstays*100))
print("The chances if he switches:{:.2f}%".format(playerchanges*100))
exit()
