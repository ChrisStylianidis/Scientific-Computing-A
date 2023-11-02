#Askisi 5
#Christodoulos Stylianides
#!/bin/python3
import numpy as np
m=""#month
d=""#day
y=""#year
print("Give date in this order:\n(first letter of the month must be capital)\nMonth day, year")
Date=input("Date:")
def months_to_numbers(month):#apo string se arithmous minwn
    switcher={
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June": 6,
        "July": 7,
        "August": 8,
        "September": 9,
        "October": 10,
        "November": 11,
        "December": 12,}
    return switcher.get(month, "Month doesnt exist in database")

for i in range(len(Date)):
    if(Date[i]!=' '):
        m+=Date[i]#pernw to string tou mina kai den to kanw int
#afou to thelw os string gia to switch
    if(Date[i]==' '):#stamatao otan vro keno
        c=i#kratao tin thesi tou kenou
        break#molis vro to keno tha vgo apo to for
c+=1#skip to keno
for i in range(c,len(Date)):#idio process stamato sto ','
    if(Date[i]!=','):
        d+=Date[i]
    if(Date[i]==','):
        c=i
        break
c+=2#kanw skip kai to koma kai to keno dld tous epomenous 2 characters
for i in range(c,len(Date)):
    y+=Date[i]
d=int(d)#apo string se int
y=int(y)

def days_to_sum(num):
    switcher={
        1: (0),
        2: (31),
        3: (31+28),
        4: (31+28+31),
        5: (31+28+31+30),#sto switch afto vrisko to sinolo twn meron
        6: (31+28+31+30+31),# ton proigoumenon minwn
        7: (31+28+31+30+31+30),# kathos meta tha prostheso tis meres
        8: (31+28+31+30+31+30+31),# tou mina pou dinei o xristis
        9: (31+28+31+30+31+30+31+31),
        10:(31+28+31+30+31+30+31+31+30),
        11:(31+28+31+30+31+30+31+31+30+31),
        12:(31+28+31+30+31+30+31+31+30+31+30),}
    return switcher.get(num,"")
nm=months_to_numbers(m)#number of month
days=0#arxikopiisi
days+=d+days_to_sum(months_to_numbers(m))#prostheto oles tis meres 
#tou xronou pou dilonei o xristis mono
last=1900
for i in range(1900,y):#vrisko ola ta leap years
    if i%4==0:         #gia na prostheso tis leap days
        if (i%100==0 and i%400==0)or(i%100!=0 and i%400!=0):
            days+=1
if nm>2 and y%4==0:
    if (y%100==0 and y%400==0)or(y%100!=0 and y%400!=0):
        days+=1#in case pou o xronos einai leap year meta ton marti
#se periptosi pou dothei leap day den epireazete afou tha prostethei sto days to 29 pou einai oi meres tou febrari pou dothikan ws d
days+=((y-1900)*365)#prostheto tis ipolipes xronies
days%=7#to ipolipo tou 7 gia na vro tin mera afou kserw oti
# i deftera(proti mera) einai days%7=1 ara triti=2 ktlp me sunday=0

def num_to_days(weekday):#switch gia na allakso to ipolipo tis dieresis
    switcher={# tou 7 me tin onomasia tis meras
        0:"Sunday",
        1:"Monday",
        2:"Tuesday",
        3:"Wednesday",
        4:"Thursday",
        5:"Friday",
        6:"Saturday",}
    return switcher.get(weekday,"Sorry something went wrong")
                                #unnecessary message epidi to days
                                #pernei pleon mono times [0-6]
print(num_to_days(days))
exit()
#kapws mperdeftiko to input s alla okay
#dokimasa 10/11/97 k einai deutera... esena vgazei savvato alla anyway
#10/10
